# name = input('Your name = ')
# sex = input('Your sex = ')
# occupation = input('Your occupation = ')
# print('Dear Mr', name, 'with all the bravado you have as a', sex, ',lets try and hustle it out as it seems the pathway for',occupation, 'is straight and narrow. The lord be with us')
num = int(input('Enter your number: '))
if num % 3 == 0 and num % 5 == 0:
    print('The number is fuzzybuzzy')
elif num % 3 == 0:
    print('The number is fuzzy')
elif num % 5 == 0:
    print('The number is buzzy')
else:
    print('The number is invalid') 
