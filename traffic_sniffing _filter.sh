#! /bin/bash

    sudo tshark -i wlan0 -Tfields -e ip.src -e ip.dst -c 500 |awk '!/224.0.0.*/' |awk '!/:/'| sort > a.txt
    cat a.txt | sed '/^\s*$/d'> b.txt         # removing blank spaces
    cat b.txt | awk '!a[$0]++' > c.txt        #removing duplicates
    cat c.txt | awk '!($2 ~ "192.*")' > all_ip.txt   # source and destination ip
    #cat all_ip.txt | awk '{print $1}' | awk '!a[$0]++' > user_ip.txt  # resolving IP to MAC
    #cat all_ip.txt | awk '{print $2}'> destination_ip.txt
    cat d2.txt | awk '{print $1}' | awk '!a[$0]++' > user_ip.txt
    cat all_ip.txt | awk '{print $2}'> destination_ip.txt
    var=$(cat user_ip.txt | wc -l)
    for i in `seq 1 $var`
    do
        val_mac=`cat user_ip.txt | awk 'NR=='$i`
        sudo arp-scan --interface=wlan0 --localnet | grep $val_mac | awk '{print $2}' >> mac_ip.txt
    done
