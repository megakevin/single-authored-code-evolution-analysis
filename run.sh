#!/bin/bash

#python3 get_contrib_per_tag.py /home/kevin/Desktop/evolution-project/repos/facebook-android-sdk
#python3 merge_contrib_data.py /home/kevin/Desktop/evolution-project/data/contrib-facebook-android-sdk /home/kevin/Desktop/evolution-project/data/sac-facebook-android-sdk.csv

# Get contrib data for all projects per tag
#echo "calculating for apache-avro"; python3 get_contrib_per_tag.py /home/kevin/Desktop/evolution-project/repos/apache-avro /home/kevin/Desktop/evolution-project/contrib-apache-avro
#echo "calculating for apache-mahout"; python3 get_contrib_per_tag.py /home/kevin/Desktop/evolution-project/repos/apache-mahout /home/kevin/Desktop/evolution-project/contrib-apache-mahout
#echo "calculating for apache-tika"; python3 get_contrib_per_tag.py /home/kevin/Desktop/evolution-project/repos/apache-tika /home/kevin/Desktop/evolution-project/contrib-apache-tika
#echo "calculating for vrapper"; python3 get_contrib_per_tag.py /home/kevin/Desktop/evolution-project/repos/vrapper /home/kevin/Desktop/evolution-project/contrib-vrapper
#echo "calculating for apache-zookeeper"; python3 get_contrib_per_tag.py /home/kevin/Desktop/evolution-project/repos/apache-zookeeper /home/kevin/Desktop/evolution-project/contrib-apache-zookeeper
#echo "calculating for facebook-android-sdk"; python3 get_contrib_per_tag.py /home/kevin/Desktop/evolution-project/repos/facebook-android-sdk /home/kevin/Desktop/evolution-project/contrib-facebook-android-sdk
#echo "calculating for github-android-app"; python3 get_contrib_per_tag.py /home/kevin/Desktop/evolution-project/repos/github-android-app /home/kevin/Desktop/evolution-project/contrib-github-android-app
#echo "calculating for wordpress-android"; python3 get_contrib_per_tag.py /home/kevin/Desktop/evolution-project/repos/wordpress-android /home/kevin/Desktop/evolution-project/contrib-wordpress-android

# Merge contrib data files into one per project
#echo "calculating for apache-avro"; python3 merge_contrib_data.py /home/kevin/Desktop/evolution-project/contrib-apache-avro /home/kevin/Desktop/evolution-project/data/sac-apache-avro.csv
#echo "calculating for apache-mahout"; python3 merge_contrib_data.py /home/kevin/Desktop/evolution-project/contrib-apache-mahout /home/kevin/Desktop/evolution-project/data/sac-apache-mahout.csv
#echo "calculating for apache-tika"; python3 merge_contrib_data.py /home/kevin/Desktop/evolution-project/contrib-apache-tika /home/kevin/Desktop/evolution-project/data/sac-apache-tika.csv
#echo "calculating for vrapper"; python3 merge_contrib_data.py /home/kevin/Desktop/evolution-project/contrib-vrapper /home/kevin/Desktop/evolution-project/data/sac-vrapper.csv
#echo "calculating for apache-zookeeper"; python3 merge_contrib_data.py /home/kevin/Desktop/evolution-project/contrib-apache-zookeeper /home/kevin/Desktop/evolution-project/data/sac-apache-zookeeper.csv
#echo "calculating for facebook-android-sdk"; python3 merge_contrib_data.py /home/kevin/Desktop/evolution-project/contrib-facebook-android-sdk /home/kevin/Desktop/evolution-project/data/sac-facebook-android-sdk.csv
#echo "calculating for github-android-app"; python3 merge_contrib_data.py /home/kevin/Desktop/evolution-project/contrib-github-android-app /home/kevin/Desktop/evolution-project/data/sac-github-android-app.csv
#echo "calculating for wordpress-android"; python3 merge_contrib_data.py /home/kevin/Desktop/evolution-project/contrib-wordpress-android /home/kevin/Desktop/evolution-project/data/sac-wordpress-android.csv

# Get bug-commit ratio for all projects per tag
#echo "calculating for apache-avro"; python3 get_bug_commit_ratio_per_tag.py /home/kevin/Desktop/evolution-project/repos/apache-avro /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/apache-avro
#echo "calculating for apache-mahout"; python3 get_bug_commit_ratio_per_tag.py /home/kevin/Desktop/evolution-project/repos/apache-mahout /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/apache-mahout
#echo "calculating for apache-tika"; python3 get_bug_commit_ratio_per_tag.py /home/kevin/Desktop/evolution-project/repos/apache-tika /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/apache-tika
#echo "calculating for vrapper"; python3 get_bug_commit_ratio_per_tag.py /home/kevin/Desktop/evolution-project/repos/vrapper /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/vrapper
#echo "calculating for apache-zookeeper"; python3 get_bug_commit_ratio_per_tag.py /home/kevin/Desktop/evolution-project/repos/apache-zookeeper /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/apache-zookeeper
#echo "calculating for facebook-android-sdk"; python3 get_bug_commit_ratio_per_tag.py /home/kevin/Desktop/evolution-project/repos/facebook-android-sdk /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/facebook-android-sdk
#echo "calculating for github-android-app"; python3 get_bug_commit_ratio_per_tag.py /home/kevin/Desktop/evolution-project/repos/github-android-app /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/github-android-app
#echo "calculating for WordPress-Android"; python3 get_bug_commit_ratio_per_tag.py /home/kevin/Desktop/evolution-project/repos/wordpress-android /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/wordpress-android

# Merge bug commit files into one per project
#echo "merging for apache-avro"; python3 merge_bug_commit_data.py /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/apache-avro /home/kevin/Desktop/evolution-project/data/bug-commit-apache-avro.csv
#echo "merging for apache-mahout"; python3 merge_bug_commit_data.py /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/apache-mahout /home/kevin/Desktop/evolution-project/data/bug-commit-apache-mahout.csv
#echo "merging for apache-tika"; python3 merge_bug_commit_data.py /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/apache-tika /home/kevin/Desktop/evolution-project/data/bug-commit-apache-tika.csv
#echo "merging for vrapper"; python3 merge_bug_commit_data.py /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/vrapper /home/kevin/Desktop/evolution-project/data/bug-commit-vrapper.csv
#echo "merging for apache-zookeeper"; python3 merge_bug_commit_data.py /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/apache-zookeeper /home/kevin/Desktop/evolution-project/data/bug-commit-apache-zookeeper.csv
#echo "merging for facebook-android-sdk"; python3 merge_bug_commit_data.py /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/facebook-android-sdk /home/kevin/Desktop/evolution-project/data/bug-commit-facebook-android-sdk.csv
#echo "merging for github-android-app"; python3 merge_bug_commit_data.py /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/github-android-app /home/kevin/Desktop/evolution-project/data/bug-commit-github-android-app.csv
#echo "merging for wordpress-android"; python3 merge_bug_commit_data.py /home/kevin/Desktop/evolution-project/data/bug-commit-ratio/wordpress-android /home/kevin/Desktop/evolution-project/data/bug-commit-wordpress-android.csv

# Merge bug commit files into one per project
#echo "calculating for apache-avro"; python3 merge_files.py /home/kevin/Desktop/evolution-project/data/stats/sac-apache-avro.csv /home/kevin/Desktop/evolution-project/data/stats/bug-commit-apache-avro.csv /home/kevin/Desktop/evolution-project/data/stats/stats-apache-avro.csv
#echo "calculating for apache-mahout"; python3 merge_files.py /home/kevin/Desktop/evolution-project/data/stats/sac-apache-mahout.csv /home/kevin/Desktop/evolution-project/data/stats/bug-commit-apache-mahout.csv /home/kevin/Desktop/evolution-project/data/stats/stats-apache-mahout.csv
#echo "calculating for apache-tika"; python3 merge_files.py /home/kevin/Desktop/evolution-project/data/stats/sac-apache-tika.csv /home/kevin/Desktop/evolution-project/data/stats/bug-commit-apache-tika.csv /home/kevin/Desktop/evolution-project/data/stats/stats-apache-tika.csv
#echo "calculating for vrapper"; python3 merge_files.py /home/kevin/Desktop/evolution-project/data/stats/sac-vrapper.csv /home/kevin/Desktop/evolution-project/data/stats/bug-commit-vrapper.csv /home/kevin/Desktop/evolution-project/data/stats/stats-vrapper.csv
#echo "calculating for apache-zookeeper"; python3 merge_files.py /home/kevin/Desktop/evolution-project/data/stats/sac-apache-zookeeper.csv /home/kevin/Desktop/evolution-project/data/stats/bug-commit-apache-zookeeper.csv /home/kevin/Desktop/evolution-project/data/stats/stats-apache-zookeeper.csv
#echo "calculating for facebook-android-sdk"; python3 merge_files.py /home/kevin/Desktop/evolution-project/data/stats/sac-facebook-android-sdk.csv /home/kevin/Desktop/evolution-project/data/stats/bug-commit-facebook-android-sdk.csv /home/kevin/Desktop/evolution-project/data/stats/stats-facebook-android-sdk.csv
#echo "calculating for github-android-app"; python3 merge_files.py /home/kevin/Desktop/evolution-project/data/stats/sac-github-android-app.csv /home/kevin/Desktop/evolution-project/data/stats/bug-commit-github-android-app.csv /home/kevin/Desktop/evolution-project/data/stats/stats-github-android-app.csv
#echo "calculating for wordpress-android"; python3 merge_files.py /home/kevin/Desktop/evolution-project/data/stats/sac-wordpress-android.csv /home/kevin/Desktop/evolution-project/data/stats/bug-commit-wordpress-android.csv /home/kevin/Desktop/evolution-project/data/stats/stats-wordpress-android.csv

# Fix bug and commit count data
#echo "calculating for apache-avro"; python3 fix_bug_commits.py /home/kevin/Desktop/evolution-project/repos/apache-avro /home/kevin/Desktop/evolution-project/data/stats/stats-apache-avro.csv /home/kevin/Desktop/evolution-project/stats-apache-avro.fixed.csv
#echo "calculating for apache-mahout"; python3 fix_bug_commits.py /home/kevin/Desktop/evolution-project/repos/apache-mahout /home/kevin/Desktop/evolution-project/data/stats/stats-apache-mahout.csv /home/kevin/Desktop/evolution-project/stats-apache-mahout.fixed.csv
#echo "calculating for apache-tika"; python3 fix_bug_commits.py /home/kevin/Desktop/evolution-project/repos/apache-tika /home/kevin/Desktop/evolution-project/data/stats/stats-apache-tika.csv /home/kevin/Desktop/evolution-project/stats-apache-tika.fixed.csv
#echo "calculating for vrapper"; python3 fix_bug_commits.py /home/kevin/Desktop/evolution-project/repos/vrapper /home/kevin/Desktop/evolution-project/data/stats/stats-vrapper.csv /home/kevin/Desktop/evolution-project/stats-vrapper.fixed.csv
#echo "calculating for apache-zookeeper"; python3 fix_bug_commits.py /home/kevin/Desktop/evolution-project/repos/apache-zookeeper /home/kevin/Desktop/evolution-project/data/stats/stats-apache-zookeeper.csv /home/kevin/Desktop/evolution-project/stats-apache-zookeeper.fixed.csv
#echo "calculating for facebook-android-sdk"; python3 fix_bug_commits.py /home/kevin/Desktop/evolution-project/repos/facebook-android-sdk /home/kevin/Desktop/evolution-project/data/stats/stats-facebook-android-sdk.csv /home/kevin/Desktop/evolution-project/stats-facebook-android-sdk.fixed.csv
#echo "calculating for github-android-app"; python3 fix_bug_commits.py /home/kevin/Desktop/evolution-project/repos/github-android-app /home/kevin/Desktop/evolution-project/data/stats/stats-github-android-app.csv /home/kevin/Desktop/evolution-project/stats-github-android-app.fixed.csv
#echo "calculating for wordpress-android"; python3 fix_bug_commits.py /home/kevin/Desktop/evolution-project/repos/wordpress-android /home/kevin/Desktop/evolution-project/data/stats/stats-wordpress-android.csv /home/kevin/Desktop/evolution-project/stats-wordpress-android.fixed.csv

# Get top contributors experience
echo "calculating for apache-avro"; python3 get_top_devs.py /home/kevin/Desktop/evolution-project/data/contrib/contrib-apache-avro /home/kevin/Desktop/evolution-project/repos/apache-avro /home/kevin/Desktop/evolution-project/top-devs-apache-avro.csv
echo "calculating for apache-mahout"; python3 get_top_devs.py /home/kevin/Desktop/evolution-project/data/contrib/contrib-apache-mahout /home/kevin/Desktop/evolution-project/repos/apache-mahout /home/kevin/Desktop/evolution-project/top-devs-apache-mahout.csv
echo "calculating for apache-tika"; python3 get_top_devs.py /home/kevin/Desktop/evolution-project/data/contrib/contrib-apache-tika /home/kevin/Desktop/evolution-project/repos/apache-tika /home/kevin/Desktop/evolution-project/top-devs-apache-tika.csv
echo "calculating for vrapper"; python3 get_top_devs.py /home/kevin/Desktop/evolution-project/data/contrib/contrib-vrapper /home/kevin/Desktop/evolution-project/repos/vrapper /home/kevin/Desktop/evolution-project/top-devs-vrapper.csv
echo "calculating for apache-zookeeper"; python3 get_top_devs.py /home/kevin/Desktop/evolution-project/data/contrib/contrib-apache-zookeeper /home/kevin/Desktop/evolution-project/repos/apache-zookeeper /home/kevin/Desktop/evolution-project/top-devs-apache-zookeeper.csv
echo "calculating for facebook-android-sdk"; python3 get_top_devs.py /home/kevin/Desktop/evolution-project/data/contrib/contrib-facebook-android-sdk /home/kevin/Desktop/evolution-project/repos/facebook-android-sdk /home/kevin/Desktop/evolution-project/top-devs-facebook-android-sdk.csv
echo "calculating for github-android-app"; python3 get_top_devs.py /home/kevin/Desktop/evolution-project/data/contrib/contrib-github-android-app /home/kevin/Desktop/evolution-project/repos/github-android-app /home/kevin/Desktop/evolution-project/top-devs-github-android-app.csv
echo "calculating for wordpress-android"; python3 get_top_devs.py /home/kevin/Desktop/evolution-project/data/contrib/contrib-wordpress-android /home/kevin/Desktop/evolution-project/repos/wordpress-android /home/kevin/Desktop/evolution-project/top-devs-wordpress-android.csv
