import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from path import Path
import base64


st.set_page_config(page_title="Nat Fernelius", page_icon=":herb:", layout="wide")


def img_to_bytes(img_path):
    img_bytes = Path("avatar.jpg").read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

header_html = "<img src='data:image/jpg;base64,{}' class='center' width='50%' height='50%' style='display:block;margin-left:auto;margin-right:auto; width:50%; border-radius: 50%;'>".format(
    img_to_bytes("avatar.png"))

# URLS

GitHub = "https://github.com/ferneliusn"
LinkedIn = "https://www.linkedin.com/in/nat-fernelius-520666270/"

#Other Assets
CV = "https://github.com/ferneliusn/CV/blob/main/resume_07-2023.pdf"


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hello, I am Nat Fernelius! :wave:")
        st.title("I am an AI developer and data scientist based out of New York City.")
        st.write("I am a current staff member on EY's Tax, Technology, and Tranformation Alwin team. I’m interested in artificial intelligence, natural language processing, Python development, and econometrics. I’m a graduate of the The University of Texas at Austin, holding degrees in Economics and Plan II while also having completed a certificate in Scientific Computation and Data Science. I’m looking to collaborate on cutting-edge machine learning projects and meet other professionals in the field.")
        st.write("---")
        st.write(" ")
        st.write(" ")
        with st.container():
            left, center, right = st.columns(3)
            with left:
                st.markdown(f'''
                    <a href={GitHub}><button style="border-radius:12px;background-color:#aecaae;height:150px;width:150px;font-size:35px;color:black">GitHub</button></a>
                    ''',
                    unsafe_allow_html=True)
            with center:
                st.markdown(f'''
                    <a href={LinkedIn}><button style="border-radius:12px;background-color:#aecaae;height:150px;width:150px;font-size:35px;color:black">LinkedIn</button></a>
                    ''',
                    unsafe_allow_html=True)
            with right:
                st.markdown(f'''
                    <a href={CV}><button id="CV" style="border-radius:12px;background-color:#aecaae;height:150px;width:150px;font-size:35px;color:black">CV</button></a>
                    ''',
                    unsafe_allow_html=True)

    with right_column:
        st.markdown(header_html, unsafe_allow_html=True,)

#Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")

lottie_brain = load_lottieurl("https://lottie.host/5e4c563c-a78d-47d4-82f6-e53c47209857/BFiTWRlwAD.json")

st.write("---")
st.header("Technical Skills")
st.write("---")
with st.container():
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.write(
                """
                ### General Python Development
                    - NumPy
                    - Pandas
                    - Scikitlearn
                    - Matplotlib
                    - Streamlit    
                ### AI/Machine Learning Libraries
                    - Tensorflow
                    - Pytorch
                    - Keras
                    - OpenAI API and LLM App Development
                    - Microsoft Semantic Kernel
                """
            )
    with middle_column:
       st.write( 
        """
        ### Cloud Services
            - Microsoft Azure
        ### Other Languages
            - git
            - Bash 
            - C++
            - Julia
            - Fortran
            - R
            - HTML
            - CSS
        ### Soft Skills
            - Public Speaking
            - Leadership
            - Technical Writing
        """
       )
    with right_column:
        st_lottie(lottie_brain, height=500, key='brain')
st.write("---")
st.header("Projects")
st.write("---")
with st.container():
    left, center, right, far_right = st.columns(4)
    with left:
        st.markdown(f'''
            <a href={"https://github.com/ferneliusn/sentiment_unemployment"}><button type="button" id="Sentiment" style="border-radius:12px;background-color:#aecaae;height:150px;width:400px;font-size:30px;color:black">Prediction of Unemployment with Sentiment Analysis</button></a>
            ''',
            unsafe_allow_html=True)
    with center:
        st.markdown(f'''
            <a href={"https://github.com/kytola/CleanAirbnb"}><button style="border-radius:12px;background-color:#aecaae;height:150px;width:400px;font-size:30px;color:black">Airbnb Web Scraping and Data Analysis Pipeline</button></a>
            ''',
            unsafe_allow_html=True)
    with right:
        st.markdown(f'''
            <a href={"https://github.com/ferneliusn/Authored-Papers"}><button style="border-radius:12px;background-color:#aecaae;height:150px;width: 400px;font-size:30px;color:black">Authored Papers</button></a>
            ''',
            unsafe_allow_html=True)
    with far_right:
        st.markdown(f'''
            <a href={"ferneliusn.github.io"}><button style="border-radius:12px;background-color:#aecaae;height:150px;width:400px;font-size:30px;color:black">This Website</button></a>
            ''',
            unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.header("Contact Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/nataliafernelius@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form> 
    """

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()