import database_connection

connection = database_connection.DatabaseConnection()
def check_membershipism(sender_id, group_chat_id):
    query = "SELECT * FROM group_membership WHERE member_id = %s AND chat_id = %s"
    info_list = [sender_id, group_chat_id]
    connection.execute_query(query, info_list)
    result = connection.get_one_row()
    if len(result) == 0:
        return False
    else:
        return True
