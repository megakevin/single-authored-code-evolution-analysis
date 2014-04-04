#Usage: $ python3 get_contrib_per_tag.py /home/kevin/Desktop/facebook-android-sdk

# Runs Git By A Bus on every tag of the specified repository
# and extracts the file-level contribution information using
# the get_top_contrib_per_file script.


__author__ = 'kevin'

from datetime import datetime
from subprocess import call, check_output
from shutil import copytree, rmtree
import math
import sys
import os
from multiprocessing import Process

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


git_by_a_bus_executable = "/home/kevin/Desktop/git_by_a_bus/git_by_a_bus.py"
get_top_contrib_per_file_executable = "get_top_contrib_per_file.py"
estimate_unique_knowledge_file_name = "estimate_unique_knowledge.tsv"
contributions_output_dir = "/home/kevin/Desktop/contrib-output/"
degree_of_parallelism = 4


def split(list, chunk_size):
    return [list[i:i + chunk_size] for i in range(0, len(list), chunk_size)]


def extract_contribution_data(git_repo, tags):
    exec_dir = os.getcwd()

    for tag in tags:
        os.chdir(git_repo)

        call(["git", "checkout", "tags/" + tag.name])

        os.chdir(exec_dir)

        call(["python",
              git_by_a_bus_executable,
              "-o", os.path.join(contributions_output_dir, "gbab_output_" + tag.name),
              git_repo])

        call(["python3",
              get_top_contrib_per_file_executable,
              os.path.join(contributions_output_dir,
                           "gbab_output_" + tag.name,
                           estimate_unique_knowledge_file_name),
              contributions_output_dir,
              "contrib_" + tag.name + ".csv"])

        rmtree(os.path.join(contributions_output_dir, "gbab_output_" + tag.name))

        print("tags/" + tag.name + " processed")

    os.chdir(git_repo)
    call(["git", "checkout", "master"])


def main(git_repo):

    repo = GitRepository(git_repo)
    tags = repo.get_tags()

    # Use this to run process in a single thread.
    # extract_contribution_data(git_repo, tags)

    # Use this to run process in parallel
    repo_copies = [git_repo[:-1] + "-" + str(i) + "/" for i in range(degree_of_parallelism)]
    tag_groups = split(tags, math.ceil(len(tags)/degree_of_parallelism))

    for repo_copy in repo_copies:
        copytree(git_repo, repo_copy, symlinks=True)

    for repo_copy, tags in zip(repo_copies, tag_groups):
        p = Process(target=extract_contribution_data, args=(repo_copy, tags))
        p.start()
    #
    # for repo_copy in repo_copies:
    #     rmtree(repo_copy)

    print("lol")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("USAGE {0} <repository_root>".format(__file__))
        sys.exit(1)

    main(sys.argv[1])
    # main("/home/kevin/Desktop/facebook-android-sdk/")