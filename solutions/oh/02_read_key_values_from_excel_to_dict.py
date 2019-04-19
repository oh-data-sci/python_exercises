data = sheet.values
# the data object is a generator, meaning we can step through its values with the `next()` method.
# each call to `next()` generates a row in the form of a tuple of columns
first_row = next(data)
sheet_title = first_row[0] # first row, first column (cell A1) contains a title.

# collect the key, value pairs in the sheet into a dict
chart_details = {}
for row in data:
    chart_details[row[0]] = row[1]
print(chart_details)

# this only works so far. some files have a lot of rubbish in the footer that needs to be ignored/cleaned
# let's see a problematic file

filename_spreadsheet = 'datafiles/example_filters/Example filters - Nokia.xlsx'
#spreadsheet = load_workbook(filename_spreadsheet, read_only=True)
spreadsheet = load_workbook(filename_spreadsheet) # read only files are more limited
sheet = spreadsheet.active
data = sheet.values
# the data object is a generator, meaning we can step through its values with the `next()` method.
# each call to `next()` generates a row in the form of a tuple of columns
first_row = next(data)
sheet_title = first_row[0] # first row, first column (cell A1) contains a title.
print(
    'file', filename_spreadsheet,
    'contains the sheet', sheet.title, 
    'with', sheet_title, 'in the A1 cell')
# collect the key, value pairs in the sheet into a dict
chart_details = {}
for row in data:
    if row[0] is not None and row[0] is not '':
        chart_details[row[0]] = row[1]
    else: 
        # stop processing data rows on first blank cell in A column:
        break
print(chart_details)

# now just wrap this up as a function
def read_chart_export(filename_spreadsheet):
    # reads chart data export in excel format and extracts the chart data
    # returns a dictionary with the chart properties 
    # assumes:
    #   cell A1 contains a table title
    #   the keys are in cells A2:An, where n is number of properties
    #   the values are in cells B2:Bn 
    #   any rows below a blank cell in the A column are 'rubbish'
    # nb! files are opened as read-write. because read-only files have limited functionality in the openpyxl module
    
    spreadsheet = load_workbook(filename_spreadsheet) 
    sheet = spreadsheet.active
    data = sheet.values
    # the `data` object is a generator, meaning we can step through its values with the `next()` method.
    # each call to `next()` generates a row in the form of a tuple of columns
    first_row = next(data)
    sheet_title = first_row[0] # first row, first column (cell A1) contains a title.
    print('reading exported chart data from', sheet.title, 'in', filename_spreadsheet)
    # collect the key, value pairs in the sheet into a dict
    chart_details = {}
    for row in data:
        if row[0] is not None and row[0] is not '':
            chart_details[row[0]] = row[1]
        else: 
            # stop processing data rows on first blank cell in A column:
            break
    return chart_details

# test the function on the example files peter provided:
import os
example_file_dir = 'datafiles/example_filters/'
file_list = os.listdir(example_file_dir)
path_list = [os.path.join(example_file_dir,filename) for filename in file_list]

all_the_chart_dataz = []
for filepath in path_list:
    chart_data = read_chart_export(filepath)
    if chart_data != {}:
        all_the_chart_dataz.append(chart_data)
# a list of the information from all the example files
print(all_the_chart_dataz)