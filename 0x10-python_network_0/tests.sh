#!/usr/bin/bash

stat_code=$(curl -L -o- -I -s -w "%{http_code}\n" $1)
for stat in "${stat_code[@]}"
do
	if [ $stat -eq 200 ]
	then
		echo "Thisis bad"
	fi
done


