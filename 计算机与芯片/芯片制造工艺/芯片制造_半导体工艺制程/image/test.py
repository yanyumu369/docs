from graphviz import Digraph

# 太过麻烦
# 改用 Latex

dot = Digraph(name="芯片制造—半导体工艺制程", comment="the test", format="png")
dot.attr(rankdir='LR')
dot.attr(
    'node', shape='rect', fontname='Arial, SimHei', fontsize='14')

# 生成图片节点，name：这个节点对象的名称，label:节点名，color：画节点的线的颜色
dot.node(name='A1', label='半导体工艺')

dot.node(name='B1', label='氧化')
dot.node(name='B2', label='图形化工艺')
dot.node(name='B2C1', label='曝光')
dot.node(name='B2C2', label='显影')

dot.node(name='B3', label='掺杂')
dot.node(name='B3C1', label='扩散')
dot.node(name='B3C2', label='离子注入')

dot.node(name='B4', label='薄膜沉积')
dot.node(name='B4C1', label='设备')
dot.node(name='B4C2', label='生长材料')

dot.node(name='B4C2D1', label='半导体')
dot.node(name='B4C2D1E1', label='外延硅（单晶硅）')
dot.node(name='B4C2D1E2', label='多晶硅或非晶硅')
dot.node(name='B4C2D1E3', label='砷化镓（GaAs）')

dot.node(name='B4C2D2', label='绝缘体')
dot.node(name='B4C2D2E1', label='二氧化硅（SiO2）')
dot.node(name='B4C2D2E2', label='氮化硅（SiN）')

dot.node(name='B4C2D3', label='导体')

dot.node(name='B5', label='金属化')

# 一次性画多条线
dot.edges(['cb', 'ac'])

dot.render(filename='MyPicture', directory=r"E:\Desktop\Notebook\docs\computer_science\IC_fabrication\芯片制造_半导体工艺制程\image", view=True)
