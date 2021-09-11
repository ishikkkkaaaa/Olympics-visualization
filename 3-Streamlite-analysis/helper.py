def medal_tally(df):
    """ this is medal wise tally, duplicates have been removed because in some games there are group medals """
    medal_tally = df.drop_duplicates(
        subset=['Team','NOC','Games','Year','City','Sport','Event'])
    medal_tally=medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values(
        'Gold', ascending=False).reset_index()

    medal_tally['total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

    #converting all numbers to integers
    medal_tally['Gold']= medal_tally['Gold'].astype('int')
    medal_tally['Silver']= medal_tally['Silver'].astype('int')
    medal_tally['Bronze']= medal_tally['Bronze'].astype('int')
    medal_tally['total']= medal_tally['total'].astype('int')
    
    return medal_tally
