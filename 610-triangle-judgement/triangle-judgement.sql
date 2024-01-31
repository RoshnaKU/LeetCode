/* Write your PL/SQL query statement below */
SELECT x,y,z,
CASE WHEN (x+y+z)-greatest(x,y,z) >GREATEST(x,y,z) THEN 'Yes'
ELSE 'No' END as triangle
from Triangle