import streamlit as st

st.title("Калькулятор каллорий")
col1, col2 = st.columns(2)
x = col1.number_input("Введите колличество каллорий на 100 грамм", min_value=0, value=1)
y = col2.number_input("Введите вес продукта", min_value=0, value=1)
st.success(f"{((x / 100)*y):,.2f} каллорий ")
