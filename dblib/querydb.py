from databricks import sql
import os


def querydb(query="1"):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute("SELECT Weekly_Sales, Date FROM walmart WHERE Holiday_Flag="+query+" ORDER BY Weekly_Sales DESC LIMIT 10")
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result