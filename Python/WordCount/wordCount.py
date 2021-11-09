def word_count():
    opening = open('Big file text.rtf')
    reading = opening.read()
    splitting = reading.split()
    print(len(splitting))
    opening.close()

def make_a_list():
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    openTheFile = open('readme.txt')
    fileString = openTheFile.read()
    for ele in fileString:
        if ele in punctuation:
            fileString = fileString.replace(ele, "")
            fileString = fileString.lower()
    newList = list(fileString.split(" "))
    print(newList)
    openTheFile.close()

word_count()
# make_a_list()