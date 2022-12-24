## tikz 命令速查

> 本内容主要来自 pgfmanual.pdf

> 1. default 表示 key 后面的选项并不是必须的
> 2. initially 表示该 key 未出现时的默认值
> 3. 默认省略开头/tikz
> 4. Keys 的内容都需要放在方括号内，但放在`\begin{tikzpicture}`后面、\draw等命令后面，还是路径内部node等命令后面需要具体区分。
> 5. 范围的限定是通过花括号实现的。

### 13 Specifying Coordinates 指定坐标

#### 13.1 Overview 概述

`(<coordinate system> cs:<list of key–value pairs specific to the coordinate system>)`

```latex
\draw (canvas cs:x=0cm,y=2mm) -- (canvas polar cs:radius=2cm,angle=30);
\draw (0cm,2mm) -- (30:2cm);
\draw (0,0) -- ([xshift=3pt] 1,1);
\draw (1,0) -- +([shift=(135:5pt)] 30:2cm);
```

#### 13.2 Coordinate Systems 坐标系

##### 13.2.1 Canvas, XYZ, and Polar Coordinate Systems Canvas，XYZ 和 Polar 坐标系

**Coordinate system** `canvas`

|Keys (/tikz/cs/)|Types|Values|
|-----|-----|-----|
|x=&lt;*dimension*&gt;|no default, initially `0pt`||
|y=&lt;*dimension*&gt;|no default, initially `0pt`||

```latex
\fill (canvas cs:x=1cm,y=1.5cm) circle (2pt);
\fill (canvas cs:x=2cm,y=-5mm+2pt) circle (2pt);
等同于：
\fill (1cm,1.5cm) circle (2pt);
\fill (2cm,-5mm+2pt) circle (2pt);
```

**Coordinate system** `xyz`

|Keys (/tikz/cs/)|Types|Values|
|-----|-----|-----|
|x=&lt;*factor*&gt;|no default, initially `0`||
|y=&lt;*factor*&gt;|no default, initially `0`||
|z=&lt;*factor*&gt;|no default, initially `0`||

```latex
\draw (0,0) -- (xyz cs:x=1);
\draw (0,0) -- (xyz cs:y=1);
\draw (0,0) -- (xyz cs:z=1);
等同于：
\draw (0,0) -- (1,0);
\draw (0,0) -- (0,1,0);
\draw (0,0) -- (0,0,1);
```

**Coordinate system** `canvas polar`

|Keys (/tikz/cs/)|Types|Values|
|-----|-----|-----|
|angle=&lt;*degrees*&gt;|no default||
|radius=&lt;*dimension*&gt;|no default||
|x radius=&lt;*dimension*&gt;|no default||
|y radius=&lt;*dimension*&gt;|no default||

```latex
\draw (0,0) -- (canvas polar cs:angle=30,radius=1cm);
\draw (0cm,0cm) -- (30:1cm) -- (60:1cm) -- (90:1cm) -- (120:1cm) -- (150:1cm) -- (180:1cm);
\draw (0,0) -- (2ex,0pt) -- +(up:1ex);
```

**Coordinate system** `xyz polar`

|Keys (/tikz/cs/)|Types|Values|
|-----|-----|-----|
|angle=&lt;*degrees*&gt;|no default||
|radius=&lt;*factor*&gt;|no default||
|x radius=&lt;*dimension*&gt;|no default||
|y radius=&lt;*dimension*&gt;|no default||

```latex
\draw (xyz polar cs:angle=0,radius=2)
  -- (xyz polar cs:angle=30,radius=2)
  -- (xyz polar cs:angle=60,radius=2)
  -- (xyz polar cs:angle=90,radius=2);
\draw (0,0) -- (30:1) -- (60:1) -- (90:1) -- (120:1) -- (150:1) -- (180:1);
```

**Coordinate system** `xy polar`

这只是 `xyz polar` 的一个别名，有些人可能更喜欢这个名字，因为 `xyz polar` 坐标中不涉及 `z` 坐标。

#### 13.3 Coordinates at Intersections 交点坐标

##### 13.3.1 Intersections of Perpendicular Lines 垂直线的交点

**Coordinate system** `perpendicular`

|Keys (/tikz/cs/)|Types|Values|
|-----|-----|-----|
|horizontal line through={(&lt;*coordinate*&gt;)}|no default||
|vertical line through={(&lt;*coordinate*&gt;)}|no default||

`(<p> |- <q>)` or `(<q> -| <p>)`

```latex
\path (30:1cm) node(p1) {$p_1$} (75:1cm) node(p2) {$p_2$};
\draw (-0.2,0) -- (1.2,0) node(xline)[right] {$q_1$};
\draw (2,-0.2) -- (2,1.2) node(yline)[above] {$q_2$};
\draw[->] (p1) -- (p1 |- xline);
\draw[->] (p2) -- (p2 |- xline);
\draw[->] (p1) -- (p1 -| yline);
\draw[->] (p2) -- (p2 -| yline);

\node (A) at (0,1) {A};
\node (B) at (1,1.5) {B};
\node (C) at (2,0) {C};
\node (D) at (2.5,-2) {D};
\draw (A) -- (B) node [midway] {x};
\draw (C) -- (D) node [midway] {x};
\node at ({$(A)!.5!(B)$} -| {$(C)!.5!(D)$}) {X};
```
##### 13.3.2 Intersections of Arbitrary Paths 任意路径的交点

**TikZ Library** `intersections`

`\usetikzlibrary{intersections}`

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|name path=&lt;*name*&gt;|no default||
|name path path global=&lt;*name*&gt;|no default||
|name intersections=&lt;*options*&gt;|no default||

```latex
\draw [name path=ellipse] (2,0.5) ellipse (0.75cm and 1cm);
\draw [name path=rectangle, rotate=10] (0.5,0.5) rectangle +(2,1);
\fill [red, opacity=0.5, name intersections={of=ellipse and rectangle}]
  (intersection-1) circle (2pt) node {1}
  (intersection-2) circle (2pt) node {2};
```

|Keys (/tikz/intersections)|Types|Values|
|-----|-----|-----|
|of=&lt;*name path 1*&gt; and &lt;*name path 2*&gt;|no default||
|name=&lt;*prefix*&gt;|no default, initially `intersection`||
|total=&lt;*macro*&gt;|no default||
|by=&lt;*comma-separated list*&gt;|no default||
|sort by=&lt;*path name*&gt;|no default||

```latex
\draw [name path=curve 1] (-2,-1) .. controls (8,-1) and (-8,1) .. (2,1);
\draw [name path=curve 2] (-1,-2) .. controls (-1,8) and (1,-8) .. (1,2);
\fill [name intersections={of=curve 1 and curve 2, name=i, total=\t}]
      [red, opacity=0.5, every node/.style={above left, black, opacity=1}]
      \foreach \s in {1,...,\t}{(i-\s) circle (2pt) node {\footnotesize\s}};

\draw [name path=curve 1] (-2,-1) .. controls (8,-1) and (-8,1) .. (2,1);
\draw [name path=curve 2] (-1,-2) .. controls (-1,8) and (1,-8) .. (1,2);
\fill [name intersections={of=curve 1 and curve 2, by={a,b}}]
      (a) circle (2pt)
      (b) circle (2pt);
\fill [name intersections={
        of=curve 1 and curve 2,
        by={[label=center:a],[label=center:...],[label=center:i]}}];

\foreach \pathname/\shift in {line/0cm, curve/2cm}{
  \tikzset{xshift=\shift}
  \draw [->, name path=curve] (1,1.5) .. controls (-1,1) and (2,0.5) .. (0,0);
  \draw [->, name path=line] (0,-.5) -- (1,2) ;
  \fill [name intersections={of=line and curve,sort by=\pathname, name=i}]
    [red, opacity=0.5, every node/.style={left=.25cm, black, opacity=1}]
    \foreach \s in {1,2,3}{(i-\s) circle (2pt) node {\footnotesize\s}};
}
```

### 14 Syntax for Path Specifications 路径说明语法

`\path<specification>;`

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|name=&lt;*path name*&gt;|no default||
|every path|style, initially empty|as `every path/.style={draw}`|
|insert path=&lt;*path*&gt;|no default|as `c/.style={insert path={circle[radius=2pt]}}`|
|append after command=&lt;*path*&gt;|no default|as `[append after command={(foo)--(1,1)},draw]`|
|prefix after command=&lt;*path*&gt;|no default||

#### 14.1 The Move-To Operation move-to 操作

`\path … <coordinate> …;`

#### 14.2 The Line-To Operation line-to 操作

##### 14.2.1 Straight Lines 直线

`\path … --<coordinate or cycle> …;`

```latex
\draw (0,0) --(1,1) (1,1) --(2,0);
\draw (3,0) -- (4,1) -- (5,0);
\draw (5,0) -- (6,1) -- (6,0) -- cycle (7,0) -- (8,1) -- (8,0) -- cycle;
```

##### 14.2.2 Horizontal and Vertical Lines 水平和垂直线

`\path … -|<coordinate or cycle> …;`
`\path … |-<coordinate or cycle> …;`

```latex
\draw (0,0) node(a) [draw] {A} (1,1) node(b) [draw] {B};
\draw (a.north) |- (b.west);
\draw[color=red] (a.east) -| (2,1.5) -| (b.north);
```

#### 14.3 The Curve-To Operation curve-to 操作

`\path … ..controls<c>and<d>..<y or cycle> …;`

```latex
\draw[line width=10pt] (0,0) .. controls (1,1) .. (4,0) 
                             .. controls (5,0) and (5,1) .. (4,1);
```

#### 14.4 The Rectangle Operation 矩形操作

`\path … rectangle<corner or cycle> …;`

```latex
\draw (0,0) rectangle (1,1);
```

#### 14.5 Rounding Corners 圆角

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|rounded corners=&lt;*inset*&gt;|default 4pt||
|sharp corners|no value||

#### 14.6 The Circle and Ellipse Operations 圆和椭圆操作

`\path … circle[<options>] …;`
`\path … ellipse[<options>] …;`

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|x radius=&lt;*value*&gt;|no default||
|y radius=&lt;*value*&gt;|no default||
|radius=&lt;*value*&gt;|no default||
|at=&lt;*coordinate*&gt;|no default||
|every circle|style, no value||

```latex
\fill (1,0) circle [x radius=1cm, y radius=5mm, rotate=30];
\draw (1,1) ellipse [x radius=1cm,y radius=.5cm];
```

#### 14.7 The Arc Operation 弧线操作

`\path … arc[<options>] …;`

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|start angle=&lt;*degrees*&gt;|no default||
|end angle=&lt;*degrees*&gt;|no default||
|delta angle=&lt;*degrees*&gt;|no default||

```latex
\begin{tikzpicture}[radius=1cm]
    \draw (0,0) arc[start angle=180, end angle=90]
      -- (2,.5) arc[start angle=90, delta angle=-90];
    \draw (4,0) -- +(30:1cm)
                arc [start angle=30, delta angle=30] -- cycle;
    \draw (8,0) arc [start angle=0, end angle=270,
                     x radius=1cm, y radius=5mm] -- cycle;
\end{tikzpicture}

\begin{tikzpicture}[radius=1cm,delta angle=30]
  \draw (-1,0) -- +(3.5,0);
  \draw (1,0) ++(210:2cm) -- +(30:4cm);
  \draw (1,0) +(0:1cm) arc [start angle=0];
  \draw (1,0) +(180:1cm) arc [start angle=180];
  \path (1,0) ++(15:.75cm) node{$\alpha$};
  \path (1,0) ++(15:-.75cm) node{$\beta$};
\end{tikzpicture}
```

#### 14.8 The Grid Operation 网格操作

`\path … grid[<options>]<corner or cycle> …;`

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|step=&lt;*number or dimension or coordinate*&gt;|no default, initially 1cm||
|xstep=&lt;*dimension or number*&gt;|no default, initially 1cm||
|ystep=&lt;*dimension or number*&gt;|no default, initially 1cm||
|help lines|style, initially line width=0.2pt, gray||

```latex
\draw (0,0) grid [xstep=.5,ystep=.75] (3,2);
\draw[help lines] (0,0) grid (3,3);
```

#### 14.13 The To Path Operation

`\path … to[<options>] <nodes> <coordinate or cycle> …;`

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|edge node=&lt;*node specification*&gt;|no default||
|edge label=&lt;*text*&gt;|no default||
|edge label'=&lt;*text*&gt;|no default||
|every to|style, initially empty||
|to path=&lt;*path*&gt;|no default||
|execute at begin to=&lt;*code*&gt;|no default||
|execute at end to=&lt;*code*&gt;|no default||

```latex
\draw (0,0) to[out=90,in=180] node [sloped,above] {x} (3,2);
\draw (0,0) to [out=90,in=180,
                edge node={node [sloped,above] {x}}] (3,2);
\begin{tikzpicture}[to path={
    .. controls +(1,0) and +(1,0) .. (\tikztotarget) \tikztonodes}]

```

#### 14.14 The Foreach Operation foreach操作

`\path … foreach<variables>[<options>] in <list> {<path commands>} …;`

```latex
\draw (0,0) foreach \x in {1,...,3} { -- (\x,1) -- (\x,0) };
```

关于 foreach 命令的更多细节，见第 88 节。

#### 14.17 The Node and Edge Operations 节点和边操作

> 详见第17节

### 15 Actions on Paths 路径上的行为

#### 15.1 Overview 概述

|Abbreviation|Full Name|
|---------|---------|
|`\draw`|`\path[fill]`|
|`\fill`|`\path[fill]`|
|`\filldraw`|`\path[fill, draw]`|
|`\pattern`|`\path[pattern]`|
|`\shade`|`\path[shade]`|
|`\shadedraw`|`\path[shade, draw]`|
|`\clip`|`\path[clip]`|
|`\useasboundingbox`|`\path[use as bounding box]`|

#### 15.2 Specifying a Color 指定颜色

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|color=&lt;*color name*&gt;|no default||

#### 15.3 Drawing a Path 绘制路径

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|draw=&lt;*color*&gt;|default is scope’s color setting||

##### 15.3.1 Graphic Parameters: Line Width, Line Cap, and Line Join 图形参数：线宽、线帽和线条连接

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|line width=&lt;*dimension*&gt;|no default, initially 0.4pt||
|ultra thin|style, no value|fixed 0.1pt|
|very thin|style, no value|fixed 0.2pt|
|thin|style, no value|fixed 0.4pt|
|semithick|style, no value|fixed 0.6pt|
|thick|style, no value|fixed 0.8pt|
|very thick|style, no value|fixed 1.2pt|
|ultra thick|style, no value|fixed 1.6pt|
|line cap=&lt;*type*&gt;|no default, initially *butt*|*round*, *rect*, *butt*|
|line join=&lt;*type*&gt;|no default, initially *miter*|*round*, *bevel*, *miter*|
|miter limit=&lt;*factor*&gt;|no default, initially 10||

##### 15.3.2 Graphic Parameters: Dash Pattern 图形参数：虚线

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|dash pattern=&lt;*dash pattern*&gt;|no default|as *on 2pt off 3pt on 4pt off 4pt*|
|dash phase=&lt;*dash phase*&gt;|no default, initially 0pt||
|dash=&lt;*dash pattern*&gt; phase &lt;*dash phase*&gt;|no default||
|dash expand off|no value||
|solid|style, no value||
|dotted|style, no value||
|densely dotted|style, no value||
|loosely dotted|style, no value||
|dashed|style, no value||
|densely dashed|style, no value||
|loosely dashed|style, no value||
|dash dot|style, no value||
|densely dash dot|style, no value||
|loosely dash dot|style, no value||
|dash dot dot|style, no value||
|densely dash dot dot|style, no value||
|loosely dash dot dot|style, no value||

##### 15.3.3 Graphic Parameters: Draw Opacity 图形参数：绘制不透明度

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|draw opacity|||

##### 15.3.4 Graphic Parameters: Double Lines and Bordered Lines 图形参数：双线和边界线

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|double=&lt;*core color*&gt;|default white||
|double distance=&lt;*dimension*&gt;|no default, initially 0.6pt||
|double distance between line centers=&lt;*dimension*&gt;|no default||
|double equal sign distance|style, no value||

#### 15.4 Adding Arrow Tips to a Path 在路径上添加箭头

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|arrows|||

#### 15.5 Filling a Path

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|fill=&lt;*color*&gt;|default is scope’s color setting||

### 16 Arrows 箭头

#### 16.1 Overview 概述

`\usetikzlibrary {arrows.meta}`

#### 16.2 Where and When Arrow Tips Are Placed 箭头放置的位置和时间

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|arrows=&lt;*start arrow specification*&gt;-&lt;*end arrow specification*&gt;|no default||
|tips=&lt;*value*&gt;|default *true*, initially *on draw*|*true*, *proper*, *on draw*, *on proper draw*, *never* or *false*|

#### 16.3 Arrow Keys: Configuring the Appearance of a Single Arrow Tip 箭头键：配置单个箭头的外观

##### 16.3.1 Size 大小

|Keys (/pgf/arrow keys)|Types|Values|
|-----|-----|-----|
|length=&lt;*dimension*&gt; &lt;*line width factor*&gt;&lt;*outer factor*&gt;|no default|as *-Latex[length=0pt 3 1]*|
|width=&lt;*dimension*&gt; &lt;*line width factor*&gt;&lt;*outer factor*&gt;|no default||
|width'=&lt;*dimension*&gt; &lt;*length factor*&gt;&lt;*line width factor*&gt;|no default||
|inset=&lt;*dimension*&gt; &lt;*line width factor*&gt;&lt;*outer factor*&gt;|no default||
|inset'=&lt;*dimension*&gt; &lt;*length factor*&gt;&lt;*line width factor*&gt;|no default||
|angle'=&lt;*angle*&gt;|no default||

##### 16.3.2 Scaling 缩放

|Keys (/pgf/arrow keys)|Types|Values|
|-----|-----|-----|
|scale=&lt;*factor*&gt;|no default, initially 1||
|scale length=&lt;*factor*&gt;|no default, initially 1||
|scale width=&lt;*factor*&gt;|no default, initially 1||

##### 16.3.6 Coloring 颜色

|Keys (/pgf/arrow keys)|Types|Values|
|-----|-----|-----|
|color=&lt;*color or empty*&gt;|no default, initially empty||
|fill=&lt;*color or none*&gt;|no default||
|open|no value||

#### 16.4 Arrow Tip Specifications 箭头规范

##### 16.4.4 Defining Shorthands 定义速记

`Key handler <key>/.tip=<end specification>`

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|>=&lt;*end arrow specification*&gt;|no default||
|shorten <=&lt;*length*&gt;|no default||
|shorten >=&lt;*length*&gt;|no default||

##### 16.4.5 Scoping of Arrow Keys 箭头键的范围

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|arrows={[&lt;*arrow keys*&gt;]}|no default||

### 17 Nodes and Edges 节点和边

#### 17.1 Overview 概述

#### 17.2 Nodes and Their Shapes 节点和它们的形状

```latex
\fill[fill=yellow!80!black] 
       (0,0) node {first node} 
    -- (1,1) node[behind path] {second node} 
    -- (2,0) node {third node};
```

##### 17.2.1 Syntax of the Node Command 节点命令语法

`\path … node <foreach statements> [<options>] (<name>) at (<coordinate>) :<animation attribute>={<options>} {<node contents>} …;`

**Order of the parts of the specification. 指定中各部分的顺序。**

**The text of a node. 节点的文本。**

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|node contents=&lt;*node contents*&gt;|no default||
- `node contents=<node contents>`
    ```latex
    \path (0,0) node[red] {A}
        (1,0) node[blue] {B}
        (2,0) node[green,node contents=C]
        (3,0) node[node contents=D];
    ```

**Specifying the location of the node. 指定节点的位置。**

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|at=&lt;*coordinate*&gt;|no default||
|behind path|no value||
|in front of path|no value||

- `behind path`
    ```latex
    \fill[fill=blue!50, draw=blue, very thick]
           (0,0) node[behind path,fill=red!50] {first node}
        -- (1.5,0) node[behind path,fill=green!50] {second node}
        -- (1.5,1) node[behind path,fill=brown!50] {third node}
        -- (0,1) node[fill=blue!30] {fourth node};
    ```

**The name of a node. 节点的名称。**

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|name=&lt;*node name*&gt;|no default||
|alias=&lt;*another node name*&gt;|no default||

**The shape of a node. 节点的形状。**

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|shape=&lt;*shape name*&gt;|no default, initially `rectangle`|`rectangle`, `circle`, `coordinate`|

```latex
\fill[fill=yellow!80!black]
       (0,0) node {first node}
    -- (1,1) node[draw,behind path] {second node}
    -- (0,2) node[fill=red!20,draw,double,rounded corners] {third node};
```
```latex
\usetikzlibrary {shapes.geometric}
\fill[fill=yellow!80!black]
       (0,0) node {first node}
    -- (1,1) node[ellipse,draw,behind path] {second node}
    -- (0,2) node [circle,fill=red!20] {third node};
```

**Animating a node. 对节点进行动画处理。** 动画在第 26 节中详细讨论。

```latex
\usetikzlibrary {animations}
\node :fill opacity = { 0s="1", 2s="0", begin on=click }
      :rotate = { 0s="0", 2s="90", begin on=click }
      [fill = blue!20, draw = blue, ultra thick, circle] {Click me!};
```

**The foreach statement for nodes. 节点的 foreach 语句**

以下两个代码具有相同的效果：
```latex
\draw (0,0) node foreach \x in {1,2,3} at (\x,0) {\x};
\draw (0,0) node at (1,0) {1} node at (2,0) {2} node at (3,0) {3};
```
当你提供几个 `foreach` 语句时，它们就像“嵌套循环”一样工作：
```latex
\node foreach \x in {1,...,4} foreach \y in {1,2,3}
    [draw] at (\x,\y) {\x,\y};
```

实际上，您可以在此处使用 `\foreach` 命令的全部功能，包括多个参数和选项，请参见第 88 节。

**Styles for nodes. 节点样式。**下列样式影响了节点的渲染方式：

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|every node|style, initially empty||
|every &lt;*shape*&gt; node|style, initially empty||
|execute at begin node=&lt;*node*&gt;|no default||
|execute at end node=&lt;*node*&gt;|no default||

- `every node`
    ```latex
    \begin{tikzpicture}[every node/.style={draw}]
        \draw (0,0) node {A} -- (1,1) node {B};
    \end{tikzpicture}
    ```
- `every <shape> node`
    ```latex
    \begin{tikzpicture}
        [every rectangle node/.style={draw},
         every circle node/.style={draw,double}]
        \draw (0,0) node[rectangle] {A} -- (1,1) node[circle] {B};
    \end{tikzpicture}
    ```
- `execute at begin node=<code>`
- `execute at end node=<code>`
    ```latex
    \begin{tikzpicture}
        [execute at begin node={A},
         execute at end node={D}]
        \node[execute at begin node={B}] {C};
    \end{tikzpicture}
    ```

**Name scopes. 命名节点。**

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|name prefix=&lt;*text*&gt;|no default, initially empty||
|name suffix=&lt;*text*&gt;|no default, initially empty||

- `name prefix=<text>`
    ```latex
    \begin{scope}[name prefix = top-]
        \node (A) at (0,1) {A};
        \node (B) at (1,1) {B};
        \draw (A) -- (B);
    \end{scope}
    \begin{scope}[name prefix = bottom-]
        \node (A) at (0,0) {A};
        \node (B) at (1,0) {B};
        \draw (A) -- (B);
    \end{scope}
    \draw[red] (top-A) -- (bottom-B);
    ```

有一种特殊的语法用于指定“轻量级”节点：

`\path … coordinate [<options>] (<name>) at (<coordinate>) …;`

这与 `\node [shape=coordinate] [<options>] (<name>) at (<coordinate>) {};` 具有相同的效果，其中 `at` 部分可以省略。

由于节点往往是路径上唯一的路径操作，所以有两条特殊命令用于创建只包含一个节点的路径：

|Abbreviation|Full Name|
|---------|---------|
|\node|\path node|
|\coordinate|\path coordinate|

##### 17.2.2 Predefined Shapes 预定义形状

默认情况下，pgf 和 TikZ 定义了三种形状：`rectangle`，`circle`，以及 `coordinate`。通过加载库包，您可以定义更多形状，如椭圆或菱形；有关形状的完整列表，请参见第 71 节。

```latex
\begin{tikzpicture}[every node/.style={draw}]
    \path[yshift=1.5cm,shape=rectangle]
        (0,0) node(a1){} (1,0) node(a2){}
        (1,1) node(a3){} (0,1) node(a4){};
    \filldraw[fill=yellow!80!black] (a1) -- (a2) -- (a3) -- (a4);

    \path[shape=coordinate]
        (0,0) coordinate(b1) (1,0) coordinate(b2)
        (1,1) coordinate(b3) (0,1) coordinate(b4);
    \filldraw[fill=yellow!80!black] (b1) -- (b2) -- (b3) -- (b4);
\end{tikzpicture}
```

##### 17.2.3 Common Options: Separations, Margins, Padding and Border Rotation 常用选项：间隔、边距、填充和边框旋转

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|inner sep=&lt;*dimension*&gt;|no default, initially 0.3333em||
|inner xsep=&lt;*dimension*&gt;|no default, initially 0.3333em||
|inner ysep=&lt;*dimension*&gt;|no default, initially 0.3333em||
|outer sep=&lt;*dimension or “auto”*&gt;|no default||
|outer xsep=&lt;*dimension*&gt;|no default, initially 0.5\pgflinewidth||
|outer ysep=&lt;*dimension*&gt;|no default, initially 0.5\pgflinewidth||
|minimum height=&lt;*dimension*&gt;|no default, initially 1pt||
|minimum width=&lt;*dimension*&gt;|no default, initially 1pt||
|minimum size=&lt;*dimension*&gt;|no default||
|shape aspect=&lt;*aspect ratio*&gt;|no default||
|shape border uses incircle=&lt;*boolean*&gt;|default true||
|shape border rotate=&lt;*angle*&gt;|no default, initially 0||

- `inner sep=<dimension>`：将在形状内部文本和形状的背景路径之间添加 `<dimension>` 的附加（不可见）分隔空间。
    ```latex
    \begin{tikzpicture}
        \draw (0,0) node[inner sep=0pt,draw] {tight}
            (0cm,2em) node[inner sep=5pt,draw] {loose}
            (0cm,4em) node[fill=yellow!80!black] {default};
    \end{tikzpicture}
    ```
- `outer sep=<dimension>`：此选项在背景路径之外添加一个附加（不可见）分隔空间 `<dimension>`。
    ```latex
    \begin{tikzpicture}
        \draw[line width=5pt]
            (0,0) node[fill=yellow!80!black] (f) {filled}
            (2,0) node[draw] (d) {drawn}
            (1,-2) node[draw,scale=2] (s) {scaled};
        \draw[->] (1,-1) -- (f);
        \draw[->] (1,-1) -- (d);
        \draw[->] (1,-1) -- (s);
    \end{tikzpicture}
    ``` 
    ```latex
    \begin{tikzpicture}[outer sep=auto]
        \draw[line width=5pt]
            (0,0) node[fill=yellow!80!black] (f) {filled}
            (2,0) node[draw] (d) {drawn}
            (1,-2) node[draw,scale=2] (s) {scaled};
        \draw[->] (1,-1) -- (f);
        \draw[->] (1,-1) -- (d);
        \draw[->] (1,-1) -- (s);
    \end{tikzpicture}
    ```
- `minimum height=<dimension>`
    ```latex
    \begin{tikzpicture}
        \draw (0,0) node[minimum height=1cm,draw] {1cm}
            (2,0) node[minimum height=0cm,draw] {0cm};
        \draw (0,0) node[minimum height=2cm,minimum width=3cm,draw] {$3 \times 2$};
    \end{tikzpicture}
    ```
- `minimum size=<dimension>`
    ```latex
    \begin{tikzpicture}
        \draw (0,0) node[minimum size=2cm,draw] {square};
        \draw (0,-2) node[minimum size=2cm,draw,circle] {circle};
    \end{tikzpicture}
    ```
- `shape aspect=<aspect ratio>`
    ```latex
    \begin{tikzpicture}
        \draw (0,0) node[shape aspect=1,diamond,draw] {aspect 1};
        \draw (0,-2) node[shape aspect=2,diamond,draw] {aspect 2};
    \end{tikzpicture}
    ```
    ```latex
    \usetikzlibrary {shapes.geometric}
    \tikzset{every node/.style={dart, shape border uses incircle,
        inner sep=1pt, draw}}
    \tikz \node foreach \a/\b/\c in {A/0/0, B/45/0, C/0/45, D/45/45}
            [shape border rotate=\b, rotate=\c] at (\b/36,-\c/36) {\a};
    ```
    ```latex
    \usetikzlibrary {shapes.geometric}
    \tikzset{every node/.style={isosceles triangle, draw}}
    \begin{tikzpicture}
        \node {abc};
        \node [shape border uses incircle] at (2,0) {abc};
    \end{tikzpicture}
    ```
- `shape border rotate=<angle>`
    ```latex
    \usetikzlibrary {shapes.geometric}
    \tikzset{every node/.style={shape=trapezium, draw, shape border uses incircle}}
    \begin{tikzpicture}
        \node at (0,0) (A) {A};
        \node [shape border rotate=30] at (1.5,0) (B) {B};
        \foreach \s/\t in
            {left side/base east, bottom side/north, bottom left corner/base}{
                \fill[red] (A.\s) circle(1.5pt) (B.\s) circle(1.5pt);
                \fill[blue] (A.\t) circle(1.5pt) (B.\t) circle(1.5pt);
        }
    \end{tikzpicture}
    ```

#### 17.3 Multi-Part Nodes 多部分节点

`\nodepart[<options>]{<part name>}`

```latex
\usetikzlibrary {shapes.multipart}
\begin{tikzpicture}
    \node [circle split,draw,double,fill=red!20]
    {
        % No \nodepart has been used, yet. So, the following is put in the
        % ``text'' node part by default.
        $q_1$
        \nodepart{lower} % Ok, end ``text'' part, start ``output'' part
        $00$
    }; % output part ended.
\end{tikzpicture}
```

以下样式影响节点部分：

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|every &lt;*part name*&gt; node part|style, initially empty||

- `every <part name> node part`
    ```latex
    \usetikzlibrary {shapes.multipart}
    \tikz [every lower node part/.style={red}]
        \node [circle split,draw] {$q_1$ \nodepart{lower} $00$};
    ```

#### 17.4 The Node Text 节点文本

##### 17.4.1 Text Parameters: Color and Opacity 文本参数：颜色和透明度

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|text=&lt;*color*&gt;|no default||

- `text=<color>`
    ```latex
    \begin{tikzpicture}
        \draw[red] (0,0) -- +(1,1) node[above] {red};
        \draw[text=red] (1,0) -- +(1,1) node[above] {red};
        \draw (2,0) -- +(1,1) node[above,red] {red};
    \end{tikzpicture}
    ```

##### 17.4.2 Text Parameters: Font 文本参数：字体

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|node font=&lt;*font commands*&gt;|no default||
|font=&lt;*font commands*&gt;|no default||

- `node font=<font commands>`
    ```latex
    \begin{tikzpicture}
        \draw[node font=\itshape] (1,0) -- +(1,1) node[above] {italic};
    \end{tikzpicture}
    ```
    ```latex
    \tikz \node [node font=\tiny, minimum height=3em, draw] {tiny};
    \tikz \node [node font=\small, minimum height=3em, draw] {small};
    ```
- `font=<font commands>`
    ```latex
    \begin{tikzpicture}
        \node [font=\itshape] {italic};
    \end{tikzpicture}

    \tikz \node [font=\tiny, minimum height=3em, draw] {tiny};
    \tikz \node [font=\small, minimum height=3em, draw] {small};
    ```
    下面是如何使用 `font` 选项的一个有用示例：
    ```latex
    \usetikzlibrary {shapes.multipart}
    \tikz [every text node part/.style={font=\itshape},
        every lower node part/.style={font=\footnotesize}]
        \node [circle split,draw] {state \nodepart{lower} output};
    ```

##### 17.4.3 Text Parameters: Alignment and Width for Multi-Line Text 文本参数：多行文本的对齐方式和宽度

创建包含多行文本的节点有三种不同的方法：

1. 在节点内，可以放置一些标准环境，以生成多行对齐的文本。例如，可以在节点内使用 `{tabular}`：
    ```latex
    \tikz \node [draw] {
        \begin{tabular}{cc}
            upper left & upper right\\
            lower left & lower right
        \end{tabular}
    };
    ```
2. 在节点内使用 `\\` 标记行的结尾，然后请求 TikZ 以某种方式排列这些行。但是，只有在提供了 `align` 选项的情况下，才能执行此操作。
    ```latex
    \tikz[align=left] \node[draw] {This is a\\demonstration.};

    \tikz[align=center] \node[draw] {This is a\\demonstration.};
    ```
    `\\` 命令将可选的额外空间作为方括号中的参数。
    ```latex
    \tikz \node[fill=yellow!80!black,align=right]
        {This is a\\[-2pt] demonstration text for\\[1ex] alignments.};
    ```
3. 通过为节点指定固定的 `text width`，可以请求 TikZ 在节点内为您自动换行。在这种情况下，仍然可以使用 `\\` 进行强制换行。请注意，指定文本宽度时，节点将具有此宽度，而与文本是否实际“到达节点的末端”无关。

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|text width=&lt;*dimension*&gt;|no default||
|align=&lt;*alignment option*&gt;|no default|*left*, *flush left*, *right*, *flush right*, *center*, *flush center*, *justify*, *none*|
|node halign header=&lt;*macro storing a header*&gt;|no default, initially empty||

- `text width=<dimension>`
    ```latex
    \tikz \draw (0,0) node[fill=yellow!80!black,text width=3cm]
        {This is a demonstration text for showing how line breaking works.};
    ```
- `align=<alignment option>`：可以将 `<alignment option>` 设置为：`left`，`flush left`，`right`，`flush right`，`center`，`flush center`，`justify`，`none`。
- 

##### 17.4.4 Text Parameters: Height and Depth of Text 文本参数：文本的高度和深度

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|text height=&lt;*dimension*&gt;|no default||
|text depth=&lt;*dimension*&gt;|no default||

- `text height=<dimension>`
    ```latex
    \tikz \node[draw]                  {y};
    \tikz \node[draw,text height=10pt] {y};
    ```

#### 17.5 Positioning Nodes 定位节点

##### 17.5.1 Positioning Nodes Using Anchors 使用锚点定位节点

```latex
\tikz \draw           (0,0) node[anchor=north east] {first node}
            rectangle (1,1) node[anchor=west] {second node};
```

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|anchor=&lt;*anchor name*&gt;|no default|*center*, *base*, *mid*, *east*, *south*, *west*, *north*, *north east*, *north west*, *south east*, *south west*|

```latex
\begin{tikzpicture}[scale=3,transform shape]
    % First, center alignment -> wobbles
    \draw[anchor=center] (0,1)  node{x} -- (0.5,1)  node{y} -- (1,1)  node{t};
    % Second, base alignment -> no wobble, but too high
    \draw[anchor=base]   (0,.5) node{x} -- (0.5,.5) node{y} -- (1,.5) node{t};
    % Third, mid alignment
    \draw[anchor=mid]    (0,0)  node{x} -- (0.5,0)  node{y} -- (1,0)  node{t};
\end{tikzpicture}
```

##### 17.5.2 Basic Placement Options 基本放置选项

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|above=&lt;*offset*&gt;|default 0pt||
|below=&lt;*offset*&gt;|default 0pt||
|left=&lt;*offset*&gt;|default 0pt||
|right=&lt;*offset*&gt;|default 0pt||
|above left|no value||
|above right|no value||
|below left|no value||
|below right|no value||
|centered|no value||

- `above=<offset>`
    ```latex
    \tikz \fill (0,0) circle (2pt) node[above] {above};
    \tikz \fill (0,0) circle (2pt) node[above=2pt] {above};
    ```
- `above left`
    ```latex
    \tikz \fill (0,0) circle (2pt) node[above left] {above left};
    ```

##### 17.5.3 Advanced Placement Options 高级放置选项

**TikZ Library** `positioning`

`\usetikzlibrary{positioning}`

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|above=&lt;*specification*&gt;|default 0pt||
|on grid=&lt;*boolean*&gt;|no default, initially false||
|node distance=&lt;*shifting part*&gt;|no default, initially 1cm and 1cm||
|below=&lt;*specification*&gt;|no default||
|left=&lt;*specification*&gt;|no default||
|right=&lt;*specification*&gt;|no default||
|above left=&lt;*specification*&gt;|no default||
|below left=&lt;*specification*&gt;|no default||
|above left=&lt;*specification*&gt;|no default||
|above right=&lt;*specification*&gt;|no default||
|below right=&lt;*specification*&gt;|no default||
|base left=&lt;*specification*&gt;|no default||
|base right=&lt;*specification*&gt;|no default||
|mid left=&lt;*specification*&gt;|no default||
|mid right=&lt;*specification*&gt;|no default||

- `above=<specification>`
    ```latex
    \begin{tikzpicture}
        \draw[help lines] (0,0) grid (2,2);
        \node at (1,1) [above=2pt+3pt,draw] {above};
    \end{tikzpicture}
    ```
    ```latex
    \begin{tikzpicture}
        \draw[help lines] (0,0) grid (2,2);
        \node at (1,1) [above=.2,draw] {above};
        % south border of the node is now 2mm above (1,1)
    \end{tikzpicture}
    ```
    ```latex
    \usetikzlibrary {positioning}
    \begin{tikzpicture}
        \draw[help lines] (0,0) grid (2,2);
        \node at (1,1) [above=.2 and 3mm,draw] {above};
        % south border of the node is also 2mm above (1,1)
    \end{tikzpicture}
    ```
    ```latex
    \usetikzlibrary {positioning}
    \begin{tikzpicture}[every node/.style=draw]
        \draw[help lines] (0,0) grid (2,2);
        \node (somenode) at (1,1) {some node};

        \node [above=5mm of somenode.north east] {\tiny 5mm of somenode.north east};
        \node [above=1cm of somenode.north]      {\tiny 1cm of somenode.north};
    \end{tikzpicture}
    ```
    ```latex
    \usetikzlibrary {positioning}
    \begin{tikzpicture}[every node/.style=draw]
        \draw[help lines] (0,0) grid (2,2);
        \node (some node) at (1,1) {some node};

        \node (other node) [above=1cm of some node] {\tiny above=1cm of some node};

        \draw [<->] (some node.north) -- (other node.south)
                                        node [midway,right,draw=none] {1cm};
    \end{tikzpicture}
    ```
- `on grid=<boolean>`
    ```latex
    \usetikzlibrary {positioning}
    \begin{tikzpicture}[every node/.style=draw]
        \draw[help lines] (0,0) grid (2,3);

        % Not gridded
        \node (a1) at (0,0) {not gridded};
        \node (b1) [above=1cm of a1] {fooy};
        \node (c1) [above=1cm of b1] {a};

        % gridded
        \node (a2) at (2,0) {gridded};
        \node (b2) [on grid,above=1cm of a2] {fooy};
        \node (c2) [on grid,above=1cm of b2] {a};
    \end{tikzpicture}
    ```
- `node distance=<shifting part>`
    ```latex
    \usetikzlibrary {positioning}
    \begin{tikzpicture}[every node/.style=draw,node distance=5mm]
        \draw[help lines] (0,0) grid (2,3);

        % Not gridded
        \node (a1) at (0,0) {not gridded};
        \node (b1) [above=of a1] {fooy};
        \node (c1) [above=of b1] {a};

        % gridded
        \begin{scope}[on grid]
            \node (a2) at (2,0) {gridded};
            \node (b2) [above=of a2] {fooy};
            \node (c2) [above=of b2] {a};
        \end{scope}
    \end{tikzpicture}
    ```
- `above left=<specification>`
    ```latex
    \usetikzlibrary {positioning}
    \begin{tikzpicture}[every node/.style={draw,circle}]
    \draw[help lines] (0,0) grid (2,5);
    \begin{scope}[node distance=5mm and 5mm]
        \node (b) at (1,4) {b};
        \node [left=of b] {1};       \node [right=of b] {2};
        \node [above=of b] {3};      \node [below=of b] {4};
        \node [above left=of b] {5}; \node [above right=of b] {6};
        \node [below left=of b] {7}; \node [below right=of b] {8};
    \end{scope}
    \begin{scope}[node distance=5mm]
        \node (a) at (1,1) {a};
        \node [left=of a] {1};       \node [right=of a] {2};
        \node [above=of a] {3};      \node [below=of a] {4};
        \node [above left=of a] {5}; \node [above right=of a] {6};
        \node [below left=of a] {7}; \node [below right=of a] {8};
    \end{scope}
    \end{tikzpicture}
    ```
    ```latex
    \usetikzlibrary {positioning}
    \begin{tikzpicture}[every node/.style={draw,rectangle}]
    \draw[help lines] (0,0) grid (2,5);
    \begin{scope}[node distance=5mm and 5mm]
        \node (b) at (1,4) {b};
        \node [left=of b] {1};       \node [right=of b] {2};
        \node [above=of b] {3};      \node [below=of b] {4};
        \node [above left=of b] {5}; \node [above right=of b] {6};
        \node [below left=of b] {7}; \node [below right=of b] {8};
    \end{scope}
    \begin{scope}[node distance=5mm]
        \node (a) at (1,1) {a};
        \node [left=of a] {1};       \node [right=of a] {2};
        \node [above=of a] {3};      \node [below=of a] {4};
        \node [above left=of a] {5}; \node [above right=of a] {6};
        \node [below left=of a] {7}; \node [below right=of a] {8};
    \end{scope}
    \end{tikzpicture}
    ```
    ```latex
    \usetikzlibrary {positioning}
    \begin{tikzpicture}[every node/.style={draw,rectangle},on grid]
    \draw[help lines] (0,0) grid (4,4);
    \begin{scope}[node distance=1]
        \node (a) at (2,3) {a};
        \node [left=of a] {1};       \node [right=of a] {2};
        \node [above=of a] {3};      \node [below=of a] {4};
        \node [above left=of a] {5}; \node [above right=of a] {6};
        \node [below left=of a] {7}; \node [below right=of a] {8};
    \end{scope}
    \begin{scope}[node distance=1 and 1]
        \node (b) at (2,0) {b};
        \node [left=of b] {1};       \node [right=of b] {2};
        \node [above=of b] {3};      \node [below=of b] {4};
        \node [above left=of b] {5}; \node [above right=of b] {6};
        \node [below left=of b] {7}; \node [below right=of b] {8};
    \end{scope}
    \end{tikzpicture}
    ```
- `base right=<specification>`
    ```latex
    \usetikzlibrary {positioning}
    \begin{tikzpicture}[node distance=1ex]
        \draw[help lines] (0,0) grid (3,1);
        \huge
        \node (X) at (0,1)     {X};
        \node (a) [right=of X] {a};
        \node (y) [right=of a] {y};

        \node (X) at (0,0)          {X};
        \node (a) [base right=of X] {a};
        \node (y) [base right=of a] {y};
    \end{tikzpicture}
    ```

##### 17.5.4 Advanced Arrangements of Nodes 节点的高级排列

简单的 `above` 和 `right` 选项可能并不总是能满足安排大量节点的需要。对于这种情况，TikZ 提供了一些库，使定位更容易：`matrix` 库和 `graphdrawing` 库。这些用于定位节点的库在第 20 节和第 27 节分别描述。

#### 17.6 Fitting Nodes to a Set of Coordinates 将节点与一组坐标相匹配

### 40 Three Dimensional Drawing Library 3D绘图库

**TikZ Library** `3d`

`\usetikzlibrary{3d}`

#### 40.1 Coordinate Systems 坐标系

**Coordinate system** `xyz cylindrical`

|Keys (/tikz/cs/)|Types|Values|
|-----|-----|-----|
|angle=&lt;*degrees*&gt;|no default, initially `0`||
|radius=&lt;*number*&gt;|no default, initially `0`||
|z=&lt;*number*&gt;|no default, initially `0`||

```latex
\draw (0,0,0) -- (xyz cylindrical cs:radius=1);
\draw (0,0,0) -- (xyz cylindrical cs:radius=1,angle=90);
\draw (0,0,0) -- (xyz cylindrical cs:z=1);
```

**Coordinate system** `xyz spherical`

|Keys (/tikz/cs/)|Types|Values|
|-----|-----|-----|
|radius=&lt;*number*&gt;|no default, initially `0`||
|latitude=&lt;*degrees*&gt;|no default, initially `0`||
|longitude=&lt;*degrees*&gt;|no default, initially `0`||
|angle=&lt;*degrees*&gt;|no default, initially `0`||

```latex
\draw (0,0,0) -- (xyz spherical cs:radius=1);
\draw (0,0,0) -- (xyz spherical cs:radius=1,latitude=90);
\draw (0,0,0) -- (xyz spherical cs:radius=1,longitude=90);
```

#### 40.2 Coordinate Planes 坐标平面

##### 40.2.1 Switching to an arbitrary plane 切换到任意平面

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|plane origin=&lt;*point*&gt;|no default, initially `(0, 0)`||
|plane x=&lt;*point*&gt;|no default, initially `(1, 0)`||
|plane y=&lt;*point*&gt;|no default, initially `(0, 1)`||
|canvas is plane|no value||

```latex
\begin{tikzpicture}[
  plane x={(0.707,-0.707)},
  plane y={(0.707,0.707)},
  canvas is plane]
\end{tikzpicture}
```

##### 40.2.2 Predefined planes 预定义的平面

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|canvas is xy plane at z=&lt;*dimension*&gt;|no default||
|canvas is yx plane at z=&lt;*dimension*&gt;|no default||
|canvas is xz plane at y=&lt;*dimension*&gt;|no default||
|canvas is xz plane at y=&lt;*dimension*&gt;|no default||
|canvas is yz plane at y=&lt;*dimension*&gt;|no default||
|canvas is zy plane at y=&lt;*dimension*&gt;|no default||

```latex
\begin{scope}[canvas is zy plane at x=0]
\end{scope}
```

### 45 Background Library 背景库

**TikZ Library** `backgrounds`

`\usetikzlibrary{backgrounds}`

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|on background layer=&lt;*options*&gt;|no default||
|every on background layer|style, no value||
|show background rectangle|style, no value||
|inner frame xsep=&lt;*dimension*&gt;|no default, initially *1ex*||
|inner frame ysep=&lt;*dimension*&gt;|no default, initially *1ex*||
|inner frame sep=&lt;*dimension*&gt;|no default, initially *1ex*||
|tight background|style, no value|fixed, *0pt*|
|loose background|style, no value|fixed, *2ex*|
|background rectangle|style, initially *draw*||
|framed|style, no value||
|show background grid|style, no value||
|background grid|style, initially *draw*, *help lines*||
|gridded|style, no value||
|show background top|style, no value||
|outer frame xsep=&lt;*dimension*&gt;|no default, initially *0pt*||
|outer frame ysep=&lt;*dimension*&gt;|no default, initially *0pt*||
|outer frame sep=&lt;*dimension*&gt;|no default||
|background top|style, initially *draw*||
|show background bottom|style, no value||
|show background left|style, no value||
|show background right|style, no value||

### 88 Repeating Things: The Foreach Statement 重复的事情：Foreach 语句

`\foreach <variables> [<options>] in <list> <commands>`

```latex
\foreach \x in {1,2,3,0} {[\x]}
等同于：
\def\mylist{1,2,3,0}
\foreach \x in \mylist {[\x]}
```

**Syntax for the commands. 命令的语法**

```latex
\foreach \x in {0,1,2,3}
  \draw (\x,0) circle (0.2cm);

\foreach \x in {0,1,2,3}
  \foreach \y in {0,1,2,3}
  {
    \draw (\x,\y) circle (0.2cm);
    \fill (\x,\y) circle (0.1cm);
  }
```

**The dots notation. 圆点标记。**

```latex
\foreach \x in {1,2,...,6} {\x, } yields 1, 2, 3, 4, 5, 6,
\foreach \x in {1,2,3,...,6} {\x, } yields 1, 2, 3, 4, 5, 6,
\foreach \x in {1,3,...,11} {\x, } yields 1, 3, 5, 7, 9, 11,
\foreach \x in {1,3,...,10} {\x, } yields 1, 3, 5, 7, 9,
\foreach \x in {0,0.1,...,0.5} {\x, } yields 0, 0.1, 0.20001, 0.30002, 0.40002,
\foreach \x in {a,b,9,8,...,1,2,2.125,...,2.5} {\x, } yields a, b, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2,
2.125, 2.25, 2.375, 2.5,

\foreach \x in {1,...,6} {\x, } yields 1, 2, 3, 4, 5, 6,
\foreach \x in {9,...,3.5} {\x, } yields 9, 8, 7, 6, 5, 4,

\foreach \x in {a,...,m} {\x, } yields a, b, c, d, e, f, g, h, i, j, k, l, m,
\foreach \x in {Z,X,...,M} {\x, } yields Z, X, V, T, R, P, N,

\foreach \x in {2^1,2^...,2^7} {$\x$, } yields 2^1, 2^2, 2^3, 2^4, 2^5, 2^6, 2^7,
\foreach \x in {0\pi,0.5\pi,...\pi,3\pi} {$\x$, } yields 0\pi, 0.5\pi, 1\pi, 1.5\pi, 2\pi, 2.5\pi, 3\pi,
\foreach \x in {A_1,..._1,H_1} {$\x$, } yields A_1, B_1, C_1, D_1, E_1, F_1, G_1, H_1,
```

**Special handling of pairs. 对的特殊处理。**

```latex
\foreach \position in {(0,0), (1,1), (2,0), (3,1)}
  \draw \position rectangle +(.25,.5);
```

**Using the foreach-statement inside paths. 在 paths 中使用 foreach 语句。**

```latex
\draw (0,0) \foreach \x in {1,...,3} { -- (\x,1) -- (\x,0) };
\draw foreach \p in {1,...,3} {(\p,1)--(\p,3) (1,\p)--(3,\p)};
```

**Multiple variables. 多个变量。**

```latex
\foreach \x / \y in {1/2,a/b} {``\x\ and \y''} yields “1 and 2”“a and b”.

\foreach \x/\xtext in {0,...,3,2.72 / e}
  \draw (\x,0) node{$\xtext$};

% Define some coordinates:
\path[nodes={circle,fill=yellow!80!black,draw}]
  (0,0) node(a) {a}
  (2,0.55) node(b) {b}
  (1,1.5) node(c) {c}
  (2,1.75) node(d) {d};
% Draw some connections:
\foreach \source/\target in {a/b, b/c, c/a, c/d}
  \draw (\source) .. controls +(.75cm,0pt) and +(-.75cm,0pt)..(\target);

\foreach \x / \y / \r in {0 / 0 / 2mm, 1 / 1 / 3mm, 2 / 0 / 1mm}
  \draw (\x,\y) circle (\r);
等同于：
\foreach \center/\r in {{(0,0)/2mm}, {(1,1)/3mm}, {(2,0)/1mm}}
  \draw[yshift=2.5cm] \center circle (\r);

\foreach \x / \cola in {0/red,1/green,2/blue,3/yellow}
  \foreach \y / \colb in {0/red,1/green,2/blue,3/yellow}
    \shade[ball color=\cola!50!\colb] (\x,\y) circle (0.4cm);
```

**Options to customize the foreach-statement. 自定义 foreach 语句的选项。**

|Keys (/pgf/foreach/)|Types|Values|
|-----|-----|-----|
|var=&lt;*variable*&gt;|no default||
|evaluate=&lt;*variable*&gt;|no default||
|evaluate=&lt;*variable*&gt; as &lt;*macro*&gt;|no default||
|evaluate=&lt;*variable*&gt; as &lt;*macro*&gt; using &lt;*formula*&gt;|no default||
|remember=&lt;*variable*&gt; as &lt;*macro*&gt;|no default||
|remember=&lt;*variable*&gt; as &lt;*macro*&gt; (initially &lt;*value*&gt;)|no default||
|count=&lt;*macro*&gt;|no default||
|count=&lt;*macro*&gt; from &lt;*value*&gt;|no default||
|parse={&lt;*boolean*&gt;}|default `false`||
|expand list={&lt;*boolean*&gt;}|default `false`||

```latex
\foreach \x [evaluate=\x] in {2^0,2^...,2^8}{$\x$, }
\foreach \x [evaluate=\x as \xeval] in {2^0,2^...,2^8}{$\x=\xeval$, }
\foreach \x [evaluate=\x as \shade using \x*10] in {0,1,...,10}
  \node [fill=red!\shade!yellow, minimum size=0.65cm] at (\x,0) {\x};

\foreach \x [remember=\x as \lastx (initially A)] in {B,...,H}{$\overrightarrow{\lastx\x}$, }

\foreach \x [count=\xi] in {a,...,e}
  \foreach \y [count=\yi] in {\x,...,e}
    \node [draw, top color=white, bottom color=blue!50, minimum size=0.666cm]
      at (\xi,-\yi) {$\mathstrut\x\y$};

\def\Iota#1#2{%
  \ifnum\numexpr#1\relax<\numexpr#2\relax
    \the\numexpr#1\relax,%
    \expandafter\Iota\expandafter{\the\numexpr(#1)+1\relax}{#2}%
  \else
    \the\numexpr#2\relax
  \fi}
\foreach [expand list=true] \x in {\Iota{1}{5}} {
  \x
}
```

**\breakforeach**

```latex
\foreach \x in {1,...,4}
  \foreach \y in {1,...,4}
    {
      \fill[red!50] (\x,\y) ellipse (3pt and 6pt);

      \ifnum \x<\y
        \breakforeach
      \fi
    }
```

### 69 Shadings Library 渐变填充库

**Tikz Library** `shadings`

`\usetikzlibrary{shadings}`

**Shading** `axis`

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|top color=&lt;*color*&gt;|no default||
|bottom color=&lt;*color*&gt;|no default||
|middle color=&lt;*color*&gt;|no default||
|left color=&lt;*color*&gt;|no default||
|right color=&lt;*color*&gt;|no default||

```latex
\usepgflibrary {shadings}
\draw[top color=red] (0,0) rectangle (2,1);
\draw[top color=white,bottom color=black,middle color=red] (0,0) rectangle (2,1);
```

**Shading** `ball`

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|ball color=&lt;*color*&gt;|no default||

```latex
\usepgflibrary {shadings}
\shade[ball color=white] (0,0) circle (2ex);
\shade[ball color=red] (1,0) circle (2ex);
\shade[ball color=black] (2,0) circle (2ex);
```

**Shading** `bilinear interpolation`

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|lower left=&lt;*color*&gt;|no default, initially `white`||
|upper left=&lt;*color*&gt;|no default, initially `white`||
|upper right=&lt;*color*&gt;|no default, initially `white`||
|lower right=&lt;*color*&gt;|no default, initially `white`||

```latex
\usepgflibrary {shadings}
\shade[upper left=red,upper right=green,
       lower left=blue,lower right=yellow]
    (0,0) rectangle (3,2);
```

**Shading** `color wheel`

```latex
\usepgflibrary {shadings}
\shade[shading=color wheel] (0,0) circle (1.5);

\shade[shading=color wheel] [even odd rule]
    (0,0) circle (1.5)
    (0,0) circle (1);
```

**Shading** `color wheel black center`

```latex
\usepgflibrary {shadings}
\shade[shading=color wheel black center] (0,0) circle (1.5);
```

**Shading** `color wheel white center`

```latex
\usepgflibrary {shadings}
\shade[shading=color wheel white center] (0,0) circle (1.5);
```

**Shading** `Mandelbrot set`

```latex
\usepgflibrary {shadings}
\shade[shading=Mandelbrot set] (0,0) rectangle (2,2);
```

**Shading** `radial`

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|inner color=&lt;*color*&gt;|no default||
|outer color=&lt;*color*&gt;|no default||

```latex
\usepgflibrary {shadings}
\draw[inner color=red] (0,0) rectangle (2,1);
\draw[outer color=red,inner color=white] (0,0) rectangle (2,1);
```

### 70 Shadows Library 阴影库

**TikZ Library** `shadows`

`\usetikzlibrary{shadows}`

#### 70.1 Overview 概述

#### 70.2 The General Shadow Option 一般阴影选项

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|general shadow=&lt;*shadow options*&gt;|default empty||
|shadow scale=&lt;*factor*&gt;|no default, initially *1*||
|shadow xshift=&lt;*dimension*&gt;|no default, initially *0pt*||
|shadow yshift=&lt;*dimension*&gt;|no default, initially *0pt*||

```latex
\usetikzlibrary {shadows}
\draw [general shadow={fill=red}] (0,0) circle (.5) (0.5,0) circle (.5);
\draw [general shadow={fill=red,shadow scale=1.25}]
    (0,0) circle (.5) (0.5,0) circle (.5);
\draw [general shadow={fill=red,shadow xshift=-5pt}]
    (0,0) circle (.5) (0.5,0) circle (.5);
```

#### 70.3 Shadows for Arbitrary Paths and Shapes 任意路径和形状的阴影

##### 70.3.1 Drop Shadows 下落阴影

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|drop shadow=&lt;*shadow options*&gt;|default empty||
|every shadow|style, initially empty||

```latex
\usetikzlibrary {shadows}
\filldraw [drop shadow,fill=white] (0,0) circle (.5) (0.5,0) circle (.5);
\filldraw [drop shadow={opacity=0.25},fill=white]
    (1,.5) circle (.5) (1.5,.5) circle (.5);
\begin{tikzpicture}[every shadow/.style={opacity=.8,fill=blue!50!black}]
    \filldraw [drop shadow,fill=white] (0,0) circle (.5) (0.5,0) circle (.5);
\end{tikzpicture}
```

##### 70.3.2 Copy Shadows 副本阴影

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|copy shadow=&lt;*shadow options*&gt;|default empty||
|double copy shadow=&lt;*shadow options*&gt;|default empty||

```latex
\usetikzlibrary {shadows,shapes.symbols}
\node at (0,-3) [copy shadow={left color=blue!50},left color=blue!50 draw=blue,thick]
    {Hello World!};
\node at (0,-2) [double copy shadow={opacity=.5},tape,fill=blue!20,draw=blue,thick]
    {Hello World!};
```

#### 70.4 Shadows for Special Paths and Nodes 特殊路径和节点的阴影

|Keys (/tikz/)|Types|Values|
|-----|-----|-----|
|circular drop shadow=&lt;*shadow options*&gt;|no default||
|circular glow=&lt;*shadow options*&gt;|no default||

```latex
\usetikzlibrary {shadows}
\foreach \i in {1,...,8}
    \node[circle,circular drop shadow,draw=blue,fill=blue!20,thick]
        at (\i*45:1) {Circle \i};
    \node[circle,circular glow={fill=white},fill=red!20,draw=red,thick]
        at (\i*45:1) {Circle \i};
```

### 87 Key Management 键管理

`\usepackage{pgfkeys}`

#### 87.1 Introduction 简介

##### 87.1.1 Comparison to Other Packages 与其它宏包比较

```latex
\pgfkeys{/my key=hallo,/your keys/main key=something\strange,
    key name without path=something else}

\pgfkeys{/my key/.code=The value is '#1'.}
\pgfkeys{/my key=hi!}

\pgfkeys{/my key/.code 2 args=The values are '#1' and '#2'.}
\pgfkeys{/my key={a1}{a2}}

\pgfkeys{/my key/.code=(#1)}
\pgfkeys{/my key/.default=hello}
\pgfkeys{/my key=hallo,/my key}

\pgfkeys{/tikz/.cd,line width=1cm,line cap=round}
\def\tikzset#1{\pgfkeys{/tikz/.cd,#1}}

\pgfkeys{/a/.code=(a:#1)}
\pgfkeys{/b/.code=(b:#1)}
\pgfkeys{/my style/.style={/a=foo,/b=bar,/a=#1}}
\pgfkeys{/my style=wow}

\pgfkeys{/tikz/.style=/tikz/.cd}
\pgfkeys{tikz,line width=1cm,draw=red}
```

### 94 Mathematical Expressions 数学表达式

### 113 Layered Graphics 分层图形

#### 113.1 Overview 概述

#### 113.2 Declaring Layers 声明图层

|Keys|Types|Values|
|-----|-----|-----|
|\pgfdeclarelayer{&lt;*name*&gt;}|||
|\pgfsetlayers{&lt;*layer list*&gt;}|||

```latex
\pgfdeclarelayer{background}
\pgfdeclarelayer{foreground}
\pgfsetlayers{background,main,foreground}
```

#### 113.3 Using Layers 使用图层

```latex
\begin{pgfonlayer}{<layer name>}
  <environment contents>
\end{pgfonlayer}

\pgfdeclarelayer{background layer}
\pgfdeclarelayer{foreground layer}
\pgfsetlayers{background layer,main,foreground layer}
\begin{tikzpicture}
  % On main layer:
  \fill[blue] (0,0) circle (1cm);
  \begin{pgfonlayer}{background layer}
  \fill[yellow] (-1,-1) rectangle (1,1);
  \end{pgfonlayer}
  \begin{pgfonlayer}{foreground layer}
  \node[white] {foreground};
  \end{pgfonlayer}
  \begin{pgfonlayer}{background layer}
  \fill[black] (-.8,-.8) rectangle (.8,.8);
  \end{pgfonlayer}
  % On main layer again:
  \fill[blue!50] (-.5,-1) rectangle (.5,1);
\end{tikzpicture}
```