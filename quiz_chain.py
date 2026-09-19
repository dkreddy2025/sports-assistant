from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv

load_dotenv()

# LLM
llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.7)

# Web Search
search = DuckDuckGoSearchRun()

# Parser
parser = StrOutputParser()

def search_sports_info(query):
    try:
        result = search.run(query)
        return result, 5
    except Exception as e:
        return f"Search failed: {str(e)}", 0

# ─────────────────────────────────────────
# Q&A
# ─────────────────────────────────────────
qa_prompt = PromptTemplate(
    input_variables=["question", "search_result"],
    template="""
You are an expert sports analyst with deep knowledge of all sports.
Use the search result below to answer the question precisely.

Search Result:
{search_result}

Question: {question}

Format your response EXACTLY like this:

ANSWER:
<your detailed answer here>

RELATED QUESTIONS:
1. <related question 1>
2. <related question 2>
3. <related question 3>

CONFIDENCE:
<a number between 60 and 99>
"""
)

qa_chain = qa_prompt | llm | parser

def answer_sports_question(question):
    search_result, sources = search_sports_info(question)
    response = qa_chain.invoke({
        "question": question,
        "search_result": search_result
    })
    return response, search_result, sources

# ─────────────────────────────────────────
# NEWS
# ─────────────────────────────────────────
news_prompt = PromptTemplate(
    input_variables=["sport", "search_result"],
    template="""
You are a sports journalist. Based on the search results below,
provide the latest news about {sport} in India.

Search Result:
{search_result}

Format as exactly 4 news items like this:
NEWS1_TITLE: <headline>
NEWS1_SUMMARY: <2-3 sentence summary>
NEWS1_CATEGORY: <category>

NEWS2_TITLE: <headline>
NEWS2_SUMMARY: <2-3 sentence summary>
NEWS2_CATEGORY: <category>

NEWS3_TITLE: <headline>
NEWS3_SUMMARY: <2-3 sentence summary>
NEWS3_CATEGORY: <category>

NEWS4_TITLE: <headline>
NEWS4_SUMMARY: <2-3 sentence summary>
NEWS4_CATEGORY: <category>
"""
)

news_chain = news_prompt | llm | parser

def get_sports_news(sport="all Indian sports"):
    search_result, _ = search_sports_info(f"latest {sport} news India 2025")
    response = news_chain.invoke({
        "sport": sport,
        "search_result": search_result
    })
    return response

# ─────────────────────────────────────────
# QUIZ
# ─────────────────────────────────────────
quiz_prompt = PromptTemplate(
    input_variables=["sport", "num_questions", "search_result"],
    template="""
You are a professional sports quiz master.
Generate {num_questions} multiple choice questions about {sport}.
Mixed difficulty: 30% Easy, 40% Medium, 30% Hard.
Use search result for latest facts: {search_result}

For EACH question use EXACTLY this format:

QUESTION: <question text>
DIFFICULTY: <Easy/Medium/Hard>
A) <option A>
B) <option B>
C) <option C>
D) <option D>
ANSWER: <A/B/C/D>
WHY_CORRECT: <why correct answer is right>
WHY_A: <why A is correct or wrong>
WHY_B: <why B is correct or wrong>
WHY_C: <why C is correct or wrong>
WHY_D: <why D is correct or wrong>

---
"""
)

quiz_chain = quiz_prompt | llm | parser

def generate_quiz(sport, num_questions):
    search_result, _ = search_sports_info(f"latest {sport} facts records 2025")
    response = quiz_chain.invoke({
        "sport": sport,
        "num_questions": num_questions,
        "search_result": search_result
    })
    return response