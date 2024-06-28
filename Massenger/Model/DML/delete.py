from Model.DB_Connection import database_connection

connection = database_connection.DatabaseConnection()


# delete
def delete_user_by_userid(userid):
    sql_formula = "DELETE FROM user WHERE user_id = %s;"
    user_id_info = [userid]
    done = connection.execute_query(sql_formula, user_id_info)
    connection.commit_query()
    if done[0]:
        return "Successfully deleted"
    else:
        return "Not able to delete"


def delete_contact(user_id, contact_id):
    sql_formula = "DELETE FROM contacts WHERE user_id = %s AND user_s_contact_id = %s;"
    contact_info = [user_id, contact_id]
    done = connection.execute_query(sql_formula, contact_info)
    connection.commit_query()
    if done[0]:
        return "Successfully deleted"
    else:
        return "Not able to delete"


def delete_group(chat_id):
    sql_formula = "DELETE FROM group_chat WHERE chat_id = %s;"
    group_info = [chat_id]
    done = connection.execute_query(sql_formula, group_info)
    connection.commit_query()
    if done[0]:
        return "Successfully deleted"
    else:
        return "Not able to delete"

def delete_group_member(chat_id, member_id):
    sql_formula = "DELETE FROM group_membership WHERE chat_id = %s AND member_id = %s;"
    member_info = [chat_id, member_id]
    done = connection.execute_query(sql_formula, member_info)
    connection.commit_query()
    if done[0]:
        return "Successfully deleted"
    else:
        return "Not able to delete"


def delete_msg(msg_id):
    sql_formula = "DELETE FROM msg WHERE msg_id = %s;"
    msg_info = [msg_id]
    done = connection.execute_query(sql_formula, msg_info)
    connection.commit_query()
    if done[0]:
        return "Successfully deleted"
    else:
        return "Not able to delete"


def delete_pv(chat_id):
    sql_formula = "DELETE FROM pv_chat WHERE chat_id = %s;"
    pv_info = [chat_id]
    done = connection.execute_query(sql_formula, pv_info)
    connection.commit_query()
    if done[0]:
        return "Successfully deleted"
    else:
        return "Not able to delete"
