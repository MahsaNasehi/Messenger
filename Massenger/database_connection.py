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

    def get_result_rows(self):
        return self.connection_cursor.fetchall()

    def close_connection(self):
        if self.db_connector_obj.is_connected():
            self.connection_cursor.close()
            self.db_connector_obj.close()

# TODO
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
