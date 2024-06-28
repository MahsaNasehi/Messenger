ALTER TABLE user
ADD last_seen DATETIME;

ALTER TABLE group_chat
ADD admin varchar(20);