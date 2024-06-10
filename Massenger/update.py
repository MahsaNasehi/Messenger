import database_connection

connection = database_connection.DatabaseConnection()


# update
def update_user(user_id, field_to_update, new_value):
    if field_to_update == "user_id":
        return "You are not allowed to update id"
    sql = f"UPDATE user SET {field_to_update} = %s WHERE user_id = %s"
    update_values = [new_value, user_id]
    done = connection.execute_query(sql, update_values)
    connection.commit_query()
    if done[0]:
        return "User updated successfully"
    else:
        return "Error while updating"


def update_group(group_id: int, field_to_update: str, new_value: str):
    if field_to_update == "chat_id":
        return "You are not allowed to update id"

    sql = f"UPDATE group_chat SET {field_to_update} = %s WHERE chat_id = %s"
    update_values = [new_value, group_id]
    done = connection.execute_query(sql, update_values)
    connection.commit_query()
    if done[0]:
        return "Group updated successfully"
    else:
        return "Error while updating"


def update_massage(msg_id: int, field_to_update: str, new_value: str):
    if field_to_update == "msg_id":
        return "You are not allowed to update id"
    sql = f"UPDATE msg SET {field_to_update} = %s WHERE msg_id= %s"
    update_values = [new_value, msg_id]
    done = connection.execute_query(sql, update_values)
    connection.commit_query()
    if done[0]:
        return "Message updated successfully"
    else:
        return "Error while updating"
