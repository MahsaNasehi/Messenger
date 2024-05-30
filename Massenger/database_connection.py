import mysql.connector


class DatabaseConnection:
    def __init__(self, host, port, user, password, database):
        self.db_connector_obj = None
        self.connection_cursor = None
        try:
            self.db_connector_obj = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            )
            self.connection_cursor = self.db_connector_obj.cursor()
        except mysql.connector.Error as error:
            print(f"Error while connecting to: {error}")

    def execute_query(self, query, values=None):
        if self.db_connector_obj.is_connected() and self.connection_cursor:
            try:
                self.connection_cursor.execute(query, values)
                self.db_connector_obj.commit()
            except mysql.connector.Error as err:
                print(f"Error while executing : {err}")

    def close_connection(self):
        if self.db_connector_obj.is_connected():
            self.connection_cursor.close()
            self.db_connector_obj.close()



# ////////////////////////////////
# def get_cursor():
#     return connection_cursor
#
#
# def get_connection():
#     return db_connector_obj


# # remember in order to connect to db, you should run docker(server up)
#
# # should add three params, your host, password, username
# db_connector_obj = mysql.connector.connect(
#     host="localhost",
#     port="3307",
#     user="root",
#     password="password",
#     database="db"
# )
# # test connection print(mydb)
#
# connection_cursor = db_connector_obj.cursor()
# # in order to check your cursor functionality
# # print(connection_cursor)

# # in order to show all the tables in db
# connection_cursor.execute("SHOW TABLES")

# # in order to get all the tuples in user table
# connection_cursor.execute("SELECT * FROM user")
#
# # iteration on cursor obj
# for x in connection_cursor:
#   print(x)
# # # or this way
# print(connection_cursor.fetchall())

# # inserting special data in user table
# sql_formula = "INSERT INTO user(first_name, last_name, phone_number) VALUES (%s, %s, %s)"
# user1 = ("John", "Smith", "09876543210")
# connection_cursor.execute(sql_formula, user1)
# db_connector_obj.commit()
