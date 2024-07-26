from database import read_data, connect
import requests
from requests.auth import HTTPBasicAuth
import time
from function import chech_endpoint, check_channels


def read_subscriber():
    data = read_data(table_name='main_server')

    for i in data:
        api = i[2]
        port = i[3]
        username = i[4]
        password = i[5]
        chech_endpoint(api, port, username, password)
        check_channels(api, port, username, password)


while True:
    read_subscriber()
    time.sleep(1)
