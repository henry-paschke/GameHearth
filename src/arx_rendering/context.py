import moderngl as gl
from PIL import Image
from .color import Color

class Context:
    initialized: bool = False
    gl_context: gl.Context = None

    @classmethod
    def create_texture(cls, image: Image) -> gl.Texture:
        return cls.gl_context.texture(image.size, 4, image.tobytes())

    @classmethod
    def initialize(cls) -> None:
        cls.gl_context = gl.create_context()
        cls.initialized = True

    @classmethod
    def clear(cls, color: Color = Color()) -> None:
        cls.gl_context.clear(color.r, color.g, color.b, color.a)