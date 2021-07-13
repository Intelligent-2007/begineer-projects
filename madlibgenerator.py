from time import sleep
from random import randint

user = input("Type your nickname: ")
Welcome = f"Hello {user}, Lets start our game\nRules are very easy you have to type the word for which you are asked\nFor example if we say you to type any verb then u can type any verb\nSo lets start "

#Send welcome message
for letters in range(0, (len(Welcome) - 1)):
    print(Welcome[letters], end = "")
    sleep(0.01)

#take topic
adjective = input("\nType any adjective: ")
Noun = input("Type any noun: ")
verb_past_tense = input("Verb Past Tense: ")
adverb = input("adverb: ")
adjective1 = input("Type one more adjective: ")
noun1 = input("Noun: ")
noun2 = input("Noun: ")
adjective2 = input("Adjective: ")
verb = input("verb: ")
adverb1 = input("adverb: ")
adjective5 = input("adjective: ")
verb_past_tense2 = input("Verb past tense: ")
plural_noun = input("Purual Noun: ")
number = input("type any number ")
_est_adjective = input("Type any -est adjective: ")

#Base of the stories 
Stories = [f"""Today, my fabulous camp group went to a (an)\n{adjective} amusement park. It was a\nfun park with lots of cool  {plural_noun}\nand enjoyable play structures. When we got there, my\nkind counselor shouted loudly, "Everybody off the\n{Noun}." We all pushed out in a terrible\nhurry. My counselor handed out yellow tickets, and\nwe scurried in. I was so excited! I couldn't figure out\nwhat exciting thing to do first. I saw a scary roller\ncoaster I really liked so, I  {adverb} ran\nover to get in the long line that had about\n{number} people in it. When I finally\ngot on the roller coaster I was  {verb_past_tense}.\nIn fact I was so nervous my two knees were knocking together. This was the \n{_est_adjective} ride I had ever been on! In about two\nminutes I heard the crank and grinding of the gears.\nThat’s when the ride began! When I got to the bottom,\nwas a little  {verb_past_tense2} but I\nwas proud of myself. The rest of the day went \n{adverb1}. It was a(n)\n{adjective1} day at the fun park. """, 
f"""Today I went to the zoo. I saw a(n){adjective}\n{Noun} jumping up and down in its tree.\nHe {verb_past_tense} {adverb}\nthrough the large tunnel that led to its {adjective1}\n{noun1}. I got some peanuts and passed\nthem through the cage to a gigantic gray {noun2}\ntowering above my head. Feeding that animal made\nme hungry. I went to get a {adjective2} scoop\nof ice cream. It filled my stomach. Afterwards I had to\n {verb}  {adverb1} to catch our bus.\nWhen I got home I {verb_past_tense2} my\nmom for a {adjective5} day at the zoo"""]

#print the random topic 
print(Stories[randint(0,(len(Stories) - 1 ))])