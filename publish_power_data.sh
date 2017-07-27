#!/bin/sh

INFLUX_DB_HOST=http://localhost:8086
CURL_OPTS=""

ups_status=$(pwrstat -status)
status_code=$?
if [[ $status_code == 1 ]]; then
	echo "Can't find daemon, aborting"
	exit 124
fi
power_in_watts=$(echo $ups_status | grep -oP "Load\.+ ?\d+ ?Watt"  | grep -oP "\d+")
voltage=$(echo $ups_status | grep -oP "Utility Voltage\.+ ?\d+ ?"  | grep -oP "\d+")
percent=$(echo $ups_status | grep -oP "Battery Capacity\.+ ?\d+ ?"  | grep -oP "\d+")

echo Power: $power_in_watts
echo voltage: $voltage
echo percent: $percent


curl -i -XPOST "$INFLUX_DB_HOST/write?db=grafana" --data-binary "power value=$power_in_watts"
curl -i -XPOST "$INFLUX_DB_HOST/write?db=grafana" --data-binary "voltage value=$voltage"
curl -i -XPOST "$INFLUX_DB_HOST/write?db=grafana" --data-binary "percent value=$percent"

