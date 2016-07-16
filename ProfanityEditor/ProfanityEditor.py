shitty_words_file = open("swearWords.txt")
shitty_words = [line.replace("\r\n","") for line in shitty_words_file]

def read_text():
    quotes = open("movie.txt")
    contents_of_file = quotes.read()
    quotes.close()
    return contents_of_file

def check_profanity(text_to_check):
    text_to_check = text_to_check.replace("\r\n"," ")
    words = text_to_check.split(" ")
    for word in words:
        if(word in shitty_words):
            return "Oh, We have a swear word inside your file!"
    return "Your file is clear!"

content = read_text()
print check_profanity(content)
