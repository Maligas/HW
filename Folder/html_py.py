import sqlite3

f = sqlite3.connect('fruit.db')
cursor = f.cursor()

cursor.execute("select (select login from user where id == user_id) as name, (select name from fruit where id == item_id) as item from ord;")
print(cursor.fetchall())

cursor.execute("select (select login from user where id == user_id) as name, (select registration_date from user where id=user_id) as reg_data, date from ord;")
print(cursor.fetchall())

cursor.execute("select (select login from user where id == user_id) as name,(select name from fruit where id == item_id) as item, (select price from fruit where id=item_id) as price_one_item, amount from ord;")
print(cursor.fetchall())

cursor.execute("select (select name from fruit where id == item_id) as item, discount, (select login from user where id == user_id) as name, date from ord;")
print(cursor.fetchall())

cursor.execute("select (select login from user where id == user_id) as name, (select birth_date from user where id=user_id) as birth_date, (select registration_date from user where id=user_id) as reg_date, discount from ord;")
print(cursor.fetchall())

f.close()
