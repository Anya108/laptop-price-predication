import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np

#import the model
pipe=pickle.load(open('pipe.pkl','rb')) #load the model
df=pickle.load(open('df.pkl','rb')) #import 

page_bg_img  = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url('https://i.pinimg.com/564x/43/dd/e2/43dde2833165fd35eea82358cd844f33.jpg');
background-size: cover;
}
[data-testid = "stHeader"]{
background-color : rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title('Laptop Price Predictor')

#brand of laptop
company=st.selectbox('Brand',df['Company'].unique())

#type of laptop
type=st.selectbox('Type',df['TypeName'].unique())

#Ram
ram=st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

#weight
weight=st.number_input('Weight of laptop')

#touchscreen
touchscreen=st.selectbox('Touchscreen',['No','Yes'])

#ips
ips=st.selectbox('IPS',['No','Yes'])

#screensize
screen_size=st.number_input('Screen Size')

#resolution
resolution=st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
cpu=st.selectbox('CPU',df['Cpu brand'].unique())

#hdd
hdd=st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

#sdd
sdd=st.selectbox('HDD(in GB)',[0,8,128,256,512,1024])

#gpu
gpu=st.selectbox('GPU',df['Gpu brand'].unique())

#os
os=st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    #query 
    ppi=None
    if touchscreen=='Yes':
        touchscreen=1
    else:
        touchscreen=0
        
    if ips=='Yes':
        ips=1
    else:
        ips=0

        
    x_res=int(resolution.split('x')[0])
    y_res=int(resolution.split('x')[1])
    ppi=((x_res**2) + (y_res**2))**0.5/screen_size
    query=np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,sdd,gpu,os])
    
    query=query.reshape(1,12)
    st.title('The predicted price of this configuration is ₹' +str(int(np.exp(pipe.predict(query)[0]))))