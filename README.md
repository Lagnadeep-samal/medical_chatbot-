# medical_chatbot-
## 🩺 Medical Conversational RAG Chatbot

An AI-powered Medical Chatbot built using:

- LangChain
- Pinecone
- HuggingFace Embeddings
- Groq LLM
- Flask
- Adaptive RAG
- Conversational Memory

The chatbot can answer medical questions using Retrieval-Augmented Generation (RAG) from medical PDF documents.

---

## 🚀 Features

- Conversational AI Chatbot
- Adaptive RAG Pipeline
- Dense + Sparse Hybrid Retrieval
- HyDE Query Expansion
- Conversational Memory
- Medical PDF Knowledge Base
- Modern Flask Frontend
- Pinecone Vector Database
- Groq LLM Integration

---

## 🧠 Tech Stack

- Python
- Flask
- LangChain
- Pinecone
- HuggingFace
- Groq API
- HTML
- CSS

---

## 📂 Project Structure

```bash
medical_chatbot/
│
├── app.py
├── requirements.txt
├── .env
│
├── data/
│   └── medical_book.pdf
│
├── src/
│   ├── chatbot.py
│   ├── retrieval.py
│   ├── ingest.py
│   ├── chain.py
│   ├── hyde.py
│   ├── router.py
│   ├── memory.py
│   └── llm.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
```

---

# ⚙️ Installation

## STEP 1 — Clone Repository

```bash
git clone <your-github-repo-link>
```

---

## STEP 2 — Create Virtual Environment

```bash
python -m venv medibot
```

### Activate Environment

#### Windows

```bash
medibot\Scripts\activate
```

#### Linux/Mac

```bash
source medibot/bin/activate
```

---

## STEP 3 — Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory:

```ini
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX=medical-chatbot
```

---

# 📚 Store Embeddings into Pinecone

Run the following command:

```bash
python src/ingest.py
```

---

# ▶️ Run the Flask App

```bash
python app.py
```

Open the browser and visit:

```bash
http://127.0.0.1:5000
```

---

# 💬 Example Questions

- What are symptoms of diabetes?
- Difference between dengue and malaria
- What causes hypertension?
- Explain asthma treatment
- Symptoms of pneumonia

---

# 🧠 Adaptive RAG Workflow

1. User asks a medical question
2. Query routing is performed
3. Hybrid retrieval fetches relevant documents
4. HyDE improves retrieval quality
5. Context is passed to the LLM
6. Final response is generated

---

# 🎨 Frontend

- Responsive UI
- Modern Violet + Black Theme
- Conversational Chat Interface
- Real-time AI Responses

---

# 🔮 Future Improvements

- Voice Assistant Support
- OCR Medical Report Analysis
- Multi-PDF Upload
- Authentication System
- Database Chat History
- Medical Image Analysis

---

# 👨‍💻 Author

Lagnadeep Samal

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.
## Installation
### STEP 1 — Clone Repository
```bash
git clone <your-github-repo-link>
```
### STEP 2 — Create Virtual Environment
```bash
python -m venv medibot
```
```bash
Windows
medibot\Scripts\activate
Linux/Mac
source medibot/bin/activate
```
### STEP 3 — Install Requirements
```bash
pip install -r requirements.txt
```



## Environment Variables
Create a `.env` file:
```ini
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX=medical-chatbot
```

## Store Embeddings into Pinecone
```bash
python src/ingest.py
```

## Run the Flask App
```bash
python app.py
```
