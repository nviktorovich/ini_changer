class Config:
    PATTERN = r" *отправитель(Резервный|Основной) *{ *[ \t]*[ \n]*[ \t]*адрес:([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})"
    ENCODING = "koi8-r"
    RU_MAIN_NAME = "Основной"
    RU_REZ_NAME = "Резервный"
    DEFAULT_STRING = ""
    FIRST_ARG_MAIN = "-m"
    FIRST_ARG_REZ = "-r"
    HELP_FLAG = "-h"
    HELP_FLAG_LONG = "--help"
    MEDIA_MOUNT_DIR = "/media/kts_mount"
    BIN_PATH = "BIN"
    ETC_PATH = "etc"
    CONFIG_FILE = "project.conf"
    KTS_MOUNT_DIR = "/mnt/sys"
    DATE_PATTERN = "%Y-%m-%d %H:%M "


class ConsoleCommands:
    KTS_LOGIN_REQUEST = "login"
    KTS_USER_NAME = "root"
    KTS_PASSWORD_REQUEST = "Password"
    KTS_PASSWORD_ROOT = "crtc"
    KTS_SET_RW_MODE = "mount -o rw,remount /mnt/sys"
    KTS_SET_RO_MODE = "mount -o ro,remount /mnt/sys"
    EXIT_MESS = "exit"
    REBOOT_MESS = "reboot"
    UMOUNT_CMD = "umount -f {}"
    MOUNT_CMD = "mount {}:{} {}"
    ECHO_WITH_ONE_ARG = "echo '{}'"
    HELP_INFO = """Использование:
 python3 [комплект] <INI-файл>
 python3 -m | -r INI-file
 python3 -h | --help "" | INI-file
"""


class Errors:
    NOT_TWO_ARGS_MESS = "echo ошибка ввода команды. Необходимо два аргумента --help"
    FILE_NOT_EXIST_MESS = "echo ошибка ввода команды. В папке: {} отсутствует файл: {}"
    INCORRECT_SET_NAME = "echo ошибка ввода команды. Допустимы обозначения -m для main, -r для rez, выбрано: {}"
    EXIT_MESS = "echo ошибка работы приложения. Приложение завершило работу"
    IP_NOT_FOUND = "echo ошибка распознования. В INI-файле не найден ip адрес Основной: {}, Резервный: {}"
    FILE_NOT_EXIST_IN_MOUNT_MPK = "echo ошибка работы приложения. В папке: {} отсутствует файл: {}"
    NOT_AVAILABLE_NETWORK_DEVICE = "echo ошибка работы с сетью МПК. Сетевое устройство: {} недоступно"
    NOT_ETC_DIR = "echo ошибка структуры данных. Отсутствует директория /etc в примонтированной директории {}"
    NOT_PATH_IN_PROJECT_CONF = "echo ошибка структуры данных. В файле project.conf не прописана или неверно прописана рабочая директория"
