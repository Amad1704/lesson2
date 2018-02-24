def stroki(line1, line2):
    if line1==line2:
        print(1)

    elif line1!=line2 and len(line1)>len(line2) and line2!='learn':
        print(2)
        
    elif line1!=line2 and line2=='learn':
        print(3)
        

stroki('stroka11','stroka2')
stroki('stroka1', 'stroka1')
stroki('stroka1', 'learn')
