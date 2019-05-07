for i in {525443..520366}; do zcash-cli getblock $i >> ~/Desktop/blockdata.txt ; done
cd Desktop 
sudo g++ parse.cpp
./a.out
for var in $(cat Desktop/txid2.csv); do temp=$(echo $var | sed 's/"//g') ;temp1=$(zcash-cli getrawtransaction $temp  ); zcash-cli decoderawtransaction $temp1 ;done &>testest1.txt

