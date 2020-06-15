import moderngl
import numpy as np
from PIL import Image
from pyrr import Matrix44

# -------------------
# CREATE CONTEXT HERE
# -------------------
ctx = moderngl.create_context(standalone=True)

prog = ctx.program(vertex_shader="""
    #version 330
    uniform mat4 model;
    in vec2 in_vert;
    in vec3 in_color;
    out vec3 color;
    void main() {
        gl_Position = model * vec4(in_vert, 0.0, 1.0);
        color = in_color;
    }
    """,
    fragment_shader="""
    #version 330
    in vec3 color;
    out vec4 fragColor;
    void main() {
        fragColor = vec4(color, 1.0);
    }
""")

vertices = np.array([
    -0.6, -0.6,
    1.0, 0.0, 0.0,
    0.6, -0.6,
    0.0, 1.0, 0.0,
    0.0, 0.6,
    0.0, 0.0, 1.0,
], dtype='f4')

vbo = ctx.buffer(vertices)
# Context.buffer(data=None, reserve=0, dynamic=False) → Buffer
#   data (bytes) – Content of the new buffer.
#   reserve (int) – The number of bytes to reserve.
#   dynamic (bool) – Treat buffer as dynamic.

vao = ctx.vertex_array(prog, vbo, 'in_vert', 'in_color')
# Context.vertex_array(*args, **kwargs) → VertexArray
#   program (Program) – The program used when rendering.
#   content (list) – A list of (buffer, format, attributes). See Buffer Format.
#   index_buffer (Buffer) – An index buffer.
#   index_element_size (int) – byte size of each index element, 1, 2 or 4.
#   skip_errors (bool) – Ignore skip_errors varyings.
fbo = ctx.framebuffer(color_attachments=[ctx.texture((512, 512), 4)])

fbo.use()
ctx.clear()
prog['model'].write(Matrix44.from_eulers((0.0, 0.1, 0.0), dtype='f4'))
vao.render(moderngl.TRIANGLES)

data = fbo.read(components=3)
image = Image.frombytes('RGB', fbo.size, data)
image = image.transpose(Image.FLIP_TOP_BOTTOM)
import os
from motiontools import normpath, dir_of_file
output = normpath(dir_of_file(), "output")
image.save(normpath(output, 'headless_ubunut18_server.png'))
