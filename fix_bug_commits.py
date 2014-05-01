__author__ = 'kevin'

from datetime import datetime
from subprocess import call, check_output
import sys
import os
import csv
import copy

import tag_lists

class GitTag():
    """Represents a Tag in a git repository"""

    def __init__(self, line):
        raw_tag, raw_hash, raw_date, raw_timestamp = line.split("|")

        # process the hash:
        self.tag_hash = raw_hash.strip()

        # process the timestamp
        self.tag_timestamp = float(raw_timestamp.strip())

        # process the datetime
        self.date = raw_date.strip()

        raw_tag = raw_tag.split("tag:")[1]
        # get the git-tag
        if "," in raw_tag:
            self.name = raw_tag.split(",")[0].strip()
        else:
            self.name = raw_tag.replace(")", "").strip()

    def date_to_string(self, time):
        """Returns: A string representation of a UNIX timestamp"""
        return str(datetime.fromtimestamp(time))

    def __str__(self):
        return str({'name': self.name, 'date': self.date})


class GitRepository():

    git_folder = ".git/"

    def __init__(self, repo_path):
        """Constructor for GitRepository"""
        self.repo_path = repo_path

    def get_tags(self):
        """Returns: List of all the tags in the repository"""

        cmd_get_tags = 'cd {0}; git log --tags --simplify-by-decoration --pretty="format:%d | %H | %ai | %at" |grep "tag:"'.format(self.repo_path)
        results_cmd = check_output(cmd_get_tags, shell=True).decode("utf-8")

        tags = [GitTag(str(line)) for line in results_cmd.splitlines()]

        # tags.sort(key=lambda t: t.date)



        return tags


def distinct(l, field_selector=None):
    # order preserving
    if field_selector is None:
        def field_selector(x):
            return x

    seen = {}
    result = []

    for item in l:
        comparison_field = field_selector(item)

        if comparison_field in seen:
            continue
        else:
            seen[comparison_field] = True
            result.append(item)

    return result


def get_interesting_releases(git_repo):

    ordered_tags = []

    if 'apache-avro' in git_repo:
        ordered_tags = tag_lists.apache_avro_releases
    elif 'apache-mahout' in git_repo:
        ordered_tags = tag_lists.apache_mahout_releases
    elif 'apache-tika' in git_repo:
        ordered_tags = tag_lists.apache_tika_releases
    elif 'vrapper' in git_repo:
        ordered_tags = tag_lists.vrapper_releases
    elif 'apache-zookeeper' in git_repo:
        ordered_tags = tag_lists.apache_zookeeper_releases
    elif 'facebook-android-sdk' in git_repo:
        ordered_tags = tag_lists.facebook_android_sdk_releases
    elif 'github-android-app' in git_repo:
        ordered_tags = tag_lists.github_android_app_releases
    elif 'wordpress-android' in git_repo:
        ordered_tags = tag_lists.wordpress_android_app

    return ordered_tags


def sort_tags(git_repo, tags):

    result = []
    ordered_tags = get_interesting_releases(git_repo)

    # tags_copy = copy.deepcopy(tags)

    # for i, tag in enumerate(ordered_tags):
    for tag in ordered_tags:
        # tags[i] = [t for t in tags_copy if t.name == tag][0]
        result.append([t for t in tags if t.name == tag][0])

    # del tags[len(ordered_tags):]
    return result


def handle_negative(value, actual_version, past_version):
    # return value

    if value < 0:
        if actual_version['loc'] == past_version['loc']:
            return 0
        else:
            return int(actual_version['commit_num'])
    else:
        return value

csv_header = ['file_name', 'release', 'is_sac', 'loc', 'commit_num', 'bug_commit_num', 'bug_commit_ratio']


def main():
    git_repo = sys.argv[1]
    stats_file = sys.argv[2]
    output_file = sys.argv[3]

    repo = GitRepository(git_repo)
    tags = sort_tags(git_repo, repo.get_tags())

    with open(stats_file, "r") as stats_file:
        # 'file_name', 'release', 'is_sac', 'loc', 'commit_num', 'bug_commit_num', 'bug_commit_ratio'
        stats = [row for row in csv.DictReader(stats_file) if row['release'] in get_interesting_releases(git_repo)]

    unique_files = distinct(stats, field_selector=lambda f: f['file_name'])

    for file in unique_files:
        # print("Processing file: " + file['file_name'])

        file_versions = [f for f in stats if f['file_name'] == file['file_name']]
        file_tags = [t for t in tags if t.name in [f['release'] for f in file_versions]]
        # file_tags.sort(key=lambda t: t.date)
        # file_tags = file_tags[::-1]

        fixed_values = {}

        for i, tag in enumerate(file_tags):

            # print("Processing tag: " + tag.name)

            if i + 1 < len(file_tags):
                # if not tag.date == file_tags[i + 1].date:
                actual_version = [f for f in file_versions if f['release'] == tag.name][0]
                past_version = [f for f in file_versions if f['release'] == file_tags[i + 1].name][0]

                commit_num = handle_negative(int(actual_version['commit_num']) - int(past_version['commit_num']),
                                             actual_version,
                                             past_version)

                bug_commit_num = handle_negative(int(actual_version['bug_commit_num']) - int(past_version['bug_commit_num']),
                                                 actual_version,
                                                 past_version)

                bug_commit_ratio = (bug_commit_num / commit_num) if commit_num != 0 else 0

                fixed_values[tag.name] = {'commit_num': commit_num,
                                          'bug_commit_num': bug_commit_num,
                                          'bug_commit_ratio': bug_commit_ratio}

        for tag, data in fixed_values.items():
            actual_version = [f for f in file_versions if f['release'] == tag][0]

            actual_version['commit_num'] = data['commit_num']
            actual_version['bug_commit_num'] = data['bug_commit_num']
            actual_version['bug_commit_ratio'] = data['bug_commit_ratio']

    with open(output_file, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, csv_header)
        writer.writeheader()
        writer.writerows(stats)


if __name__ == "__main__":
    main()