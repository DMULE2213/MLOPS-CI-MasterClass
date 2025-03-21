import streamlit as st


# streamlit UI
st.title('Power Calculater')
st.write('Enter the number to calculate its square, cube and fifth power')



# get user input
n = st.number_input('Enter an integer', value =1, step = 1)

# calculate result
square = n ** 2
cube =   n ** 3
fifth = n ** 5


# display result
st.write(f'The square of (n) is : {square}')
st.write(f'the cube of (n) is : {cube}')
st.write(f'the fifth of (n) is :{fifth}')