import numpy as np
from vispy import gloo
from vispy import app
"""
2 этап. 
Подготовить массив данных для отрисовки, обновлять массив по таймеру. 
Отрисовать точки решетки на водной поверхности. 
Сделать анимацию. 
Положение камеры считать фиксированным: камера смотрит на воду сверху, перпендикулярно поверхности.
"""

""" Это исходник вершинного шейдера, он будет вызывается для каждой вершины (точки) в отрисовываемой сцене.
 Шейдеры пишутся на языке GLSL, который представляет собой C++ с рядом ограничений и расширений."""
vert = ("""#version 120
        attribute vec2 a_position;
        attribute float a_height;
        void main (void) {
            float z=(1-a_height)*0.5;
            gl_Position = vec4(a_position.xy,z,z);
        }"""
        )

""" Это исходный текст шейдера фрагменов, он отвечает за определение цвета отображаемых на экране пикселя 
(чуть сложнее, если разрешить смешивание цветов)."""
frag = ("""#version 120
        void main() {
            gl_FragColor = vec4(0.5,0.5,1,1);
        }"""
        )


class Surface(object):
    """ объект состояния водной глади """
    def __init__(self, size=(150, 200), nwave=5):
        """конструктор обьекта окна"""
        self._size = size
        self._wave_vector = nwave * np.random.randn(nwave, 2)
        self._angular_frequency = np.random.randn(nwave) / nwave
        self._phase = 2 * np.pi * self._angular_frequency
        self._amplitude = np.random.rand(nwave) / nwave

    def position(self):
        """расчет координат точек прямоугольной решетки"""
        xy = np.empty(self._size + (2,), dtype=np.float32)
        xy[:, :, 0] = np.linspace(-1, 1, self._size[0])[:, None]
        xy[:, :, 1] = np.linspace(-1, 1, self._size[1])[None, :]
        return xy  # xy координаты точек - прямоугольную решетку в квадрате [0,1]x[0,1]

    def height(self, t):
        """расчет изменения высот водной глади в момент времени t"""
        x = np.linspace(-1, 1, self._size[0])[:, None]
        y = np.linspace(-1, 1, self._size[1])[None, :]
        z = np.zeros(self._size, dtype=np.float32)
        for n in range(self._amplitude.shape[0]):
            z[:, :] += self._amplitude[n] * np.cos(self._phase[n] +
                                                   x * self._wave_vector[n, 0] + y * self._wave_vector[n, 1] +
                                                   t * self._angular_frequency[n])
        return z  # массив высот водной глади в момент времени t



class Canvas(app.Canvas):
    """ холст """
    def __init__(self):
        """конструктор обьекта окна"""
        app.Canvas.__init__(self, title="step 2", size=(500, 500), vsync=True)
        gloo.set_state(clear_color=(0, 0, 0, 1), depth_test=False, blend=False)
        self.program = gloo.Program(vert, frag)
        self.surface = Surface()  # обьект, который будет давать состояние поверхности
        self.program["a_position"] = self.surface.position()  # xy=const шейдеру,
        self.t = 0  # t - time
        self._timer = app.Timer('auto', connect=self.on_timer, start=True)
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
        self.program["a_height"] = self.surface.height(self.t)  # пересчет высот для текущего времени
        self.program.draw('points')

    def on_timer(self, event):
        """приращение времени с обновлением изображения"""
        self.t += 0.01
        self.update()

    def on_resize(self, event):
        """данные о новом размере окна в OpenGL"""
        self.activate_zoom()


if __name__ == '__main__':
    c = Canvas()  # обьект приложения
    app.run()     # обработчик событий.
