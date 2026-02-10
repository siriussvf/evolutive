import sqlite3
import os

db_path = 'ievolutiva.db'
if not os.path.exists(db_path):
    print("Database not found at ievolutiva.db")
    exit(1)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("Updating 'user' table...")
# Add missing columns
columns_to_add = [
    ("nickname", "TEXT"),
    ("user_context", "TEXT"),
    ("response_style", "TEXT DEFAULT 'default'"),
    ("custom_instructions", "TEXT"),
    ("enable_memory", "BOOLEAN DEFAULT 1")
]

for col_name, col_type in columns_to_add:
    try:
        cursor.execute(f"ALTER TABLE user ADD COLUMN {col_name} {col_type}")
        print(f"✅ Added column {col_name} to user table.")
    except sqlite3.OperationalError:
        print(f"ℹ️ Column {col_name} already exists or error.")

print("Creating 'user_memory' table if not exists...")
try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        fact TEXT NOT NULL,
        extracted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        is_active BOOLEAN DEFAULT 1,
        FOREIGN KEY(user_id) REFERENCES user(id)
    )
    """)
    print("✅ user_memory table created/checked.")
except Exception as e:
    print(f"❌ Error creating user_memory: {e}")

conn.commit()
conn.close()
print("Migration completed.")
