from arx_resources import Resource

class Rendering_Settings (Resource):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.vsync = True
        self.opengl_version = (4, 1)


r = Rendering_Settings(".engine_resources/rendering_settings.pkl")
r.save_to_file()