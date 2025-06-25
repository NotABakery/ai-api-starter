import sqlite3

conn = sqlite3.connect("usage.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usage (api_key TEXT PRIMARY KEY, count INT)")
conn.commit()

def get_usage(api_key):
    cursor.execute("SELECT count FROM usage WHERE api_key=?", (api_key,))
    row = cursor.fetchone()
    return row[0] if row else 0

def log_usage(api_key):
    current = get_usage(api_key)
    if current == 0:
        cursor.execute("INSERT INTO usage VALUES (?, ?)", (api_key, 1))
    else:
        cursor.execute("UPDATE usage SET count=? WHERE api_key=?", (current + 1, api_key))
    conn.commit()
