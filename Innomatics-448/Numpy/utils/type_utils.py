import multiprocessing as mp

def str2int(ele :  str):
    return int(ele)

def convert_line(line : list):
    int_line = list(map(str2int, line))
    return int_line

def convert_all_lines(lines: list):
    # with mp.Pool() as pool:
    #     all_lines = pool.map(convert_line, lines)
    # return all_lines
    all_lines = list(map(convert_line, lines))
    return all_lines