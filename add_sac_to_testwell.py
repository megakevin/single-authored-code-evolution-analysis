
__author__ = 'kevin'

import sys
import csv

testwell_header = ['Release', 'File', 'Line', 'Measured item', 'vG_b', 'vG_e', 'Params', 'MaxND', 'LOCphy', 'LOCbl', 'LOCpro', 'LOCcom', 'V', 'B(x100)', 'T', 'N1', 'N2', 'n1', 'n2', 'D', 'E', 'L(x1000)', 'MIwoc', 'MIcw', 'MI', 'WarnMask']
sac_header = ['file_name', 'release', 'is_sac', 'loc']
output_header = ['Release', 'File', 'Line', 'Measured item', 'vG_b', 'vG_e', 'Params', 'MaxND', 'LOCphy', 'LOCbl', 'LOCpro', 'LOCcom', 'V', 'B(x100)', 'T', 'N1', 'N2', 'n1', 'n2', 'D', 'E', 'L(x1000)', 'MIwoc', 'MIcw', 'MI', 'WarnMask', 'is_sac']

def first_or_default(l, default=None):
    if l:
        return l[0]
    else:
        return default

def merge_files(sac_file, testwell_file, output_file):
    with open(testwell_file, "r") as testwell_file:
        # 'file_name', 'release', 'is_sac', 'loc'
        testwell_reader = [row for row in csv.DictReader(testwell_file)]

    with open(sac_file, "r") as sac_file:
        # 'file_name', 'release', 'is_sac', 'loc'
        sac_reader = [row for row in csv.DictReader(sac_file)]

    with open(output_file, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, output_header)
        writer.writeheader()

        for testwell_row in testwell_reader:
            file_name = testwell_row['File'].replace('\\', '/')
            release = testwell_row['Release']

            sac_row = first_or_default([row for row in sac_reader
                                        if row['file_name'] in file_name and row['release'] == release])

            if sac_row:
                testwell_row['is_sac'] = sac_row['is_sac']
                writer.writerow(testwell_row)


def main():
    sac_file = sys.argv[1]
    testwell_file = sys.argv[2]
    output_file = sys.argv[3]

    merge_files(sac_file, testwell_file, output_file)


if __name__ == "__main__":
    main()