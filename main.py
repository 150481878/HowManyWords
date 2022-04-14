import re


remain_list = []

def fileContent(file):
    '''读取文件，返回内容.
    file:文件地址'''
    f = open(file,'r')  #以r模式打开路径下的文件
    content = f.read()  #读取文件内容
    return content

def totalWords(file):
    '''统计文件内容的总字数'''
    content = fileContent(file)
    content = re.split('[,.!? - \n()]', content)  # 初步分割为单词
    split_symble = ['', ' ', '-', '--']  # 建立特殊字符列表，若为这些字符，则不统计
    remain_list = []  # 筛选后的列表，开始为空，满足条件后append到这里
    for i in content:
        if i not in split_symble:
            remain_list.append(i)
    return len(remain_list)

def everyWord(file):
    '''统计文件每个单词'''
    content = fileContent(file)
    content = re.split('[,.!? - \n()]', content)  # 初步分割为单词
    split_symble = ['', ' ', '-', '--']  # 建立特殊字符列表，若为这些字符，则不统计
    remain_list = []  # 筛选后的列表，开始为空，满足条件后append到这里
    for i in content:
        if i not in split_symble:
            remain_list.append(i)
    return remain_list

def totalUniqueWords(file):
    '''返回文件不重复的单词总数'''
    content = fileContent(file)
    content = re.split('[,.!? - \n()]', content)  # 初步分割为单词
    split_symble = ['', ' ', '-', '--']  # 建立特殊字符列表，若为这些字符，则不统计
    remain_list = []  # 筛选后的列表，开始为空，满足条件后append到这里
    for i in content:
        if i not in split_symble:
            remain_list.append(i)
    remain_list = list(set(remain_list)) #set去重
    return len(remain_list)

def everyUniqueWord(file):
    '''返回文件不重复的每个单词'''
    content = fileContent(file)
    content = re.split('[,.!? - \n()]', content)  # 初步分割为单词
    split_symble = ['', ' ', '-', '--']  # 建立特殊字符列表，若为这些字符，则不统计
    remain_list = []  # 筛选后的列表，开始为空，满足条件后append到这里
    for i in content:
        if i not in split_symble:
            remain_list.append(i)
    remain_list = list(set(remain_list)) #set去重
    return remain_list

def everyWordCount(file):
    '''统计文件中每个单词出现的次数'''
    remain_list = everyUniqueWord(file) #不重复的单词列表
    all_words_list = everyWord(file)  # 所有单词列表
    words_count_list = []
    for word in remain_list:
        if word not in words_count_list:
            words_count_list.append([word,0])# 定义每个单词出现次数的列表,初始值为1
    for word in all_words_list:
        for i in words_count_list:
            if word == i[0]:
                i[1] += 1
    return words_count_list

def maxWord(file):
    '''统计文件中出现次数最多的单词'''
    countList = everyWordCount(file) #文件中每个单词及其出现次数组成的列表
    numList = [] #定义一个存放单词出现次数的字典
    for i in countList:
        numList.append(i[1])
        numdic = dict(countList) #定义一个存放单词出现次数的字典
    maxCount = max(numList)
    # 根据字典的value反找字典的key
    max_word = list(numdic.keys())[list(numdic.values()).index(maxCount)]
    return max_word

print(everyWordCount('test.txt'))