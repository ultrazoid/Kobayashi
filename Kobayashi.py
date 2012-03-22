'''
Created on 22/03/2012

@author: ultrazoid_
'''
import random
import time
import datetime
vn = "1.1"
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

fo.write("KOBAYASHI LOG")

fo.write(intro)
fo.write(vp)
fo.write(vn)
fo.write(intro2)
fo.write("\n")

print now.strftime("%Y-%d-%m %H%M")
print intro1,vp,vn,intro3
myString=raw_input("Type hi to start:") #Asks for user to enter text

greetings = ["hi","hello","Hello","Hi","gday","Gday","G'day","Bonjour","Hallo","Dia duit"]
hruForms = ["how are you", "hru","how r you","how are u","how r u"," How r you","How are you",]
hruReplies1 = ["and you","and u","And you","And u","Et toi","et toi"]
hruReplies2 = ["im good","i'm good","Im good","I'm good","i am good","I am good","good thanks","good thanx",
               "good thank you","good","Good","Good thanks","Good thanx","Good thank you","im good thanks","i'm good thanks",
               "Im good thanks","I'm good thanks","i am good thanks","I am good thanks","im good thanx",
               "i'm good thanx","Im good thanx","I'm good thanx","i am good thanx","I am good thanx",
               "im good thank you","i'm good thank you","Im good thank you","I'm good thank you",
               "i am good  thank you","I am good thank you"]
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

while myString != "end":
    fo.write(myString);fo.write("\n")
    if myString in greetings:
        a=greetings[random.randrange(0,10)]
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
        a=hruForms[random.randrange(0,2)]
        print kob,a
        fo.write(kob);fo.write(a);fo.write("\n")
    elif myString in hruForms:
        print kob,hruReplies2[random.randrange(0,30)]
        print kob,hruReplies1[random.randrange(0,6)]
    elif myString in hruReplies1:
        print kob,hruReplies2[random.randrange(0,30)]
    elif myString in times:
        print kob,"i know the 2 times-table"
    elif myString=="multiply":
        print kob,"Multiplying..."
        for multiple in that:
            print multiple
    elif myString in byes:
        print kob,byes[random.randrange(0,5)]
        print sys,"type end to end"
    elif myString in hruReplies2:
        print kob,hrReplies[random.randrange(0,8)]
    elif myString in hrReplies:
        print kob,thanks[random.randrange(0,4)]
    elif myString in thanks:
        print kob,thanksReplies[random.randrange(0,8)]
    elif myString in thanksReplies:
        print kob,smiles[random.randrange(0,6)]
        a = kob,smiles[random.randrange(0,6)]
    elif myString in smiles:
        print kob,"No need for smilies"
    elif myString in sReplies:
        print kob,"Are you calling me a Hypocrite?"
    elif myString in yes:
        print kob,"lol"
    elif myString=="lol?":
        print kob,"Yes, lol"
    elif myString=="test.all":
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
            print kob,"is everything alright?"
        elif which==2:
            print kob,"are you alright?"
        elif which==4:
            print kob,":( what's wrong?"
        elif which==6:
            print kob,"what's wrong?"
        elif which==8:
            print kob,"is it alright if I ask why?"
            myInput=raw_input("input:") #Asks for user to enter text
            if myInput in yes:
                print kob,"sorry I won't ask then"
            else:
                print kob,"what is wrong then?"
        elif which==10:
            print kob,":("
        else:
            print kob,"sucks to be you"
    elif myString in multiplyQ:
        print kob,that
    elif myString=="":
        print kob,"Well aren't you interesting"
    else:
        print kob,unsure[random.randrange(0,4)]
    myString=raw_input("You:") #Asks for user to enter text
print sys,"Ending..."
print sys,"Saving Log"
fo.close()
time.sleep(3)





