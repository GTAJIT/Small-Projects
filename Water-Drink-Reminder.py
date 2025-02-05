import time, win32com.client as wincl
from notifypy import Notify

t = int(input("Gap Time in Sec: "))
name = input("Name: ")
cmt = input("Custom Msg: ")

speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name"))
spk.Voice
spk.SetVoice(vcs.Item(speaker_number))
spk.Speak(f"Hello, I'm {name}")
a = 1
while a > 0:
    notification = Notify()
    notification.title = "Challlo"
    notification.message = "Walking is important"
    notification.send()
    spk.speak (cmt)
    time.sleep(t)