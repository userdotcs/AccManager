import acc_manager_sys


class delete_com:
    def __init__(self, com):
        self.is_exe_command = com == 'delete'

    def run_com(self):
        if self.is_exe_command:
            acc_name = input('Acc Name>> ').strip()
            acc_manager_sys.delete_acc(acc_name)
