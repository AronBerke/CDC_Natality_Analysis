
def targetchoice(column,dataframe):
    '''
    Takes a column and a dataframe, returns four values for;
    x_train, X_test, y_train, and y_test
    '''
    #Cutting the data and target dataframes
    sample_data = dataframe.loc[:, dsample.columns != column ]
    sample_target = dataframe.loc[:,column]
    
    #assigning to variables
    X_train, X_test, y_train, y_test = train_test_split(sample_data, sample_target, test_size=0.2, random_state=0)
    
    #appending to a list to return for multi-assignment
    varlist = []
    varlist.append(X_train)
    varlist.append(X_test)
    varlist.append(y_train)
    varlist.append(y_test)
    return varlist

#format is "X_train, X_test, y_train, y_test = targetchoice()"