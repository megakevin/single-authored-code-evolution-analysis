# Usage: $ python3 get_bug_commit_ratio_per_tag.py /home/kevin/Desktop/evolution-project/repos/facebook-android-sdk ./output/

# Runs Git By A Bus on every tag of the specified repository
# and extracts the file-level contribution information using
# the get_top_contrib_per_file script.


__author__ = 'kevin'

from datetime import datetime
from subprocess import call, check_output
import sys
import os

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

        tags.sort(key=lambda t: t.date)

        return tags


get_bug_commit_per_file_executable = "get_bug_commit_ratio_per_file.py"
default_bug_commit_output_dir = "/home/kevin/Desktop/evolution-project/"


def extract_bug_commit_data(git_repo, tags, output_dir):
    exec_dir = os.getcwd()

    for tag in tags:
        os.chdir(git_repo)
        call(["git", "checkout", "tags/" + tag.name])

        os.chdir(exec_dir)
        call(["python3",
              get_bug_commit_per_file_executable,
              git_repo,
              os.path.join(output_dir, "bug-commit-" + tag.name + ".csv")])

        print("tags/" + tag.name + " processed")

    os.chdir(git_repo)
    call(["git", "checkout", "master"])


def main(git_repo, output_dir):

    repo = GitRepository(git_repo)
    tags = repo.get_tags()

    try:
        os.makedirs(output_dir)
    except FileExistsError as ex:
        pass

    # Use this to run process in a single thread.
    extract_bug_commit_data(git_repo, tags, output_dir)


if __name__ == '__main__':
    repo_path = sys.argv[1]

    output_dir = default_bug_commit_output_dir
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]

    main(repo_path, output_dir)
    # main("/home/kevin/Desktop/facebook-android-sdk/")