import pynetbox, configparser
from ipaddress import ip_interface

config = configparser.ConfigParser()
config.read('/etc/oxidized/netbox.ini')

BASE_API_URL = config.get('base', 'netbox_url')
API_TOKEN = config.get('base', 'netbox_token')
API_PRIV_KEY = config.get('base', 'netbox_priv_key', fallback='/etc/oxidized/netbox/secret.key')
INVENTORY_FILE = config.get('base', 'inventory_file', fallback='/etc/oxidized/router.db')

nb = pynetbox.api(
    BASE_API_URL,
    private_key_file=API_PRIV_KEY,
    token=API_TOKEN
)

def form_output_inventory(inventory_file_path, log_file_path, devices):
    with open(inventory_file_path, 'w') as inventory_file:
        for item in devices:
            # check if device has an enable secret 
            secret = nb.secrets.secrets.get(device_id=item.id, role='enable')
            if secret:
                inventory_file.write('{}:{}:{}:{}\n'.format(item.name, ip_interface(item.primary_ip.address).ip, item.platform.slug, secret.plaintext))
            else:
                inventory_file.write('{}:{}:{}\n'.format(item.name, ip_interface(item.primary_ip.address).ip, item.platform.slug))
        inventory_file.close()


if __name__ == "__main__":

    devices = nb.dcim.devices.filter(role=['router','switch'], status='1', has_primary_ip=True)

    form_output_inventory(INVENTORY_FILE, devices)