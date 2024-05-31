import glfw
from .window_settings import Window_settings
from arx_resources import Loader

class Window:
    initialized: bool = False
    main_window = None

    @classmethod
    def initialize(cls, window_settings: Window_settings):
        cls.main_window = glfw.create_window(window_settings.dimensions.x, window_settings.dimensions.y, window_settings.title, None, None)
        glfw.make_context_current(cls.main_window)

    @classmethod
    def terminate(cls):
        glfw.destroy_window(cls.main_window)
        glfw.terminate()

    @classmethod
    def should_close(cls) -> bool:
        return glfw.window_should_close(cls.main_window)
    
    @classmethod
    def flip(cls):
        glfw.swap_buffers(cls.main_window)

    

Window.initialize(Loader.load(".engine_resources/window_settings.pkl"))