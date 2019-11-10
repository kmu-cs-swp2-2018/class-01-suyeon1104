class Guess:
    def __init__(self, word):
        self.secretWord = word
        self.numTries = 0  # 추측 실패 횟수
        self.guessedChars = set()  # 지금까지 추측한 글자들의 집합
        self.currentStatus = []  # 단어 중 맞춘 글자의 위치를 표시한 글자의 리스트
        for i in range(len(word)):
            self.currentStatus += ['_']

    def display(self):
        print("Current Status: ", self.currentStatus)
        print("Tries ", self.numTries)
        #print("word", self.secretWord)

    # 전체 단어를 완성했는지 여부를 리턴
    def guess(self, character):
        # 입력받은 charcter가 secretWord 안에 있는 글자면
        # guessedChars와 character를 합집합 연산
        # 그렇지 않으면 numTries 1 증가
        if character in self.secretWord:
            self.guessedChars |= {character}
        else:
            self.numTries += 1
        #character가 secretWord의 i번째에 있는 글자이면 currentStatus의 i번 째에 있는 글자에 character를 대입
        for i in range(len(self.secretWord)):
            if character == self.secretWord[i]:
                self.currentStatus[i] = character
        #currentStatus 안에 모든 글자가 채워졌는지(모든 글자를 맞추었는지)를 반환
        return '_' not in self.currentStatus

        #if list(self.secretWord) == self.currentStatus:
        #    return True
