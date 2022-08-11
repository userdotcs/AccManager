import os
from commands import get, append, delete


class account:
    def __init__(self, nick, password):
        self.nick = nick
        self.password = password

    def printaccinfos(self):
        print('Nick:', self.nick)
        print('Password:', self.password)


class command:
    def __init__(self, command):
        self.command = command

    def run_command(self):
        get.get_com(self.command).run_com()
        delete.delete_com(self.command).run_com()
        append.append_com(self.command).run_com()


def get_infos_in_acc_file(accnick):
    accs = os.listdir('accs')
    for acc in accs:
        if acc == accnick:
            accfile = open('accs/' + acc)
            nick = accfile.readline().strip()
            password = accfile.readline().strip()
            accfile.close()
            return account(nick, password)
    return None


def delete_acc(accnick):
    if os.path.exists('accs/' + accnick):
        os.remove('accs/' + accnick)
    else:
        print('This account is not defined.')


def new_acc(accnick, nick, password):
    if os.path.exists('accs/' + accnick):
        print('This account already exists.')
    else:
        new_acc_file = open('accs/' + accnick, 'w')
        new_acc_file.write(nick + '\n' + password)
        new_acc_file.close()
