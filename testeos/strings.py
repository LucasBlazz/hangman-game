def main():
    
    word_list = ['o','j','o','t','a']
    
    hidden_word_list = ['_','_','_','_','_']
    
    user_input = input()
    lifes = 6
    index = 0
    
    for char in word_list:
        if char == user_input:
            hidden_word_list[index] = user_input
        index = index + 1

    print(hidden_word_list)
    
    # .find() retorna '-1' si no encuentra la letra en el string 
    '''if word.find(user_input) == -1:
        lifes = lifes -1'''


if __name__ == '__main__':
    main()
    