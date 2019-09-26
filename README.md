# Netoxidized

This simple (quick & dirty) script retrieves actives devices from Netbox and convert them to a simple inventory for (Oxidized)[https://github.com/ytti/oxidized].

Netbox deserves a better & direct integration to Oxidized, but since you might need something working quickly, you can use this script as a workaround.

## Usage 

Put it on your server, install requirements, create a config file in `/etc/oxidized/netbox.ini`, with the appropriate values for your case.

Install a crontab to launch `netbox_to_oxidized.py` on an appropriate frequency with your oxidized user, then you are ready to go.

Use | as separator instead of :.

Example source config :
```
source:
  default: csv
  csv:
    file: /etc/oxidized/router.db
    delimiter: !ruby/regexp /|/
    map:
      name: 0
      ip: 1
      model: 2
    vars_map:
      enable: 4
    gpg: false
```