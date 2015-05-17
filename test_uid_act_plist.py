import re
f = open('EHC_2nd_round_test.log', 'r')
f2 = open('test_uid_act_pid_num_price.txt','w')
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

	f2.write( "%s\t%s\t%s\t%s\n"%(act, uid, erUid, pid) )

f2.close()
f.close()

