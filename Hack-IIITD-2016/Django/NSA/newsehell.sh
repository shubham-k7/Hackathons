#! /bin/bash
var=$(cat destination_ip.txt | wc -l)
for i in `seq 1 $var`
do
	bic=$(cat destination_ip.txt | awk 'NR=='$i)
	tes=$(whois $bic | grep -i orgname | awk 'NR==1 {print $2}')
	tes2=$(whois $bic | grep -i descr | awk 'NR==1 {print $2}')
	if [ tes ]
	then
		whois $bic | grep -i orgname | awk '{print $2}' >> dest_host.txt
	fi
	if [ !tes ] && [ tes2 ]
	then
		whois $bic | grep -i descr | awk 'NR==1 {print $2}' >> dest_host.txt
	fi
done 
