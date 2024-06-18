import time

import keyboard
import random
words=["Хорош", "ага", "понятно", "ааааааа", "что", "ромпомпом", "ну блин", "шиза", "первый бам", "жестко", "мощь", "мощный"]

time.sleep(3)
oldword="Хорош"
word="Хорош"
keyboard.write(word)
keyboard.press("enter")
time.sleep(5)
while True:
    otherlist=[]
    for element in words:
        if not element in otherlist:
            otherlist.append(element)
    otherlist.remove(oldword)
    word=random.choice(otherlist)
    oldword=word
    keyboard.write(word)
    keyboard.press("enter")
    print("Написано слово " + word)
    time.sleep(random.randint(15, 20))