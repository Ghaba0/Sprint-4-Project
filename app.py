import streamlit as st
import pandas as pd 
import plotly.express as px
import altair

vehicles = pd.read_csv('.\\vehicles_us.csv')

vehicles['is_4wd'].fillna(0.0, inplace=True)
vehicles.dropna()
vehicles['price'] = vehicles['price'].astype(float)

# Convert 'date_posted' column to datetime
vehicles['date_posted'] = pd.to_datetime(vehicles['date_posted'])

vehicles['month_posted'] = vehicles['date_posted'].dt.month_name()

# Checkbox to toggle graphs
show_scatter = st.checkbox("Show Odometer vs. Price")
show_price = st.checkbox("Show Distribution of Prices")
show_histogram_month = st.checkbox("Show Month Distribution Histogram")
show_histogram_odometer = st.checkbox("Show Odometer Histogram")


# Alpha slider for scatter plot
alpha_value = st.slider("Select Alpha Value for Scatterplot", min_value=0.1, max_value=1.0, value=0.8, step=0.1)

# Header
st.header('Data Analysis Dashboard')

# Distribution of Price
if show_price:
    fig_price = px.histogram(vehicles, x='price', nbins=50, title='Distribution of Prices',
                                labels={'price': 'Price', 'count': 'Frequency'})
    st.plotly_chart(fig_price)

# Scatter plot for 'odometer' vs. 'price'
if show_scatter:
    fig_scatter = px.scatter(vehicles, x='odometer', y='price', title='Scatter Plot: Odometer vs. Price',
                             labels={'odometer': 'Odometer (Mileage)', 'price': 'Price (In USD)'})
    fig_scatter.update_traces(marker=dict(opacity=alpha_value))
    st.plotly_chart(fig_scatter)

# Plotly Express histogram for the most common month posted
if show_histogram_month:
    fig_month_posted = px.histogram(vehicles, x='month_posted', labels={'month_posted': 'Month'}, title='Distribution of Months Posted')
    st.plotly_chart(fig_month_posted)

# Distribution of Odometer Mileage
if show_histogram_odometer:
    fig_odometer = px.histogram(vehicles, x='odometer', nbins=20, title='Histogram: Distribution of Odometer Mileage',
                                labels={'odometer': 'Odometer (Mileage)', 'count': 'Frequency'})
    st.plotly_chart(fig_odometer)