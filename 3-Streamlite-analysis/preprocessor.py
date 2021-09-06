import pandas as pandas

df=pd_csv('atlete.events.csv')
region_df=pd.read_csv('noc_regions.csv')

def preprocess():
    global df,region_df
    #filtering for summer olympics
    df=df[df['Season']=='Summer']
    #merge region and and noc
    df=df.merge(region_df,on='NOC',how='left')
    #drop useless duplicates
    df=df.drop_duplicates(inplace=True)
    #one hot encoding for medals
    df.pd.cancat([df,pd.get_dummies(df['Medal'])]),axis=1)
    return df