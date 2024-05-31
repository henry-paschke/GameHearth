from arx_resources import Resource
from arx_math import Vector2


class Window_settings(Resource):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.dimensions = Vector2(800, 600)
        self.title = "Arx Engine"
        self.fullscreen = False
        self.vsync = True
        self.resizable = True