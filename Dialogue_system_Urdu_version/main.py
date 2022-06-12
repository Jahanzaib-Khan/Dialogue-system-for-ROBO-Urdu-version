from googletrans import Translator
tr = Translator()
out = tr.translate("How are you",dest="ur")
print(out.text)

