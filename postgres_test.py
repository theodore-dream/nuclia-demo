import psycopg2
from psycopg2 import OperationalError

def test_connection(connection_string):
    try:
        # Attempt to connect to the PostgreSQL server
        conn = psycopg2.connect(connection_string)
        # If the connection is successful, print a success message
        print("Connection successful!")
        # Close the connection
        conn.close()
    except OperationalError as e:
        # If the connection fails, print the error message
        print(f"Connection failed: {e}")

# Define your connection string
connection_string = "postgresql://postgres:password@localhost:5432/postgres"

# Call the test_connection function with your connection string
test_connection(connection_string)
