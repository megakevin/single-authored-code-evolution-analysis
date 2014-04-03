#Usage: $ python3 get_contrib_per_tag.py /home/kevin/Desktop/facebook-android-sdk

# Runs Git By A Bus on every tag of the specified repository
# and extracts the file-level contribution information using
# the get_top_contrib_per_file script.


__author__ = 'kevin'

from datetime import datetime
from subprocess import call
from shutil import copytree
import math
import sys
import os
import pygit2
from multiprocessing import Process


class GitObjectType():
    """Defines Git object types in terms of pygiy2's GIT_OBJs"""

    commit = pygit2.GIT_OBJ_COMMIT
    tag = pygit2.GIT_OBJ_TAG


class GitTag():
    """Represents a Tag in a git repository"""

    def __init__(self, name, time):
        """Constructor for Tag"""
        self.name = name
        self.date = self.date_to_string(time)

    def date_to_string(self, time):
        """Returns: A string representation of a UNIX timestamp"""
        return str(datetime.fromtimestamp(time))

    def __str__(self):
        return str({'name': self.name, 'date': self.date})


class GitRepository():
    """Wraps around the pygit2's Repository class"""

    git_folder = ".git/"

    def __init__(self, repo_path):
        """Constructor for GitRepository"""
        repo_path = os.path.join(repo_path, GitRepository.git_folder)
        self.repo = pygit2.Repository(repo_path)

    def get_tags(self):
        """Returns: List of all the tags in the repository"""

        tags = [GitTag(self.repo[obj_hex].name,
                       self.repo[obj_hex].get_object().commit_time)
                for obj_hex in self.repo if self.repo[obj_hex].type == GitObjectType.tag]

        tags.sort(key=lambda t: t.date)

        return tags


git_by_a_bus_executable = "/home/kevin/Desktop/git_by_a_bus/git_by_a_bus.py"
get_top_contrib_per_file_file_name = "get_top_contrib_per_file.py"
estimate_unique_knowledge_file_name = "estimate_unique_knowledge.tsv"
degree_of_parallelism = 4


def split(list, chunk_size):
    return [list[i:i + chunk_size] for i in range(0, len(list), chunk_size)]


def extract_contribution_data(git_repo, tags):
    exec_dir = os.getcwd()

    for tag in tags:
        os.chdir(git_repo)
        call(["git", "checkout", "tags/" + tag.name])

        os.chdir(exec_dir)
        call(["python", git_by_a_bus_executable, "-o", "gbab_output_" + tag.name, git_repo])

        call(["python3",
              get_top_contrib_per_file_file_name,
              os.path.join("gbab_output_" + tag.name, estimate_unique_knowledge_file_name),
              "contribs",
              "contrib_" + tag.name + ".csv"])

        print("tags/" + tag.name + " processed")

    os.chdir(exec_dir)
    call(["git", "checkout", "master"])


def main(git_repo):

    repo = GitRepository(git_repo)
    tags = repo.get_tags()

    repo_copies = [git_repo[:-1] + "-" + str(i) + "/" for i in range(degree_of_parallelism)]
    tag_groups = split(tags, math.ceil(len(tags)/degree_of_parallelism))

    for repo_copy in repo_copies:
        copytree(git_repo, repo_copy, symlinks=True)

    for repo_copy, tags in zip(repo_copies, tag_groups):
        p = Process(target=extract_contribution_data, args=(repo_copy, tags))
        p.start()

    print("lol")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("USAGE {0} <repository_root>".format(__file__))
        sys.exit(1)

    main(sys.argv[1])
    # main("/home/kevin/Desktop/facebook-android-sdk/")