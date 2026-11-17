import time
import os
import winsound

folder_path = "audiotts/"

q = int(input("Is your pc \n1.Fast     2.Slow\n: "))
if q == 1:
    q = True
elif q == 2:
    q = False

# Get a list of all WAV files
wav_files = [file for file in os.listdir(folder_path) if file.endswith('.wav')]
for x in wav_files:
    wav_files[wav_files.index(x)] = x.replace(".wav","")

def PlayVoice(v,r):
    timedelay = 0.1
    winsound.PlaySound(folder_path + v + ".wav", winsound.SND_FILENAME)
    if r:
        time.sleep(timedelay)


while True:
    pls = input("Text: ").lower().replace("?", "")
    yes = pls.split(" ")
    for x in yes:
        if "," in x:
            yay = yes[:yes.index(x)]
            yay.extend([x.replace(",",""),","])
            yay.extend(yes[yes.index(x)+1:])
            yes = yay
        elif "." in x:
            yay = yes[:yes.index(x)]
            yay.extend([x.replace(".",""),"."])
            yay.extend(yes[yes.index(x)+1:])
            yes = yay

    for x in yes:

        # Comma and Full Stop
        if x == ",":
            time.sleep(0.5)
            continue
        elif x == ".":
            time.sleep(1)
            continue

        y = x.split("'")
        if x == "christmas":
            try:
                if yes[yes.index(x) +1] == "song":
                    PlayVoice("christmas song",q)
                    continue
            except:
                pass

        if x.endswith("s"):
            if x not in wav_files and x[:len(x)-1] in wav_files:
                PlayVoice(x[:len(x)-1],False)
                PlayVoice("s",q)
                continue
        if x.endswith("ing"):
            if x not in wav_files and x[:len(x)-3] in wav_files:
                PlayVoice(x[:len(x)-3], False)
                PlayVoice("ing",q)
                continue
            elif x not in wav_files and (x[:len(x)-3]+"e") in wav_files:
                PlayVoice(x[:len(x) - 3]+"e", False)
                PlayVoice("ing", q)
                continue

        if x in wav_files or y[0] in wav_files:
            if y[0] != x:
                PlayVoice(y[0],False)
                if y[1] == "d":
                    PlayVoice("would",q)
                elif y[1] == "m":
                    PlayVoice("am",q)
                elif y[1] == "s":
                    PlayVoice("s",q)
            else:
                PlayVoice(x,q)
        else:
            print(x,"not in sound library!")