#!/bin/bash

python3 get_contrib_per_tag.py /home/kevin/Desktop/evolution-project/repos/facebook-android-sdk
python3 merge_contrib_data.py /home/kevin/Desktop/evolution-project/data/contrib-facebook-android-sdk /home/kevin/Desktop/evolution-project/data/sac-facebook-android-sdk.csv
python3 get_bug_commit_ratio_per_tag.py /home/kevin/Desktop/evolution-project/repos/facebook-android-sdk /home/kevin/Desktop/evolution-project/data/bug-commit-ratio
python3 merge_bug_commit_data.py /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/facebook-android-sdk /home/kevin/Desktop/evolution-project/data/bug_commit-facebook-android-sdk