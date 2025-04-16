from operator import itemgetter
def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_of_char(text):
    words = text.split()
    letter_dic = {}
    for word in words:
        for char in word: 
            lower_case_char = char.lower()
            if lower_case_char not in letter_dic:
                letter_dic[lower_case_char] = 1
            else:
                letter_dic[lower_case_char] += 1
    return letter_dic

def sort_dic_of_chars(dic_of_chars):
    
    list_info_chars = []
    for char in dic_of_chars:
        list_info_chars.append({
            "char" : char,
            "count" : dic_of_chars[char]
        })
    list_info_chars.sort(key=itemgetter('count'), reverse=True)
    return list_info_chars