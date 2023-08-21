# import sqlite3

# # Connect to the database
# conn = sqlite3.connect('favorites.db')
# c = conn.cursor()

# # Create the table if it doesn't exist
# c.execute('''CREATE TABLE IF NOT EXISTS favorite_foods
#              (name TEXT PRIMARY KEY, food TEXT)''')

# # Define the list of names
# names = ['Anna', 'Bob', 'Candice']

# # Prompt user for favorite foods
# for name in names:
#     food = input(f"Enter the favorite food for {name}: ")

#     # Update the database
#     c.execute(
#         "INSERT OR REPLACE INTO favorite_foods (name, food) VALUES (?, ?)", (name, food))

# # Commit the changes and close the connection
# conn.commit()
# conn.close()

# print("Database updated successfully!")


import sqlite3

conn = sqlite3.connect('favorites.db')
favorites = conn.cursor().execute("SELECT name, food FROM favorite_foods").fetchall()
for name, food in favorites:
    print(f"{name}'s favorite food is: {food}")
conn.close()