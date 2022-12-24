import graphviz

# 生成多个 Gigraph 实例，存储在一个字典中，每个实例对应一张图片
dir_g = {}
dir_g['a_c'] = graphviz.Digraph(name='GrammarA_C')
for i in range(16):
    dir_g['c'+str(i)+'_f'] = graphviz.Digraph(name='GrammarC'+str(i)+'_F')

# 设置 Gigraph 属性
for dig in dir_g.keys():
    dir_g[dig].attr(rankdir='LR')
    dir_g[dig].attr(
        'node', shape='rect', fontname='Arial, SimHei', fontsize='14')

# 生成节点
list_A = ['A']
dir_g['a_c'].node('A', 'English Grammar\n英语语法')

list_B = ['B'+str(i) for i in range(3)]  # 列表解析
list_B_content = [
    'Parts of Speech\n词类', 'Inflection (Accidence)\n屈折变化 (词法)',
    'Syntax\n句法']
for i in range(3):
    dir_g['a_c'].node(list_B[i], list_B_content[i])

list_C = ['C'+str(i) for i in range(16)]
list_C_content = [
    'Nouns\n名词', 'Pronouns\n代词', 'Verbs\n动词', 'Adjectives\n形容词',
    'Adverbs\n副词', 'Prepositions\n介词', 'Conjunctions\n连接词 (连词)',
    'Other parts of speech\n其它词类', 'Conjugation\n动词的词形变化',
    'Declension\n词尾变化', 'Regular and Irregular Inflection\n规则和不规则屈折变化',
    'Subjects and Predicates\n主语和谓语', 'Modifiers\n修饰词', 'Phrases\n短语',
    'Clauses\n分句', 'Sentences\n句子']
for i in range(16):
    dir_g['a_c'].node(list_C[i], list_C_content[i])

# 生成边
for i in range(3):
    dir_g['a_c'].edge('A', 'B'+str(i))
for i in range(16):
    if i <= 7:
        dir_g['a_c'].edge('B0', 'C'+str(i))
    elif i <= 10:
        dir_g['a_c'].edge('B1', 'C'+str(i))
    else:
        dir_g['a_c'].edge('B2', 'C'+str(i))

dir_g['a_c'].render(
    directory='E:/Desktop/Codefield/Notebook/docs/programme'
    '/Python/Graphviz/')
