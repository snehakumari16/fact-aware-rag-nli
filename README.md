 Fact-Aware RAG + NLI Hallucination Prevention System

An AI-powered research project that reduces hallucinations in Large Language Models (LLMs) using Retrieval-Augmented Generation (RAG) and Natural Language Inference (NLI) verification.

This system retrieves trusted contextual information, generates responses using Llama 3, and verifies factual consistency using an NLI model to improve answer reliability and transparency.

---

Features

- Retrieval-Augmented Generation (RAG)
- FAISS vector database for semantic search
- Llama 3 based response generation
- Natural Language Inference (NLI) verification
- Hallucination detection pipeline
- Context-aware factual answering
- Streamlit web interface
- Modular and research-oriented architecture

---

Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Ollama
- Llama 3
- Hugging Face Transformers
- Sentence Transformers
- PyTorch

---

 Project Architecture

User Query
    ↓
Document Retrieval (FAISS)
    ↓
Relevant Context Extraction
    ↓
Llama 3 Response Generation
    ↓
NLI Verification
    ↓
Hallucination Detection
    ↓
Verified Final Response

Folder Structure

fact-aware-rag-nli/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── docs.txt
│
├── utils/
│   ├── retriever.py
│   ├── generator.py
│   └── verifier.py
│
└── venv/

Installation

1. Clone Repository

git clone https://github.com/YOUR_USERNAME/fact-aware-rag-nli.git

2. Open Project Folder
cd fact-aware-rag-nli

3. Create Virtual Environment

python -m venv venv

 4. Activate Virtual Environment

Windows

venv\Scripts\activate

 Mac/Linux

source venv/bin/activate

 5. Install Dependencies

pip install -r requirements.txt

---

 Install Ollama

Download Ollama:

[https://ollama.com/download](https://ollama.com/download)

Run Llama 3 model:

ollama run llama3


Run the Project

streamlit run app.py
---

Example Questions

* What is Artificial Intelligence?
* Explain Machine Learning.
* What is Natural Language Processing?
* How does Retrieval-Augmented Generation work?

---

 Research Contribution

This project focuses on reducing hallucinations in LLMs by combining:

* Semantic retrieval
* Context-grounded generation
* NLI-based factual verification

The system compares standard LLM outputs with fact-aware verified outputs to improve reliability and explainability in AI-generated responses.

---

 Future Improvements

* PDF document upload
* Real-time web retrieval
* SHAP explainability
* Hallucination confidence scoring
* Multi-document reasoning
* Research paper publication
* Cloud deployment

---
 Applications

* AI Research
* NLP Systems
* Fact Verification
* Explainable AI
* Educational Assistants
* Legal and Medical AI Systems

---

 Author

Sneha Kumari

B.Tech Engineering Student
AI / ML / NLP Enthusiast

---

 License

This project is developed for research and educational purposes.


