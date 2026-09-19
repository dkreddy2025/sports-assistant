Here's a complete README for your SportsIQ AI project — copy everything between the lines below and paste it into your `README.md` file on GitHub (replacing whatever's there), then commit.

```markdown
# 🏏 SportsIQ AI

**Your Personal Sports Knowledge Hub — Powered by AI**

SportsIQ AI is an AI-powered sports assistant built with Streamlit that lets you ask sports questions, generate custom quizzes, read the latest sports news, and track your quiz history — all backed by live web search and a Groq-hosted LLM.

## ✨ Features

- **💬 Sports Q&A** — Ask any sports question and get an AI-generated answer backed by real-time web search, complete with a confidence score and related questions.
- **🎯 Quiz Arena** — Generate custom multiple-choice quizzes on 15+ sports (Cricket, Football, Badminton, Kabaddi, and more) with adjustable difficulty, question count, and an optional timer. Attempt quizzes online or download a blank version to solve on paper.
- **📰 Sports News** — Get the latest sports news headlines and summaries by sport, generated from live search results.
- **📚 Quiz History** — Every quiz attempt is saved in-session, with scores and downloadable results.
- **📥 Export Options** — Download quizzes and results as PDF or Word documents, with or without answers/explanations.

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **LLM Orchestration:** [LangChain](https://www.langchain.com/)
- **LLM Provider:** [Groq](https://groq.com/) (`openai/gpt-oss-120b`)
- **Web Search:** DuckDuckGo Search
- **Document Export:** FPDF2, python-docx

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A [Groq API key](https://console.groq.com/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dkreddy2025/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
├── app.py            # Streamlit UI and app logic
├── quiz_chain.py      # LangChain chains for Q&A, news, and quiz generation
├── requirements.txt   # Python dependencies
└── README.md
```

## 👤 Developer

**Kishore Reddy Dudipala**
B.E. Electronics & Communication Engineering, Vasavi College of Engineering, Hyderabad

- 📧 [dkreddy2025@gmail.com](mailto:dkreddy2025@gmail.com)
- 💼 [LinkedIn](https://linkedin.com/in/kishorereddy945)
- 🐙 [GitHub](https://github.com/dkreddy2025)

---
*Sports Intelligence Powered by AI*
```

Once you've pasted that in and committed, tell me and we'll move on to **uploading `app.py`, `quiz_chain.py`, and `requirements.txt`** to this same repo.
