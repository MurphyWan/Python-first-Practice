


# 《三天搞定Python基础概念之第二天》 Day 2 

```
前言：
非常感谢Jiang老师将其分享出来！本课件非常经典！
只是鉴于Jiang老师提供的原始课件用英文写成，而我作为Python的爱好者计算机英文又不太好，讲义看起来比较慢，
为了提高自学课件的效率，故我花了点时间将其翻译成中文版，以便将来自己快速复习用
该版仅用于个人学习之用，绝不作商业用途。
在征得原作者Yupeng Jiang老师的同意后，现在我将中文版本分享给大家。

```
## 作者：Yupeng Jiang
* 伦敦大学学院 数学系  (英国顶尖大学，2018 QS世界大学排名中位列世界第7名，英国第3名)
* email:yupeng.jiang.13@ucl.ac.uk
* 2016年6月5日
* [课件来自] https://zhuanlan.zhihu.com/p/21332075
## 翻译：Murphy Wan

```python
```

## 大纲（ Outline）

* 第1天：Python和科学编程介绍。 Python中的基础知识：  
  - 数据类型  
  - 控制结构  
  - 功能  
  - I/O文件

* 第2天：用Numpy，Scipy，Matplotlib和其他模块进行计算。 用Python解决一些数学问题。

* 第3天：时间序列：用Pandas进行统计和实际数据分析。 随机和蒙特卡罗。

------------------------------以下为英文原文-------------------------------------

* Day 1: Introduction to Python and scientific programming. Basics in Python: data type, contro structures, fu nctions,  l/O file.
* Day 2: Computation with Numpy, Scipy, Matplotlib and other modules. Solving some maths problems with  Python.
* Day 3: Time series: statistics and real data analysis with Pandas. Stochastics and Monte Carlo.

```python

```

## 第二天的内容
### Import modules
### Numpy
### Scipy
### Matplotlib
### Sympy



```python
```

## 导入模块 (Import modules)

* 可以通过输入import关键字来导入模块

```python
import numpy
```

* 或者使用简称，即将模块通过as关键字来命名一个简称 

```python
import numpy as np
```


* 有时您不必导入整个模块，就像

```python
from scipy.stats import norm
```


------------------------------以下为英文原文-------------------------------------


* One can import a module by typing

```python
import numpy
```

* or for short by

```python
2import numpy as np
```

* Sometimes you do not have to import the whole module, like

```python
from scipy.stats import norm
```



```python
```


## 练习  (Exercise)

* 尝试导入模块时间，并使用它来获取计算机运行特定代码所需的时间。

```python
import timeitdef  
funl (x, y):      
return x**2 + y**3t_start  =  timeit.default_timer()z =  funl(109.2, 367.1)t_end  =   timeit.default_timer()cost  =  t_end -t_startprint ( 'Time cost of funl is  %f' %cost)```


* Try to import the module timeit and use it to obtain how long you computer takes to run a specific code.

```python
impddddfsdfsdfort timeit
def  funl (x, y):      
return x**2 + y**3
t_start  =  timeit.default_timer()
z =  funl(109.2, 367.1)
t_end  =   timeit.default_timer()
cost  =  t_end -t_start
print ( 'Time cost of funl is  %f' %cost)
```







```python
```





```python
```





```python
```




```python
```





```python
```




```python
```






```python
```





```python
```




```python
```





```python
```





```python
```






```python
```





```python
```






```python
```






```python
```






```python
```







```python
```







```python
```







```python
```






```python
```







```python
```







```python
```






```python
```







```python
```







```python
```







```python
```








```python
```









```python
```








```python
```








```python
```







```python
```


