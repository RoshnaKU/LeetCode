/* Write your PL/SQL query statement below */
SELECT t.request_at as "Day",
ROUND(AVG(CASE WHEN t.status!='completed' THEN 1 ELSE 0 END), 2) as "Cancellation Rate"
FROM Trips t
where t.client_id in (select users_id from Users where role='client' and banned='No') 
and  t.driver_id in (select users_id from Users where role='driver' and banned='No') 
and t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at
ORDER BY t.request_at