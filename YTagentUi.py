import streamlit as st
from ytagent import *


st.set_page_config(
    page_title='youtube video analyser',
)

st.title('Youtube video analyser')

@st.cache_resource 
def get_agent():
    return build_agent()
agent=get_agent()
video=st.text_input('Enter Youtube URL')
button=st.button('Analyse video')

if video and button:
    with st.spinner('Analysing video.....'):
        res=agent.run(
            f'analyse the video {video}'
        )
    st.markdown(res.content)