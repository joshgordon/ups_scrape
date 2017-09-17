This is a project to scrape power usage (and supply voltage) data off my cyberpower UPS for ingest into influxdb. 

I have a raspi0w plugged into my UPS running `NUT` (Network UPS toolS) to scrape the data and publish it into
mqtt. Then I have `publish_ups.py` running on my NUC and ingesting the data into influx. Then grafana's on top of that
to show off pretty graphs and dashboards and stuff. 

Also in this directory is `publish_temperature` - I have two temperature sensors connected to a particle photon which
is publishing temperature data into mqtt every second. This script picks that up and drops that in influx for pretty 
graphs and stuff.
