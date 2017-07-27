#!/bin/bash

delay=10
timeout=0

while true; do 
	timeout 3 ./publish_power_data.sh
	status_code=$?
	if [[ $status_code == 124 ]]; then
		if [[ $timeout == 1 ]]; then
			delay=$((delay + 1))
		fi
		timeout=1
		echo "This is taking too long... restarting pwrstatd"
		systemctl stop pwrstatd
		sleep $delay
		systemctl start pwrstatd
		sleep $delay
	else
		timeout=0
	fi
	sleep 10
done
