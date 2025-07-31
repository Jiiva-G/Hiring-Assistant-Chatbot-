# 🤖 Hiring Assistant Chatbot

An AI-powered Hiring Assistant Chatbot built using **Python**, **Streamlit**, and **OpenAI GPT-3.5-Turbo**, designed to help recruiters collect candidate information and generate customized technical interview questions.

---

## 🚀 Features

- ✅ Step-by-step candidate detail collection (Name, Email, Phone, Tech Stack)
- ✅ GPT-based technical question generation
- ✅ Interactive chat interface using Streamlit
- ✅ Smart session-based conversation flow
- ✅ Lightweight, easy to run locally

---

## 🧠 Technologies Used

- **Python 3.10+**
- **Streamlit**
- **OpenAI GPT API (gpt-3.5-turbo)**

---

## 📁 Project Structure

HiringAssistantChatbot/
├── chatbot.py # Main Streamlit app
├── requirements.txt # Python dependencies
└── env/ # Virtual environment (optional)


---

## ⚙️ Installation Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/HiringAssistantChatbot.git
cd HiringAssistantChatbot

# Create and activate virtual environment
python -m venv env
source env/bin/activate   # or env\Scripts\activate (on Windows)

# Install dependencies
pip install -r requirements.txt

▶️ Run the Application

streamlit run chatbot.py

✨ Prompt Design

    Clear instruction to GPT:
    “Generate 3 technical interview questions for each of the following tech stack items: {tech_stack}”

    Conversational structure designed to distinguish between:

        Info-gathering phase

        Technical generation phase

    Emphasis on professional and HR-friendly tone

🧩 Challenges & Solutions
Challenge	Solution
OpenAI API migration	Migrated to latest openai.ChatCompletion format with updated prompts
Streamlit session handling	Used internal state flags to avoid key conflicts
Accurate prompt interpretation by GPT	Crafted structured, bullet-pointed instructions for better accuracy

📄 License
This project is for educational and demonstration purposes.
