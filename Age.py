def what_should_i_do(age):
    if age<7 :
        print('Добро пожаловть в детский сад)')
    elif 7<=age<=18 :
        print('Добро пожаловать в школу')
    elif 18<=age<=24 :
        print('Добро пожаловать в универ')
    elif age>24 :
        print('Work hard, play hard')

question=input('How old are you? ')
what_should_i_do(int(question))