
import streamlit as s
import pandas

s.title("test")
s.header("The header")
s.text("Lorem ipsum dolor sin amet.")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
