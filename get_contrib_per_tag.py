#Usage: $ python3 get_contrib_per_tag.py /home/kevin/Desktop/facebook-android-sdk

# Runs Git By A Bus on every tag of the specified repository
# and extracts the file-level contribution information using
# the get_top_contrib_per_file script.

__author__ = 'kevin'

import json
import os

import pygit2

git_folder = ".git/"

def main(git_repo):
    repo_path = os.path.join(git_repo, git_folder)
    repo = pygit2.Repository(repo_path)

    objects = {
        'tags': []
    }

    for objhex in repo:
        obj = repo[objhex]
        if obj.type == pygit2.GIT_OBJ_TAG:
            objects['tags'].append({
                'hex': obj.hex,
                'name': obj.name,
                'message': obj.message,
                'target': obj.target.hex, # base64.b16encode(obj.target).lower(),
                'tagger_name': obj.tagger.name,
                'tagger_email': obj.tagger.email,
            })
        else:
            # ignore blobs and trees
            pass

    print(json.dumps(objects, indent=2))


if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     print("USAGE {0} <repository_root>".format(__file__))
    #     sys.exit(1)

    # main(sys.argv[1])
    main("/home/kevin/Desktop/facebook-android-sdk")