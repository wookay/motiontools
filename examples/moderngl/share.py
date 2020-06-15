# Object sharing is an experimental feature

"""
import moderngl
import numpy

data1 = numpy.array([1, 2, 3, 4], dtype='u1')
data2 = numpy.array([4, 3, 2, 1], dtype='u1')

ctx1 = moderngl.create_context(standalone=True)
ctx2 = moderngl.create_context(standalone=True, share=True)

with ctx1 as ctx:
    b1 = ctx.buffer(data1)

with ctx2 as ctx:
    b2 = ctx.buffer(data2)

print(b1.glo)  # Displays: 1
print(b2.glo)  # Displays: 2

with ctx1:
    print(b1.read())
    print(b2.read())

with ctx2:
    print(b1.read())
    print(b2.read())
"""
