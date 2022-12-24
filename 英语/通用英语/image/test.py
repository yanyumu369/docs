from graphviz import Digraph

dot = Digraph(name="芯片制造—半导体工艺制程", comment="the test", format="png")
dot.attr(rankdir='LR')
dot.attr(
    'node', shape='rect', fontname='Arial, SimHei', fontsize='14')

# 生成图片节点，name：这个节点对象的名称，label:节点名，color：画节点的线的颜色
dot.node(name='A1', label='Ming', color='green')
dot.node(name='B1', label='Hong', color='yellow')
dot.node(name='B2', label='Dong')

# 在节点之间画线，label：线上显示的文本，color:线的颜色
# dot.edge('a', 'b', label='', color='black')

# 一次性画多条线，c到b的线，a到c的线
dot.edges(['cb', 'ac'])

# 打印生成的源代码
# print(dot.source)

# 画图，filename:图片的名称，若无filename，则使用Digraph对象的name，默认会有gv后缀
# directory:图片保存的路径，默认是在当前路径下保存
# dot.view(filename="mypicture", directory="D:\MyTest")

# 跟view一样的用法(render跟view选择一个即可)，一般用render生成图片，不使用view=True,view=True用在调试的时候
# dot.render(filename='MyPicture', directory="D:\MyTest", view=True)

dot.render(filename='MyPicture', directory=r"E:\Desktop\Notebook\docs\english\general_english\image", view=True)
