import time

import pexpect
import constant as ct
import os


class KTS:

    def __init__(self, ip):
        self.ip = ip

    def set_rw(self):
        conn = pexpect.spawn('telnet {}'.format(self.ip))

        conn.expect(ct.ConsoleCommands.KTS_LOGIN_REQUEST)
        time.sleep(200 / 1000)
        conn.sendline(ct.ConsoleCommands.KTS_USER_NAME)
        time.sleep(200 / 1000)
        conn.expect(ct.ConsoleCommands.KTS_PASSWORD_REQUEST)
        time.sleep(200 / 1000)
        conn.sendline(ct.ConsoleCommands.KTS_PASSWORD_ROOT)
        time.sleep(200 / 1000)
        conn.sendline(ct.ConsoleCommands.KTS_SET_RW_MODE)
        time.sleep(200 / 1000)
        conn.sendline(ct.ConsoleCommands.EXIT_MESS)

    def set_ro(self):
        conn = pexpect.spawn('telnet {}'.format(self.ip))

        conn.expect(ct.ConsoleCommands.KTS_LOGIN_REQUEST)
        time.sleep(200 / 1000)
        conn.sendline(ct.ConsoleCommands.KTS_USER_NAME)
        time.sleep(200 / 1000)
        conn.expect(ct.ConsoleCommands.KTS_PASSWORD_REQUEST)
        time.sleep(200 / 1000)
        conn.sendline(ct.ConsoleCommands.KTS_PASSWORD_ROOT)
        time.sleep(200 / 1000)
        conn.sendline(ct.ConsoleCommands.KTS_SET_RO_MODE)
        time.sleep(200 / 1000)
        conn.sendline(ct.ConsoleCommands.REBOOT_MESS)


def pingCheck(ip):
    """
    Функция для проверки соединения с устройством, принимает на вход строку, возвращает булево значение
    :param ip: строковый параметр - адресс устройства МПК
    :return: булево значение, если устройтсво по сети отвечает - True, если нет - False
    """
    response = os.system("ping -c 1 " + ip)
    if response == 0:
        return True
    return False
