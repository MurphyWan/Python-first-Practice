


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
import timeit
def funl (x, y):      
     return x**2 + y**3

t_start  =  timeit.default_timer()
z =  funl(109.2, 367.1)
t_end  =   timeit.default_timer()

cost  =  t_end -t_start
print ( 'Time cost of funl is  %f' %cost)
```

------------------------------以下为英文原文-------------------------------------

* Try to import the module timeit and use it to obtain how long you computer takes to run a specific code.

```python
import timeit
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

## 我们会遇到的模块

* NumPy：多维数组的有效操作。 高效的数学函数。
* Matplotlib：可视化：2D和（最近）3D图
* SciPy：大型库实现各种数值算法，例如：            
  - 线性和非线性方程的解
  - 优化
  - 数值整合

* Sympy：符号计算（解析的 Analytical）
* Pandas：统计与数据分析（明天）

------------------------------以下为英文原文-------------------------------------

## Modules we will encounter
* NumPy: Efficient manipulation of multidimensional arrays. Efficient mathematical functions.
* Matplotlib: Visualisations: 2D and (recently) 3D plots
* SciPy: Large library implementing various numerical algorithms, e.g.:
  - solution of linear and nonlinear equations           
  - optimisation           
  - numerical integration
* Sympy: Symbolic computation (Analytical).
* Pandas: Statistical and data analysis(tomorrow)


```python
```


## Numpy




```python
```


## ndarray类型
* NumPy提供了一种新的数据类型：ndarray（n维数组）。
  - 与元组和列表不同，数组只能存储相同类型的对象（例如只有floats或只有ints）  
  - 这使得数组上的操作比列表快得多; 此外，阵列占用的内存少于列表。  
  - 数组为列表索引机制提供强大的扩展。


------------------------------以下为英文原文-------------------------------------


## The ndarray type

* NumPy provides a new data type: ndarray (n-dimensional array).  
  
  - Unlike tuples and lists, arrays can only store objects of the same type (e.g. only floats or only ints)  
  - This makes operations on arrays much faster than on lists; in addition, arrays take less memory than lists.  
  - Arrays provide powerful extensions to the list indexing mechanism.






```python
```



## 创建ndarray

* 我们导入Numpy（在脚本的开头或终端）：

```python
import numpy as np
```

* 然后我们创建numpy数组：

```python
In [1] : np.array([2, 3, 6, 7])   
Out[l] : array([2, 3, 6, 7])   
In [2] : np.array([2, 3, 6, 7.])   
Out [2] :  array([ 2.,  3.,  6., 7.])  <- Hamogenaous   
In  [3] :  np.array( [2,  3,  6,  7+ij])   
Out [3] :  array([ 2.+O.j,  3.+O.j,  6.+O.j,  7.+1.j])
```


------------------------------以下为英文原文-------------------------------------

Create the ndarray
* We import Numpy (at the beginning of the script or in the terminal): 
```python
import numpy as np
```
* Then we create numpy arrays:   

```python
In [1] : np.array([2, 3, 6, 7])   
Out[l] : array([2, 3, 6, 7])   
In [2] : np.array([2, 3, 6, 7.])   
Out [2] :  array([ 2.,  3.,  6., 7.])  <- Hamogenaous   
In  [3] :  np.array( [2,  3,  6,  7+ij])   
Out [3] :  array([ 2.+O.j,  3.+O.j,  6.+O.j,  7.+1.j])
```


```python
```



## 创建均匀间隔的数组

* arange：

```python          
in[1]：np.arange（5）
Out [l]：array（[0，1，2，3，4]）
```    

  range(start, stop, step)的所有三个参数即起始值，结束值，步长都是可以用的 另外还有一个数据的dtype参数 
  
  
```python
  in[2]：np.arange（10，100，20，dtype = float）
  Out [2]：array（[10.，30.，50.，70.，90.]）
```
  
* linspace（start，stop，num）返回数字间隔均匀的样本，按区间[start，stop]计算：

```python
  in[3]：np.linspace（0.，2.5，5）         
  Out [3]：array（[0.，0.625，1.25，1.875，2.5]）
```   
  
  * 注释：即从0开始，到2.5结束，然后分成5等份
  
  这在生成plots图表中非常有用。



------------------------------以下为英文原文-------------------------------------


##  Creating evenly spaced arrays
* arange:
```python
         In [1] : np.arange(5)
         Out[l] : array([0, 1, 2, 3, 4])
```

  -  All three parameters of range (start, stop, step) are supported, plus an additional dtype argument for data type:

```python
        In  [2] : np.arange(l0, 100, 20. dtype=float)        
        Out [2] : array([ 10.,  30.,  50.,  70., 90.])
```

* linspace(start, stop, num) Returns num evenly spaced samples, calculated over the interval [start, stop]:

```python
      In [3] : np.linspace(0., 2.5, 5)        
      Out[ 3] : array([ 0. , 0.625, 1.25 , 1.875, 2.5])
```

   Very useful in generation plots.





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


