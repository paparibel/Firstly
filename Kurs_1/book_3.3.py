#Exercise 3: Write a program to prompt for a score between 0.0 and
#1.0. If the score is out of range, print an error message. If the score is
#between 0.0 and 1.0, print a grade using the following table:
#dodaje funkcje While, zeby pgrogram sie nie wywalal
x = input('Podaj wartość między 0.0, a 1.0')
try:
    x = float(x)
except: 
    print('Liczba ma być dziesiętna')
    quit()
if  x >= 1.0 or x <= 0.0 :
    print('Liczba ma byc z zakresiu od 0.0 do 1.0')
elif x >= 0.9 :
    print('A')
elif x >= 0.8 :
    print('B')
elif x >= 0.7 :
    print('C')
elif x >= 0.6 :
    print('D')    
elif x < 0.6 :
    print('E')    