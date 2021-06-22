

class TradeDetailEvent:
    """
    The trade received by subscription of trade.

    :member
        symbol: The symbol you subscribed.
        timestamp: The UNIX formatted timestamp generated by server in UTC.
        trade_list: The trade list. The content is Trade class.
    """

    def __init__(self):
        self.ch = ""
        self.id = 0
        self.ts = 0
        self.data = list()


    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.ch, format_data + "Channel")
        PrintBasic.print_basic(self.id, format_data + "ID")
        PrintBasic.print_basic(self.ts, format_data + "Unix Time")
        if len(self.data):
            for trade_detail in self.data:
                trade_detail.print_object()
                print()