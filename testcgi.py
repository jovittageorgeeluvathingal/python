#!C:\Users\CCL37\AppData\Local\Programs\Python\Python310\python.exe
import cgi
import mysql.connector

# Set the content type to HTML
print("Content-type: text/html\n")

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mydatabase'
)

# Create a cursor to execute SQL queries
cursor = db_connection.cursor()

# Retrieve the form data
form = cgi.FieldStorage()
name = form.getvalue('name', '')
email = form.getvalue('email', '')

# Insert data into the database (Create operation)
if name and email:
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(query, values)
    db_connection.commit()

# Fetch all data from the database (Read operation)
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Display the HTML page with the dynamic content
print("""
<!DOCTYPE html>
<html>
<head>
    <title>Python CGI MySQL Example</title>
</head>
<body>
    <h1>Users</h1>
    <form method="post" action="test.py">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name">
        <label for="email">Email:</label>
        <input type="text" name="email" id="email">
        <input type="submit" value="Add User">
    </form>
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
        </tr>
""")
for row in rows:
    user_id, user_name, user_email = row
    print(f"<tr><td>{user_id}</td><td>{user_name}</td><td>{user_email}</td></tr>")

print("""
    </table>
</body>
</html>
""")

# Close the cursor and database connection
cursor.close()
db_connection.close()
