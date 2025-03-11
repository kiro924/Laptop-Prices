
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide',
                  page_title='Charts'
                  )

df=pd.read_csv('cleaned data')

tab1, tab2= st.tabs(['Bi Variate Analysis','Multi Variate Analysis'])

with tab1:

    col1, col2=st.columns([4,4])
    
    brands=df.groupby('Brand')['Price ($)'].sum().astype(int).sort_values(ascending=False).round()
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=brands.index,  
        y=brands.values,
        marker=dict(color=px.colors.qualitative.Vivid[2])  
    ))
    
    fig1.update_layout(
        title="total sales for each brand".title(),
        xaxis_title="Brand",
        yaxis_title="Sales"
    )
    col1.plotly_chart(fig1)

    Processors=df.groupby('Processor')['Price ($)'].sum().astype(int).sort_values(ascending=False).round()
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=Processors.index,  
        y=Processors.values,
        marker=dict(color=px.colors.qualitative.Vivid[7])  
    ))
    
    fig2.update_layout(
        title="total sales for each processor".title(),
        xaxis_title="Processor",
        yaxis_title="Sales"
    )
    col2.plotly_chart(fig2)
    
    
    Storages=df.groupby('Storage (GB)')['Price ($)'].sum().astype(int).sort_values(ascending=False).round()
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(
        x=Storages.index,  
        y=Storages.values,
        marker=dict(color=px.colors.qualitative.Vivid[2])  
    ))
    
    fig3.update_layout(
        title="total sales for each Storage (GB)".title(),
        xaxis_title="Storage",
        yaxis_title="Sales"
    )
    col1.plotly_chart(fig3)
    
    
    gpu=df.groupby('GPU')['Price ($)'].sum().astype(int).sort_values(ascending=False).round()
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(
        x=gpu.index,  
        y=gpu.values,
        marker=dict(color=px.colors.qualitative.Vivid[7])  
    ))
    
    fig4.update_layout(
        title="total sales for each gpu".title(),
        xaxis_title="Gpu",
        yaxis_title="Sales"
    )
    col2.plotly_chart(fig4)
    
    Operating_Systems=df.groupby('Operating System')['Price ($)'].sum().astype(int).sort_values(ascending=False).round()
    fig5 = go.Figure()
    fig5.add_trace(go.Bar(
        x=Operating_Systems.index,  
        y=Operating_Systems.values,
        marker=dict(color=px.colors.qualitative.Vivid[2])  
    ))
    
    fig5.update_layout(
        title="total sales for each gpu".title(),
        xaxis_title="Gpu",
        yaxis_title="Sales"
    )
    col2.plotly_chart(fig5)
    


with tab2:
    col1, col2=st.columns([2,2])

    t_s_o_s_b=df.groupby(['Brand','Operating System'])['Price ($)'].sum().reset_index().sort_values(ascending=False, by='Price ($)')   
    fig1 = px.bar(t_s_o_s_b, 
             x='Brand', 
             y='Price ($)', 
             color='Operating System',  
             title="total sales for each brand and operating system".title(),
             color_discrete_sequence=px.colors.qualitative.Vivid_r
              )

    col1.plotly_chart(fig1)

    t_s_o_s_s=df.groupby(['Storage (GB)','Operating System'])['Price ($)'].sum().reset_index().sort_values(ascending=False, by='Price ($)')
    fig2 = px.bar(t_s_o_s_s, 
             x='Storage (GB)', 
             y='Price ($)', 
             color='Operating System',  
             title="total sales for each storage and operating system".title(),
             color_discrete_sequence=px.colors.qualitative.Vivid_r
              )

    col2.plotly_chart(fig2)


    t_s_o_s_r=df.groupby(['RAM (GB)','Operating System'])['Price ($)'].sum().reset_index().sort_values(ascending=False, by='Price ($)')
    fig3 = px.bar(t_s_o_s_r, 
             x='RAM (GB)', 
             y='Price ($)', 
             color='Operating System',  
             title="total sales for each ram and operating system".title(),
             color_discrete_sequence=px.colors.qualitative.Vivid_r
              )


    col1.plotly_chart(fig3)

    t_s_o_s_p=df.groupby(['Processor','Operating System'])['Price ($)'].sum().reset_index().sort_values(ascending=False, by='Price ($)')

    fig4 = px.bar(t_s_o_s_p, 
             x='Processor', 
             y='Price ($)', 
             color='Operating System',  
             title="total sales for each storage and operating system".title(),
             color_discrete_sequence=px.colors.qualitative.Vivid_r
              )


    col2.plotly_chart(fig4)
