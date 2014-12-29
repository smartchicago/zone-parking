select t.trans_id,
z.street_direction,
t.pre_dir,
z.street_name,
t.street_nam,
z.street_type,
t.street_typ,
z.second_street_direction,
t.suf_dir,
z.row_id,
z.ar_low,
t.logiclf,
t.logiclt,
z.zone
from
transportation t,
zones z
where
z.street_name = t.street_nam
and
z.street_direction = t.pre_dir
and
z.street_type = t.street_typ
and
t.logiclf <= z.ar_low
AND
t.logiclt >= z.ar_low
and
t.l_parity = z.odd_even

ALTER TABLE zones ADD COLUMN trans_id_low integer;
ALTER TABLE zones ADD COLUMN trans_id_high integer;
ALTER TABLE zones ADD COLUMN geom_low geometry(MultiLineString,3435);
ALTER TABLE zones ADD COLUMN geom_high geometry(MultiLineString,3435);

ALTER TABLE zones DROP COLUMN trans_id_low2;
ALTER TABLE zones DROP COLUMN trans_id_high2;

---------------------------------------------------------------------------
update zones
Set trans_id_low = transportation.trans_id,
    geom_low = transportation.geom
from transportation
where
zones.street_name = transportation.street_nam
and
zones.street_direction = transportation.pre_dir
and
zones.street_type = transportation.street_typ
and
transportation.logiclf <= zones.ar_low
AND
transportation.logiclt >= zones.ar_low
and
transportation.l_parity = zones.odd_even;
---------------------------------------------------------------------------
update zones
Set trans_id_high = transportation.trans_id,
    geom_high = transportation.geom
from transportation
where
zones.street_name = transportation.street_nam
and
zones.street_direction = transportation.pre_dir
and
zones.street_type = transportation.street_typ
and
transportation.logiclf <= zones.ar_high
AND
transportation.logiclt >= zones.ar_high
and
transportation.l_parity = zones.odd_even;
---------------------------------------------------------------------------

----------------------------------------------------------------------

update zones
Set trans_id_low = transportation.trans_id,
    geom_low = transportation.geom
from transportation
where
zones.street_name = transportation.street_nam
and
zones.street_direction = transportation.pre_dir
and
zones.street_type = transportation.street_typ
and
transportation.logicrf <= zones.ar_low
AND
transportation.logicrt >= zones.ar_low
and
transportation.r_parity = zones.odd_even;
---------------------------------------------------------------------------
update zones
Set trans_id_high = transportation.trans_id,
    geom_high = transportation.geom
from transportation
where
zones.street_name = transportation.street_nam
and
zones.street_direction = transportation.pre_dir
and
zones.street_type = transportation.street_typ
and
transportation.logicrf <= zones.ar_high
AND
transportation.logicrt >= zones.ar_high
and
transportation.r_parity = zones.odd_even;

---------------------------------------------------------------------


