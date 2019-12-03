from hangman import Hangman
from guess import Guess
from word import Word

def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB()) #랜덤 단어 선택

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife() #목숨개수 초기화

    while guess.numTries < maxTries:
        # numTries는 추측 실패 횟수
        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()

        guessedChar = input('Select a letter: ')
        # 입력받은 문자열이 1개의 문자가 아닐 때
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        # 입력받은 문자가 이미 이전에 입력받은 것일 떄
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue
        # 입력받은 문자가 a~z가 아닐 때
        if guessedChar < 'a' or guessedChar > 'z':
            print('please enter a character between a and z')
            continue
        #전체 문자 맞추면 while문 break 하고 Success 프린트
        finished = guess.guess(guessedChar)
        if finished == True:
            break

    if finished == True:
        print()
        print(guess.secretWord)
        print('Success!')
        print('You win by trying', guess.numTries, 'Times')
    #허용된 횟수 내에 전체 문자 못 맞추면 hangman.text[0] 출력, 즉 목 매다는 그림 출력
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print()
        print('Fail')
        print("The word was", guess.secretWord)

if __name__ == '__main__':
    gameMain()
