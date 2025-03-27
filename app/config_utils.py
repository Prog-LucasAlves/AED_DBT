import streamlit as st
from sqlalchemy import create_engine


def create_db_engine():
    db_url = st.secrets["postgresql"]['URL']
    return create_engine(db_url)


engine = create_db_engine()
