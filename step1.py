import numpy as np
from vispy import gloo
from vispy import app
"""
1 этап. 
Создать окно приложения, контекст OpenGL. 
Очистить фон и отрисовать одну точку.
"""

""" Это исходник вершинного шейдера, он будет вызывается для каждой вершины (точки) в отрисовываемой сцене.
 Шейдеры пишутся на языке GLSL, который представляет собой C++ с рядом ограничений и расширений."""
vert = ("""#version 120
        attribute vec2 a_position;
        void main (void) { 
        gl_Position = vec4(a_position.xy,1,1);
        }"""
        )

""" Это исходный текст шейдера фрагменов, он отвечает за определение цвета отображаемых на экране пикселя 
(чуть сложнее, если разрешить смешивание цветов)."""
frag = ("""#version 120
        void main() {
        gl_FragColor = vec4(0.5,0.5,1,1);
        }"""
        )


class Canvas(app.Canvas):
    """ холст """
    def __init__(self):
        """конструктор обьекта окна"""
        app.Canvas.__init__(self, title="step 1", size=(300, 300), vsync=True)
        gloo.set_state(clear_color=(0, 0, 0, 1), depth_test=False, blend=False)
        self.program = gloo.Program(vert, frag)
        self.program["a_position"] = np.array([[0, 0]], dtype=np.float32)
        self.activate_zoom()
        self.show()

    def activate_zoom(self):
        """установка размера окна"""
        self.width, self.height = self.size
        print(self.width, self.height)
        gloo.set_viewport(0, 0, *self.physical_size)

    def on_draw(self, event):
        """перерисовка окна"""
        gloo.clear()
        self.program.draw('points')


if __name__ == '__main__':
    c = Canvas()  # обьект приложения
    app.run()     # обработчик событий.

