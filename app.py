import streamlit as st
import pandas as pd


df = pd.read_csv('./data/청소년패스트푸드섭취량.csv')
df.set_index = df['연도']

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)
    st.stop()

st.title('청소년 패스트푸드 섭취량과 비만율 사이의 상관관계')
st.image('./data/data.png')
st.write('현재까지 청소년 패스트푸드 섭취량과 배만율은 계속해서 증가하고 있다.ㄴㄴ')