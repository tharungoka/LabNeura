def create_list(line : str):
    list_line = line.split(",") # hardcoding 
    return list_line

def create_lists(lines :  list):
    list_lines = list(map(create_list,lines))
    return list_lines