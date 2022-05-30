import jieba
import os

def seg_file_words(inpath, outpath):
    file_names = os.listdir(inpath)
    for i, file_name in enumerate(file_names):
        file_in = open(inpath + file_name, 'r', encoding='ansi', errors='ignore')
        file_out = open(outpath + file_name, 'w', encoding='ansi')
        sentence = ''
        for line in file_in:
            seg_list = jieba.cut(line.strip())
            sentence += ' '.join(seg_list) + ' '
        file_out.write(sentence.strip())
        file_in.close()
        file_out.close()


if __name__ == '__main__':
    in_prepath = "./Homework2/Training Dataset/"
    paths = os.listdir(in_prepath)
    out_prepaht = "./Segment_Data/training_dataset/"

    for path in paths:
        seg_file_words(in_prepath+path+'/', out_prepaht+path+'/')

    in_prepath = "./Homework2/Test Dataset/"
    out_prepaht = "./Segment_Data/test_dataset/"
    seg_file_words(in_prepath, out_prepaht)