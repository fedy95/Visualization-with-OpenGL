[задание](https://alepoydes.github.io/introduction-to-numerical-simulation/practice/render/render.html).

![Этап 1](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/step1.py): 
- Создать окно приложения, контекст OpenGL; 
- Очистить фон и отрисовать одну точку.

Результат:

![step1_result](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/images/step1_result.jpg)

![Этап 2](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/step2.py):
- Подготовить массив данных для отрисовки, обновлять массив по таймеру;
- Отрисовать точки решетки на водной поверхности;
- Сделать анимацию;
- Положение камеры считать фиксированным: камера смотрит на воду сверху, перпендикулярно поверхности.

Уравнение плоской волны:

![\xi(x,t)=Acos(\omega t)=Acos(2\pi\nu t)](http://latex.codecogs.com/svg.latex?%5Cfn_jvn%20%5Cxi%28x%2Ct%29%3DAcos%28%5Comega%20t%29%3DAcos%282%5Cpi%5Cnu%20t%29)

**nwave** - количество волн.

![waveVector=nwave*\begin{bmatrix}
 wV_{11}& wV_{12}\\ 
 \vdots& \vdots\\ 
 wV_{nwave1}& wV_{nwave2}
\end{bmatrix}](http://latex.codecogs.com/svg.latex?%5Cfn_jvn%20waveVector%3Dnwave*%5Cbegin%7Bbmatrix%7D%20wV_%7B11%7D%26%20wV_%7B12%7D%5C%5C%20%5Cvdots%26%20%5Cvdots%5C%5C%20wV_%7Bnwave1%7D%26%20wV_%7Bnwave2%7D%20%5Cend%7Bbmatrix%7D)

![\nu=angularFrequency=\frac{\begin{bmatrix}aF_{11}&  \cdots &  aF_{1nwave}\end{bmatrix}}{nwave}](http://latex.codecogs.com/svg.latex?%5Cfn_jvn%20%5Cnu%3DangularFrequency%3D%5Cfrac%7B%5Cbegin%7Bbmatrix%7DaF_%7B11%7D%26%20%5Ccdots%20%26%20aF_%7B1nwave%7D%5Cend%7Bbmatrix%7D%7D%7Bnwave%7D)

![\omega=phase=2\pi\nu=2\pi*angularFrequency=2\pi*\begin{bmatrix}aF_{11}&  \cdots &  aF_{1nwave}\end{bmatrix}](http://latex.codecogs.com/svg.latex?%5Cfn_jvn%20%5Comega%3Dphase%3D2%5Cpi%5Cnu%3D2%5Cpi*angularFrequency%3D2%5Cpi*%5Cbegin%7Bbmatrix%7DaF_%7B11%7D%26%20%5Ccdots%20%26%20aF_%7B1nwave%7D%5Cend%7Bbmatrix%7D)

![A=amplutude=\frac{\begin{bmatrix}A_{11}&  \cdots &  A_{1nwave}\end{bmatrix}}{nwave}](http://latex.codecogs.com/svg.latex?%5Cfn_jvn%20A%3Damplutude%3D%5Cfrac%7B%5Cbegin%7Bbmatrix%7DA_%7B11%7D%26%20%5Ccdots%20%26%20A_%7B1nwave%7D%5Cend%7Bbmatrix%7D%7D%7Bnwave%7D)

Уравнение высоты (z) волны в трехмерном пространстве:

![z=A*cos(\omega + x*waveVector+y*waveVector+t*\nu )](http://latex.codecogs.com/svg.latex?%5Cfn_jvn%20z%3DA*cos%28%5Comega%20&plus;%20x*waveVector&plus;y*waveVector&plus;t*%5Cnu%20%29)

Результат:

![step2_result](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/images/step2_result.gif)

![Этап 3](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/step3.py):
- Отрисовать отрезки, соединяющие соседние узлы решетки (wireframe);
- Убедиться в корректности изображения перспективы.

Изменения по сравнению с этапом 2 помечены в коде как # step3.

Наглядная визуализация работы функции wireframe класса Surface:

![step3_wireframe](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/images/step3_wireframe.jpg)

Результат:

![step3_result](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/images/step3_result.gif)

![Этап 4](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/step4.py):
- Построить триангуляцию поверхности, отрисовать треугольники. 
- Реализовать вычисление цвета отдельных точек треугольинка. 
- Отрисовать ![тепловую карту](https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D0%BF%D0%BB%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BA%D0%B0%D1%80%D1%82%D0%B0) высот.

Изменения по сравнению с этапом 3 помечены в коде как # step4.

Триангуляция - процесс разбиения полигональной области со сложной конфигурацией в набор треугольников.

Треугольник является простейшим полигоном, с использованием множества которых возможно с необходимой точностью аппроксимировать любую плоскость. Таким образом, возможно значительно точно и относительно других методов просто дать представление о кривизне поверхности.

Визуализация реализованного разделения прямоугольника на два треугольника ABC и ACD:

![step4_theory1](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/images/step4_theory1.jpg)

Окрашивание получившихся после триангуляции треугольников логично проводить по единственной изменяющейся переменной - высоте.
Тепловая карта реализовывается с помощью модификации шейдеров, внедренных на предыдущих этапах.

Результат:

![step4_result](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/images/step4_result.gif)

![Этап 5](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/step5.py):
- Вычислить нормали к водной поверхности.
- Реализовать затенение по Фонгу с одним направленным источником света (Солнце) и рассеянным светом.

Ссылки:
![Введение в освещение](https://metanit.com/web/webgl/8.1.php);
![Создание освещенного объекта по модели Фонга. Шейдеры](https://metanit.com/web/webgl/8.2.php);
![Особенности моделирования света: Аппроксимации Фонга (Phong Shading)](http://www.ixbt.com/video/light-model-phong.html).
3
Изменения по сравнению с этапом 4 помечены в коде как # step5.

Выделяют три типа освещения:
- ambient light: окружающее естественное освещение, рассеянный свет (грубо говоря, Directional + Point lights);
- directional light: направленный свет (солнечный свет);
- point light: точечный свет (свет лампы).

![step5_theory1](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/images/step5_theory1.png)

Важно правильно подойти к освещаемому материалу, так как очевидно, что в реальной жизни взаимодействие света и материала дает различные эффекты (например, дерево и металл значительно отличаются при одинаковом освещении).

Освещение объекта непосредственно связано с понятием нормали.

Нормаль - вектор, перпендикулярный освещаемый поверхности.

Нормаль является результатом векторного произведение векторов (в нашем случае векторы это стороны простейшего полигона - треугольника).

![step5_theory2](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/images/step5_theory2.png)

При создании модели освещения необходимо выбрать:
- lighting model (модель освещения/отражения) (в нашем случае в большей степени направленный свет (Солнце));
- shading model (модель затенения) (в нашем случае затенение по Фонгу).

Модель освещения - способ взаимодействия материалов и света для получения финального значения цвета объекта.

Модель затенения - тип интерполяции, с помощью которого возможно получить конечное значение цвета объекта в зависимости от освещения. 

Необходимо установить в шейдерах следующие объекты:
- матрицу нормалей;
- нормали вершины;
- направления света и световые точки;
- цвета освещения.

Например, возьмем пиксель на этом полигоне (красная точка). 

Вектор нормали, соответствующий этому пикселю на поверхности — **n**. 

Свет падает на полигон вдоль вектора **l**. 

Скалярное произведение векторов - количество света, отраженного от данного пикселя. Существуют два способа его подсчета:

![nl=n_xl_x+n_yl_y+n_zl_z](http://latex.codecogs.com/svg.latex?%5Cfn_jvn%20nl%3Dn_xl_x&plus;n_yl_y&plus;n_zl_z)

![nl=\left | n \right |\left | l \right |*cos(\theta)](http://latex.codecogs.com/svg.latex?%5Cfn_jvn%20nl%3D%5Cleft%20%7C%20n%20%5Cright%20%7C%5Cleft%20%7C%20l%20%5Cright%20%7C*cos%28%5Ctheta%29)

Проще проводить расчет со вторым выражением, так как он оперирует с длинами векторов и углом между ними.
- величина нормали к поверхности равна 1;
- величина вектора падающего света приводится к 1 и будет иметь значения от 0 до 1 (1 самый яркий свет).

![step5_theory3](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/images/step5_theory3.gif)

Цвет представляется как сумма рассеянного и направленного света.

Результат:

![step5_result](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/images/step5_result.gif)


------
with vispy
Класс Canvas:

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

Скайбокс (Skybox/cubemap)
- Происходит рендер большого куба и размещение зрителя в центре.

- При движении камеры куб следует за ней, поэтому зритель никогда не достигнет края сцены.

Пример тестуры скайбокса:

![example_skybox](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/images/example_skybox.jpg)
