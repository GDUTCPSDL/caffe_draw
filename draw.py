# -*- coding: utf-8 -*-
"""
use to read the log file
    then draw a graph about acc and loss
"""
import numpy as np
import matplotlib.pyplot as pl
import sys


test_options = dict()
train_options = dict()


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


def draw_line(column, result, option_num, pic_path, options):
    x_num, y_num, description = options[str(option_num)]
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


def set_option(test_column, train_column):
    for i in range(0, len(test_column)):
        test_column[i] = test_column[i].replace("/", ".")

    for i in range(0, len(train_column)):
        train_column[i] = train_column[i].replace("/", ".")

    test_column_len = len(test_column)
    train_column_len = len(train_column)

    for i in range(1, test_column_len-2+1):
        test_options[str(i)] = [0, i+1, "[TEST]"+test_column[0]+"-"+test_column[i+1]]

    for i in range(test_column_len-2+1, (test_column_len-2)*2+1):
        test_options[str(i)] = [1, i+1-(test_column_len-2), "[TEST]"+test_column[1]+"-"+test_column[i+1-(test_column_len-2)]]

    for i in range(1, train_column_len-2+1):
        train_options[str(i)] = [0, i+1, "[TRAIN]"+train_column[0]+"-"+train_column[i+1]]

    for i in range(train_column_len-2+1, (train_column_len-2)*2+1):
        train_options[str(i)] = [1, i+1-(train_column_len-2), "[TRAIN]"+train_column[1]+"-"+train_column[i+1-(train_column_len-2)]]


def draw(file_name, pic_path):
    #file_name = sys.argv[1]  # out.log(.train)/out.log(.test)
    #pic_path = sys.argv[2]  # .
    global test_options
    global train_options

    test_column, test_result = parse_line_list(file_name+".test")
    train_column, train_result = parse_line_list(file_name+".train")
    set_option(test_column, train_column)


    for option_num in [str(i) for i in range(1, (len(test_column)-2)*2+1)]:
        draw_line(test_column, test_result, option_num,
                  pic_path+file_name+test_options[option_num][2]+".jpg",
                  test_options)

    for option_num in [str(i) for i in range(1, (len(train_column)-2)*2+1)]:
        draw_line(train_column, train_result, option_num,
                  pic_path+file_name+train_options[option_num][2]+".jpg",
                  train_options)


if __name__ == '__main__':
    test_column, result = parse_line_list("out.log.test")
    train_column, result = parse_line_list("out.log.train")

    set_option(test_column, train_column)

    print (test_options)
    for option_num in [str(i) for i in range(1, len(test_options)+1)]:
        print test_options[option_num]

    for option_num in [str(i) for i in range(1, len(train_options)+1)]:
        print train_options[option_num]