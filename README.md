# 🤖 AI Resume Optimizer using Multi-Agent RAG

An intelligent AI-powered resume optimization platform that analyzes a candidate's resume against a job description and generates an ATS-friendly optimized resume using a Multi-Agent Architecture, LangGraph workflow, Retrieval-Augmented Generation (RAG), OpenAI LLMs, and Qdrant Vector Database.

---

## 🚀 Features

### 🧠 Multi-Agent Resume Optimization

The system uses multiple specialized AI agents:

- 📌 Job Description Analyzer  
  Extracts job role, required skills, responsibilities, experience level, and ATS keywords.

- 📄 Resume Analyzer  
  Evaluates the current resume, identifies strengths, weaknesses, missing information, and ATS issues.

- ❓ Smart Question Generator  
  Asks targeted follow-up questions to gather missing candidate information.

- 🔍 Skill Gap Analyzer  
  Compares the candidate profile against job requirements and identifies gaps.

- 📚 Skill Recommender  
  Suggests technologies, certifications, projects, and learning paths.

- ✨ Resume Generator  
  Creates an optimized ATS-friendly resume tailored to the target role.

- 📊 Resume Reviewer  
  Reviews the generated resume and provides improvement feedback.

---

## 🧩 Multi-Agent Workflow

```text
            Job Description
                   |
                   ▼
          JD Analyzer Agent
                   |
                   ▼
         Resume Analyzer Agent
                   |
                   ▼
       Question Planner Agent
                   |
                   ▼
        User Interaction Agent
                   |
                   ▼
          Gap Analyzer Agent
                   |
                   ▼
       Skill Recommendation Agent
                   |
                   ▼
        Resume Generator Agent
                   |
                   ▼
         Resume Reviewer Agent
                   |
                   ▼
                  END
```

---

## 🔎 Retrieval-Augmented Generation (RAG)

The application uses a Qdrant vector database to provide domain knowledge to AI agents.

### Knowledge Base

- ATS Resume Rules
- Resume Templates
- Resume Examples
- Industry Keywords
- Job-Specific Skills
- Action Verbs

### RAG Pipeline

```
Knowledge Files
       |
       ▼
Document Chunking
       |
       ▼
OpenAI Embeddings
       |
       ▼
Qdrant Vector Database
       |
       ▼
Semantic Retrieval
       |
       ▼
AI Agents
```

---

## 🛠 Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| AI Framework | LangChain, LangGraph |
| LLM | OpenAI GPT Models |
| Vector Database | Qdrant |
| Embeddings | OpenAI text-embedding-3-small |
| Frontend | Streamlit |
| Environment | Python Virtual Environment |

---

## 📁 Project Structure

```text
AI-Resume-Optimizer
│
├── agents/              # Multi-agent implementations
├── config/              # Application configuration
├── knowledge/           # RAG knowledge base
├── parsers/             # Resume parsing utilities
├── prompts/             # Agent prompt templates
├── rag/                 # RAG helper modules
├── state/               # LangGraph state management
├── ui/                  # Streamlit user interface
├── utils/               # Utility functions
├── vector_db/           # Qdrant integration
├── workflow/            # LangGraph workflow
│
├── app.py               # Application entry point
├── requirements.txt     # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Meghana-Ravalkol/AI-Resume-Optimizer.git

cd AI-Resume-Optimizer
```

---

### 2. Create Virtual Environment

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key

OPENAI_BASE_URL=your_base_url

QDRANT_URL=your_qdrant_url

QDRANT_API_KEY=your_qdrant_api_key

QDRANT_COLLECTION_NAME=resume_knowledge
```

---

### 5. Create Vector Database

Generate embeddings and store knowledge in Qdrant:

```bash
python reset_qdrant.py

python -m vector_db.embed_documents
```

---

### 6. Run the Application

```bash
streamlit run ui/streamlit_app.py
```

---

## 📸 Application Demo

Add screenshots here.

Example:

```
/screenshots/home_page.png
/screenshots/generated_resume.png
/screenshots/optimized_resume output1.png
/screenshots/optimized_resume output2.png
/screenshots/optimized_resume output3.png
/screenshots/optimized_resume output4.png
/screenshots/resume_review output1.png
/screenshots/resume_review output2.png
/screenshots/resume_review output3.png


```

---

## 🎯 Future Improvements

- Upload resumes directly as PDF/DOCX
- Add resume version tracking
- Improve ATS scoring algorithm
- Add support for more LLM providers
- Deploy using Docker and cloud services
- Add user authentication and resume history

---

## 👩‍💻 Author

**Bharath Abbanoni**
**Meghana Ravalkol**

GitHub:  
https://github.com/Abbanoni-Bharat
https://github.com/Meghana-Ravalkol

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
