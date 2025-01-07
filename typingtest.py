from time import time

prompt = "Set your minds on things that are above, not on things that are on earth. Colossians 3:2"


while True:
    start = time()
    print(prompt)
    response = input()

    if response == prompt:
        break
    else:
        print("incorrect, time restarted")
stop = time()


timespan = (stop - start) / 60
wordcount = len(prompt.split(" "))
print(f"{round(wordcount/timespan)} WPM")