CREATE TRIGGER log_user_insert AFTER INSERT ON user
FOR EACH ROW
BEGIN
  INSERT INTO log_table (timestamp, operation, table_name, record_id, new_data)
  VALUES (NOW(), 'INSERT', 'User', NEW.user_id, NEW);  -- Use JSON to store new data
END;


CREATE TRIGGER log_user_update AFTER UPDATE ON user
FOR EACH ROW
BEGIN
  INSERT INTO log_table (timestamp, operation, table_name, record_id, old_data, new_data)
  VALUES (NOW(), 'UPDATE', 'User', NEW.user_id, OLD, NEW);
END;



CREATE TRIGGER log_user_delete AFTER DELETE ON user
FOR EACH ROW
BEGIN
  INSERT INTO log_table (timestamp, operation, table_name, record_id)
  VALUES (NOW(), 'DELETE', 'User', OLD.user_id);
END;