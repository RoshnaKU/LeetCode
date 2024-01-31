/* Write your PL/SQL query statement below */
with dis_val as
(SELECT  distinct customer_id ,product_key from Customer ),
c_p as (SELECT customer_id,count(*) as cnt FROM dis_val group by customer_id) 
,
p_cnt as (SELECT count(product_key) as tot from product)
SELECT customer_id from c_p where cnt in (SELECT tot from p_cnt)
