import itchat
import os
import random
from PIL import Image
import math
import re
from wordcloud import WordCloud
from matplotlib import pyplot as plt

def headImg():
    itchat.login()
    friends = itchat.get_friends(update=True)
    #print(friends)
    for count, f in enumerate(friends):
        img = itchat.get_head_img(userName=f["UserName"])
        imgFile = open("img/" + str(count) + ".jpg", "wb")
        imgFile.write(img)
        imgFile.close()

def createImg():
    x = 0
    y = 0
    imgs = os.listdir("img")
    random.shuffle(imgs)
    newImg = Image.new("RGB", (640, 640))
    width = int(math.sqrt(640 * 640 / len(imgs)))
    numLine = int(640 / width)
    for i in imgs:
        img = Image.open("img/" + i)
        img = img.resize((width, width), Image.ANTIALIAS)
        newImg.paste(img, (x * width, y * width))
        x += 1
        if x >= numLine:
            x = 0
            y += 1
        newImg.save("all.jpg")

def getSignature():
    itchat.login()
    friends = itchat.get_friends(update=True)
    file = open('Sign.txt', 'a', encoding='utf-8')
    for f in friends:
        signature = f["Signature"].strip().replace("emoji", "").replace("span", "").replace("class", "")
        rec = re.compile("1f\d+\w*|[<>/=]")
        signature = rec.sub("", signature)
        file.write(signature + "\n")

def create_word_cloud(filename):
    text = open("{}.txt".format(filename), encoding='utf-8').read()
    wc = WordCloud(
        background_color="white",
        max_words=2000,
        font_path='/System/Library/Fonts/PingFang.ttc',
        height=500,
        width=500,
        max_font_size=60,
        random_state=30,
    )
    myword = wc.generate(text)
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    wc.to_file('signature.png')

#headImg()
#createImg()
#getSignature()
create_word_cloud('sign')