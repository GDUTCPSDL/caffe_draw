# -*- coding: utf-8 -*-
"""
use to read the log file
    then draw a graph about acc and loss
"""
import numpy as np
import matplotlib.pyplot as pl
import sys

option = {
    "1": [0, 2, "[TEST]Iter-LearningRate"],
    "2": [0, 3, "[TEST]Iter-Loss1"],
    "3": [0, 4, "[TEST]Iter-Top1"],
    "4": [0, 5, "[TEST]Iter-Top3"],
    "5": [1, 2, "[TEST]Time-LearningRate"],
    "6": [1, 3, "[TEST]Time-Loss1"],
    "7": [1, 4, "[TEST]Time-Top1"],
    "8": [1, 5, "[TEST]Time-Top3"],

    "11": [0, 2, "[TRAIN]Iter-LearningRate"],
    "12": [0, 3, "[TRAIN]Iter-Loss1"],
    "13": [1, 2, "[TRAIN]Time-LearningRate"],
    "14": [1, 3, "[TRAIN]Time-Loss1"],
}


def parse_line_str(line_str):
    """
    Parse the line string to a list
    """
    line_list = line_str.split(",")

    # cut the NEWLINE
    line_len = len(line_list) - 1
    line_list[line_len] = line_list[line_len].strip('\n').strip('\r')

    return line_list


def parse_line_list(file_name):
    """
    Open the file,
    parse the logging data to a list
    :return: (column, result)
    """

    result = list()
    column = list()

    f = open(file_name, 'r')
    line = f.readline()

    column = parse_line_str(line)

    for line in open(file_name):
        line = f.readline()
        result.append(parse_line_str(line))
    f.close()

    return column, result[:-1]


def draw_line(column, result, option_num, pic_path):
    x_num, y_num, description = option[str(option_num)]
    np_result = np.asarray(result).astype(np.float)

    data = dict()

    for i in range(0, len(column)):
        data[column[i]] = np_result[:, i]

    # print type(data[column[0]])

    pl.clf()

    pl.xlabel(column[x_num])
    pl.ylabel(column[y_num])

    pl.title(description)
    pl.plot(data[column[x_num]], data[column[y_num]], label=column[y_num])
    pl.legend()
    #pl.show()
    pl.savefig(pic_path)


def draw(file_name, pic_path):
    #file_name = sys.argv[1]  # out.log(.train)/out.log(.test)
    #pic_path = sys.argv[2]  # .

    column, result = parse_line_list(file_name+".test")

    for option_num in [str(i) for i in range(1, 9)]:
        draw_line(column, result, option_num,
                  pic_path+file_name+option[option_num][2]+".jpg")

    column, result = parse_line_list(file_name+".train")

    for option_num in [str(i) for i in range(11, 15)]:
        draw_line(column, result, option_num,
                  pic_path+file_name+option[option_num][2]+".jpg")


if __name__ == '__main__':
    draw()
