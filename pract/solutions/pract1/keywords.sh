#!/bin/bash

str=$(cat $1 | tr -s '#<>!?,.(){}0123456789";\ ' ' ')

str=$(echo $str | xargs -n1 | sort | xargs )
echo $str