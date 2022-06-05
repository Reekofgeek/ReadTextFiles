# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        file = f.read()
        f.close()
        return file

read_file_content('./story.txt')    

def count_words():
    text = read_file_content("./story.txt").strip()
    # [assignment] Add your code here
    words= text.split(" ")
    count = {}
    for string in words:
        if (string in count):
            count[string] += 1
        else:
            count[string] = 1
    return count

print(count_words())
