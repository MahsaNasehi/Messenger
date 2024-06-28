from Model import check_query

from Model.DB_Connection import database_connection

connection = database_connection.DatabaseConnection()


# insertion / creation
def user_insertion(user_obj):
    sql_formula = ("INSERT INTO user (user_name, first_name, last_name, phone_number, join_date) VALUES (%s, %s, %s, "
                   "%s, %s)")
    user = [user_obj.user_name, user_obj.first_name, user_obj.last_name, user_obj.phone_number, user_obj.join_date]
    done = connection.execute_query(sql_formula, user)
    connection.commit_query()
    if done[0]:
        return "Added"
    else:
        return "Error while Adding"


def pv_chat_insertion(pv_obj):
    sql_formula = "INSERT INTO pv_chat (user1_id, user2_id) VALUES (%s, %s)"
    pv = [pv_obj.first_user_id, pv_obj.second_user_id]
    done = connection.execute_query(sql_formula, pv)
    connection.commit_query()
    if done[0]:
        return "Added"
    else:
        return "Error while Adding"


def group_chat_insertion(group_obj):
    sql_formula = "INSERT INTO group_chat (chat_name) VALUES (%s)"
    group = [group_obj.chat_name]
    done = connection.execute_query(sql_formula, group)
    connection.commit_query()
    if done[0]:
        return "Added"
    else:
        return "Error while Adding"


def group_member_insertion(member):
    sql_formula = "INSERT INTO group_membership (chat_id, member_id) VALUES (%s, %s)"
    member_info = [member.group_chat_id, member.member_id]
    done = connection.execute_query(sql_formula, member_info)
    connection.commit_query()
    if done[0]:
        return "Added"
    else:
        return "Error while Adding"


def contacts_insertion(contact):
    sql_formula = "INSERT INTO contacts (user_id, user_s_contact_id) VALUES (%s, %s)"
    contact_info = [contact.users_id, contact.users_contact_id]
    done = connection.execute_query(sql_formula, contact_info)
    connection.commit_query()
    if done[0]:
        return "Added"
    else:
        return "Error while Adding"


def message_insertion(message):
    continue_the_insertion = True
    if message.is_group_chat:
        continue_the_insertion = check_query.check_membershipism(message.sender_id, message.chat_id)
    if continue_the_insertion:
        sql_formula = "INSERT INTO msg (chat_id, pv_id, sender_id, content) VALUES (%s, %s, %s, %s)"
        if message.is_group_chat:
            msg = [message.chat_id, None, message.sender_id, message.content]
        else:
            msg = [None, message.chat_id, message.sender_id, message.content]

        done = connection.execute_query(sql_formula, msg)
        connection.commit_query()
        if done[0]:
            return "Added"
        else:
            return "Error while Adding"
    else:
        return "You are not member of this chat"
