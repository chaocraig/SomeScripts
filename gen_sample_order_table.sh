#!/bin/bash
wget https://s3-ap-southeast-1.amazonaws.com/etubigdata/EHC_1st.tar.gz
tar zxvf EHC_1st.tar.gz
hadoop fs -mkdir -p data
time hadoop fs -put EHC_1st_round.log /tmp/EHC_1st_round.log &
time grep "act=order" EHC_1st_round.log | grep -v "plist=;" | sed -e 's/.*plist=\([^;]*\);.*/\1/g' | sed -e 's/\(\([^,]*,\)\{2\}[^,]*\),/\1\'$'\n/g' | hadoop fs -put - data/orders.csv
impala-shell -q "create external table IF NOT EXISTS orders ( pid STRING, count INT, price INT ) ROW FORMAT DELIMITED FIELDS TERMINATED BY ','  LOCATION '/user/$(whoami)/data'; invalidate metadata;"
