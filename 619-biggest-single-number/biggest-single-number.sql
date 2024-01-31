/* Write your PL/SQL query statement below */
with cnt_t as
(SELECT num,count(*) as cnt from MyNumbers group by num having count(*)=1
order by num desc)
select max(num) as num  from cnt_t