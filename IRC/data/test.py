import codecs
import json

def merge_db(src_1,src_2,tgt):
    with codecs.open(src_1, 'r' ,encoding='utf-8') as s1, codecs.open(src_2, 'r', encoding='utf-8') as s2, codecs.open(tgt, 'w', encoding='utf-8') as t:
        jsons_1 = json.load(s1)
        jsons_2 = json.load(s2)
        jsons = jsons_1 + jsons_2
        t.write(json.dumps(jsons))

def convert_dataset_format(path):
    temp = []
    with codecs.open(path, 'r', encoding='utf-8') as src:
        for line in src:
            line = line.strip()
            line = '<s> ' + line[3:]
            temp.append(line)
    with codecs.open(path, 'w', encoding='utf-8') as tgt:
        for line in temp:
            tgt.write(line + '\n')

def split_dataset(path):
    train_path = 'train.txt'
    dev_path = 'dev.txt'
    test_path = 'test.txt'

    temp = []
    with codecs.open(path, 'r', encoding='utf-8') as src:
        for line in src:
            line = line.strip()
            temp.append(line)

    train = temp[:-2400]
    dev = temp[-2400:-1200]
    test = temp[-1200:]

    with codecs.open(train_path, 'w', encoding='utf-8') as tgt:
        for line in train:
            tgt.write(line + '\n')
    with codecs.open(dev_path, 'w', encoding='utf-8') as tgt:
        for line in dev:
            tgt.write(line + '\n')
    with codecs.open(test_path, 'w', encoding='utf-8') as tgt:
        for line in test:
            tgt.write(line + '\n')

if __name__ == '__main__':
    # src_1 = 'db_wiki.txt'
    # src_2 = 'db_spider.txt'
    # tgt = 'db.txt'
    # merge_db(src_1,src_2,tgt)

    path = 'aug_data.txt'
    # convert_dataset_format(path)

    split_dataset(path)