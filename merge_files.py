# Usage: $ python3 merge_files.py /home/kevin/Desktop/sac-data/contrib-facebook-android-sdk/highest_contributions.csv /home/kevin/Desktop/sac-data/bug-commit-facebook-android-sdk/bug_commit_ratio.csv /home/kevin/Desktop/sac-data/metrics-facebook-android-sdk/metrics.csv output.csv
#
# Merges two given contrib and git_commit files.
# TODO: need to include Metrics

__author__ = 'kevin'

import sys
import csv

csv_header = ['file_name', 'release', 'is_sac', 'loc', 'commit_num', 'bug_commit_num', 'bug_commit_ratio']


def merge_files(contrib_file, bug_commit_file, output_file):
    with open(contrib_file, "r") as contrib_file:
        # 'file_name', 'release', 'is_sac', 'loc'
        contrib_reader = [row for row in csv.DictReader(contrib_file)]

    with open(bug_commit_file, "r") as bug_commit_file:
        # 'release', 'commit_num', 'bug_commit_num', 'bug_commit_ratio'
        bug_commit_reader = [row for row in csv.DictReader(bug_commit_file)]

    with open(output_file, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, csv_header)
        writer.writeheader()

        # The driver of the iteration needs to be this one because it has only the files
        # "interesting to Git By A Bus". contrib files have less rows than bug-commit and metric files.
        for contrib_row in contrib_reader:
            file_name = contrib_row['file_name']
            release = contrib_row['release']

            bug_commit_row = [row for row in bug_commit_reader
                              if row['file_name'] == file_name and row['release'] == release]

            if bug_commit_row:
                bug_commit_row = bug_commit_row[0]
            else:
                bug_commit_row = {'commit_num': "",
                                  'bug_commit_num': "",
                                  'bug_commit_ratio': ""}

            writer.writerow({'file_name': file_name,
                             'release': release,
                             'is_sac': contrib_row['is_sac'],
                             'loc': contrib_row['loc'],
                             'commit_num': bug_commit_row['commit_num'],
                             'bug_commit_num': bug_commit_row['bug_commit_num'],
                             'bug_commit_ratio': bug_commit_row['bug_commit_ratio']})


def main():
    contrib_file = sys.argv[1]
    bug_commit_file = sys.argv[2]
    output_file = sys.argv[3]

    merge_files(contrib_file, bug_commit_file, output_file)


if __name__ == "__main__":
    main()