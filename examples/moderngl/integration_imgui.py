from pathlib import Path
import imgui
import moderngl
from pyrr import Matrix44
import moderngl_window as mglw
from moderngl_window import geometry
from moderngl_window.integrations.imgui import ModernglWindowRenderer

def string(*args):
    return "".join([str(elem) for elem in args])

class WindowEvents(mglw.WindowConfig):
    gl_version = (3, 3)
    title = "imgui Integration"
    resource_dir = (Path(__file__).parent / 'resources').resolve()
    aspect_ratio = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        imgui.create_context()
        self.wnd.ctx.error
        self.imgui = ModernglWindowRenderer(self.wnd)

        self.cube = geometry.cube(size=(2, 2, 2))
        self.prog = self.load_program('programs/cube_simple.glsl')
        self.prog['color'].value = (1.0, 1.0, 1.0, 1.0)
        self.prog['m_camera'].write(Matrix44.identity(dtype='f4'))
        self.prog['m_proj'].write(Matrix44.perspective_projection(75, self.wnd.aspect_ratio, 1, 100, dtype='f4'))
        self.slider_value = 88

    def render(self, time: float, frametime: float):
        # rotation = Matrix44.from_eulers((time, 0, 0), dtype='f4')
        # rotation = Matrix44.from_eulers((0, time, 0), dtype='f4')
        rotation = Matrix44.from_eulers((0, 0, time), dtype='f4')
        translation = Matrix44.from_translation((0.0, 0.0, -3.5), dtype='f4')
        model = translation * rotation

        self.ctx.enable(moderngl.DEPTH_TEST | moderngl.CULL_FACE)
        self.prog['m_model'].write(model)
        self.cube.render(self.prog)

        self.render_ui(time, rotation, translation, model)

    def render_ui(self, time, rotation, translation, model):
        imgui.new_frame()
        if imgui.begin_main_menu_bar():
            if imgui.begin_menu("File", True):

                clicked_quit, selected_quit = imgui.menu_item(
                    "Quit", '', False, True
                )

                if clicked_quit:
                    exit(1)

                imgui.end_menu()
            imgui.end_main_menu_bar()

        # imgui.show_test_window()
        imgui.begin("Custom window", True)
        value = self.slider_value
        changed, changed_value = imgui.slider_int(
            "slide ints", value,
            min_value=0, max_value=100,
            format="%d"
        ) 
        if changed:
            self.slider_value = changed_value
        imgui.text(string("time: \n", time))
        imgui.text(string("rotation: \n", rotation))
        imgui.text(string("translation: \n", translation))
        imgui.text(string("model = translation * rotation: \n", model))
        imgui.end()

        imgui.render()
        self.imgui.render(imgui.get_draw_data())

    def resize(self, width: int, height: int):
        self.prog['m_proj'].write(Matrix44.perspective_projection(75, self.wnd.aspect_ratio, 1, 100, dtype='f4'))
        self.imgui.resize(width, height)

    def key_event(self, key, action, modifiers):
        self.imgui.key_event(key, action, modifiers)

    def mouse_position_event(self, x, y, dx, dy):
        self.imgui.mouse_position_event(x, y, dx, dy)

    def mouse_drag_event(self, x, y, dx, dy):
        self.imgui.mouse_drag_event(x, y, dx, dy)

    def mouse_scroll_event(self, x_offset, y_offset):
        self.imgui.mouse_scroll_event(x_offset, y_offset)

    def mouse_press_event(self, x, y, button):
        self.imgui.mouse_press_event(x, y, button)

    def mouse_release_event(self, x: int, y: int, button: int):
        self.imgui.mouse_release_event(x, y, button)

    def unicode_char_entered(self, char):
        self.imgui.unicode_char_entered(char)


if __name__ == '__main__':
    mglw.run_window_config(WindowEvents)
