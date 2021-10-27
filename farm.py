import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import plotly.express as px


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('sigma-hydra-330209-caffce86067c.json',scope)

# authorize the clientsheet 
client = gspread.authorize(creds)
sheet = client.open('kulashekar project')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)
print(sheet_instance.col_count)
sheet_instance.cell(col=3,row=2)
records_data = sheet_instance.get_all_records()
records_df = pd.DataFrame.from_dict(records_data)
records_df["average"]=records_df.mean(axis=1)
print(records_df.head())

st.title("Daily progress tracker")
st.markdown("The dashboard will visualize the daily performance of candidates")

st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Enter your name here")
user_input = st.sidebar.text_input("Enter name ")

if user_input:
    
    st.bar_chart(records_df[[user_input, 'average']])
    st.text("x-axis=days")
    st.line_chart(records_df[[user_input, 'average']])
    st.text("x-axis=days")
    st.area_chart(records_df[[user_input, 'average']])
    st.text("x-axis=days")

g=0
h=""
for i in records_df.columns:
    me=sum(records_df[i])
    if me>g:
        h=i
        g=me
st.markdown("###coder of the day"+" :"+h)


    
    
    

    

    
    
    

