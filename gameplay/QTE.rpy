 # QTE Specific

screen timer_scr(place="blank"):

    timer 1  action If(t_var>1, SetScreenVariable("t_var", t_var-1), [Hide("timer_scr"), Jump(place)] ) repeat True


    if t_var <= qtetotal*.4:
        text "{font=mechsuit.ttf}{color=#FF0000}{size=70}[t_var]{/size}{/font}" xalign 0.28 yalign 0.491
        
    elif t_var <= qtetotal*.8:
        text "{font=mechsuit.ttf}{color=#FFFF00}{size=70}[t_var]{/size}{/font}" xalign 0.28 yalign 0.491
        
    elif t_var <= qtetotal:
        text "{font=mechsuit.ttf}{color=#FFFFFF}{size=70}[t_var]{/size}{/font}" xalign 0.28 yalign 0.491

        
#Reference data
#$ qteintel = qteintel
#$ qteath = qteath
#$ qtetrack = qtetrack
#$ qtebase = qtebase
#$ qtetotal = 

#$ qtetotal = qteintel + qtebase
#$ t_var = qtetotal
#show screen timer_scr(place="qtelosstimeout")

#$ renpy.hide_screen ("timer_scr")
