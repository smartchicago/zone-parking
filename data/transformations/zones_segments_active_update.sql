

(select 
row_id,
status,
zone,
odd_even,
ar_low,
ar_high,
buffer,
trans_id_low as trans_id,
street_direction,
street_name,
street_type,
second_street_direction,
ST_Transform(geom_low, 4326) as geom,
ST_AsText(ST_Transform(geom_low, 4326)) as geomtext

from zones where status = 'ACTIVE' and trans_id_low = trans_id_high)
UNION
(select 
row_id,
status,
zone,
odd_even,
ar_low,
ar_high,
buffer,
trans_id_low as trans_id,
street_direction,
street_name,
street_type,
second_street_direction,
ST_Transform(geom_low, 4326) as geom,
ST_AsText(ST_Transform(geom_low, 4326)) as geomtext
from zones where status = 'ACTIVE' and trans_id_low <> trans_id_high)
UNION
(select 
row_id,
status,
zone,
odd_even,
ar_low,
ar_high,
buffer,
trans_id_high as trans_id,
street_direction,
street_name,
street_type,
second_street_direction,
ST_Transform(geom_high, 4326) as geom,
ST_AsText(ST_Transform(geom_high, 4326)) as geomtext
from zones where status = 'ACTIVE' and trans_id_low <> trans_id_high)
order by trans_id, odd_even, ar_low, ar_high;
