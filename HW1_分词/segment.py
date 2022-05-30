# -*- coding=utf-8 -*-

max_len = 15

# 作为预处理，已运行过得到最大长度为 15，存在全局变量 max_len 中。
# def get_max_len(text):
#     """
#     得到词典中词的最大长度
#     :param text:
#     :return: max_len
#     """
#     max_len = 0
#     for word in text:
#         word = word.strip()
#         if(len(word) > max_len):
#             max_len = len(word)
#     return max_len

def str_process(text):
    """
    预处理，将文档中多余的空格去掉
    :param text:
    :return: 句子列表 -> temp_list
    """
    temp_list = []
    for sen in text.readlines():
        sen = sen.strip()
        temp_list.append(sen)
    return temp_list

def forward_segment(text, dic):
    """
    正向最大匹配算法
    1_得到每个句子
    2_从 max_len 开始匹配，无法匹配则长度减一直到能够匹配。
    :param text:
    :return: word_list -> 二维数组 -> 每句的分词独立存储
    """
    word_list = []
    for sen in text:
        temp_list = []      # 存储单句的分词结果
        sen = sen.strip()
        i = 0
        temp_len = max_len
        while i < len(sen):
            if(i + temp_len > len(sen)):            # i+temp_len 是右边界（不被包含）
                temp_len -= 1
                continue
            word = sen[i: i+temp_len]
            if word in dic or temp_len == 1:
                temp_list.append(word + ' ')
                i += temp_len
                temp_len = max_len
                continue
            temp_len -= 1
        word_list.append(temp_list)
    return word_list

def backward_segment(text, dic):
    word_list = []
    for sen in text:
        temp_list = []      # 存储单句的分词结果
        sen = sen.strip()
        i = len(sen)
        temp_len = max_len
        while i > 0:
            if(i - temp_len < 0):
                temp_len -= 1
                continue
            word = sen[i-temp_len: i]
            if word in dic or temp_len == 1:
                temp_list.append(word + ' ')
                i -= temp_len
                temp_len = max_len
                continue
            temp_len -= 1
        word_list.append(temp_list)
    return word_list

def count_single_num(sen):
    num = 0
    for word in sen:
        if len(word.strip()) == 1:
            num += 1
    return num


if __name__ == "__main__":
    input_file = "./测试样本.txt"
    dic_file = "./Dictionary.TXT"
    forward_output_file = "./Forward_Segment.txt"
    backward_output_file = "./Backward_Segment.txt"
    bidirect_output_file = "./Bidirect_Segment.txt"

    with open(dic_file, "r", encoding="utf-8") as dic, \
            open(input_file, "r", encoding="utf-8") as input:
        dic_list = str_process(dic)
        input_list = str_process(input)

    forward_word_list = forward_segment(input_list, dic_list)
    backward_word_list = backward_segment(input_list, dic_list)

    with open(forward_output_file, "w") as fw_output, \
            open(backward_output_file, "w") as bw_output, \
            open(bidirect_output_file, "w") as bi_output:
        for fw_sen, bw_sen in zip(forward_word_list, backward_word_list):
            bw_sen = bw_sen[::-1]
            if fw_sen:
                fw_output.writelines(fw_sen)
                fw_output.write('\n')
            if bw_sen:
                bw_output.writelines(bw_sen)
                bw_output.write('\n')
            if fw_sen and bw_sen:
                if len(bw_sen) < len(fw_sen):
                    bi_output.writelines(bw_sen)
                    bi_output.write('\n')
                elif len(bw_sen) > len(fw_sen):
                    bi_output.writelines(fw_sen)
                    bi_output.write('\n')
                else:
                    b = count_single_num(bw_sen)
                    f = count_single_num(fw_sen)
                    if b >= f:
                        bi_output.writelines(bw_sen)
                        bi_output.write('\n')
                    else:
                        bi_output.writelines(fw_sen)
                        bi_output.write('\n')
