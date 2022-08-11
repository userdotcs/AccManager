import acc_manager_sys


class append_com:
    def __init__(self, com):
        self.is_exe_command = com == 'append'

    def run_com(self):
        if self.is_exe_command:
            acc_name = input('Acc Name>> ').strip()
            nick = input('Nick>> ').strip()
            password = input('Password>> ').strip()
            acc_manager_sys.new_acc(acc_name, nick, password)
