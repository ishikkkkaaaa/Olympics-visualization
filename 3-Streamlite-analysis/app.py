import streamlit as st
import pandas as pd
import preprocessor
import helper

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)

user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally', 'Overall Analysis',
     'Country-wise Analytics', 'Athlete wise Analysis')
)

#st.dataframe(df) 

if user_menu == 'Medal Tally':
    medal_tally = helper.medal_tally(df)
    st.dataframe(medal_tally)
