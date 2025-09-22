import streamlit as st
st.header("hello world")
st.image("NOOB%21.webp")
st.image("Taco.webp")
st.audio("i_r_tacos.mp3", format="audio/mpeg")
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", "5.772 K", "100000000 °")
col2.metric("vento", "9999999 al/s", "-8%")
col3.metric("umidade", "100000000000%", "1000%")