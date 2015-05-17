import re, sys,json
f = open('out/MergeParsed.out','r')
dic = {}
for line in f.readlines():
        ele =  line.strip()
        info = ele.split('\t')
        if info[1] == 'view':
                if info[2] not in dic:
                        dic[info[2]] = {'uid': info[2], 'view':[info[4]]}
                else:
                        dic[info[2]]['view'].append(info[4])
        elif info[1] == 'order':
                if info[2] in dic:
                        dic[info[2]]['order'] = info[6]
                        print json.dumps(dic[info[2]])
                        del dic[info[2]]
f.close()

