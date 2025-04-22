import requests, time, uuid, socket, subprocess, os
import ntplib
from datetime import datetime
from time import ctime
from pymongo import MongoClient

def users_db():
    client = MongoClient("mongodb+srv://kapengbarako:latte@test-cluster.qsvaj.mongodb.net/?retryWrites=true&w=majority&appName=Test-Cluster")
    t_db = client["Tracking_db"]
    users = t_db["computers"]
    return users

def check_internet_connection(url='http://www.google.com', timeout=5):
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False
    
def tracking_funtion():
   
    user = users_db()
    
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1])
    hostname = socket.gethostname()
    externalIP  = os.popen('curl -s ifconfig.me').readline()
    users = "ls /home"
    result = subprocess.run(users, shell=True, capture_output=True, text=True)
    users_output = result.stdout
    client = ntplib.NTPClient()
    response = client.request('time.google.com', version=3)
    ntp_datetime = datetime.strptime(ctime(response.tx_time), "%a %b %d %H:%M:%S %Y")
    stamp = ntp_datetime.strftime("%b %d %Y - %X %p")
    print(stamp)
    existance_checker = user.find_one({"mac_address" : mac })

    if existance_checker :

        user.update_one(
            {"mac_address" : mac},
            {"$set" : {
                "public_ip" : externalIP,
                "computer" : hostname,
                "users" : users_output,
                "time_stamp" : stamp
            }}
        )

        user.update_one(
            {"mac_address" : mac},
            {"$push" : {
                    "record" : {"public_ip" : externalIP, "time_stamp" : stamp}
                }
            }
        )

    else:
        user.insert_one(
            {
                "mac_address" : mac,
                "public_ip" : externalIP,
                "computer" : hostname,
                "users" : users_output,
                "time_stamp" : stamp,
                "pfpath" : "",
                "record" : [
                    {"public_ip" : externalIP, "time_stamp" : stamp}
                ]
            }
        )

def main():
    print("Checking for internet connection...")
    while not check_internet_connection():
        print("No internet connection. Retrying in 5 seconds...")
        time.sleep(5)

    tracking_funtion()

if __name__ == "__main__":
    main()
