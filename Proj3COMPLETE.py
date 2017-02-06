from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

import tkinter.filedialog

import pytesseract
from PIL import Image,ImageTk
from yandex_translate import YandexTranslate

import json

from gtts import gTTS

import os

translate = YandexTranslate('trnsl.1.1.20160427T215515Z.21fac82dc2654817.ea554fe0b9334eb8f3b4c6ae0379b3ceb8e99bd0')

root = Tk()
 
def showImg():
     load = Image.open('translatepic.png')
     render = ImageTk.PhotoImage(load)
 
     backroundimage = render
 
     img = Label(image=render)
 
     backroundlabel = Label
 
     img.image = backroundimage
     img.place(x=0,y=0)
 
     root.wm_geometry("822x462")
 
showImg()
 
 
root.title("Picture Translator")
root.geometry("822x462")
 
 
app = Frame(root)
app.grid()

#print('Translate Directions: ', translate.directions)

"""
TO REMOVE /N

replacing = translatedString.replace('[','').replace('\','').replace(']','')
newstring = replacing.replace(r'\n',"")

"""

def english():
     filename = filedialog.askopenfilename()
     extracted_text = pytesseract.image_to_string(Image.open(filename))
     print (extracted_text)
     
     orig_language = translate.detect(extracted_text)
     lang_conversions = orig_language + "-en"
     
     translation =  translate.translate(extracted_text, lang_conversions)
     soloText =  str(translation['text'])
     
     clean_translate = (soloText[2:])
     clean_translate = (clean_translate[:-2])

     clean_translate = clean_translate.replace(r'\n'," ")     
     print(clean_translate)
     
     tts = gTTS(text = clean_translate, lang = 'en')
     tts.save("testing.mp3")
     os.startfile('testing.mp3')

def spanish():
     filename = filedialog.askopenfilename()
     extracted_text = pytesseract.image_to_string(Image.open(filename))
     print (extracted_text)
     
     orig_language = translate.detect(extracted_text)
     lang_conversions = orig_language + "-es"
     
     translation =  translate.translate(extracted_text, lang_conversions)
     soloText =  str(translation['text'])
     
     clean_translate = (soloText[2:])
     clean_translate = (clean_translate[:-2])

     clean_translate = clean_translate.replace(r'\n'," ")     
     print(clean_translate)
     
     tts = gTTS(text = clean_translate, lang = 'es')
     tts.save("testing.mp3")
     os.startfile('testing.mp3')     

def french():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-fr"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'fr')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')
    
def russian():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-ru"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'ru')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def hungarian():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-hu"

     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'hu')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def danish():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-da"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'da')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def albanian():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-sq"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'sq')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')
    

def arabic():
     
     filename = filedialog.askopenfilename()
     extracted_text = pytesseract.image_to_string(Image.open(filename))
     print(extracted_text)
     
     orig_language = translate.detect(extracted_text)
     lang_conversions = orig_language + "-da"
     
     translation =  translate.translate(extracted_text, lang_conversions)
     soloText =  str(translation['text'])
     clean_translate = (soloText[2:])
     clean_translate = (clean_translate[:-2])
     clean_translate = clean_translate.replace(r'\n'," ")
     clean_translate = clean_translate.replace('\\','')
     print(clean_translate)

     tts = gTTS(text = clean_translate, lang = 'da')
     tts.save("testing.mp3")
     os.startfile('testing.mp3')


def armenian():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-hy"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'hy')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def afrikaans():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-af"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'af')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')


def dutch():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-nl"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'nl')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')


def greek():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-el"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'el')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def indonesian():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-id"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'id')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def italian():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-it"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'it')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')


def icelandic():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-is"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'is')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def chinese():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-zh"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'zh')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def korean():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-ko"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'ko')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def latin():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-la"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'la')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def latvian():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-lv"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'lv')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def macedonian():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-mk"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'mk')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def german():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-de"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'de')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def norwegian():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-no"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'no')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def polish():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-pl"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'pl')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def portuguese():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-pt"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'pt')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def romanian():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-ro"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'ro')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def serbian():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-sr"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'sr')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def slovakian():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-sk"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'sk')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def swahili():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-sw"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'sw')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def thai():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-th"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'th')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def turkish():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-tr"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'tr')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def vietnamese():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-vi"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'vi')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')

def welsh():
    filename = filedialog.askopenfilename()
    extracted_text = pytesseract.image_to_string(Image.open(filename))
    print(extracted_text)
     
    orig_language = translate.detect(extracted_text)
    lang_conversions = orig_language + "-cy"
     
    translation =  translate.translate(extracted_text, lang_conversions)
    soloText =  str(translation['text'])
    clean_translate = (soloText[2:])
    clean_translate = (clean_translate[:-2])
    clean_translate = clean_translate.replace(r'\n'," ")
    clean_translate = clean_translate.replace('\\','')
    print(clean_translate)

    tts = gTTS(text = clean_translate, lang = 'cy')
    tts.save("testing.mp3")
    os.startfile('testing.mp3')
     

def replay():
    os.startfile('testing.mp3')

albanianButton = Button(app, text = "Albanian", width=10, height=1,command=albanian)
albanianButton.grid(row=1,column=1)

arabicButton = Button(app, text = "Arabic", width=10, height=1,command=arabic)
arabicButton.grid(row=1,column=2)

armenianButton = Button(app, text = "Armenian", width=10, height=1,command=armenian)
armenianButton.grid(row=1,column=3)

afrikaansButton = Button(app, text = "Afrikaans", width=10, height=1,command=afrikaans)
afrikaansButton.grid(row=1,column=4)

dutchButton = Button(app, text = "Dutch", width=10, height=1,command=dutch)
dutchButton.grid(row=1,column=5)

danishButton = Button(app, text = "Danish", width=10, height=1,command=danish)
danishButton.grid(row=1,column=6)

frenchButton = Button(app, text = "French", width=10, height=1,command=french)
frenchButton.grid(row=1,column=7)

greekButton = Button(app, text = "Greek", width=10, height=1,command=greek)
greekButton.grid(row=1,column=8)

hungarianButton = Button(app, text = "Hungarian", width=10, height=1,command=hungarian)
hungarianButton.grid(row=1,column=9)

indonesianButton = Button(app, text = "Indonesian", width=10, height=1,command=indonesian)
indonesianButton.grid(row=1,column=10)

italianButton = Button(app, text = "Italian", width=10, height=1,command=italian)
italianButton.grid(row=2,column=1)

icelandicButton = Button(app, text = "Icelandic", width=10, height=1,command=icelandic)
icelandicButton.grid(row=2,column=2)

chineseButton = Button(app, text = "Chinese", width=10, height=1,command=chinese)
chineseButton.grid(row=2,column=3)

koreanButton = Button(app, text = "Korean", width=10, height=1,command=korean)
koreanButton.grid(row=2,column=4)

latinButton = Button(app, text = "Latin", width=10, height=1,command=latin)
latinButton.grid(row=2,column=5)

latvianButton = Button(app, text = "Latvian", width=10, height=1,command=latvian)
latvianButton.grid(row=2,column=6)

macedonianButton = Button(app, text = "Macedonian", width=10, height=1,command=macedonian)
macedonianButton.grid(row=2,column=7)

germanButton = Button(app, text = "German", width=10, height=1,command=german)
germanButton.grid(row=2,column=8)

norwegianButton = Button(app, text = "Norwegian", width=10, height=1,command=norwegian)
norwegianButton.grid(row=2,column=9)

polishButton = Button(app, text = "Polish", width=10, height=1,command=polish)
polishButton.grid(row=2,column=10)

portugueseButton = Button(app, text = "Portuguese", width=10, height=1,command=portuguese)
portugueseButton.grid(row=3,column=1)

romanianButton = Button(app, text = "Romanian", width=10, height=1,command=romanian)
romanianButton.grid(row=3,column=2)

russianButton = Button(app, text = "Russian", width=10, height=1,command=russian)
russianButton.grid(row=3,column=3)

serbianButton = Button(app, text = "Serbian", width=10, height=1,command=serbian)
serbianButton.grid(row=3,column=4)

slovakianButton = Button(app, text = "Slovakian", width=10, height=1,command=slovakian)
slovakianButton.grid(row=3,column=5)

spanishButton = Button(app, text = "Spanish", width=10, height=1,command=spanish)
spanishButton.grid(row=3,column=6)

swahiliButton = Button(app, text = "Swahili", width=10, height=1,command=swahili)
swahiliButton.grid(row=3,column=7)

thaiButton = Button(app, text = "Thai", width=10, height=1,command=thai)
thaiButton.grid(row=3,column=8)

turkishButton = Button(app, text = "Turkish", width=10, height=1,command=turkish)
turkishButton.grid(row=3,column=9)

vietnameseButton = Button(app, text = "Vietnamese", width=10, height=1,command=vietnamese)
vietnameseButton.grid(row=3,column=10)

welshButton = Button(app, text = "Welsh", width=10, height=1,command=welsh)
welshButton.grid(row=4,column=1)

englishButton = Button(app, text = "English", width=10, height=1,command=english)
englishButton.grid(row=4,column=2)


replayButton = Button(app, text = "Replay Audio", width = 10, height = 1, command = replay)
replayButton.grid(row = 5, column = 1)

 
root.mainloop()# your code goes here
