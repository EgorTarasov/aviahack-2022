DATABASE_URL = "postgresql://test_user:test_password@localhost:5432/test"
# "postgresql://postgres:postgres@localhost:5433/crocDb"
# POSTGRES_PASSWORD = "postgres"
d = "postgres"
"""postgres docker start"""
# docker run --name crocdb -p 5433:5432 -e POSTGRES_PASSWORD=postgres -d postgres

"""
conn = psycopg2.connect(
    host="localhost",
    database="crocDb",
    user="postgres",
    password="postgres",
    port=5433,
)"""
