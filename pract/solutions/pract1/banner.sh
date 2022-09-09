#!/usr/bin/bash
str=$1
n=`expr "$str" : '.*'`

buf="+"
for (( i = 0; i<$n+2;i++ ))
do
    buf="${buf}-"
done
buf="${buf}+"

echo $buf

echo "| ${str} |"
echo $buf