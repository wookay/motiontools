import moderngl_window as mglw

class Window1(mglw.WindowConfig):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("init:", kwargs)
        # init: {'ctx': <Context 140261633158032 version_code=410>, 'wnd': <moderngl_window.context.pyglet.window.Window object at 0x7f9133dc6a10>, 'timer': <moderngl_window.timers.clock.Timer object at 0x7f9134d2c690>}

    def render(self, time: float, frame_time: float):
        if time < 0.2:
            print("time: ", time,
                  "frame_time: ", frame_time,
                  "self.ctx.screen:", self.ctx.screen)
        pass

mglw.run_window_config(Window1)
