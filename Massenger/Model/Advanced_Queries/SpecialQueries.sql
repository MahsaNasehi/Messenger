# delete all users who are not added into any groups
DELETE FROM user WHERE user_id NOT IN(
    SELECT member_id FROM group_membership
    );


# info of each user with her/his groups
SELECT user_name, first_name, last_name, phone_number, chat_name
FROM group_chat, group_membership, user
WHERE user_id = member_id AND group_chat.chat_id = group_membership.chat_id
UNION
SELECT user_name, first_name, last_name, phone_number, null as chat_name
FROM user LEFT JOIN group_membership ON user.user_id = group_membership.member_id
WHERE group_membership.chat_id IS NULL OR group_membership.chat_id = '';



# info of the users and their messages' count in a special group
SELECT user.user_name, user.first_name, user.last_name, user.phone_number,COUNT(msg.msg_id) AS message_count
FROM user JOIN group_chat JOIN group_membership JOIN msg
ON user.user_id = msg.sender_id AND user.user_id = group_membership.member_id AND
   group_chat.chat_id = group_membership.chat_id AND  group_chat.chat_id = msg.chat_id
WHERE group_chat.chat_name = 'amar mohan'
GROUP BY user.user_id
ORDER BY  message_count DESC;

# each group with its complete info has how many members that have pv_chat with each other
SELECT group_chat.chat_id, group_chat.chat_name,
       COALESCE(COUNT(DISTINCT CASE WHEN pv_chat.user1_id IS NOT NULL THEN M1.member_id END), 0)
        AS count_users_having_pv
FROM group_membership AS M1
JOIN group_membership AS M2
    ON M1.chat_id = M2.chat_id AND M1.member_id != M2.member_id
JOIN group_chat
    ON M1.chat_id = group_chat.chat_id
LEFT JOIN pv_chat ON
    (pv_chat.user1_id = M1.member_id AND pv_chat.user2_id = M2.member_id) OR
    (pv_chat.user1_id = M2.member_id AND pv_chat.user2_id = M1.member_id)
GROUP BY chat_iD;

# users that joined our messanger in a special date and send more than one message in at least 2 groups
SELECT distinct sender_id, user.first_name, user.last_name
FROM msg
JOIN group_membership ON msg.sender_id = group_membership.member_id
                     AND msg.chat_id = group_membership.member_id
JOIN user ON user_id = sender_id
WHERE date(user.join_date) = '2009-10-04'
GROUP BY msg.sender_id, msg.chat_id
HAVING COUNT(msg.msg_id) > 1
LIMIT 0, 1000;


SELECT DISTINCT M.sender_id
FROM msg as M
JOIN user ON M.sender_id = user.user_id
WHERE user.join_date = '2009-10-04' AND chat_id IS NOT NULL
GROUP BY M.sender_id
HAVING (
SELECT COUNT(*) FROM (
SELECT chat_id FROM msg
WHERE sender_id = M.sender_id AND msg.chat_id IS NOT NULL
GROUP BY chat_id
HAVING COUNT(*) > 1
) AS subquery
) >= 2;



# users that are co_member with a special user in at least one group
SELECT  distinct U.user_id, U.first_name, U.last_name, U.phone_number
FROM user AS U
JOIN group_membership AS M ON U.user_id = M.member_id
WHERE M.chat_id IN (
    SELECT chat_id
    FROM group_membership
    WHERE member_id = 3
) AND U.user_id != 3;