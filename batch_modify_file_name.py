# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : 批量修改文件名
# @Time  : 2021/10/17 8:21

import os, yaml

import log


def batch_modify():
    # 1，创建日志文件modify.log到当前目录
    create_log_file()

    # 2，获取打印日志对象
    logger = log.Logger(log_file_path).get_logger()

    # 3，读取配置文件，读取出配置的路径，默认路径为当前路径
    cfg_dict = read_yaml()

    # 4，读取要批量重命名的文件夹路径
    dir_path = cfg_dict['dir_path']
    if not dir_path:
        dir_path = os.getcwd()

    if not os.path.isdir(dir_path):
        logger.error(f'路径非法，请检查：{dir_path} ')
        exit(1)

    # 5，读取指定目录下的所有文件
    file_name_list = os.listdir(dir_path)

    # 6，读取配置文件中的被替换字符串和要替换成的字符串
    replaced_str = cfg_dict['replaced_str']
    goal_str = cfg_dict['goal_str']

    # 7，遍历所有文件名，找到被替换的字符串进行替换
    replace_count = 0
    for file_name in file_name_list:
        if replaced_str in file_name:
            file_path = f'{dir_path}\{file_name}'

            file_name_replaced = file_name.replace(replaced_str, goal_str)
            file_path_new = f'{dir_path}\{file_name_replaced}'

            os.rename(file_path, file_path_new)
            replace_count += 1
            logger.info(f'修改文件名：{file_name}，为：{file_name_replaced}')

    logger.info(f'替换完成，共计替换数为：{replace_count}。')


def create_log_file():
    """
    创建日志文件modify.log到当前目录
    """
    global log_file_name, cur_path, log_file_path
    log_file_name = "modify.log"
    cur_path = os.getcwd()
    log_file_path = f'{cur_path}\{log_file_name}'
    if not os.path.isfile(log_file_name):
        file = open(log_file_path, 'w+', encoding='utf-8')
        file.close()


def read_yaml(config_file_path="config.yml"):
    """
    读取配置文件
    :return: 读取后的对象，为字典类型
    """
    infer_cfg = open(config_file_path, encoding='utf-8')
    data = infer_cfg.read()
    yaml_reader = yaml.load(data, Loader=yaml.Loader)
    return yaml_reader


if __name__ == "__main__":
    batch_modify()
