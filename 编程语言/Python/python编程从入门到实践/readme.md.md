# 1. 起步

在本章中，你将运行自己的第一个程序——hello_world.py。为此，你首先需要**检查自己的计算机是否安装了较新版本的 Python**；如果没有，就要安装它。你还要安装一个**文本编辑器**，用于**编写和运行 Python 程序**。你输入 Python 代码时，这个文本编辑器能够**识别它们并突出显示不同的部分**，让你能够轻松地了解代码的结构。

1. 大致了解 Python，并在自己的系统中**安装 Python**；
2. 安装一个**文本编辑器**，以简化 Python 代码的编写工作；
3. 如何**在终端会话中运行 Python 代码片段**，并运行第一个程序—hello_world.py；
4. 如何解决安装问题。

## 1.1 搭建编程环境

### 1.1.2 运行 Python 代码片段

Python 自带一个在**终端窗口**中运行的**解释器**，让你无需保存并运行整个程序就能尝试运行 Python 代码片段。

代码片段：
```python
>>> print("Hello Python interpreter!")
Hello Python interpreter!
```
提示符 `>>>` 表明正在使用**终端窗口**，而加粗的文本表示需要你**输入**之后按**回车键**来执行的代码。只要代码清单中包含**三个右尖括号**，就意味着代码是在**终端会话**中执行的，而输出也是来自**终端会话**的。

## 1.2 在不同操作系统中搭建 Python 编程

### 1.2.1 在 Windows 系统中搭建 Python 编程环境

1. 安装 Python<br>
    首先，检查你的系统是否安装了 Python。为此，在“**开始**”菜单中输入 **command (cmd)** 并按**回车**以打开一个**命令窗口**；也可以按住 **Shift 键**并**右击桌面**，选择“**在此处打开命令窗口**”。 在终端窗口中输入 **python** （全部小写）并**按回车**：如果出现了 Python 提示符（`>>>`），就说明系统安装了 Python；如果出现了一条错误消息，指出 python 是无法识别的命令，就说明没有安装 Python。

2. 在终端会话中运行 Python<br>
    打开一个**命令窗口**，并在其中执行命令 `python`。每当要运行 Python 代码片段时，都请打开一个命令窗口并启动 **Python 终端会话**。要关闭该终端会话，可按 **Ctrl+Z**、再按**回车键**，也可执行命令 `exit()`。

### 1.2.3 在 Linux 系统中搭建 Python 编程环境

<mark>Linux 系统是为编程而设计的</mark>，因此大多数 Linux 计算机默认安装了 Python。编写和维护 Linux 的人认为，你很可能会使用这种系统进行编程，他们也鼓励你这样做。因此，要在这种系统中编程，你几乎不用安装什么软件，只需要修改一些设置。

## 1.3 运行 Hello Word 程序

### 1.3.2 运行程序 hello_world.py

编写第一个程序前，在系统中创建一个名为 **python_work** 的文件夹，用于存储你开发的项目。文件名和文件夹名称最好使用**小写字母**，并使用**下划线**代替空格，因为 python 采用了这些命名约定。

## 1.4 解决安装问题

如果无法运行程序，可尝试如下几个解决方法，这些通用方法适用于所有编程问题：
- 程序存在严重错误时，Python 将显示 **traceback**，即**错误报告**。
- 语法在编程中非常重要，即便是**少一个冒号**、**引号不匹配**或**括号不匹配**，都可能导致程序无法正确运行。

## 1.5 从终端运行 Python 程序

你编写的大多数程序将直接在文本编辑器中运行，但有时候**从终端运行程序**很有用。例如，你可能想直接运行既有的程序。

### 1.5.1 在 Windows 系统中从终端运行 Python 程序

在命令窗口中，可以使用终端命令 **cd**（表示 **change directory**，即**切换目录**）在文件系统中导航。使用命令 **dir**（表示 **directory**，即**目录**）可以显示当前目录中的所有文件。最后使用命令 `python hello world.py` 来运行这个文件。

大多数程序可直接**从编辑器运行**，但待解决的问题比较复杂时，你编写的程序可能需要**从终端运行**。

# 2. 变量和简单数据类型

在本章中，你将学习**可在 Python 程序中使用的各种数据**，还将学习**如何在程序中使用变量来表示这些数据**。

1. 如何**使用变量**；
2. 如何**创建描述性变量名**以及如何**消除名称错误和语法错误**；
3. **字符串**是什么，以及如何**使用小写、大写和首字母大写方式显示字符串**；
4. 使用**空白**来显示整洁的输出，以及如何**剔除字符串中多余的空白**；
5. 如何使用**整数**和**浮点数**；
6. 一些使用**数值数据**的方式；
7. 如何**编写说明性注释**，让代码对你和其他人来说更容易理解；
8. 让代码尽可能简单的理念。

## 2.2 变量

```python
message = "Hello Python world!"
print(message)

Output:
Hello Python world!
```

我们添加了一个名为 `message` 的**变量**。每个变量都指向一个值——与该变量相关联的信息。在这里，指向的值为文本 `"Hello Python world!"`。

添加变量导致 Python 解释器需要做更多的工作。处理第一行代码时，它将变量 `message` 与文本 `"Hello Python world!"` 关联起来；处理第二行代码时，它将与变量 `message` 关联的值打印到屏幕。
```python
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

Output:
Hello Python world!
Hello Python Crash Course world!
```
<mark>在程序中可随时修改变量的值，而 Python 将始终记录变量的最新值。</mark>

### 2.2.1 变量的命名和使用

在 Python 中使用变量时，需要遵守一些**规则和指南**。违反这些规则将引发错误，而指南旨在让你编写的代码更容易阅读和理解。

- <mark>变量名只能包含字母、数字和下划线</mark>。<mark>变量名能以字母或下划线打头，但不能以数字打头</mark>。例如，可将变量命名为 `message_1`，但不能将其命名为 `1_message`。
- <mark>变量名不能包含空格，但能使用下划线来分隔其中的单词</mark>。例如，变量名 `greeting_message` 可行，但变量名 `greeting message` 会引发错误。
- <mark>不能将 Python 关键字和函数名用作变量名，即不要使用 Python 保留用于特殊用途的单词</mark>，如 `print`。
- <mark>变量名应既简短又具有描述性</mark>。例如，`name` 比 `n` 好，`student_name` 比 `s_n` 好，`name_length` 比 `length_of_persons_name` 好。
- <mark>慎用小写字母 l 和大写字母 O，因为它们可能被人错看成数字 1 和 0</mark>。

> 注意：就目前而言，应使用小写的 Python 变量名。虽然在变量名中使用大写字母不会导致错误，但是大写字母在变量名中有特殊含义。

### 2.2.2 使用变量名时应避免命名错误

程序存在错误时，**Python 解释器**将竭尽所能地帮助你找到问题所在。程序无法成功运行时，解释器将提供一个 **traceback**。traceback 是一条记录，指出了解释器尝试运行代码时，在什么地方陷入了困境。

**名称错误**通常意味着两种情况：要么是使用变量前忘记给它赋值，要么是输入变量名时拼写不正确。

Python 解释器不会对代码做拼写检查，但要求**变量名的拼写一致**。

编程语言要求严格，但并不关心拼写是否正确。因此，创建变量名和编写代码时，无需考虑英语中的拼写和语法规则。

### 2.2.3 变量是标签

**变量**的定义：<mark>变量是可以赋给值的标签，也可以说变量指向特定的值</mark>。

## 2.3 字符串

**字符串**就是一系列字符。在 Python 中，用引号括起来的都是字符串，其中引号可以是**单引号**，也可以是**双引号**，如下所示：
```python
"This is a string."
'This is also a string.'
```

这种灵活性让你能够在字符串中包含**引号**和**撇号**：
```python
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
```

### 2.3.1 使用方法修改字符串的大小写

对于字符串，可执行的最简单的操作之一是**修改其中单词的大小写**。
```python
name = "ada lovelace"
print(name.title())

Output:
Ada Lovelace
```

在这个示例中，变量 `name` 指向小写的字符串 `"ada lovelace"`。在函数调用 print() 中，方法 `title()` 出现在这个变量的后面。**方法**是 Python 可对数据执行的操作。在 `name.title()` 中，`name` 后面的句点（`.`）让 Python 对变量 `name` 执行方法 `title()` 指定的操作。每个方法后面都跟着一对**圆括号**，这是因为**方法通常需要额外的信息来完成其工作**。这种信息是在圆括号内提供的。函数 title() 不需要额外的信息，因此它后面的圆括号是空的。

**方法** `title()` **以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写**。这很有用，因为你经常需要将名字视为信息。例如，你可能希望程序将值 Ada、ADA 和 ada 视为同一个名字，并将它们都显示为 Ada。

还有其它几个很有用的大小写处理方法。例如，要**将字符串改为全部大写**或**全部小写**，可以像下面这样做：
```python
name = "ada lovelace"
print(name.upper())
print(name.lower())

Output:
ADA LOVELACE
ada lovelace
```

存储数据时，方法 `lower()` 很有用。很多时候，你无法依靠用户来提供正确的大小写，因此需要将字符串先转换为小写，再存储它们。以后需要显示这些信息时，再其转换为最合适的大小写方式。

### 2.3.2 在字符串中使用变量

在某些情况下，你可能想**在字符串中使用变量的值**。
```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

Output:
ada lovelace
```

要在字符串中插入变量的值，可以在前引号前加上字母 `f`，再将要插入的变量放在**花括号**内。

这种字符串名为 **f 字符串**。`f` 是 format（设置格式）的简写，因为 **Python 通过把花括号内的变量替换为其值来设置字符串的格式**。

使用 `f` 字符串可完成很多任务，如利用与变量关联的信息来创建完整的消息，如下所示：
```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

Output:
Hello, Ada Lovelace!
```

还可以**使用 f 字符串来创建消息，再把整条消息赋给变量**：
```python
first_name = "ada"
last_name = "lovelace"
message = f"Hello, {full_name.title()}!"
print(message)

Output:
Hello, Ada Lovelace!
```

### 2.3.3 使用制表符或换行符来添加空白

在编程中，**空白**泛指任何**非打印字符**，如**空格**、**制表符**和**换行符**。

要在字符串中添加**制表符**，可使用字符组合 `\t` ：
```python
print("Python")
print("\tPython")

Output:
Python
        Python
```

要在字符串中添加**换行符**，可使用字符组合 `\n`：
```python
print("Language:\nPython\nC\nJavascript")

Output:
Language:
Python
C
Javascript
```

还可在同一个字符串中同时包含**制表符**和**换行符**。字符串 `"\n\t"` 让 Python 换到下一行，并在下一行开头添加一个制表符。
```python
print("Language:\n\tPython\n\tC\n\tJavascript")

Output:
Language:
        Python
        C
        Javascript
```

### 2.3.4 删除空白

`'python'` 和 `'python '` 对于程序来说是两个不同的字符串。Python 能够发现 `'python '` 中额外的空白，并认为它意义重大。

<mark>空白很重要，因为你经常需要比较两个字符串是否相同</mark>。一个重要的示例是，在用户登录网站时检查其用户名。

**Python 能够找出字符串开头和末尾多余的空白**。要**确保字符串末尾没有空白**，可使用方法 `rstrip()`。
```python
>>> favorite_language = 'python '
>>> favorite_language
'python '
>>> favorite_language.rstrip()
'python'
>>> favorite_language
'python '
```

在终端会话中项 Python 询问 `favorite_language` 的值时，可看到末尾的空格。对这个变量调用方法 `rstrip()` 后，这个多余的空格被删除了。然而，这种删除只是**暂时的**，接下来再次询问 `favorite_language` 的值时，你会发现这个字符串与输入时一样，依然包含多余的空白。

**要永久删除这个字符串中的空白，必须将删除操作的结果关联到变量**：
```python
>>> favorite_language = 'python '
>>> favorite_language = favorite_language.rstrip()
>>> favorite_language
'python'
```

你还可以**剔除字符串开头的空白**，或者**同时剔除字符串两端的空白**。为此，可分别使用方法 `lstrip()` 和 `strip()`：
```python
>>> favorite_language = ' python '
>>> favorite_language.rstrip()
' python'
>>> favorite_language.lstrip()
'python '
>>> favorite_language.strip()
'python'
```

在实际程序中，这些剔除函数最常用于在存储用户输入前对其进行清理。

### 2.3.5 使用字符串时避免语法错误

**语法错误**是一种你时不时会遇到的错误。程序中包含**非法的 Python 代码**时，就会导致语法错误。**例如在用单引号括起的字符串中，如果包含撇号，就将导致错误**。这是因为这会导致 Python 将第一个单引号和撇号之间的内容视为一个字符串，进而将余下的文本视为 Python 代码，从而引发错误。语法错误也是最不具体的错误类型，因此可能难以找出并修复。 

## 2.4 数字和下划线

在编程中，经常使用**数**来**记录得分**、**表示可视化数据**、**存储 Web 应用信息**，等等。Python 能根据数的用法以不同的方式处理它们。

### 2.4.1 整数

在 Python 中，可对整数执行**加**（`+`）**减**（`-`）**乘**（`*`）**除**（`/`）运算。

```python
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5
```

在终端会话中，Python 直接返回运算结果。**Python 使用两个乘号表示乘方运算**：

```python
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000
```

Python 还支持**运算次序**，因此**可在同一个表达式中使用多种运算**，还**可以使用圆括号来修改运算次序**，让 Python 按你指定的次序执行运算，如下所示：

```python
>>> 2 + 3 * 4
14
>>> (2 + 3) * 4
20
```

在这些示例中，**空格不影响 Python 计算表达式的方式**，它们的存在旨在让你在阅读代码时能迅速确定先执行哪些运算。

### 2.4.2 浮点数

Python 将所有带小数点的数称为**浮点数**。小数点可出现在数的任何位置。

从很大程度上说，使用浮点数时无须考虑其行为。你只需输入要使用的数，Python 通常会按你期望的方式处理它们：
```python
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
```

但需要注意的是，结果包含的小数位数可能是不确定的：
```python
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
```

所有语言都存在这种问题，没有什么可担心的。Python 会尽力找到一种精确表示结果的方法，但鉴于计算机内部表示数的方式，这在有些情况下很难。就现在而言，暂时忽略多余的小数位数即可。

### 2.4.3 整数和浮点数

**将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除**：
```python
>>> 4 / 2
2.0
```

**在其它任何运算中，如果一个操作数是整数，另一个操作数是浮点数，结果也总是浮点数**：
```python
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0
```

<mark>无论是哪种运算，只要有操作数是浮点数，Python 默认得到的总是浮点数，即便结果原本为整数也是如此</mark>。

### 2.4.4 数中的下划线

**书写很大的数时，可使用下划线将其中的数字分组，使其更清晰易读**：
```python
>>> universe_age = 14_000_000_000
>>> print(universe_age)
14000000000
```

**当你打印这种使用下划线定义的数时，Python 不会打印其中的下划线**。

这是因为存储这种数时，Python 会忽略其中的下划线。**将数字分组时，即便不是将每三位分成一组，也不会影响最终的值**。在 Python 看来，1000 与 1_000 没什么不同，1_000 与 10_00 也没什么不同。这种表示法适用于**整数**和**浮点数**，但只有 Python 3.6 和更高的版本支持。

### 2.4.5 同时给多个变量赋值

**可在一行代码中给多个变量赋值，这有助于缩短程序并提高可读性。这种做法最常用于将一系列数赋给一组变量**。

例如，下面演示了如何将变量 `x`、`y` 和 `z` 都初始化为零：
```python
>>> x, y, z = 0, 0, 0
```

这样做时，需要用**逗号将变量名分开**，对于要赋给变量的值，也需同样处理。**Python 将按顺序将每个值赋给对应的变量**。只要变量和值的个数相同，Python 就能正确地将它们关联起来。

### 2.4.6 常量

**常量**类似于变量，但其值在程序的整个生命周期内保持不变。**Python 没有内置的常量类型**，但 Python 程序员会使用**全大写**来指出应**将某个变量视为常量**，其值应始终不变。
```python
>>> MAX_CONNECTIONS = 5000
```

<mark>在代码中，要指出应将特定的变量视为常量，可将其字母全部大写</mark>。

## 2.5 注释

**注释**让你能够使用自然语言在程序中**添加说明**。

### 2.5.1 如何编写注释

在 Python 中，注释用**井号**（`hcq`）标识。井号后面的内容都会被 Python 解释器忽略，如下所示：
```python
hcq 向大家问好。
print("Hello Python people!")

Output:
Hello Python people!
```
Python 解释器将忽略第一行，只执行第二行。

### 2.5.2 该编写什么样的注释

<mark>编写注释的主要目的是阐述代码要做什么，以及是如何做的</mark>。

## 2.6 Python 之禅

经验丰富的程序员倡导尽可能**避繁就简**。Python 社区的理念都包含在 Tim Peters 撰写的“**Python 之禅**”中。要获悉这些有关编写优秀 Python 代码的指导原则，只需再解释器中执行命令 `import this`。

1. Beautiful is better than ugly.
2. Simple is better than complex.
3. Complex is better than complicated.
4. Readability counts.
5. There should be one-- and preferably only one --obvious way to do it.
6. Now is better than never.

不要企图编写完美无缺的代码，而是要**先编写行之有效的代码**，再决定是对其**做进一步改进**，还是转而去**编写新代码**。

# 3. 列表简介

在本章和下一章中，你将学习**列表是什么**以及**如何使用列表元素**。**列表**让你能够在一个地方**存储成组的信息**，其中可以只包含几个元素，也可以包含数百万个元素。

1. **列表是什么**以及**如何使用其中的元素**；
2. 如何**定义列表**以及如何**增删元素**；
3. 如何**对列表进行永久性排序**，以及如何为展示列表而进行**临时排序**；
4. 如何**确定列表的长度**，以及在使用列表时如何**避免索引错误**。

## 3.1 列表是什么

**列表由一系列按特定顺序排列的元素组成**。你可以创建只包含字母表中**所有字母**、**数字 0 ~ 9** 或**所有家庭成员姓名**的列表；也可以将任何东西加入列表中，**其中的元素之间可以没有任何关系**。列表通常包含多个元素，因此给列表指定一个表示**复数的名称**（如 letters、digits 或 names）是个不错的注意。

在 Python 中，用**方括号**（`[]`）表示列表，并用**逗号分隔**其中的元素。
```Python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

Output:
['trek', 'cannondale', 'redline', 'specialized']
```
如果让 Python 将列表打印出来，Python 将打印列表的内部表示，包括**方括号**。

### 3.1.1 访问列表元素

**列表**是**有序集合**，因此要访问列表的任意元素，只要将该元素的位置（**索引**）告诉 Python 即可。要访问列表元素，可指出列表的名称，再指出列表的索引，并将后者放在方括号内。

当你请求**获取列表元素**时，Python 只返回该元素，而不包括方括号：
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())

Output:
trek
Trek
```

### 3.1.2 索引从 0 而不是 1 开始

在 Python 中，**第一个列表元素的索引**为 `0`，而不是 `1`。大多数编程语言是如此规定的，这与**列表操作的底层实现**相关。

第二个列表元素的索引为 1。根据这种简单的计数方式，**要访问列表的任何元素**，都可将其位置减 `1`，并将结果作为索引。
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

Output:
cannondale
specialized
```

Python 为**访问最后一个列表元素**提供了一种特殊语法。通过将索引指定为 `-1`，可让 Python 返回最后一个列表元素：
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

Output:
specialized
```

这种语法很有用，因为你经常需要在不知道列表长度的情况下访问最后的元素。这种约定也适用于其他**负数索引**。例如，索引 -2 返回倒数第二个列表元素，索引 -3 返回倒数第三个列表元素，以此类推。

### 3.1.3 使用列表中的各个值

你可以像使用其它变量一样使用列表中的各个值。例如，可以使用 **f 字符串**根据列表中的值创建消息。
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

Output:
My first bicycle was a Trek.
```

## 3.2 修改、添加和删除元素

你创建的大多数列表将是**动态的**，这意味着列表创建后，将随着程序的运行**增删元素**。

### 3.2.1 修改列表元素

要**修改列表元素**，可指定**列表名**和要修改的**元素的索引**，再指定**该元素的新值**。
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

Output:
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```

### 3.2.2 在列表中添加元素

#### 1. 在列表末尾添加元素

**在列表中添加新元素**时，最简单的方式使将元素**附加**（append）到列表。**给列表附加元素**时，它将添加到列表末尾。
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

Output:
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
```

方法 `append()` 让动态地创建列表易如反掌。例如，你可以先创建一个空列表，再使用一系列函数调用 `append()` 来添加元素。
```python
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

Output:
['honda', 'yamaha', 'suzuki']
```

#### 2. 在列表中插入元素

使用方法 `insert()` 可在列表的任何位置**添加新元素**。为此，你需要指定新元素的**索引**和**值**。

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

Output:
['ducati', 'honda', 'yamaha', 'suzuki']
```

### 3.2.3 从列表中删除元素

你经常需要**从列表中删除一个或多个元素**。你可以根据**位置**或**值**来删除列表中的元素。

#### 1. 使用 `del` 语句删除元素

如果知道要删除的元素在列表中的位置，可使用 `del` 语句。
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

Output:
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']
```
<mark>使用 `del` 语句可删除任意位置处的列表元素，条件是知道其索引</mark>。

#### 2. 使用方法 `pop()` 删除元素

有时候，你要将元素从列表中删除，并接着使用它的值。

**方法 `pop()` 删除列表末尾的元素，并让你能够接着使用它**。术语**弹出**（pop）源自这样的类比：<mark>列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素</mark>。
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

Output:
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki
```
输出表明，列表末尾的值 `'suzuki'` 已经删除，它现在被赋给了变量 `popped_motorcycle`。

#### 3. 弹出列表中任何位置处的元素

实际上，可以使用 `pop()` 来**删除列表中任意位置的元素**，只需要**在圆括号中指定要删除元素的索引**即可。

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

Output:
The first motorcycle I owned was a Honda.
```
<mark>别忘了，每当你使用 `pop()` 时，被弹出的元素就不再在列表中了</mark>。

如果你不确定该使用 `del` 语句还是 `pop()` 方法，下面是一个简单的判断标准：<mark>如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用 `del` 语句；如果你要在删除元素后还能继续使用它，就使用方法 `pop()`</mark>。

#### 4. 根据值删除元素

有时候，你不知道要从列表中删除的值所处的位置。如果**只知道要删除的元素的值**，可使用方法 `remove()`。
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

Output:
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']

A Ducati is too expensive for me.
```

> 注意：方法 `remove()` 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都删除。

## 3.3 组织列表

### 3.3.1 使用方法 `sort()` 对列表永久排序

Python 方法 `sort()` 让你能够较为轻松地**对列表进行排序**。假设你有一个汽车列表，并要让其中的汽车**按字母顺序排序**。
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

Output:
['audi', 'bmw', 'subaru', 'toyota']
```
<mark>方法 `sort()` 永久性地修改列表元素的排列顺序</mark>。现在，汽车是**按字母顺序排列的**，再也**无法恢复**到原来的排列顺序。

**还可按与字母顺序相反的顺序排列列表元素**，只需向 `sort()` 方法**传递参数** `reverse=True` 即可。
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

Output:
['toyota', 'subaru', 'bmw', 'audi']
```
同样，对列表元素的排列顺序的修改是**永久性的**。

### 3.3.2 使用函数 `sorted()` 对列表临时排序

要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用**函数** `sorted()`。函数 `sorted()` 让你**能够按特定顺序显示列表元素**，同时**不影响它们在列表中的原始排列顺序**。

> 注意**函数**和**方法**的区别。
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

Output:
Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']

Here is the sorted list:
['audi', 'bmw', 'subaru', 'toyota']

Here is the original list again:
['bmw', 'audi', 'toyota', 'subaru']
```

注意，调用函数 `sorted()` 后，列表元素的排列顺序并没有变。如果要按与字母顺序相反的顺序显示列表，也可向函数 `sorted()` 传递参数 `reverse=True`。

>注意，并非所有的值都是小写时，按字母顺序排列列表要复杂些。决定排列顺序时，有多种解读大写字母的方式。然而，大多数排序方式是以本节介绍的知识为基础的。

### 3.3.3 倒着打印列表

要**反转列表元素的排列顺序**，可使用**方法** `reverse()`。
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

Output:
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
```
<mark>注意，`reverse()` 不是按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序</mark>。

<mark>方法 `reverse()` 永久性地修改列表元素的排列顺序，但可以随时恢复到原来的排列顺序，只需对列表再次调用 `reverse()` 即可</mark>。

### 3.3.4 确定列表的长度

使用**函数** `len()` 可快速**获悉列表的长度**。
```python
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4
```
> 注意：Python 计算列表元素数时从 1 开始，因此确定列表长度时，你应该不会遇到差一错误。

## 3.4 使用列表时避免索引错误

假设你有一个包含三个元素的列表，却要求获取第四个元素，这将导致**索引错误**。

**索引错误**意味着 Python 在指定索引处找不到元素。程序发生索引错误时，请尝**试将指定的索引减 1**，然后再次运行程序，看看结果是否正确。

别忘了，每当需要**访问最后一个列表**时，都可使用索引 `-1`。仅当列表为空时，这种访问最后一个元素的方式才会导致错误。

> 注意：发生索引错误却找不到解决办法时，请尝试将列表或其长度打印出来。列表可能与你以为的截然不同，在程序对其进行了动态处理时尤其如此。通过查看列表或其包含的元素数，可帮助你找出这种逻辑错误。

# 4. 操作列表

在本章中，你将学习如何**遍历整个列表**，这只需要几行代码，无论列表有多长。**循环让你能够对列表的每个元素都采取一个或一系列相同的措施**，从而高效地处理任何长度的列表，包括包含数千乃至数百万个元素的列表。

1. 如何**高效地处理列表中的元素**；
2. 如何**使用 `for` 循环遍历列表**，Python 如何根据**缩进**来确定程序的结构，以及如何避免一些常见的缩进错误；
3. 如何**创建简单的数字列表**，以及**可对数字列表执行的一些操作**；
4. 如何**通过切片来使用列表的一部分和复制列表**；
5. **元组**（它对不应变化的值提供了一定程度的保护），以及在代码变得越来越复杂时如何**设置格式**，使其易于阅读。

## 4.1 遍历整个列表

你经常需要遍历列表的所有元素，对每个元素执行相同的操作。**需要对列表中的每个元素都执行相同的操作时**，可使用 Python 中的 `for` 循环。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

Output:
alice
david
carolina
```
`for` 循环让 Python 从列表 magicians 中取出一个名字，并将其与变量 magician 相关联。

### 4.1.1 深入研究循环

<mark>对列表中的每个元素，都将执行循环指定的步骤，而不管列表包含多少个元素</mark>。

编写 for 循环时，可以给依次与列表中每个值相关联的临时变量**指定任意名称**。然而，选择描述单个列表元素的有意义名称大有裨益。例如：
```python
for cat in cats:
for dog in dogs:
for item in list_of_items:
```
这些命名约定有助于你明白 for 循环中将对每个元素执行的操作。使用**单数和复数式名称**，可帮助你判断代码段处理的是单个列表元素还是整个列表。

### 4.1.2 在 `for` 循环中执行更多的操作

在 `for` 循环中，**可对每个元素执行任何操作**。
```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

Output:
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

```
在代码行 `for magician in magicians:` 后面，<mark>每个缩进的代码行都是循环的一部分</mark>，将针对列表中的每个值都执行一次。

<mark>在 for 循环中，想包含多少行代码都可以</mark>。

### 4.1.3 在 `for` 循环结束后执行一些操作

for 循环结束后怎么办？<mark>通常，你需要提供总结性输出或接着执行程序必须完成的其他任务</mark>。

<mark>在 for 循环后面，没有缩进的代码都只执行一次，不会重复执行</mark>。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

Output:
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you, everyone. That was a great magic show!
```

## 4.2 避免缩进错误

Python 根据**缩进**来判断代码行与前一个代码行的关系。Python 通过使用缩进让代码**更易读**。简单地说，它要求你使用缩进让**代码整洁而结构清晰**。在较长的 Python 程序中，你将看到缩进程度各不相同的代码块，从而对**程序的组织结构**有大致的认识。

### 4.2.1 忘记缩进

<mark>对于位于 for 语句后面且属于循环组成部分的代码行，一定要缩进</mark>。

### 4.2.2 忘记缩进额外的代码块

**逻辑错误**。

### 4.2.3 不必要的缩进

为避免意外缩进错误，请只缩进需要缩进的代码。

### 4.2.4 循环后不必要的缩进

在有些情况下，这可能导致 Python 报告**语法错误**，但在大多数情况下，这只会导致**逻辑错误**。

### 4.2.5 遗漏了冒号

<mark>for 语句末尾的冒号告诉 Python，下一行是循环的第一行</mark>。

<mark>这种错误虽然易于消除，但并不那么容易发现。程序员为找出这样的单字符错误，花费的时间多得令人惊讶。此类错误之所以难以发现，是因为通常在人们的意料之外</mark>。

## 4.3 创建数值列表

**列表非常适合用于存储数字集合**，而 Python 提供了很多工具，可帮助你高效地处理数字列表。

### 4.3.1 使用函数 `range()`

Python 函数 `range()` 让你能够轻松地生成一系列数。
```python
for value in range(1, 5):
    print(value)

Output:
1
2
3
4
```
在这个示例中，`range()` 只打印数 1~4。这是编程语言中常见的**差一**行为的结果。<mark>函数 `range()` 让 Python 从指定的第一个值开始数，并在到达你指定的第二个值时停止。因为它在第二个值出停止，所以输出不包含该值（这里为 5）</mark>。

调用函数 `range()` 时，也可只指定一个参数，这样它**将从 0 开始**，例如，`range(6)` 返回数 0~5.

### 4.3.2 使用 `range()` 创建数字列表

要创建**数字列表**，可使用函数 `list()` 将 `range()` 的结果直接转换为列表。如果**将 `range()` 作为 `list()` 的参数**，输出将是一个数字列表。

```python
numbers = list(range(6))
print(numbers)

Output:
[0, 1, 2, 3, 4, 5]
```
使用函数 `range()` 时，还可指定**步长**。为此，可给这个函数指定**第三个参数**，Python 将根据这个步长来生成数。
```python
even_numbers = list(range(2, 11, 2))
print(even_numbers)

Output:
[2, 4, 6, 8, 10]
```
使用函数 `range()` 几乎能够创建任何需要的**数集**。例如，如何创建一个列表，其中包含前 10 个整数（1~10）的平方呢？<mark>在 Python 中，用两个星号（`**`）表示乘方运算</mark>。
```python
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

Output:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
为了让代码更简洁，可不使用临时变量 `square`，而**直接将每个计算得到的值附加到列表的末尾**：
```python
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)
```
<mark>有时候，使用临时变量会让代码更易读；而在其他情况下，这样做只会让代码无谓地变长。你首先应该考虑的是，编写清晰易懂且能完成所需功能的代码，等到审核代码时，再考虑采用更高效的方法</mark>。

### 4.3.3 让数字列表执行简单的统计计算

有几个专门用于**处理数字列表**的 Python **函数**。例如，你可以轻松地找出数字列表的**最大值**、**最小值**和**总和**：

```python
>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45
```

> 这里介绍的知识也适用于包含数百万个数的列表。

### 4.3.4 列表解析

<mark>列表解析将 `for` 循环和创建新元素的代码合并成一行，并自动附加新元素</mark>。

```python
squares = [value*2 for value in range(1, 11)]
print(squares)

Output:
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

要使用这种语法，首先指定一个描述性的**列表名**。然后指定一个**左方括号**并定义一个**表达式**，用于生成要存储到列表的值。接下来，编写一个 **`for` 循环**，用于给表达式提供值，再加上**右方括号**。<mark>注意，这里的 for 语句末尾没有冒号</mark>。

## 4.4 使用列表的一部分

在第 3 章中，你学习了**如何访问单个列表元素**。在本章中，你一直在学习**如何处理列表的所有元素**。你还可以**处理列表的部分元素**，Python 称之为**切片**。

### 4.4.1 切片

<mark>要创建切片，可指定要使用的第一个元素和最后一个元素的索引</mark>。与**函数** `range()` 一样，Python 在到达第二个索引之前的元素后停止。要输出列表中的前三个元素，需要指定索引 `0` 和 `3`，这将返回索引为 `0`、`1` 和 `2` 的元素，

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

Output:
['charles', 'martina', 'michael']
['martina', 'michael', 'florence']
['charles', 'martina', 'michael', 'florence']
['michael', 'florence', 'eli']
['michael', 'florence', 'eli']
```
<mark>如果没有指定第一个索引，Python 将自动从列表开头开始。要让切片终止于列表末尾，也可省略终止索引。负数索引返回离列表末尾相应距离的元素，因此你可以输出列表末尾的任意切片</mark>。

> 可在表示切片的方括号内指定第三个值。这个值告诉 Python 在指定范围内每隔多少元素提取一个。

### 4.4.2 遍历切片

<mark>如果要遍历列表的部分元素，可在 `for` 循环中使用切片</mark>。

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

Output:
Here are the first three players on my team:
Charles
Martina
Michael
```

### 4.4.3 复制列表

我们经常需要**根据既有列表创建全新的列表**。<mark>要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（`[:]`）。这让 Python 创建一个始于第一个元素、终止于最后一个元素的切片，即整个列表的副本</mark>。

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

Output:
My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake', 'ice cream']
```

如果是 `friend_foods = my_foods`，则是将 `my_foods` 赋给 `friend_foods`，而不是将 `my_foods` 的副本赋给 `friend_foods`。<mark>这种语法实际上是让 Python 将新变量 friend_foods 关联到已与 my_foods 相关联的列表，因此这两个变量指向同一个列表</mark>。

## 4.5 元组

<mark>列表非常适合用于存储在程序运行期间可能变化的数据集</mark>。**列表是可以修改的**，然而，有时候你需要**创建一系列不可修改的元素**，**元组**可以满足这种需求。<mark>Python 将不能修改的值称为不可变的，而不可变的列表被称为元组</mark>。

### 4.5.1 定义元组

**元组**看起来很像列表，但使用**圆括号**而非中括号来标识。定义元组后，就可**使用索引来访问其元素**，就像访问列表元素一样。

```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

Output:
200
50
```

> 注意：<mark>严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰</mark>。如果你要定义只包含一个元素的元组，必须要在这个元素后面加上逗号：`my_t` = (3,)。创建只包含一个元素的元组通常没有意义，但自动生成的元组有可能只有一个元素。

### 4.5.2 遍历元组中的所有值

像列表一样，也可以使用 `for` 循环来**遍历元组中的所有值**：

```python
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

Output:
200
50
```

### 4.5.3 修改元组变量

<mark>虽然不能修改元组的元素，但可以给存储元组的变量赋值，即重新定义整个元组</mark>。

```python
dimensions = (200, 50)
dimensions = (400, 100)
print("\nModified dimensions")
for dimension in dimensions:
    print(dimension)

Output:
400
100
```

相比于列表，**元组**是更简单的数据结构。<mark>如果需要存储的一组值在程序的整个生命周期内都不变，就可以使用元组</mark>。

## 4.6 设置代码格式

为确保所有人编写的代码结构都大致一致，Python 程序员会遵循一些格式设置约定。

### 4.6.1 格式设置指南

要提出 Python 语言修改建议，需要编写 **Python 改进提案**（Python Enhancement Proposal, PEP）。**PEP 8** 是最古老的 PEP 之一，向 Python 程序员提供了代码格式设置指南。PEP 8 的篇幅很长，但基本上与复杂的编码结构相关。

### 4.6.2 缩进

<mark>PEP 8 建议每级缩进都使用四个空格</mark>。这既可提高可读性，又留下了足够的多级缩进空间。

<mark>在字处理文档中，大家常常使用制表符而不是空格来缩进。对于字处理文档来说，这样做的效果很好，但混合使用制表符和空格会让 Python 解释器感到迷惑。每款文本编辑器都提供了一种设置，可将你输入的制表符转换为指定数量的空格。你在编写代码时，绝对应该使用制表符键，但一定要对编辑器进行设置，使其在文档中插入空格而不是制表符</mark>。

<mark>在程序中混合使用制表符和空格可能导致难以排查的问题。如果混合使用了制表符和空格，可将文件中的所有制表符都转换为空格，大多数编辑器都提供了这样的功能</mark>。

### 4.6.3 行长

<mark>很多 Python 程序员建议每行不超过 80 字符</mark>。**最初指定这样的指南时，在大多数计算机中，终端窗口每行只能容纳 79 字符**。当前，计算机屏幕每行可容纳的字符数多得多，为何还要使用 79 字符的标准行长呢？这里由别的原因。<mark>专业程序员通常会在同一个屏幕上打开多个文件，使用标准行长可以让他们在屏幕上并排打开两三个文件时同时看到各个文件的完整行</mark>。<mark>PEP 8 还建议注释的行长不应超过 72 字符，因为有些工具为大型项目自动生成文档时，会在每行注释开头添加格式化字符</mark>。

PEP 8 中有关行长的指南并非不可逾越的红线，有些小组将最大行长设置为 **99 字符**。协作编写程序时，大家几乎都遵守 PEP 8 指南。<mark>在大多数编辑器中，可以设置一个视觉标志（通常是一条竖线）</mark>，让你直到不能越过的界限在什么地方。

### 4.6.4 空行

<mark>要将程序的不同部分分开，可使用空行。你应该使用空行来组织程序文件，但也不能滥用</mark>。只要按本书的示例展示的那样做，就能掌握其中的平衡。

<mark>空行不会影响代码的运行，但会影响代码的可读性。Python 解释器根据水平缩进情况来解读代码，但不关心垂直间距</mark>。

### 4.6.5 其它格式设置指南

# 5. if 语句

编程时经常需要**检查一系列条件**，并据此决定采取什么措施。<mark>在 Python 中，`if` 语句让你能够检查程序的当前状态，并采取相应的措施</mark>。

在本章中，你将学习**条件测试**，以**检查所关心的任何条件**。你将学习**简单的 `if` 语句**，以及**创建一系列复杂的 `if` 语句**来确定当前到底处于什么情形。接下来，你将把学到的知识应用于列表，编写一个 `for` 循环，以一种方式处理列表中的大多数元素，并以另一种方式处理包含特定值的元素。

1. 如何**编写结果要么为 `True` 要么为 `False` 的条件测试**；
2. 如何**编写简单的 `if` 语句、`if-else` 语句和 `if-elif-else` 语句**，并且在程序中使用这些结构来测试特定的条件，以确定这些条件是否满足；
3. 如何**在利用高效的 `for` 循环的同时，以不同于其他元素的方式对特定的列表元素进行处理**；
4. 再次学习 Python 就代码格式提出的建议，从而确保即便编写的程序越来越复杂，其代码依然易于阅读和理解。

## 5.1 一个简单示例

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

Output:
Audi
BMW
Subaru
Toyota
```

## 5.2 条件测试

<mark>每条 if 语句的核心都是一个值为 True 或 False 的表达式，这种表达式称为条件测试</mark>。Python 根据条件测试的值为 True 还是 False 来决定是否执行 if 语句中的代码。如果条件测试的值为 True，Python 就执行紧跟在 if 语句后面的代码；如果为 False，Python 就忽略这些代码。

### 5.2.1 检查是否相等

最简单的条件测试**检查变量的值是否与特定值相等**：
```python
>>> car = 'bmw'
>>> car == 'bmw'
True
>>> car == 'audi'
False
```
这个**相等运算符**在两边的值相等时返回 `True`，否则返回 `False`。

### 5.2.2 检查是否相等时忽略大小写

<mark>在 Python 中检查是否相等时区分大小写</mark>。

```python
>>> car = 'Audi'
>>> car == 'audi'
False
```
如果大小写很重要，这种行为有其优点。**但如果大小写无关紧要，只想检查变量的值，可将变量的值转换为小写**，再进行比较：
```python
>>> car = 'Audi'
>>> car == 'audi'
False
```

### 5.2.3 检查是否不相等

<mark>要判断两个值是否不等，可结合使用惊叹号和等号（`!=`），其中的惊叹号表示不，其他很多编程语言中也是如此</mark>。

```python
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

Output:
Hold the anchovies!
```
<mark>你编写的大多数条件表达式检查两个值是否相等，但有时候检查两个值是否不等的效率更高</mark>。

### 5.2.4 数值比较

条件语句中可包含各种**数学比较**，如**等于**、**小于**、**小于等于**、**大于**、**大于等于**：

```python
>>> age = 18
>>> age == 18
True
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >=21
False
```

### 5.2.5 检查多个条件

你可能想**同时检查多个条件**。例如，有时候需要在两个条件都为 True 时才执行相应的操作，而有时候只要求一个条件为 True。在这些情况下，**关键字** `and` 和 `or` 都可助你一臂之力。

#### A. 使用 `and` 检查多个条件

<mark>要检查是否两个条件都为 `True`，可使用关键字 `and` 将两个条件测试合而为一</mark>。如果每个测试都通过了，整个表达式就为 `True`；如果至少一个测试没有通过，整个表达式就为 `False`。

```Python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21
False
>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
```
<mark>为改善可读性，可将每个测试分别放在一对圆括号内，但并非必须这样做</mark>。如`(age_0 >= 21) and (age_1 >= 21)`。

#### B. 使用 `or` 检查多个条件

<mark>关键字 `or` 也能够让你检查多个条件，但只要至少一个条件满足，就能通过整个测试</mark>。仅当两个测试都没有通过时，使用 `or` 的表达式才为 `False`。

### 5.2.6 检查特定值是否包含在列表中

**有时候，执行操作前必须检查列表是否包含特定的值**。

要**判断特定的值是否已包含在列表**中，可使用**关键字** `in`。
```python
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
```

### 5.2.7 检查特定值是否不包含在列表中

还有些时候，**确定特定的值未包含在列表中**很重要。在这种情况下，可使用**关键字** `not in`。
```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

Output:
Marie, you can post a response if you wish.
```

### 5.2.8 布尔表达式

术语**布尔表达式**不过是条件测试的别名。与条件表达式一样，布尔表达式的结果要么为 `True`，要么为 `False`。

**布尔值通常用于记录条件**，如游戏是否正在运行，或者用户是否可以编辑网站的特定内容：
```python
game_active = True
can_edit = False
```
在**跟踪程序状态或程序中重要的条件**方面，布尔值提供了一种高效的方式。

## 5.3 `if` 语句

理解**条件测试**后，就可以开始编写 **`if` 语句**了。`if` 语句有很多种，选择使用哪种取决于**要测试的条件数**。

### 5.3.1 简单的 `if` 语句

最简单的 `if` 语句只有**一个测试**和**一个操作**：
```python
if conditional_test:
    do something
```
第一行可包含**任何条件测试**，而在紧跟在测试后面的**缩进代码块**中，**可执行任何操作**。如果条件测试的结果为 `True`，Python 就会执行紧跟在 `if` 语句后面的代码，否则 Python 将忽略这些代码。
```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

Output:
You are old enough to vote!
Have you registered to vote yet?
```
<mark>在 `if` 语句中，缩进的作用与在 `for` 循环中相同</mark>。如果测试通过了，将执行 `if` 语句后面所有缩进的代码行，否则将忽略它们。

<mark>在紧跟 `if` 语句后面的代码块中，可根据需要包含任意数量的代码行</mark>。

### 5.3.2 if-else 语句

我们经常需要**在条件测试通过时执行一个操作，在没有通过时执行另一个操作**。在这种情况下，可使用 Python 提供的 `if-else` 语句。`if-else` 语句块类似于简单的 `if` 语句，但<mark>其中的 `else` 语句让你能够指定条件测试未通过时要执行的操作</mark>。

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

Output:
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
```

### 5.3.3 if-elif-else 结构

我们经常需要**检查超过两个的情形**，为此可使用 Python 提供的 **`if-elif-else` 结构**。Python 只执行 `if-elif-else` 结构中的一个代码块。它一次检查每个条件测试，直到遇到通过了的条件测试。测试通过后，Python 将执行紧跟在它后面的代码，并跳过余下的测试。
```python
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

Output:
Your admission cost is $25.
```
为了让代码更简洁，可不在 `if-elif-else` 代码块中打印门票价格，而只**在其中设置门票价格，并在它后面添加一个简单的函数调用 `print()`**:
```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
```
这些代码的输出与前一个示例相同，但 `if-elif-else` 结构的作用更小：它只确定门票价格，而不是在确定门票的同时打印一条消息。除效率更高外，这些修订后的代码还更容易修改：要调整输出消息的内容，只需修改一个而不是三个函数调用 `print()`。

### 5.3.4 使用多个 elif 代码块

<mark>可根据需要使用任意数量的 `elif` 代码块</mark>。

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")
```

### 5.3.5 省略 else 代码块

<mark>Python 并不要求 `if-else` 结构后面必须有 `else` 代码块</mark>。在有些情况下，`else` 代码块很有用；而在其他一些情况下，使用一条 `elif` 语句来处理特定的情形更清晰：

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
```
`else` 是一条包罗万象的语句，只要不满足任何 `if` 或 `elif` 中的条件测试，其中的代码就会执行。**这可能引入无效甚至恶意的数据**。如果知道最终要测试的条件，应考虑使用一个 `elif` 代码块来代替 `else` 代码块。这样就可以肯定，仅当满足相应的条件时，代码才会执行。

### 5.3.6 测试多个条件

`if-elif-else` 结构功能强大，但**仅适合用于只有一个条件满足的情况**：<mark>遇到通过了的测试后，Python 就跳过余下的测试</mark>。这种行为很好，效率很高，让你能够测试一个特定的条件。

然而，**有时候必须检查你关心的所有条件**。在这种情况下，**应使用一系列不包含 `elif` 和 `else` 代码块的简单 `if` 语句**。在可能有多个条件为 `True` 且需要在每个条件为 `True` 时都采取相应措施时，适合使用这种方法。
```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

Output:
Adding mushrooms.
Adding extra cheese.

Finished making your pizza!
```
<mark>总之，如果只想执行一个代码块，就使用 `if-elif-else` 结构；如果要执行多个代码块，就使用一系列独立的 `if` 语句</mark>。

## 5.4 使用 `if` 语句处理列表

### 5.4.1 检查特殊元素

下面就来进一步研究**如何检查列表中的特殊值**，并对其做合适的处理。
```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

Output:
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.

Finished making your pizza!
```

### 5.4.2 确定列表不是空的

到目前为止，我们对于处理的每个列表都做了一个简单的**假设**—**假设它们都至少包含一个元素**。<mark>因为马上就要让用户来提供存储在列表中的信息，所以不能再假设循环运行时列表不是空的</mark>。有鉴于此，**在运行 `for` 循环前确定列表是否为空很重要**。

```python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

Output:
Are you sure you want a plain pizza?
```
<mark>在 `if` 语句中将列表名用作条件表达式，Python 将在列表至少包含一个元素时返回 `True`，并在列表为空时返回 `False`</mark>。

### 5.4.3 使用多个列表

可使用**列表**和 `if` 语句来确定能否满足顾客的要求。在制作比萨前如何拒绝怪异的配料要求。
```python
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'peperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

Output:
Adding mushrooms.
Sorry, we don't have french fries.
Adding extra cheese.

Finished making your pizza!
```
<mark>请注意，如果比萨店供应的配料是固定的，也可使用一个元组来存储它们</mark>。

## 5.5 设置 `if` 语句的格式

在**条件测试的格式设置**方面，PEP 8 提供的**唯一建议**是，<mark>在诸如 `==` 、`>=` 和 `<=` 等比较运算符两边各添加一个空格</mark>。例如：

```python
if age < 4
```
<mark>这样的空格不会影响 Python 对代码的解读，而只是让代码阅读起来更容易</mark>。

# 6. 字典

在本章中，你将学习能够**将相关信息关联**起来的 Python **字典**，以及**如何访问和修改字典中的信息**。字典可存储的信息量几乎不受限制，因此我们会演示**如何遍历字典中的数据**。另外，你还将学习**存储字典的列表**、**存储列表的字典**和**存储字典的字典**。

1. 如何**定义字典**，以及如何**使用存储在字典中的信息**；
2. 如何**访问和修改字典中的元素**，以及如何**遍历字典中的所有信息**；
3. 如何**遍历字典中所有的键值对、所有的键和所有的值**；
4. 如何**在列表中嵌套字典**、**在字典中嵌套列表**以及**在字典中嵌套字典**。

## 6.1 一个简单的字典

```python
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

Output:
green
5
```

## 6.2 使用字典

在 Python 中，**字典**是一系列**键值对**。**每个键都与一个值相关联，你可使用键来访问相关联的值**。<mark>与键相关联的值可以是数、字符串、列表乃至字典。事实上，可将任何 Python 对象用作字典中的值</mark>。

在 Python 中，**字典用放在花括号（`{}`）中的一系列键值对表示**。

**键值对是两个相关联的值**。**指定键时，Python 将返回与之相关联的值**。**键和值之间用冒号分隔，而键值对之间用逗号分隔**。在字典中，想存储多少个键值对都可以。

### 6.2.1 访问字典中的值

**要获取与键相关联的值，可依次指定字典名和放在方括号内的键**。
```python
alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

Output:
You just earned 5 points!
```

### 6.2.2 添加键值对

**字典**是一种**动态结构**，可随时在其中**添加键值对**。**要添加键值对，可依次指定字典名、用方括号括起的键和相关联的值**。
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

Output:
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```
> 注意 在 Python 3.7 中，<mark>字典中元素的排列顺序与定义时相同</mark>。如果将字典打印出来或遍历其元素，将发现元素的排列顺序与添加顺序相同。

### 6.2.3 先创建一个空字典

**在空字典中添加键值对**有时候可提供便利，而有时候必须这样做。为此，**可先使用一对空花括号定义一个字典，再分行添加各个键值对**。
```python
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

Output:
{'color': 'green', 'points': 5}
```
<mark>使用字典来存储用户提供的数据或在编写能自动生成大量键值对的代码时，通常需要先定义一个空字典</mark>。

### 6.2.4 修改字典中的值

**要修改字典中的值，可依次指定字典名、用方括号括起的键，以及与该键相关联的新值**。
```python
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

Output:
The alien is green.
The alien is now yellow.
```
```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': "medium"}
print(f"Original x_position: {alien_0['x_position']}")

# 向右移动外星人。
# 根据当前速度确定将外星人向右移动多远。
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快。
    x_increment = 3

# 新位置为旧位置加上移动距离。
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x_position: {alien_0['x_position']}")

Output:
Original x_position: 0
New x_position: 2
```
这种技术很棒：**通过修改外星人字典中的值，可改变外星人的行为**。
```python
alien_0['speed'] = 'fast'
```

### 6.2.5 删除键值对

<mark>对于字典中不再需要的信息，可使用 `del` 语句将相应的键值对彻底删除</mark>。**使用 `del` 语句时，必须指定字典名和要删除的键**。

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

Output:
{'color': 'green', 'points': 5}
{'color': 'green'}
```
> 注意：删除的键值对会永远消失。 

### 6.2.6 由类似对象组成的字典

在前面的示例中，字典存储的是**一个对象（游戏中的一个外星人）的多种信息**，但你也可以使用字典来存储**众多对象的同一种信息**。

确定需要**使用多行来定义字典**时，要在输入**左花括号**后按**回车键**。**在下一行缩进四个空格，指定第一个键值对，并在它后面加上一个逗号**。</mark>此后再按回车键时，文本编辑器将自动缩进后续键值对，且缩进量与第一个键值对相同</mark>。

定义好字典后，在最后一个键值对的下一行添加一个**右花括号**，并**缩进四个空格**，**使其与字典中的键对齐**。<mark>一种不错的做法是，在最后一个键值对后面也加上逗号，为以后在下一行添加键值对做好准备</mark>。

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

Output:
Sarah's favorite language is C.
```

### 6.2.7 使用 `get()` 来访问值

使用放在方括号内的键从字典中获取感兴趣的值时，可能会引发问题：<mark>如果指定的键不存在就会出错</mark>。

就字典而言，可使用**方法** `get()` **在指定的键不存在时返回一个默认值**，从而避免这样的错误。

方法 `get()` 的**第一个参数用于指定键，是必不可少的**；**第二个参数为指定的键不存在时要返回的值，是可选的**：

```python
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

Output:
No point value assigned.
```
如果字典中有键 `points`，将获得与之相关联的值；**如果没有，将获得指定的默认值**。虽然这里没有键 `points`，但将获得一条清晰的消息，不会引发错误。

<mark>如果指定的键有可能不存在，应考虑使用方法 `get()`，而不要使用方括号表示法</mark>。

> <mark>注意 调用 `get()` 时，如果没有指定第二个参数且指定的键不存在，Python 将返回值 `None`。这个特殊值表示没有相应的值。`None` 并非错误，而是一个表示所需值不存在的特殊值</mark>。

## 6.3 遍历字典 

字典可用于以各种方式存储信息，因此有**多种遍历方式**：**可遍历字典的所有键值对**，也可**仅遍历键或值**。

### 6.3.1 遍历所有键值对

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

Output:

Key: username
Value: efermi

Key: first
Value: enrico

Key: last
Value: fermi
```
<mark>要编写遍历字典的 `for` 循环，可声明两个变量，用于存储键值对中的键和值。这两个变量可以使用任意名称</mark>。

`for` 语句的第二部分包含字典名和**方法** `items()`，它**返回一个键值对列表（元组列表）**。接下来，`for` **循环依次将每个键值对赋给指定的两个变量**。第一个函数调用 `print()` 中的 `\n` **确保在输出每个键值对前都插入一个空行**。

由于该字典中的**键都是人名，值都是语言**，因此在循环中使用变量 `name` 和 `language` ，而不是 `key` 和 `value`。这让人更容易明白循环的作用：
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

Output:
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.
```

### 6.3.2 遍历字典中的所有键

在**不需要使用字典中的值**时，方法 `keys()` 很有用。
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

Output:
Jen
Sarah
Edward
Phil
```
</mark>遍历字典时，会默认遍历所有的键。因此，如果将上述代码中的 `for name in favorite_languages.keys():` 替换为 `for name in favorite_languages:`，输出将不变。显式地使用方法 `keys()` 可让代码更容易理解，你可以选择这样做，但是也可以省略它。</mark>。

在这种循环中，可**使用当前键来访问与之相关联的值**。
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

Output:
Hi Jen.
Hi Sarah.
        Sarah, I see you love C!
Hi Edward.
Hi Phil.
        Phil, I see you love Python!
```
还可使用方法 `keys()` 确定某个人是否接受了调查。
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
    print("Eric, please take our poll!")

Output:
Eric, please take our poll!
```
<mark>方法 `keys()` 并非只能用于遍历：实际上，它返回一个列表，其中包含字典中的所有键</mark>。因此 `if 'erin' not in favorite_languages.keys():` 处的代码行**只核实** `erin` **是否包含在这个列表中**。

### 6.3.3 按特定顺序遍历字典中的所有键

<mark>从 Python 3.7 起，遍历字典时将按插入的顺序返回其中的元素</mark>。

要**以特定顺序返回元素**，一种办法是在 `for` 循环中**对返回的键进行排序**。为此，可使用**函数** `sorted()` **来获得按特定顺序排列的键列表的副本**：



# 7. 用户输入和 while 循环

# 8. 函数

# 9. 类

# 10. 文件和异常

# 11. 测试代码

# 12. 武装飞船

# 13. 外星人来了

# 14. 计分

# 15. 生成数据

# 16. 下载数据

# 17. 使用 API

# 18. 从 Django 入手

# 19. 用户账户

# 20. 设置应用程序的样式并部署