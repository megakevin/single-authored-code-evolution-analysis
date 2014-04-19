# Usage: $ python3 merge_bug_commit_data.py /home/kevin/Desktop/contribs-facebook-android-sdk/ /home/kevin/Desktop/merge_contrib.csv
#          python3 merge_bug_commit_data.py <bug_commits_per_tag_directory> <output_file>
#
# Merges all the extracted contribution per tag data into one single file.

__author__ = 'kevin'

import sys
import csv
import os

bug_commit_file_prefix = "bug-commit-"
bug_commit_file_extension = ".csv"

# RQ 1: Generate a csv file for each project with: file, release, if its SAC, LOC
csv_header = ['file_name', 'release', 'commit_num', 'bug_commit_num', 'bug_commit_ratio']

def main():

    bug_commit_files_dir = sys.argv[1]
    output_file = sys.argv[2]

    result = []

    for bug_commit_file in os.listdir(bug_commit_files_dir):

        release = bug_commit_file[len(bug_commit_file_prefix):][:-len(bug_commit_file_extension)]
        bug_commit_file = os.path.join(bug_commit_files_dir, bug_commit_file)

        # file_name,commit_num,bug_commit_num,bug_commit_ratio
        with open(bug_commit_file, newline="") as csv_file:
            reader = csv.DictReader(csv_file)

            result.extend([{'file_name': f['file_name'],
                            'release': release,
                            'commit_num': f['commit_num'],
                            'bug_commit_num': f['bug_commit_num'],
                            'bug_commit_ratio': f['bug_commit_ratio']}
                           for f in reader])

    with open(output_file, 'w', newline='') as output:
        writer = csv.DictWriter(output, csv_header)
        writer.writeheader()
        writer.writerows(result)


if __name__ == "__main__":
    main()
