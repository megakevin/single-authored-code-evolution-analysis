# Usage: $ python3 merge_contrib_data.py /home/kevin/Desktop/contribs-facebook-android-sdk/ /home/kevin/Desktop/merge_contrib.csv
#          python3 merge_contrib_data.py <contributions_per_tag_directory> <output_file>
#
# Merges all the extracted contribution per tag data into one single file.

__author__ = 'kevin'

import sys
import csv
import os

contrib_file_prefix = "contrib_"
contrib_file_extension = ".csv"
single_authored_threshold = 90.0

# RQ 1: Generate a csv file for each project with: file, release, if its SAC, LOC
csv_header = ['file_name', 'release', 'is_sac', 'loc']


def format_dict(raw_data, release):
    return {'file_name': raw_data['file_name'],
            'release': release,
            'is_sac': float(raw_data['top_single_dev_contribution_knowledge_percent']) > single_authored_threshold,
            'loc': int(raw_data['lines_count'])}


def main(argv):

    contrib_data_dir = argv[1]
    output_file = argv[2]
    # project_name = argv[3]

    result = []

    for contrib_file in os.listdir(contrib_data_dir):

        release = contrib_file[len(contrib_file_prefix):][:-len(contrib_file_extension)]
        contrib_file = os.path.join(contrib_data_dir, contrib_file)

        with open(contrib_file, newline="") as csv_file:
            for row in csv.DictReader(csv_file):
                result.append(format_dict(row, release))

    with open(output_file, 'w', newline='') as output:
        writer = csv.DictWriter(output, csv_header)
        writer.writeheader()
        writer.writerows(result)


if __name__ == "__main__":
    main(sys.argv)
