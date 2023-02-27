import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import numpy as np
import os


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "Resources")

option = st.selectbox(
         'Choose DataSet',
        ('iris','titanic','tips'))
if option == "iris":
    IMAGE_PATH = os.path.join(dir_of_interest, "images", "iris.jpg")
    DATA_PATH = os.path.join(dir_of_interest, "data", "iris.csv")
    st.title("Dashboard - Iris Data")
    img = image.imread(IMAGE_PATH)
    st.image(img)

    df = pd.read_csv(DATA_PATH)
    st.dataframe(df)

    species = st.selectbox("Select the Species:", df['Species'].unique())

    type = st.radio(
    "Choose one ",
    ('SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm','PetalWidthCm'))
    
    tab1, tab2 = st.tabs(["2D Plots","3D Plots"])

    with tab1:
        col1, col2, col3 = st.columns(3)


        def vs(type):
            fig_1 = px.histogram(df[df['Species'] == species], x=type,title="Histogram")
            col1.plotly_chart(fig_1, use_container_width=True)
        

            fig_2 = px.box(df[df['Species'] == species], y=type,title="Box Plot")
            col2.plotly_chart(fig_2, use_container_width=True)

            fig1 = px.scatter(df[df["Species"]== species], y= type,title="Scatter Plot")
            col3.plotly_chart(fig1, use_container_width=True)

        vs(type)
        cc = st
        fg = px.scatter(df, x=df['SepalWidthCm'], y=df['SepalLengthCm'], color=df["Species"],size=df['PetalLengthCm'], hover_data=['PetalWidthCm'])
        cc.plotly_chart(fg)
    with tab2:
        cl1 = st
        fig = px.scatter_3d(df, x=df['SepalLengthCm'], y=df['SepalWidthCm'], z=df['PetalWidthCm'],color=df['Species'])
        cl1.plotly_chart(fig)




elif option == "titanic" :
    st.title("Dashboard - Titanic Data")
    IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
    DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

    img = image.imread(IMAGE_PATH)
    st.image(img)

    df = pd.read_csv(DATA_PATH)
    st.dataframe(df)
    survival_rate = df.groupby(['sex']).mean()[['survived']]
    male_rate = survival_rate.loc['male']
    female_rate = survival_rate.loc['female']
    sr = pd.DataFrame(survival_rate)
    
    col1 = st

    fig_2 = px.histogram(df["sex"].value_counts().values, x=df['sex'],title="Total Passengers Gender wise")
    col1.plotly_chart(fig_2, use_container_width=True)

    st.write(sr)
    fig = px.pie(sr, values='survived', names=df["sex"].unique(),title="Survival Rate")
    col1.plotly_chart(fig, use_container_width=True)

    

else :
    st.title("Dashboard - Tips Data")
    IMAGE_PATH = os.path.join(dir_of_interest, "images", "tips.jpg")
    DATA_PATH = os.path.join(dir_of_interest, "data", "tips.csv")

    img = image.imread(IMAGE_PATH)
    st.image(img)

    df = pd.read_csv(DATA_PATH)
    st.dataframe(df)
    st.subheader("Restuarent Sales percentage per day")
    col = st
    fig = px.pie(df, values='tip', names='day')
    col.plotly_chart(fig, use_container_width=True)
    
    col1, col2 =st.columns(2)
    fig_1 = px.histogram(df["total_bill"].value_counts().index, x=df['day'],title="Customers per day")
    col1.plotly_chart(fig_1, use_container_width=True)

    fig_2 = px.histogram(df["total_bill"].value_counts().values, x=df['sex'],title="Customers Gender wise")
    col2.plotly_chart(fig_2, use_container_width=True)



    