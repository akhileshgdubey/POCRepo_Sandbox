
from knowledge_graph.kg_tool import search_business_context
from analytics_tools.sql_generator import generate_sql
from analytics_tools.bigquery_tool import run_business_query


question = input("Enter your business question: ")

print("\n========== USER QUESTION ==========")
print(question)

# Knowledge Graph
kg_context = search_business_context(question)

print("\n========== KNOWLEDGE GRAPH ==========")
print(kg_context)

# Generate SQL
sql = generate_sql(question)

print("\n========== GENERATED SQL ==========")
print(sql)

# Execute SQL
result = run_business_query(sql)

print("\n========== BIGQUERY RESULT ==========")

for row in result:
    print(row)

print("\n========== END ==========")