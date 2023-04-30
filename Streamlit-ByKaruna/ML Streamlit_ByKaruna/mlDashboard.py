import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import requests
import time  # to simulate a real time data, time loop
import requests
import pandas as pd
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
from streamlit_card import card
from random import randint





#Loading the saved models
regression_model = pickle.load(open('reg_model.sav', 'rb'))
classif_model = pickle.load(open('classi_model.sav', 'rb'))


st.set_page_config(
    page_icon="💧",
    layout="wide",
    )





#Creating the sidebar for navigation
with st.sidebar:
    selected = option_menu('Water Quality Prdeiction System',
                            ['WQI',
                            'Water Quality Classification', 'Real Time Data'],
                            icons= ['moisture', 'water', 'speedometer2' ],
                            default_index=2)
    

    
url = "https://sheets.googleapis.com/v4/spreadsheets/16Z2M5jiDQVznFXZkekCR5VkAi1rXbph_VD0GTpi-ZLU/values/Data?alt=json&key=AIzaSyANKDwMwwG_TXuUyRX3JqFgY6ylBPfOc0M";
data = requests.get(url).json()
valLen = len(data['values'])

dataset = [data['values'][i]  for i in range(valLen - 101, valLen, 1)]
df = pd.DataFrame(dataset, columns= ['Date', 'Time', 'Temperature', 'TDS(ppm)', 'pH', 'Turbidity', 'Longitude', 'Latitude'])

df["Date"] = pd.to_datetime(df["Date"] + " " + df["Time"], format='%d/%m/%Y %H:%M:%S')
df["Date"] = df['Date'].dt.date
df = df.sort_values('Date')

df ['pH'] = pd.to_numeric(df['pH'], errors='coerce')
df ['TDS(ppm)'] = pd.to_numeric(df['TDS(ppm)'], errors='coerce')
df ['Turbidity'] = pd.to_numeric(df['Turbidity'], errors='coerce')
df ['Temperature'] = pd.to_numeric(df['Temperature'], errors='coerce')

#Data cleaning 
df = df.replace(np.nan, 0, regex=True)


to_display = df.drop_duplicates('Date', keep = 'last')

# print("to_display: ", to_display.shape, "DF: ", df.shape)
# print(to_display)

    
#----------------------------------------------------------Regression Onwards-----------------------------------------------------------#
    
placeholder  = st.empty()

with placeholder.container():
    #WQI Prediction
    if(selected == 'WQI'):

        col1, col2 = st.columns(2, gap = "large")

        #On real time sensor data
        with col1:

            wqi = ''

            #Page Title
            st.subheader("WQI, For Real Time Sensor Data..!")
            st.divider()

            #For blank= line
            st.text("")

            st.metric("pH", value = str(df['pH'].iloc[-1]))
            st.metric("TDS", value = str(df['TDS(ppm)'].iloc[-1]))
            st.metric("Turbidity", value = str(df['Turbidity'].iloc[-1]))
            st.metric("Temperature", value = str(df['Temperature'].iloc[-1]))
        

            try:
                if st.button('Get WQI', 1):
                    wqi = "Water Quality Index(WQI) for Real-time data is: " + str(regression_model.predict([[df['pH'].iloc[-1], df['TDS(ppm)'].iloc[-1], df['Turbidity'].iloc[-1] , df['Temperature'].iloc[-1]]])).replace(']', '').replace('[', '')
                st.success(wqi)
            
            except ValueError as ve:
                st.success("Invalid input")

            
        
        #On user values
        with col2:

            wqi = ''

            #Page Title
            st.subheader("Predict WQI, For User Inputted values..!")
            st.divider()

            #For blank line
            st.text("")
            st.empty()
            ph = st.text_input('Input pH', key = 10)
            tds = st.text_input('Input TDS', key = 20)
            turbidity = st.text_input('Input Turbidity', key = 30)
            temperature = st.text_input('Input Temperature', key = 40)
            

            try:

                #Creating a button for prediction
                if st.button('Get WQI', 2):
                    wqi = "Water Quality Index is: " + str(regression_model.predict([[float(ph), float(tds), float(turbidity), float(temperature)]])).replace(']', '').replace('[', '')
                st.success(wqi)
            
            except ValueError as ve:
                st.success("Input Values")

            

    #----------------------------------------------------------Classification Onwards-----------------------------------------------------------#
        
        
    #water Quality Classification
    if(selected == 'Water Quality Classification'):

        col1, col2 = st.columns(2, gap = "large")

        #On real time sensor data
        with col1:

            wq = ''

            #Page Title
            st.subheader("Classification, For Real Time Sensor Data..!")
            st.divider()

            #For blank line
            st.text("")
            st.metric("pH", value = str(df['pH'].iloc[-1]))
            st.metric("TDS", value = str(df['TDS(ppm)'].iloc[-1]))
            st.metric("Turbidity", value = str(df['Turbidity'].iloc[-1]))
            st.metric("Temperature", value = str(df['Temperature'].iloc[-1]))
        

            
            

            try:

                if st.button('Get Quality', 1):
                    wq = "Water Quality for Real-time Data is: " + str(classif_model.predict([[df['pH'].iloc[-1], df['TDS(ppm)'].iloc[-1], df['Turbidity'].iloc[-1] , df['Temperature'].iloc[-1]]])).replace(']', '').replace('[', '')
                st.success(wq)
            
            except ValueError as ve:
                st.success("Invalid input")

            
        
        #On user values
        with col2:

            wq = ''

            #Page Title
            st.subheader("classification, For User Inputted values..!")
            st.divider()

            #For blank line
            st.text("")
            st.empty()
            pH = st.text_input('Input pH', key = 50)
            tdS = st.text_input('Input TDS', key = 60)
            turbiditY = st.text_input('Input Turbidity', key = 70)
            temperaturE = st.text_input('Input Temperature', key = 80)
            

            try:

                #Creating a button for prediction
                if st.button('Get Quality', 2):
                    wq = "Water Quality is  " + str(classif_model.predict([[float(pH), float(tdS), float(turbiditY), float(temperaturE)]])).replace(']', '').replace('[', '')
                st.success(wq)
            
            except ValueError as ve:
                st.success("Input Values")



    #----------------------------------------------------------Dashboard Onwards-----------------------------------------------------------#
        
    if(selected == 'Real Time Data'):
        #Page Title
        st.header("DashBoard 💻 ")
        col1, col5, col6 = st.columns([5, 4, 4], gap="large")
        with col1:
            st.markdown("#### 💧Current Values")
            col1, col2, col3, col4 = st.columns([1,1,1,1])
            with col1:
                
                st.metric("pH", value = str(df['pH'].iloc[-1]), delta= str(df['pH'].iloc[-1] - df['pH'].iloc[-2]))
            with col2:
                st.metric("TDS(ppm)", value = str(df['TDS(ppm)'].iloc[-1]), delta= str(df['TDS(ppm)'].iloc[-1] - df['TDS(ppm)'].iloc[-2]))
            with col3:
                st.metric("Turbidity", value = str(df['Turbidity'].iloc[-1]), delta= str(df['Turbidity'].iloc[-1] - df['Turbidity'].iloc[-2]))
            with col4: 
                st.metric("Temperature", value = str(df['Temperature'].iloc[-1]), delta= str(df['Temperature'].iloc[-1] - df['Temperature'].iloc[-2]))
            
            st.markdown('#### Detailed Real Time Data')
            st.dataframe(df, height = 800, width = 600)

        with col5:
            st.info("pH Chart")
            st.line_chart(to_display, x = "Date", y = "pH", width = 200, height = 425 )
            st.info("TDS Chart")
            st.line_chart(to_display, x = "Date", y = "TDS(ppm)", width = 200, height = 425 )
        

        with col6:
            st.info("Turbidity Chart")
            st.line_chart(to_display, x = "Date", y = "Turbidity", width = 200, height = 425 )
            st.info("Temperature Chart")
            st.line_chart(to_display, x = "Date", y = "Temperature", width = 200, height = 425 )
        
    time.sleep(2)

        # Date_filter = st.selectbox('Filter Data with Date',pd.unique(df["Date"]))
        # df = df[df["Date"] == Date_filter]
        # st.dataframe(df)

        




  

