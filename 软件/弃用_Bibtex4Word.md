## [Bibtex4Word](http://www.ee.ic.ac.uk/hp/staff/dmb/perl/index.html)

> Bibtex4Word 是微软 Word 的一个插件，它允许引用参考文献，并使用你选择的格式风格将文献条目插入你的文档中。

### 设置

1. 将 bibtex4word.dot 文件复制到 Word Startup 文件夹：C:\Users\ *****\AppData\Roaming\Microsoft\Word\STARTUP。
2. 对于 Texlive ，设置环境变量：
    - BIBEXE = xxx\bin\win32\bibtex.exe, where xxx is your TexLive folder (e.g. C:\texlive\2011)
    - 然后，以下方式任选其一：
        - OPENOUT_ANY= r
        - 在 xxx\texmf.cnf 结尾添加 OPENOUT_ANY = r

### 定义文献格式

在 Define Bibtex Style 对话框中填写“GBT7714-2005NLang/nsch^”（引号内的内容），定义你选用的参考文献样式文件名（斜杠前）和该样式属性（斜杠后）。这部分内容详见 Bibtex4Word 网站的文献样式说明。此处稍作讲述
1. 斜杠前是你选用的参考文献样式名称，如：GBT7714-2005NLang，或 abbrvnat，或 IEEEtran 等等；
2. 斜杠后是你想在该样式文件中决定的参考文献引用的方式（上标？压缩引用？超链接？），例如：
    - n，表示强制文后文献以数字顺序排列，不管选用的样式文件是著者年还是顺序方式的；
    - s，表示 “sort”，将顺序引用的标记 [2,4,1,3] 整理为 [1,2,3,4]；
    - c，表示 “compress”，将顺序引用的标记 [1,2,3,4] 压缩为 [1-4]；
    - h，表示 “hyperlink”，将引用标记与文后文献的对应条目之间建立超链接关系，按住 “Ctrl” 键用鼠标左击标记即可跳转至对应的文献条目，返回则是按住 “Alt” 键后按一下方向键中的 “<-” 键即可；
    - ^，表示上标引用方式，即 $^{[4]}$ 样式；
    - [，表示引用标记采用方括号样式，例如 [4-9]；
    - (，表示引用标记采用圆括号样式，例如 (Smith, 2000)；
常见期刊设置：
- Advanced Materials ：MSP/nsch^

### 具体插入文献步骤

地址：<https://www.cnblogs.com/shenxiaolin/p/10394497.html>

1. 打开 word，点**加载项**，第 5 个图标（Define Bibtex File），打开 bib 文件，也就是加入自己想要插入文献的 bib 文件。
2. 点第 4 个图标（刷子形状（Define Bibtex Style）），选择参考文献格式。此时用到上面的文献格式，例如：输入 gbt7714-unsrt/nsch^，斜杠前是格式名，后面是属性。
3. 鼠标放在想插入文献的正文中，点第 1 个图标（红色加号），像 latex 一样，输入待插入的文献（bibtexkey），一般用 [auth][year][veryshorttitle]，如 jing2018prominence，多个文献间用逗号分开，然后确定。
4. 鼠标放在准备放置参考文献列表的位置，点第 2 个图标（列表），然后你就会发现你插入的参考文献出现了。修改 bib 文件并保存后再次点击第 2 个图标进行更新。
5. 此时如果正文中插入文献的地方是具体的文献的名字（jing2018prominence）而不是序号，点第 3 个图标（眼睛），就好啦~

### .bst 文件地址

下载的 .bst 文件可以保存到以下文件夹：C:\texlive\2021\texmf-dist\bibtex\bst\

### 参考文献缩写名 .csv 文件

[Github: JabRef/abbrv.jabref.org](https://github.com/JabRef/abbrv.jabref.org)

### 注意

1. 文献在正文中的编号顺序与 .bst 文件相关。
2. 将 .bst 文件与 word 文件放在同一个文件夹，否则可能显示 Bibtex was unable to find style  file：...。