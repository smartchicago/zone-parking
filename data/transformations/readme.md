Psuedo description of creating data (I will expand this soon):
1. Get Parking Zone data from https://data.cityofchicago.org/Transportation/Parking-Permit-Zones/u9xt-hiju
2. Get Street Center lines from https://data.cityofchicago.org/Transportation/Street-Center-Lines/6imu-meau
3. For each zone record in (1), find the matching street center line for both address_range__low and address_range__high by matching street name and checking if it is within the segment's address range. (see add_transid_to_zones.sql)
4. Filter for only active zones and export zone information and segment geometry (zones_segments_active_update.sql)
5. Combine zone records so that there is only one record for each street segment, cleanup for simple infowindow, and buffer/zone symbology. (trans_zone_join.py)
