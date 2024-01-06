import streamlit as st
import pandas as pd 
import plotly_express as px

vehicles = pd.read_csv('./vehicles_us.csv')

st.title('Vehicle Data Analysis')

# Header with text
st.header('Overview of Vehicle Data')

# Checkbox to toggle visibility of histograms
show_histograms = st.checkbox('Show Histograms')

if show_histograms:
    # Plotly Express histogram for 'price'
    fig_price = px.histogram(vehicles, x='price', nbins=50, title='Distribution of Prices')
    st.plotly_chart(fig_price)

    # Plotly Express histogram for 'model_year'
    fig_model_year = px.histogram(vehicles.dropna(subset=['model_year']), x='model_year', nbins=20, title='Distribution of Model Years')
    st.plotly_chart(fig_model_year)

# Checkbox to toggle visibility of scatter plot
show_scatter_plot = st.checkbox('Show Scatter Plot')

if show_scatter_plot:
    # Plotly Express scatter plot for 'odometer' vs. 'price'
    fig_scatter = px.scatter(vehicles, x='odometer', y='price', title='Scatter Plot: Odometer vs. Price')
    st.plotly_chart(fig_scatter)
