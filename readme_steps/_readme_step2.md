# Этап 2
- [Оглавление](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/README.md);
- [Код](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/step2.py).

## Задача
- Подготовить массив данных для отрисовки, обновлять массив по таймеру;
- Отрисовать точки решетки на водной поверхности;
- Сделать анимацию;
- Положение камеры считать фиксированным: камера смотрит на воду сверху, перпендикулярно поверхности.

## Теория

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

## Результат

![step2_result](https://github.com/fedy95/Visualization-with-OpenGL/blob/master/images/step2_result.gif)
