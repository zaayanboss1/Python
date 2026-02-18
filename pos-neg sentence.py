from textblob import TextBlob

print("welcome to the AI Mood detector !")
name=input("What's your name?")
print(f"Nice to meet you,{name}! let's find out the sentiment of your sentences.")
print("Type 'exit' to quit.\n")

while True:
    sentence = input("Your sentence:")
    if sentence.lower()==exit:
        print(f"Goodbye,{name}!")
        break
    blob=  TextBlob(sentence)
    sentiement = blob.sentiement.polarity
    if sentiement > 0:
        print("Positive sentiement detected!\n")
        elif sentiement<0:
            print("Negative sentiement detected!\n")
        else:
            print("Neutral sentiemnt detected!\n")