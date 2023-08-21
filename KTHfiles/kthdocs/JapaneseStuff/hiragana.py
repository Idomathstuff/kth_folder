import random

class Hiragana:
    def __init__(self, h, r):
        self.h = h
        self.r = r

    def __str__(self):
        return self.h + ", " + self.r

    def __repr__(self):
        return str(self)

def drawHiragana():
    correct = 0
    for syllable in hiragana:
        print(syllable.r)
        input("Press enter to see the character...")
        print(syllable.h)
        if input("Were you correct? (y/n)") == "y":
            correct += 1
            print("Nice!")
        else:
            print("Better luck next time...")
        input()
    print("Finished. Your final score is", correct)
    input()



def tryHiragana():
    correct = 0
    for syllable in hiragana:
        print(syllable.h, "=" , end=" ")
        if input() == syllable.r:
            print("Correct!")
            correct += 1
        else:
            print("Wrong. The answer is", syllable.r)
        input()
    print("Finished. Your final score is", correct)
    input()

def tryRomaji():
    correct = 0
    for syllable in hiragana:
        correctChoice = random.randint(0,9)
        wrongChoices = []
        for i in range(10):
            if i == correctChoice:
                if i != 9:
                    print(str(i+1)+":", syllable.h, end=", ")
                else:
                    print(str(i+1)+":", syllable.h)
            else:
                wrongChoice = hiragana[random.randint(0, len(hiragana)-1)].h
                while wrongChoice in wrongChoices or wrongChoice == syllable.h:
                    wrongChoice = hiragana[random.randint(0, len(hiragana)-1)].h
                wrongChoices.append(wrongChoice)
                if i != 9:
                    print(str(i+1)+":", wrongChoice, end=", ")
                else:
                    print(str(i+1)+":", wrongChoice)

        print(syllable.r, "=", end=" ")
        reply = int(input())-1
        if reply == correctChoice:
            correct += 1
            print("Correct!")
        else:
            print("Wrong. The answer is", correctChoice+1)
        input()
    print("Finished. Your final score is", correct)
    input()

def main():
    while True:
        print("1. Hiragana -> Romaji",
        "2. Romaji -> Hiragana", "3. Draw Hiragana", "4. Quit", sep="\n")
        random.shuffle(hiragana)
        reply = input()
        if reply == "1":
            tryHiragana()
        if reply == "2":
            tryRomaji()
        if reply == "3":
            drawHiragana()
        elif reply == "4":
            break


if __name__ == '__main__':
    hiragana = [Hiragana("あ", "a"),
                Hiragana("い", "i"),
                Hiragana("う", "u"),
                Hiragana("え", "e"),
                Hiragana("お", "o"),
                Hiragana("か", "ka"),
                Hiragana("き", "ki"),
                Hiragana("く", "ku"),
                Hiragana("け", "ke"),
                Hiragana("こ", "ko"),
                Hiragana("さ", "sa"),
                Hiragana("し", "shi"),
                Hiragana("す", "su"),
                Hiragana("せ", "se"),
                Hiragana("そ", "so"),
                Hiragana("た", "ta"),
                Hiragana("ち", "chi"),
                Hiragana("つ", "tsu"),
                Hiragana("て", "te"),
                Hiragana("と", "to"),
                Hiragana("な", "na"),
                Hiragana("に", "ni"),
                Hiragana("ぬ", "nu"),
                Hiragana("ね", "ne"),
                Hiragana("の", "no"),
                Hiragana("は", "ha"),
                Hiragana("ひ", "hi"),
                Hiragana("ふ", "hu"),
                Hiragana("へ", "he"),
                Hiragana("ほ", "ho"),
                Hiragana("ま", "ma"),
                Hiragana("み", "mi"),
                Hiragana("む", "mu"),
                Hiragana("め", "me"),
                Hiragana("も", "mo"),
                Hiragana("や", "ya"),
                Hiragana("ゆ", "yu"),
                Hiragana("よ", "yo"),
                Hiragana("ら", "ra"),
                Hiragana("り", "ri"),
                Hiragana("る", "ru"),
                Hiragana("れ", "re"),
                Hiragana("ろ", "ro"),
                Hiragana("わ", "wa"),
                Hiragana("を", "wo"),
                Hiragana("ん", "n"),
                Hiragana("が", "ga"),
                Hiragana("ぎ", "gi"),
                Hiragana("ぐ", "gu"),
                Hiragana("げ", "ge"),
                Hiragana("ご", "go"),
                Hiragana("ざ", "za"),
                Hiragana("じ", "jis"),
                Hiragana("ず", "zus"),
                Hiragana("ぜ", "ze"),
                Hiragana("ぞ", "zo"),
                Hiragana("だ", "da"),
                Hiragana("ぢ", "jit"),
                Hiragana("づ", "zut"),
                Hiragana("で", "de"),
                Hiragana("ど", "do"),
                Hiragana("ば", "ba"),
                Hiragana("び", "bi"),
                Hiragana("ぶ", "bu"),
                Hiragana("べ", "be"),
                Hiragana("ぼ", "bo"),
                Hiragana("ぱ", "pa"),
                Hiragana("ぴ", "pi"),
                Hiragana("ぷ", "pu"),
                Hiragana("ぺ", "pe"),
                Hiragana("ぽ", "po")]
    main()
