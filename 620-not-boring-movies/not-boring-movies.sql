/* Write your PL/SQL query statement below */
SELECT *
FROM Cinema
where description!='boring' and MOD(id,2)!=0
order by rating desc