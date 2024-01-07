import streamlit as st
import pandas as pd 
import plotly_express as px

vehicles = pd.read_csv('./vehicles_us.csv')

# Checkbox to toggle behavior
show_histogram = st.checkbox("Show Histogram")

# Alpha slider for scatter plot
alpha_value = st.slider("Select Alpha Value", min_value=0.1, max_value=1.0, value=0.8, step=0.1)

# Header
st.header("Data Analysis Dashboard")

# Histogram for 'price'
if show_histogram:
    fig_price = px.histogram(vehicles, x='price', nbins=50, title='Distribution of Prices',
                             labels={'price': 'Price', 'count': 'Frequency'})
    st.plotly_chart(fig_price)

# Scatter plot for 'odometer' vs. 'price' with alpha slider
fig_scatter = px.scatter(vehicles, x='odometer', y='price', title='Scatter Plot: Odometer vs. Price',
                         labels={'odometer': 'Odometer', 'price': 'Price'})
fig_scatter.update_traces(marker=dict(opacity=alpha_value))
st.plotly_chart(fig_scatter)

# Plotly Express histogram for the most common month posted
fig_month_posted = px.histogram(vehicles, x='month_posted', title='Distribution of Months Posted')
st.plotly_chart(fig_month_posted)

# Distribution of Odometer Mileage
fig_odometer = px.histogram(vehicles, x='odometer', nbins=20, title='Histogram: Distribution of Odometer Mileage',
                            labels={'odometer': 'Odometer (Mileage)', 'count': 'Frequency'})
st.plotly_chart(fig_odometer)
