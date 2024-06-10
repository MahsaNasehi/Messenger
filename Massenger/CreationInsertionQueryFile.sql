## create queries
CREATE TABLE IF NOT EXISTS user(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(15) UNIQUE ,
    first_name VARCHAR(10) NOT NULL ,
    last_name VARCHAR(10) NOT NULL ,
    phone_number CHAR(11) UNIQUE NOT NULL
);


CREATE TABLE  IF NOT EXISTS contacts(
    user_id INT,
    user_s_contact_id INT,
    PRIMARY KEY (user_id, user_s_contact_id),
    FOREIGN KEY(user_id) references user(user_id)ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY(user_s_contact_id) references user(user_id)ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS  group_chat(
    chat_id  INT PRIMARY KEY AUTO_INCREMENT,
    chat_name VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS pv_chat(
    chat_id  INT PRIMARY KEY AUTO_INCREMENT,
    user1_id INT NOT NULL,
    user2_id INT NOT NULL,
    FOREIGN KEY (user1_id) REFERENCES user(user_id) ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (user1_id) REFERENCES user(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS group_membership(
    chat_id INT,
    member_id INT,
    PRIMARY KEY (chat_id, member_id),
    FOREIGN KEY (chat_id) REFERENCES group_chat(chat_id) ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY  (member_id) REFERENCES user(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS  msg(
    msg_id  INT PRIMARY KEY AUTO_INCREMENT,
    chat_id INT DEFAULT NULL,
    pv_id INT DEFAULT NULL,
    sender_id INT NOT NULL ,
    content VARCHAR(100) NOT NULL,
#     CONSTRAINT enforce_one_not_null CHECK (chat_id IS NULL XOR pv_id IS NULL),
    FOREIGN KEY (chat_id) REFERENCES group_chat(chat_id) ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (pv_id) REFERENCES pv_chat(chat_id) ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (sender_id) REFERENCES user(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

# # trigger for constraint in msg
#     CREATE TRIGGER enforce_one_not_null_msg BEFORE INSERT ON msg
#     FOR EACH ROW
#     BEGIN
#         IF NEW.chat_id IS NULL AND NEW.pv_id IS NULL THEN
#             SIGNAL SQLSTATE '45000'  'Either chat_id or pv_id must be not null';
#         ELSEIF NEW.chat_id IS NOT NULL AND NEW.pv_id IS NOT NULL THEN
#                 SIGNAL SQLSTATE '45000' SET MESSAGE 'Only one of chat_id or pv_id can be not null';
#         END IF;
#     END
# #     // DELIMITER ;
## insert queries
INSERT INTO user(user_name, first_name, last_name, phone_number) VALUES
    ('u1', 'mahsa', 'nasehi', '09111111111'),
    ('u2', 'mahya', 'nasehi', '09111111112'),
    ('u3', 'parisa', 'sia', '09111111113'),
    ('u4', 'sara', 'gerami', '09111111114'),
    ('u5', 'mona', 'eradi', '09111111115'),
    ('u6', 'zahra', 'saha', '09111111116');

INSERT INTO user(user_name, first_name, last_name, phone_number) VALUES
    ('u7', 'mahan', 'nasehi', '09111111117');
INSERT INTO contacts(user_id, user_s_contact_id) VALUES
    ('1', '2'),
    ('1', '3'),
    ('2', '1'),
    ('5', '6'),
    ('5', '4');


INSERT INTO group_chat(chat_name) VALUES
    ('amar mohan'),
    ('CE'),
    ('mohajeran'),
    ('koodak'),
    ('safar'),
    ('uni'),
    ('hobby');

INSERT INTO pv_chat(user1_id, user2_id) VALUES
    ('1', '2'),
    ('1', '4'),
    ('5', '4'),
    ('2', '6');


INSERT INTO group_membership(chat_id, member_id) VALUES
    ('1', '1'),
    ('1', '2'),
    ('3', '4'),
    ('3', '5'),
    ('4', '1'),
    ('4', '3'),
    ('6', '6');


INSERT INTO msg(chat_id, pv_id, sender_id, content)  VALUES
    ('1', NULL, '1', 'Hi everybody! group c1'),
    ('1', NULL, '2', 'Hi mahsa! yes c1 group'),
    (NULL, '1', '1', 'Hi mahya, this is our pv'),
    (NULL, '1', '2', 'Hi mahsa, yes our pv'),
    (NULL, '3', '5', 'Hi sara, I am mona, this is our pv');