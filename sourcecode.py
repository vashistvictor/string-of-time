def generatetime1(str0):
    h1 = (1000*int(str0[0])) + (100*int(str0[1]))
    m1 = (10*int(str0[3])) + (1*int(str0[4]))
    if str0[6]=='A':
        if h1==1200:
            h1=h1-1200
    else:
        if h1!=1200:
            h1=h1+1200
    return h1+m1
str1 = input('Enter the string of time in format HH:MM AM/PM ')
print('The equivalent integer is :',generatetime1(str1))
