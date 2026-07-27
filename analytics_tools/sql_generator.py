from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

# client = genai.Client(
#     vertexai=True,
#     project="gen-lang-client-0975221347",
#     location="us-central1"
# )

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

PROJECT_ID = "gen-lang-client-0975221347"
DATASET = "business_demo"


def generate_sql(user_question: str, business_context: str):

    prompt = f"""
You are a BigQuery SQL expert.

Generate ONLY valid BigQuery SQL.

Dataset:
`{PROJECT_ID}.{DATASET}`

Tables:

customers(
customer_id,
customer_name,
city,
region_id,
customer_segment,
signup_date
)

products(
product_id,
product_name,
category
)

regions(
region_id,
region_name
)

sales_transactions(
transaction_id,
customer_id,
product_id,
quantity,
revenue,
transaction_date
)

Business Context:
{business_context}

User Question:
{user_question}

Rules:
- Return ONLY SQL.
- No markdown.
- No explanation.
- Use fully-qualified table names.
"""

    #print("\n========== SQL PROMPT ==========")
    #print(prompt)

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
    )

    sql = response.text.strip()

    print("\n========== GENERATED SQL ==========")
    print(sql)
    print("==================================\n")

    return sql