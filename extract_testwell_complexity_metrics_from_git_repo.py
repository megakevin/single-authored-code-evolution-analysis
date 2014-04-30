#Usage: $ python extract_complexity_metrics_from_git_repo.py <REPO-PATH>

# Extract code metrics for each release in the Git-repo <REPO-PATH>
# based on Harold script.

__author__ = 'Felivel'

import sys
import os
import subprocess
from dateutil import parser
import time



class GitTag:
    name=None
    tag_hash=None
    date=None
    tag_timestamp=None
    
    def __init(self, name=None,t_hash=None, date=None, t_timestamp=None):
        self.name=name
        self.tag_hash=t_hash
        self.date=date
        self.tag_timestamp=t_timestamp

    @staticmethod
    def tag_from_rawline(tag_as_line):
        git_tag = GitTag()
        raw_tag, raw_hash, raw_date, raw_timestamp = tag_as_line.split("|")
        
        # process the hash:
        git_tag.tag_hash = raw_hash.strip()
        
        # process the timestamp
        git_tag.tag_timestamp = float(raw_timestamp.strip())
        
        # process the datetime
        git_tag.date = parser.parse(raw_date.strip())
        #git_tag.date = git_tag.date.replace( tzinfo=None )
                
        #raw_tag = raw_tag.split("tag:")[1]
        
        # get the git-tag
        if "," in raw_tag:
            #git_tag.name = raw_tag.split(",")[0].replace("(tag: ","").strip()
            git_tag.name = raw_tag.split(",")[0].strip()
            #git_tag.name = raw_tag.split("tag:")[1].split(",")[0].strip()
        else:
            #git_tag.name = raw_tag.replace("(tag: ","").replace(")","").strip()
            git_tag.name = raw_tag.replace(")","").strip()
            git_tag.name = git_tag.name.replace("(","").strip()
            #git_tag.name = raw_tag.split("tag:")[1].replace(")","").strip()
        return git_tag
        

def get_tags_from_repo(repo_path):
    """Get a list of git-tags objects"""
    
    # Get the list of the tags and their date using git-commands 
    # tag_name | tag_hash | tag_date | tag_timestamp 
    cmd_get_tags = 'cd {0} & git log --tags --simplify-by-decoration --pretty="format:%d | %H | %ai | %at"'.format(repo_path)
    
    results_cmd = subprocess.check_output(cmd_get_tags, shell=True)    
        
    # Convert each line into a git-tag    
    list_tags = list()
    for line in results_cmd.splitlines():
        list_tags.append(GitTag.tag_from_rawline(line))    
    
    # Sort the tags by date (earliest - latest)
    list_tags.sort(key=lambda tag: tag.date, reverse=False)
    return list_tags


def extract_metrics_for_tags_in_repo(repo_path):
    """Extract metrics for each release of the repo"""    
    
    # Get the list of tags
    print "\n\tGetting the tags from {0}...".format(repo_path)
    list_tags = get_tags_from_repo(repo_path)
    for tag in list_tags:
        print "\ttag: "+tag.name, " \t- \tdate: "+tag.date.isoformat()
    print "\n\tNum-tags: {0}".format(len(list_tags))
    
    # Create the directory for the metrics
    # file_basename = repo_path.replace("/"," ").strip().replace(" ","-")
    # vmetrics_dir = "metrics-{0}".format(file_basename)
    # os.system( "mkdir -p {0}".format(metrics_dir) )
    
    # Extract the metrics for each tag
    counter = 1
    total_number = len(list_tags)
    start_time = time.time()
    for tag in list_tags:
        # Do the checkuot
        # git checkout tags/<tag_name>
        print "\tChecking out the tag: {0}...".format( tag.name )
        os.system( "cd {0} & git checkout tags/{1}".format(repo_path, tag.name) )
        
        
        # Getting file list
        print "\tGetting file list..."        
        os.system('dir {0}*.java /B /S > C:/cmtdata/temp/filelist.txt'.format(repo_path))
        
        # Analyze the code
        print "\tGetting the metrics.."
        os.system('cmtjava -f C:/cmtdata/filelist.txt -x -s -o C:/cmtdata/testwell-{0}.xls'.format(tag.name))

        # Report progress and speed
        if counter % 2 == 0:
            end_time = time.time()
            report_info(start_time, end_time, counter, total_number)
        counter = counter + 1
        print "\n"
        

def report_info(start_time, end_time, counter, total_number):
    elapse = end_time - start_time
    rate = counter / elapse
    time_required = total_number/rate/3600
    print "\n\t\tprocessed-tags:", counter, "   -   total-tags:",total_number
    print "\n\t\ttime in secs: {0}  -  time in mins: {1}  -  time in hours: {2}".format(elapse, (elapse/60), (elapse/3600))
    print "\n\t\trate: {0} tags/secs".format(rate)
    print "\n\t\tTotal time Required:  -   {2} years   -   {1} days  -   {0} hours".format(time_required,time_required/24,time_required/(24*365))
    remaining_tags = total_number - counter
    time_remained = remaining_tags/rate/3600
    print "\n\t\tTotal time Remained:  -   {2} years   -   {1} days  -   {0} hours  -  {3} mins\n".format(time_remained, time_remained/24, time_remained/(24*365), time_remained * 60 )
    
    
if __name__ == "__main__":
#    repo_paths = ["tmp/facebook-android-sdk/", "tmp/facebook-php-sdk"]#sys.argv[1]
#    repo_paths = ["tmp/facebook-php-sdk"]    
#    repo_paths = ["mongo"]    
#    repo_paths = ["nodejs"]
#    for repo in repo_paths:
#        extract_metrics_for_tags_in_repo(repo)

    # The path of the repo
    repo_repo = sys.argv[1]
    extract_metrics_for_tags_in_repo(repo_repo)
    