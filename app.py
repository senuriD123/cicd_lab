import streamlit as st
from late_fee import calculate_late_fee

st.title("Library Late Fee Calculator")

st.markdown("Calculate the fine for late book returns based on library policy.")

# User input
days_late = st.number_input("Enter number of days late:", min_value=0, max_value=365, value=0, step=1)

# Calculate button
if st.button("Calculate Fine"):
    fee = calculate_late_fee(int(days_late))
    st.success(f"The total late fee is: Rs. {fee}")
