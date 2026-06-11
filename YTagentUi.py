import streamlit as st
from ytagent import *


st.set_page_config(
    page_title='youtube video analyser',
)
st.write('welcome to youtube video analyser')

st.title('Youtube video analyser')

@st.cache_resource 
def get_agent():
    return build_agent()
agent=get_agent()
video=st.text_input('enter yt url')
button=st.button('analyse video')

if video and button:
    with st.spinner('analysing video.....'):
        res=agent.run(
            f'analyse the video {video}'
        )
    st.markdown(res.content)