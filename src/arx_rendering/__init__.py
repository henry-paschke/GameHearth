from .window_settings import Window_settings
from .rendering_settings import Rendering_Settings

#import order is important here
# rendering settings loaded first
from .rendering import Rendering
# Window created with settings from rendering
from .window import Window
# Context created from the window's context
from .context import Context

