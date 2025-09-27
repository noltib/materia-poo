import sqlite3

# Use 'with' to connect to the SQLite database and automatically close the connection when done
with sqlite3.connect('danco_de_bados.db') as connection:

    # Create a cursor object
    cursor = connection.cursor()

    # Write the SQL command to create the Students table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    );
    '''

    # Execute the SQL command
    cursor.execute(create_table_query)

    # Commit the changes
    connection.commit()

    # Print a confirmation message
    print("Table 'Students' created successfully!")