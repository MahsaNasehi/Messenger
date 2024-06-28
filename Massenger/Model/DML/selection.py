from Model.DB_Connection import database_connection

connection = database_connection.DatabaseConnection()


# read from tables
def select_usertable_by_userid(userid):
    sql_formula = "SELECT * FROM user WHERE user_id = %s"
    user_id_info = [userid]
    done = connection.execute_query(sql_formula, user_id_info)
    result = connection.get_result_rows()
    if done[0]:
        return result
    else:
        return "Error while reading user table"
    # try:
    #
    #     return result
    # except Exception as e:
    #     return "Error while reading"


def select_contactstable_by_userid(userid):
    sql_formula = "SELECT * FROM contacts WHERE user_id = %s"
    user_id_info = [userid]
    done = connection.execute_query(sql_formula, user_id_info)
    result = connection.get_result_rows()
    if done[0]:
        return result
    else:
        return "Error while reading contacts table"


def select_grouptable_by_id(group_id):
    sql_formula = "SELECT * FROM group_chat WHERE chat_id = %s"
    group_info = [group_id]
    done = connection.execute_query(sql_formula, group_info)
    result = connection.get_result_rows()
    if done[0]:
        return result
    else:
        return "Error while reading group table"


def select_group_membertable_by_userid(userid):
    sql_formula = "SELECT * FROM group_membership WHERE member_id = %s"
    user_id_info = [userid]
    done = connection.execute_query(sql_formula, user_id_info)
    result = connection.get_result_rows()
    if done[0]:
        return result
    else:
        return "Error while reading membership table"


def select_msgtable_by_userid(msg_id):
    sql_formula = "SELECT * FROM msg WHERE msg_id = %s"
    msg_id_info = [msg_id]
    done = connection.execute_query(sql_formula, msg_id_info)
    result = connection.get_result_rows()
    if done[0]:
        return result
    else:
        return "Error while reading msg table"


def select_pvtable_by_userid(pv_id):
    sql_formula = "SELECT * FROM pv_chat WHERE chat_id = %s"
    pv_id_info = [pv_id]
    done = connection.execute_query(sql_formula, pv_id_info)
    result = connection.get_result_rows()
    if done[0]:
        return result
    else:
        return "Error while reading pv table"
