# based on moderngl/examples/basic_empty_window.py

import moderngl
import moderngl_window as mglw
from motiontools import normpath, dir_of_file

LCTRL         = 0xffe3

class Test(mglw.WindowConfig):
    window_size = (500, 300)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def key_event(self, key, action, modifiers):
        if action == self.wnd.keys.ACTION_PRESS and key == LCTRL:
            print("press ctrl ", modifiers)
        elif action == self.wnd.keys.ACTION_RELEASE and key == LCTRL:
            print("release ctrl ", modifiers)

    def mouse_press_event(self, x, y, button):
        print("press x: ", x, " y: ", " button: ", button)

    def render(self, time, frame_time):
        pass

if __name__ == '__main__':
    mglw.run_window_config(Test)
