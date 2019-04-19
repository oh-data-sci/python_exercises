""" Generates a CSV file for Queries: name, includedTerms, language, samplePercent """

from bwresources import BWQueries
from ps_utils import ps_helper as ps
import csv
import re

#start script
project, username, projname = ps.create_proj_from_user()
filename = input('Enter name of CSV file to write to:')


# Now create a BWQueries object and retrieve the detailed information of each query in the project
queries = BWQueries(project)
query_info = queries.get()


# Next we format the list of queries before outputting them to a csv.
formatted_list = []

for query in query_info:
    if query["type"] == "search string":
        included_terms = re.sub(r"[\r\n ]+?", " ",query["includedTerms"][0])
        formatted = [query["name"], included_terms, ', '.join(query["languages"]), query["samplePercent"]]
        formatted_list.append(formatted)

with open(filename, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows([["name", "includedTerms", "language", "samplePercent"]])
    writer.writerows(formatted_list)
