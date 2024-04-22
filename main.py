import streamlit as st
from streamlit_elements import elements, mui

def app():
    with elements():
        with mui.Box(sx={"width": 300, "height": 300, "resize": "both", "overflow": "auto", "border": "1px solid grey", "padding": 2}):
            mui.Typography("Hello, world!", variant="h6")

if __name__ == "__main__":
    app()