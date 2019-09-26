# Netoxidized

This simple (quick & dirty) script retrieves actives devices from Netbox and convert them to a simple inventory for (Oxidized)[https://github.com/ytti/oxidized].

Netbox deserves a better & direct integration to Oxidized, but since you might need something working quickly, you can use this script as a workaround.

## Usage 

Put it on your server, install requirements, create a config file in `/etc/oxidized/netbox.ini`, with the appropriate values for your case.

Install a crontab to launch `netbox_to_oxidized.py` on an appropriate frequency with your oxidized user, then you are ready to go.
