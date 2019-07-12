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
import Auto_sentence_creater as ac,new_2_gram as ng
def generate_best(gram,target,n):
    sentences = ac.generate_n(ac.create_grammar(gram),target,n).split('\n')
    sentences_pro = [ng.get_probablity(s) for s in sentences]
    sentences_and_pro = [(sentences[i],sentences_pro[i]) for i in range(n)]
    sentences_and_pro = sorted(sentences_and_pro,key=lambda x: x[0],reverse=True)
    return 'In sentences(probability):\n{}\n\nThe most reasonable one is：\n{}'.format( '\n'.join(sentences),sentences_and_pro[0][0])
print(generate_best(narrator,'narrate',5))

#Q: 这个模型有什么问题？ 你准备如何提升？
#A: 问题是准确率并不高，需要完善语法或者更换适应性高的文本数据集