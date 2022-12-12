# Sophie Davidson 2022, for IMT Atlantique

# Imports -----------------------------------------------------------------------
import pyglet
from pyglet.window import Window
from pyglet.text import Label


# Display the message given as a parameter in a small onscreen window
def displayMessage(message):
    window = Window(300, 180)
    window.set_caption("Eye Control Mouse")
    pyglet.gl.glClearColor(1, 1, 1, 1)  # background colour

    # Create a label for the button text
    label = Label(message,
                  x=window.width//2,
                  y=window.height//2+25,
                  anchor_x='center',
                  anchor_y='center',
                  color=(0, 0, 0, 255))

    description = Label("\nPress space to continue",
                        x=window.width//2,
                        y=window.height//2 - 25,
                        anchor_x="center",
                        anchor_y="center",
                        color=(0, 0, 0, 255))

    # When space is pressed, close the window
    @window.event
    def on_key_press(symbol, modifiers):
        # If the space key is pressed, close the window
        if symbol == pyglet.window.key.SPACE:
            window.close()

    @window.event
    def on_draw():
        window.clear()
        label.draw()
        description.draw()

    pyglet.app.run()
