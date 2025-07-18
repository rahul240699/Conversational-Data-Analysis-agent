import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path

# Optional: For vector store/RAG
# from langchain.vectorstores import FAISS
# from langchain.embeddings.openai import OpenAIEmbeddings

load_dotenv()

st.set_page_config(page_title="Conversational Data Analysis Agent", layout="wide")
st.title("Conversational Data Analysis Agent 🧑‍💻")

# Sidebar for file upload
st.sidebar.header("Upload your dataset")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

# Session state for conversation
if "history" not in st.session_state:
    st.session_state.history = []

# DataFrame placeholder
df = None
sdf = None

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of your data:")
    st.dataframe(df.head())
    llm = OpenAI(api_token=os.getenv("OPENAI_API_KEY"))
    sdf = SmartDataframe(df, config={"llm": llm})
    # Optional: Vector store setup (e.g., FAISS/Chroma)
    # embeddings = OpenAIEmbeddings()
    # vectorstore = FAISS.from_documents([...], embeddings)
else:
    st.info("Please upload a CSV file to get started.")

# User prompt input
if sdf is not None:
    user_prompt = st.text_input("Ask a question about your data:")
    if st.button("Submit") and user_prompt:
        with st.spinner("Thinking..."):
            result = sdf.chat(user_prompt)
            st.session_state.history.append((user_prompt, result))
        st.write(f"**You:** {user_prompt}")
        st.write(f"**Agent:** {result}")

# Conversation history workspace
if st.session_state.history:
    st.write("---")
    st.write("### Conversation History")
    for i, (q, a) in enumerate(st.session_state.history[::-1]):
        st.markdown(f"**Q{i+1}:** {q}")
        st.markdown(f"**A{i+1}:** {a}")
