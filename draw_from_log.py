"""
    Directly draw all graphs from original log file
"""
from parse_log import *
from draw import *


if __name__ == '__main__':
    file_name = sys.argv[1]  # out.log(.train)/out.log(.test)
    pic_path = "./"  # .

    train_dict_list, test_dict_list = parse_log(file_name)

    save_csv_files(file_name, pic_path, train_dict_list,
                   test_dict_list, delimiter=",")

    draw(file_name, pic_path)
