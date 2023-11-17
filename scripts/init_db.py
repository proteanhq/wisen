# Example script to initialize schema registry database
import sqlite3

def initialize_schema_registry_db():
    # Connect to the database
    conn = sqlite3.connect("schema_registry.db")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create the schema registry table
    create_table_query = """
        CREATE TABLE IF NOT EXISTS schema_registry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            schema_name TEXT NOT NULL,
            schema_version INTEGER NOT NULL,
            schema_definition TEXT NOT NULL
        );
    """
    cursor.execute(create_table_query)
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Call the function to initialize the schema registry database
initialize_schema_registry_db()
