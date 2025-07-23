import os 
import streamlit as st 
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Fuction to load Google Gemini model and provide sql query as response 

def get_gemini_response(question , prompt) :
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt[0] , question])
    return response.text


# Retrieve query from the sql database 

def read_sql_query(sql , db) :
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows :
        print(row)
    return rows


prompt = [
    """
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION and MARKS.

For example,

Example 1 - How many entries of records are present?
The SQL command will be something like this:
SELECT COUNT(*) FROM STUDENT;

Example 2 - Tell me all the students studying in Data Science class?
The SQL command will be something like this:
SELECT * FROM STUDENT WHERE CLASS="Data Science";

Also, the SQL code should not have ``` in the beginning or end and the word 'sql' should not be included.
    """
]

#  Streamlit APP 

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini APP TO Retrieve SQL Data ")

question = st.text_input("Input: " , key = "input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question , prompt)
    print(response)
    data = read_sql_query(response , "student.db")
    st.subheader("THe Response is ")
    for row in data :
        print(row)
        st.write(row)
