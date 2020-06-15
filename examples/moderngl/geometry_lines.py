# based on moderngl-window/examples/geometry_lines.py

import moderngl
import moderngl_window as mglw
import numpy as np
from pyrr import Matrix44
from motiontools import normpath, dir_of_file


class CameraWindow(mglw.WindowConfig):
    """Base class with built in 3D camera support"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera = mglw.scene.camera.KeyboardCamera(self.wnd.keys, aspect_ratio=self.wnd.aspect_ratio)
        self.camera_enabled = True

    def key_event(self, key, action, modifiers):
        keys = self.wnd.keys

        if self.camera_enabled:
            self.camera.key_input(key, action, modifiers)

        if action == keys.ACTION_PRESS:
            if key == keys.C:
                self.camera_enabled = not self.camera_enabled
                self.wnd.mouse_exclusivity = self.camera_enabled
                self.wnd.cursor = not self.camera_enabled
            if key == keys.SPACE:
                self.timer.toggle_pause()

    def mouse_position_event(self, x: int, y: int, dx, dy):
        if self.camera_enabled:
            self.camera.rot_state(-dx, -dy)

    def resize(self, width: int, height: int):
        self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)


class LinesDemo(CameraWindow):
    window_size = (500, 500)
    resource_dir = normpath(dir_of_file(), 'resources')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.prog = self.load_program('programs/lines/lines.glsl')
        self.prog['color'].value = (1.0, 1.0, 1.0, 1.0)
        self.prog['m_model'].write(Matrix44.from_translation((0, 0, -2), dtype='f4'))

        def gen_lines(N):
            with np.nditer(np.linspace(-1, 1, N+1, endpoint=True)) as it:
                for i in it:
                    # vertical line (x1, x2)
                    yield i
                    yield -1
                    yield 0
                    yield i
                    yield 1
                    yield 0
                    # horizontal line (y1, y2)
                    yield -1
                    yield i
                    yield 0
                    yield 1
                    yield i
                    yield 0

        N = 5
        buffer = self.ctx.buffer(np.fromiter(gen_lines(N), dtype='f4', count=(N+1) * 6 * 2).tobytes())
        self.lines = self.ctx.vertex_array(
            self.prog,
            [
                (buffer, '3f', 'in_position'),
            ],
        )

    def render(self, time, frametime):
        self.prog['m_proj'].write(self.camera.projection.matrix)
        self.prog['m_cam'].write(self.camera.matrix)
        self.lines.render(mode=moderngl.LINES)


if __name__ == '__main__':
    mglw.run_window_config(LinesDemo)
