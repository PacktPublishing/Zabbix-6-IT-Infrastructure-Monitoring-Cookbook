import requests
import json

#API login information
url = "http://192.168.0.102/zabbix/api_jsonrpc.php"
api_token = "b4ca33e6bdf67e0988f6dd0bad61317d4b7fe45fe2afc56d4b8e999e0a3fc23b"

#Add new code below here

#Function to retrieve the hosts and interfaces
def get_hosts(api_token, url):

    payload = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": [
            "hostid",
            "host"
        ],
        "selectInterfaces": [
            "interfaceid",
            "ip",
            "main"
        ]
    },
    "id": 2,
    "auth": api_token
    }
    resp = requests.post(url=url, json=payload )
    out = resp.json()
    return out['result']


#Write the results to a file
def generate_host_file(hosts,host_file):

    hostname = None
    f = open(host_file, "w")
    #Write the host entries retrieved from Zabbix
    for host in hosts:
        hostname = host['host']
        for interface in host["interfaces"]:
            if interface["main"] == "1":
                f.write(hostname + " " + interface["ip"] + "\n")

    f.close()
    return

#Add new code above here

#Generate hosts
zabbix_hosts = get_hosts(api_token,url)
generate_host_file(zabbix_hosts,"/home/results")
