


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
  Out [3]：array([0.，0.625，1.25，1.875，2.5])
  
```  
  
  
  
  这在生成plots图表中非常有用。
  
* 注释：即从0开始，到2.5结束，然后分成5等份


```python
```


## 多维数组矩阵  (Matrix by multidimensional array)

```python
In [1] : a = np.array([[l, 2, 3]  [4, 5, 6]])
                          ^ 第一行 (Row 1)
In  [2] : a
Out [2] : array([[l, 2,  3] ,   [4,  5,  6]])

In  [3] : a.shape  #<- 行、列数等 (Number of rows, columns etc.)
Out [3] : (2,3)

In  [4] : a.ndim   #<- 维度数  (Number of dimensions)
Out [4] : 2

In  [5] : a,size   #<- 元素数量 (Total number of elements)
Out [5] : 6
```




```python
```



## 形状变化  (Shape changing)

```python
import numpy as np

a = np .arange(0, 20, 1) ＃1维
b = a.reshape((4, 5))   ＃4行5列
c = a.reshape((20, 1))  ＃2维
d = a.reshape((-1, 4))  ＃-1：自动确定
＃a.shape =(4, 5) ＃改变a的形状
```




```python
```


##  Size（N，），（N，1）和（1，N）是不同的!!!

* Size（N, ）表示数组是一维的。
* Size（N，1）表示数组是维数为2, N列和1行。
* Size（1，N）表示数组是维数为2, 1行和N列。

让我们看一个例子,如下




```python
```


## 例子 (Example)

```python
import numpy as np

a = np.array([1,2,3,4,5])
b = a.copy ()

c1 =  np.dot(np.transpose(a), b)
print(c1)
c2  = np.dot(a, np.transpose(b))
print(c2)

ax  =  np.reshape(a, (5,1))
bx  =  np.reshape(b, (1,5))
c = np.dot(ax, bx)
print(c)
```



```python
```



## 使用完全相同的元素填充数组 (Filling arrays with identical elements)

```python
In [1] : np.zeros(3)              # zero(),全0填充数组
Out[l] : array([ O., 0., 0.])

In [2] : np.zeros((2, 2), complex)
Out[2] : array([[ 0.+0.j, 0.+0.j],                
                [ 0.+O.j, 0.+0.j]])

In [3] : np.ones((2, 3))          # ones(),全1填充数组
Out[3] : array([[ 1., 1., 1.],
                [ 1., 1., 1.]])
```





```python
```


## 使用随机数字填充数组 (Filling arrays with random numbers)

* rand: 0和1之间均匀分布的随机数  (random numbers uniformly distributed between 0 and 1)

```python   
   In [1] : np.random.rand(2, 4)   
   Out[1] : array([[ 0.373767 , 0.24377115, 0.1050342 , 0.16582644] , 
                   [ 0.31149806, 0.02596055, 0.42367316, 0.67975249l])
```

* randn: 均值为0，标准差为1的标准（高斯）正态分布  {standard normal (Gaussian) distribution with mean 0 and variance 1} 

```python
  In [2]: np.random.randn(2, 4)  
  Out[2]: array([[ O.87747152, 0.39977447, -0.83964985, -1.05129899], 
                 [-1.07933484, 0.49448873,   -1.32648606, -0.94193424]])
```

* 其他标准分布也可以使用 (Other standard distributions are also available.)



```python
```



## 数组切片（1D） (Array sliciing(1D))

* 以格式start：stop可以用来提取数组的片段（从开始到不包括stop）

```python
In [77]：a = np.array（[0，1，2，3，4]）
Out[77]：array（[0，1，2，3，4]）

In [78]：a [1：3]        #<--index从0开始 ,所以1是第二个数字，即对应1到3结束，就是到第三个数字，对应是2
Out[78]：array([1，2])
```

* start可以省略，在这种情况下，它被设置为零(Notes:貌似留空更合适)：

```python
In [79]：a [:3]
Out[79]：array（[0，1，2]）
```

* stop也可以省略，在这种情况下它被设置为数组长度：

```python
In [80]：a [1：]
Out[80]：array（[1，2，3，4]）
```

* 也可以使用负指数，具有标准含义：

```python
In [81]：a [1：-1]
Out[81]：array（[1,2,3]）      # <-- stop为-1表示倒数第二个数
```





```python
```



## 阵列切片（1D）

* 整个数组：a或a [：]  

```python
In [77]：a = np.array（[0,1,2,3,4]）
Out[77]：array（[0，1，2，3，4])
```
* 要获取，例如每个其他元素，您可以在第二个冒号后面指定第三个数字（步骤(step)）：  
```python
In [79]：a [：：2]
Out[79]：array（[0，2，4]） 

In [80]：a [1：4：2]
Out[80]：array（[l，3]）
```
* -1的这个步骤可用于反转数组：

```python
In [81]：a [::-1]
Out[81]：array（[4，3，2，1，0]）
```








```python
```



## 数组索引(2D)  （Array indexing (2D)）

* 对于多维数组，索引是整数元组：(For multidimensional arrays, indices are tuples of integers:)  

```python
In [93] :  a = np.arange(12) ; a.shape =  (3,  4);  a
Out[93] :  array([[0,  1,  2,  3],
                  [4,  5,  6,  7],
                  [8, 9,  10, 11]])

In [94] : a[1,2]
Out[94] : 6

In [95] : a[1,-1]
Out[95] : 7
```







```python
```





## 数组切片（2D）：单行和列 (Array slicing (2D): single rows and columns)

* 索引的工作与列表完全相同：（Indexing works exactly like for lists:）

```python
In [96] : a = np.arange(12); a.shape = (3, 4); a   
Out[96] : array([[0, 1, 2, 3],
                 [4, 5, 6, 7],
                 [8, 9,10,11]])

In [97] : a[:,1]
Out[97] : array([1,5,9])

In [98] : a[2,:]
Out[98] : array([ 8, 9, 10, 11])

In [99] : a[1][2]
Out[99] : 6
```

* 不必明确提供尾随的冒号：（Trailing colons need not be given explicitly:）

```python
In [100] : a[2]
Out[100] : array([8,9,10,11]) 
```





```python
```




## 数组索引 (Array indexing)

```python

>>> a[0,3:5]
array( [3,4] )

>>> a[4:,4:]
array([[44, 45], 
       [54, 55]])

>>> a[:,2]
array([2,12,22,32,42,52])

>>> a[2: :2, ::2]
array([[20, 22, 24]       
       [40, 42, 44]])

```

![note-book0](https://github.com/MurphyWan/Python-first-Practice/blob/master/images/mofang.jpg)



```python
```



## 副本和视图

* 采用标准的list切片建其副本
* 采用一个NumPy数组的切片可以在原始数组中创建一个视图。 两个数组都指向相同的内存。因此，当修改视图时，原始数组也被修改：

```python
In [30] : a = np.arange(5); a
Out[30] : array([0, 1, 2, 3, 4])

In [31] : b = a[2:]; b
Out[31] : array([2, 3, 4])

In [32] : b[0] = 100
In [33] : b

Out[33] : array([l00, 3, 4])
In [34] : a
Out[34] : array([0,1,100,3,4])
```





```python
```






## 副本和视图 (Copies and views)

* 为避免修改原始数组，可以制作一个片段的副本 (To avoid modifying the original array, one can make a copy of a slice:)

```python
In [30] : a = np.arange(5); a
Out[30] : array([0, 1, 2, 3, 4])

In [31] : b = a[2:].copy(); b
Out[31] : array([2, 3, 4])

In [32] : b[0] = 100
In [33] : b
Out[33] : array([1OO, 3, 4])

In [34] : a 
Out[34] : array([ 0,  1.  2,  3,  4])

```




```python
```



## 矩阵乘法  (Matrix multiplication)

* 运算符 \* 表示元素乘法，而不是矩阵乘法：(The * operator represents  elementwise multiplication , not matrix multiplication:)    

```python

In [1]: A = np.array([[1, 2],[3, 4]])
In [2]: A
Out[2]: array([[1, 2],
               [3, 4]])

In [3]: A * A
Out[3]: array([[1, 4],
               [9, 16]])            
```

* 使用dot（）函数进行矩阵乘法：(Matrix multiplication is done with the dot() function:)

```python

In [4]: np.dot(A, A)
Out[4]: array([[ 7, 10],    
               [15, 22]])  
```




```python
```


## 矩阵乘法

* dot（）方法也适用于矩阵向量(matrix-vector)乘法：

```python

In [1]: A
Out[1]: array([[1, 2],[3, 4]])

In [2]: x = np.array([10, 20])
In [3]: np.dot(A, x)
Out[3]: array([ 50, 110])

In [4]: np.dot(x, A)
Out[4]: array([ 70, 100])

```



```python
```


## Numpy包含更高效率的功能

* Numpy包含许多常用的数学函数，例如：
  
  - np.log
  - np.maximum
  - np.sin
  - np.exp
  - np.abs

* 在大多数情况下，Numpy函数比Math包中的类似函数更有效，特别是对于大规模数据。




```python
```


## Scipy (库)



```python
```



## SciPy的结构

* scipy.integrate  - >积分和普通微分方程
* scipy.linalg  - >线性代数
* scipy.ndimage  - >图像处理
* scipy.optimize  - >优化和根查找(root finding)
* scipy.special  - >特殊功能
* scipy.stats  - >统计功能
* ...

要加载一个特定的模块，请这样使用, 例如 :

* from scipy import linalg



```python
```



## 线性代数  (Linearalgebra)         

* 线性方程的解  (Solution of linear equations:)

```python

import numpy as np
from scipy import linalg    

A = np.random.randn(5, 5)
b = np.random.randn(5)
x = linalg.solve(A, b)     # A x = b#print(x)    
eigen = linalg.eig(A)     # eigens#print(eigen)    
det = linalg.det(A)     # determinant    
print(det)            

```

* linalg的其他有用的方法：eig()（特征值和特征向量），det()（行列式）。{Other useful functions from linalg: eig() (eigenvalues and eigenvectors), det()  (determinant). } 



```python
```





## 数值整合  (Numerical integration)

* integration.quad是一维积分的自适应数值积分的函数。 (integrate.quad is a function for adaptive numerical quadrature of one-dimensional integrals.)

```python

import numpy as np
from scipy import integrate

def fun(x):
    return np.log(x)

value, error = integrate.quad(fun,0,1)
print(value)
print(error)

```

![Numerical-integration](https://github.com/MurphyWan/Python-first-Practice/blob/master/images/3days_img009_Numerical-integration.jpg)


```python
```




## Statistics in Scipy

* scipy has a sub-library for statistical functions, you can import it by

```python
from scipy import stats
```

* Then you are able to use some useful statistical function. For example, the cummulative density function of a standard normal distribution is given like
()

* With this package, we can directly use it like

```python
from scipy import statsy = stats.norm.cdf(1.2)
```

![Statistics-in-Scipy](https://github.com/MurphyWan/Python-first-Practice/blob/master/images/3days_img010_statistics_in_scipy.jpg)



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


