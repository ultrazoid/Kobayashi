import math

__author__ = 'ultrazoid_'

import random

myString=raw_input("input:") #Asks for user to enter text
#list of 2 times table
greetings = ["hi","hello","Hello","Hi","gday","Gday","G'day"]
hruForms = ["how are you", "hru"]
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
multiplyQ = ["Show me then","show me then","show me then","Show me then","show me","Sow me"]
end = ["quit","end"]
byes = ["bye","Bye","cya","See You","see you"]
that = [2*1,2*2,2*3,2*4,2*5,2*6,2*7,2*8,2*9,2*10,2*11,2*12]

while myString!="end":
    if myString in greetings:
        print greetings[random.randrange(0,7)]
        print hruForms[random.randrange(0,2)]
    elif myString in hruForms:
        print hruReplies2[random.randrange(0,30)]
        print hruReplies1[random.randrange(0,6)]
    elif myString in hruReplies1:
        print hruReplies2[random.randrange(0,30)]
    elif myString in times:
        print "i know the 2 times-table"
    elif myString=="multiply":
        print "Multiplying..."
        for multiple in that:
            print multiple
    elif myString in byes:
        print byes[random.randrange(0,5)]
        print "type end to end"
    elif myString in hruReplies2:
        print hrReplies[random.randrange(0,8)]
    elif myString in hrReplies:
        print thanks[random.randrange(0,4)]
    elif myString in thanks:
        print thanksReplies[random.randrange(0,8)]
    elif myString in thanksReplies:
        print smiles[random.randrange(0,6)]
    elif myString in smiles:
        print "No need for smilies"
    elif myString in sReplies:
        print "Are you calling me an Hypocrite?"
    elif myString in yes:
        print "lol"
    elif myString=="lol?":
        print "Yes, lol"
    elif myString=="test.all":
        print "Testing All Lists"
        print greetings
        print hruForms
        print hruReplies1
        print hruReplies2
        print hrReplies
        print thanks
        print thanksReplies
        print smiles
        print sReplies
        print yes
        print times
        print multiplyQ
        print end
        print byes
        print that
    elif myString=="test.greetings":
        print "Testing Greetings List"
        print greetings
    elif myString=="bad":
        which=random.randrange(0,10)
        if which==0:
            print "is everything alright?"
        elif which==2:
            print "are you alright?"
        elif which==4:
            print ":( what's wrong?"
        elif which==6:
            print "what's wrong?"
        elif which==8:
            print "is it alright if I ask why?"
            myInput=raw_input("input:") #Asks for user to enter text
            if myInput in yes:
                print "sorry I won't ask then"
            else:
                print "what is wrong then?"
        elif which==10:
            print ":("
        else:
            print "sucks to be you"
    elif myString in multiplyQ:
        print that
    else:
        print "I do not understand"
    myString=raw_input("input:") #Asks for user to enter text
print "Ending..."





