# USSD
code = input('Enter ussd code: ')
if code == '*312#':
    print(''''
          1. Data plan
          2. Voice Offers
          3. Roaming/int'l
          4. Borrow credit
          5. Recharge
          6. Gift Data
          7. Video Packs
          8. Chat with Zigi
          9. VAS
          0. Back
          ''')
    choice = input('choice: ')
    if choice == '1':
        print('''
              1. Daily plan
              2. Weekly Plan
              3. Bi-weekly plan
              4. monthly Plan
''')
        daily = input ('Enter ussd code: ')
        if daily == '1':
            print('''
                 1. 5GB for #2000
                 2.1GB for #500
                 #. Exit
''')
            gb = input ('Enter ussd: ')
            if gb == '1':
                print('''Your account has been
                          debited and you've been given 
                          5gb of data''')
            elif gb == '2':
                    print('''Your account has been
                          debited and you've been given 
                          1024mb of data''')
            elif gb == '#':
                    print('Thanks for your time')
            else:
                    print('Invalid Ussd code')
            
        else:
            print('No more data available')
    else:
        print('No more package available')