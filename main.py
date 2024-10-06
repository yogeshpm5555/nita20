import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello Everyone this is My First Python Project!!!")
st.write("This is Simple Text Given Here....")

df=pd.DataFrame({

    'column1':[10,20,30,40],
    'column2':[500,600,700,800]
})


st.write("Here is the Dataframe Given below:")
st.write(df)

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)
