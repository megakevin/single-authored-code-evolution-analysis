# Usage: $ python3 merge_bug_commit_data.py /home/kevin/Desktop/contribs-facebook-android-sdk/ /home/kevin/Desktop/merge_contrib.csv
#          python3 merge_bug_commit_data.py <bug_commits_per_tag_directory> <output_file>
#
# Merges all the extracted contribution per tag data into one single file.


__author__ = 'felivel'
#based on kevin's script

import sys
import csv
import os

bug_commit_file_prefix = "testwell-"
bug_commit_file_extension = ".xls"


#csv_header = ['file_name', 'release', 'commit_num', 'bug_commit_num', 'bug_commit_ratio']
csv_header = ['Release', 'File', 'Line', 'Measured item', 'vG_b', 'vG_e', 'Params', 'MaxND', 'LOCphy', 'LOCbl', 'LOCpro', 'LOCcom', 'V', 'B(x100)', 'T', 'N1', 'N2', 'n1', 'n2', 'D', 'E', 'L(x1000)', 'MIwoc', 'MIcw', 'MI', 'WarnMask']

def main():

    bug_commit_files_dir = sys.argv[1]
    output_file = sys.argv[2]

    result = []

    for bug_commit_file in os.listdir(bug_commit_files_dir):

        release = bug_commit_file[len(bug_commit_file_prefix):][:-len(bug_commit_file_extension)]
        bug_commit_file = os.path.join(bug_commit_files_dir, bug_commit_file)

        # file_name,commit_num,bug_commit_num,bug_commit_ratio
        with open(bug_commit_file) as csv_file:
            reader = csv.DictReader(csv_file , dialect="excel",delimiter='	')
                           
            result.extend([{'Release': release, 
                            'File': f['File'], 
                            'Line': f['Line'], 
                            'Measured item': f['Measured item'], 
                            'vG_b': f['vG_b'], 
                            'vG_e': f['vG_e'], 
                            'Params': f['Params'], 
                            'MaxND': f['MaxND'], 
                            'LOCphy': f['LOCphy'], 
                            'LOCbl': f['LOCbl'], 
                            'LOCpro': f['LOCpro'], 
                            'LOCcom': f['LOCcom'], 
                            'V': f['V'], 
                            'B(x100)': f['B(x100)'], 
                            'T': f['T'], 
                            'N1': f['N1'], 
                            'n1': f['n1'], 
                            'n2': f['n2'], 
                            'D': f['D'], 
                            'E': f['E'], 
                            'L(x1000)': f['L(x1000)'], 
                            'MIwoc': f['MIwoc'], 
                            'MIcw': f['MIcw'], 
                            'MI': f['MI'],
                            'WarnMask': f['WarnMask']}
                           for f in reader])

    with open(output_file, 'w') as output:
        writer = csv.DictWriter(output, csv_header)
        writer.writeheader()
        writer.writerows(result)


if __name__ == "__main__":
    main()
