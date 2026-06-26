import streamlit as st
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

st.set_page_config(page_title="Funnel Dashboard", layout="wide")
st.title("Funnel Dashboard")

NOTEBOOK_FILE = "End-to-End-Funnel-Drop-Off-Returns-Retention-Analysis-for-a-Fashion-E-commerce.ipynb"

with open(NOTEBOOK_FILE) as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
ep.preprocess(nb)

st.success("Notebook executed successfully")
