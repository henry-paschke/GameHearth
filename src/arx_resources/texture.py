import moderngl as gl
from PIL import Image

from .resource import Resource
from .imported_resource import Imported_Resource
from .loader import Loader
from arx_rendering import Context

def load_texture(path: str) -> gl.Texture:
    texture_image = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM)
    return Context.create_texture(texture_image)

Loader.file_associations[".png"] = "load_texture"
Loader.load_texture = load_texture


class Texture (Imported_Resource):
    def __init__(self, import_path: str, resource_path: str = None) -> None:
        super().__init__(import_path, resource_path)

        self.mipmaps_enabled = True
        self.default_filter = gl.NEAREST
        #self.default_wrap = gl.REPEAT
