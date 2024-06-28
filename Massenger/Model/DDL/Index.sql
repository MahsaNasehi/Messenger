# for active users in the past 24 hrs
CREATE INDEX last_seen_index ON user(last_seen);

# for finding history in pv messages
CREATE INDEX pv_find_index ON msg(pv_id);