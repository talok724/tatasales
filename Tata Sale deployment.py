import streamlit as st
import pickle

pipe = pickle.load(open("pipeline.pkl","rb"))
X = pickle.load(open("X.pkl","rb"))