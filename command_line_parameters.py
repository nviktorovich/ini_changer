import file_operation as fo
import os
import constant as ct


def args_check(*args):
    """
    Функция для проверки корректности введенных аргументов.
    В случае ошибки возвращает комментарий с конкретным описанием ошибки.
    :param args: указание названия INI файла, выбор комлекта КТС УК для замены софта
    :return: Булево значение, если True - все проверки пройдены; False - ошибки не пройдены
    """
    # проверка количества аргументов, должно быть два аргумента
    if len(*args) != 3:
        os.system(ct.Errors.NOT_TWO_ARGS_MESS)
        return False

    # проверка аргумента обозначения комплекта
    if args[0][1] not in [ct.Config.FIRST_ARG_MAIN, ct.Config.FIRST_ARG_REZ]:
        os.system(ct.Errors.INCORRECT_SET_NAME.format(args[0][1]))
        return False

    # проверка существования файла
    if not fo.check_exist(args[0][2], os.getcwd()):
        os.system(ct.Errors.FILE_NOT_EXIST_MESS.format(os.getcwd(), args[0][2]))
        return False

    return True
