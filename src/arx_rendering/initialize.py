from arx_resources import Loader

from .window_settings import Window_settings
from .rendering_settings import Rendering_Settings

from .rendering import Rendering
from .window import Window
from .context import Context

def initialize(window_settings: Window_settings = None, rendering_settings: Rendering_Settings = None) -> None:
    if window_settings is None:
        window_settings = Loader.load(".engine_resources/window_settings.pkl")
    if rendering_settings is None:
        rendering_settings = Loader.load(".engine_resources/rendering_settings.pkl")
    Rendering.initialize()
    Window.initialize(window_settings)
    Context.initialize()
    Rendering.apply_settings(rendering_settings)