#!/usr/bin/env python3.7
"""
The program outputs the following metrics:
0. Number of users accessed the server
1. Number of uploads > 50kb
2. Number of uploads by `jeff22` on 04/15th/2020
"""
import csv
from datetime import datetime


def read_csv():
    """
    Parses server_log file
    """
    with open('server_log.csv') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        jeff22_uploads_count = 0
        fifty_kb_count = 0
        unique_names = []

        for row in csv_read:
            # adding every new name to the list
            if row['username'] not in unique_names:
                unique_names.append(row['username'])

            # counts jeff22's upload on 04/15
            # converting str to datetime object
            date_time_format = '%a %b %d %H:%M:%S %Z %Y'
            date_time = datetime.strptime(row['timestamp'], date_time_format)
            # D-M-d-H:M:S-Y to YYYY-MM-DD format
            date_only = datetime.strftime(date_time, "%Y-%m-%d")
            if row['username'] == "jeff22" \
               and row['operation'] == 'upload'\
               and date_only == '2020-04-15':
                jeff22_uploads_count += 1

            # checks # of upload > 50kb
            if int(row['size']) > 50 and row['operation'] == 'upload':
                fifty_kb_count += 1

    print(f"{len(unique_names)} users accessed the server")
    print(f"jeff22 uploaded {jeff22_uploads_count} times"
          "to the server on April 15th")
    print(f"{fifty_kb_count} uploads  were larger than `50kB`")


read_csv()
