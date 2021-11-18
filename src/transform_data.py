#####
# Setting environment variable. NOTE: This is not a production-safe practice.
# This is only acceptable because this is a lab.
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '//c/Users/yaoyu/musa509-0829-1d970995ed94.json'
#####

from pathlib import Path
from pipeline_tools import run_transform_gbq

sql_root = Path(__file__).parent / 'sql'

def main():
    run_transform_gbq('lab09', 'model_blockgroups', sql_root)
    run_transform_gbq('lab09', 'blockgroups_mapdata', sql_root)
    run_transform_gbq('lab09', 'blockgroups_chartdata', sql_root)
    run_transform_gbq('lab09', 'blockgroups_listdata', sql_root)

if __name__ == '__main__':
    main()
