# contains tuples with user's info and her/his message
CREATE VIEW user_messege AS
SELECT user.user_name, user.first_name, user.last_name, user.phone_number, msg.content AS message
FROM user, msg
WHERE user.user_id = msg.sender_id
ORDER BY user_name;


# user's name and her/his contact's name
CREATE VIEW user_contacts AS
SELECT u1.first_name AS User_Fname, u1.last_name AS User_Lname,
       u2.first_name AS Contact_Fname, u2.last_name AS Contact_Lname
FROM user u1
JOIN contacts c ON u1.user_id = c.user_id
JOIN user u2 ON c.user_s_contact_id = u2.user_id
ORDER BY u1.first_name, u1.last_name;


# user's name and her/his group's name with messages that she/he sent in that group
CREATE VIEW user_messege_group AS
SELECT u1.first_name AS User_Fname, u1.last_name AS User_Lname,
       g.chat_name Chat_name,
       m.content Message
FROM user u1
JOIN group_membership gm ON u1.user_id = gm.member_id
JOIN group_chat g ON gm.chat_id = g.chat_id
JOIN msg m ON g.chat_id = m.chat_id AND u1.user_id = m.sender_id
ORDER BY u1.first_name, u1.last_name;