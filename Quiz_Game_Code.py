
print("Welcome to my quiz!")

playing=input()
if playing.lower()!='yes':
    quit()

print("okay! lets play:)")
score=0

#1Q
answer=input('What does CPU stand for? ')
if answer.lower()=="central processing unit":
    print("Corrrect!")
    score+=1
else:
    print("Incorrect!")

 #2Q
answer=input('What does GPU stand for? ')
if answer.lower()=="graphic processing unit ":
    print("Corrrect!")
    score += 1
else:
    print("Incorrect!")

 #3Q
answer=input('What does RAM stand for? ')
if answer.lower()=="random access unit ":
    print("Corrrect!")
    score += 1
else:
    print("Incorrect!")
#4Q
answer=input('What does UPS stand for? ')
if answer.lower()=="unit power supply ":
    print("Corrrect!")
    score += 1
else:
    print("Incorrect!")
#5Q
answer=input('What does ROM stand for? ')
if answer.lower()=="random access memory ":
    print("Corrrect!")
    score += 1
else:
    print("Incorrect!")

print("You got "+str(score)+ "question correct!")
print("You got "+str((score/4)*100) +"%")



