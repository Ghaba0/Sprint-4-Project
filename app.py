import streamlit as st
import pandas as pd
import altair as alt

vehicles = pd.read_csv('vehicles_us.csv')

vehicles['is_4wd'].fillna(0.0, inplace=True)
vehicles.dropna()
vehicles['price'] = vehicles['price'].astype(float)

# Convert 'date_posted' column to datetime
vehicles['date_posted'] = pd.to_datetime(vehicles['date_posted'])

vehicles['month_posted'] = vehicles['date_posted'].dt.month_name()

# Extract the first word from each entry in the 'model' column
vehicles['brand'] = vehicles['model'].str.split().str[0]

# Checkbox to toggle graphs
show_scatter = st.checkbox("Show Odometer vs. Price")
show_price = st.checkbox("Show Distribution of Prices")
show_histogram_month = st.checkbox("Show Month Distribution Histogram")
show_brand_count = st.checkbox("Show Vehicle Count by Brand")

# Alpha slider for scatter plot
alpha_value = st.slider("Select Alpha Value for Scatterplot", min_value=0.1, max_value=1.0, value=0.8, step=0.1)

# Header
st.header('Data Analysis Dashboard')

# Distribution of Price
if show_price:
    fig_price = alt.Chart(vehicles).mark_bar().encode(
        alt.X('price', bin=alt.Bin(maxbins=50), title='Price'),
        alt.Y('count()', title='Frequency'),
        tooltip=['count()']
    ).properties(
        title='Distribution of Prices'
    )
    st.altair_chart(fig_price, use_container_width=True)

# Scatter plot for 'odometer' vs. 'price'
if show_scatter:
    fig_scatter = alt.Chart(vehicles).mark_circle().encode(
        alt.X('odometer', title='Odometer (Mileage)'),
        alt.Y('price', title='Price (In USD)'),
        opacity=alt.value(alpha_value)
    ).properties(
        title='Scatter Plot: Odometer vs. Price'
    )
    st.altair_chart(fig_scatter, use_container_width=True)

# Altair histogram for the most common month posted
if show_histogram_month:
    fig_month_posted = alt.Chart(vehicles).mark_bar().encode(
        alt.X('month_posted:N', title='Month'),
        alt.Y('count()', title='Frequency'),
        tooltip=['count()']
    ).properties(
        title='Distribution of Months Posted'
    )
    st.altair_chart(fig_month_posted, use_container_width=True)

# Count of vehicles by brand using Altair (Bar Chart)
if show_brand_count:
    fig_brand_count = alt.Chart(vehicles).mark_bar().encode(
        alt.X('brand:N', title='Brand'),
        alt.Y('count()', title='Number of Vehicles'),
        tooltip=['count()']
    ).properties(
        title='Count of Vehicles by Brand'
    )
    st.altair_chart(fig_brand_count, use_container_width=True)
