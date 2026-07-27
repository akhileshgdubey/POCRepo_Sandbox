from analytics_tools.sql_generator import generate_sql

business_context = """
Customers are classified based on their revenue contribution.
"""

user_question = input("Enter your question: ")

try:
    sql = generate_sql(
        user_question=user_question,
        business_context=business_context
    )

    print("\n========== GENERATED SQL ==========")
    print(sql)

except Exception as e:
    print("\nERROR:")
    print(e)