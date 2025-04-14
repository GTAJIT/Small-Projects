import win32com.client as wincl 
list = [ "Jit", "Shreya", "Ananya"]
speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name"))
spk.Voice
spk.SetVoice(vcs.Item(speaker_number))
spk.Speak("Hello, I'm Zira")
for i in list:
    spk.Speak(f"Shout-out to {i}")