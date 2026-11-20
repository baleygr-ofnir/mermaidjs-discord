import os
import sqlite3
from contextlib import closing

DB_PATH = os.environ.get('THEME_DB_PATH', 'themes.db')


def _connect():
  return sqlite3.connect(DB_PATH)


def init():
  with closing(_connect()) as con, con:
    con.execute('CREATE TABLE IF NOT EXISTS themes (user_id TEXT PRIMARY KEY, theme TEXT NOT NULL)')


def get_theme(user_id):
  with closing(_connect()) as con:
    row = con.execute('SELECT theme FROM themes WHERE user_id = ?', (str(user_id),)).fetchone()
  return row[0] if row else None


def set_theme(user_id, theme):
  with closing(_connect()) as con, con:
    con.execute(
      'INSERT INTO themes (user_id, theme) VALUES (?, ?) '
      'ON CONFLICT(user_id) DO UPDATE SET theme = excluded.theme',
      (str(user_id), theme),
    )
