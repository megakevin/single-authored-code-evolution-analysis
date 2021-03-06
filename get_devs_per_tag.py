# Usage: $ python3 get_bug_commit_ratio_per_tag.py /home/kevin/Desktop/evolution-project/repos/facebook-android-sdk ./output/
# Calculates each files overall (not per tag) changes and bug related changes.

__author__ = 'kevin'

from datetime import datetime, timedelta
from subprocess import call, check_output
import sys
import os
import tag_lists
import csv


class GitTag():
    """Represents a Tag in a git repository"""

    def __init__(self, line):
        raw_tag, raw_hash, raw_date, raw_timestamp = line.split("|")

        # process the hash:
        self.tag_hash = raw_hash.strip()

        # process the timestamp
        self.tag_timestamp = float(raw_timestamp.strip())

        # process the datetime
        self.date = datetime.fromtimestamp(float(raw_timestamp.strip()))

        self.date_as_str = raw_date

        raw_tag = raw_tag.split("tag:")[1]
        # get the git-tag
        if "," in raw_tag:
            self.name = raw_tag.split(",")[0].strip()
        else:
            self.name = raw_tag.replace(")", "").strip()

    def __str__(self):
        return str({'name': self.name, 'date': str(self.date)})


class GitCommit():
    """Represents a commit in a git repository"""

    bug_related_words = ["bug", "fix", "defect", "broken", "crash", "freeze", "break", "wrong", "glitch", "proper"]
    line_separator = "<commit_data_separator>"
    entry_separator = "<commit_entry_separator>"

    @staticmethod
    def get_commits_command(git_repo):
        get_commits_command = 'cd {0}; git log --pretty="format:' \
                              '%H<commit_data_separator>' \
                              '%an<commit_data_separator>' \
                              '%ai<commit_data_separator>' \
                              '%at<commit_data_separator>' \
                              '%b<commit_entry_separator>"'.format(git_repo)

        return get_commits_command

    def __init__(self, line, repo):
        raw_hash, raw_author, raw_date, raw_timestamp, raw_body = line.split(GitCommit.line_separator)

        self.hash = raw_hash.strip()
        self.author = raw_author.strip()
        self.date = datetime.fromtimestamp(float(raw_timestamp))
        self.timestamp = float(raw_timestamp)
        self.date_as_str = raw_date
        self.message = raw_body

        self.repo = repo

    def get_touched_files(self):
        # This git command returns:
        # "\n
        # <added_lines>\t<deleted_lines>\t<file_name>\n
        # <added_lines>\t<deleted_lines>\t<file_name>"
        cmd_show_numstat = "cd {0}; git show --numstat --format='format:' {1}".format(self.repo.repo_path, self.hash)
        commit_stats = check_output(cmd_show_numstat, shell=True).decode("utf-8")

        touched_files = []

        for file_stats in commit_stats.split("\n"):
            if len(file_stats.split("\t")) == 3:  # Process only if it's a line with actual data
                added_lines, deleted_lines, file_name = file_stats.split("\t")
                touched_files.append(file_name)

        return touched_files

    def is_bug_related(self):
        return any([word.upper() in self.message.upper() for word in GitCommit.bug_related_words])

    def __str__(self):
        return str({'hash': self.hash, 'date': str(self.date)})


class GitRepository():

    git_folder = ".git/"

    def __init__(self, repo_path):
        """Constructor for GitRepository"""
        self.repo_path = repo_path

    def get_tags(self):
        """Returns: List of all the tags in the repository"""

        cmd_get_tags = 'cd {0}; git log --tags --simplify-by-decoration --pretty="format:%d | %H | %ai | %at" |grep "tag:"'.format(self.repo_path)
        results = check_output(cmd_get_tags, shell=True).decode("utf-8")

        tags = [GitTag(str(line)) for line in results.splitlines()]
        tags = [t for t in tags if t.name in self.get_interesting_releases()]

        tags.sort(key=lambda t: t.date)

        return tags

    def get_commits(self):
        """Returns: List of all the commits in the repository"""

        cmd_get_commits = GitCommit.get_commits_command(self.repo_path)
        results = check_output(cmd_get_commits, shell=True).decode("utf-8")

        commits = [GitCommit(str(line), self) for line in results.split(GitCommit.entry_separator) if line]
        commits.sort(key=lambda t: t.date)

        return commits

    def sort_tags(self, tags):
        result = []
        ordered_tags = self.get_interesting_releases()

        for tag in ordered_tags:
            result.append([t for t in tags if t.name == tag][0])

        return result
    
    def get_interesting_releases(self):
        ordered_tags = []
    
        if 'apache-avro' in self.repo_path:
            ordered_tags = tag_lists.apache_avro_releases
        elif 'apache-mahout' in self.repo_path:
            ordered_tags = tag_lists.apache_mahout_releases
        elif 'apache-tika' in self.repo_path:
            ordered_tags = tag_lists.apache_tika_releases
        elif 'vrapper' in self.repo_path:
            ordered_tags = tag_lists.vrapper_releases
        elif 'apache-zookeeper' in self.repo_path:
            ordered_tags = tag_lists.apache_zookeeper_releases
        elif 'facebook-android-sdk' in self.repo_path:
            ordered_tags = tag_lists.facebook_android_sdk_releases
        elif 'github-android-app' in self.repo_path:
            ordered_tags = tag_lists.github_android_app_releases
        elif 'wordpress-android' in self.repo_path:
            ordered_tags = tag_lists.wordpress_android_app
    
        return ordered_tags


def reverse(l):
    return l[::-1]


def first_or_default(l, default=None):
    if l:
        return l[0]
    else:
        return default


csv_header = ['release', 'authors', 'num_authors']


def main(args):
    git_repo = args[1]
    output_file = args[2]

    repo = GitRepository(git_repo)
    commits = repo.get_commits()
    tags = repo.get_tags()

    result = []
    initial_date = None

    for tag in tags:

        authors = {}
        final_date = tag.date

        if initial_date:
            commits_in_tag = [c for c in commits if initial_date < c.date <= final_date]
        else:
            commits_in_tag = [c for c in commits if c.date <= final_date]

        initial_date = final_date

        # commits_in_tag = commits

        for commit in commits_in_tag:
            if commit.author in authors:
                authors[commit.author] += 1
            else:
                authors[commit.author] = 1

        result.append({'release': tag.name,
                       'authors': ':'.join(authors),
                       'num_authors': len(authors)})

    with open(output_file, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, csv_header)
        writer.writeheader()
        writer.writerows(result)


if __name__ == '__main__':
    main(sys.argv)
