# file manipulations

filename = 'datafiles/NY_rodent_inspections_sample.csv'

with open(filename, encoding='utf-8') as infile:
    # infile is an iterator over the lines in the file
    for i, line in enumerate(infile):
        # process each row?
        print('row number:', i, ':', line)
