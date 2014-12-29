import csv
from collections import defaultdict
zones = csv.DictReader(open('zone_complete.csv', "rb"))
zonedict = defaultdict(dict)
zonekeys = []

for row in zones:
    key = row['trans_id']
    if key not in zonedict:
        zonedict[key] = defaultdict(str)
        zonedict[key]['row_id_1'] = row['row_id']
        zonedict[key]['status_1'] = row['status']
        zonedict[key]['zone_1'] = row['zone']
        zonedict[key]['odd_even_1'] = row['odd_even']
        zonedict[key]['ar_low_1'] = row['ar_low']
        zonedict[key]['ar_high_1'] = row['ar_high']
        if row['buffer'] == "t":
            zonedict[key]['buffer_1'] = "Buffer"
        else:
            zonedict[key]['buffer_1'] = "Zone"
        zonedict[key]['street_direction'] = row['street_direction']
        zonedict[key]['street_name'] = row['street_name']
        zonedict[key]['street_type'] = row['street_type']
        zonedict[key]['second_street_direction'] = row['second_street_direction']
        zonedict[key]['geom'] = row['geom']
        zonedict[key]['geomtext'] = row['geomtext']
        zonedict[key]['trans_id'] = row['trans_id']
        zonedict[key]['buffercheck'] = zonedict[key]['buffer_1']
    elif 'row_id_2' not in zonedict[key]:
        zonedict[key]['row_id_2'] = row['row_id']
        zonedict[key]['status_2'] = row['status']
        zonedict[key]['zone_2'] = row['zone']
        zonedict[key]['odd_even_2'] = row['odd_even']
        zonedict[key]['ar_low_2'] = row['ar_low']
        zonedict[key]['ar_high_2'] = row['ar_high']
        if row['buffer'] == "t":
            zonedict[key]['buffer_2'] = "Buffer"
        else:
            zonedict[key]['buffer_2'] = "Zone"        
        zonedict[key]['buffercheck'] = zonedict[key]['buffercheck'] + zonedict[key]['buffer_2']
    elif 'row_id_3' not in zonedict[key]:
        zonedict[key]['row_id_3'] = row['row_id']
        zonedict[key]['status_3'] = row['status']
        zonedict[key]['zone_3'] = row['zone']
        zonedict[key]['odd_even_3'] = row['odd_even']
        zonedict[key]['ar_low_3'] = row['ar_low']
        zonedict[key]['ar_high_3'] = row['ar_high']
        if row['buffer'] == "t":
            zonedict[key]['buffer_3'] = "Buffer"
        else:
            zonedict[key]['buffer_3'] = "Zone"  
        zonedict[key]['buffercheck'] = zonedict[key]['buffercheck'] + zonedict[key]['buffer_3']
    elif 'row_id_4' not in zonedict[key]:
        zonedict[key]['row_id_4'] = row['row_id']
        zonedict[key]['status_4'] = row['status']
        zonedict[key]['zone_4'] = row['zone']
        zonedict[key]['odd_even_4'] = row['odd_even']
        zonedict[key]['ar_low_4'] = row['ar_low']
        zonedict[key]['ar_high_4'] = row['ar_high']
        if row['buffer'] == "t":
            zonedict[key]['buffer_4'] = "Buffer"
        else:
            zonedict[key]['buffer_4'] = "Zone"  
        zonedict[key]['buffercheck'] = zonedict[key]['buffercheck'] + zonedict[key]['buffer_4']
    elif 'row_id_5' not in zonedict[key]:
        zonedict[key]['row_id_5'] = row['row_id']
        zonedict[key]['status_5'] = row['status']
        zonedict[key]['zone_5'] = row['zone']
        zonedict[key]['odd_even_5'] = row['odd_even']
        zonedict[key]['ar_low_5'] = row['ar_low']
        zonedict[key]['ar_high_5'] = row['ar_high']
        if row['buffer'] == "t":
            zonedict[key]['buffer_5'] = "Buffer"
        else:
            zonedict[key]['buffer_5'] = "Zone"  
        zonedict[key]['buffercheck'] = zonedict[key]['buffercheck'] + zonedict[key]['buffer_5']
    elif 'row_id_6' not in zonedict[key]:
        zonedict[key]['row_id_6'] = row['row_id']
        zonedict[key]['status_6'] = row['status']
        zonedict[key]['zone_6'] = row['zone']
        zonedict[key]['odd_even_6'] = row['odd_even']
        zonedict[key]['ar_low_6'] = row['ar_low']
        zonedict[key]['ar_high_6'] = row['ar_high']
        if row['buffer'] == "t":
            zonedict[key]['buffer_6'] = "Buffer"
        else:
            zonedict[key]['buffer_6'] = "Zone"  
        zonedict[key]['buffercheck'] = zonedict[key]['buffercheck'] + zonedict[key]['buffer_6']
    zonekeys.extend(zonedict[key].keys()) 
    zonekeys = list(set(zonekeys))

with open ('zones_final.csv', 'wb') as csvfile:
    fieldnames = ['trans_id','buffercheck','street_direction','street_name','street_type','second_street_direction','row_id_1','zone_1','buffer_1','status_1','odd_even_1','ar_low_1','ar_high_1','row_id_2','zone_2','buffer_2','status_2','odd_even_2','ar_low_2','ar_high_2','row_id_3','zone_3','buffer_3','status_3','odd_even_3','ar_low_3','ar_high_3','row_id_4','zone_4','buffer_4','status_4','odd_even_4','ar_low_4','ar_high_4','row_id_5','zone_5','buffer_5','status_5','odd_even_5','ar_low_5','ar_high_5','row_id_6','zone_6','buffer_6','status_6','odd_even_6','ar_low_6','ar_high_6','geom','geomtext']
    #fieldnames = zonekeys
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for key, value in zonedict.iteritems():
        if value['buffercheck'].find('Buffer') == -1:
            value['buffercheck'] = "Zone Only"
        elif value['buffercheck'].find('Zone') == -1:
            value['buffercheck'] = "Buffer Only"
        else:
            value['buffercheck'] = "Zone & Buffer"
        writer.writerow(value)
