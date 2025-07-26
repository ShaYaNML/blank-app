import streamlit as st

st.title("Basic Arithmetic Calculator")

# User inputs
num1 = st.number_input("Enter first number:", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number:", value=0.0, format="%.2f")

operation = st.selectbox(
    "Choose operation:",
    ("Add", "Subtract", "Multiply", "Divide")
)

result = None

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"

    st.write(f"Result: {result}")
