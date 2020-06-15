import os
String = str

def normpath(*paths) -> String:
    return os.path.join(*paths)

import inspect
def dir_of_file() -> String:
    caller_frame = inspect.stack()[1]
    return os.path.dirname(os.path.abspath(caller_frame.filename))
