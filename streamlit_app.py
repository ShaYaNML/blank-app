import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

st.markdown("""
    <style>
    .calculator {background:#222;padding:20px;border-radius:15px;width:370px;margin:auto;}
    .screen {background:#111;color:#0f0;font-size:2rem;text-align:right;padding:10px 20px;border-radius:8px;margin-bottom:20px;}
    button.cal-btn {font-size:1.2rem;margin:5px;padding:18px 28px;border-radius:8px;border:none;background:#333;color:#fff;cursor:pointer;}
    button.cal-btn:hover {background:#444;}
    </style>
""", unsafe_allow_html=True)

def calc(expr):
    try:
        # Replace mathematical function names with the math module equivalents
        expr = expr.replace('^', '**')
        for fn in ['sin','cos','tan','log','sqrt','exp','fabs','asin','acos','atan']:
            expr = expr.replace(fn, f'math.{fn}')
        result = eval(expr, {'math': math, '__builtins__': None})
        return result
    except Exception:
        return 'Error'

st.markdown('<div class="calculator">', unsafe_allow_html=True)

if 'input' not in st.session_state:
    st.session_state.input = ""
if 'result' not in st.session_state:
    st.session_state.result = ""

def button_click(label):
    if label == "C":
        st.session_state.input = ""
        st.session_state.result = ""
    elif label == "=":
        st.session_state.result = calc(st.session_state.input)
    else:
        st.session_state.input += label

# Display screen
screen_content = st.session_state.input if st.session_state.result == "" else str(st.session_state.result)
st.markdown(f'<div class="screen">{screen_content}</div>', unsafe_allow_html=True)

# Calculator button layout
buttons = [
    ["7", "8", "9", "/", "sin("],
    ["4", "5", "6", "*", "cos("],
    ["1", "2", "3", "-", "tan("],
    ["0", ".", "(", ")", "+"],
    ["log(", "sqrt(", "exp(", "^", "C"],
    ["=",]
]

for row in buttons:
    cols = st.columns(len(row))
    for i, label in enumerate(row):
        with cols[i]:
            st.button(label, key=label, on_click=button_click, args=(label,), use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

st.info("Functions: sin, cos, tan, log (natural log), sqrt, exp, ^ (power). Example: sin(3.14/2)+log(10

