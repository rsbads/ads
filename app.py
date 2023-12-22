import streamlit as st
from plot.interactive import plot_line_i

st.title('Stock Price App')

st.sidebar.header('User: Input')
symbol = st.sidebar.text_input('Escolha um ativo:', 'AAPL')

fig= plot_line_i(symbol)
st.plotly_chart(fig)