DATABASE_URL = "sqlite:///foo.db"
# "postgresql://test_user:test_password@94.45.223.241:46873/testDb"
# "sqlite:///foo.db"
# "postgresql://postgres:postgres@localhost:5433/crocDb"
# POSTGRES_PASSWORD = "postgres"
# d = "postgres"
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
