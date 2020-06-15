# based on moderngl-window/examples/advanced/animated_sprites.py

import moderngl
import moderngl_window as mglw
from pyrr import Matrix44
from motiontools import normpath, dir_of_file

darkgray = [169/255] * 3

class Test(mglw.WindowConfig):
    window_size = (500, 300)
    resource_dir = normpath(dir_of_file(), 'resources')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.caveman_texture = self.load_texture_array('textures/animated_sprites/player_2.gif', layers=35)
        self.caveman_texture.repeat_x = False
        self.caveman_texture.repeat_y = False
        self.caveman_texture.filter = moderngl.NEAREST, moderngl.NEAREST
        print("self.caveman_texture.layers: ", self.caveman_texture.layers)

        # Geometry
        self.sprite_geometry = mglw.geometry.quad_2d(size=(1.0, 1.0), pos=(0, 0))

        # Programs
        self.sprite_program = self.load_program('programs/animated_sprites/sprite_array.glsl')
        self.projection = self.sprite_program['projection']

    def render(self, time, frame_time):
        self.ctx.clear(*darkgray)

        proj = Matrix44.perspective_projection(100, self.aspect_ratio, 0.1, 1000)
        lookat = Matrix44.look_at(
            (0, -1, 50),
            (0, 0, 0),
            (0, 0, 1),
        )
        self.projection.write((proj * lookat).astype('f4').tobytes())
        self.render_sprite(self.caveman_texture, frame=int(time * 15) % self.caveman_texture.layers, blend=True, position=(0, 0))

    def render_sprite(self, texture, frame=0, blend=False, position=(0, 0)):
        if blend:
            self.ctx.enable(moderngl.BLEND)

        if self.wnd.frames < 10:
            print("self.wnd.frames: ", self.wnd.frames, "frame: ", frame)

        texture.use(location=0)
        self.sprite_program['layer_id'] = frame
        self.sprite_program['position'] = position
        self.sprite_geometry.render(self.sprite_program)

        if blend:
            self.ctx.disable(moderngl.BLEND)

if __name__ == '__main__':
    mglw.run_window_config(Test)
