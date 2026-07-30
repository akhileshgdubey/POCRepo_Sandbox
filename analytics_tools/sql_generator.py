from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

PROJECT_ID = "gen-lang-client-0975221347"
DATASET = "business_demo"


def generate_sql(user_question: str, business_context: str):

    prompt = f"""
You are an expert BigQuery SQL Engineer.

Generate ONLY executable BigQuery SQL.

====================================================
PROJECT
====================================================

Project ID:
{PROJECT_ID}

Dataset:
{DATASET}

====================================================
DATABASE SCHEMA
====================================================

Table:
`{PROJECT_ID}.{DATASET}.customers`

Columns:
- customer_id
- customer_name
- city
- region_id
- customer_segment
- signup_date


Table:
`{PROJECT_ID}.{DATASET}.products`

Columns:
- product_id
- product_name
- category


Table:
`{PROJECT_ID}.{DATASET}.regions`

Columns:
- region_id
- region_name


Table:
`{PROJECT_ID}.{DATASET}.sales_transactions`

Columns:
- transaction_id
- customer_id
- product_id
- quantity
- revenue
- transaction_date

====================================================
BUSINESS CONTEXT
====================================================

{business_context}

====================================================
USER QUESTION
====================================================

{user_question}

====================================================
RULES
====================================================

1. Return ONLY SQL.
2. No markdown.
3. No explanation.
4. Always generate Standard SQL.
5. ALWAYS use FULLY QUALIFIED BigQuery table names.
6. Never use table names without project and dataset.

Correct:

FROM `{PROJECT_ID}.{DATASET}.sales_transactions`

Wrong:

FROM sales_transactions

Correct:

JOIN `{PROJECT_ID}.{DATASET}.customers`

Wrong:

JOIN customers
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
    )

    sql = response.text.strip()

    # -----------------------------------------
    # Auto-fix table names if Gemini forgets
    # -----------------------------------------

    TABLES = [
        "customers",
        "products",
        "regions",
        "sales_transactions"
    ]

    for table in TABLES:

        sql = sql.replace(
            f"FROM {table}",
            f"FROM `{PROJECT_ID}.{DATASET}.{table}`"
        )

        sql = sql.replace(
            f"JOIN {table}",
            f"JOIN `{PROJECT_ID}.{DATASET}.{table}`"
        )

        sql = sql.replace(
            f"from {table}",
            f"FROM `{PROJECT_ID}.{DATASET}.{table}`"
        )

        sql = sql.replace(
            f"join {table}",
            f"JOIN `{PROJECT_ID}.{DATASET}.{table}`"
        )

    print("\n========== GENERATED SQL ==========")
    print(sql)
    print("==================================\n")

    return sql