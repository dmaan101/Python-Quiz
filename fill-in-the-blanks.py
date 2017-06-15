# -*- coding: utf-8 -*-
#list containing the quiz of different difficulties
quiz=["Batman is a superhero co-created by artist Bob Kane and writer Bill Finger and published by __1__. The character made his first appearance in Detective Comics #27 (May, 1939). Batman is the secret identity of __2__ Wayne. Witnessing the murder of his parents as a child leads him to train himself to physical and intellectual perfection and don a bat-themed costume in order to fight crime. Batman operates in __3__ City, assisted by various supporting characters including his sidekick __4__ and his butler Alfred Pennyworth","The Taj Mahal is an ivory-white marble mausoleum on the __1__ bank of the __2__ river in the Indian city of __3__. It was commissioned in 1632 by the Mughal emperor, Shah Jahan (reigned 1628–1658), to house the tomb of his favourite wife, __4__ Mahal. The tomb is the centrepiece of a 17-hectare complex, which includes a mosque and a guest house, and is set in formal gardens bounded on three sides by a crenellated wall.","Europe is a continent. It is the western part of __1__. It is separated from Asia by the __2__ Mountains in Russia and the Bosporus strait in Turkey.Europe is surrounded by water on three sides. On the west is the Atlantic Ocean. To the north is the Arctic Ocean. The Mediterranean Sea separates Southeastern Europe from __3__.There are more than __4__ countries in Europe. Most of these countries are members of the European Union.Europe covers about 10,180,000 square kilometres (3,930,000 square miles). This is 2% of the Earth's surface (6.8% of its land area).As of 2015, about 740 million people lived in Europe. This was about 11% of the world's population.Europe is a major tourist attraction. People come from all over the world to see its many World Heritage Sites and other attractions."]

#answers to the blanks 
keys=[["dc","bruce","gotham","robin"],["south","yamuna","agra","mumtaz"],["eurasia","Ural","africa","fifty"]]

#function returning the chosen difficulty
def difficulty_level():
    return int(raw_input(" SELECT YOUR DIFFICULTY.\n1. EASY.\n2. MEDIUM.\n3. HARD\n"))

#function replacing the blanks in the quiz
def replace_blank(blank,answer,current_quiz):
    temp = "__"+str(blank+1)+"__"
    new_quiz = current_quiz.replace(temp,current_key[blank])
    print new_quiz
    return new_quiz

#this function takes the answer from the user as an input, converts the string to lower case to check from the keys, prints a statement and return a value accordingly.
def answer_check(blank,current_key,current_quiz,tries):
    answer = raw_input("\n What should come instead of __"+str(blank + 1)+"__?\n")
    answer = answer.lower()
    if answer == current_key[blank]:
        print "Correct\n"
        
        return answer
    else:
        print "Wrong Choice. You have "+str(tries - 1)+" guesses left\n"
        
        return False
    
            
            
#function to start the quiz.
def start_quiz(current_quiz,current_key):
    tries = 4
    max_blank = 4
    blank = 0
    print current_quiz
    
    while tries > 0 and blank < max_blank:
        flag = answer_check(blank,current_key,current_quiz,tries)
        if flag:
            current_quiz = replace_blank(blank,flag,current_quiz)
            blank = blank + 1
            if blank > 3:
                print "*************************Congratulations!!! You won***********************\n"
        else:
            tries = tries - 1
            if tries < 1:
                print "*****************You loose!!!******************\n"
            

print "\nWelcome to the quiz.\n\nYou have 4 guesses per problem. Get all correct to win.\n\n"

difficulty=difficulty_level() - 1
current_quiz = quiz[difficulty]
current_key = keys[difficulty]
start_quiz(current_quiz,current_key)
















