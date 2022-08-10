import acc_manager_sys


while True:
    comtext = input('>> ').strip()
    com = acc_manager_sys.command(comtext)
    com.run_command()
