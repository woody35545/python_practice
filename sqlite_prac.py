import sqlite3

# DB 연결
connect = sqlite3.connect("temp.db")
# 커서 획득
cursor = connect.cursor()

cursor.execute("CREATE TABLE TEST_TABLE(name text, age integer)")