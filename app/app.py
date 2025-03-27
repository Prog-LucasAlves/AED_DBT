import streamlit as st
import pandas as pd
import dbt_utils
import sql_utils

st.set_page_config(page_title="DBT & SQL App", layout="wide")

tab1, tab2 = st.tabs([["⚙️ DBT Executor", "📊 SQL Query"]])
