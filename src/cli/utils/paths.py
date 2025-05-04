import os

def get_path(*args) -> os.path:
    """
    Builds a path based on args received
    :param args: path add to absolute path
    :return: new_path
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    counter_path = os.path.join(base_dir, *args)
    counter_path = os.path.normpath(counter_path)  # Removing redundant dots
    return counter_path