from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
import os
# inp = "Well, we'll debate that ... . . . test . .. .".split()
# result = st.tag(inp)
# print(inp)
# print(result)

data =[]
pathsave = './sentences/data_train_ner/'
pathload = 'C:/Users/dell/Desktop/package/ace2005_conll/'
# pathload = './sentences/data_train_ner/'
folders = os.listdir(pathload)
for folder in folders:
# folder = 'wl'
    filenames = os.listdir(pathload + folder+'/')
    dirs = []
    print('Number files: ', len(filenames))
    for file in filenames:
        # datas =[]
        with open(pathload +folder +'/' + file, encoding='utf-8') as f:
            lines = f.read().split('\n')
            data = [line.split('\t') for line in lines]
            feature = ''
            features = []
            # print(sentences)
            i = -1
            for word_tag in data:
                i += 1
                if word_tag[0] == '':
                    features.append(feature)
                    feature = ''
                    if len(features) == 4:
                        break
                    pass
                if len(features) < 3:
                    feature += word_tag[0]
                else:
                    feature += ' ' + word_tag[0]
            data = data[i + 1:]
            i = 0
            while i < len(data):
                if data[i][0] == '':
                    data.pop(i)
                    continue
                i += 1
        words = [word_tag[0] for word_tag in data]
        # print('--',len(words))#,words[390:400])
        result_ner = st.tag(words)
        i = 0
        while i < len(result_ner):
            if(result_ner[i][0] == '...'):
                result_ner[i]=('.','O')
                result_ner.insert(i+1,('.','O'))
                result_ner.insert(i+1,('.','O'))
                i+=2
                continue
            i+=1

        for i, word_ner in enumerate(result_ner):
            # if len(word_ner) ==1:
            #     print(sentences[i])
            (data[i]).append(word_ner[1][:3])
        print('--',len(result_ner),len(data))#,sentences[390:400])
        with open(pathsave + folder + '/' +file, 'w', encoding='utf-8') as f:
            for j,word_e_ner in enumerate(data):
                # if word_e_ner[0] != sentences[j][0]:
                #     print(j,sentences[j][0], word_e_ner[0], word_e_ner[1])
                for i, element in enumerate(word_e_ner):
                    if i==2:
                        f.write(element+'\n')
                    else:
                        f.write(element+'\t')

print('Xin chào các bạn')

print('Đây chỉ là file code demo')