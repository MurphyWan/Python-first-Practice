
# 《三天搞定Python基础》

### 注释：鉴于Jiang老师提供的原始课件是英文版本，对于英文不太好的同学来讲看起来比较慢，为了提高大家的学习效率，故我花点时间做个中文版。如果翻译的有不当之处，还请大家指正。谢谢！

## 作者：Yupeng Jiang
* 伦敦大学学院 数学系（英国顶尖大学，2018 QS世界大学排名中位列世界第7名，英国第3名）
* 2016年6月5日
* [课件来自] https://zhuanlan.zhihu.com/p/21332075

## 翻译：Murphy Wan


## 大纲（ Outline）

* 第1天：Python和科学编程介绍。 Python中的基础知识：
  - 数据类型
  - 控制结构
  - 功能
  - I/O文件
* 第2天：用Numpy，Scipy，Matplotlib和其他模块进行计算。 用Python解决一些数学问题。
* 第3天：时间序列：与Pandas统计和实际数据分析。 随机序列和蒙特卡罗。

------------------------------以下为英文原文-------------------------------------
* Day 1: Introduction to Python and scientific programming. Basics in Python: data type, contro structures, fu nctions,  l/O file.
* Day 2: Computation with Numpy, Scipy, Matplotlib and other modules. Solving some maths problems with
  Python.
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
* Python is open source, which means it is free.
* Python is a glue language.
  - Python makes your coding life easier.
  - Python is faster (on average) than some computing a pplications, like Matlab.
* Python has a large community of programmers. It comes
   with a large number of standard library and extended
  packages.
* Python is widely used in the industry (Google, NASA
   hedge funds, banks, etc.).

## 使用Python 2或3？
* Python 3不能向后兼容Python 2，这意味着Python 2中的某些软件包或库无法在Python 3中使用。
* 然而，许多机构仍在使用Python 2，因为仍然有几个软件包与Python 3不兼容。
* Python 2.x是历史遗留物，而现在，Python 3.x是该语言的未来。 2010年年中，2.7版本的2.7版本将不会再出现新的主要版本。
* 我们会遇到一些差异，但不会太多。
* 检查
https：//wiki.python.org/moin/Python2或Python3或其他在线资源获取更多信息

------------------------------以下为英文原文-------------------------------------

Python 2 or 3?
* Python 3 is not backward compatible with Python 2 which means some packages or libraries in Python 2 cannot work on Python 3.
* However, a large number of institutions are still using Python 2 since there is still several packages incompatible with Python 3.
* Python 2.x is legacy and the present, Python 3.x is the future of the language. The 2.x branch will see no new major releases after 2.7 in mid-2010.
* We will encounter some difFerences, but not much.
* Check
https : //wiki.python.org/moin/Python2 or Python3 or other online resources for more information

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


```python

```


```python

```
