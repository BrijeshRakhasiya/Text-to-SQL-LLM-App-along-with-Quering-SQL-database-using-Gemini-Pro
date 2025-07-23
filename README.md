# 🧠 Text-to-SQL LLM App using Gemini Pro

A powerful **Text-to-SQL web application** built using **Google Gemini Pro** and **Streamlit**. This app converts natural language questions into SQL queries using a language model and fetches results from a **SQLite** database.

---

## 🚀 Features

- 🔍 Converts plain English to SQL using Google Gemini Pro (1.5 Flash)
- 🧑‍🎓 Queries a student database with fields: `NAME`, `CLASS`, `SECTION`, `MARKS`
- 💬 User-friendly interface with Streamlit
- 🧠 Built-in prompt tuning for reliable query generation
- 🗃️ Uses `sqlite3` for fast in-memory querying

---

## 🧱 Tech Stack

- Python 🐍  
- [Streamlit](https://streamlit.io/) — UI Framework  
- [Google Generative AI (Gemini)](https://ai.google.dev/) — LLM for text-to-SQL translation  
- [SQLite3](https://www.sqlite.org/index.html) — Lightweight SQL database  
- python-dotenv — For secure API key management

---


---

## 🧪 Example Prompts

> ❓ "How many entries of records are present?"  
> 🧾 `SELECT COUNT(*) FROM STUDENT;`

> ❓ "Tell me all the students studying in Data Science class?"  
> 🧾 `SELECT * FROM STUDENT WHERE CLASS="Data Science";`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/BrijeshRakhasiya/Text-to-SQL-LLM-App-along-with-Quering-SQL-database-using-Gemini-Pro.git
cd text-to-sql-gemini-app
```

## 2.Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows

#  3. Install Dependencies
```
pip install -r requirements.txt
```

# 4. Add Google API Key

Create a .env file in the root directory:
```
GOOGLE_API_KEY=your_google_api_key_here
```

# 5. Initialize the SQLite Database

Run the sql.py script to create the STUDENT table and insert sample records.
```
python sql.py
```

# 6. Run the Streamlit App
```
streamlit run app.py
```

# 💡 How It Works
User enters a natural language question (e.g., “Show all students in section A”)

Gemini 1.5 Flash converts it into a valid SQL query

The query is executed on a local student.db SQLite database

The result is shown in the app

# 🧪 Example Prompts

| English Question                                   | SQL Generated                                       |
| -------------------------------------------------- | --------------------------------------------------- |
| How many entries of records are present?           | `SELECT COUNT(*) FROM STUDENT;`                     |
| Tell me all the students studying in Data Science? | `SELECT * FROM STUDENT WHERE CLASS="Data Science";` |


# 🙋 Author
Brijesh Rakhasiya
📍 AI/ML Enthusiast | Python Developer | Data Scientist


# 📜 License
This project is licensed under the GNU General Public License (GPL).
Feel free to use, distribute, and modify it under the terms of the GNU GPL v3.
