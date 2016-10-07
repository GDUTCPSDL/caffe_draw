"""
    Directly draw all graphs from original log file
"""
from parse_log import *
from draw import *


if __name__ == '__main__':
    file_name = sys.argv[1]  # out.log(.train)/out.log(.test)

    if '/' in file_name:
        pic_path = file_name[:file_name.rindex('/')+1]
    else:
        pic_path = "./"  # .

    print("LOG FILE:" + file_name)
    print("PIC GENERATING PATH:" + pic_path)

    train_dict_list, test_dict_list = parse_log(file_name)

    save_csv_files(file_name, pic_path, train_dict_list,
                   test_dict_list, delimiter=",")

    draw(file_name, pic_path)
