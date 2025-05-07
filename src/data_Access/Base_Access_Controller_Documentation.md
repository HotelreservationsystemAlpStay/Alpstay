# Documentation Base_Access_Controller

The `Base_Access_Controller` class is used to manage our SQLite database for the project. It encapsulates all logic for the basic functions of establishing, using, and closing the database connection.

## Initialization

- **Constructor (`__init__`)**
  When creating a new object of `Base_Access_Controller`:
  - The relative path to the SQL file (`db.sql`) is determined.
  - The SQLite database connection is established.
  - The SQLite connection's attribute `row_factory` is set to `sqlite3.Row`, which causes results to be returned as objects where columns can be accessed by name.

  **Example:**
  ```python
  from controller.Base_Access_Controller import Base_Access_Controller
  db_controller = Base_Access_Controller()
  ```

## Methods

### execute
- **Task:** Executes generic SQL commands (INSERT, UPDATE, DELETE).
- **Parameters:**
  - `query` (str): The SQL command to be executed.
  - `params` (tuple, optional): Parameters for the SQL command to prevent SQL injections.
- **Return:**
  Returns a `sqlite3.Cursor` object after the command has been executed.
- **Usage:**
  Ideal for performing operations that modify the database.
  **Example:**
  ```python
  query = "INSERT INTO user (id, username, password, role) VALUES (?, ?, ?, ?)"
  params = (1, "AdminUser", "secretPassword", "admin")
  cursor = db_controller.execute(query, params)
  ```

### fetchall
- **Task:** Executes an SQL select query and returns all found rows.
- **Parameters:**
  - `query` (str): The SQL select query to be executed.
  - `params` (tuple, optional): Parameters for the SQL command to prevent SQL injections.
- **Return:**
  A list of all result rows.
- **Usage:**
  Useful when all records matching a query are needed.
  **Example:**
  ```python
  query = "SELECT id, username, password, role FROM user WHERE role = ? AND id > ?"
  params = ("admin", 5)
  rows = db_controller.fetchall(query, params)
  for row in rows:
      print(row["id"], row["username"], row["role"])
  ```

### fetchone
- **Task:** Executes an SQL select query and returns only the first found row.
- **Parameters:**
  - `query` (str): The SQL select query to be executed.
  - `params` (tuple, optional): Parameters for the SQL command to prevent SQL injections.
- **Return:**
  A single Row object representing the first row from the result.
- **Usage:**
  Practical when only a single record (e.g., a detail record) is needed.
  **Example:**
  ```python
  query = "SELECT id, username, password, role FROM user WHERE id = ?"
  params = (1,)
  row = db_controller.fetchone(query, params)
  if row:
      print(row["id"], row["username"], row["role"])
  ```

### close
- **Task:** Closes the active database connection.
- **Usage:**
  Should be called when database operations are finished to release resources.

  **Example:**
  ```python
  db_controller.close()
  ```