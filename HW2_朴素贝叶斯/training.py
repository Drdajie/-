"""
训练
思路：
    训练过程是统计的过程：
    1. 统计每一类的文档数和总文档数 -> 存入 parameters.txt 中
    2. 针对每个类别统计 vocabulary 中各个词在对应类别文档中出现的次数（以及每个类别的总词数）
"""

import os

def get_vocabulary_info():
    """
    5w 个词汇针对每个类别分别得到对应的 P(w|c) -> 对应的存入类别对应的参数文件。
    步骤：
    1_得到词汇列表，初始化词汇字典
    2_统计该词汇在该类别下出现的次数，同时统计该类别下所有的词汇
    3_每统计完一个类别，将该类下的词汇参数存入对应文件。
    """
    # prepare
    def zero_map(msi):
        for key in msi.keys():
            msi[key] = 0
    voc_path = './new_vocabulary.txt'
    out_pathes = ['08.txt', '10.txt', '13.txt', '14.txt', '16.txt', '20.txt', '22.txt', '23.txt', '24.txt']
    voc_map = {}
    with open(voc_path, 'r', encoding='ansi') as f:
        for word in f:
            voc_map[word.strip()] = 0

    # process
    prepath = './Segment_Data/training_dataset/'
    classes_path = os.listdir(prepath)
    for i, c_path in enumerate(classes_path):
        files_path = os.listdir(prepath + c_path + '/')
        cat_voc_num = 0         # category vocabulary num
        for f_path in files_path:
            with open(prepath+c_path+'/'+f_path, 'r', encoding='ansi') as f:
                line = f.read()
                for word in line.split(' '):
                    if word in voc_map.keys():
                        voc_map[word.strip()] += 1
                        cat_voc_num += 1
        out_path = out_pathes[i]
        with open('./Parameter/'+out_path, 'w', encoding='ansi') as f:
            for item in voc_map.items():
                temp = (item[1]+1)/(cat_voc_num+50000)
                f.write(str(temp) + '\n')
        zero_map(voc_map)


if __name__ == '__main__':
    get_vocabulary_info()