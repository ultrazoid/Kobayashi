'''
Created on 22/03/2012

@author: ultrazoid_
'''
import random
import time
import datetime
import os
'''
path = "Logs"
paths = "/"+path
os.chdir(paths)
'''
vn = "1.3.2"
vp = "InDev"
version = vp, vn
version1 = "\n",vp,vn
now = datetime.datetime.now()
intro = "\nWelcome to: \nKobayashi "
intro1 = "Welcome to: \nKobayashi"
intro2 = "\nBy ultrazoid_\nType hi to start:"
intro3 = "\nBy ultrazoid_"
fod = now.strftime("%Y-%d-%m %H%M")
fon = fod+".txt"
fo = open(fon , 'a')

fo.write("KOBAYASHI LOG\n")
fo.write("Date: ")
fo.write(fod) 
fo.write(intro)
fo.write(vp)
fo.write(vn)
fo.write(intro2)
fo.write("\n")

print now.strftime("%Y-%d-%m %H%M")
print intro1,vp,vn,intro3

fc = open("greetings.txt",'r')
fg = fc.readlines()
greetings = []
nn=0
for line in fg:
    greetings.insert(nn,line)
    nn=nn+1
fc = open("hruForms.txt",'r')
fh = fc.readlines()
hruForms = []
nn=0
for line in fh:
    hruForms.insert(nn,line)
    nn=nn+1
fd = open("hruReplies1.txt",'r')
fhr1 = fd.readlines()
hruReplies1 = []
nn=0
for line in fhr1:
    hruReplies1.insert(nn,line)
    nn=nn+1
hruReplies2 = ["im good","i'm good","Im good","I'm good","i am good","I am good","good thanks","good thanx",
               "good thank you","good","Good","Good thanks","Good thanx","Good thank you","im good thanks","i'm good thanks",
               "Im good thanks","I'm good thanks","i am good thanks","I am good thanks","im good thanx",
               "i'm good thanx","Im good thanx","I'm good thanx","i am good thanx","I am good thanx",
               "im good thank you","i'm good thank you","Im good thank you","I'm good thank you",
               "i am good  thank you","I am good thank you","good"]
hrReplies = ["thats good","Thats good","that's good","That's good","thats good to hear","Thats good to hear",
             "that's good to hear","That's good to hear"]
thanks = ["thank you", "thanks","thanx","why thank you"]
thanksReplies = ["no problems","No problems","no worries","No worries","np","NP","nw","NW"]
smiles = [":D",":)",":P","=D","=)","=P"]
sReplies = ["but you used smilies","But you used smilies","but u used smilies","But u used smilies"]
yes = ["yes","Yes"]
times = ["what can you do","what can you do?", "What can you do","What can you do?"]
multiplyQ = ["Show me then","show me then","show me then","Show me then","show me","Show me",'Can you show me','can you show me']
unsure = ["lol","rofl","lmao","lmaoshtmtfoamsfo"]
end = ["quit","end"]
byes = ["bye","Bye","cya","See You","see you"]
that = [2*1,2*2,2*3,2*4,2*5,2*6,2*7,2*8,2*9,2*10,2*11,2*12]
kob = 'Kobayashi:'
sys = 'System:'

myString=raw_input("Type hi to start:")+'\n' #Asks for user to enter text

while myString != "end\n":
    fo.write("You:");fo.write(myString);fo.write("\n")
    if myString in greetings:
        a=greetings[random.randrange(0,len(greetings))]
        print kob,a
        fo.write(kob);fo.write(a)
        a=hruForms[random.randrange(0,len(hruForms))]
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString in hruForms:
        a=hruReplies2[random.randrange(0,len(hruForms))]
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
        a=hruReplies1[random.randrange(0,len(hruReplies1))]
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString in hruReplies1:
        a=hruReplies2[random.randrange(0,len(hruReplies2))]
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString in times:
        a="i know the 2 times-table"
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString=="multiply":
        a="Multiplying..."
        print kob,a
        fo.write(sys);fo.write(a);fo.write("\n")
        for multiple in that:
            a=multiple
            print multiple
            fo.write(sys);fo.write(a);fo.write("\n")
    elif myString in byes:
        a=byes[random.randrange(0,len(byes))]
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
        a="type end to end"
        print sys,a
        fo.write(sys);fo.write(a);fo.write("\n")
    elif myString in hruReplies2:
        a=hrReplies[random.randrange(0,len(hrReplies))]
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString in hrReplies:
        a=thanks[random.randrange(0,len(thanks))]
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString in thanks:
        a=thanksReplies[random.randrange(0,len(thanksReplies))]
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString in thanksReplies:
        a = smiles[random.randrange(0,len(smiles))]
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString in smiles:
        a="No need for smilies"
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString in sReplies:
        a="Are you calling me a Hypocrite?"
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString in yes:
        a="lol"
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString=="lol?":
        a="Yes, lol"
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString=="test.all\n":
        print sys,"Testing All Lists"
        print sys,greetings
        print sys,hruForms
        print sys,hruReplies1
        print sys,hruReplies2
        print sys,hrReplies
        print sys,thanks
        print sys,thanksReplies
        print sys,smiles
        print sys,sReplies
        print sys,yes
        print sys,times
        print sys,multiplyQ
        print sys,end
        print sys,byes
        print sys,that
    elif myString=="test.greetings":
        print sys,"Testing Greetings List"
        print sys,greetings
    elif myString=="bad":
        which=random.randrange(0,10)
        if which==0:
            a="is everything alright?"
            print kob,a
            fo.write(kob);fo.write(a);fo.write("\n")
        elif which==2:
            a="are you alright?"
            print kob,a
            fo.write(kob);fo.write(a);fo.write("\n")
        elif which==4:
            a=":( what's wrong?"
            print kob,a
            fo.write(kob);fo.write(a);fo.write("\n")
        elif which==6:
            a="what's wrong?"
            print kob,a
            fo.write(kob);fo.write(a);fo.write("\n")
        elif which==8:
            a="is it alright if I ask why?"
            print kob,a
            fo.write(kob);fo.write(a);fo.write("\n")
            myInput=raw_input("input:") #Asks for user to enter text
            if myInput in yes:
                a="sorry I won't ask then"
                print kob,a
                fo.write(kob);fo.write(a);fo.write("\n")
            else:
                a="what is wrong then?"
                print kob,a
                fo.write(kob);fo.write(a);fo.write("\n")
        elif which==10:
            a=":("
            print kob,a
            fo.write(kob);fo.write(a);fo.write("\n")
        else:
            a="sucks to be you"
            print kob,a
            fo.write(kob);fo.write(a);fo.write("\n")
    elif myString in multiplyQ:
        a=that
        print kob,that
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString=="":
        print kob,"Well aren't you interesting"
        fo.write(kob);fo.write(a);fo.write("\n")
    else:
        a=unsure[random.randrange(0,len(unsure))]
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    myString=raw_input("You:")+'\n' #Asks for user to enter text
fo.write("You:");fo.write(myString);fo.write("\n")
a="Ending..."
print sys,a
fo.write(sys);fo.write(a);fo.write("\n")
a="Saving Log"
print sys,a
fo.write(sys);fo.write(a);fo.write("\n")
fo.close()
time.sleep(3)





