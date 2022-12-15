import sqlite3


def add_user(username, userpass):
    cur.execute(f"INSERT INTO users(name, password) VALUES('{username}', '{userpass}')")
    conn.commit()


conn = sqlite3.connect('my.db')
cur = conn.cursor()

name = input("Введите Логин: ")
passwd = input("Введите Пароль: ")
add_user(name, passwd)
print('\n')

print('Список пользователей:')
cur.execute('SELECT * FROM users')
row = cur.fetchone()
while row is not None:
    print(f'id: {row[0]}, логин: {row[1]}, пароль: {row[2]}')
    row = cur.fetchone()

cur.close()
conn.close()
