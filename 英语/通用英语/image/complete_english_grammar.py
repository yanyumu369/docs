import graphviz

a_c = graphviz.Digraph('GrammarA_C')
c1_f = graphviz.Digraph('GrammarC1_F')
c2_f = graphviz.Digraph('GrammarC2_F')
c3_f = graphviz.Digraph('GrammarC3_F')
c4_f = graphviz.Digraph('GrammarC4_F')
c5_f = graphviz.Digraph('GrammarC5_F')
c6_f = graphviz.Digraph('GrammarC6_F')
c7_f = graphviz.Digraph('GrammarC7_F')
c8_f = graphviz.Digraph('GrammarC8_F')
c9_f = graphviz.Digraph('GrammarC9_F')
c10_f = graphviz.Digraph('GrammarC10_F')
c11_f = graphviz.Digraph('GrammarC11_F')
c12_f = graphviz.Digraph('GrammarC12_F')
c13_f = graphviz.Digraph('GrammarC13_F')
c14_f = graphviz.Digraph('GrammarC14_F')
c15_f = graphviz.Digraph('GrammarC15_F')
c16_f = graphviz.Digraph('GrammarC16_F')

list1 = (a_c, c1_f, c2_f, c3_f, c4_f, c5_f, c6_f, c7_f, c8_f, c9_f,
         c10_f, c11_f, c12_f, c13_f, c14_f, c15_f, c16_f)

for i in list1:
    i.attr(rankdir='LR')
    i.attr('node', shape='rect', fontname='Helvetica, SimHei', fontsize='14')

a_c.node('A', 'English Grammar\n英语语法')
a_c.node('B1', 'Parts of Speech\n词类')
a_c.node('C1', 'Nouns\n名词')
a_c.node('C2', 'Pronouns\n代词')
a_c.node('C3', 'Verbs\n动词')
a_c.node('C4', 'Adjectives\n形容词')
a_c.node('C5', 'Adverbs\n副词')
a_c.node('C6', 'Prepositions\n介词')
a_c.node('C7', 'Conjunctions\n连接词（连词）')
a_c.node('C8', 'Other parts of speech\n其它词类')
a_c.node('B2', 'Inflection (Accidence)\n屈折变化（词法）')
a_c.node('C9', 'Conjugation\n动词的词形变化')
a_c.node('C10', 'Declension\n词尾变化')
a_c.node('C11', 'Regular and Irregular Inflection\n规则和不规则屈折变化')
a_c.node('B3', 'Syntax\n句法')
a_c.node('C12', 'Subjects and Predicates\n主语和谓语')
a_c.node('C13', 'Modifiers\n修饰词')
a_c.node('C14', 'Phrases\n短语')
a_c.node('C15', 'Clauses\n分句')
a_c.node('C16', 'Sentences\n句子')

a_c.edges(
    [('A', 'B1'), ('A', 'B2'), ('A', 'B3'), ('B1', 'C1'), ('B1', 'C2'),
     ('B1', 'C3'), ('B1', 'C4'), ('B1', 'C5'), ('B1', 'C6'), ('B1', 'C7'),
     ('B1', 'C8'), ('B2', 'C9'), ('B2', 'C10'), ('B2', 'C11'), ('B3', 'C12'),
     ('B3', 'C13'), ('B3', 'C14'), ('B3', 'C15'), ('B3', 'C16')])

c1_f.node('C1', 'Nouns\n名词')
c1_f.node('D1', 'Common and Proper Nouns\n普通名词和专有名词')
c1_f.node('D2', 'Nouns of Address\n称呼名词')
c1_f.node('D3', 'Concrete and Abstract Nouns\n具体名词和抽象名词')
c1_f.node('D4', 'Countable Nouns\n可数名词')
c1_f.node('D5', 'Uncountable Nouns\n不可数名词')
c1_f.node('D6', 'Collective Nouns\n集体名词')
c1_f.node('D7', 'Compound Nouns\n复合名词')
c1_f.node('D8', 'Nominalization (Creating Nouns)\n名词化（创造名词）')

c1_f.edges(
    [('C1', 'D1'), ('C1', 'D2'), ('C1', 'D3'), ('C1', 'D4'),
     ('C1', 'D5'), ('C1', 'D6'), ('C1', 'D7'), ('C1', 'D8')])

c2_f.node('C2', 'Pronouns\n代词')
c2_f.node('D9', 'Personal Pronouns\n人称代词')
c2_f.node('E1', 'Number\n数量')
c2_f.node('E2', 'Person\n人称')
c2_f.node('E3', 'Gender\n性')
c2_f.node('E4', 'Case\n格')
c2_f.node('E5', 'Reflexive Pronouns\n反身代词')
c2_f.node('D10', 'Intensive Pronouns\n强化代词')
c2_f.node('D11', 'Indefinite Pronouns\n不定代词')
c2_f.node('D12', 'Demonstrative Pronouns\n指示代词')
c2_f.node('D13', 'Interrogative Pronouns\n疑问代词')
c2_f.node('D14', 'Relative Pronouns\n关系代词')
c2_f.node('D15', 'Reciprocal Pronouns\n相互代词')
c2_f.node('D16', 'Dummy Pronouns\n虚拟代词')

c2_f.edges(
    [('C2', 'D9'), ('C2', 'D10'), ('C2', 'D11'), ('C2', 'D12'), ('C2', 'D13'),
     ('C2', 'D14'), ('C2', 'D15'), ('C2', 'D16'), ('D9', 'E1'), ('D9', 'E2'),
     ('D9', 'E3'), ('D9', 'E4'), ('D9', 'E5')])

c3_f.node('C3', 'Verbs\n动词')
c3_f.node('D17', 'Finite and Non-finite Verbs\n限定性动词和非限定性动词')
c3_f.node('D18', 'Transitive and Intransitive Verbs\n及物动词和不及物动词')
c3_f.node('D19', 'Regular and Irregular Verbs\n规则动词和不规则动词')
c3_f.node('D20', 'Auxiliary Verbs\n助动词')
c3_f.node('E6', 'Primary Auxiliary Verbs\n主要助动词')
c3_f.node('F1', 'Modal Auxiliary Verbs\n情态助动词')
c3_f.node('G1', 'Will')
c3_f.node('G2', 'Would')
c3_f.node('G3', 'Shall')
c3_f.node('G4', 'Should')
c3_f.node('G5', 'Can')
c3_f.node('G6', 'Could')
c3_f.node('G7', 'May')
c3_f.node('G8', 'Might')
c3_f.node('G9', 'Must')
c3_f.node('G10', 'Substituting Modal Verbs\n替换情态动词')
c3_f.node('E7', 'Semi-Modal Auxiliary Verbs\n半情态助动词')
c3_f.node('D21', 'Infinitives\n不定式')
c3_f.node('D22', 'Participles\n分词')
c3_f.node('D23', 'Action Verbs\n动作动词')
c3_f.node('D24', 'Stative Verbs\n状态动词')
c3_f.node('D25', 'Linking Verbs\n连系动词（系动词）')
c3_f.node('D26', 'Light Verbs\n轻动词')
c3_f.node('D27', 'Phrasal Verbs\n短语动词')
c3_f.node('E8', 'Common Phrasal Verbs\n常见短语动词')
c3_f.node('D28', 'Conditional Verbs\n使役动词')
c3_f.node('D29', 'Causative Verbs\n因果动词')
c3_f.node('D30', 'Factitive Verbs\n宾补动词')
c3_f.node('D31', 'Reflexive Verbs\n反身动词')

c3_f.edges(
    [('C3', 'D17'), ('C3', 'D18'), ('C3', 'D19'), ('C3', 'D20'), ('C3', 'D21'),
     ('C3', 'D22'), ('C3', 'D23'), ('C3', 'D24'), ('C3', 'D25'), ('C3', 'D26'),
     ('C3', 'D27'), ('C3', 'D28'), ('C3', 'D29'), ('C3', 'D30'), ('C3', 'D31'),
     ('D20', 'E6'), ('D20', 'E7'), ('D27', 'E8'), ('E6', 'F1'), ('F1', 'G1'),
     ('F1', 'G2'), ('F1', 'G3'), ('F1', 'G4'), ('F1', 'G5'), ('F1', 'G6'),
     ('F1', 'G7'), ('F1', 'G8'), ('F1', 'G9'), ('F1', 'G10')])


c4_f.node('C4', 'Adjectives\n形容词')
c4_f.node('D32', 'Attributive Adjectives\n定语形容词')
c4_f.node('D33', 'Predicative Adjectives\n表语形容词')
c4_f.node('D34', 'Proper Adjectives\n专有形容词')
c4_f.node('D35', 'Collective Adjectives\n集体形容词')
c4_f.node('D36', 'Demonstrative Adjectives\n指代形容词')
c4_f.node('D37', 'Interrogative Adjectives\n疑问形容词')
c4_f.node('D38', 'Nominal Adjectives\n名词性形容词')
c4_f.node('D39', 'Compound Adjectives\n复合形容词')
c4_f.node('D40', 'Order of Adjectives\n形容词的顺序')
c4_f.node('D41', 'Degrees of Comparison\n比较的程度')
c4_f.node('E9', 'Comparative Adjectives\n比较级形容词')
c4_f.node('E10', 'Superlative Adjectives\n最高级形容词')

c4_f.edges(
    [('C4', 'D32'), ('C4', 'D33'), ('C4', 'D34'), ('C4', 'D35'), ('C4', 'D36'),
     ('C4', 'D37'), ('C4', 'D38'), ('C4', 'D39'), ('C4', 'D40'), ('C4', 'D41'),
     ('D41', 'E9'), ('D41', 'E10')])
# c4_f.view()

c5_f.node('C5', 'Adverbs\n副词')
c5_f.node('D42', 'Adverbs of Time\n时间副词')
c5_f.node('D43', 'Adverbs of Place\n地点副词')
c5_f.node('D44', 'Adverbs of Degree\n程度副词')
c5_f.node('E11', 'Mitigators\n弱化')
c5_f.node('E12', 'Intensifiers\n强调')
c5_f.node('D45', 'Adverbs of Frequency\n频度副词')
c5_f.node('D46', 'Adverbs of Purpose\n目的副词')
c5_f.node('D47', 'Focusing Adverbs\n焦点副词')
c5_f.node('D48', 'Negative Adverbs\n否定副词')
c5_f.node('D49', 'Conjunctive Adverbs\n连接副词')
c5_f.node('D50', 'Evaluative Adverbs\n评价副词')
c5_f.node('D51', 'Viewpoint Adverbs\n观点副词')
c5_f.node('D52', 'Relative Adverbs\n关系副词')
c5_f.node('D53', 'Adverbial Nouns\n副词性名词（名词作状语）')
c5_f.node('D54', 'Regular and Irregular Adverbs\n规则副词和不规则副词')
c5_f.node('D55', 'Degrees of Comparison\n比较的程度')
c5_f.node('E13', 'Comparative Adverbs\n比较级副词')
c5_f.node('E14', 'Superlative Adverbs\n最高级副词')
c5_f.node('D56', 'Order of Adverbs\n副词的顺序')

c5_f.edges(
    [('C5', 'D42'), ('C5', 'D43'), ('C5', 'D44'), ('C5', 'D45'), ('C5', 'D46'),
     ('C5', 'D47'), ('C5', 'D48'), ('C5', 'D49'), ('C5', 'D50'), ('C5', 'D51'),
     ('C5', 'D52'), ('C5', 'D53'), ('C5', 'D54'), ('C5', 'D55'), ('C5', 'D56'),
     ('D44', 'E11'), ('D44', 'E12'), ('D55', 'E13'), ('D55', 'E14')])
# c5_f.view()

c6_f.node('C6', 'Prepositions\n介词')
c6_f.node('D57', 'Prepositional Phrases\n介词短语')
c6_f.node('D58', 'Categories of Prepositions\n介词的类别')
c6_f.node('D59', 'Common Prepositional Errors\n常见介词错误')
c6_f.node('D60', 'Prepositions with Nouns\n带名词的介词')
c6_f.node('D61', 'Prepositions with Verbs\n带动词的介词')
c6_f.node('D62', 'Prepositions with Adjectives\n带形容词的介词')
c6_f.node('D63', 'Prepositions in Idioms\n习语中的介词')
c6_f.node('E15', 'Idioms that Start with Prepositions\n以介词开头的习语')
c6_f.node('E16', 'Idioms that End with Prepositions\n以介词结尾的习语')
c6_f.node('D64', 'Dangling Prepositions\n悬垂介词')

c6_f.edges(
    [('C6', 'D57'), ('C6', 'D58'), ('C6', 'D59'), ('C6', 'D60'), ('C6', 'D61'),
     ('C6', 'D62'), ('C6', 'D63'), ('C6', 'D64'), ('D63', 'E15'),
     ('D63', 'E16')])
# c6_f.view()

c7_f.node('C7', 'Conjunctions\n连接词（连词）')
c7_f.node('D65', 'Coordinating Conjunctions\n并列连词')
c7_f.node('D66', 'Correlative Conjunctions\n关联连词')
c7_f.node('D67', 'Subordinating Conjunctions\n从属连词')

c7_f.edges(
    [('C7', 'D65'), ('C7', 'D66'), ('C7', 'D67')])
# c7_f.view()

c8_f.node('C8', 'Other parts of speech\n其它词类')
c8_f.node('D68', 'Particles\n虚词')
c8_f.node('D69', 'Articles\n冠词')
c8_f.node('D70', 'Determiners\n限定词')
c8_f.node('E17', 'Possessive Determiners\n物主限定词')
c8_f.node('D71', 'Gerunds\n动名词')
c8_f.node('E18', 'Gerunds as Objects of Verbs\n作为动词宾语的动名词')
c8_f.node('D72', 'Interjections\n感叹词')

c8_f.edges(
    [('C8', 'D68'), ('C8', 'D69'), ('C8', 'D70'), ('C8', 'D71'), ('C8', 'D72'),
     ('D70', 'E17'), ('D71', 'E18')])
# c8_f.view()

c9_f.node('C9', 'Conjugation\n动词的词形变化')
c9_f.node('D73', 'Tense\n时态')
c9_f.node('E19', 'Present Tense\n现在时')
c9_f.node('F2', 'Present Simple Tense\n一般现在时')
c9_f.node('F3', 'Present Continuous Tense (Progressive)\n现在进行时（渐进式）')
c9_f.node('F4', 'Present Perfect Tense\n现在完成时')
c9_f.node('F5', 'Present Perfect Continuous Tense\n现在完成进行时')
c9_f.node('E20', 'Past Tense\n过去时')
c9_f.node('F6', 'Past Simple Tense\n一般过去时')
c9_f.node('F7', 'Past Continuous Tense\n过去进行时')
c9_f.node('F8', 'Past Perfect Tense\n过去完成时')
c9_f.node('F9', 'Past Perfect Continuous Tense\n过去完成进行时')
c9_f.node('E21', 'Future Tense (Approximation)\n将来时')
c9_f.node('F10', 'Future Simple Tense\n一般将来时')
c9_f.node('F11', 'Future Continuous Tense\n将来进行时')
c9_f.node('F12', 'Future Perfect Tense\n将来完成时')
c9_f.node('F13', 'Future Perfect Continuous Tense\n将来完成进行时')
c9_f.node('D74', 'Aspect\n体')
c9_f.node('E22', 'Perfective and Imperfective Aspect\n完成和非完成的体')
c9_f.node('E23', 'Aspects of the Present Tense\n现在时的体')
c9_f.node('E24', 'Aspects of the Past Tense\n过去时的体')
c9_f.node('E25', 'Aspects of the Future Tense\n将来时的体')
c9_f.node('D75', 'Mood\n语气')
c9_f.node('E26', 'Indicative Mood\n陈述语气')
c9_f.node('F14', 'Subjunctive Mood\n虚拟语气')
c9_f.node('G11', 'Subjunctive Mood - Expressing Wishes\n虚拟语气 - 表达愿望')
c9_f.node('D76', 'Voice\n语态')
c9_f.node('E27', 'Active Voice\n主动语态')
c9_f.node('E28', 'Passive Voice\n被动语态')
c9_f.node('E29', 'Middle Voice\n中动语态')
c9_f.node('D77', 'Speech\n引语')
c9_f.node('E30', 'Reported Speech (Indirect Speech)\n间接引语')
c9_f.node('D78', 'Grammatical Person\n语法上的人称')

c9_f.edges(
    [('C9', 'D73'), ('C9', 'D74'), ('C9', 'D75'), ('C9', 'D76'), ('C9', 'D77'),
     ('C9', 'D78'), ('D73', 'E19'), ('D73', 'E20'), ('D73', 'E21'),
     ('D74', 'E22'), ('D74', 'E23'), ('D74', 'E24'), ('D74', 'E25'),
     ('D75', 'E26'), ('D76', 'E27'), ('D76', 'E28'), ('D76', 'E29'),
     ('D77', 'E30'), ('E19', 'F2'), ('E19', 'F3'), ('E19', 'F4'),
     ('E19', 'F5'), ('E20', 'F6'), ('E20', 'F7'), ('E20', 'F8'),
     ('E20', 'F9'), ('E21', 'F10'), ('E21', 'F11'), ('E21', 'F12'),
     ('E21', 'F13'), ('E26', 'F14'), ('F14', 'G11')])

c10_f.node('C10', 'Declension\n词尾变化')
c10_f.node('D79', 'Plurals\n复数')
c10_f.node('D80', 'Gender in Nouns\n名词中的性')

c10_f.edges(
    [('C10', 'D79'), ('C10', 'D80')])
c11_f.node('C11', 'Regular and Irregular Inflection\n规则和不规则屈折变化')

c12_f.node('C12', 'Subjects and Predicates\n主语和谓语')
c12_f.node('D81', 'The Subject\n主语')
c12_f.node('E31', 'The Predicate\n谓语')
c12_f.node('F15', 'Complements\n补足语')
c12_f.node('G12', 'Objects\n宾语')
c12_f.node('G13', 'Subject Complements\n主语补足语')
c12_f.node('G14', 'Object Complements\n宾语补足语')
c12_f.node('G15', 'Adjective Complements\n形容词补足语')
c12_f.node('G16', 'Adverbial Complements\n副词补足语')

c12_f.edges(
    [('C12', 'D81'), ('D81', 'E31'), ('E31', 'F15'), ('F15', 'G12'),
     ('F15', 'G13'), ('F15', 'G14'), ('F15', 'G15'), ('F15', 'G16')])

c13_f.node('C13', 'Modifiers\n修饰词')
c13_f.node('D82', 'Adjuncts\n修饰语')

c13_f.edges(
    [('C13', 'D82')])

c14_f.node('C14', 'Phrases\n短语')
c14_f.node('D83', 'Noun Phrases\n名词短语')
c14_f.node('D84', 'Adjective Phrases\n形容词短语')
c14_f.node('D85', 'Adverbial Phrases\n副词短语')
c14_f.node('D86', 'Participle Phrases\n分词短语')
c14_f.node('D87', 'Absolute Phrases\n绝对短语')
c14_f.node('D88', 'Appositives\n同位语')

c14_f.edges(
    [('C14', 'D83'), ('C14', 'D84'), ('C14', 'D85'), ('C14', 'D86'),
     ('C14', 'D87'), ('C14', 'D88')])

c15_f.node('C15', 'Clauses\n分句')
c15_f.node('D89', 'Independent Clauses\n独立分句')
c15_f.node('E32', 'Dependent Clauses\n从属分句（从句）')
c15_f.node('F16', 'Noun Clauses\n名词性从句')
c15_f.node('F17', 'Relative Clauses\n关系从句')
c15_f.node('F18', 'Adverbial Clauses\n副词性从句（状语从句）')

c15_f.edges(
    [('C15', 'D89'), ('D89', 'E32'), ('E32', 'F16'), ('E32', 'F17'),
     ('E32', 'F18')])

c16_f.node('C16', 'Sentences\n句子')
c16_f.node('D90', 'Compound Sentences\n复合句')
c16_f.node('D91', 'Complex Sentences\n复杂句')
c16_f.node('D92', 'Compound-Complex Sentences\n复合-复杂句')
c16_f.node('D93', 'Declarative Sentences\n陈述句')
c16_f.node('D94', 'Interrogative Sentences\n疑问句')
c16_f.node('D95', 'Negative Interrogative Sentences\n否定疑问句')
c16_f.node('D96', 'Imperative Sentences\n祈使句')
c16_f.node('D97', 'Conditional Sentences\n条件句')
c16_f.node('D98', 'Major and Minor Sentences '
           '(Regular and Irregular Sentences)\n大句和小句（规则句和不规则句）')

c16_f.edges(
    [('C16', 'D90'), ('C16', 'D91'), ('C16', 'D92'), ('C16', 'D93'),
     ('C16', 'D94'), ('C16', 'D95'), ('C16', 'D96'), ('C16', 'D97'),
     ('C16', 'D98')])

for i in list1:
    i.render(directory='E:/Desktop/Codefield/Notebook/docs/english/'
                       'general_english/image/')
