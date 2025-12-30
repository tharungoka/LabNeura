import os

def check_file_status(filepath : str):
    status = os.path.isfile(filepath)
    return status

def read_file(filepath : str):
    with open(filepath) as f:
        lines = f.readlines()
        lines = list(map(lambda x:x.strip(), lines))
    return lines
    # Dangling Pointer: Referening to the data which is deleted.