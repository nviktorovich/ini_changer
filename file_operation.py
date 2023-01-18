import os
import constant as ct
import shutil
import re
import datetime


def mount(ip):
    """
    Функция предназначена для монтирования устройства МПК в директорию по умолчанию /media/kts-mount
    работа функции включает в себя проверку, существования указанной директории, и если она существует,
    форсированного размонтирования и удаления директории, затем создания новой пустой папки /media/kts-mount
    и монтирования флеш карты МПК с устройства с заданным адресом ip
    :param ip: параметр, содерщащий значение ip адреса
    """
    # 1. Проверка сущестсвавания каталога /media/kts_mount
    if os.path.exists(ct.Config.MEDIA_MOUNT_DIR):
        make_clear(ct.Config.MEDIA_MOUNT_DIR)
    os.mkdir(ct.Config.MEDIA_MOUNT_DIR)
    os.system(ct.ConsoleCommands.MOUNT_CMD.format(ip, ct.Config.KTS_MOUNT_DIR, ct.Config.MEDIA_MOUNT_DIR))


def make_clear(mnt_dir):
    """
    Функция предназначена для форсированного размонтирования каталога и удаления каталога
    :param mnt_dir: каталог для форсированного размонтирования и удаления
    """
    # 1. Форсированное отмонтирование того, что было, удаление папки
    os.system(ct.ConsoleCommands.UMOUNT_CMD.format(mnt_dir))
    # 2. Удаление каталока /media/kts_mount
    shutil.rmtree(mnt_dir)


def check_exist(file, path):
    """
    Функция для проверки существования указанного файла в указанном каталоге
    :param file: строковый параметр - название ини файла
    :param path: строковый параметр - абсолютный путь до исполняемой папки
    :return: Булево значение True - если файл в папке существует, False - не существует
    """
    if file not in os.listdir(path):
        return False
    return True


def get_ip(path):
    """
    Функция обрабатывает ini файл, с помощью регулярных выражений находит ip адреса основного и резервного комплекта
    КТС УК Возвращает два строковых значения
    :param path: строковое значение - путь до файла
    :return: два строковых
    значения, на 1м месте ip адрес основного комлекта, на 2м - резервного
    """
    with open(path, encoding=ct.Config.ENCODING) as file:
        data = file.read()
    ip_main, ip_rez = ct.Config.DEFAULT_STRING, ct.Config.DEFAULT_STRING
    checks_list = re.findall(pattern=ct.Config.PATTERN, string=data)
    for check in checks_list:
        if check[0] == ct.Config.RU_REZ_NAME:
            ip_rez = check[1]
        elif check[0] == ct.Config.RU_MAIN_NAME:
            ip_main = check[1]

    return ip_main, ip_rez

def get_path_to_ini_dir(path):
    with open(path, encoding=ct.Config.ENCODING) as file:
        project_path = (file.readline().split("/"))
    if len(project_path) < 4:
        return ""
    return os.path.join(*project_path[3::])



def get_timestamp():
    """
    Функция с отсуствующими аргументами, предназначена для получения строки с
    отформатированными данными по текущему времени и дате
    :return: отформатированную строку с датой и временем
    """
    now = datetime.datetime.now()
    return now.strftime(ct.Config.DATE_PATTERN)


def file_renamer(path, file):
    """
    Функция для переименования файла, переименовывает файл по заданному пути с использованием функции get_timestamp
    переименованный файл остается на прежнем месте
    :param path: путь до файла
    :param file: название файла
    :return:
    """
    name_with_timestamp = get_timestamp() + file
    os.rename(os.path.join(path, file), os.path.join(path, name_with_timestamp))
