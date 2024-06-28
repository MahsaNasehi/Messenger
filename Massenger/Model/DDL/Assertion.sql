# MYSQL doesn't support assertion
# so I add Check clauses

# 1
ALTER TABLE `user`
ADD CONSTRAINT `unique_mobile` UNIQUE (`phone_number`);

# 2
ALTER TABLE `group_chat`
ADD CONSTRAINT `unique_admin` UNIQUE (`admin`);