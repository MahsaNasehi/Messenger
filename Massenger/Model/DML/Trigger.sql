CREATE TRIGGER log_user_insert AFTER INSERT ON user
FOR EACH ROW
BEGIN
  INSERT INTO log_table (timestamp, operation, table_name, record_id, user_info)
  VALUES (NOW(),'INSERT', 'User', NEW.user_id, USER());
END;


CREATE TRIGGER log_user_update AFTER UPDATE ON user
FOR EACH ROW
BEGIN
  INSERT INTO log_table (timestamp, operation, table_name, record_id, user_info)
  VALUES (NOW(), 'UPDATE', 'User', NEW.user_id, USER());
END;



CREATE TRIGGER log_user_delete AFTER DELETE ON user
FOR EACH ROW
BEGIN
  INSERT INTO log_table (timestamp, operation, table_name, record_id, user_info)
  VALUES (NOW(), 'DELETE', 'User', OLD.user_id, USER());
END;