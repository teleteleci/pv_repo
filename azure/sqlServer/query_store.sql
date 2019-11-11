SELECT
       rs.first_execution_time [fet],
       rs.last_execution_time [lat],
       q.query_id ,
       t.query_sql_text,
       rs.*
FROM
       sys.query_store_query q
       JOIN sys.query_store_query_text t ON q.query_text_id = t.query_text_id
       JOIN sys.query_store_plan p ON p.query_id = q.query_id
       JOIN sys.query_store_runtime_stats rs ON rs.plan_id = p.plan_id
WHERE rs.first_execution_time like '2019-10-01 14%'
  and rs.last_execution_time like '2019-10-01 14%'
order by 
  rs.max_duration -- 1839332	
--   rs.max_cpu_time -- 1839332		
--   rs.avg_cpu_time -- 1839332	
--   rs.max_logical_io_reads -- 1839332	
--   rs.max_physical_io_reads -- 696	
  -- rs.max_query_max_used_memory -- 1382241	

desc;



-- SELECT * from sys.query_store_query where query_id = 1839332;
-- select * from sys.query_store_query_text where query_text_id = 479812	;
-- SELECT * from sys.query_store_plan;
-- select * from sys.query_store_runtime_stats;

select t.query_sql_text
from sys.query_store_query q
inner join sys.query_store_query_text t on t.query_text_id = q.query_text_id
where q.query_id = 1839332;


