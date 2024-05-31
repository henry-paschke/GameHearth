import glfw

class Input_handler:
    initialized = False

    @classmethod
    def handle_input(cls):
        glfw.poll_events()

    @classmethod
    def initialize(cls):
        cls.initialized = True


Input_handler.initialize()