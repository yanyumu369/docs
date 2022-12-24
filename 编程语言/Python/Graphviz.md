# Graphviz

1. GitHub：https://github.com/xflr6/graphviz
2. PyPI：https://pypi.org/project/graphviz/
3. 文档：https://graphviz.readthedocs.io
4. Graphviz：https://graphviz.org/

## 安装

`pip install graphviz`

## Pyreverse 结合 Graphviz 自动绘制 Python 类图

1. **安装 Pyreverse**（已集成于 `pylint` 模块中）：`pip install pylint`；
2. 将 Scripts 路径下的 pyreverse.exe（"C:\Users\xie\AppData\Roaming\Python\Python38\Scripts\pyreverse.exe"）添加到**环境变量**；
3. 检查安装是否完成：`pyreverse -h`；
4. 在 "C:\Users\xie\AppData\Roaming\Python\Python38\site-packages\" 路径下**打开终端**，并**执行命令** `pyreverse graphviz/`；
5. 在文件夹 graphviz 所在路径下得到新文件 **classes.dot**；
6. 继续执行命令 `dot -Tpdf classes.dot -o classes.pdf`，产生了类图 **classes.pdf**。
7. 由 Graphviz 的 `dot` 命令读取 classes.dot 文件可以修改 **classes.dot** 文件来改变输出的类图内容。

## dot 命令

### Principal Node Attributes 主要的节点属性

| Name         | Default             | Values                                                             |
| ------------ | ------------------- | ------------------------------------------------------------------ |
| color        | `black`             | node shape color                                                   |
| colorscheme  | X11                 | scheme for interpreting color names                                |
| comment      |                     | any string (format-dependent)                                      |
| distortion   | `0.0`               | node distortion for `shape=polygon`                                |
| fillcolor    | `lightgrey`/`black` | node fill color                                                    |
| fixedsize    | false               | label text has no affect on node size                              |
| fontcolor    | `black`             | type face color                                                    |
| fontname     | `Times-Roman`       | font family                                                        |
| fontsize     | `14`                | point size of label                                                |
| group        |                     | name of node’s horizontal alignment group                          |
| height       | `.5`                | minimum height in inches                                           |
| id           |                     | any string (user-defined output object tags)                       |
| image        |                     | image file name                                                    |
| imagescale   | false               | true, width, height, both                                          |
| label        | node name           | any string                                                         |
| labelloc     | c                   | node label vertical alignment                                      |
| layer        | overlay range       | `all`, _id_ or _id&colon;id_, or a comma-separated list of the former    |
| margin       |                     | 0.11,0.55 space around label                                       |
| nojustify    | false               | if true, justify to label, not node                                |
| orientation  | `0.0`               | node rotation angle                                                |
| penwidth     | 1.0                 | width of pen for drawing boundaries, in points                     |
| peripheries  | `shape-dependent`   | number of node boundaries                                          |
| regular      | false               | force polygon to be regular                                        |
| samplepoints | 8 or 20             | number vertices to convert circle or ellipse                       |
| shape        | `ellipse`           | node shape; see Section 2.1 and Appendix H                         |
| sides        | `4`                 | number of sides for `shape=polygon`                                |
| skew         | `0.0`               | skewing of node for `shape=polygon`                                |
| style        |                     | graphics options, e.g. `bold`, `dotted`, `filled`; cf. Section 2.4 |
| target       |                     | if URL is set, determines browser window for URL                   |
| tooltip      | label               | tooltip annotation                                                 |
| URL          |                     | URL associated with node (format-dependent)                        |
| width        | `.75`               | minimum width in inches                                            |

### Principal Edge Attributes 主要的边属性

| Name           | Default       | Values                                                                        |
| -------------- | ------------- | ----------------------------------------------------------------------------- |
| arrowhead      | normal        | style of arrowhead at head end                                                |
| arrowsize      | `1.0`         | scaling factor for arrowheads                                                 |
| arrowtail      | normal        | style of arrowhead at tail end                                                |
| color          | `black`       | edge stroke color                                                             |
| colorscheme    | X11           | scheme for interpreting color names                                           |
| comment        |               | any string (format-dependent)                                                 |
| constraint     | true          | use edge to affect node ranking                                               |
| decorate       |               | if set, draws a line connecting labels with their edges                       |
| dir            | `forward`     | `forward`, `back`, `both`, or `none`                                          |
| edgeURL        |               | URL attached to non-label part of edge                                        |
| edgehref       |               | synonym for edgeURL                                                           |
| edgetarget     |               | if URL is set, determines browser window for URL                              |
| edgetooltip    | label         | tooltip annotation for non-label part of edge                                 |
| fontcolor      | `black`       | type face color                                                               |
| fontname       | `Times-Roman` | font family                                                                   |
| fontsize       | `14`          | point size of label                                                           |
| headclip       | true          | if false, edge is not clipped to head node boundary                           |
| headherf       |               | synonym for headURL                                                           |
| headlabel      |               | label placed near head of edge                                                |
| headport       |               | `n`, `ne`, `e`, `se`, `s`, `sw`, `w`, `nw`                                    |
| headtarget     |               | if headURL is set, determines browser window for URL                          |
| headtooltip    | label         | tooltip annotation near head of edge                                          |
| headURL        |               | URL attached to head label                                                    |
| herf           |               | alias for URL                                                                 |
| id             |               | any string (user-defined output object tags)                                  |
| label          |               | edge label                                                                    |
| labelangle     | `-25.0`       | angle in degrees which head or tail label is rotated off edge                 |
| labeldistance  | `1.0`         | scaling factor for distance of head or tail label from node                   |
| labelfloat     | false         | lessen constraints on edge label placement                                    |
| labelfontcolor | `black`       | type face color for head and tail labels                                      |
| labelfontname  | `Times-Roman` | font family for head and tail labels                                          |
| labelfontsize  | `14`          | point size for head and tail labels                                           |
| labelhref      |               | synonym for labelURL                                                          |
| labelURL       |               | URL for label, overrides edge URL                                             |
| labeltarget    |               | if URL or labelURL is set, determines browser window for URL                  |
| labeltooltip   | label         | tooltip annotation near label                                                 |
| layer          | overlay range | `all`, _id_ or _id&colon;id_, or a comma-separated list of the former             |
| lhead          |               | name of cluster to use as head of edge                                        |
| ltail          |               | name of cluster to use as tail of edge                                        |
| minlen         | `1`           | minimum rank distance between head and tail                                   |
| penwidth       | 1.0           | width of pen for drawing edge stroke, in points                               |
| samehead       |               | tag for head node; edge heads with the same tag are merged onto the same port |
| sametail       |               | tag for head node; edge heads with the same tag are merged onto the same port |
| style          |               | graphics options, e.g. `bold`, `dotted`, `filled`; cf. Section 2.4            |
| tailclip       | true          | if false, edge is not clipped to tail node boundary                           |
| tailhref       |               | synonym for tailURL                                                           |
| taillabel      |               | label placed near tail of edge                                                |
| tailport       |               | `n`, `ne`, `e`, `se`, `s`, `sw`, `w`, `nw`                                    |
| tailtarget     |               | if tailURL is set, determines browser window for URL                          |
| tailtooltip    | label         | tooltip annotation near tail of edge                                          |
| tailURL        |               | URL attached to tail label                                                    |
| target         |               | if URL is set, determines browser window for URL                              |
| tooltip        | label         | tooltip annotation                                                            |
| weight         | `1`           | integer cost of stretching an edge                                            |

### Principal Graph Attributes 主要的图属性

| Name         | Default       | Values                                                                            |
| ------------ | ------------- | --------------------------------------------------------------------------------- |
| aspect       |               | controls aspect ratio adjustment                                                  |
| bgcolor      |               | background color for drawing, plus initial fill color                             |
| center       | false         | center drawing on `page`                                                          |
| clusterrank  | `local`       | may be `global` or `none`                                                         |
| color        | `black`       | for clusters, outline color, and fill color if `fillcolor` not defined            |
| colorscheme  | X11           | scheme for interpreting color names                                               |
| comment      |               | any string (format-dependent)                                                     |
| compound     | false         | allow edges between clusters                                                      |
| concentrate  | false         | enables edge concentrators                                                        |
| dpi          | 96            | dots per inch for image output                                                    |
| fillcolor    | `black`       | cluster fill color                                                                |
| fontcolor    | `black`       | type face color                                                                   |
| fontname     | `Times-Roman` | font family                                                                       |
| fontnames    |               | `svg`, `ps`, `gd` (SVG only)                                                      |
| fontpath     |               | list of directories to search for fonts                                           |
| fontsize     | `14`          | point size of label                                                               |
| id           |               | any string (user-defined output object tags)                                      |
| label        |               | any string                                                                        |
| labeljust    | centered      | ”l” and ”r” for left- and right-justified cluster labels, respectively            |
| labelloc     | top           | ”t” and ”b” for top- and bottom-justified cluster labels, respectively            |
| landscape    |               | if true, means orientation=landscape                                              |
| layers       |               | _id&colon;id&colon;id_...                                                         |
| layersep     | `:`           | specifies separator character to split `layers`                                   |
| margin       | `.5`          | margin included in `page`, inches                                                 |
| mindist      | `1.0`         | minimum separation between all nodes (not dot)                                    |
| nodesep      | `.25`         | separation between nodes, in inches.                                              |
| nojustify    | false         | if true, justify to label, not graph                                              |
| ordering     |               | if `out` out edge order is preserved                                              |
| orientation  | `portrait`    | if `rotate` is not used and the value is `landscape`, use landscape orientation   |
| outputorder  | breadthfirst  | or nodesfirst, edgesfirst                                                         |
| page         |               | unit of pagination, e.g. "`8.5,11`"                                               |
| pagedir      | `BL`          | traversal order of pages                                                          |
| pencolor     | black         | color for drawing cluster boundaries                                              |
| penwidth     | 1.0           | width of pen for drawing boundaries, in points                                    |
| peripheries  | 1             | number of cluster boundaries                                                      |
| rank         |               | `same`, `min`, `max`, `source` or `sink`                                          |
| rankdir      | `TB`          | `LR` (left to right) or `TB` (top to bottom)                                      |
| ranksep      | `.75`         | separation between ranks, in inches.                                              |
| ratio        |               | approximate aspect ratio desired, `fill` or `auto` minimization                   |
| rotate       |               | If 90, set orientation to landscape                                               |
| samplepoints | `8`           | number of points used to represent ellipses and circles on output (cf. Appendix F |
| searchsize   | `30`          | maximum edges with negative cut values to check when looking for a                |
| minimum      |               | one during network simplex                                                        |
| size         |               | maximum drawing size, in inches                                                   |
| splines      |               | draw edges as splines, polylines, lines                                           |
| style        |               | graphics options, e.g. `filled` for clusters                                      |
| stylesheet   |               | pathname or URL to XML style sheet for SVG                                        |
| target       |               | if URL is set, determines browser window for URL                                  |
| tooltip      | label         | tooltip annotation for cluster                                                    |
| truecolor    |               | if set, force 24 bit or indexed color in image output                             |
| viewport     |               | clipping window on output                                                         |
| URL          |               | URL associated with graph (format-dependent)                                      |

## 示例

### 官方示例

Examples：https://graphviz.readthedocs.io/en/stable/examples.html#hello-py

### 一个简单的有向图

<div align=center>
<img width="25%" src="programme\Python\Graphviz\MyPicture.png"/>
</div>

```python
from graphviz import Digraph

# 实例化一个 Digraph 对象（有向图），name:生成的图片的图片名，format:生成的图片格式
dot = Digraph(name="MyPicture", comment="the test", format="pdf")

# 生成图片节点，name：这个节点对象的名称，label:节点名，color：画节点的线的颜色
dot.node(name='a', label='Ming', color='green')
dot.node(name='b', label='Hong', color='yellow')
dot.node(name='c', label='Dong')

# 在节点之间画线，label：线上显示的文本，color:线的颜色
dot.edge('a', 'b', label="ab\na-b", color='red')
# 一次性画多条线，c 到 b 的线，a 到 c 的线
dot.edges(['cb', 'ac'])

# 打印生成的源代码
print(dot.source)

# 画图，filename:图片的名称，若无 filename，则使用 Digraph 对象的 name，默认会有 gv后缀
# directory:图片保存的路径，默认是在当前路径下保存
# dot.view(filename="mypicture", directory=r"docs\programme\Python\Graphviz")

# 跟 view 一样的用法（render 跟 view 选择一个即可），一般用 render 生成图片，不使用 ，
# view=True 用在调试的时候
dot.render(filename='MyPicture', directory=r"docs\programme\Python\Graphviz",
           view=True)

```