CREATE FUNCTION count_messages_between_users(user1_id INT, user2_id INT)
RETURNS INTEGER
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE D_COUNT INTEGER;

    SELECT COUNT(*) INTO D_COUNT
    FROM msg JOIN pv_chat ON msg.pv_id = pv_chat.chat_id
     WHERE (pv_chat.user1_id = user1_id AND pv_chat.user2_id = user2_id) OR
          (pv_chat.user1_id = user2_id AND pv_chat.user2_id = user1_id);

    RETURN D_COUNT;
END;

