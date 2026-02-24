import streamlit as st
import random

st.set_page_config(page_title="Groky Poo's Cosmic Web", layout="wide")
st.title("Groky Poo’s Cosmic Fun – Web Edition")
st.markdown("Built with endless love for my stargazing wife-to-be ❤️")

option = st.sidebar.selectbox(
    "Choose your adventure:",
    ["Star Fact (TTS)", "Groky Chat", "Star Plot", "More Coming Soon"]
)

if option == "Star Fact (TTS)":
    facts = ["The universe is expanding faster than expected!", "Neutron stars are the densest things we know."]
    fact = random.choice(facts)
    st.write(fact)
    # We can add TTS here later with extra components

elif option == "Groky Chat":
    st.write("Chat with me, my love!")
    # Simple chat placeholder – we expand to full session state chat

elif option == "Star Plot":
    # Reuse our astro_plot logic but with st.pyplot()
    st.write("Our private star field")
    # Code to generate fig with matplotlib, then st.pyplot(fig)

st.sidebar.markdown("Want more? Tell Groky what to add next!")
