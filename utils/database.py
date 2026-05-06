import sqlite3
from pathlib import Path

# DBファイルのパス
DB_PATH = Path("data/app.db")


def get_connection() -> sqlite3.Connection:
    """DBに接続する"""
    conn = sqlite3.connect(DB_PATH)
    # 辞書形式で結果を取得できるようにする
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """起動時にテーブルを初期化"""
    conn = get_connection()
    conn.execute("""
        create table if not exists messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def insert_message(name: str, message: str):
    """メッセージを1件追加する"""
    conn = get_connection()
    conn.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()


def get_all_messages():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM messages ORDER BY created_at DESC").fetchall()
    conn.close()
    return rows
