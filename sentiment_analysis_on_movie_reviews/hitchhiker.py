import sys, random

def transform_train_data_to_liblinear(path):
    # Transform train data to train and test
    path_train = 'data_liblinear_train'
    path_train_train = 'data_liblinear_train_train'
    path_train_test = 'data_liblinear_train_test'
    file_train = open(path_train, 'w')
    file_train_train = open(path_train_train, 'w')
    file_train_test = open(path_train_test, 'w')
    random.seed()
    n_line = -1
    set_f = set([])
    for line in open(path):
        n_line += 1
        if n_line == 0:
            continue
        lst = line.strip('\n').split('\t')
        words = lst[2].split(' ')
        for w in words:
            if not w in set_f:
                set_f.add(w)
    d_index = {}
    sorted_set_f = sorted(list(set_f), key = lambda k : k)
    i = 1
    for f in sorted_set_f:
        d_index[f] = i
        i += 1

    n_line = -1
    for line in open(path):
        n_line += 1
        if n_line == 0:
            continue
        lst = line.strip('\n').split('\t')
        label = lst[-1]
        words = lst[2].split(' ')
        d = {}
        for w in words:
            d.setdefault(w, 0.0)
            d[w] += 1
        sort_words = sorted(list(set(words)), key = lambda k: k)
        #res = label + ' ' + ' '.join([str(d_index[key]) + ':' + str(d[key]) for key in sort_words]) + ' \n'
        res = label + ' ' + ' '.join([str(d_index[key]) + ':' + str(1) for key in sort_words]) + ' \n'
        file_train.write(res)
        if random.random() <= 0.7:
            file_train_train.write(res)
        else:
            file_train_test.write(res)
    file_train.close()
    file_train_train.close()
    file_train_test.close()

def transform_test_data_to_liblinear(path):
    # Transform test data to test and test
    path_test = 'data_liblinear_test'
    file_test = open(path_test, 'w')
    random.seed()
    n_line = -1
    set_f = set([])
    for line in open(path):
        n_line += 1
        if n_line == 0:
            continue
        lst = line.strip('\n').split('\t')
        words = lst[2].split(' ')
        for w in words:
            if not w in set_f:
                set_f.add(w)
    d_index = {}
    sorted_set_f = sorted(list(set_f), key = lambda k : k)
    i = 1
    for f in sorted_set_f:
        d_index[f] = i
        i += 1

    n_line = -1
    for line in open(path):
        n_line += 1
        if n_line == 0:
            continue
        lst = line.strip('\n').split('\t')
        label = '1'
        words = lst[2].split(' ')
        d = {}
        for w in words:
            d.setdefault(w, 0.0)
            d[w] += 1
        sort_words = sorted(list(set(words)), key = lambda k: k)
        #res = label + ' ' + ' '.join([str(d_index[key]) + ':' + str(d[key]) for key in sort_words]) + ' \n'
        res = label + ' ' + ' '.join([str(d_index[key]) + ':' + str(1) for key in sort_words]) + ' \n'
        file_test.write(res)
    file_test.close()

def test():
    path = 'heart_scale'
    for line in open(path):
        line = line.strip('\n')
        print line.split(' ')

def join_id_label():
    header = 'PhraseId,Sentiment'
    path_res = 'result.txt'
    file = open(path_res, 'w')
    path_test = 'test.tsv'
    path_score = 'data_liblinear_test.output'
    score = open(path_score).readlines()
    id = [ l.strip('\n').split('\t')[0] for l in open(path_test).readlines()[1:]]
    file.write(header + '\n')
    for i in range(len(score)):
        file.write(id[i] + ',' + score[i])
    file.close()

def statis_data():
    path = 'data_libsvm_train'
    d = {}
    Sum = 0.0
    for line in open(path):
        Sum += 1
        label = line.strip('\n').split(' ')[0]
        d.setdefault(label, 0)
        d[label] += 1
    
    for key in d.keys():
        print key, d[key], Sum / d[key]
if __name__ == '__main__':
    statis_data()
    #join_id_label()
    #transform_train_data_to_liblinear('train.tsv')
    #transform_test_data_to_liblinear('test.tsv')
