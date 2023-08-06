n = input("Enter your name:")
e = int(input("Enter your 4 digit salary expectation:"))

if len(str(e)) > 4 or len(str(e)) < 4:
    print('You have not entered a 4 digit number. Run the program again!')
else:
    if int(e[0] >= e[1] >= int((e[2] and e[3])) and int(e[1] % 2 == 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int(e[0]) * 1000) + ".")
    elif int(e[0] >= e[2] >= int((e[3] and e[1])) and int(e[2] % 2 == 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int(e[0]) * 1000) + ".")
    elif int(e[0] >= e[3] >= int((e[2] and e[1])) and int(e[3] % 2 == 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int(e[0]) * 1000) + ".")
    elif int(e[1] >= e[3] >= int((e[2] and e[0])) and int(e[3] % 2 == 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int(e[1]) * 1000) + ".")
    elif int(e[1] >= e[0] >= int((e[2] and e[3])) and int(e[1] % 2 == 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int(e[1]) * 1000) + ".")
    elif int(e[1] >= e[2] >= int((e[0] and e[3])) and int(e[1] % 2 == 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int(e[1]) * 1000) + ".")
    elif int(e[2] >= e[1] >= int((e[0] and e[3])) and int(e[2] % 2 == 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int(e[2]) * 1000) + ".")
    elif int(e[2] >= e[0] >= int((e[1] and e[3])) and int(e[2] % 2 == 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int(e[2]) * 1000) + ".")
    elif int(e[2] >= e[3] >= int((e[1] and e[0])) and int(e[2] % 2 == 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int(e[2]) * 1000) + ".")
    elif int(e[3] >= e[1] >= int((e[0] and e[2])) and int(e[3] % 2 == 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int(e[3]) * 1000) + ".")
    elif int(e[3] >= e[0] >= int((e[1] and e[2])) and int(e[3] % 2 == 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int(e[3]) * 1000) + ".")
    elif int(e[3] >= e[2] >= int((e[1] and e[0])) and int(e[3] % 2 == 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int(e[3]) * 1000) + ".")

    elif int(e[0] >= e[1] >= int((e[2] and e[3])) and int(e[1] % 2 != 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int((e[0] * 1000) + (e[3] * 100) + (e[3] * 10) + e[3]) + "."))
    elif int(e[0] >= e[2] >= int((e[1] and e[3])) and int(e[2] % 2 != 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int((e[0] * 1000) + (e[3] * 100) + (e[3] * 10) + e[3]) + "."))
    elif int(e[0] >= e[3] >= int((e[1] and e[2])) and int(e[3] % 2 != 0)):
        print("Congrats for the raise " + n + ".Your new monthly salary is " + str(int(e[0]) * 1000) + ".")

        n= input("Enter your name:")
        e= int(input("Enter your 4 digit salary expectation:"))

        for char in n:
        	print(char)


        abcd=int(input("Enter: "))
        digit = str(abcd)
        x = abcd % 1000
        a = (abcd-x)//1000
        y = (abcd- a*1000) % 100
        b = ((abcd-a*1000)-y) //100

        print(x,a,y,b)


n= input("Enter your name:")
e= (input("Enter your 4 digit salary expectation:"))
if len(str(e))>4 or len(str(e))<4:
    print('You have not entered a 4 digit number. Run the program again!')
#if   int(e[0])>=int(e[1])>= int((e[2]) and int(e[3])) and int(e[1])%2==0  :
        #print("Congrats for the raise " + n +".Your new monthly salary is " + str(int(e[0])*1000) + ".")
if int(e[0])>=int(e[1])>= (int((e[2]) and int(e[3]))) and int(e[3])%2==0  :
    print("Congrats for the raise " + n +".Your new monthly salary is " + str(int(e[0])*1000) + ".")


elif int(e[0]) >= int(e[3])>=int((e[1] and int(e[2]))) and int(e[3]) % 2 != 0:
    print("Congrats for the raise " + n + ".Your new monthly salary is " + str((((int(e[0])*1000)+int(e[3])*100)+int(e[3])*10) +int(e[3])) + ".")


        n= input("Enter your name:")
        e= int(input("Enter your 4 digit salary expectation:"))

        print(e[0])




        n = input("Enter your name:")
        e = input("Enter your 4 digit salary expectation:")


        if len(str(e))>4 or len(str(e))<4:
                print('You have not entered a 4 digit number. Run the program again!')



        else:
            print(int(e[1])%2)

text = "We're no strangers to love&You know the rules and so do I@A full\
        commitment's what I'm thinking of@You wouldn't get this from any\
          other guy%I just wanna tell you how I'm feeling&Gotta make you\
       understand$Never gonna give you up$Never gonna let you down@Never\
    gonna run around and desert you%Never gonna make you cry&Never gonna\
        say goodbye%Never gonna tell a lie and hurt you@We've known each\
    other for so long%Your heart's been aching but you're too shy to say\
        it$Inside we both know what's been going on$We know the game and\
     we're gonna play it@And if you ask me how I'm feeling&Don't tell me\
     you're too blind to see$Never gonna give you up%Never gonna let you\
    down&Never gonna run around and desert you$Never gonna make you cry%\
     Never gonna say goodbye@Never gonna tell a lie and hurt you$No, I'm\
       never gonna give you up%No, I'm never gonna let you down&No, I'll\
   never run around and hurt you$Never, ever desert you&We've known each\
     other for so long@Your heart's been aching but$Never gonna give you\
       up%Never gonna let you down@Never gonna run around and desert you\
    $Never gonna make you cry$Never gonna say goodbye@Never gonna tell a\
    lie and hurt you%No, I'm never gonna give you up%No, I'm never gonna\
    let you down@No, I'll never run around and hurt you&I'll never, ever\
                                                              desert you"


# DO NOT CHANGE ABOVE THIS LINE!!!



required_word = input("Enter the word you want to censor: ")
def count_words():
    counter = 0
    for word in text.split():
        if word== required_word:
            counter = counter + 1
    return(counter)

print(count_words())


# DO NOT CHANGE BELOW THIS LINE!!!
text = "We're no strangers to love&You know the rules and so do I@A full\
        commitment's what I'm thinking of@You wouldn't get this from any\
          other guy%I just wanna tell you how I'm feeling&Gotta make you\
       understand$Never gonna give you up$Never gonna let you down@Never\
    gonna run around and desert you%Never gonna make you cry&Never gonna\
        say goodbye%Never gonna tell a lie and hurt you@We've known each\
    other for so long%Your heart's been aching but you're too shy to say\
        it$Inside we both know what's been going on$We know the game and\
     we're gonna play it@And if you ask me how I'm feeling&Don't tell me\
     you're too blind to see$Never gonna give you up%Never gonna let you\
    down&Never gonna run around and desert you$Never gonna make you cry%\
     Never gonna say goodbye@Never gonna tell a lie and hurt you$No, I'm\
       never gonna give you up%No, I'm never gonna let you down&No, I'll\
   never run around and hurt you$Never, ever desert you&We've known each\
     other for so long@Your heart's been aching but$Never gonna give you\
       up%Never gonna let you down@Never gonna run around and desert you\
    $Never gonna make you cry$Never gonna say goodbye@Never gonna tell a\
    lie and hurt you%No, I'm never gonna give you up%No, I'm never gonna\
    let you down@No, I'll never run around and hurt you&I'll never, ever\
                                                              desert you"


# DO NOT CHANGE ABOVE THIS LINE!!!


req_word =input("Enter the word you want to censor: ")
def replace_words(text):
    for word in text.split():
        if word== req_word:
            text = text.replace(word, word[0] + "*" * (len(word) - 1))
    return text





print(replace_words(text))






icerik = "merhaba ben can can can"
wordcount={}
for word in icerik.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for key in wordcount.keys():
  print ("%s %s " %(key , wordcount[key]))




name = input('Enter your name:')
e = (input('Enter your four-digit salary expectation:'))

a=int(e[0])
b=int(e[1])
c=int(e[2])
d=int(e[3])

if a>=b and a>=c and a>=d :
     if b>=c and b>=d :
         if  b%2==0 :e=1000*a
         else: e=1000*a+111*b
     elif c>=b and c>=d :
         if c%2==0 : e=1000*a
         else: e=1000*a+111*c
     elif d>=b and d>=c:
         if d%2==0 : e=1000*a
         else : e=1000*a+111*d
if b>=a and b>=c and b>=d :
     if a>=c and a>=d :
         if  a%2==0 :e=1000*b
         else: e=1000*b+111*a
     elif c>=a and c>=d :
         if c%2==0 : e=1000*b
         else: e=1000*b+111*c
     elif d>=a and d>=c:
         if d%2==0 : e=1000*b
         else : e=1000*b+111*d
if c>=b and c>=a and c>=d :
     if b>=a and b>=d:
         if  b%2==0 :
             e=1000*c
         else: e=1000*c+111*b
     elif a>=b and a>=d :
         if a%2==0 : e=1000*c
         else: e=1000*c+111*a
     elif d>=b and d>=c:
         if d%2==0 : e=1000*c
         else : e=1000*c+111*d
if d>=b and d>=c and d>=a :
     if b>=c and b>=d :
         if  b%2==0 :e=1000*d
         else: e=1000*d+111*b
     elif c>=b and c>=a :
         if c%2==0 : e=1000*d
         else: e=1000*d+111*c
     elif a>=b and a>=c:
         if a%2==0 : e=1000*d
         else : e=1000*d+111*a

new_salary=e

if  len(str(e))==4:
         print("Congrats for the raise,"+ name +". Your new monthly salary is "+ str(new_salary))
else : print('You have not entered four-digit number. Run the program again')

desired_future_value = float(input('Enter the desired future value: '))
annual_interest = float(input('Enter annual interest: '))
number_of_years = int(input('Enter number of years: '))
present_value = desired_future_value/((1+annual_interest)**number_of_years)
print(present_value)
print(round(present_value,1))
