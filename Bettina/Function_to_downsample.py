def downsample_df (df):

    '''
    Remove undefined information on NICU admissions (AB_NICU == 'U'),
    create a binary target vector, and create a "balanced" dataframe
    with all NICU admissions and matching numbers of randomly selected non-NICU admissions.
    '''

    import pandas as pd
    import numpy as np

    # remove unknown class from df
    df_no_unknown = df[df['AB_NICU'].isin(['Y', 'N'])]

    # Create binary target vector, NICU = yes classified as class 0
    df_y_n = np.where((df_no_unknown['AB_NICU'] == 'Y'), 0, 1)

    # Get indicies of each class' observations
    index_class0 = np.where(df_y_n == 0)[0]
    index_class1 = np.where(df_y_n == 1)[0]

    # Get numbers of observations in class 0
    n_class0 = len(index_class0)

    # Randomly sample the same number of observations from class 1 as in class 0, without replacement
    np.random.seed(0)
    index_class1_downsampled = np.random.choice(index_class1, size=n_class0, replace=False)

    # Create dataframes for NICU and downsampled non-NICU
    df_NICU = df.iloc[index_class0]
    df_adj_NONICU = df.iloc[index_class1_downsampled]

    # Append into 1 dataframe
    df_downsampled = df_NICU.append(df_adj_NONICU)

    return df_downsampled
