import streamlit as st

st.title("streamlit First")

st.header("This is header")
st.subheader("This is sub-header")

st.text("hello Dhruv")

st.markdown("### This is markdown")

st.success("successful")
st.info("information")
st.warning("This is Warning")
st.error("Error")
st.exception("Name error")

st.help(list)

st.write("text with write")
st.write(range(10))

from PIL import Image
import cv2
img_cv=cv2.imread("image1.jpg")
st.image(img_cv)


img = Image.open("image1.jpg")
st.image(img,width=600,caption="Dog")

vid=open("6.mp4","rb").read()
st.video(vid)


#widget
if st.checkbox("show/Hide"):
    st.text("showing or Hinding Widget")


status=st.radio("Whatis Your Status",('Activate','Inactive'))
if status=="Activate":
    st.warning("You are Active")
else:
    st.warning("Inactivte,Activate")


occupation=st.selectbox("what is your occupation",('programmer','Data scientist','Analyst'))
st.write("you selected this option:",occupation)


mul_select=st.multiselect("select multiple",("A","B","C","D","F"))
st.write("you have selected",len(mul_select),"option")


level=st.slider("what is your level",1,5)

st.button("simple Button")
if st.button("click for cool"):
    st.write("cool")


name=st.text_input("Enter Your Name:")
if st.button('submit'):
    result=name.title()
    st.success(result)


message=st.text_area("Enter Your Message")
if st.button("Submit"):
    result=message.title()
    st.success(result)

import  datetime
today=st.date_input("Today is",datetime.datetime.now())



with st.echo():
    import pandas as pd
    df=pd.DataFrame()

import time
my_bar =st.progress(0)
for p in range(10):
    my_bar.progress(p+1)

with st.spinner("Waiting.."):
    time.sleep(5)
st.success("Finished")


st.balloons()

st.sidebar.header("ABout")
st.sidebar.text("This is streamlit Tut")

#function
@st.cache
def run_fxn():
    return range(100)

import matplotlib
st.write(run_fxn())

st.pyplot()

st.dataframe()