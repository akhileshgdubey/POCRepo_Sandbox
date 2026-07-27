from analytics_tools.sql_generator import generate_sql
from google.cloud import bigquery

PROJECT_ID = "gen-lang-client-0975221347"

business_context = """
Customers are classified based on their revenue contribution.
"""

# user input
question = input("Enter your question: ")

# Generate SQL
sql = generate_sql(
    user_question=question,
    business_context=business_context
)

print("\n========== GENERATED SQL ==========\n")
print(sql)

# Execute SQL on BigQuery
client = bigquery.Client(project=PROJECT_ID)

query_job = client.query(sql)
results = query_job.result()

print("\n========== QUERY RESULT ==========\n")

rows_found = False

for row in results:
    rows_found = True
    print(dict(row.items()))

if not rows_found:
    print("No rows returned.")

print("\n==================================")