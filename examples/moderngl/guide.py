import moderngl

# Create a Context.
# ctx = moderngl.create_context()
# If successful we can now render to the window
# print("Default framebuffer is:", ctx.screen)


# Creating a headless context:
ctx = moderngl.create_standalone_context()
# ctx = moderngl.create_context(standalone=True)
# Create a framebuffer we can render to
fbo = ctx.simple_framebuffer((100, 100), 4)
fbo.use()


# Create a Program object.
prog = ctx.program(
    vertex_shader='''
        #version 330

        in vec2 in_vert;
        in vec3 in_color;

        out vec3 v_color;

        void main() {
            v_color = in_color;
            gl_Position = vec4(in_vert, 0.0, 1.0);
        }
    ''',
    fragment_shader='''
        #version 330

        in vec3 v_color;

        out vec3 f_color;

        void main() {
            f_color = v_color;
        }
    ''',
)


import numpy as np
# Create a VertexArray object.
x = np.linspace(-1.0, 1.0, 50)
y = np.random.rand(50) - 0.5
r = np.ones(50)
g = np.zeros(50)
b = np.zeros(50)

vertices = np.dstack([x, y, r, g, b])

vbo = ctx.buffer(vertices.astype('f4').tobytes())
vao = ctx.simple_vertex_array(prog, vbo, 'in_vert', 'in_color')


# Rendering
fbo = ctx.simple_framebuffer((512, 512))
fbo.use()
fbo.clear(0.0, 0.0, 0.0, 1.0)
vao.render(moderngl.LINE_STRIP)

from PIL import Image
image = Image.frombytes('RGB', fbo.size, fbo.read(), 'raw', 'RGB', 0, -1)
print("image: ", image)
import os
from motiontools import normpath, dir_of_file
output = normpath(dir_of_file(), "output")
image.save(normpath(output, 'guide.png'))
