# 《三天搞定Python基础概念之第一天》 Day 1
>#### 为【零基础】的人设计，带你串一遍Python的基本操作。若你已经get了Python的基础知识，请直接去第二天的内容 [(传送门-->第二天)](https://github.com/MurphyWan/Python-first-Practice/blob/master/D2_of_3Day_DoneWithPython.md)

```
前言：
首先，非常感谢Jiang老师将其分享出来！本课件非常经典！
经过笔者亲测，竟然确实只要三天，便可管中窥豹洞见Python及主要库的应用。实属难得诚意之作！
其次，只是鉴于Jiang老师提供的原始课件用英文写成，而我作为Python的爱好者计算机英文又不太熟练，讲义看起来比较慢。
为了提高自学课件的效率，故我花了点时间将其翻译成中文，以便将来自己快速复习用。
该版仅用于个人学习之用。
再次，译者因工作中需要用到数据分析、风险可视化与管理，因此学习python，翻译水平有限，请谅解。
在征得原作者Yupeng Jiang老师的同意后，现在我将中文版本分享给大家。

```

## 作者：Dr.Yupeng Jiang
* 伦敦大学学院 数学系  (全球顶尖大学，世界排名第7[《2018QS世界大学排名》](https://www.topuniversities.com/university-rankings/world-university-rankings/2018)，英国第3名)
* 2016年6月5日
* [原版课件来自] https://zhuanlan.zhihu.com/p/21332075
* [中文版的说明] https://zhuanlan.zhihu.com/p/29184240
## 翻译：[Murphy Wan](https://github.com/MurphyWan/Python-first-Practice/blob/master/README.md)
```python
```

## 大纲（ Outline）
* 第1天：Python和科学编程介绍。 Python中的基础知识：  - 数据类型  - 控制结构  - 功能  - I/O文件
* 第2天：用Numpy，Scipy，Matplotlib和其他模块进行计算。 用Python解决一些数学问题。
* 第3天：时间序列：用Pandas进行统计和实际数据分析。 随机和蒙特卡罗。

------------------------------以下为英文原文-------------------------------------

* Day 1: Introduction to Python and scientific programming. Basics in Python: data type, contro structures, fu nctions,  l/O file.
* Day 2: Computation with Numpy, Scipy, Matplotlib and other modules. Solving some maths problems with  Python.
* Day 3: Time series: statistics and real data analysis with Pandas. Stochastics and Monte Carlo.
```python
```

## 第一天的主要内容

* 为【零基础】的人设计，带你串一遍Python的基本操作。若你已经get了Python的基础知识，请直接去第二天的内容 [(传送门-->第二天)](http://www.jianshu.com/p/8551e878de39)

* Python的背景
* Python基础知识
* 控制结构
* 功能
* 读/写文件
* 实验部分

```python
```

> ## 为什么使用Python （ Why Python?）
* Python是开源的，这意味着它是免费的。
* Python是一种胶水语言：   
  - Python使你的编码更加轻松  
  - Python平均来讲，比一些语言计算更快，比如Matlab
* Python有一个很大的程序员社区。 它带来了与大量的标准库和扩展包。
* Python广泛应用于各种行业（Google，NASA，对冲基金，银行等）。


```python
```

## 使用Python 2或3？
* Python 3不能向后兼容Python 2，这意味着Python 2中的某些软件包或库无法在Python 3中使用。
* 然而，许多机构仍在使用Python 2，因为仍然有几个软件包与Python 3不兼容。
* Python 2.x是历史遗留物，而现在，Python 3.x是该语言的未来。 2010年年中，2.7版本的2.7版本将不会再出现新的主要版本。
* 我们会遇到一些差异，但不会太多。
* 检查https://wiki.python.org/moin/Python2 或Python3或其他在线资源获取更多信息


```python
```

## 一些在线资源 （Some online resources）
* http://openbookproject.net/thinkcs/python/english2e/ 通过前几章能获得基本思想。
* http://learnpythonthehardway.org/book/ 做练习。
* https://www.kevinsheppard.com/images/0/09/Python_introduction.pdf 强大的计量经济学重点。本说明的部分内容基于本文档。
* 对于一些特定的软件包，如Numpy和Pandas，最好的学习方法是使用他们的官方文档，并自己实现一些例子。
* 使用Google和一堆程序员相互切磋的Stack Overflow网站。


```python
```

## Python环境 （Python environment）

* 安装Python科学堆栈的推荐方法是使用Continuum Analytics Anaconda。
* Anaconda是一个免费的软件包管理器，环境管理器，以及开源软件包的集合。
* Anaconda包括核心Python解释器和标准库。
* https://www.continuum.io/downloads


```python
```

## Anaconda中包括的库（Libararies）
* NumPy（http://numpy.scipy.org ）：该库用于处理（大）数组。
* SciPy（http://www.scipy.org ）：该库包含许多有用的科学功能。
* Matplotlib（http://matplotlib.sourceforge.net ）：该库用于绘图。
* Pandas（http://pandas.sourceforge.net ）：该库有效并快速分析大数据集; 尤其针对金融时间序列。
* IPython（http://wprw.ipython.org ）：shell、或基于浏览器：开发环境。
* Spyder（http://pythonhosted.org/spyder/ ）：IDE交互式开发环境
```python
```

## 管理你的Anaconda
* 在你的终端或cmd，输入
 conda list
* 您可以看到已安装的软件包列表
* 更多的管理方法可以在这里找到：  http://conda.pydata.org/docs/using/pkgs.html

```python
```

## 你可以在本课程中学到什么？                                       
* 本课程是为初学者设计的。 它不需要任何以前的任何编程语言的知识。
* Python编程的基础知识。
* 使用Numpy，Scipy和Sympy进行数学计算。
* 使用Matplotlib库绘制图形。
* 与Pandas分析实际数据和时间序列。
* 学习如何使用它作为工具。
```python
```

## 今天的安排
* 早上：Python编程基础介绍。 在上午的会议中，您将需要做一些练习。 只是一些热身水平的问题，他们会给你一个关于Python编程的想法。
* 下午：半小时内完成介绍部分。 那么我们会有三个大问题要解决。 他们将是今天的一个很好的总结：讲座。 你将有一个小时独立工作。 然后，我将在过去半小时内提供分析和解决方案。




```python
```

## 练习1
* 安装Anaconda并更新它以便拥有   所有包的最新版本。 我们将使用Python 3.4（而不是以前的Python 2.7版本）。
* 通过键入以下命令启动Spyder并计算76：     
  
  x = 7 ** 6   打印（x）

* 启动IPython Notebook并计算7的6次方


```python
```


## 缩进（Indentation）
* 在某些语句之后，会加一个缩进; 缩进减少，则表示当前块结束。
* 例如
    x = 7 ** 6
    print（x）#witt. fron't  inden-tation
* 这段代码在Python中是错误的，虽然它在C ++，Matlab和许多其他代码或应用程序中是可以接受的。


```python
```

## 编程中的一些好习惯（Some good habit in programming）
* 在需要缩进和换行的地方使用这个功能；不要把你的脚本弄乱了。
* 不要使用没有意义的变量；要用可以被描述的变量。
* 写注释。 帮助别人和自己在以后理解你现在所写的代码内容。
* 不要同时开始学习多种编程语言。



```python
```

## 关于Python的基础知识（Basic knowlegde on Python）

```python
```

## 常用的数字数据类型（Common used numeric data types）
|Name|       Notation|  Declaration e.g.
|:--------|--------------:|:------------:|
|Integers|   int|       a = 10|
|Floating|   float|     b = 3.14|
|Complex|    complex|   c = 1 + 2j|
|String|     str|       d = 'Python'|

* 备注：   
- 在Python 2.7中，int与另一个int运算将导致int结果。 但是，一个浮点运算与int会导致浮点数。   
- 在Python 3.x中，int与另一个int运算将导致浮点数。

```python
```

## 算数运算符（Arithmetic operators）

|Name|Notation|Examples|
|----|:--------:|:--------:|
|Addition|+| a + b |
|Subtraction|-|c - b|
|Multiplication|*|x*y|
|Division|/|x/z|
|Modulus|%|x%a|
|Exponent|**|a**x|

```python
```

## 练习2（Exercise 2）
* 猜下面代码的结果。执行他们，看答案。
* Try to guess the results of the following code. Implement them and check your answers. 
- a = 10   # int 
- b = 3.14 # fLoat 
- c = 3    #int 
- d = a ** 2 # square of a 
- print (type (d))    # return the type of d  
- print (type (d/l0)) # return the type of d/l0 
- print (type (a/b))  # return the type of a/b 
- print (type (a/c))  # return the type of a/c 
- print (type (b*d))  # return the type of b*d

```python
```

## 浮点数的精度（Precision of float）
* 尝试在您的控制台中键入0.1 + 0.2。 你会发现这个值是  
- 0.30000000000000004

* 这是二进制浮点的本质。 您可以在支持硬件浮点运算的所有语言中看到同样的东西。
* 可以使用“round（）”功能控制显示精度，但也有上述情况，这意味着round(9.995,2)返回9.99而不是10，因为9.995的存储稍小于9.995。
* decimal Library将给出精确的存储值，请参见以下示例。



```python
```

## 例子（Example）
```python
import  decimal  
# import  the  libray  "decimal"    
# display  2  decimal  precision
print (round (3*1415 ,   2))   #  result  3. 14
print (round (9 .995 ,   2))   #  result  9. 99

#call   function   "Decimal "  from lib "decimal"
print (decimal.Decimal (9.995))
The last "print" returns
9.9949999999999992184029906638897955417633056640625,
which is exactly how 9.995 is stored in the hardware.
```

```python
```

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

```python
```

## Python功能：索引（Python features: Indexing）
* Python具有与C ++类似的索引规则，其起始索引为0。
* 当通过索引返回值时，间隔实际上是[，]样式，这意味着不包括终端索引。



```python
```

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



```python
```

## 列表的一些有用功能（Some useful functions for list）
```python

l = [1, 2, 3.14, 'data'] #list
print (type(l))l.append ([4,  3])
print(l)l.extend (['delta' ,5 ,6] )   #add  a  list
print(l)l.insert(3, 'beta')  #insert  before  index 3
print(l)l.remove ('data')   #delete an elementprint(l)
```
```python
<class 'list'>    
[1, 2, 3.14, 'data', [4, 3]]    
[1, 2, 3.14, 'data', [4, 3], 'delta', 5, 6]    
[1, 2, 3.14, 'beta', 'data', [4, 3], 'delta', 5, 6]    
[1, 2, 3.14, 'beta', [4, 3], 'delta', 5, 6]    
```

```python
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
z  =  x.copy()
z[0] = 5
print (x)
输出将会是[5,2,3,4],[1,2,3,4]
```


```python
```

## 多维列表（Multidimensional  list）

* 我们可以创建一个包含多行的列表
```python
a  =  [[1,2 , 3 ,4],[1,2 ,3,4],[1,2 ,3]] 
print(a)
print(a[0][3])
```
* 但请注意：
  多维列表不是矩阵。 数学运算符可能会导致您不想看到的结果。 对于矩阵计算，我们将在明天花费大量的时间。


```python
```

## 条件语句（Conditions）
* 条件控制元素包括if，else和elif。
* 对于条件语句，我们有如下几种：

|Name|     Notation|
|----|:-----------:|
|larger|       >|
|smaller|        <|
|equal|      ==|
|larger or equal |     >=|
|sma

* 对于多条件同时使用的情况，我么使用and, or 或者 not作为关键字来相互衔接

```python
```

## 示例和练习：条件语句 (Example & exercise: conditions)
```python
a = [24, 16, 54]
b = []
if  a[0]< a[1]  and a[0]< a[2] :
    b.append(a[0])
    if  a[1]  <  a[2]:
        b.append(a[1])
        b.append(a[2])
    else:                 
        b.append(a[2])
        b.append(a[1])   
# This piece of code is not done yet.  
# Please  complete  it !!!
```

```python
```

## 循环语句 （Loops）
* 循环语句有很多不同的样式代码，我们只提供两个常用的语句。
```python
     for...in ... ：statement A
     是循环中最常用的语句，通常与range（start,end,step）一起使用,start为起始值，end为结束值，step为步长。 例如，                
     range(0,8,1)  给出[0，1，2，3，4，5，6，7]

2/                     
        while ...：statement A        
     将会执行A语句，直到满足while的条件。
```


```python
```

## 举例：循环语言(Example: loops)     
```python
# for和range的例子 example  of  for  and  range  
# 初始值默认值为default start of range is O     
# 步长默认值为default step of range is 1     
for i in range(2, 10, 3):         
    print(i)         
    l= i**2         
    print(l)

# white to sum   up 1 to 100
a = 0
sumup = O
while  a < 100 :
    a + 1
    sumup += a
    print ( sumup)
```
```python
```
## break和continue. 

* 你可以在循环语句中使用关键字break，以跳出循环。(you can use the keyword break inside a loop to leave the loop..) 
* 你也可以在循环语句中使用关键字continue，以暂停当前循环执行后面的语句。(you can use the keyword continue inside a loop to stop pracessing the current iteration of the loop and immediately go on to the next round.)
* 举例 E.g.
```python
# search the first
# be divided by 17
for i in range(300, 351):
    if i % 17 == O:
        print (i)
        break
    else :
        cantinue
```
```python
```
## 循环语句嵌套（Loop inside the loop）
* 循环语句可以内嵌在另一个循环语句中(Loop can be written inside another loop)

```python
for  i  in range (10):
     print (i)     
     for j in range (5):
         print (j)
```
```python
```
## 练习(Exercises)
* 计算从1到1000的累计值。
* 计算从1到1000的偶数之和。

```python

```
## 功能 (Functions)


```python

```

## 功能(方法or函数)的声明 (Function declaration)
* 方法定义如下(Functions are defined as)
```python
def   TheNameOfFunction(paral, para2):
      ...      
      return Outcome
```
* 函数（方法）返回的输出结果会在函数被调用的地方出现。

```python
```
## 举例：求两个变量最大值的函数
```python
def  MaxOfTwo (x1, x2):
     if  x1 >= x2:
          return x1       
     else:
          return x2

a = l
b = 2
c = MaxOfTwo(a, b)
print(c)
```

```python
```

## 默认参数
* Python中的函数没有函数重载(function overloading)。 这意味着你不能有两个共享同名的功能。 但是操作符重载（operator overloading）是正常的。
* 您可以为函数的参数提供默认值，例如。

```python
   def MaxOfTwo(xl, x2 = 1): ...
```
* 请将您的默认参数放在一堆函数参数的末尾处。


```python
```
## 具有两个输出的函数（方法）
* 函数还可以返回两个或多个输出。 在这种情况下，你应该这样写出代码：

```python
def  f (x1, x2,  x3, ...):
     ......
     return(y1,  y2,  y3, ...)

a1,b1,c1 = f(...)
```




```python

```

## 读取/写入文件  (Reading/ writing files)

```python

```
## 内建open()方法  [Built-in open() function]
* 要打开一个文件，使用Python内建的open()函数。 open()方法返回一个文件对象，最常用的一般使用两个参数。

```python
file_object = open(filename, mode)
```

* 这个mode参数可以是（The mode can be）
  - 'r' 只读模式（when the file will only be read）
  - 'w' 只写模式（与一个现存文件文件同名，则被清除） 
  - 'a' 添加模式，即任意写入文件的数据都被自动添加到末尾
  - 'r+' 打开文件，可以读、写

```python

```

## 创建一个文件  (Creating new file)
```python
   file = open('newfile.txt', 'w')
   file.write('I am created for the course. \n')
   file.write('How about you? ')
   file.write('How is your exam?')
   file.close()
```


```python
```

## 读取一个文件 (Reading a file)



```python

file = open('newfile.txt', 'r')
#show whole efile
print(file.read())
#show first ten characterrs
print(file.read(10))
#view by line
print(file.readline())
#view all by line
print(file.readlines())
file.close()

```





```python

```

## 循环读取一个文件 (Looping over a file object)

```python

file = open('newfile.txt', 'r')
for  line  in  file:
     print (line)
file.close()

```


```python
输出将是
        我是为这个课程而诞生的
        你怎么样？你的考试如何

* ------以下是英文原文--------------------
Output would be:
          I am created for the course   
          How about you? How is your exam?


```



```python
```


## 增加一个文件 (Adding in a file)

```python
file = open（'newfile.txt', 'a')
file.write('\nI am back again. \n'）
file.write('Do  you miss me?\n')
file.clase()

```


```python
```

## with语句  (The with statement)

* 很容易忘记关闭{close()}文件。 由于这个和其他原因，最好使用with语句:

```python

with open(“humpty.txt”) as f：

```

* 这样可以确保文件正确关闭，即使读取时发生错误。




```python


```


## 文件路径  (File paths)

* 也可以使用绝对路径指定文件名。
* 示例（Mac / Linux）：

```python
open ('/etc/gimp/2.O/gtkrc')
```

* 示例（Windows）：

```python
open('C:\Users\user\Documents\file.txt')
```

* 请注意，反斜杠需要转义（写入两次'\\'）




```python


```


## 实验部分  (Lab Session)


```python


```

## 目标1  (Target 1)

* 您的老板要求您编写一段代码，以便对于具有float或int类型元素的任何长度列表(list)，您的函数可以将它们按照从大到小排序。

* 例如 如果你的老板给一个list

```python               
               [8, 2, 4, 6, 1, 9, 0, 3, 5, 7]

```

* 你的方法将返回

```python
               [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

```




```python


```


## 目标1提示： (Hint for Target 1:)     

* 有三种不同的排序算法：

  - 气泡排序：从最后开始，将最后两次的最大值传递给前一个索引。 你第一次遍历每一个数字，你通过最大的数字到一开始。 然后你在剩下的数字中重复一遍。
  - 选择排序：首先搜索整个列表。 并将最小的数字传递到列表的末尾。 然后搜索整个列表排除最后一个数字。 再重复该步骤。
  - 插入排序：从一开始，按顺序比较第一个数字和第二个数字，将第一个数字交换为最大数字。 然后重复它构成第二个直到结束。

-----以下为英文原文----- 

There are three different algorithms of sorting:
* Bubble sort: Starting from the end, pass the maximum of last two to the former index. The first time you traverse every number, you pass the largest number to the beginning. Then you repeat them in the rest numbers.
* Selectian sort: Search the whole list first. And pass the smallest number to the end af the list. Then search the whole list exclude the last number. Repeat it.
* Insert sort: Starting from the beginning, compare the first number and the rest sequentially to swap the first number to be the biggest. Then repeat it fram the second one until end


```python


```


## 目标2  (Target 2)

* 代码功能
  -  ![3days_img01.gif](http://upload-images.jianshu.io/upload_images/5522220-418ac8b18c09ac84.gif?imageMogr2/auto-orient/strip)

* 使用派生词的定义，对其数字导数函数进行编码。

* 找到数值解

  -  ![3days_img02.gif](http://upload-images.jianshu.io/upload_images/5522220-e771b389230d48a4.gif?imageMogr2/auto-orient/strip)

通过二等分法。

* 通过Newton-Raphson方法再次解决，该方法是“根搜索”的另一种数值方法。 它是由...给出的
  -  ![3days_img03.png](http://upload-images.jianshu.io/upload_images/5522220-c6312df5d2f9abe1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* https://www.codecogs.com/latex/eqneditor.php


```python


```


## 目标2的提示  (Hint for Target 2:)

* 衍生物可以近似于 
  
  -  ![3days_img04.gif](http://upload-images.jianshu.io/upload_images/5522220-b07449cf9570fccb.gif?imageMogr2/auto-orient/strip)
 -  ![3days_img05.gif](http://upload-images.jianshu.io/upload_images/5522220-cf4b06f5c8313550.gif?imageMogr2/auto-orient/strip)


 -  ![3days_img06.gif](http://upload-images.jianshu.io/upload_images/5522220-45115ef5f9311b20.gif?imageMogr2/auto-orient/strip)



* 二分法实现如下：
  - 给出间隔[a，b]，使得f（a）和f（b）具有不同的符号。
  - 计算中点c = 0.5 （a + b）和中点f（c）的函数值。
  - 如果f（x）足够，则停止。 否则，将（a，f（a））或（b，f（b））替换为（c，f（c）），以便在新间隔内存在过零点

-----以下为英文原文----- 

* The derivative can be appraximated by
  - f'(x) ≈ [f(x + h) - f (x)]/h,              
  - f'(x) ≈ [f(x + h) - f(x - h)]/h,
  - f'(x) ≈ [f(x+h) - f (x-h)]/2h                 

* Bisection is implemented as:
  - Give an interval [a, b] such that f(a) and f(b) have different sign.
  - Calculate the midpoint c= 0.5 * (a + b) and the functian value at the midpoint, f(c).
  - If f(x) is goad enough, stop. Otherwise replace either (a, f(a)) or (b, f(b) with (c, f(c)) so that there is a zero crossing within the new interval


```python


```


## 目标3  (Target 3)

* 在面试时 ，你的面试官者要求你编写一个可以给他第n个斐波纳契数字的函数，其中n由你的面试官决定。


-----

* In your interview. your interviewer ask yau to code a function that could give him the n-th Fibonacci number, where n is determined by your interviewer.



```python


```


## 目标3提示：  (Hint for Target 3:)

* 斐波那契序列如下

    -  ![3days_img07.gif](http://upload-images.jianshu.io/upload_images/5522220-bec05cbc2b8384cb.gif?imageMogr2/auto-orient/strip)

   -  ![3days_img08.gif](http://upload-images.jianshu.io/upload_images/5522220-6d9674a5a8cfb297.gif?imageMogr2/auto-orient/strip) 




* 其中一个方法是递归地使用一个函数。

* 其中一个方法是利用append（）函数。

-----以下为英文原文----- 

* Fibonacci sequence is given like
  
  ao = 1, a1 = 1,
  
  an = an-1 + an-2 for n> 2

* One of the method is to recursively use a function.* One of the method is to take advantage from append() function.





```python

第一天的课程到此结束，辛苦了

```

[传送门-->第二天(Day2)](https://github.com/MurphyWan/Python-first-Practice/blob/master/D2_of_3Day_DoneWithPython.md)

