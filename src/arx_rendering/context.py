import moderngl as gl
from PIL import Image
from .window import Window

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

Context.initialize()