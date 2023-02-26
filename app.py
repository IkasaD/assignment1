import streamlit as st


st.title("Hi!!")
st.header("Welcome to my Page")
st.write("Want to see magic click the button")
if st.button("button"):
    st.snow()
    st.balloons()
    st.write(":100:")
    st.write("Check the dashboards")
    video_file = open('bear.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    






