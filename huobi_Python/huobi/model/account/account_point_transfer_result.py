class AccountPointTransferResult:
    """
    The account change information received by subscription of account.

    :member
        timestamp: The UNIX formatted timestamp generated by server in UTC.
        change_type: The event that asset change notification related.
        account_change_list: The list of account change, the content is AccountChange class

    """

    def __init__(self):
        self.transactId = ""
        self.transactTime = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.transactId, format_data + "transactId")
        PrintBasic.print_basic(self.transactTime, format_data + "transactTime")
        self.data.print_object()