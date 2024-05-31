from arx_resources import * 
import arx_rendering
from arx_input import Input_handler

arx_rendering.initialize()

while True:
    arx_rendering.Context.clear()

    Input_handler.handle_input()
    
    arx_rendering.Window.flip()