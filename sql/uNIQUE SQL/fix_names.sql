# Write your MySQL query statement below


select user_id,
CONCAT(UPPER(SUBSTR(name,1,1)),LOWER(SUBSTR(NAME,2))) AS name
FROM USERS 
order by 
user_id


















# SELECT USER_ID as user_id,
# CONCAT(UPPER(SUBSTR(USERS.NAME,1,1)),LOWER(SUBSTR(USERS.NAME,2)))
# AS name
# FROM USERS
# ORDER BY USER_ID