import re
f = open('EHC_2nd_round_train.log', 'r')
f2 = open('EHC_2nd_round_train.log.out','w')
for line in f.readlines():
        ele =  line.strip()
        m1 = re.match('.*act=(.*?);.*', ele)
        act = m1.group(1) if m1 else None
        m2 = re.match('.*uid=(.*?);.*', ele)
        uid = m2.group(1) if m2 else None
        m3 = re.match('.*erUid=(.*?);.*', ele)
        erUid = m3.group(1) if m3 else None
        m4 = re.match('.*pid=(.*?);.*', ele)
        pid = m4.group(1) if m4 else None
        m5 = re.match('.*cat=(.*?);.*', ele)
        cat = m5.group(1) if m5 else None
        m6 = re.match('.*plist=(.*?);.*', ele)
        plist = m6.group(1) if m6 else None
        f2.write("%s\t%s\t%s\t%s\t%s\t%s\n"%(act, uid, erUid, pid, cat, plist))
f2.close()
f.close()

