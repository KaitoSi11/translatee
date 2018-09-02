# bla bla bla

#$ survived = 0
#$ qtetotal = qtereaction
#$ t_var = qtetotal
#show screen timer_scr(place="qtelosstimeout")
#jump qte_game
#label qtelosstimeout:
#    if survived >= 5:
#        "You win!"
#        return
#    else:
#         "You lose!"
#         return

screen battle_screen:

    #frame:
        #xpadding 1
        #ypadding 1
        #xalign 0.5
        #yalign 0.05
        #hbox:
            #xfill True
            #text " "
            
    if survived <= 4:
        text "{font=mechsuit.ttf}{color=#FFFFFF}{size=50}[survived]x{/size}{/font}" xalign 0.5 yalign 0.575
        text "COMBO" size 40 xalign 0.5 yalign 0.65
        
    elif survived <= 8:
        text "{font=mechsuit.ttf}{color=#FFFF00}{size=50}[survived]x{/size}{/font}" xalign 0.5 yalign 0.575
        text "COMBO" size 40 xalign 0.5 yalign 0.65
        
    elif survived <= 12:
        text "{font=mechsuit.ttf}{color=#FFBF00}{size=50}[survived]x{/size}{/font}" xalign 0.5 yalign 0.575
        text "COMBO" size 40 xalign 0.5 yalign 0.65
        
    elif survived > 12:
        text "{font=mechsuit.ttf}{color=#FF0000}{size=50}[survived]x{/size}{/font}" xalign 0.5 yalign 0.575
        text "COMBO" size 40 xalign 0.5 yalign 0.65
        
    #text "[survived]x HITS" size 50 xalign 0.5 yalign 0.65

    # [enemyHP:.2]
    if enemyHP <= enemyHPMax*.25:
        text "HP:" size 40 xalign 0.7 yalign 0.0585
        text "{font=mechsuit.ttf}{color=#FF0000}{size=40}[enemyHP]{/size}{/font}" xalign 0.8 yalign 0.0265
        
    elif enemyHP <= enemyHPMax*.5:
        text "HP:" size 40 xalign 0.7 yalign 0.0585
        text "{font=mechsuit.ttf}{color=#FFFF00}{size=40}[enemyHP]{/size}{/font}" xalign 0.8 yalign 0.0265
        
    elif enemyHP <= enemyHPMax*1:
        text "HP:" size 40 xalign 0.7 yalign 0.0585
        text "{font=mechsuit.ttf}{color=#33FF33}{size=40}[enemyHP]{/size}{/font}" xalign 0.8 yalign 0.0265

    if mcEnergy <= mcEnergyMax*.25:
        text "ENERGY:" size 40 xalign 0.075 yalign 0.0585
        text "{font=mechsuit.ttf}{color=#FF0000}{size=40}[mcEnergy]{/size}{/font}" xalign 0.2 yalign 0.0265
        
    elif mcEnergy <= mcEnergyMax*.5:
        text "ENERGY:" size 40 xalign 0.075 yalign 0.0585
        text  "{font=mechsuit.ttf}{color=#FFFF00}{size=40}[mcEnergy]{/size}{/font}" xalign 0.2 yalign 0.0265
        
    elif mcEnergy <= mcEnergyMax*1:
        text "ENERGY:" size 40 xalign 0.075 yalign 0.0585
        text "{font=mechsuit.ttf}{color=#0066FF}{size=40}[mcEnergy]{/size}{/font}" xalign 0.2 yalign 0.0265
        
screen timer_scrReaction(place="blank"):
    
    timer 1 action If(t_var>1, SetScreenVariable("t_var", t_var-1), [Hide("timer_scrReaction"), Jump(place)] ) repeat True

    if t_var <= qtetotal*.25:
        text "{font=mechsuit.ttf}{color=#FF0000}{size=40}[t_var]{/size}{/font}" xalign 0.5 yalign 0.25
        
    elif t_var <= qtetotal*.5:
        text "{font=mechsuit.ttf}{color=#FFFF00}{size=40}[t_var]{/size}{/font}" xalign 0.5 yalign 0.25
        
    elif t_var <= qtetotal*1:
        text "{font=mechsuit.ttf}{color=#FFFFFF}{size=40}[t_var]{/size}{/font}" xalign 0.5 yalign 0.25

screen quicktime_event:

    if context != "E1D3S4_ShouPracticeComplete":
        if enemyHP <= 0:
            frame:
                xpadding 10
                ypadding 5
                xalign 0.5
                yalign 0.8
                
                vbox:
                    text "{font=mechsuit.ttf}{color=#FFBF00}{size=42}PRESS 'SPACEBAR' FOR FINISHER{/size}{/font}" xalign 0.5 yalign 0.8
                    key "K_SPACE" action Jump("finisher")
        
    if mode == "overdrive":
        frame:
            xpadding 10
            ypadding 5
            xalign 0.5
            yalign 0.45
    
            vbox:
                text "{color=#FFBF00}Repeatedly Press 'D'!" size 50 xalign 0.5 yalign 0.45
                key "K_SPACE" action Jump("finisher")
    
        key fail1 action Jump("success")
        key fail2 action Jump("success")
        key fail3 action Jump("success")
        key fail4 action Jump("success")
        key fail5 action Jump("success")
        key fail6 action Jump("success")
        key qte_key2 action Jump("success")
        key qte_key3 action Jump("success")
    else:
        frame:
            xpadding 10
            ypadding 5
            xalign 0.5
            yalign 0.45
    
            vbox:
                text "{color=#FFBF00}[qte_key]" size 50 xalign 0.5 yalign 0.45
    
        key fail1 action Jump("failure")
        key fail2 action Jump("failure")
        key fail3 action Jump("failure")
        key fail4 action Jump("failure")
        key fail5 action Jump("failure")
        key fail6 action Jump("failure")
        key qte_key2 action Jump("success")
        key qte_key3 action Jump("success")
        timer 2.0 action Jump("failure")
#show screen timer_scr(place="qtelosstimeout")

label qte_game:
    $ diceroll = renpy.random.randint(1, 4)
    if diceroll == 1:
        $ qte_key = "W"
        $ qte_key2 = "w"
        $ qte_key3 = "K_UP"
        $ fail1 = "a"
        $ fail2 = "s"
        $ fail3 = "d"
        $ fail4 = "K_LEFT"
        $ fail5 = "K_DOWN"
        $ fail6 = "K_RIGHT"
    elif diceroll == 2:
        $ qte_key = "A"
        $ qte_key2 = "a"
        $ qte_key3 = "K_LEFT"
        $ fail1 = "w"
        $ fail2 = "s"
        $ fail3 = "d"
        $ fail4 = "K_UP"
        $ fail5 = "K_DOWN"
        $ fail6 = "K_RIGHT"
    elif diceroll == 3:
        $ qte_key = "S"
        $ qte_key2 = "s"
        $ qte_key3 = "K_DOWN"
        $ fail1 = "a"
        $ fail2 = "w"
        $ fail3 = "d"
        $ fail4 = "K_UP"
        $ fail5 = "K_LEFT"
        $ fail6 = "K_RIGHT"
    else:
        $ qte_key = "D"
        $ qte_key2 = "d"
        $ qte_key3 = "K_RIGHT"
        $ fail1 = "a"
        $ fail2 = "s"
        $ fail3 = "w"
        $ fail4 = "K_UP"
        $ fail5 = "K_LEFT"
        $ fail6 = "K_DOWN"

    call screen quicktime_event
    
    
label finisher:
    if finishFirst == 0:
        $ finishLine = renpy.input("What should I say for my final attack?")
        $ finishLine = finishLine.strip()
        if finishLine == "":
            $ finishLine = "Here goes!"
        $ finishFirst = 1

                
    if mode == "overdrive":
        hide mco
        hide shou
        hide aiM
        hide aiR
        hide arM
        with dissolve
        
        if enemy == "aiM":
            show mco neuFist at bl:
                xzoom -1
            show aiM neu at br
            with dissolve
        elif enemy == "aiR":
            show mco neuFist at bl:
                xzoom -1
            show aiR neu at br
            with dissolve
        elif enemy == "arM":
            show mco neuFist at bl:
                xzoom -1
            show arM neu at br
            with dissolve
        elif enemy == "shou":
            show mco neuFist at bl:
                xzoom -1
            show shou mech at br
            with dissolve
            
        show mco attFist at bl with dissolve
        $renpy.pause(.5)
        pf "[finishLine]"
        play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
        show mco attFist at bl, Shake(None, 1, dist=20):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 1750
                
        $renpy.pause(.15)
        play sound2 [ 'audio/sfx/GEAR Combat/Power Fist Attack 1.ogg', 'audio/sfx/GEAR Combat/Hit.ogg' ]
        if enemy == "aiM":
            show aiM neu at br, Shake(None, 1, dist=15) behind mco with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
        elif enemy == "aiR":
            show aiR neu at br, Shake(None, 1, dist=15) behind mco with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
        elif enemy == "arM":
            show arM neu at br, Shake(None, 1, dist=15) behind mco with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
        elif enemy == "grunt":
            show grunt neu at br, Shake(None, 1, dist=15) behind mco with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
        elif enemy == "boss":
            show boss neu at br, Shake(None, 1, dist=15) behind mco with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
        elif enemy == "bugeisha":
            show bugeisha neu at br, Shake(None, 1, dist=15) behind mc with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
        elif enemy == "shou":
            show shou mech at br, Shake(None, 1, dist=15) behind mco with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
                    
        show white with dissolve
        
    else:
        show mc ready at bl with dissolve
        $renpy.pause(.5)
        pf "[finishLine]"
        show mc ready at bl, Shake(None, 1, dist=20):
            xzoom -1
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 1750
                
        $renpy.pause(.15)
        if enemy == "aiM":
            show aiM neu at br, Shake(None, 1, dist=15) behind mc with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
        elif enemy == "aiR":
            show aiR neu at br, Shake(None, 1, dist=15) behind mc with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
        elif enemy == "arM":
            show arM neu at br, Shake(None, 1, dist=15) behind mc with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
        elif enemy == "grunt":
            show grunt neu at br, Shake(None, 1, dist=15) behind mc with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
        elif enemy == "boss":
            show boss neu at br, Shake(None, 1, dist=15) behind mc with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
        elif enemy == "bugeisha":
            show bugeisha neu at br, Shake(None, 1, dist=15) behind mc with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
        elif enemy == "shou":
            show shou mech at br, Shake(None, 1, dist=15) behind mc with Dissolve(.1):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1500
                    
        show white with dissolve
        
    $renpy.pause(1)
    hide white with dissolve
    jump expression context
    
    
label success:
    
    $ bloSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Block.ogg', 'audio/sfx/GEAR Combat/Block.ogg' ])
    $ dodSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Dodge.ogg', 'audio/sfx/GEAR Combat/Dodge.ogg' ])
    $ fistSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Power Fist Attack 1.ogg', 'audio/sfx/GEAR Combat/Power Fist Attack 2.ogg' ])
    $ hitSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Hit.ogg', 'audio/sfx/GEAR Combat/Hit.ogg' ])
    $ rifSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Rifle.ogg', 'audio/sfx/GEAR Combat/Rifle.ogg' ])
    $ smgSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/SMG.ogg', 'audio/sfx/GEAR Combat/SMG.ogg' ])
    $ sniSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Sniper.ogg', 'audio/sfx/GEAR Combat/Sniper.ogg' ])
    $ sw1Sound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Sword Single.ogg', 'audio/sfx/GEAR Combat/Sword Single.ogg' ])
    $ sw2Sound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Sword Double.ogg', 'audio/sfx/GEAR Combat/Sword Double.ogg' ])
    
    if "defaultBuster" in list(inv.equipped.values()):
        $ meleeSound = "audio/sfx/GEAR Combat/Sword Single.ogg"
    if "defaultDaggers" in list(inv.equipped.values()):
        $ meleeSound = "audio/sfx/GEAR Combat/Sword Double.ogg"
    if "defaultKatana" in list(inv.equipped.values()):
        $ meleeSound = "audio/sfx/GEAR Combat/Sword Single.ogg"
    if "defaultPistol" in list(inv.equipped.values()):
        $ rangeSound = "audio/sfx/GEAR Combat/Sniper.ogg"
    if "defaultRifle" in list(inv.equipped.values()):
        $ rangeSound = "audio/sfx/GEAR Combat/Rifle.ogg"
    if "defaultSMG" in list(inv.equipped.values()):
        $ rangeSound = "audio/sfx/GEAR Combat/SMG.ogg"
    
        
    $ survived += 1
    
    if survived > score:
        $ score = survived
    
    if mode == "overdrive":
        
        $ enemyHP -= 10 + damage + ( combo * survived )
        $ knockback += 20
        $ mcEnergy -= 10
        
        play sound fistSound
        show mco attFist at bl with Dissolve(.05):
            parallel:
                easein .1 alpha 1.0
            parallel:
                easein .1 xoffset ( knockback + 25 )
        play sound2 hitSound
        if enemy == "aiM":
            show aiM neu at br, Shake(None, .1, dist=15) with Dissolve(.1):
                parallel:
                    easein .1 alpha 1.0
                parallel:
                    easein .1 xoffset knockback
        elif enemy == "aiR":
            show aiR neu at br, Shake(None, .1, dist=15) with Dissolve(.1):
                parallel:
                    easein .1 alpha 1.0
                parallel:
                    easein .1 xoffset knockback
        elif enemy == "arM":
            show arM neu at br, Shake(None, .1, dist=15) with Dissolve(.1):
                parallel:
                    easein .1 alpha 1.0
                parallel:
                    easein .1 xoffset knockback
        elif enemy == "shou":
            show shou mech at br, Shake(None, .1, dist=15) with Dissolve(.1):
                parallel:
                    easein .1 alpha 1.0
                parallel:
                    easein .1 xoffset knockback
            
        show mco neuFist at bl with Dissolve(.05)
        
    elif mode == "retreat":
        # No attacks in this mode
        
        $ mcEnergy -= 10
        
        if diceroll == 1:
            $ retSound = bloSound
        elif diceroll == 2:
            $ retSound = dodSound
        elif diceroll == 3:
            $ retSound = bloSound
        else:
            $ retSound = dodSound
        if enemy == "aiM":
            play sound sw2Sound
            show aiM att at br with Dissolve(.05)
        elif enemy == "aiR":
            play sound smgSound
            show aiR att at br with Dissolve(.05)
        elif enemy == "arM":
            play sound sw2Sound
            show arM att at br with Dissolve(.05)
        elif enemy == "shou":
            play sound smgSound
            show shou att at br with Dissolve(.05)
            
        play sound2 retSound
        if diceroll == 1:
            show mc blo at bl with Dissolve(.45)
        elif diceroll == 2:
            show mc dod at bl with Dissolve(.45)
        elif diceroll == 3:
            show mc blo at bl with Dissolve(.45)
        else:
            show mc dod at bl with Dissolve(.45)
                
        show mc mech at bl with Dissolve(.1)
        
        if enemy == "aiM":
            show aiM neu at br with Dissolve(.1)
        elif enemy == "aiR":
            show aiR neu at br with Dissolve(.1)
        elif enemy == "arM":
            show arM neu at br with Dissolve(.1)
        elif enemy == "shou":
            show shou mech at br with Dissolve(.1)
        
        if survived > score:
            $ score = survived
            
    else:
        
        $ mcAction = renpy.random.choice([ "attack", "attack", "attack", "defense" ])
        
        if mcAction == "defense":
            
            $ comradeUsed = 1
            
            if diceroll == 1:
                $ retSound = bloSound
            elif diceroll == 2:
                $ retSound = "audio/sfx/GEAR Combat/Dodge.ogg" # dodSound
            elif diceroll == 3:
                $ retSound = bloSound
            else:
                $ retSound = "audio/sfx/GEAR Combat/Dodge.ogg" # dodSound
                
            if enemy == "aiM":
                play sound sw2Sound
                show aiM att at br with Dissolve(.05)
            elif enemy == "aiR":
                play sound smgSound
                show aiR att at br with Dissolve(.05)
            elif enemy == "arM":
                play sound sw2Sound
                show arM att at br with Dissolve(.05)
            elif enemy == "boss":
                play sound sw2Sound
                show boss att at br with Dissolve(.05)
            elif enemy == "bugeisha":
                play sound sw1Sound
                show bugeisha att at br with Dissolve(.05)
            elif enemy == "grunt":
                play sound sniSound
                show grunt att at br with Dissolve(.05)
            elif enemy == "shou":
                play sound smgSound
                show shou att at br with Dissolve(.05)
                
            $ mcEnergy -= 10
                
            play sound2 retSound
            if diceroll == 1:
                show mc blo at bl with Dissolve(.45)
            elif diceroll == 2:
                show mc dod at bl with Dissolve(.45)
            elif diceroll == 3:
                show mc blo at bl with Dissolve(.45)
            else:
                show mc dod at bl with Dissolve(.45)
                    
            show mc mech at bl with Dissolve(.1)
            
            if enemy == "aiM":
                show aiM neu at br with Dissolve(.1)
            elif enemy == "aiR":
                show aiR neu at br with Dissolve(.1)
            elif enemy == "arM":
                show arM neu at br with Dissolve(.1)
            elif enemy == "boss":
                show boss neu at br with Dissolve(.1)
            elif enemy == "bugeisha":
                show bugeisha neu at br with Dissolve(.1)
            elif enemy == "grunt":
                show grunt neu at br with Dissolve(.1)
            elif enemy == "shou":
                show shou mech at br with Dissolve(.1)
        
        #$ comradeAssist = renpy.random.randint(0, 100)
        # Temp code until points are used, SocialLink is used instead of friend/romance
        $ comradeAssist = renpy.random.randint(0, 10)
        
        if context == "E1D3S4_ShouPracticeComplete" or "E1D5S2_SoloComplete" or "E1D5S2_DuelComplete" or "E2D5S2_FirstPractice":
            $ comradeUsed = 1
        
        if comradeUsed == 0:
            
            #$ mcAction = "None"
            
            if comradeAssist < kaoriSocialLink and comradeKaori == 1:
                $ comradeUsed = 1
                $ enemyHP -= 10 + ( kaoriSocialLink * 10 )
                play sound "audio/sfx/GEAR Combat/Sword Single.ogg"
                show kaori att at br behind aiM, aiR, arM, boss, grunt, shou with Dissolve(.45):
                    xoffset 200
                    xzoom .95
                    yzoom .95
                
                play sound2 hitSound
                if enemy == "aiM":
                    show aiM neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "aiR":
                    show aiR neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "arM":
                    show arM neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "boss":
                    show boss neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "bugeisha":
                    show bugeisha neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "grunt":
                    show grunt neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "shou":
                    show shou mech at br, Shake(None, .25, dist=15) with Dissolve(.25)
                    
                hide kaori with Dissolve(.25)
                
            elif comradeAssist < mayuSocialLink and comradeMayu == 1:
                $ comradeUsed = 1
                $ enemyHP -= 10 + ( mayuSocialLink * 10 )
                play sound "audio/sfx/GEAR Combat/Sniper.ogg"
                show mayu att at tl behind mc with Dissolve(.45):
                    xzoom -.7
                    yzoom .7
                
                play sound2 hitSound
                if enemy == "aiM":
                    show aiM neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "aiR":
                    show aiR neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "arM":
                    show arM neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "boss":
                    show boss neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "bugeisha":
                    show bugeisha neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "grunt":
                    show grunt neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "shou":
                    show shou mech at br, Shake(None, .25, dist=15) with Dissolve(.25)
                    
                hide mayu with Dissolve(.25)
                
            elif comradeAssist < shouSocialLink and comradeShou == 1:
                $ comradeUsed = 1
                $ enemyHP -= 10 + ( shouSocialLink * 10 )
                play sound "audio/sfx/GEAR Combat/SMG.ogg"
                show shou att at tl behind mc with Dissolve(.45):
                    xzoom -.7
                    yzoom .7
                
                play sound2 hitSound
                if enemy == "aiM":
                    show aiM neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "aiR":
                    show aiR neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "arM":
                    show arM neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "boss":
                    show boss neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "bugeisha":
                    show bugeisha neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                elif enemy == "grunt":
                    show grunt neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
                    
                hide shou with Dissolve(.25)
                
            else:
                $ comradeUsed = 0
                
        else:
            $ comradeUsed = 0
        
        if mcAction == "attack":
            
            if context == "E2D5S2_FirstPractice":
                $ enemyHP -= 1
            else:
                $ enemyHP -= 10 + damage + ( combo * survived )
                
            if diceroll == 1:
                $ attSound = meleeSound
                play sound attSound
                #show mc attM at bl with Dissolve(.45)
                if "defaultBuster" in list(inv.equipped.values()):
                    $ mcEnergy -= 10
                    show mc attM at bl with Dissolve(.45):
                        xoffset 150
                elif "defaultKatana" in list(inv.equipped.values()):
                    show mc attM at bl with Dissolve(.45):
                        xoffset 50
                else:
                    show mc attM at bl with Dissolve(.45)
                
            elif diceroll == 2:
                $ attSound = rangeSound
                play sound attSound
                #show mc attR at bl with Dissolve(.45)
                if "defaultPistol" in list(inv.equipped.values()):
                    show mc attR at bl with Dissolve(.45):
                        xoffset 75
                elif "defaultRifle" in list(inv.equipped.values()):
                    $ mcEnergy -= 23
                    show mc attR at bl with Dissolve(.45)
                else:
                    show mc attR at bl with Dissolve(.45)
                
            elif diceroll == 3:
                $ attSound = meleeSound
                play sound attSound
                #show mc attM at bl with Dissolve(.45)
                if "defaultBuster" in list(inv.equipped.values()):
                    $ mcEnergy -= 10
                    show mc attM at bl with Dissolve(.45):
                        xoffset 150
                elif "defaultKatana" in list(inv.equipped.values()):
                    show mc attM at bl with Dissolve(.45):
                        xoffset 50
                else:
                    show mc attM at bl with Dissolve(.45)
                
            else:
                $ attSound = rangeSound
                play sound attSound
                #show mc attR at bl with Dissolve(.45)
                if "defaultPistol" in list(inv.equipped.values()):
                    show mc attR at bl with Dissolve(.45):
                        xoffset 75
                elif "defaultRifle" in list(inv.equipped.values()):
                    $ mcEnergy -= 23
                    show mc attR at bl with Dissolve(.45)
                else:
                    show mc attR at bl with Dissolve(.45)
                    
            $ mcEnergy -= 10
                
            play sound2 hitSound
            if enemy == "aiM":
                show aiM neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
            elif enemy == "aiR":
                show aiR neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
            elif enemy == "arM":
                show arM neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
            elif enemy == "boss":
                show boss neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
            elif enemy == "bugeisha":
                show bugeisha neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
            elif enemy == "grunt":
                show grunt neu at br, Shake(None, .25, dist=15) with Dissolve(.25)
            elif enemy == "shou":
                show shou mech at br, Shake(None, .25, dist=15) with Dissolve(.25)
                
            show mc mech at bl with Dissolve(.1)
            
                
        if survived > score:
            $ score = survived
        
        
    if mode == "overdrive":
        if enemyHP <= -2500:
            jump expression context
    else:
        if enemyHP <= 0:
            jump expression context
            
    if mcEnergy <= 0:
        $renpy.pause(2.5)
        jump expression context
    else:
        jump qte_game

label failure:
    
    $ bloSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Block.ogg', 'audio/sfx/GEAR Combat/Block.ogg' ])
    $ dodSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Dodge.ogg', 'audio/sfx/GEAR Combat/Dodge.ogg' ])
    $ fistSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Power Fist Attack 1.ogg', 'audio/sfx/GEAR Combat/Power Fist Attack 2.ogg' ])
    $ hitSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Hit.ogg', 'audio/sfx/GEAR Combat/Hit.ogg' ])
    $ rifSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Rifle.ogg', 'audio/sfx/GEAR Combat/Rifle.ogg' ])
    $ smgSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/SMG.ogg', 'audio/sfx/GEAR Combat/SMG.ogg' ])
    $ sw1Sound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Sword Single.ogg', 'audio/sfx/GEAR Combat/Sword Single.ogg' ])
    $ sw2Sound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Sword Double.ogg', 'audio/sfx/GEAR Combat/Sword Double.ogg' ])
    
    
    
    $ mcEnergy -= 10
    $ survived = 0
    
    if mode == "overdrive":
        if enemy == "aiM":
            play sound sw2Sound
            show aiM att at br with Dissolve(.25)
        elif enemy == "aiR":
            play sound smgSound
            show aiR att at br with Dissolve(.25)
        elif enemy == "arM":
            play sound sw2Sound
            show arM att at br with Dissolve(.25)
        elif enemy == "boss":
            play sound sw2Sound
            show boss att at br with Dissolve(.25)
        elif enemy == "bugeisha":
            play sound sw1Sound
            show bugeisha att at br with Dissolve(.25)
        elif enemy == "grunt":
            play sound sniSound
            show grunt att at br with Dissolve(.25)
        elif enemy == "shou":
            play sound smgSound
            show shou att at br with Dissolve(.25)
            
        play sound2 hitSound
        show mco neuFist at bl, Shake(None, .25, dist=15) with Dissolve(.25)
                
        if enemy == "aiM":
            show aiM neu at br with Dissolve(.1)
        elif enemy == "aiR":
            show aiR neu at br with Dissolve(.1)
        elif enemy == "arM":
            show arM neu at br with Dissolve(.1)
        elif enemy == "boss":
            show boss neu at br with Dissolve(.1)
        elif enemy == "bugeisha":
            show bugeisha neu at br with Dissolve(.1)
        elif enemy == "grunt":
            show grunt neu at br with Dissolve(.1)
        elif enemy == "shou":
            show shou mech at br with Dissolve(.1)
            
    else:    
        if enemy == "aiM":
            play sound sw2Sound
            show aiM att at br with Dissolve(.25)
        elif enemy == "aiR":
            play sound smgSound
            show aiR att at br with Dissolve(.25)
        elif enemy == "arM":
            play sound sw2Sound
            show arM att at br with Dissolve(.25)
        elif enemy == "boss":
            play sound sw2Sound
            show boss att at br with Dissolve(.25)
        elif enemy == "bugeisha":
            show bugeisha att at br with Dissolve(.25)
        elif enemy == "grunt":
            play sound sniSound
            show grunt att at br with Dissolve(.25)
        elif enemy == "shou":
            play sound smgSound
            show shou att at br with Dissolve(.25)
            
        play sound2 hitSound
        show mc mech at bl, Shake(None, .25, dist=15) with Dissolve(.25)
        
        if enemy == "aiM":
            show aiM neu at br with Dissolve(.1)
        elif enemy == "aiR":
            show aiR neu at br with Dissolve(.1)
        elif enemy == "arM":
            show arM neu at br with Dissolve(.1)
        elif enemy == "boss":
            show boss neu at br with Dissolve(.1)
        elif enemy == "bugeisha":
            show bugeisha neu at br with Dissolve(.1)
        elif enemy == "grunt":
            show grunt neu at br with Dissolve(.1)
        elif enemy == "shou":
            show shou mech at br with Dissolve(.1)
        
    #$ failCount +=1
    #if failCount == 3:
        #"GAME OVER"
        #return
    if mcEnergy <= 0:
        $renpy.pause(2.5)
        jump expression context
    else:
        jump qte_game

##### TEST CODE #####

# Below is some test code you can use to test all aspects of this particular minigame

#    $ qtebase = 10
#    $ qtetotal = qteath + qtebase
#    $ t_var = qtetotal
#    jump testArena
#    label testArena:
#        scene bg battleground day with fade
#        show mc mech at bl with dissolve:
#            xzoom -1
#        show aiR neu at br with dissolve
#        "Ready?"
#        "Let's fight!"
#        $ survived = 0
#        $ enemy = "aiR"
#        $renpy.pause(1)
#        #"Simulator starts, standard protocols. Just for now, MC doesn't have attack art assets finished."
#        show screen timer_scrReaction(place="testEnd1")
#        jump qte_game
#        label testEnd1:
#            "Alright, we're finished with 1."
#        $ survived = 0
#        $ enemy = "aiM"
#        $ mode = "retreat"
#        hide aiR with dissolve
#        $renpy.pause(1)
#        show aiM neu at br with dissolve
#        #"Simulator starts, gamplay only block/dodge options"
#        # This means only using block/dodge visuals/sounds, no attacks.
#        show screen timer_scrReaction(place="testEnd2")
#        jump qte_game
#        label testEnd2:
#            "Alright, we're finished with 2."
#        $ survived = 0
#        $ mode = "overdrive"
#        $renpy.pause(1)
#        hide mc
#        show mco mech at bl:
#            xzoom -1
#        with dissolve
#        #"Simulator starts, only good options, even if you time out, only good options."
#        # This means only using attack/dodge visuals/sounds, no blocks.
#        show screen timer_scrReaction(place="testEnd3")
#        jump qte_game
#        label testEnd3:
#            "Alright, we're finished with 3."
#            scene black with fade
#        return
