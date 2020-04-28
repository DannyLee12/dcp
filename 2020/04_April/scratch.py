
if __name__ == '__main__':
    poem = input("Enter your poem here: ")
    word_list = poem.split()
    print(word_list)
    length_list = len(word_list)
    new_word = ""
    for index in range(0, length_list):
        print(len(word_list[index]))
        print(word_list[index])
        if len(word_list[index]) <= 3:
            new_word = word_list.pop(index)
            word_list.append(new_word.lower())
        elif len(word_list[index]) >= 7:
            print(word_list[index])
            new_word = word_list.pop(index)
            word_list.append(new_word.upper())
    print(word_list)