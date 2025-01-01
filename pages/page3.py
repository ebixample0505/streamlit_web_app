import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#データ分析関連
df = pd.read_csv('./data/yokohama_daily_temperature.csv')
st.bar_chart(df['平均気温(℃)'])

#matplotlib
fig, ax = plt.subplots()
ax.plot(df['年月日'], df['平均気温(℃)'])
ax.set_title('横浜の日別平均気温')
st.pyplot(fig)
