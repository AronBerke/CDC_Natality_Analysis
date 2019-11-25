def create_column_dictionary(text_file):
    '''
    Takes text file from User Guide to create library identifying locations of each feature.
    Returns pd.DataFrame
    The 'length' feature appears to be inconsistent
    '''

    import re
    import pandas as pd

    with open(text_file, 'r+') as f:
        ug2018 = f.readlines()
        
    # Get field codes and corresponding columns
    field_list = [
        re.search(r'\b[0-9-]+\b\s\b[0-9]+\b\s\b[A-Z0-9_]{2,}\b',i).group() for i in ug2018 if 
        re.search(r'\b[0-9-]+\b\s\b[0-9]+\b\s\b[A-Z0-9_]{2,}\b',i)
    ]

    # Place field numbers into DF
    field_code = pd.DataFrame(columns = ['start','end','length','field'])
    field_code['length'] = [re.split('\s',i)[1] for i in field_list]
    field_code['field'] = [re.split('\s',i)[2] for i in field_list]
    field_range = [re.split('\s',i)[0] for i in field_list]
    field_code['start'] = [re.split('-',i)[0] if re.search('-',i) else i for i in field_range]
    field_code['end'] = [re.split('-',i)[1] if re.search('-',i) else i for i in field_range]

    # Convert entry to numeric
    for i in ['start','end','length']:
        field_code[i] = pd.to_numeric(field_code[i])

    # Find inconsistencies
    for i in range(0,len(field_code)-1):
        if field_code['end'][i] + 1 != field_code['start'][i+1]:
            print('check after: ', i,  field_code['field'][i], field_code['start'][i], '-', field_code['start'][i])
        if field_code['end'][i] - field_code['start'][i] + 1 != field_code['length'][i]:
            print('check range for: ', i,  field_code['field'][i], field_code['start'][i], '-', 
                  field_code['end'][i], field_code['length'][i])





create_column_dictionary('ug2018.txt')

