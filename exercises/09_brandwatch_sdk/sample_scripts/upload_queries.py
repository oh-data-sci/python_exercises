""" Generates a uploads queries from a CSV file: name, includedTerms, language, samplePercent """

from bwresources import BWQueries
from ps_utils import ps_helper as ps
import csv
import re

#start script
project, username, projname = ps.create_proj_from_user()
queries = BWQueries(project)

#print a template for the csv file if requested
template = input("Would you like a template? [Y/N] ")
if template in ["y", "Y", "yes", "Yes", "YES"]:
	filename = input('Enter name of CSV file for the template (e.g. template.csv): ')
	with open(filename, 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='"', escapechar = '"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(["name", "includedTerms", "language", "samplePercent"])
		writer.writerow(["Sample Query", "(jibberish OR nonsense) AND nvajhfaehn", "en", "100"])

#get name of csv file and read it in
filename = input("When you're ready, enter the name of the CSV file that the queries are stored in: ")
query_list = []
with open(filename) as infile:
    reader = csv.reader(infile)
    for row in reader:
        query_list.append(row)

#format data from csv file for bulk upload of queries
if query_list[0] == ['name', 'includedTerms', 'language', 'samplePercent']:
    query_list.pop(0)
query_dicts = []
for row in query_list:
    query_dicts.append({"name": row[0],
                        "includedTerms": row[1],
                        "language": row[2],
                        "samplePercent": row[3]})
#upload all queries
print("Uploading your queries now.")
queries.upload_all(query_dicts)
print("All done!  Check in your account to see your new queries.")
