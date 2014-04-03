#Usage: $ python3 get_contrib_per_tag.py /home/kevin/Desktop/facebook-android-sdk

# Runs Git By A Bus on every tag of the specified repository
# and extracts the file-level contribution information using
# the get_top_contrib_per_file script.


__author__ = 'kevin'

from datetime import datetime
from subprocess import call
import json
import os
import pygit2

git_folder = ".git/"
git_by_a_bus_executable = "/home/kevin/Desktop/git_by_a_bus/git_by_a_bus.py"


class GitObjectType():
    """Defines Git object types in terms of pygiy2's GIT_OBJs"""

    commit = pygit2.GIT_OBJ_COMMIT
    tag = pygit2.GIT_OBJ_TAG

class Tag():
    """Represents a Tag in a git repository"""

    def __init__(self, args):
        """Constructor for Tag"""


class GitRepository():
    """Wraps around the pygit2's Repository class"""

    def __init__(self, ):
        """Constructor for GitRepository"""




class GitRepository():
    """Wraps pygit2's Repository object"""

    def __init__(self, repo_path):
        """Constructor for GitRepository"""

        self.repo = pygit2.Repository(repo_path)

    def get_tags(self):
        """
        Returns: List of all the tags in the repository

        """
        return




def main(git_repo):
    repo_path = os.path.join(git_repo, git_folder)
    repo = pygit2.Repository(repo_path)

    tags = [{'name': repo[obj_hex].name,
             'date': str(datetime.fromtimestamp(repo[obj_hex].get_object().commit_time))}
            for obj_hex in repo if repo[obj_hex].type == GitObjectType.tag]

    tags.sort(key=lambda t: t['date'])

    exec_dir = os.getcwd()

    for tag in tags:
        os.chdir(git_repo)
        call(["git", "checkout", "tags/" + tag['name']])

        os.chdir(exec_dir)
        call(["python", git_by_a_bus_executable, "-o", "gbab_output_" + tag['name'], git_repo])

        call(["python3",
              "get_top_contrib_per_file.py",
              os.path.join("gbab_output_" + tag['name'], "estimate_unique_knowledge.tsv"),
              "contribs",
              "contrib_" + tag['name'] + ".csv"])

    os.chdir(git_repo)
    call(["git", "checkout", "master"])
    os.chdir(exec_dir)


if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     print("USAGE {0} <repository_root>".format(__file__))
    #     sys.exit(1)

    # main(sys.argv[1])
    main("/home/kevin/Desktop/facebook-android-sdk/")