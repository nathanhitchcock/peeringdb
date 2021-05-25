
# !/usr/bin/env python3
import requests
import collections as ct
import more_itertools as mit

r_netixlan = []
r_netixlan_sorted = []
reduced_netixlan = []

def main():
    net_id = collect_user_input()
    r_netixlan_sorted = api_request(net_id)
    reduced_netixlan = aggregate_speeds(r_netixlan_sorted)
    print_results(r_netixlan, r_netixlan_sorted, reduced_netixlan)

def collect_user_input():
    # Change this variable to adjust which PeeringDB NET_ID [not asn] this application looks for
    net_id = input("Please enter the desired PeeringDB NET_ID [not asn] to search: ")
    return net_id

def api_request(net_id):
    print(net_id)
    # Make a GET request to get the PeeringDB network information
    r = requests.get("https://peeringdb.com/api/net/" + str(net_id)).json()

    # Populate the main variables from the base request
    r_netixlan = r['data'][0]['netixlan_set']

    # Sort the array
    r_netixlan_sorted = sorted(r_netixlan, key=lambda k: k['name'])

    return r_netixlan_sorted

def aggregate_speeds(r_netixlan_sorted):
    # Collect the total number of Peerings in the Dataset
    #total_Peerings = len(r_netixlan_sorted)

    # Aggregate the total bandwidth per Peering Group
    # Using 'd[ix_id]' there are 49 unique peerings and using the name there are 52 unique peerings
    kfunc = lambda d: d["name"]
    vfunc = lambda d: {k:v for k, v in d.items() if k.startswith("speed")}
    rfunc = lambda lst: sum((ct.Counter(d) for d in lst), ct.Counter())

    # Build the reduced dictionary object
    reduced_netixlan = mit.map_reduce(r_netixlan_sorted, keyfunc=kfunc, valuefunc=vfunc, reducefunc=rfunc)

    return reduced_netixlan


def print_results(r_netixlan, r_netixlan_sorted, reduced_netixlan):
    # Display the number of Unique Peerings
    total_Unique_Peerings = len(reduced_netixlan)

    # Collect the Aggreate speed across all Peerings
    total_speed = 0
    speed = 0
    total_Peerings = len(r_netixlan_sorted)

    # Format & Print the results
    print("List of Public Peerings \n")
    for net in r_netixlan_sorted:
        name = net['name']
        ix_id = net['ix_id']
        speed = net['speed']
        total_speed += speed
        print(name, ix_id, str(speed / 1000) + "GBs")

    total_speed = total_speed / 1000

    print("\n")
    print("Aggreate Speed Per Peering Group: \n" + str(reduced_netixlan))
    print("\n")
    print("Total Peerings: " + str(total_Peerings))
    print("Total Number of Unique Peerings: " + str(total_Unique_Peerings))
    print("Total Aggreate Speed for All Peerings: " + str(total_speed) + "GBs")

if __name__ == '__main__':
    main()
