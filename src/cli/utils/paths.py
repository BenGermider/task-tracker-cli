import os

def get_path(*args):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    counter_path = os.path.join(base_dir, *args)
    counter_path = os.path.normpath(counter_path)  # clean up path
    return counter_path