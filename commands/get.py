import acc_manager_sys


class get_com:
    def __init__(self, com):
        self.is_exe_command = com == 'get'

    def run_com(self):
        if self.is_exe_command:
            acc_name = input('Acc Name>> ').strip()
            acc = acc_manager_sys.get_infos_in_acc_file(acc_name)
            if acc is not None:
                acc.printaccinfos()
