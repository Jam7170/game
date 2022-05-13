from time import sleep
dialogue_speed = 0.05 #Default dialogue speed
import os

clear = lambda: os.system('clear')

def dialogue(msg='',char=None,time=dialogue_speed,newline=True):
    if char:
        for l in char:
            print(l, end='',flush=True)
            sleep(dialogue_speed)
        print(': ',end='',flush=True)
    else: print('* ',end='',flush=True)
    for l in msg:
        print(l, end='',flush=True)
        sleep(time)
    if newline == True:print('')
    else: print(' ', end='',flush=True)
    sleep(0.25)
def dialogue_ellipsis(msg='',char=None,time=dialogue_speed,ellipsistime=0.5,newline=True):
    if char:
        for l in char:
            print(l, end='',flush=True)
            sleep(time*1.2)
        print(': ',end='',flush=True)
    else: print('* ',end='',flush=True)
    for l in msg:
        print(l, end='',flush=True); sleep(time) 
    sleep(ellipsistime)
    print('.', end='',flush=True)
    sleep(ellipsistime)
    print('.', end='',flush=True)
    sleep(ellipsistime)
    if newline == True: print('.')
    else: print('. ',end='',flush=True)
    sleep(0.25)
def dialogue_input(msg='',time=dialogue_speed,type=1,lower=True,char=None): #type 0 - Y/N, 1 - Input
    if char:
        for l in char:
            print(l, end='',flush=True)
            sleep(time*1.2)
        print(': ',end='',flush=True)
    else: print('* ',end='',flush=True)
    for l in msg:
        print(l, end='',flush=True)
        sleep(time)
    if type == 0:
        print(' (Y/N)\n>',end='',flush='')
    elif type == 1:
        print(' \n>', end='',flush=True)
    user_input = input('')
    if lower: user_input = user_input.lower()
    return user_input