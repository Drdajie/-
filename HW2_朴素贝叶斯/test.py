"""
测试部分
步骤：
    1_将多个类别的参数分别读入
    2_针对每个文档算出概率最高的类别
"""

import os
import math

CATE_NUM = 9

def get_parameters(voc_para_map):
    """ 得到类别和词汇的参数

    :param cat_para_list: P(ci)
    :param voc_para_map: P(w|c)，每个词汇对应 9 个类别的概率
    """
    # prepare
    files_path = os.listdir('./Parameter')

    for file_path in files_path:
        with open('./Parameter/'+file_path, 'r', encoding='ansi') as f:
            for key, line in zip(voc_para_map.keys(), f):
                voc_para_map[key].append(float(line.strip()))

def predict(cat_para_list, voc_para_map):
    category_name = ['财经', 'IT', '健康', '体育', '旅游', '教育', '招聘', '文化', '军事']
    prepath = './Segment_Data/test_dataset/'
    files_path = os.listdir(prepath)
    for f_path in files_path:
        with open(prepath + f_path, 'r', encoding='ansi') as f:
            line = f.read()
            temp_ans = []
            for i in range(CATE_NUM):
                temp_ans.append(math.log(cat_para_list[i]))
            for word in line.split(' '):
                if word in voc_para_map.keys():
                    for i in range(CATE_NUM):
                        temp_ans[i] += math.log(voc_para_map[word.strip()][i])
            max_index = 0
            max = temp_ans[0]
            for i, v in enumerate(temp_ans):
                if v > max:
                    max = v
                    max_index = i
            print(category_name[max_index])


if __name__ == '__main__':
    cat_para_list = [1/CATE_NUM] * CATE_NUM
    voc_para_map = {}
    with open('./new_vocabulary.txt', 'r', encoding='ansi') as f:
        for line in f:
            voc_para_map[line.strip()] = []
    
    get_parameters(voc_para_map)
    predict(cat_para_list, voc_para_map)