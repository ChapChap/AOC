#!/bin/bash

# input=$(sort input)
echo "Date   ID   Minute"
echo "            000000000011111111112222222222333333333344444444445555555555"
echo "            012345678901234567890123456789012345678901234567890123456789"
#     11-01  #10  .....####################.....#########################.....
#     11-02  #99  ........................................##########..........

OLDIFS=${IFS}
IFS=$'\n'
shift=60
for line in $(sort input);do
    if echo ${line} | grep -q "begins shift";then
        while [[ ${shift} -lt 60 ]] ;do
            echo -n "${char}"
            ((shift++))
        done
        echo
        char='.'
        if echo ${line} | grep -q "23:";then
            day=
        date=$(echo ${line}|awk '{print $1}'|cut -d'-' -f2,3)
        echo -n "${date}"
        id=$(echo ${line}|grep -o "#[0-9]*")
        printf " %5s " ${id}
        shift=0
    else
        minute=$(echo ${line}|grep -o ":[0-9]*"|cut -d':' -f2)
        minute=${minute#0} # Conversion en decimal
        while [[ ${shift} -lt ${minute} ]] ;do
            echo -n "${char}"
            ((shift++))
        done
        if echo ${line} | grep -q "falls asleep";then
            char='#'
        elif echo ${line} | grep -q "wakes up";then
            char='.' 
        fi
        shift=${minute}
    fi
done
while [[ ${shift} -lt 60 ]] ;do
    echo -n "${char}"
    ((shift++))
done
echo
IFS=${OLDIFS}