# Python-first-Practice



# 《三天搞定Python基础概念之第一天》

"""
#### 注释：鉴于Jiang老师提供的原始课件是英文版本，而我的计算机英文不太好，讲义看起来比较慢，为了提高学习效率，故我花了点时间将其翻译成中文版。该版本仅用于个人学习使用，绝不作商业用途。现将其分享出来。翻译水平有限，若有不当之处，还请大家指正。谢谢！
"""

## 作者：Yupeng Jiang
* 伦敦大学学院 数学系（英国顶尖大学，2018 QS世界大学排名中位列世界第7名，英国第3名）
* email:yupeng.jiang.13@ucl.ac.uk
* 2016年6月5日
* [课件来自] https://zhuanlan.zhihu.com/p/21332075
## 翻译：Murphy Wan


## 大纲（ Outline）
* 第1天：Python和科学编程介绍。 Python中的基础知识：  - 数据类型  - 控制结构  - 功能  - I/O文件
* 第2天：用Numpy，Scipy，Matplotlib和其他模块进行计算。 用Python解决一些数学问题。
* 第3天：时间序列：与Pandas统计和实际数据分析。 随机序列和蒙特卡罗。

------------------------------以下为英文原文-------------------------------------

* Day 1: Introduction to Python and scientific programming. Basics in Python: data type, contro structures, fu nctions,  l/O file.
* Day 2: Computation with Numpy, Scipy, Matplotlib and other modules. Solving some maths problems with  Python.
* Day 3: Time series: statistics and real data analysis with Pandas. Stochastics and Monte Carlo.


## _
* Python的背景
* Python基础知识
* 控制结构
* 功能
* 读/写文件
* 实验部分

------------------------------以下为英文原文-------------------------------------

* Background of Python
* Basic knowledge on Python
* Control structures
* Functions
* Reading/writing files
* Lab session


## 为什么使用Python （ Why Python?）
* Python是开源的，这意味着它是免费的。
* Python是一种胶水语言：   
  - Python使你的编码更加轻松  
  - Python平均来讲，比一些语言计算更快，比如Matlab
* Python有一个很大的程序员社区。 它带来了与大量的标准库和扩展包。
* Python广泛应用于各种行业（Google，NASA，对冲基金，银行等）。

------------------------------以下为英文原文-------------------------------------

Why Python?

* Python is open source, which means it is free.
* Python is a glue language.  
  - Python makes your coding life easier.  
  - Python is faster (on average) than some computing a pplications, like Matlab.
* Python has a large community of programmers. It comes   with a large number of standard library and extended  packages.
* Python is widely used in the industry (Google, NASA   hedge funds, banks, etc.).


## 使用Python 2或3？
* Python 3不能向后兼容Python 2，这意味着Python 2中的某些软件包或库无法在Python 3中使用。
* 然而，许多机构仍在使用Python 2，因为仍然有几个软件包与Python 3不兼容。
* Python 2.x是历史遗留物，而现在，Python 3.x是该语言的未来。 2010年年中，2.7版本的2.7版本将不会再出现新的主要版本。
* 我们会遇到一些差异，但不会太多。
* 检查https://wiki.python.org/moin/Python2 或Python3或其他在线资源获取更多信息

------------------------------以下为英文原文-------------------------------------

Python 2 or 3?
* Python 3 is not backward compatible with Python 2 which means some packages or libraries in Python 2 cannot work on Python 3.
* However, a large number of institutions are still using Python 2 since there is still several packages incompatible with Python 3.
* Python 2.x is legacy and the present, Python 3.x is the future of the language. The 2.x branch will see no new major releases after 2.7 in mid-2010.
* We will encounter some difFerences, but not much.
* Checkhttps : //wiki.python.org/moin/Python2 or Python3 or other online resources for more information


## 一些在线资源 （Some online resources）
* http://openbookproject.net/thinkcs/python/english2e/ 通过前几章能获得基本思想。
* http://learnpythonthehardway.org/book/ 做练习。
* https://www.kevinsheppard.com/images/0/09/Python_introduction.pdf 强大的计量经济学重点。本说明的部分内容基于本文档。
* 对于一些特定的软件包，如Numpy和Pandas，最好的学习方法是使用他们的官方文档，并自己实现一些例子。
* 使用Google和一堆程序员相互切磋的Stack Overflow网站。

------------------------------以下为英文原文-------------------------------------

* http://openbookproject.net/thinkcs/python/english2e/ First few chapters to get the basic idea
* http://learnpythonthehardway.org/book/Exercises.
* https://www.kevinsheppard.com/images/0/09/Python_introduction.pdf A strong econometrics focus. Parts of this note are based on this document.
* For some particular packages, such as Numpy and Pandas, the best way to learn is to use their official documentation and implement some examples by yourself.
* Use Google and Stack Overflow.


## Python环境 （Python environment）

* 安装Python科学堆栈的推荐方法是使用Continuum Analytics Anaconda。
* Anaconda是一个免费的软件包管理器，环境管理器，以及开源软件包的集合。
* Anaconda包括核心Python解释器和标准库。
* https://www.continuum.io/downloads

------------------------------以下为英文原文-------------------------------------

* The recommended method to install the Python scientific stack is to use Continuum Analytics Anaconda.
* Anaconda is a free package manager, environment manager, and collection of open source packages.
* Anaconda includes both the core Python interpreter and standard libraries.
* https://www.continuum.io/downloads



## Anaconda中包括的库（Libararies）
* NumPy（http://numpy.scipy.org ）：该库用于处理（大）数组。
* SciPy（http://www.scipy.org ）：该库包含许多有用的科学功能。
* Matplotlib（http://matplotlib.sourceforge.net ）：该库用于绘图。
* Pandas（http://pandas.sourceforge.net ）：该库有效并快速分析大数据集; 尤其针对金融时间序列。
* IPython（http://wprw.ipython.org ）：shell、或基于浏览器：开发环境。
* Spyder（http://pythonhosted.org/spyder/ ）：IDE交互式开发环境


## 管理你的Anaconda
* 在你的终端或cmd，输入
 conda list
* 您可以看到已安装的软件包列表
* 更多的管理方法可以在这里找到：  http://conda.pydata.org/docs/using/pkgs.html


## 你可以在本课程中学到什么？                                       
* 本课程是为初学者设计的。 它不需要任何以前的任何编程语言的知识。
* Python编程的基础知识。
* 使用Numpy，Scipy和Sympy进行数学计算。
* 使用Matplotlib库绘制图形。
* 与Pandas分析实际数据和时间序列。
* 学习如何使用它作为工具。


## 今天的安排
* 早上：Python编程基础介绍。 在上午的会议中，您将需要做一些练习。 只是一些热身水平的问题，他们会给你一个关于Python编程的想法。
* 下午：半小时内完成介绍部分。 那么我们会有三个大问题要解决。 他们将是今天的一个很好的总结：讲座。 你将有一个小时独立工作。 然后，我将在过去半小时内提供分析和解决方案。



Today's arrangements
* Morning: An introduction to Python programming basics. There will be a few exercises you need to do during the morning session.  But just some warm-up level  questions, and they will give you an idea about Python programming.
* Afternoon: We will finish the introduction part in half an hour. Then we will have three big problems to solve. They will be a good summary of today:s lecture. You will have one hour to work them out independently. I will then provide the analytics and the solutions in the last half an hour.


## 练习1
* 安装Anaconda并更新它以便拥有   所有包的最新版本。 我们将使用Python 3.4（而不是以前的Python 2.7版本）。
* 通过键入以下命令启动Spyder并计算76：     
  
  x = 7 ** 6   打印（x）

* 启动IPython Notebook并计算7的6次方

-----------------

Exercises 1

* Install Anaconda and update it in order to have the  newest version of all packages. We shall use Python 3.4 (and not the previous Python 2.7 version).
* Start Spyder and compute 76 by typing:    

x = 7 ** 6  print (x)

* Start IPython Notebook and compute 76

```python
```


## 缩进（Indentation）
* 在某些语句之后，会加一个缩进; 缩进减少，则表示当前块结束。
* 例如
    x = 7 ** 6
    print（x）#witt. fron't  inden-tation
* 段代码在Python中是错误的，虽然它在C ++，Matlab和许多其他代码或应用程序中是可以接受的。

--------------

* An increase in indentation comes after certain statements; a decrease in indentation signifies the end of the current block.
* For e.g
x = 7 ** 6          print (x)  # witt. fron't  inden-tation
* This piece of code will be error in Python, though it is acceptable in C++, Matlab and many other code or applications.


## 编程中的一些好习惯（Some good habit in programming）
* 在需要缩进和换行的地方使用这个功能；不要把你的脚本弄乱了。
* 不要使用没有意义的变量；要用可以被描述的变量。
* 写注释。 帮助别人和自己在以后理解你现在所写的代码内容。
* 不要同时开始学习多种编程语言。

----------------

* Be consistent with indentation and line break. Don't mess your scripts up.
* Do Never write variables without its real meaning. Write descriptive variables.
* Write comments. Help others and the the future yourself to understand what you write right now.
* Do not start to learn more than one programming language at the same time.


## 关于Python的基础知识（Basic knowlegde on Python）

## 常用的数字数据类型（Common used numeric data types）
|Name|       Notation|  Declaration e.g.
|:--------|--------------:|:------------:|
|Integers|   int|       a = 10|
|Floating|   float|     b = 3.14|
|Complex|    complex|   c = 1 + 2j|
|String|     str|       d = 'Python'|

* 备注：   
- 在Python 2.7中，int与另一个int运算将导致int结果。 但是，一个浮点运算与int会导致浮点数。   
- 在Python 3.x中，int与另一个int运算将导致浮点数。
-----

* Remarks:  - In Python 2.7, an int operates with another int will lead to an int result. However, a float operates with an int will lead to a float.  - In Python 3.x, an int operates with another int will lead to a float.


## 算数运算符（Arithmetic operators）

|Name|Notation|Examples|
|----|:--------:|:--------:|
|Addition|+| a + b |
|Subtraction|-|c - b|
|Multiplication|*|x*y|
|Division|/|x/z|
|Modulus|%|x%a|
|Exponent|**|a**x|


## 练习2（Exercise 2）
* 猜下面代码的结果。执行他们，看答案。
* Try to guess the results of the following code. Implement them and check your answers. 
- a = 10   # int 
- b = 3.14 # fLoat 
- c = 3    #int 
- d = a ** 2 # square of a 
- print (type (d))    # return the type of d  
- print (type (d/l0)) # return the type of d/l0 
- print (type (a/b))  # return the type of a/b 
- print (type (a/c))  # return the type of a/c 
- print (type (b*d))  # return the type of b*d


## 浮点数的精度（Precision of float）
* 尝试在您的控制台中键入0.1 + 0.2。 你会发现这个值是  
- 0.30000000000000004

* 这是二进制浮点的本质。 您可以在支持硬件浮点运算的所有语言中看到同样的东西。
* 可以使用“round（）”功能控制显示精度，但也有上述情况，这意味着round(9.995,2)返回9.99而不是10，因为9.995的存储稍小于9.995。
* decimal Library将给出精确的存储值，请参见以下示例。

----------------

* Try to type 0.1+0.2 in your console. You will find that the value is  - 0.30000000000000004            * This is in the very nature of binary floating-point. You can see the same kind of thing in all languages that support your hardware's floating-point arithmetic.* The display precision can be controled using "round()" function, but it also has above situation, which means round(9.995, 2) returns 9.99 rather than 10, since 9.995 is stored slightly smaller than 9.995.* Library decimal would give precise stored value, See the following example.



## 例子（Example）
* import  decimal  
# import  the  libray  "decimal"    
# display  2  decimal  precision
* print (round (3*1415 ,   2))   #  result  3. 14
* print (round (9 .995 ,   2))   #  result  9. 99

* #call   function   "Decimal "  from lib "decimal"
* print (decimal.Decimal (9.995))
* The last "print" returns
9.9949999999999992184029906638897955417633056640625,
* which is exactly how 9.995 is stored in the hardware.

## 练习3：字符串str的一些功能（Exercise3:Some functions for str）
```python
t = 'He is a string. Who are you?'
print(t.capitalize()) # Cap first letter
print(t.split()) # split by words
print(t.find('i')) # return index of 'i'
print(t.find('in')) # index of 'i' in 'in'
print(t.find('Python')) # find sth not in
print(t[0:4]) # returu from index 0 to 3
print(t.replace(' ','|')) # replace by '|'
w = 'http://www.google.com'
print(w.strip('http://')) #delete sth
```
```python
    He is a string. who are you?    
    ['He', 'is', 'a', 'string.', 'Who', 'are', 'you?']    
    11    
    -1    
    He i    
    He|is|a|string.|Who|are|you?    
    www.google.com    
```

## Python功能：索引（Python features: Indexing）
* Python具有与C ++类似的索引规则，其起始索引为0。
* 当通过索引返回值时，间隔实际上是[，]样式，这意味着不包括终端索引。

--------------------------------
* Python  has similar indexing rules with C++ , where its starting index is 0.
* When you return values by index, the interval is actually [  , ) style, which means that the terminal index will not be included.

## 基本的数据结构（Basic data structures）
|Name| Nation| Declaration e.g.|
|----|-------|-----------------|
|Tuple| tuple| b = (1,2.5, 'data')|
|List|list|c = [1,2.5,'data']|
|Dictionary|dict|d = {'Name': 'Kobe', 'Country':'US'}|
|Set|set|e = set(['u','d','ud','d','du'])|

* 元组（tuple）只有几种方法可以更改。
* 列表（list）比元组更灵活。
* 字典（dict）是一个键值对存储对象。
* 集合（set）是对象中唯一的无序集合对象。

-------------------------------------------------------

* tuple has only a few methods available to change.
* list is much more flexible than tuples.
* dict is a key-value store object.
* set is an unordered collection object of unique objects.


## 列表的一些有用功能（Some useful functions for list）
```python

l = [1, 2, 3.14, 'data'] #list
print (type(l))l.append ([4,  3])
print(l)l.extend (['delta' ,5 ,6] )   #add  a  list
print(l)l.insert(3, 'beta')  #insert  before  index 3
print(l)l.remove ('data')   #delete an elementprint(l)
```
```python
<class 'list'>    
[1, 2, 3.14, 'data', [4, 3]]    
[1, 2, 3.14, 'data', [4, 3], 'delta', 5, 6]    
[1, 2, 3.14, 'beta', 'data', [4, 3], 'delta', 5, 6]    
[1, 2, 3.14, 'beta', [4, 3], 'delta', 5, 6]    
```

## Python功能：参考对象（Python features: Refer for object）
* 在Python中，如果要将值从一个对象传递给另一个对象，则=(等号)将按地址传递值。
* 例如，
```python
x = [1, 2. 3, 4]
y = x
y[0] = 5
print(x)

x = [1, 2, 3, 4]
z  =  x.copy()
z[0] = 5
print (x)
输出将会是[5,2,3,4],[1,2,3,4]
```
--------------------------------------------------

* In Python if you want pass the value from one object to another, = will pass the value by address.
* For example,
  - x = [1, 2. 3, 4]  
  - y = x  - y[0] = 5  - print(x)
  - x = [1, 2, 3, 4]  - z  =  x.copy()  - z[0] = 5  - print (x)
  - The output will be [5,2,3,4],[1,2,3,4]


## 多维列表（Multidimensional  list）

* 我们可以创建一个包含多行的列表
```python
a  =  [[1,2 , 3 ,4],[1,2 ,3,4],[1,2 ,3]] 
print(a)
print(a[0][3])
```
* 但请注意：
  多维列表不是矩阵。 数学运算符可能会导致您不想看到的结果。 对于矩阵计算，我们将在明天花费大量的时间。

-------------------------

We can create a list with multi-rows like

a  =  [[1,2 , 3 ,4],[1,2 ,3,4],[1,2 ,3]]
print(a)
print(a[0][3])

But note:
Multidimensional list is not a matrix. Mathematical operators may lead to the results that you don't want to see. For matrix computations, we will spend a lot of time on it tomorrow.


## 条件语句（Conditions）
* 条件控制元素包括if，else和elif。
* 对于条件语句，我们有如下几种：

|Name|     Notation|
|----|:-----------:|
|larger|       >|
|smaller|        <|
|equal|      ==|
|larger or equal |     >=|
|sma

* 对于多条件同时使用的情况，我么使用and, or 或者 not作为关键字来相互衔接

## 示例和练习：条件语句 (Example & exercise: conditions)
```python
a = [24, 16, 54]
b = []
if  a[0]< a[1]  and a[0]< a[2] :
    b.append(a[0])
    if  a[1]  <  a[2]:
        b.append(a[1])
        b.append(a[2])
    else:                 
        b.append(a[2])
        b.append(a[1])   
# This piece of code is not done yet.  
# Please  complete  it !!!
```




## 循环语句 （Loops）
* 循环语句有很多不同的样式代码，我们只提供两个常用的语句。
```python
     for...in ... ：statement A
     是循环中最常用的语句，通常与range（start,end,step）一起使用,start为起始值，end为结束值，step为步长。 例如，                
     range(0,8,1)  给出[0，1，2，3，4，5，6，7]

2/                     
        while ...：statement A        
     将会执行A语句，直到满足while的条件。
```

-------

```python
There are many different style code for loops, We just present two common used statements.
  -     for _ in ... : statement A
    is the most common used statement for loops, ait is combined with range(starC end, step). For e.g.,
  - range(0, 8, 1) gives [0, 1, 2, 3, 4, 5, 6, 7]
while ... : statement A* will implement A until it satisfy the condition of while.
```

