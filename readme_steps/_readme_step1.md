# Этап 1
- [Оглавление](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/README.md);
- [Код](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/step1.py).

## Задача
- Создать окно приложения, контекст OpenGL; 
- Очистить фон и отрисовать одну точку.

## Теория

Класс [Canvas](https://github.com/vispy/vispy/blob/master/vispy/app/canvas.py) - представление GUI элемента в контексте OpenGL.

Параметры:
- **title(str)**: строка, залоговок окна;
- **size((width, height))**: структура (целое число, целое число), размер окна;
- **position((x, y))**: структура (целое число, целое число), положение окна в координатах экрана;
- **show(bool)**: T/**F**,  не показывать окно сразу;
- **autoswap(bool)**: **T**/F, следует ли менять буферы автоматически после отрисовки:
    - если T, метод *swap_buffers* Canvas будет вызываться последним обработчиком события *canvas.draw*.
- **app(Application | str)**: *Give vispy Application instance to use as a backend. (vispy.app is used by default.) If str, then an application using the chosen backend (e.g., 'pyglet') will be created. Note the canvas application can be accessed at canvas.app*;
- **create_native(bool)**: **T**/F, создать окно немедленно;
- **vsync(bool)**: T/F, включить вертикальную синхронизацию;
- **resizable(bool)**: T/F, разрешить изменять размер окна;
- **decorate(bool)**: **T**/F, украсить окно;
- **fullscreen(bool | int)**: структура(T/**F**, целое число)
  - если F использовать оконный режим;
  - если T использовать полноэкранный режим;
  - если указано целое число, то использовать монитор с этим номером.
- **config(dict)**: *A dict with OpenGL configuration options, which is combined with the default configuration options and used to initialize the context. See canvas.context.config for possible options*;
- **shared:(Canvas | GLContext | None)**: *An existing canvas or context to share OpenGL objects with*.
- **keys:(str | dict | None)**: структура(строка, словарь)
Default key mapping to use. If 'interactive', escape and F11 will close the canvas and toggle full-screen mode, respectively. If dict, maps keys to functions. If dict values are strings, they are assumed to be Canvas methods, otherwise they should be callable.
- **parent:(widget-object)**: The parent widget if this makes sense for the used backend.
- **dpi:(float | None)**: Resolution in dots-per-inch to use for the canvas. If dpi is None, then the value will be determined by querying the global config first, and then the operating system.
- **always_on_top:(bool)**: If True, try to create the window in always-on-top mode.
- **px_scale:(int > 0)**: A scale factor to apply between logical and physical pixels in addition to the actual scale factor determined by the backend. This option allows the scale factor to be adjusted for testing.

События:
- **initialize**;
- **resize**;
- **draw**;
- **mouse_press**;
- **mouse_release**;
- **mouse_double_click**;
- **mouse_move**;
- **mouse_wheelм**;
- **key_press**;
- **key_release**;
- **stylus**;
- **touch**;
- **close**.

## Результат

![step1_result](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/images/step1_result.jpg)

