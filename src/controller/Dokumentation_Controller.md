# Dokumentation DataBaseController

Die Klasse `DataBaseController` dient zur Verwaltung unserer SQLite-Datenbank für das Projekt. Sie kapselt sämtliche Logik für die Grundfunktionen zum Herstellen, Verwenden und Schliessen der Datenbankverbindung.

## Initialisierung

- **Konstruktor (`__init__`)**  
  Beim Erstellen eines neuen Objekts von `DataBaseController` wird:
  - Der relative Pfad zur SQL-Datei (`db.sql`) ermittelt.  
  - Die SQLite-Datenbankverbindung wird hergestellt.
  - Das Attribut der SQLite Verbindung namens `row_factory` wird auf `sqlite3.Row` gesetzt, wodurch Ergebnisse als Objekte zurückgegeben werden, bei denen man über Spaltennamen zugreifen kann.
  
  **Beispiel:**
  ```python
  from controller.DataBaseController import DataBaseController
  db_controller = DataBaseController()
  ```

## Methoden

### initialize_database
- **Aufgabe:** Initialisiert die Datenbank, indem ein SQL-Schema aus der Datei (`db.sql`) gelesen und ausgeführt wird.
- **Vorgehensweise:** 
  - Liest die Datei `db.sql` im Unterordner `database` ein.
  - Führt das SQL-Schema mittels `executescript` aus.
  - Commitet die Änderungen an der Datenbank.
- **Verwendung:**  
  Diese Methode eignet sich beispielsweise als Setup-Schritt, wenn die Datenbankstruktur neu initialisiert werden soll.
  
  **Beispiel:**
  ```python
  db_controller.initialize_database()
  ```

### execute
- **Aufgabe:** Führt generische SQL-Kommandos (INSERT, UPDATE, DELETE) aus.
- **Parameter:**
  - `query` (str): Das auszuführende SQL-Kommando.
  - `params` (tuple, optional): Parameter für das SQL-Kommando, um SQL-Injections vorzubeugen.
- **Rückgabe:**  
  Gibt ein `sqlite3.Cursor`-Objekt zurück, nachdem das Kommando ausgeführt wurde.
- **Verwendung:**  
  Ideal zur Durchführung von Operationen, die die Datenbank verändern.  
  **Beispiel:**
  ```python
  query = "INSERT INTO users (id, username, password, role) VALUES (?, ?, ?, ?)"
  params = (1, "AdminUser", "secretPassword", "admin")
  cursor = db_controller.execute(query, params)
  ```

### fetchall
- **Aufgabe:** Führt ein SQL-Select-Query aus und gibt alle gefundenen Zeilen zurück.
- **Parameter:**
  - `query` (str): Die auszuführende SQL Select-Query.
  - `params` (tuple, optional): Parameter für das SQL-Kommando, um SQL-Injections vorzubeugen.
- **Rückgabe:**  
  Eine Liste aller Ergebniszeilen.
- **Verwendung:**  
  Nützlich, wenn alle Datensätze, die einer Abfrage entsprechen, benötigt werden.  
  **Beispiel:**
  ```python
  query = "SELECT id, username, password, role FROM users WHERE role = ? AND id > ?"
  params = ("admin", 5)
  rows = db_controller.fetchall(query, params)
  for row in rows:
      print(row["id"], row["username"], row["role"])
  ```

### fetchone
- **Aufgabe:** Führt eine SQL Select-Query aus und gibt nur die erste gefundene Zeile zurück.
- **Parameter:**
  - `query` (str): Die auszuführende SQL Select-Query.
  - `params` (tuple, optional): Parameter für das SQL-Kommando, um SQL-Injections vorzubeugen.
- **Rückgabe:**  
  Eine einzelnes Row Objekt, welches die erste Zeile aus dem Ergebnis darstellt.
- **Verwendung:**  
  Praktisch, wenn nur ein einzelner Datensatz (z.B. ein Detail-Datensatz) benötigt wird.  
  **Beispiel:**
  ```python
  query = "SELECT id, username, password, role FROM users WHERE id = ?"
  params = (1,)
  row = db_controller.fetchone(query, params)
  if row:
      print(row["id"], row["username"], row["role"])
  ```

### close
- **Aufgabe:** Schliesst die aktive Datenbankverbindung.
- **Verwendung:**  
  Sollte aufgerufen werden, wenn die Datenbankoperationen beendet sind, um Ressourcen freizugeben.
  
  **Beispiel:**
  ```python
  db_controller.close()
  ```