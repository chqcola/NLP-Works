#足球比赛机器解说
#解说员
narrator = '''
narrate = 队员 动作 结果
队员 = 队伍 位置 号码 号
队伍 = 主队 | 客队
位置 = 门将 | 后卫 | 中场 | 前锋
号码 = 数字 | 数字 数字
数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
动作 = 传球 | 带球 | 射门 | 扑救
结果 = 失误 | 成功 | 得分 | 偏出
'''
#评论员
commentator = '''
comment = 事件 态度 比分
事件 = 配合 | 过人 | 进球 | 丢球
态度 = 程度 形容 ，
程度 = 非常 | 实在
形容 = 精彩 | 及时 | 倒霉 | 遗憾
比分 = 当前比分 主队 数字 ： 数字 客队
数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0
'''
def create_grammar(grammar_str, split='=', line_split='\n'):
    grammar = {}
    for line in grammar_str.split(line_split):
        if not line.strip(): continue
        exp, stmt = line.split(split)
        grammar[exp.strip()] = [s.split() for s in stmt.split('|')]
    return grammar

import random
choice = random.choice

def generate(gram, target):
    if target not in gram: return target
    expaned = [generate(gram, t) for t in choice(gram[target])]
    return ''.join([e if e != '/n' else '\n' for e in expaned if e != 'null'])

print(generate(gram=create_grammar(narrator),target='narrate'))
print(generate(gram=create_grammar(commentator),target='comment'),'\n')

def generate_n(gram,target,n):
    gram_n = [generate(gram,target) for i in range(n)]
    return '\n'.join(gram_n)
print(generate_n(gram=create_grammar(narrator),target='narrate',n=5))
print(generate_n(gram=create_grammar(commentator),target='comment',n=5))