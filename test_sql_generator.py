from analytics_tools.sql_generator import generate_sql

business_context = """
Customers are classified based on their revenue contribution.
"""

sql = generate_sql(
    user_question="Who are my best customers?",
    business_context=business_context
)

print("\n========== FINAL GENERATED SQL ==========")
print(sql)