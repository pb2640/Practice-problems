# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

# delete 
# from 
# Person 
# where id in
# (select 
#  a.id
#  from Person as a,Person as b
# where a.Email=b.Email and a.id>=b.id )