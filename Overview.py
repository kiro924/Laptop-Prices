
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide',
                  page_title='Laptop Prices'
                   )

df=pd.read_csv('cleaned data')

st.markdown(
    f"<h3 style='color: purple; font-weight: bold; font-size: 40px; text-align: center;'>Laptop Prices Overview</h3>", 
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"<h3 style='color: black;'>Number Of Brands: {df['Brand'].nunique()}</h3>", unsafe_allow_html=True)

col2.markdown(f"<h3 style='color: black;'>Top Ram Size: {df['RAM (GB)'].max()}</h3>", unsafe_allow_html=True)

col3.markdown(f"<h3 style='color: black;'>Top Battery Life: {df['Battery Life (hours)'].max()}</h3>", unsafe_allow_html=True)

col4.markdown(f"<h3 style='color: black;'>Highest Storage(GB): {df['Storage (GB)'].max()}</h3>", unsafe_allow_html=True)


col1, col2, col3=st.columns([4,4,4])

brand_sales=df.groupby('Brand')['Price ($)'].sum().astype(int).sort_values(ascending=False).round()
fig1 = go.Figure()
fig1.add_trace(go.Bar(
    x=brand_sales.index,  
    y=brand_sales.values,    
    marker=dict(color=px.colors.qualitative.Bold[1])  
))

fig1.update_layout(
    title="total sales for each brand",
    xaxis_title="Brand",
    yaxis_title="Sales"
)
col1.plotly_chart(fig1)


processor_sales=df.groupby('Processor')['Price ($)'].sum().astype(int).sort_values(ascending=False).round()
fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=processor_sales.index,  
    y=processor_sales.values,    
    marker=dict(color=px.colors.qualitative.Bold[1])  
))

fig2.update_layout(
    title="total sales for each processor".title(),
    xaxis_title="Processor",
    yaxis_title="Sales"
)
col2.plotly_chart(fig2)


storage_sales=df.groupby('Storage (GB)')['Price ($)'].sum().astype(int).sort_values(ascending=False).round()
fig3 = go.Figure()
fig3.add_trace(go.Bar(
    x=storage_sales.index,  
    y=storage_sales.values,    
    marker=dict(color=px.colors.qualitative.Bold[1])  
))

fig3.update_layout(
    title="total sales for each storage".title(),
    xaxis_title="Storage(GB)",
    yaxis_title="Sales"
)
col3.plotly_chart(fig3)
