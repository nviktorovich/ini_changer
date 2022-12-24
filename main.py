import os
import shutil
import sys

import constant as ct
import net_conn as kts
import file_operation as fo
import command_line_parameters as clp


def run():
    # Проверка аргумента, если был вызван с -h или --help
    if len(sys.argv) == 1 or sys.argv[1] in [ct.Config.HELP_FLAG, ct.Config.HELP_FLAG_LONG]:
        os.system(ct.ConsoleCommands.ECHO_WITH_ONE_ARG.format(ct.ConsoleCommands.HELP_INFO))
        sys.exit(1)
    # Если проверка аргументов пройдена, начинает работать основная программа по замене INI-файла
    if clp.args_check(sys.argv):
        ip_main, ip_rez = fo.get_ip(sys.argv[2])
        ip = ct.Config.DEFAULT_STRING

        # Если не удалось "вытащить" IP адреса из INI-файла, программа завешает работу
        if ip_main == ct.Config.DEFAULT_STRING or ip_rez == ct.Config.DEFAULT_STRING:
            os.system(ct.Errors.IP_NOT_FOUND.format(ip_main, ip_rez))
            sys.exit(1)

        # Если удалось "вытащить" IP адреса из INI-файла, программа продолжает работу
        else:
            if sys.argv[1] == ct.Config.FIRST_ARG_MAIN:
                ip = ip_main
            elif sys.argv[1] == ct.Config.FIRST_ARG_REZ:
                ip = ip_rez

            # Если не удалось установить соединение с устройством в сети, программа завершает работу
            if not kts.pingCheck(ip):
                os.system(ct.Errors.NOT_AVAILABLE_NETWORK_DEVICE.format(ip))
                sys.exit(1)

            kts_obj = kts.KTS(ip)
            kts_obj.set_rw()
            fo.mount(ip)
            # Проверка существования файла с аналогичным названием в директории BIN примонтированной папки
            if not fo.check_exist(sys.argv[2], os.path.join(ct.Config.MEDIA_MOUNT_DIR, ct.Config.BIN_PATH)):
                os.system(ct.Errors.FILE_NOT_EXIST_IN_MOUNT_MPK.format(sys.argv[2],
                                                                       os.path.join(
                                                                           ct.Config.MEDIA_MOUNT_DIR,
                                                                           ct.Config.BIN_PATH)
                                                                       )
                          )
                fo.make_clear(ct.Config.MEDIA_MOUNT_DIR)
                sys.exit(1)
            fo.file_renamer(os.path.join(ct.Config.MEDIA_MOUNT_DIR, ct.Config.BIN_PATH), sys.argv[2])
            shutil.copy(sys.argv[2], os.path.join(ct.Config.MEDIA_MOUNT_DIR, ct.Config.BIN_PATH))
            fo.make_clear(ct.Config.MEDIA_MOUNT_DIR)
            kts_obj.set_ro()
            os.system("echo на устройство МПК записана новая версия конфигурационного файла")
            sys.exit(1)
    # Если проверка аргументов не пройдена, программа завершает свою работу
    else:
        os.system(ct.Errors.EXIT_MESS)
        sys.exit(1)


if __name__ == "__main__":
    run()
