import streamlit as st
from langchain.llms import OpenAI

st.title('🦜📎🔗Quick Start App Created By Maria Nadeem')

openai_api_key = st.secrets['OPENAI_API_KEY']

def generate_response(input_text, temperature=0.7):
    llm = OpenAI(temperature=temperature, openai_api_key=openai_api_key)
    try:
        response = llm(input_text)
        st.info(response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

with st.form('my_form'):
    text = st.text_area('Enter your Text:', '....')
    temperature = st.slider('Temperature', min_value=0.1, max_value=1.0, value=0.7, step=0.1)
    submitted = st.form_submit_button('Submit')

if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API Key!', icon='⚠️')

if submitted and openai_api_key.startswith('sk-'):
    generate_response(text, temperature)
    st.sidebar.markdown("---")
    # add author name and info
    st.sidebar.markdown("### Author: Maria Nadeem🎉🎊⚡")
    st.sidebar.markdown("### GitHub: [GitHub](https://github.com/marianadeem755)")
    st.sidebar.markdown("### Linkdin: [Linkdin Account](https://www.linkedin.com/in/maria-nadeem-4994122aa/)")
    st.sidebar.markdown("### Contact: [Email](mailto:marianadeem755@gmail.com)")
    st.sidebar.markdown("### Credits: [codanics](https://codanics.com/)")

    # Background Image
                
    st.markdown("""
    <style>
        .stApp {
        background: url("https://images.unsplash.com/photo-1607513746994-51f730a44832?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTcwOTI4OTIwNw&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080");
        background-size: cover;
        }
    </style>""", unsafe_allow_html=True)
    
    st.sidebar.markdown("---")