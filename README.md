# PeeringDB
Review of the Peering DB API, aggregating the NET_ID links

## requirements
* Python 3.9.0

## setup
* `pip3 install -r requirements.txt`

## run
* `./init.py`

### respond to the prompts and watch it work:

```
╰─ python init.py
Please enter the desired PeeringDB NET_ID [not asn] to search: 22
List of Public Peerings

AMS-IX Chicago 944 10.0GBs
DE-CIX Dallas: DE-CIX Dallas Peering LAN 1249 10.0GBs
Equinix Ashburn 1 10.0GBs
Equinix Chicago 2 10.0GBs
Equinix Dallas 3 20.0GBs
Equinix New York 12 10.0GBs
Equinix San Jose 5 10.0GBs
LINX LON1: Main 18 40.0GBs
LINX NoVA 777 10.0GBs
LONAP: LON0 53 20.0GBs
NYIIX 14 10.0GBs


Aggreate Speed Per Peering Group:
defaultdict(None, {'AMS-IX Chicago': Counter({'speed': 10000}), 'DE-CIX Dallas: DE-CIX Dallas Peering LAN': Counter({'speed': 10000}), 'Equinix Ashburn': Counter({'speed': 10000}), 'Equinix Chicago': Counter({'speed': 10000}), 'Equinix Dallas': Counter({'speed': 20000}), 'Equinix New York': Counter({'speed': 10000}), 'Equinix San Jose': Counter({'speed': 10000}), 'LINX LON1: Main': Counter({'speed': 40000}), 'LINX NoVA': Counter({'speed': 10000}), 'LONAP: LON0': Counter({'speed': 20000}), 'NYIIX': Counter({'speed': 10000})})


Total Peerings: 11
Total Number of Unique Peerings: 11
Total Aggreate Speed for All Peerings: 160.0GBs
```
