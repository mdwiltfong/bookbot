def countLetters(word,dict):
    letters=list(word.lower())
    for letter in letters:
        if letter in dict:
            dict[letter]+=1
        else:
            dict[letter]=1
    return dict
def formatReport(dict,numberOfWords):
    dictToList=list(dict)
    dictToList.sort()
    print("--- Begin report of books/frankenstein.txt --- \n")
    print(f"{numberOfWords} words found in the document\n")
    for letter in dictToList:
        if letter.isalpha():
            print(f"The \'{letter}\' character was found {dict[letter]} times")
        else:
            pass
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words=file_contents.split()
    print(words.__len__())
    dict={}
    for word in words:
        dict=countLetters(word,dict)
    formatReport(dict,words.__len__())


