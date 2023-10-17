Vowels = "aeiou" #put all letters to search for in string without spaces together

def CountVowels(Text):
    Text = str.lower(Text)
    ReturnString = ""
    for Vowel in Vowels:
        VowelCount = 0
        for Char in Text:
            if Char == Vowel:
                VowelCount += 1

        ReturnString += Vowel+":"+str(VowelCount)+"  "

    return ReturnString


a = input()

print(CountVowels(a))



