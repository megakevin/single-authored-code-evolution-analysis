#Usage: $ python3 get_contrib_per_tag.py /home/kevin/Desktop/facebook-android-sdk

# Runs Git By A Bus on every tag of the specified repository
# and extracts the file-level contribution information using
# the get_top_contrib_per_file script.


__author__ = 'kevin'

from datetime import datetime
from subprocess import call
import sys
import os
import pygit2


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


class OSCommandDispatcher():
    """Encapsulates os calls"""

    def __init__(self):
        """Constructor for CommandDispatcher"""
        self.exec_dir = os.getcwd()

    def chdir(self, dir):
        os.chdir(dir)

    def go_back_to_exec_dir(self):
        self.chdir(self.exec_dir)

    def call(self, command):
        call(command)

    def join_path(self, path, file):
        return os.path.join(path, file)


git_by_a_bus_executable = "/home/kevin/Desktop/git_by_a_bus/git_by_a_bus.py"
get_top_contrib_per_file_file_name = "get_top_contrib_per_file.py"
estimate_unique_knowledge_file_name = "estimate_unique_knowledge.tsv"


def main(git_repo):
    repo = GitRepository(git_repo)
    tags = repo.get_tags()

    os_command = OSCommandDispatcher()

    for tag in tags:
        os_command.chdir(git_repo)
        os_command.call(["git", "checkout", "tags/" + tag.name])

        os_command.go_back_to_exec_dir()
        os_command.call(["python", git_by_a_bus_executable, "-o", "gbab_output_" + tag.name, git_repo])

        os_command.call(["python3",
                         get_top_contrib_per_file_file_name,
                         os.path.join("gbab_output_" + tag.name, estimate_unique_knowledge_file_name),
                         "contribs",
                         "contrib_" + tag.name + ".csv"])

    os_command.chdir(git_repo)
    os_command.call(["git", "checkout", "master"])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("USAGE {0} <repository_root>".format(__file__))
        sys.exit(1)

    main(sys.argv[1])
    # main("/home/kevin/Desktop/facebook-android-sdk/")