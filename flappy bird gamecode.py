'''
Made by NEELANGSHU ROY
Student of B.Tech in Computer Science and Engineering at NIT Allahabad
Batch of 2021-25
'''
import sys
import random
import pygame
from pygame.locals import *

BACKGROUND = 'Game sprites/game background.png'
BASE = 'Game sprites/game_base.png'
PIPE = 'Game sprites/game_pillar.jpg'
SCREEN = pygame.display.set_mode((960,686))
BIRD = 'Game sprites/flappy_bird.png'
GAME_SPRITES,GAME_SOUNDS={},{}
FPS=30
def welcome():
    GAME_SOUNDS['welcomeMusic'].play()
    kk=GAME_SPRITES['play']
    mm=GAME_SPRITES['instruct']
    nn=GAME_SPRITES['exit']
    inst=GAME_SPRITES['instructions']
    bb=GAME_SPRITES['back']
    exi=GAME_SPRITES['exitpanel']
    yes=GAME_SPRITES['yes']
    no=GAME_SPRITES['no']
    k,n=0,0
    while True:
        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        SCREEN.blit(GAME_SPRITES['gamename'],(272,15))
        SCREEN.blit(GAME_SPRITES['myname'],(225,114))

        SCREEN.blit(GAME_SPRITES['base'],(0,541))
        SCREEN.blit(GAME_SPRITES['bird'],(80,300))

        if k==0 and n==0:
            SCREEN.blit(kk,(332,205))
            SCREEN.blit(mm,(332,283))
            SCREEN.blit(nn,(332,361))
        elif k==1:
            SCREEN.blit(inst,(180,205))
            SCREEN.blit(bb,(484,535))
        elif n==1:
            SCREEN.blit(exi,(180,205))
            SCREEN.blit(yes,(332,325))
            SCREEN.blit(no,(332,408))
               
        for event in pygame.event.get():
            change=0
            if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                    return False
            x,y=pygame.mouse.get_pos()
            clic=pygame.mouse.get_pressed()
            if (event.type==MOUSEBUTTONDOWN and event.button==1 and (332<=x<=628 and 205<=y<=268) and k==0 and n==0):
                GAME_SOUNDS['click'].play()
                return True
            elif (332<=x<=628 and 205<=y<=268 and k==0 and n==0):
                kk=GAME_SPRITES['play_click']
            elif k==0 and n==0:
                kk=GAME_SPRITES['play']

            if event.type==MOUSEBUTTONDOWN and event.button==1 and (484<=x<=780 and 535<=y<=598) and k==1 and n==0:
                GAME_SOUNDS['click'].play()
                k=0
            elif (484<=x<=780 and 535<=y<=598) and k==1:
                bb=GAME_SPRITES['back_click']
            elif k==1:
                bb=GAME_SPRITES['back']
            
            if event.type==MOUSEBUTTONDOWN and event.button==1 and (332<=x<=628 and 283<=y<=346) and k==0 and n==0:
                GAME_SOUNDS['click'].play()
                k=1
            elif (332<=x<=628 and 283<=y<=346 and k==0 and n==0):
                mm=GAME_SPRITES['instruct_click']
            elif k==0 and n==0:
                mm=GAME_SPRITES['instruct']

            if (event.type==MOUSEBUTTONDOWN and event.button==1 and (332<=x<=628 and 325<=y<=388) and n==1 and k==0):
                n=0
                GAME_SOUNDS['click'].play()
                pygame.quit()
                sys.exit()
                return False
            elif (332<=x<=628 and 325<=y<=388) and n==1 and k==0:
                yes=GAME_SPRITES['yes_click']
            elif n==1 and k==0:
                yes=GAME_SPRITES['yes']

            if (event.type==MOUSEBUTTONDOWN and event.button==1 and (332<=x<=628 and 408<=y<=471) and n==1 and k==0):
                GAME_SOUNDS['click'].play()
                change=1
                n=0 
            elif (332<=x<=628 and 408<=y<=471) and n==1 and k==0:
                no=GAME_SPRITES['no_click']
            elif n==1 and k==0:
                no=GAME_SPRITES['no']

            if change==1:
                continue

            if (event.type==MOUSEBUTTONDOWN and event.button==1 and (332<=x<=626 and 361<=y<=424) and k==0 and n==0):
                GAME_SOUNDS['click'].play()
                n=1
            elif (332<=x<=626 and 361<=y<=424 and k==0 and n==0):
                nn=GAME_SPRITES['exit_click']
            elif k==0 and n==0:
                nn=GAME_SPRITES['exit']   

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def gameover():
    GAME_SOUNDS['die'].play()
    new=0
    nn=''
    with open('hs.txt') as f:
        nn=f.read()
    if nn[len(nn)-1]==' ':
        new=1
        nn=nn[:len(nn)-1]
        with open('hs.txt','w') as f:
            f.write(nn)
    ss=[int(x) for x in list(nn)]

    try_ag = GAME_SPRITES['retry']
    exi = GAME_SPRITES['exit']
    exit_p = GAME_SPRITES['exitpanel']
    yes=GAME_SPRITES['yes']
    no=GAME_SPRITES['no']
    k=0

    while True:
        SCREEN.blit(GAME_SPRITES['gameover'],(0,0))
        SCREEN.blit(GAME_SPRITES['base'],(0,541))
        if k==0:
            SCREEN.blit(try_ag,(154,440))
            SCREEN.blit(exi,(510,440))
            width=435
            for item in ss:
                SCREEN.blit(GAME_SPRITES['digits'][item],(width,330))
                width+=45
            if new==1:
                SCREEN.blit(GAME_SPRITES['new'],(width+90,300))
        elif k==1:
            SCREEN.blit(exit_p,(180,205))
            SCREEN.blit(yes,(332,325))
            SCREEN.blit(no,(332,408))
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
                return False
            x,y=pygame.mouse.get_pos()
            clic=pygame.mouse.get_pressed()

            if clic[0] and (332<=x<=628 and 325<=y<=388) and k==1:
                k=0
                GAME_SOUNDS['click'].play()
                pygame.quit()
                sys.exit()
                return 0
            elif (332<=x<=628 and 325<=y<=388) and k==1:
                yes=GAME_SPRITES['yes_click']
            elif k==1:
                yes=GAME_SPRITES['yes']
            
            if clic[0] and (332<=x<=629 and 408<=y<=471) and k==1:
                GAME_SOUNDS['click'].play()
                k=0
            elif (332<=x<=629 and 408<=y<=471) and k==1:
                no=GAME_SPRITES['no_click']
            elif k==1:
                no=GAME_SPRITES['no']
            
            if clic[0] and (154<=x<=450 and 440<=y<=503) and k==0:
                GAME_SOUNDS['click'].play()
                return True
            elif (154<=x<=450 and 440<=y<=503) and k==0:
                try_ag=GAME_SPRITES['retry_click']
            elif k==0:
                try_ag=GAME_SPRITES['retry']

            if clic[0] and (510<=x<=806 and 440<=y<=503) and k==0:
                k=1
                GAME_SOUNDS['click'].play()
            elif (510<=x<=806 and 440<=y<=503) and k==0:
                exi=GAME_SPRITES['exit_click']
            elif k==0:
                exi = GAME_SPRITES['exit']
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def roll():
    w=[960, 960+310, 960+620, 960+930]
    t=[
        random.randint(250,400),
        random.randint(250,400),
        random.randint(250,400),
        random.randint(250,400)
    ]
    # pattern of pipes will remain the same as values of t[0], t[1],
    # t[2] and t[3] remain fixed outside the loop

    t_coin=[
        random.randint(0,1),
        random.randint(0,1),
        random.randint(0,1),
        random.randint(0,1)
    ]

    pipeVel = [4,5,7,9,11,13,16]
    sp=[0, 26, 50]
    sc=[0, 10, 20, 30, 40, 50, 75]

    p=300
    score = 0

    playerPosX=80

    PAUSE=0

    kk=GAME_SPRITES['resume']
    mm=GAME_SPRITES['restart']
    nn=GAME_SPRITES['instruct']
    pp=GAME_SPRITES['exit']
    inst=GAME_SPRITES['instructions']
    bb=GAME_SPRITES['back']
    rest=GAME_SPRITES['restartpanel']
    exi=GAME_SPRITES['exitpanel']
    yes=GAME_SPRITES['yes']
    no=GAME_SPRITES['no']
    k1,k2,n=0,0,0

    while True:
        s=[int(x) for x in list(str(score))]
        s.reverse()
        width=GAME_SPRITES['digits'][4].get_width()

        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        
        for i in range(4):
            SCREEN.blit(GAME_SPRITES['pipe'][0],(w[i],t[i]))
            i2=2
            for i1 in range(3):
                if 0==score:
                    SCREEN.blit(GAME_SPRITES['pipe'][1],(w[i],t[i]-750+sp[0]))
                    break
                if sc[i2-2]<score<=sc[i2]:
                    SCREEN.blit(GAME_SPRITES['pipe'][1],(w[i],t[i]-750+sp[i1]))
                    break
                elif sc[6]<score:
                    SCREEN.blit(GAME_SPRITES['pipe'][1],(w[i],t[i]-750+sp[2]))
                    break
                i2 += 2
            if t_coin[i]==1:
                k=2
                for j in range(3):
                    if score==0:
                        SCREEN.blit(GAME_SPRITES['coin'],(w[i]+50,t[i] - 13 - int( (150-sp[0])/2 )) )
                    elif sc[k-2]<score<=sc[k]:
                        SCREEN.blit(GAME_SPRITES['coin'],(w[i]+50,t[i] - 13 - int( (150-sp[j])/2 )) )
                        break
                    elif sc[6]<score:
                        SCREEN.blit(GAME_SPRITES['coin'],(w[i]+50,t[i] - 13 - int( (150-sp[2])/2 )) )
                        break
                    k+=2

        # t[i] - 163 + int( (150-sp[j])/2) )

        SCREEN.blit(GAME_SPRITES['base'],(0,541))
        SCREEN.blit(GAME_SPRITES['bird'],(playerPosX,p))

        for i in range(len(s)):
            SCREEN.blit(GAME_SPRITES['digits'][s[i]],(GAME_SPRITES['background'].get_width()-width,0))
            width+=GAME_SPRITES['digits'][4].get_width()
        SCREEN.blit(GAME_SPRITES['level'],(0,0))
        if 0<=score<=10:
            SCREEN.blit(GAME_SPRITES['digits'][1],(195,0))
        elif 10<score<=20:
            SCREEN.blit(GAME_SPRITES['digits'][2],(195,0))
        elif 20<score<=30:
            SCREEN.blit(GAME_SPRITES['digits'][3],(195,0))
        elif 30<score<=40:
            SCREEN.blit(GAME_SPRITES['digits'][4],(195,0))
        elif 40<score<=50:
            SCREEN.blit(GAME_SPRITES['digits'][5],(195,0))
        elif 50<score<=75:
            SCREEN.blit(GAME_SPRITES['digits'][6],(195,0))
        elif 75<score:
            SCREEN.blit(GAME_SPRITES['digits'][7],(195,0))
        
        if k1==0 and k2==0 and n==0 and PAUSE==1:
            SCREEN.blit(kk,(332,205))
            SCREEN.blit(mm,(332,283))
            SCREEN.blit(nn,(332,361))
            SCREEN.blit(pp,(332,439))
        elif k1==1 and k2==0 and n==0 and PAUSE==1:
            SCREEN.blit(rest,(180,205))
            SCREEN.blit(yes,(332,325))
            SCREEN.blit(no,(332,408))
        elif k2==1 and k1==0 and n==0 and PAUSE==1:
            SCREEN.blit(inst,(180,205))
            SCREEN.blit(bb,(484,535))
        elif n==1 and k1==0 and k2==0 and PAUSE==1:
            SCREEN.blit(exi,(180,205))
            SCREEN.blit(yes,(332,325))
            SCREEN.blit(no,(332,408))
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

        prev_score=score

        for i in range(4):
            a0=0

            k=2
            for j in range(3):
                if sc[k-2]<=score<sc[k]:
                    a0=t[i] - 13 - int( (150-sp[j])/2 )
                    break
                elif sc[6]<=score:
                    a0=t[i] - 13 - int( (150-sp[j])/2 )
                    break
                k+=2

            a1=a0+GAME_SPRITES['coin'].get_height()
            a2=p+GAME_SPRITES['bird'].get_height()
            a3=p+int(GAME_SPRITES['bird'].get_height()/2)
            a4=w[i]+50
            a5=playerPosX+GAME_SPRITES['bird'].get_width()
            a6=a4+GAME_SPRITES['coin'].get_width()+GAME_SPRITES['bird'].get_width()
            if (a4<=a5<a6 and (a0<=p<=a1 or a0<=a2<=a1 or a0<=a3<=a1) and t_coin[i]==1):
                score+=1
                GAME_SOUNDS['point'].play()
                t_coin[i]=0
            
        if prev_score<=10 and score>10:
            GAME_SOUNDS['level_up'].play()
        if prev_score<=20 and score>20:
            GAME_SOUNDS['level_up'].play()
        if prev_score<=30 and score>30:
            GAME_SOUNDS['level_up'].play()
        if prev_score<=40 and score>40:
            GAME_SOUNDS['level_up'].play()
        if prev_score<=50 and score>50:
            GAME_SOUNDS['level_up'].play()
        if prev_score<=75 and score>75:
            GAME_SOUNDS['level_up'].play()

        for i in range(4):
            go=0
            b1=playerPosX+GAME_SPRITES['bird'].get_width()
            b2=p+6
            b3=w[i]+GAME_SPRITES['pipe'][0].get_width()
            b4=p+GAME_SPRITES['bird'].get_height()
            if ((b1-12<=w[i]<=b1 and b2<=t[i]-150)or(playerPosX<=w[i]<b1-12 and p<=t[i]-150)or(playerPosX<w[i]<=b1 and b4>t[i])):
                go=1
            elif (w[i]<b1<=b3 and (p<=t[i]-150 or b4>t[i]) ):
                go=1
            elif ( (playerPosX<b3<=playerPosX+6 and b4-13>=t[i])or(playerPosX<b3<=playerPosX+14 and p+12<=t[i]-150)or(playerPosX+14<b3<=b1 and p<=t[i]-150)or(playerPosX+6<b3<=b1 and b4>t[i]) ):
                go=1
            if go==1:
                numb=0
                with open('hs.txt') as f:
                    numb=int(f.read())
                if score>numb:
                    with open('hs.txt','w') as f:
                        f.write(str(score)+' ')
                return 1
            '''if ( 80<=w[i]<=80+GAME_SPRITES['bird'].get_width() or w[i]<=(80+GAME_SPRITES['bird'].get_width())<=(w[i]+GAME_SPRITES['pipe'][0].get_width()) or 80<=(w[i]+GAME_SPRITES['pipe'][0].get_width())<=(80+GAME_SPRITES['bird'].get_width()) ) and (p+GAME_SPRITES['bird'].get_height())>=t[i]:
                return True
            elif ( 80<=w[i]<=80+GAME_SPRITES['bird'].get_width() or w[i]<=(80+GAME_SPRITES['bird'].get_width())<=(w[i]+GAME_SPRITES['pipe'][0].get_width()) or 80<=(w[i]+GAME_SPRITES['pipe'][0].get_width())<=(80+GAME_SPRITES['bird'].get_width()) ) and (t[i]-500+GAME_SPRITES['pipe'][0].get_height())>=p:
                return True '''

        keys=pygame.key.get_pressed() # a list storing keys pressed in 1 iteration
        if ((keys[K_UP] or keys[K_w]) and p>=0) and PAUSE==0:     # This syntax is correct, although there are no
            p-=3                      # loops involved, but if UP key is pressed 5 times
        elif ((keys[K_DOWN] or keys[K_s]) and p<=545-GAME_SPRITES['bird'].get_height()) and PAUSE==0:
            p+=3                      # in 1 iteration, then this if condition is executed
        elif ((keys[K_LEFT] or keys[K_a]) and playerPosX>=0) and PAUSE==0:
            playerPosX-=3             # 5 times, how I don't know !
        elif ((keys[K_RIGHT] or keys[K_d]) and playerPosX+GAME_SPRITES['bird'].get_width()<=960) and PAUSE==0:
            playerPosX+=3
        
        # for key in keys:          
        #     if key==K_UP:        
        #         p-=3              This syntax is wrong, though it seems
        #     elif key==K_DOWN:     correct, but it is not
        #         p+=3
        
        for i in range(4):
            if w[i]>-130 and score<=10 and PAUSE==0:
                w[i]-=pipeVel[0]
            elif w[i]>-130 and 10<score<=20 and PAUSE==0:
                w[i]-=pipeVel[1]
            elif w[i]>-130 and 20<score<=30 and PAUSE==0:
                w[i]-=pipeVel[2]
            elif w[i]>-130 and 30<score<=40 and PAUSE==0:
                w[i]-=pipeVel[3]
            elif w[i]>-130 and 40<score<=50 and PAUSE==0:
                w[i]-=pipeVel[4]
            elif w[i]>-130 and 50<score<=75 and PAUSE==0:
                w[i]-=pipeVel[5]
            elif w[i]>-130 and 75<score and PAUSE==0:
                w[i]-=pipeVel[6]
            elif 1<=i<=3 and PAUSE==0:
                w[i]=w[i-1]+GAME_SPRITES['pipe'][0].get_width()+180
                t[i]=random.randint(250,400)
                t_coin[i]=random.randint(0,1)
            elif i==0 and PAUSE==0:
                w[0]=w[3]+GAME_SPRITES['pipe'][0].get_width()+180
                t[0]=random.randint(250,400)
                t_coin[0]=random.randint(0,1)
        # now this will bring some volatility to the pipe pattern

        '''if k1==0 and k2==0 and n==0 and PAUSE==1:
            SCREEN.blit(kk,(332,205))
            SCREEN.blit(mm,(332,283))
            SCREEN.blit(nn,(332,361))
        elif k1==1 and PAUSE==1:
            SCREEN.blit(rest,(180,205))
            SCREEN.blit(yes,(332,325))
            SCREEN.blit(no,(332,408))
        elif k2==1 and PAUSE==1:
            SCREEN.blit(inst,(180,205))
            SCREEN.blit(bb,(484,535))
        elif n==1 and PAUSE==1:
            SCREEN.blit(exi,(180,205))
            SCREEN.blit(yes,(332,325))
            SCREEN.blit(no,(332,408))'''

        for event in pygame.event.get():

            change = 0

            if event.type==QUIT:
                pygame.quit()
                sys.exit()
                return 0
            elif event.type==KEYDOWN and event.key==K_ESCAPE:
                PAUSE=1
                change=1
            x,y=pygame.mouse.get_pos()
            # clic=pygame.mouse.get_pressed()

            if (n==1 or k1==1 or k2==1) and PAUSE==1:
                if event.type==MOUSEBUTTONDOWN and event.button==1 and (332<=x<=628 and 325<=y<=388) and k1==1 and PAUSE==1:
                    k1=0
                    GAME_SOUNDS['click'].play()
                    return 2
                elif (332<=x<=628 and 325<=y<=388) and k1==1 and PAUSE==1:
                    yes=GAME_SPRITES['yes_click']
                elif k1==1 and PAUSE==1:
                    yes=GAME_SPRITES['yes']

                if event.type==MOUSEBUTTONDOWN and event.button==1 and (332<=x<=629 and 408<=y<=471) and k1==1 and PAUSE==1:
                    k1=0
                    change=1
                    GAME_SOUNDS['click'].play() 
                elif (332<=x<=629 and 408<=y<=471) and k1==1 and PAUSE==1:
                    no=GAME_SPRITES['no_click']
                elif k1==1 and PAUSE==1:
                    no=GAME_SPRITES['no']

                if event.type==MOUSEBUTTONDOWN and event.button==1 and (484<=x<=780 and 535<=y<=598) and k2==1 and PAUSE==1:
                    k2=0
                    # change=1
                    GAME_SOUNDS['click'].play() 
                elif (484<=x<=780 and 535<=y<=598) and k2==1 and PAUSE==1:
                    bb=GAME_SPRITES['back_click']
                elif k2==1 and PAUSE==1:
                    bb=GAME_SPRITES['back']

                if event.type==MOUSEBUTTONDOWN and event.button==1 and (332<=x<=628 and 325<=y<=388) and n==1 and PAUSE==1:
                    n=0
                    GAME_SOUNDS['click'].play()
                    pygame.quit()
                    sys.exit()
                    return 0
                elif (332<=x<=628 and 325<=y<=388) and n==1 and PAUSE==1:
                    yes=GAME_SPRITES['yes_click']
                elif n==1 and PAUSE==1:
                    yes=GAME_SPRITES['yes']

                if event.type==MOUSEBUTTONDOWN and event.button==1 and (332<=x<=629 and 408<=y<=471) and n==1 and PAUSE==1:
                    n=0
                    change=1
                    GAME_SOUNDS['click'].play()
                elif (332<=x<=629 and 408<=y<=471) and n==1 and PAUSE==1:
                    no=GAME_SPRITES['no_click']
                elif n==1 and PAUSE==1:
                    no=GAME_SPRITES['no'] ##

            if change==1:
                continue

            if k1==0 and k2==0 and n==0 and PAUSE==1:
                if (event.type==MOUSEBUTTONDOWN and event.button==1 and (332<=x<=628 and 205<=y<=268) and k1==0 and k2==0 and n==0) and PAUSE==1:
                    '''or (event.type==KEYDOWN and event.key==K_ESCAPE)'''
                    '''or (event.type==KEYDOWN and event.key==K_ESCAPE and k1==0 and k2==0 and n==0)'''
                    PAUSE=0
                    GAME_SOUNDS['click'].play()
                elif (332<=x<=628 and 205<=y<=268) and k1==0 and k2==0 and n==0 and PAUSE==1:
                    kk=GAME_SPRITES['resume_click']
                elif k1==0 and k2==0 and n==0 and PAUSE==1:
                    kk=GAME_SPRITES['resume']
            
                if event.type==MOUSEBUTTONDOWN and event.button==1 and (332<=x<=628 and 283<=y<=346) and k1==0 and k2==0 and n==0 and PAUSE==1:
                    GAME_SOUNDS['click'].play()
                    k1,k2,n=1,0,0
                elif (332<=x<=628 and 283<=y<=346) and k1==0 and k2==0 and n==0 and PAUSE==1:
                    mm=GAME_SPRITES['restart_click']
                elif k1==0 and k2==0 and n==0 and PAUSE==1:
                    mm=GAME_SPRITES['restart']

                if event.type==MOUSEBUTTONDOWN and event.button==1 and (332<=x<=628 and 361<=y<=424) and k1==0 and k2==0 and n==0 and PAUSE==1:
                    GAME_SOUNDS['click'].play()
                    k2,k1,n=1,0,0
                elif (332<=x<=628 and 361<=y<=424) and k1==0 and k2==0 and n==0 and PAUSE==1:
                    nn=GAME_SPRITES['instruct_click']
                elif k1==0 and k2==0 and n==0 and PAUSE==1:
                    nn=GAME_SPRITES['instruct']

                if event.type==MOUSEBUTTONDOWN and event.button==1 and (332<=x<=628 and 439<=y<=502) and k1==0 and k2==0 and n==0 and PAUSE==1:
                    GAME_SOUNDS['click'].play()
                    n,k1,k2=1,0,0
                elif (332<=x<=628 and 439<=y<=502) and k1==0 and k2==0 and n==0 and PAUSE==1:
                    pp=GAME_SPRITES['exit_click']
                elif k1==0 and k2==0 and n==0 and PAUSE==1:
                    pp=GAME_SPRITES['exit'] ##

if __name__=='__main__':
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption('FLAPPY BIRD by Neelangshu Roy')
    pygame.display.set_icon(pygame.image.load('Game sprites/flappybird_windowicon.png'))
    GAME_SPRITES['background']=pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['base']=pygame.image.load(BASE).convert_alpha()
    GAME_SPRITES['pipe']=(
        pygame.image.load(PIPE).convert_alpha(),
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180)
    )
    GAME_SPRITES['bird']=pygame.image.load(BIRD).convert_alpha()
    GAME_SPRITES['myname']=pygame.image.load('Game sprites/my_name.png').convert_alpha()
    GAME_SPRITES['gamename']=pygame.image.load('Game sprites/game_name.png').convert_alpha()
    GAME_SPRITES['gameover']=pygame.image.load('Game sprites/game_over.png').convert_alpha()
    GAME_SPRITES['coin']=pygame.image.load('Game sprites/coin.png').convert_alpha()
    GAME_SPRITES['level']=pygame.image.load('Game sprites/level.png').convert_alpha()

    GAME_SPRITES['play']=pygame.image.load('Game sprites/play.png').convert_alpha()
    GAME_SPRITES['play_click']=pygame.image.load('Game sprites/play_clicked.png').convert_alpha()
    GAME_SPRITES['exit']=pygame.image.load('Game sprites/exit.png').convert_alpha()
    GAME_SPRITES['exit_click']=pygame.image.load('Game sprites/exit_clicked.png').convert_alpha()
    GAME_SPRITES['resume']=pygame.image.load('Game sprites/resume.png').convert_alpha()
    GAME_SPRITES['resume_click']=pygame.image.load('Game sprites/resume_clicked.png').convert_alpha()
    GAME_SPRITES['restart']=pygame.image.load('Game sprites/restart.png').convert_alpha()
    GAME_SPRITES['restart_click']=pygame.image.load('Game sprites/restart_clicked.png').convert_alpha()
    GAME_SPRITES['instruct']=pygame.image.load('Game sprites/instructions.png').convert_alpha()
    GAME_SPRITES['instruct_click']=pygame.image.load('Game sprites/instructions_clicked.png').convert_alpha()
    GAME_SPRITES['instructions']=pygame.image.load('Game sprites/instruction.png').convert_alpha()
    GAME_SPRITES['back']=pygame.image.load('Game sprites/back.png').convert_alpha()
    GAME_SPRITES['back_click']=pygame.image.load('Game sprites/back_clicked.png').convert_alpha()
    GAME_SPRITES['exitpanel']=pygame.image.load('Game sprites/exit_panel.png').convert_alpha()
    GAME_SPRITES['restartpanel']=pygame.image.load('Game sprites/restart_panel.png').convert_alpha()
    GAME_SPRITES['yes']=pygame.image.load('Game sprites/yes.png').convert_alpha()
    GAME_SPRITES['yes_click']=pygame.image.load('Game sprites/yes_clicked.png').convert_alpha()
    GAME_SPRITES['no']=pygame.image.load('Game sprites/no.png').convert_alpha()
    GAME_SPRITES['no_click']=pygame.image.load('Game sprites/no_clicked.png').convert_alpha()
    GAME_SPRITES['new']=pygame.image.load('Game sprites/new.png').convert_alpha()
    GAME_SPRITES['retry']=pygame.image.load('Game sprites/retry.png').convert_alpha()
    GAME_SPRITES['retry_click']=pygame.image.load('Game sprites/retry_clicked.png').convert_alpha()

    GAME_SPRITES['digits']=(
        pygame.image.load('Game sprites/0_number.png').convert_alpha(),
        pygame.image.load('Game sprites/1_number.png').convert_alpha(),
        pygame.image.load('Game sprites/2_number.png').convert_alpha(),
        pygame.image.load('Game sprites/3_number.png').convert_alpha(),
        pygame.image.load('Game sprites/4_number.png').convert_alpha(),
        pygame.image.load('Game sprites/5_number.png').convert_alpha(),
        pygame.image.load('Game sprites/6_number.png').convert_alpha(),
        pygame.image.load('Game sprites/7_number.png').convert_alpha(),
        pygame.image.load('Game sprites/8_number.png').convert_alpha(),
        pygame.image.load('Game sprites/9_number.png').convert_alpha(),
    )
    GAME_SOUNDS['die']=pygame.mixer.Sound('Game sounds/die.wav')
    GAME_SOUNDS['hit']=pygame.mixer.Sound('Game sounds/hit.wav')
    GAME_SOUNDS['point']=pygame.mixer.Sound('Game sounds/point.wav')
    GAME_SOUNDS['wing']=pygame.mixer.Sound('Game sounds/wing.wav')
    GAME_SOUNDS['welcomeMusic']=pygame.mixer.Sound('Game sounds/game_openingSound.mp3')
    GAME_SOUNDS['click']=pygame.mixer.Sound('Game sounds/click.wav')
    GAME_SOUNDS['level_up']=pygame.mixer.Sound('Game sounds/level_complete.wav')
    pygame.mixer.Sound.set_volume(GAME_SOUNDS['welcomeMusic'],0.80)
    pygame.mixer.Sound.set_volume(GAME_SOUNDS['click'],0.20)
    pygame.mixer.Sound.set_volume(GAME_SOUNDS['point'],0.30)
    pygame.mixer.Sound.set_volume(GAME_SOUNDS['level_up'],8.0)

    bool = welcome()
    while bool:
        check=0
        check = roll()
        if check==0:
            bool=False
            break
        elif check==1:
            bool=True
        elif check==2:
            continue
        bool = gameover()
        if bool==False:
            break
