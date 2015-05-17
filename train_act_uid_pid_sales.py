import re

print "Starting..."
path_in  = 'analysis/train_uid_act_pid_num_price.txt'
path_out = 'analysis/train_uid_act_pid_sales.txt'
path_map = 'analysis/train_uid_erUid.txt'
fin  = open(path_in, 'r')
fout = open(path_out,'w')
f_map = open(path_map, 'r')

print "Building & Counting & Summing ..."
recs = dict()
pid_count   = dict()
pid_count['view']   = dict()
pid_count['search'] = dict()
pid_sales  = dict()
pid_orders = dict()
pid_act_sales = dict()

for line in fin.readlines():
        ele =  line.strip()
	fields= ele.split('\t')
	field_no = len(fields)
	if ( field_no < 6 ):
		print ele
		print fields

	act    = fields[0]
	uid    = fields[1]
	eruid  = fields[2]
	pid    = fields[3]
	num    = fields[4]
	if (field_no > 5):
		price  = fields[5]
		if ( (num<>'N') and (price<>'N') ):
			sales  = int(num) * int(price)

	key = act + '_' + uid + '_' + eruid + '_' + pid
	if ( act=='order' ):
		if (pid in pid_orders):
			pid_orders[pid] = pid_orders[pid] + 1
		else:
			pid_orders[pid] = 1

		if ( key in recs ):
			recs[ key ] = recs[ key ] + sales
			pid_sales[pid] = pid_sales[pid] + sales
		else:
			recs[ key ] = sales
			if ( pid in pid_sales ):
				pid_sales[pid] = pid_sales[pid] + sales
			else:
				pid_sales[pid] = sales

	else:  # view, search
		if ( key in recs ): # limit the same act-user-pid only one time
			print fields
			recs[ key ] = 1
		else:  # new act-uid-eric-pid
			if ( (act=='view') or (act=='search') ):
				if (pid not in pid_act_sales):
					pid_act_sales[ pid ] = dict()
				if (act in pid_act_sales[ pid ]):
					pid_act_sales[pid][act] = pid_act_sales[pid][act] + 1
				else:
					pid_act_sales[pid][act] = 1

		
f_map.close()
print "Start writing to file %s ..."%(path_out)

for id in pid_sales :
	if (id not in pid_act_sales):
		pid_act_sales[ id ] = dict()
	pid_act_sales[ id ]["sales"] = pid_sales[ id ]
	pid_act_sales[ id ]["orders"] = pid_orders[ id ]


# write output file
for id in pid_act_sales:
	if ( 'view' not in pid_act_sales[id] ):
		pid_act_sales[id]['view'] = 0
	if ( 'search' not in pid_act_sales[id] ):
		pid_act_sales[id]['search'] = 0
	if ( 'orders' not in pid_act_sales[id] ):
		pid_act_sales[id]['orders'] = 0
	if ( 'sales' not in pid_act_sales[id] ):
		pid_act_sales[id]['sales'] = 0
	
	if (id == 'N'):
		continue

	fout.write( "%s\t%s\t%s\t%s\t%s\n"%(id, pid_act_sales[id]['view'], \
		 pid_act_sales[id]['search'], pid_act_sales[id]['orders'], \
		pid_act_sales[id]['sales'] ) )


fout.close()
fin.close()

