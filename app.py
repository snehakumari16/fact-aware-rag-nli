import streamlit as st

from utils.retriever import build_vectorstore
from utils.generator import generate_answer
from utils.verifier import verify_answer

st.set_page_config(page_title="Fact-Aware RAG System")

try:
    with open("data/docs.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    with st.spinner("Loading vectorstore... (this may take a moment on first run)"):
        vectorstore = build_vectorstore(text)
except Exception as e:
    st.error(f"Error loading vectorstore: {str(e)}")
    st.stop()

st.title("Fact-Aware RAG System")

question = st.text_input("Ask a question")

if question:
    try:
        with st.spinner("Searching documents..."):
            docs = vectorstore.similarity_search(question, k=2)

        context = "\n".join(
            [doc.page_content for doc in docs]
        )

        st.subheader("Retrieved Context")
        st.write(context)

        with st.spinner("Generating answer..."):
            answer = generate_answer(question, context)

        with st.spinner("Verifying answer..."):
            verification = verify_answer(
                context,
                answer
            )

        st.subheader("Generated Answer")
        st.write(answer)

        st.subheader("Verification Result")
        st.json(verification)
    
    except Exception as e:
        st.error(f"Error processing question: {str(e)}")
        import traceback
        st.error(f"Full error:\n{traceback.format_exc()}")