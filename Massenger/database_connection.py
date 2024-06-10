import mysql.connector
# import check_query

class DatabaseConnection:
    def __init__(self):
        self.db_connector_obj = None
        self.connection_cursor = None
        try:
            self.db_connector_obj = mysql.connector.connect(
                host='localhost',
                port="3307",
                user="root",
                password="password",
                database="db"
            )
            self.connection_cursor = self.db_connector_obj.cursor()
        except mysql.connector.Error as error:
            print(f"Error while connecting to mysql: {error}")

    # def get_connection(self):
    #     # get the connection
    #     connection = DatabaseConnection()
    #     return connection

    def execute_query(self, query, values=None):
        if self.db_connector_obj.is_connected() and self.connection_cursor:
            try:
                self.connection_cursor.execute(query, values)

                # self.db_connector_obj.commit()
                print(self.connection_cursor)
                # in order to get the result / results from curser
                return [True, ""]
            except mysql.connector.Error as err:
                print(f"Error while executing : {err}")
                return [False, f"Error while executing : {err}"]

    def commit_query(self):
        self.db_connector_obj.commit()

    def get_one_row(self):
        return self.connection_cursor.fetchall()

    def close_connection(self):
        if self.db_connector_obj.is_connected():
            self.connection_cursor.close()
            self.db_connector_obj.close()

#
# # insertion / creation
# def user_insertion(user_obj):
#     sql_formula = "INSERT INTO user (user_name, first_name, last_name, phone_number) VALUES (%s, %s, %s, %s)"
#     user = [user_obj.user_name, user_obj.first_name, user_obj.last_name, user_obj.phone_number]
#     try:
#         connection.execute_query(sql_formula, user)
#         connection.commit_query()
#         return "Added"
#     except mysql.connector.Error as err:
#         return "Error while Adding"
#
#
# def pv_chat_insertion(pv_obj):
#     sql_formula = "INSERT INTO pv_chat (user1_id, user2_id) VALUES (%s, %s)"
#     pv = [pv_obj.first_user_id, pv_obj.second_user_id]
#     try:
#         connection.execute_query(sql_formula, pv)
#         connection.commit_query()
#         return "Added"
#     except mysql.connector.Error as err:
#         return "Error while Adding"
#
#
# def group_chat_insertion(group_obj):
#     sql_formula = "INSERT INTO group_chat (chat_name) VALUES (%s)"
#     group = [group_obj.chat_name]
#     try:
#         connection.execute_query(sql_formula, group)
#         connection.commit_query()
#         return "Added"
#     except mysql.connector.Error as err:
#         return "Error while Adding"
#
#
# def group_member_insertion(member):
#     sql_formula = "INSERT INTO group_membership (chat_id, member_id) VALUES (%s, %s)"
#     member_info = [member.group_chat_id, member.member_id]
#     try:
#         connection.execute_query(sql_formula, member_info)
#         connection.commit_query()
#         return "Added"
#     except mysql.connector.Error as err:
#         return "Error while Adding"
#
#
# def contacts_insertion(contact):
#     sql_formula = "INSERT INTO contacts (user_id, user_s_contact_id) VALUES (%s, %s)"
#     contact_info = [contact.users_id, contact.users_contact_id]
#     try:
#         connection.execute_query(sql_formula, contact_info)
#         connection.commit_query()
#         return "Added"
#     except mysql.connector.Error as err:
#         return "Error while Adding"
#
#
# def message_insertion(message):
#     continue_the_insertion = True
#     if message.is_group_chat:
#         continue_the_insertion = check_query.check_membershipism(message.sender_id, message.chat_id)
#     if continue_the_insertion:
#         sql_formula = "INSERT INTO msg (chat_id, pv_id, sender_id, content) VALUES (%s, %s, %s, %s)"
#         if message.is_group_chat:
#             msg = [message.chat_id, None, message.sender_id, message.content]
#         else:
#             msg = [None, message.chat_id, message.sender_id, message.content]
#         try:
#             connection.execute_query(sql_formula, msg)
#             connection.commit_query()
#             return "Added"
#         except mysql.connector.Error as err:
#             return "Error while Adding"
#     else:
#         return "You are not member of this chat"

#  TODO
# # read from tables
# def select_usertable_by_userid(userid):
#     sql_formula = "SELECT * FROM user WHERE user_id = %s"
#     user_id_info = [userid]
#     try:
#         connection.execute_query(sql_formula, user_id_info)
#         result = connection.get_one_row()
#         return result
#     except Exception as e:
#         return "Error while reading"
#
#
# def select_contactstable_by_userid(userid):
#     sql_formula = "SELECT * FROM contacts WHERE user_id = %s"
#     user_id_info = [userid]
#     try:
#         connection.execute_query(sql_formula, user_id_info)
#         result = connection.get_one_row()
#         return result
#     except Exception as e:
#         return "Error while reading"
#
#
# def select_grouptable_by_id(group_id):
#     sql_formula = "SELECT * FROM group_chat WHERE chat_id = %s"
#     group_info = [group_id]
#     try:
#         connection.execute_query(sql_formula, group_info)
#         result = connection.get_one_row()
#         return result
#     except Exception as e:
#         return "Error while reading"
#
#
# def select_group_membertable_by_userid(userid):
#     sql_formula = "SELECT * FROM group_membership WHERE member_id = %s"
#     user_id_info = [userid]
#     try:
#         connection.execute_query(sql_formula, user_id_info)
#         result = connection.get_one_row()
#         return result
#     except Exception as e:
#         return "Error while reading"
#
#
# def select_msgtable_by_userid(msg_id):
#     sql_formula = "SELECT * FROM msg WHERE msg_id = %s"
#     msg_id_info = [msg_id]
#     try:
#         connection.execute_query(sql_formula, msg_id_info)
#         result = connection.get_one_row()
#         return result
#     except Exception as e:
#         return "Error while reading"
#
#
# def select_pvtable_by_userid(pv_id):
#     sql_formula = "SELECT * FROM pv_chat WHERE chat_id = %s"
#     pv_id_info = [pv_id]
#     try:
#         connection.execute_query(sql_formula, pv_id_info)
#         result = connection.get_one_row()
#         return result
#     except Exception as e:
#         return "Error while reading"
#
#
# # update
# def update_user(user_id, field_to_update, new_value):
#     sql = f"UPDATE user SET {field_to_update} = %s WHERE user_id = %s"
#     update_values = [new_value, user_id]
#     try:
#         connection.execute_query(sql, update_values)
#         connection.commit_query()
#         return "User updated successfully"
#     except Exception as e:
#         return "Error while updating"
#
#
# def update_group(group_id: str, field_to_update: str, new_value: str):
#     sql = f"UPDATE group_chat SET {field_to_update} = %s WHERE group_id = %s"
#     update_values = [new_value, group_id]
#     try:
#         connection.execute_query(sql, update_values)
#         connection.commit_query()
#         return "Group updated successfully"
#     except Exception as e:
#         return "Error while updating"
#
#
# def update_massage(msg_id: str, field_to_update: str, new_value: str):
#     sql = f"UPDATE massage SET {field_to_update} = %s WHERE msg_id= %s"
#     update_values = [new_value, msg_id]
#     try:
#         connection.execute_query(sql, update_values)
#         connection.commit_query()
#         return "Message updated successfully"
#     except Exception as e:
#         return "Error while updating"
#
#
# # delete
# def delete_user_by_userid(userid):
#     sql_formula = "DELETE FROM user WHERE user_id = %s;"
#     user_id_info = [userid]
#     try:
#         connection.execute_query(sql_formula, user_id_info)
#         connection.commit_query()
#         return "successfully deleted"
#     except Exception as e:
#         return "not able to delete"
#
#
# def delete_contact(user_id, contact_id):
#     sql_formula = "DELETE FROM contacts WHERE user_id = %s AND user_s_contact_id = %s;"
#     contact_info = [user_id, contact_id]
#     try:
#         connection.execute_query(sql_formula, contact_info)
#         connection.commit_query()
#         return "successfully deleted"
#     except Exception as e:
#         return "not able to delete"
#
#
# def delete_group(chat_id):
#     sql_formula = "DELETE FROM group_chat WHERE chat_id = %s;"
#     group_info = [chat_id]
#     try:
#         connection.execute_query(sql_formula, group_info)
#         connection.commit_query()
#         return "successfully deleted"
#     except Exception as e:
#         return "not able to delete"
#
#
# def delete_group_member(chat_id, member_id):
#     sql_formula = "DELETE FROM group_membership WHERE chat_id = %s AND member_id = %s;"
#     member_info = [chat_id, member_id]
#     try:
#         connection.execute_query(sql_formula, member_info)
#         connection.commit_query()
#         return "successfully deleted"
#     except Exception as e:
#         return "not able to delete"
#
#
# def delete_msg(msg_id):
#     sql_formula = "DELETE FROM msg WHERE msg_id = %s;"
#     msg_info = [msg_id]
#     try:
#         connection.execute_query(sql_formula, msg_info)
#         connection.commit_query()
#         return "successfully deleted"
#     except Exception as e:
#         return "not able to delete"
#
#
# def delete_pv(chat_id):
#     sql_formula = "DELETE FROM pv_chat WHERE chat_id = %s;"
#     pv_info = [chat_id]
#     try:
#         connection.execute_query(sql_formula, pv_info)
#         connection.commit_query()
#         return "successfully deleted"
#     except Exception as e:
#         return "not able to delete"
# TODO

# # get the connection
# connection = DatabaseConnection(host='localhost', port="3307", user="root", password="password",
#                                 database="db")

# ////////////////////////////////
# my trials:

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
