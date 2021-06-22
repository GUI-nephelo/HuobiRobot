
import os,json
import mainRobot
import socket,socks

#socks.set_default_proxy(socks.PROXY_TYPE_HTTP,"127.0.0.1",10809)
#socket.socket = socks.socket

#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

with open("./keys.json","r") as f:
    a=json.loads(f.read())
    (api_key, secret_key) = a[n]["accessKey"],a[n]["secretKey"]

if __name__=="__main__":
    """
    from huobi.client.market import MarketClient
    from huobi.constant import *
    from huobi.utils import *

    market_client = MarketClient(init_log=True)
    interval = CandlestickInterval.MIN1
    symbol = "btc3lusdt"
    list_obj = market_client.get_candlestick(symbol, interval, 10)
    LogInfo.output("---- {interval} candlestick for {symbol} ----".format(interval=interval, symbol=symbol))
    LogInfo.output_list(list_obj)
    """
    from huobi.client.account import AccountClient
    from huobi.constant import *
    from huobi.utils import LogInfo

    account_client = AccountClient(api_key=api_key,
                                   secret_key=secret_key)
    LogInfo.output("====== (SDK encapsulated api) not recommend for low performance and frequence limitation ======")
    account_balance_list = account_client.get_account_balance()
    if account_balance_list and len(account_balance_list):
        for account_obj in account_balance_list:
            account_obj.print_object()
            print()