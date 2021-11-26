import requests
import json

#Zabbix login
url = "http://10.16.16.152/zabbix/api_jsonrpc.php"
username = "API"
password = "password"


#Function to request API token
def get_api_token(url):

    payload = {
        "jsonrpc":"2.0",
        "method":"user.login",
        "params":{"user":username,"password":password},
        "id": 1,
        "auth": None
    }

    resp = requests.post(url=url, json=payload )
    out = resp.json()

    return out['result']

#Add new code below here



#Add new code above here


#API token request

api_token = (get_api_token(url))

zabbix_hosts = get_hosts(api_token,url)
generate_host_file(zabbix_hosts,"/home/results")
