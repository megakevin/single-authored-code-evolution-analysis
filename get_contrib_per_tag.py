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


class GitObjectType():
    """Defines Git object types in terms of pygiy2's GIT_OBJs"""

    commit = pygit2.GIT_OBJ_COMMIT
    tag = pygit2.GIT_OBJ_TAG

class Tag():
    """Represents a Tag in a git repository"""

    def __init__(self, args):
        """Constructor for Tag"""




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

    os.chdir(git_repo)

    for tag in tags:
        call(["git", "checkout", "tags/" + tag])

        # Call git by a bus
        # Call get_top_contrib_per_file
        # Delete git by a bus output folder


    print(json.dumps(tags, indent=2))


if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     print("USAGE {0} <repository_root>".format(__file__))
    #     sys.exit(1)

    # main(sys.argv[1])
    main("/home/kevin/Desktop/facebook-android-sdk/")