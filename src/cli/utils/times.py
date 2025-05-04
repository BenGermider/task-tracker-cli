from datetime import datetime

def get_time() -> str:
    """
    Returns current time nicely
    :return:
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")