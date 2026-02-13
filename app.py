import streamlit as st
from llm_loader import ask_constitution_question  
from pathlib import Path
from restore_faiss import search_constitution


st.set_page_config(
    page_title="नेपाल संविधान Q&A",
    page_icon="📝",
    layout="wide",
)


st.markdown(
    """
    <style>
    /* Set background color and font */
    body {
        background-color: #f7f7f7;
        font-family: 'Helvetica', sans-serif;
    }
    /* Style the title */
    .stApp h1 {
        color: #1b1b4f;
        font-size: 42px;
        text-align: center;
        margin-top: 10px;
    }
    /* Style user input box */
    .stTextInput>div>div>input {
        height: 50px;
        font-size: 18px;
    }
    /* Style the button */
    .stButton>button {
        background-color: #1b1b4f;
        color: white;
        font-size: 18px;
        padding: 10px 30px;
        border-radius: 10px;
    }
    /* Style the answer box */
    .answer-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        font-size: 18px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


IMAGE_PATH = "asserts/img.png" 
if Path(IMAGE_PATH).exists():
    st.image(IMAGE_PATH, width=700, caption="नेपालको संविधान Q&A")
else:
    st.warning(f"Image not found at {IMAGE_PATH}")


with st.sidebar:
    st.header("🔎 कसरी प्रयोग गर्ने")
    st.write("""
    1. तलको बक्समा तपाईंको प्रश्न लेख्नुहोस्।  
    2. 'जवाफ प्राप्त गर्नुहोस्' बटन थिच्नुहोस्।  
    3. AI ले नेपालको संविधानको आधारमा जवाफ दिनेछ।  
    4. जवाफमा स्रोत र पृष्ठ पनि उल्लेख हुनेछ।  
    """)

user_question = st.text_input("Question:")

# retrieved_context = """
# Page 7: नागरिकको मौलिक अधिकारहरू: 
# - जीवन र स्वतन्त्रताको अधिकार
# - अभिव्यक्ति र विचारको स्वतन्त्रता
# - धर्म, संस्कृति, र भाषा पालनको अधिकार
# - शिक्षा र स्वास्थ्य सेवा प्राप्त गर्ने अधिकार
# - समानता र गैर-भेदभावको अधिकार
# """

# --------------------------
# Answer generation
# --------------------------
if st.button("जवाफ प्राप्त गर्नुहोस्"):
    if not user_question.strip():
        st.warning("कृपया प्रश्न लेख्नुहोस्।")
    else:
        with st.spinner("AI ले उत्तर तयार गर्दैछ... ⏳"):
            try:
                retrieved_chunks = search_constitution(user_question, k=3)
                retrieved_context = "\n".join([docs.page_content for docs in retrieved_chunks])
                answer = ask_constitution_question(retrieved_context, user_question)
                st.write("### उत्तर:")
                st.write(answer)
            except Exception as e:
                st.error(f"उत्तर तयार गर्दा समस्या आयो: {e}")

# --------------------------
# Footer
# --------------------------
st.markdown("---")
st.markdown(
    """
    <p style='text-align:center;'>Made with ❤️ by <b>Loblesh Bhartal</b></p>
    """,
    unsafe_allow_html=True
)
