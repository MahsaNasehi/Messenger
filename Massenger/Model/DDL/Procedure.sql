CREATE PROCEDURE search_messages(IN keyword TEXT)
BEGIN
    SELECT content
    FROM msg
    WHERE content LIKE CONCAT('%', keyword, '%');
END;


CREATE PROCEDURE get_recent_active_users()
BEGIN
    SELECT DISTINCT user_id
    FROM user
    WHERE last_seen > DATE(NOW() - INTERVAL 1 DAY);
END;


CREATE PROCEDURE get_conversation_history(user1_id INT, user2_id INT, limit_val INT)
BEGIN
    SET @query = CONCAT('SELECT content AS message
                        FROM pv_chat JOIN msg
                        ON pv_chat.chat_id = msg.pv_id
                        WHERE (pv_chat.user1_id = ', user1_id, ' AND pv_chat.user2_id = ', user2_id, ') OR
                              (pv_chat.user1_id = ', user2_id, ' AND pv_chat.user2_id = ', user1_id, ')
                        LIMIT ', limit_val);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END;


