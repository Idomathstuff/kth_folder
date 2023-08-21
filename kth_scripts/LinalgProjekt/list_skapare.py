def list_one_word(txt):
    text_file = open(txt,'r', encoding='utf-8')
    text = text_file.read()
    text = text.lower()
    words = text.split()
    words = [word.strip('.,!;()[]"') for word in words]
    words = [word.strip("'") for word in words]
    words = [word.strip("\\") for word in words]
    words = [word.replace("'s", '') for word in words]

    return words  # the word list of txt file

def list_one_word_wdotcase(txt):
    text_file = open(txt,'r', encoding='utf-8')
    text = text_file.read()
    words = text.split()
    words = [word.strip(',!;()[]"') for word in words]
    words = [word.strip("'") for word in words]
    words = [word.strip("\\") for word in words]
    words = [word.replace("'s", '') for word in words]

    return words  # the word list of txt file

def list_two_words_wdotcase(txt):
    one_word_list = list_one_word_wdotcase(txt)
    return split_every_two_words(one_word_list)

def split_every_two_words(words):
    two_words_list =[]
    for i in range(0, len(words)-1):
        two_words_list.append(words[i] + " " +  words[i+1] + " ")
    return two_words_list
