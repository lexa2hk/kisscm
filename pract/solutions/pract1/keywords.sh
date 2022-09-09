#!/bin/bash

m=$(<$1)
echo $m

n=`expr "$m" : '.*'`

res=""

for ((i=1;i<$n;i++))
do
    ch_prev=${m:$i-1:1}
    ch=${m:$i:1}
    if [ $ch == $ch_prev]
        res=${res+ch}
done

mes=$(sed 's/[^a-z]*/!/g' <<< $m)
echo $mes

echo $res