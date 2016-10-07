"""
    Directly draw all graphs from original log files
    Attention! 2 or more files, and now we just accept a folder
        which contains log folders, like log_example.

    And these logs must have same attributes, like loss !!!
"""
from parse_log import *
from draw import *


def getdir(rootDir, files, folders):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)

        # collect the names of folders,
        # which mean type names of logs
        folders.append(lists)

        if os.path.isdir(path):
            getlist(path, files)


def getlist(dir, files):
    list = []
    for lists in os.listdir(dir):
        path = os.path.join(dir, lists)

        if path.endswith("out.log"):
            # collect out.log file
            list.append(path)

    files.append(list)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("--INVALID INPUT FORMAT--")
        print("    python caffe_draw/draw_from_logs.py [path to log folder]")
        print("--INVALID INPUT FORMAT--")
        exit()

    folder_name = sys.argv[1]
    files = []
    folders = []
    getdir(folder_name, files, folders)

    print("LOG FOLDER:" + folder_name)
    print("FOUND " + str(len(folders)) + " LOGS:" + ' '.join(folders))

    for log in files:
        file_name = log[0]
        train_dict_list, test_dict_list = parse_log(file_name)

        save_csv_files(file_name, file_name[:file_name.rindex('/')+1], train_dict_list,
                   test_dict_list, delimiter=",")

    #draw(file_name, pic_path)
