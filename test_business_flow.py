from analytics_tools.sql_generator import generate_customer_revenue_sql
from analytics_tools.bigquery_tool import run_business_query


sql = generate_customer_revenue_sql()

print("Generated SQL:")
print(sql)


result = run_business_query(sql)

print("\nBusiness Result:")

for row in result:
    print(row)