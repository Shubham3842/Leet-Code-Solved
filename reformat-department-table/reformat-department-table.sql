/* Write your T-SQL query statement below */
select id,
MAX(CASE WHEN month = 'Jan' THEN revenue else NULL end) as Jan_Revenue,
MAX(CASE WHEN month ='Feb' THEN revenue else NULL end) as Feb_Revenue,
MAX(CASE WHEN month ='Mar' THEN revenue else NULL end) as Mar_Revenue,
MAX(CASE WHEN month ='Apr' THEN revenue else NULL end) as Apr_Revenue,
MAX(CASE WHEN month ='May' THEN revenue else NULL end) as May_Revenue,
MAX(CASE WHEN month ='Jun' THEN revenue else NULL end) as Jun_Revenue,
MAX(CASE WHEN month ='Jul' THEN revenue else NULL end) as Jul_Revenue,
MAX(CASE WHEN month ='Aug' THEN revenue else NULL end) as Aug_Revenue,
MAX(CASE WHEN month ='Sep' THEN revenue else NULL end) as Sep_Revenue,
MAX(CASE WHEN month ='Oct' THEN revenue else NULL end) as Oct_Revenue,
MAX(CASE WHEN month ='Nov' THEN revenue else NULL end) as Nov_Revenue,
MAX(CASE WHEN month ='Dec' THEN revenue else NULL end) as Dec_Revenue
from department
group by id
