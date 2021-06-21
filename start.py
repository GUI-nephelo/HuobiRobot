
import os,json
import mainRobot
import socket,socks

#socks.set_default_proxy(socks.SOCKS5,"127.0.0.1",10808)
#socket.socket = socks.socket

n=1

with open("./keys.json","r") as f:
    a=json.loads(f.read())
    (api_key, secret_key) = a[n]["accessKey"],a[n]["secretKey"]

if __name__=="__main__":
    from huobi.client.account import AccountClient
    from huobi.constant import *

    # get accounts
    from huobi.utils import *

    account_client = AccountClient(api_key=api_key,
                                   secret_key=secret_key,
                                   url="https://api-aws.huobi.pro")

    list_obj = account_client.get_accounts()
    #LogInfo.output_list(list_obj)