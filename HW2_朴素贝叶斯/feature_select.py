"""
思路：特征提取过程 -> 计算每个词的 df -> 构造保留的词的词表
步骤：
    1_保存所有的停用词到列表 stop_words
    2_保存所有词汇进 map<string, int>
    3_遍历所有训练集文档（同时记录文档数量）
    4_遍历每个文档，该文档出现过的词汇（不在 stop_words）在 map 中 + 1
    5_排序，选出 5w 个存为新的词表。
    6_将不在词表中的词去除。
"""

import os

def get_stopwords():
    stop_path = './stoplis.txt'
    stop_words = []
    with open(stop_path, 'r', encoding='ansi') as stop_file:
        for word in stop_file:
            stop_words.append(word.strip())
    return stop_words

def get_vocabulary_dict():
    voc = {}
    voc_path = './Homework2/SegDict.TXT'
    with open(voc_path, 'r', encoding='ansi') as voc_file:
        for word in voc_file:
            voc[word.strip()] = 0
    return voc

def count_frequency(msi, stop_words):
    """
    统计 msi 中的词存在的文档个数
    """
    prepath = './Segment_Data/training_dataset/'
    first_paths = os.listdir(prepath)
    all_num = 0                     # 总文档数
    for first_dir in first_paths:
        second_paths = os.listdir(prepath+first_dir)
        for path in second_paths:
            with open(prepath+first_dir + '/' +path, 'r', encoding='ansi') as f:
                all_num += 1
                line = f.read()
                words = line.split(' ')
                temp_dict = {}
                for word in words:
                    if word not in stop_words:
                        temp_dict[word] = 1
                for item in temp_dict.items():
                    if msi.get(item[0], 0) != 0:
                        msi[item[0]] += item[1]


def dict_sort_delete(msi):
    """
    给 msi 根据 value 排序（逆序）
    并只保留前 5w 个词
    :return: msi[:50000]
    """
    msi = dict(sorted(msi.items(), key = lambda item:item[1]))
    return list(msi.keys())[0:50000]

def make_new_vocabulary(voc):
    with open('./new_vocabulary.txt', 'w', encoding='ansi') as f:
        for v in voc:
            f.write(v + '\n')


if __name__ == '__main__':
    stop_words = get_stopwords()
    msi = get_vocabulary_dict()
    count_frequency(msi, stop_words)
    voc = dict_sort_delete(msi)
    make_new_vocabulary(voc)