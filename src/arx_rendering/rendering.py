"""
This file contains the global singleton Rendering, which is used for each rendering operation regardless of window or context.
"""

import glfw
from .rendering_settings import Rendering_Settings

class Rendering:
    initialized: bool = False

    @staticmethod
    def apply_settings(rendering_settings):
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, rendering_settings.opengl_version[0])
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, rendering_settings.opengl_version[1])
        Rendering.set_vsync(rendering_settings.vsync)

    @staticmethod 
    def set_vsync(enabled: bool):
        glfw.swap_interval(1 if enabled else 0)

    @classmethod
    def initialize(cls):
        cls.initialized = True

        if not glfw.init():
            raise Exception("Failed to initialize GLFW")
        
    @classmethod
    def terminate(cls):
        glfw.terminate()