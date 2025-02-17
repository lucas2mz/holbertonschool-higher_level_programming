#!/usr/bin/python3
"""
modulo
"""


import csv 
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            data  = list(reader)

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"Error converting CSV to JSON: {e}")
        return False
