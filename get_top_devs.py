__author__ = 'kevin'

import sys
import os
import csv
from pygit2 import Repository
from subprocess import call, check_output

contrib_file_prefix = "contrib_"
contrib_file_extension = ".csv"

# file_name	lines_count	top_single_dev_contribution_knowledge	top_single_dev_contribution_knowledge_percent
csv_header = ['release', 'top_dev', 'files_owned', 'dev_commits', 'release_commits']
git_folder = ".git/"


def main():
    contrib_data_dir = sys.argv[1]
    git_repo = sys.argv[2]
    output_file = sys.argv[3]

    result = []
    exec_dir = os.getcwd()

    for contrib_file in os.listdir(contrib_data_dir):

        release = contrib_file[len(contrib_file_prefix):][:-len(contrib_file_extension)]
        contrib_file = os.path.join(contrib_data_dir, contrib_file)

        top_devs = {}

        with open(contrib_file, newline="") as csv_file:
            for row in csv.DictReader(csv_file):
                top_dev = row['top_single_dev_contribution_knowledge'].split(":")[0]

                if top_dev in top_devs:
                    top_devs[top_dev] += 1
                else:
                    top_devs[top_dev] = 1

        os.chdir(git_repo)
        call(["git", "checkout", "tags/" + release])
        os.chdir(exec_dir)

        for top_dev in top_devs:
            author_commit_count = 0
            commit_count = 0

            repo = Repository(os.path.join(git_repo, git_folder))
            for commit in repo.walk(repo.head.target):
                commit_count += 1
                if commit.author.name == top_dev:
                    author_commit_count += 1

            result.append({'release': release,
                           'release_commits': commit_count,
                           'top_dev': top_dev,
                           'files_owned': top_devs[top_dev],
                           'dev_commits': author_commit_count})

    with open(output_file, 'w', newline='') as output:
        writer = csv.DictWriter(output, csv_header)
        writer.writeheader()
        writer.writerows(result)


if __name__ == "__main__":
    main()