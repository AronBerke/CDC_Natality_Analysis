def add_random_column_to_df (dataframe):
    import random
    mylist = []
    for i in range(0, dataframe.shape[0]):
        x = random.randint(1,1000)
        mylist.append(x)
    dataframe['RANDOM'] = mylist

    return dataframe
