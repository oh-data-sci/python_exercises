# the columns of interest is the 'INSPECTION_DATE' and 'APPROVED_DATE'
# inspection by eye gives us the datetime format descriptor
format_descriptor = '%m/%d/%Y %I:%M:%S %p'

columns = ['INSPECTION_DATE', 'APPROVED_DATE']

for column in columns:
    print('transcoding the', column, 'column')
    for date_str in rodent_df[column]:
        inspection_datetime = datetime.datetime.strptime(date_str, format_descriptor)
        print(date_str, '-->', inspection_datetime) # compare before and after
