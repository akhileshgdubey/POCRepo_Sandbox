from analytics_tools.bigquery_tool import run_business_query


sql = """
SELECT
  customer_id,
  SUM(revenue) AS total_revenue
FROM
  `gen-lang-client-0975221347.business_demo.sales_transactions`
GROUP BY
  customer_id
ORDER BY
  total_revenue DESC
LIMIT 5
"""


result = run_business_query(sql)


for row in result:
    print(row)