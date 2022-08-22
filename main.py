
#TO DO: 
#    - Pasar todo el proyecto a POO.
#    - Agregar dificultad dependiendo de lo larga que sea la pablabra.


import random
import os
import time


def main(): 
    os.system('clear')
    print(inicio)
    print('1. Jugar\n2. Agregar palabra\n3. Seleccionar Dificultad\n4. Ver palabras')
    opcion = input()

    if opcion == '1':
        game()
    elif opcion == '2':
        os.system('clear')
        new_word = input('Introduzca la palabra que desea agregar al juego: ')
        assert len(new_word) > 2, 'La palabra tiene que tener un minimo de 3 letras.'
        add_word(new_word)
        print('La palabra a sido añadida con exito ✅')
        print('\nVolviendo al menu principal...')
        time.sleep(2)
        return main()
    elif opcion == '3':

        print('Proximamente...')
    elif opcion == '4':
        print('Proximamente...')
    else:
        print('Opcion no valida')


def set_difficult(num: str) -> str: # Agregar al main!
  
    with open('./archivos/words.txt', 'r', encoding='utf-8') as f:
        words = [word for word in f]
    
    for word in words:
        word.replace('\n','')

    easy = [word for word in words if len(word) <= 4] # Palabras hasta 4 letras
    normal = [word for word in words if len(word) > 4 and len(word) >= 8] # Palabras de 5 a 8 letras
    hard =  [word for word in words if len(word) > 8 ] # Palabras de 8 letras en adelante

    if num == '1': return easy
    if num == '2': return normal
    if num == '3': return hard
    else:
        return ('Opcion incorrecta')


def add_word(word: str):
    with open('./archivos/words.txt', 'a', encoding='utf-8') as f:
        f.write('\n' + word)
    

def get_word() -> list[str]:
    with open('./archivos/words.txt', 'r', encoding='utf-8') as f:
        words = [word for word in f]
    word = random.choice(words)
    word = word.replace('\n','')
    word = [letter for letter in word]
    return word


def get_replacement(user_input: str, word: list[str]
                    , hidden_word: list[str]) -> list[str]:
    """Reemplaza el input por el guion bajo en el index que corresponda y lo retorna.

    Args:
        user_input (str): Input del usuario
        word (list[str]): Palabra a adivinar
        hidden_word (list[str]): Palabra a adivinar pero con '_'

    """
    index = 0
    for char in word:
        if char == user_input:
            hidden_word[index] = user_input
        index = index + 1
    return hidden_word


def game():
    word_to_guess = get_word()
    
    hidden_word = len(word_to_guess) * '_'
    hidden_word = [char for char in hidden_word]

    lifes: int = 7
    game_status: bool = True

    while game_status:
        os.system('clear')

        #print(word_to_guess)
        
        print(inicio)
        print('\n\n\nBienvenido al juego del ahorcado.\n\n\nPalabra:', " ".join(hidden_word))  
        print('\nVidas: ' + (lifes * '♥ '))

        user_input = input('\nIngrese una letra: ')
        assert len(user_input) == 1, 'Debes ingresar solo una letra'

        # Compueba si el input esta en la palabra, si no esta resta vida.
        if word_to_guess.count(user_input) == 0: lifes = lifes - 1

        # Reemplaza los guiones bajos por el input en caso de que corresponda.
        get_replacement(user_input, word_to_guess, hidden_word)
        
        if hidden_word == word_to_guess: # Win
            game_status = False            
            os.system('clear')
            print(ganar)
            
    
        if lifes == 0: # Game over
            game_status = False
            os.system('clear')
            print(perder)
            print('La palabra era:', ' '.join(word_to_guess) + '\n\n')
            

        if lifes == 0 or game_status == False: # Final message 
            print('Presiona: \n\n\n1 para jugar de nuevo\n\n2 para volver al menu principal  \n\nCualquier otra tecla para salir.')
            option = input()
            if option == '1':
                game()
            elif option == '2':
                main()
            else:
                print('Gracias por jugar! 😎')


inicio = """
 Welcome to
  _   _                                            ____                       
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __    / ___| __ _ _ __ ___   ___  
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | |  _ / _` | '_ ` _ \ / _ \ 
 |  _  | (_| | | | | (_| | | | | | | (_| | | | | | |_| | (_| | | | | | |  __/ 
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  \____|\__,_|_| |_| |_|\___| 
                    |___/                                       by Lucasblazz
    """

ganar ='''
    
                ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
                ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
                ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
                ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
              ____ ____ _  _ ____ ____ ___ ____      /
              | __ |__| |\ | |__| [__   |  |___     / 
              |__] |  | | \| |  | ___]  |  |___    .  
    
    '''

perder = '''
$$$$$$\                            $$\ $$\             $$\                     $$\ 
$$  __$$\                           $$ |\__|            $$ |                    $$ |
$$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$$ |$$\  $$$$$$$\ $$$$$$\    $$$$$$\        $$ |
$$$$$$$  |$$  __$$\ $$  __$$\ $$  __$$ |$$ |$$  _____|\_$$  _|  $$  __$$\       $$ |
$$  ____/ $$$$$$$$ |$$ |  \__|$$ /  $$ |$$ |\$$$$$$\    $$ |    $$$$$$$$ |      \__|
$$ |      $$   ____|$$ |      $$ |  $$ |$$ | \____$$\   $$ |$$\ $$   ____|          
$$ |      \$$$$$$$\ $$ |      \$$$$$$$ |$$ |$$$$$$$  |  \$$$$  |\$$$$$$$\       $$\ 
\__|       \_______|\__|       \_______|\__|\_______/    \____/  \_______|      \__|
                                                                                                                         
    '''

if __name__ == '__main__':
    main()
    