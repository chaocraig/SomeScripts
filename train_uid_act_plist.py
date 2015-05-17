import re
f = open('EHC_2nd_round_train.log', 'r')
f2 = open('train_uid_act_pid_num_price.txt','w')
print "Starting..."


f_map = open('analysis/train_uid_erUid.txt', 'r')
print "Loading uid-eruid mapping..."
eruid_uid = dict()
for line in f_map.readlines():
        ele =  line.strip()
	ids = ele.split('\t')
	eruid_uid[ ids[1] ] = ids[0]
	#print ids
f_map.close()

for line in f.readlines():
        ele =  line.strip()
        m1 = re.match('.*act=(.*?);.*', ele)
        act = m1.group(1) if m1 else Nonw
	act = act if act else 'N'

        m2 = re.match('.*uid=(.*?);.*', ele)
        uid = m2.group(1) if m2 else None
	uid = uid if uid else 'N'

        m3 = re.match('.*erUid=(.*?);.*', ele)
        erUid = m3.group(1) if m3 else None
	if (erUid):
		if ( (erUid in eruid_uid) and uid=='N' ):
			uid = eruid_uid[ erUid ]
			#print "%s-> erUid:%s\tuid:%s"%(act, erUid, uid)
	else:
		erUid = 'N'

        m4 = re.match('.*pid=(.*?);.*', ele)
        pid = m4.group(1) if m4 else None
	pid = pid if pid else 'N'


        m6 = re.match('.*plist=(.*?);.*', ele)
        plist = m6.group(1) if m6 else None
	plist = plist if plist else 'N'

        if (plist<>'N' and act=='order'):
		prod_num_price = plist.split(',')
		for i in range(0, len(prod_num_price), 3):
        		f2.write("%s\t%s\t%s\t%s\t%s\t%s\n"%(act, uid, erUid, prod_num_price[i], \
			prod_num_price[i+1], prod_num_price[i+2] ))
	else:
		f2.write( "%s\t%s\t%s\t%s\t%s\t%s\n"%(act, uid, erUid, pid, 'N', 'N') )

f2.close()
f.close()

