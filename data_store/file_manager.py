

def file_reader(filename):
    with open(filename) as article:
        text = article.read()
        print(text)


file_reader()