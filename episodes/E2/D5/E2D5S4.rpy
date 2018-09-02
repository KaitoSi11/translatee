#
label E2D5S4:
    
    scene white with fade
    stop music fadeout 10
    scene bg campus arena day with Dissolve(1)
    
    "As we enter the arena in our GEARs, the first thing I notice is the packed stadium. This is still a top 25 team intramural match so it makes sense people would come out to watch."
    "My heart pounds in my chest. {w}This is our first match against live opponents. The anticipation is both exciting and nerve-wracking."
    play music "audio/music/Fight Song 1 (GAME VERSION).ogg" fadein 3
    #Fade in game and then show your mechs, then pan to the enemy.
    show bg battleground day with dissolve:
        alpha 1
        xzoom 1
        yzoom 1
        yoffset 25
        xoffset 225
        
    show mayu mech at tl with dissolve:
        xzoom -.8
        yzoom .8
    show shou mech at tr with dissolve:
        xzoom -.8
        yzoom .8
    show kaori mech at mm with dissolve:
        xzoom -1
    show mc mech at bl with dissolve:
        xzoom -1
        
    "The enemy team enters from the other side of the arena."
    show bg battleground day:
        parallel:
            easein 3.0 alpha 1.0
        parallel:
            easein 3.0 xoffset -225
            
    show mayu mech at tl:
        xzoom -.8
        yzoom .8
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset -1500
            
    show shou mech at tr:
        xzoom -.8
        yzoom .8
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset -1500
            
    show kaori mech at mm:
        xzoom -1
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset -1300
            
    show mc mech at bl:
        xzoom -1
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset -1300
            
    #$renpy.pause(1.5)
    #show grunt neu at tr with dissolve:
    #    xzoom .8
    #    yzoom .8
    #        
    #show grunt2 neu at tl with dissolve:
    #    xzoom .8
    #    yzoom .8
    #        
    #show boss neu at mm with dissolve
    #        
    #show grunt3 neu at br with dissolve
    
    scene black with Dissolve(1.5)
    $renpy.pause(.75)
    $ persistent.gpix[8][0] = 1
    scene cg GEAR Tatsuo with fade
    
    $renpy.pause(1.5)
    voice "audio/voice/E2/D5/S4/Tastuo/1.ogg"
    tk "RAYS OF JUSTICE ILLUMINATE THE BATTLEFIELD. TWO WORTHY PREDATORS ENTER, BUT A SINGLE PHOENIX SHALL RISE FROM THE ASHES OF WAR."
    
    voice "audio/voice/E2/D5/KI/67.ogg"
    ki "Oh my god."
    "I can hear her cringe through her comm."
    voice "audio/voice/E2/D5/SS/57.ogg"
    ss "Isn't he the greatest?!"
    # note
    voice "audio/voice/E2/D5/S4/Tastuo/2.ogg"
    tk "LET GLORY AND HONOR COMMEMORATE THIS DAY, FOR THE CROSSING OF OUR PATHS IS NOTHING SHORT OF DESTINY."
    
    voice "audio/voice/E2/D5/KI/68.ogg"
    ki "I'm changing my intercom to team chat only."
    
    voice "audio/voice/E2/D5/SS/58.ogg"
    ss "We shall face off in what will be told as legend for generations to come!"
    
    voice "audio/voice/E2/D5/KI/69.ogg"
    ki "And muting Shou as well."
    #show grunt att behind boss with dissolve
    #show grunt2 att behind boss with dissolve
    #show grunt3 att behind boss with dissolve
    voice "audio/voice/E2/D5/S4/Tastuo/3.ogg"
    tk "BLOOD AND TEARS WILL BE SHED, FOR GREATNESS DEMANDS THE FIERY CLEANSING OF WEAKNESS."
    scene bg campus arena day with dissolve
    voice "audio/voice/E2/D5/S4/Announcer/1.ogg"
    an "Are you all ready for ACE-2049-11 versus Claw of the Wild?!"
    # crowd sfx?
    "The crowd roars in response."
    voice "audio/voice/E2/D5/S4/Announcer/2.ogg"
    an "That's what I like to hear!"
    "The stadium lights go from red to yellow. My hands clutch my controls."
    voice "audio/voice/E2/D5/S4/Announcer/3.ogg"
    an "And... begin!"
    show bg battleground day with dissolve:
        parallel:
            alpha 1.0
        parallel:
            xoffset -225
            
    show grunt neu at tr:
        xzoom .8
        yzoom .8
            
    show grunt2 neu at tl:
        xzoom .8
        yzoom .8
            
    show boss neu at mm
    show grunt3 neu at br
    with dissolve
    
    #exclamation
    voice "audio/voice/E2/D5/S4/Tastuo/4.ogg"
    tk "RHINOS TAKE CHARGE!"
    # slide animation forward charge, tatsuo first and each one following
    play sound "audio/sfx/GEAR Combat/Thruster Move.ogg" fadeout 1
    show boss att at mm, Shake(None, 1, dist=20):
        parallel:
            easeout .5 alpha 1.0
        parallel:
            easeout .5 xoffset -1750
    $renpy.pause(.1)
    play sound2 "audio/sfx/GEAR Combat/Thruster Move.ogg" fadeout 1
    show grunt2 att at tl, Shake(None, 1, dist=20) behind boss:
        parallel:
            easeout .5 alpha 1.0
        parallel:
            easeout .5 xoffset -1750
    $renpy.pause(.1)
    play sound "audio/sfx/GEAR Combat/Thruster Move.ogg" fadeout 1
    show grunt att at tr, Shake(None, 1, dist=20) behind boss:
        parallel:
            easeout .5 alpha 1.0
        parallel:
            easeout .5 xoffset -1750
    $renpy.pause(.1)
    play sound2 "audio/sfx/GEAR Combat/Thruster Move.ogg"
    show grunt3 att at br, Shake(None, 1, dist=20):
        parallel:
            easeout .5 alpha 1.0
        parallel:
            easeout .5 xoffset -1850
    $renpy.pause(1)
    scene black with fade
    "As expected, their entire team does a full blitz towards us."
    # show our team again
    show bg battleground day with dissolve:
        alpha 1
        xzoom 1
        yzoom 1
        yoffset 25
        xoffset 225
        
    show mayu mech at tl:
        xzoom -.8
        yzoom .8
    show shou mech at tr:
        xzoom -.8
        yzoom .8
    show kaori mech at mm:
        xzoom -1
    show mc mech at bl:
        xzoom -1
    with dissolve
    
    voice "audio/voice/E2/D5/KI/70.ogg"
    ki "Focus and follow the plan."
    "All our comms flash green in affirmation."
    
    if E2D5S3_Distraction == "MC":
        show mc ready with dissolve
        pf "I'm breaking off now."
        voice "audio/voice/E2/D5/KI/71.ogg"
        ki "Okay, keep them busy as long as you can."
        pf "Right."
        voice "audio/voice/E2/D5/SS/59.ogg"
        ss "Good luck!"
        # slide forward animation
        play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
        show mc ready at bl, Shake(None, 1, dist=20) behind kaori:
            xzoom -1
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 1750
        $renpy.pause(1)
        scene black with fade
        "I separate from the group."
        # show mc by themself
        scene bg battleground day with fade
        show mc mech at bl with dissolve:
            xzoom -1
        voice "audio/voice/E2/D5/S4/Tastuo/5.ogg"
        tk "A STRAY SHEEP!"
        # show the two grunts
        show boss att at tr:
            xoffset 2000
            xzoom .5
            yzoom .5
        show grunt att at tr:
            xoffset 1250
            xzoom .75
            yzoom .75
        show grunt2 att at br:
            xoffset 1250
        show grunt3 att at tr:
            xoffset 2000
            xzoom .5
            yzoom .5
        show boss att at tr, Shake(None, 1, dist=20) behind mc, grunt:
            parallel:
                easeout 3 alpha 1.0
            parallel:
                easeout 3 xoffset -3000
        $renpy.pause(.15)
        show grunt att at tr, Shake(None, 1, dist=20) behind grunt2:
            parallel:
                easeout 1 alpha 1.0
            parallel:
                easeout 1 xoffset 250

        show grunt2 att at br, Shake(None, 1, dist=20):
            parallel:
                easeout 1 alpha 1.0
            parallel:
                easeout 1 xoffset 0

        $renpy.pause(1)
        show grunt3 att at tr, Shake(None, 1, dist=20) behind mc, grunt:
            parallel:
                easeout 3 alpha 1.0
            parallel:
                easeout 3 xoffset -3000
        "Two enemy GEARs divert their course and charge towards me."
        show mc ready at bl with dissolve
        voice "audio/voice/E2/D5/SS/60.ogg"
        ss "One of them didn't take the bait."
        voice "audio/voice/E2/D5/KI/72.ogg"
        ki "Put suppressive fire between Tatsuo and the other GEAR. Force it to separate and disengage."
        # shooting sfx
        play sound smgSound
        $renpy.pause(.1)
        play sound2 sniSound
        # show the last grunt slide behind mc from offscreen
        show grunt3 neu at tl with dissolve:
            xoffset -1000
            xzoom -.7
            yzoom .7
        show grunt3 att at tl, Shake(None, 1, dist=20) behind mc:
            parallel:
                easeout 2 alpha 1.0
            parallel:
                easeout 1 xoffset -300
        "Mayu and Shou unload a hail of energy beams. With no clear path for the adversary GEAR to go, it changes course to me."
        voice "audio/voice/E2/D5/SS/61.ogg"
        ss "It worked!"
        voice "audio/voice/E2/D5/KI/73.ogg"
        ki "Focus!"
        voice "audio/voice/E2/D5/SS/62.ogg"
        ss "Sorry."
        voice "audio/voice/E2/D5/KI/74.ogg"
        ki "Converge onto Tatsuo now."
        voice "audio/voice/E2/D5/KI/75.ogg"
        ki "And you, keep the rest locked down as long as you can!"
        show mc ready with dissolve
        pf "Engaging them now."
        
        scene black with fade
        "I'm soon surrounded by three enemy GEARs. {w}At least the trap worked. Tatsuo won't be able to run unless he wants to be shot at his flank."
        
        
        # show default battle 1-on-1 screen with mc and a grunt, stay ready pose
        scene bg battleground day with fade
        show mc mech at br with dissolve:
            xoffset -800
            xzoom -1

        show grunt neu at bl with dissolve:
            xoffset 500
            yoffset 0
            xzoom 1
            yzoom 1
            
        show grunt2 neu at br with dissolve:
            xoffset -100
        
        show grunt3 neu at br with dissolve:
            xoffset 275
            
        pf "Alright, let's do this."
        #show mc ready at bl with dissolve
        
        #It's going to be 3 battles back to back. It will be difficult to win all 3 but possible. These are the results after.
        #$ comradeKaori = 0
        #$ comradeMayu = 0
        #$ comradeShou = 0
        
        #$ context = "E2D5S4_Solo1st"
        #$ enemy = "grunt"
        #$ mode = "default"
        #$ survived = 0
        #$ score = 0
        
        #$ mcEnergyMax = 200
        #$ mcEnergy = 200
        
        #$ enemyHPMax = 150
        #$ enemyHP = 150
            
        #show screen battle_screen
        #$renpy.pause(1)
        #jump qte_game
        
        
        
        #label E2D5S4_Solo1st:
        #    $ renpy.hide_screen ("battle_screen")
        #    if mcEnergy <= 0:
        #        $ E2D5S4_Gladiator = 0
        #        $ E2D5S4_Victory = 0
        #        
        #    else:
        #        $ context = "E2D5S4_Solo2nd"
        #        hide grunt with dissolve
        #        $renpy.pause(1)
        #        show mc mech at bl with dissolve:
        #            xoffset 0
        #            xzoom -1
        #        $ enemyHP = 150
        #        show grunt neu at br with dissolve:
        #            xoffset 0
        #            yoffset 0
        #            xzoom 1
        #            yzoom 1
        #        show mc ready with dissolve
        #        show screen battle_screen
        #        $renpy.pause(1)
        #        jump qte_game
        #        
        #        label E2D5S4_Solo2nd:
        #            $ renpy.hide_screen ("battle_screen")
        #            if mcEnergy <= 0:
        #                $ E2D5S4_Gladiator = 0
        #                $ E2D5S4_Victory = 0
        #                
        #            else:
        #                $ context = "E2D5S4_Solo3rd"
        #                hide grunt with dissolve
        #                $renpy.pause(1)
        #                show mc mech at bl with dissolve:
        #                    xoffset 0
        #                    xzoom -1
        #                $ enemyHP = 150
        #                show grunt neu at br with dissolve:
        #                    xoffset 0
        #                    yoffset 0
        #                    xzoom 1
        #                    yzoom 1
        #                show mc ready with dissolve
        #                show screen battle_screen
        #                $renpy.pause(1)
        #                jump qte_game
        #                
        #                label E2D5S4_Solo3rd:
        #                    $ renpy.hide_screen ("battle_screen")
        #                    if mcEnergy <= 0:
        #                        $ E2D5S4_Gladiator = 0
        #                        $ E2D5S4_Victory = 0
        #                        
        #                    else:
        #                        $renpy.pause(1)
        #                        $ E2D5S4_Gladiator = 1
        #                        $ E2D5S4_Victory = 1
      
        
        
        
        menu:
            "{i}DEAD BLOSSOM{/i} IS READY.":
                $ E2D5S4_Gladiator = 1
                $ E2D5S4_Victory = 1
            
                play sound rangeSound
                show mc attR at br, Shake(None, .25, dist=10) with Dissolve(.30):
                    xoffset -800
                #play sound3 hitSound
                play sound2 hitSound

                play sound rangeSound
                show mc attR at br, Shake(None, .25, dist=15) with Dissolve(.30):
                    xoffset -815
                play sound2 hitSound
                
                play sound rangeSound
                #play sound3 hitSound
                show mc attR at br, Shake(None, .25, dist=30) with Dissolve(.30):
                    xoffset -830

                play sound2 hitSound

                play sound rangeSound
                play sound3 hitSound
                show mc attR at br, Shake(None, .25, dist=20) with Dissolve(.30):
                    xoffset -845

                play sound2 hitSound
                
                play sound rangeSound
                show mc attR at br, Shake(None, .25, dist=10) with Dissolve(.30):
                    xoffset -860

                play sound2 hitSound
                #play sound3 hitSound

                play sound rangeSound
                show mc attR at br, Shake(None, .25, dist=15) with Dissolve(.30):
                    xoffset -875

                play sound2 hitSound
                
                play sound rangeSound
                show mc attR at br, Shake(None, .25, dist=30) with Dissolve(.30):
                    xoffset -890

                play sound2 hitSound
                play sound3 hitSound

                play sound rangeSound
                play sound3 hitSound
                show mc attR at br, Shake(None, .25, dist=20) with Dissolve(.30):
                    xoffset -910

                    
                
                play sound2 hitSound
                $renpy.pause(.25)
                play sound3 hitSound
                
                
                
                $renpy.pause(.75)
                
                voice "audio/voice/E1/D4/S4/EagleAI/11_01.ogg"
                GEARpf "Power core at 1\%."
                
                $renpy.pause(1.0)
                
                play sound Depowered
                hide grunt with dissolve
                
                play sound Depowered
                hide grunt2 with dissolve
                
                play sound Depowered
                hide grunt3 with dissolve
                

                
                
            "Play defensive until Overdrive kicks in!":
                "The goal is to buy as much time as possible."
                "I diverge all my energy output to shields and brace myself for the onslaught."

                
                show mc blo with dissolve:
                    xoffset -650
                
                show grunt att:
                    yoffset -50
                    xoffset 650
                    xzoom .9
                    yzoom .9
                show grunt2 att:
                    xzoom 1
                    yzoom 1
                    yoffset 50
                show grunt3 att behind grunt2, grunt:
                    xzoom .75
                    yzoom .75
                    xoffset -25
                    yoffset -200
                with dissolve
                
                

                play sound "audio/sfx/GEAR Combat/SMG.ogg"
                $renpy.pause(.20)
                play sound2 "audio/sfx/GEAR Combat/SMG.ogg"
                $renpy.pause(.20)
                play sound3 "audio/sfx/GEAR Combat/SMG.ogg"
                $renpy.pause(.20)
                
                play sound hitSound
                $renpy.pause(.20)
                play sound2 hitSound
                $renpy.pause(.20)
                play sound3 hitSound
                
                show mc blo at bl, Shake(None, .25, dist=10):
                    xoffset 0
                    xzoom -1
        
                play sound "audio/sfx/GEAR Combat/SMG.ogg"
                $renpy.pause(.20)
                play sound2 "audio/sfx/GEAR Combat/SMG.ogg"
                $renpy.pause(.20)
                play sound3 "audio/sfx/GEAR Combat/SMG.ogg"
                $renpy.pause(.20)
                
                play sound hitSound
                $renpy.pause(.20)
                play sound2 hitSound
                $renpy.pause(.20)
                play sound3 hitSound
                
                show mc blo at bl, Shake(None, .5, dist=20):
                    linear .5 xoffset -50
                    xzoom -1
                    
                play sound "audio/sfx/GEAR Combat/SMG.ogg"
                $renpy.pause(.20)
                play sound2 "audio/sfx/GEAR Combat/SMG.ogg"
                $renpy.pause(.20)
                play sound3 "audio/sfx/GEAR Combat/SMG.ogg"
                $renpy.pause(.20)
                
                play sound hitSound
                $renpy.pause(.20)
                play sound2 hitSound
                $renpy.pause(.20)
                play sound3 hitSound
                
                show mc blo at bl, Shake(None, .75, dist=30):
                    linear .75 xoffset -100
                    xzoom -1
                    
                    
                play sound "audio/sfx/GEAR Combat/SMG.ogg"
                $renpy.pause(.20)
                play sound2 "audio/sfx/GEAR Combat/SMG.ogg"
                $renpy.pause(.20)
                play sound3 "audio/sfx/GEAR Combat/SMG.ogg"
                $renpy.pause(.20)
                
                play sound hitSound
                $renpy.pause(.20)
                play sound2 hitSound
                $renpy.pause(.20)
                play sound3 hitSound
                
                show mc ready at bl, Shake(None, .75, dist=30):
                    linear .75 xoffset -300
                    xzoom -1
        
        
        
        
        
        if E2D5S4_Gladiator == 0:
            #$ comradeKaori = 1
            #$ comradeMayu = 1
            #$ comradeShou = 1
            jump E2D5S4_Defeated
        
        else:
            #$ comradeKaori = 1
            #$ comradeMayu = 1
            #$ comradeShou = 1
            hide grunt with dissolve
            #show mc mech at bl with dissolve:
            #    xoffset 0
            #    xzoom -1
            "A pile of depowered GEARs surround Eagle."
            "I breath heavily as my sweaty palms grip the controls."
            "That was lucky! It doesn't matter how good your offense is if your defense leaves you wide open."
            show mc mech at bl with dissolve
            "I look out to see the entire stadium standing in shock then erupt in applause."
            
            menu:
                "Strike a pose for good publicity!":
                    $ E2D5S4_Style = 1
                    scene bg campus arena day with dissolve
                    "With my weapons at the ready, I morph Eagle into a powerful pose."
                    "The crowd roars even louder! Pleasing the audience will definitely be appreciated by our sponsor."
            
            
                "ARE YOU NOT ENTERTAINED?!":
                    $ E2D5S4_Style = 1
                    scene bg campus arena day with dissolve
                    "My GEAR raises both arms up."
                    pf "Who else wants a piece of me?!"
                    "The crowd begins chanting \"Eagle\" in unison."
            
                "The match isn't over yet.":
                    scene black with fade
                    "This battle isn't done yet. I need to stay focused."
                    
            play music "audio/music/Victory! (GAME VERSION).ogg" fadein 3
            $renpy.pause(1)
            voice "audio/voice/E2/D5/S4/Announcer/4.ogg"
            an "What a match! ACE-2049-11 are the winners!"
            
            scene bg battleground day with fade
            
            if E2D5S4_Style == 1:
                show mc ready at br with dissolve:
                    xzoom -1
                    
            else:
                show mc mech at br with dissolve:
                    xzoom -1
                    
            show shou mech at bl with dissolve:
                xzoom -1
            voice "audio/voice/E2/D5/SS/63.ogg"
            ss "Wait, what? We only just defeated Tatsuo."
            show mayu mech at tl behind shou with dissolve:
                xzoom -.7
                yzoom .7
            voice "audio/voice/E2/D5/MA/0-28.ogg"
            ma "Did he take out {i}three{/i} of them by himself?"
            "My team faces me."
            
            if E2D5S4_Style == 1:
                show mc ready at br with dissolve:
                    xzoom 1
                # squeeze kaori in from offscreen between shou and mayu
                $renpy.pause(1)
                show kaori mech at bl behind shou:
                    xoffset -750
                    yoffset -100
                    xzoom -.9
                    yzoom .9
                    
                show kaori mech at bl:
                    parallel:
                        easeout 1 alpha 1.0
                    parallel:
                        easeout 1 xoffset -250
                # question
                voice "audio/voice/E2/D5/KI/76.ogg"
                ki "... What is that idiot doing?"
                # note
                voice "audio/voice/E2/D5/SS/64.ogg"
                ss "Haha! I love it."
            
            else:
                pf "Excellent work."
                # note
                voice "audio/voice/E2/D5/SS/65.ogg"
                ss "That's my line for you!"
                
            jump E2D5S4_End
    
    
    
    
    if E2D5S3_Distraction == "Kaori":
        $ comradeKaori = 0
        voice "audio/voice/E2/D5/KI/77.ogg"
        ki "I'll divert my movement. You guys stay in a tight formation."
        voice "audio/voice/E2/D5/MA/0-29.ogg"
        ma "Affirmative."
        voice "audio/voice/E2/D5/SS/66.ogg"
        ss "Roger that."
        pf "Got it."
        play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
        show kaori att at mm, Shake(None, 1, dist=20):
            xzoom -1
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 1750
        show mc ready at bl with dissolve
        show mayu att at tl behind mc
        show shou att at tr behind mc
        with dissolve
        "Kaori veers to the side while the rest of us stay in a close pattern."
        voice "audio/voice/E2/D5/S4/Tastuo/6.ogg"
        tk "ONE ESCAPES THE HERD!"
        "Two enemy GEARs split off and head towards Kaori."
        # drop
        voice "audio/voice/E2/D5/SS/67.ogg"
        ss "Crap, it looks like they aren't all falling into our trap."
        ki "Put suppressive fire between Tatsuo and the other GEAR. Force it to separate and disengage."
        play sound smgSound
        $renpy.pause(.1)
        play sound2 sniSound
        scene bg campus arena day with dissolve
        "Mayu and Shou unload a hail of energy beams. With no clear path for the adversary GEAR to go, it changes course to Kaori."
        voice "audio/voice/E2/D5/SS/61.ogg"
        ss "It worked!"
        voice "audio/voice/E2/D5/KI/73.ogg"
        ki "Focus!"
        voice "audio/voice/E2/D5/SS/62.ogg"
        ss "Sorry."
        voice "audio/voice/E2/D5/KI/74.ogg"
        ki "Converge onto Tatsuo now."
        voice "audio/voice/E2/D5/KI/78.ogg"
        ki "I'll keep these guys off of you as long as I can."
        pf "Let's go!"
        scene bg battleground day with fade
        show shou mech at tl with dissolve:
            xoffset 100
            xzoom -.7
            yzoom .7
        show mayu mech at bl with dissolve:
            xoffset -100
            yoffset -100
            xzoom -.85
            yzoom .85
        show mc mech at bl with dissolve:
            xzoom -1
        "The three of us burst forward and close in on Tatsuo."
        show boss neu at br with dissolve
        voice "audio/voice/E2/D5/S4/Tastuo/7.ogg"
        tk "A MOUSETRAP TO CATCH A LION?"
        show boss att with dissolve
        "Tatsuo's GEAR enters a fighting stance."
        voice "audio/voice/E2/D5/S4/Tastuo/8.ogg"
        ### VOICE - his line sounds more like "Jurassics"
        tk "YOU FACE JURAXICS, EXEMPLAR LORD OF THE FLAMING LEGION."
        voice "audio/voice/E2/D5/MA/0-30.ogg"
        ma "Um."
        pf "What."
        voice "audio/voice/E2/D5/SS/68.ogg"
        ss "Honestly, even I have no idea."
        pf "Let's just shoot him."
        show shou att behind mc with dissolve
        voice "audio/voice/E2/D5/SS/69.ogg"
        ss "Agreed."
        
        
        
        
        scene black with fade
        scene bg battleground day with fade
        show mc ready at bl:
            xzoom -1
        show boss neu at br
        with dissolve
        
        
        "As Shou and I circle Tatsuo, Mayu hangs back, staying just out of range. She aims and shoots an energy round and Shou follows suit."
        "Tatsuo tries to weave out of the way but I move to block him and raise my sword..."
        
        call E2D5S4TATSUOCALLFIGHT from _call_E2D5S4TATSUOCALLFIGHT
        
        
        #start combat 3 vs 1.
        
        #$ context = "E2D5S4_KaoriGone"
        #$ enemy = "boss"
        #$ mode = "default"
        #$ survived = 0
        #$ score = 0
        
        #$ mcEnergyMax = 200
        #$ mcEnergy = 200
        
        #$ enemyHPMax = 500
        #$ enemyHP = 500
            
        #show screen battle_screen
        #$renpy.pause(1)
        #jump qte_game
        
        #label E2D5S4_KaoriGone:
        #    $ renpy.hide_screen ("battle_screen")
        #    if mcEnergy <= 0:
        #        $ E2D5S4_Victory = 0
        #        
        #    else:
        #        $ E2D5S4_Victory = 1
                
    
        if E2D5S4_Victory == 0:
            $ comradeKaori = 1
            jump E2D5S4_Defeated
        
        else:
            $ comradeKaori = 1
            play sound Depowered
            show boss neu at br, Shake(None, .5, dist=10):
                easeout .5
            hide boss with dissolve
            $renpy.pause(1)
            scene black with fade
            scene bg battleground day with fade
            show mc ready at mm with dissolve:
                xoffset - 200
                xzoom -1
            show shou att at tr behind mc with dissolve:
                xzoom -.7
                yzoom .7
            voice "audio/voice/E2/D5/SS/70.ogg"
            ss "Tatsuo is down! We're coming Kaori."
            "Kaori's health flashes orange before flatlining to red."
            voice "audio/voice/E2/D5/KI/79.ogg"
            ki "I'm down, but there's only one left."
            show grunt att at br with dissolve
            voice "audio/voice/E2/D5/SS/71.ogg"
            ss "Let's go broseph--"
            show mayu att at tl behind mc with dissolve:
                xzoom -.7
                yzoom .7
            #sfx
            play sound sniSound
            show grunt att at br, Shake(None, 1, dist=15):
                easeout .5
            $renpy.pause(.25)
            hide grunt with dissolve
            show shou mech at tr behind mc:
                xzoom .7
            show mc mech at mm:
                xzoom 1
            with dissolve
            "A rail shot flies between Shou and I and obliterates the remaining GEAR. We both turn back to see Mayu with her rifle up."
            voice "audio/voice/E2/D5/MA/0-31.ogg"
            ma "Target neutralized."
            show mayu mech behind mc with dissolve
            stop music fadeout 3
            "..."
        
            play music "audio/music/Victory! (GAME VERSION).ogg" fadein 3
            $renpy.pause(1)
            voice "audio/voice/E2/D5/S4/Announcer/5.ogg"
            an "That snipe, ladies and gentlemen, makes ACE-2049-11 the winners!"
            # dots
            "I sit there dumbfounded. Judging by Shou's silence, he's just as stunned."
            # panic
            voice "audio/voice/E2/D5/MA/0-32.ogg"
            ma "Ah! Sorry, I didn't mean to startle you guys. It's just the GEAR was showing its flank and it was an easy angle..."
            voice "audio/voice/E2/D5/SS/72.ogg"
            ss "You don't need to apologize. That was incredible!"
            # regBlush
            voice "audio/voice/E2/D5/MA/0-33.ogg"
            ma "T-Thanks."
            show kaori mech at bl with dissolve:
                xzoom -1
            voice "audio/voice/E2/D5/KI/80.ogg"
            ki "Good work. You guys played that well."
            pf "Thanks to your plan, Kaori."
            voice "audio/voice/E2/D5/KI/81.ogg"
            ki "Huh? Well, it wasn't just me who came up with it."
            pf "I didn't mean it in a negative way."
            voice "audio/voice/E2/D5/KI/82.ogg"
            ki "I'm not going to take full credit when we all made it together."
            voice "audio/voice/E2/D5/SS/73.ogg"
            ss "... I think he was just trying to compliment you, Kaori."
            # drop
            voice "audio/voice/E2/D5/KI/83.ogg"
            ki "Oh, um... okay."
            voice "audio/voice/E2/D5/SS/74.ogg"
            ss "Nooo, you're suppose to say, \"thank you, broseph-senpai!\"."
            voice "audio/voice/E2/D5/KI/84.ogg"
            ki "Shut up, Shou!"
            # storm
            "We all break into laughter. Except Kaori. {w}Kaori is not amused. {w}Kaori is {i}never{/i} amused."
            jump E2D5S4_End
    
    
    if E2D5S3_Distraction == "Shou":
        $ comradeKaori = 0
        $ comradeMayu = 0
        voice "audio/voice/E2/D5/KI/85.ogg"
        ki "Shou, break off from the group now."
        voice "audio/voice/E2/D5/SS/75.ogg"
        ss "On it."
        play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
        show shou att at tr, Shake(None, 1, dist=20) behind kaori:
            xzoom -1
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 1750
        show mc ready at bl with dissolve
        show mayu att at tl behind mc
        with dissolve
        "Shou's GEAR accelerates away while the rest of us remain in a tight formation."
        voice "audio/voice/E2/D5/S4/Tastuo/9.ogg"
        tk "KINSMAN, FACE ME IN GLORIOUS COMBAT!"
        show grunt att at tr:
            xoffset 1000
            xzoom .75
            yzoom .75
        show grunt2 att at br:
            xoffset 1000
        show grunt3 att at tr:
            xoffset 2000
            xzoom .5
            yzoom .5
        "Tatsuo charges towards Shou while the three remaining GEARs head for us."
        $renpy.pause(.15)
        show grunt att at tr, Shake(None, 1, dist=20) behind grunt2:
            parallel:
                easeout 1 alpha 1.0
            parallel:
                easeout 1 xoffset 250

        show grunt2 att at br, Shake(None, 1, dist=20):
            parallel:
                easeout 1 alpha 1.0
            parallel:
                easeout 1 xoffset 0

        $renpy.pause(1)
        show grunt3 att at tr, Shake(None, 1, dist=20) behind mc, grunt:
            parallel:
                easeout 3 alpha 1.0
            parallel:
                easeout 3 xoffset -3000
                
        voice "audio/voice/E2/missing/shou/4.ogg"
        ss "Crap! He didn't take the bait."
        voice "audio/voice/E2/D5/MA/0-34.ogg"
        ma "Oh no!"
        voice "audio/voice/E2/D5/KI/86.ogg"
        ki "Mayu and I will take care of these guys. You go help Shou!"
        show mc ready with dissolve
        pf "Okay."
        play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
        show mc ready at bl, Shake(None, 1, dist=20) behind kaori, grunt2:
            xzoom -1
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 1750
        $renpy.pause(.5)
        "I activate my thrusters and boost past the enemy GEARs."
        # exclamation
        show grunt2 att with dissolve:
            xzoom -1
        #$renpy.pause(.5)
        # sfx
        show mayu att behind kaori with dissolve
        show grunt2 att at br, Shake(None, 1, dist=20):
            easeout .5
        #$renpy.pause(1)
        show grunt2 neu with dissolve:
            xzoom 1
        "One of them tries to chase me but gets shot in the back by Mayu. It changes focus and turns back towards her and Kaori."
        #$renpy.pause(1)
        scene black with fade
        scene bg battleground day with fade
        show shou att at mm:
            xzoom -1
        show boss att at br:
            xoffset 200
        with dissolve
        show mc ready at bl:
            xzoom -1
            xoffset -600
            
        show mc ready at bl:
            linear .20 xoffset -75
        "Within a few seconds, I reach Shou and Tatsuo who are already locked in combat."

        voice "audio/voice/E2/D5/S4/Tastuo/10.ogg"
        tk "SHOW ME YOUR TRUE POWER!"
        voice "audio/voice/E2/D5/SS/76.ogg"
        ss "Alright, then I will show you..."
        show shou att at mm, behind mc:
            xzoom -1
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -555
        show mc ready at bl:
            xzoom -1
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 300
        "Emerald dodges and boosts next to Eagle."
        voice "audio/voice/E2/D5/SS/77.ogg"
        ss "...The power of friendship!"
        pf "Um, what."
        # drop
        voice "audio/voice/E2/D5/SS/78.ogg"
        ss "Full disclosure, it sounded a lot cooler in my head."
        pf "As do most things."
        voice "audio/voice/E2/D5/SS/79.ogg"
        ss "Rude."
        "Both our GEARs ready against Tatsuo."
        
        
        scene black with fade
        scene bg battleground day with fade
        show mc ready at bl:
            xzoom -1
        show boss neu at br
        with dissolve
        
        
        
        "Shou fires an energy round and Tatsuo dodges. I raise my sword…"
        call E2D5S4TATSUOCALLFIGHT from _call_E2D5S4TATSUOCALLFIGHT_1
        
        
        #start combat 2 vs 1.
        
        #$ context = "E2D5S4_WithShou"
        #$ enemy = "boss"
        #$ mode = "default"
        #$ survived = 0
        #$ score = 0
        
        #$ mcEnergyMax = 200
        #$ mcEnergy = 200
        
        #$ enemyHPMax = 500
        #$ enemyHP = 500
            
        #show screen battle_screen
        #$renpy.pause(1)
        #jump qte_game
        
        #label E2D5S4_WithShou:
        #    $ renpy.hide_screen ("battle_screen")
        #    if mcEnergy <= 0:
        #        $ E2D5S4_Victory = 0
        #        
        #    else:
        #        $ E2D5S4_Victory = 1
        
    
        if E2D5S4_Victory == 0:
            $ comradeKaori = 1
            $ comradeMayu = 1
            jump E2D5S4_Defeated
    
        else:
            $ comradeKaori = 1
            $ comradeMayu = 1
            play sound Depowered
            show boss neu at br, Shake(None, .5, dist=10):
                easeout .5
            hide boss with dissolve
            $renpy.pause(1)
            scene black with fade
            scene bg battleground day with fade
            show mc ready at mm with dissolve:
                xzoom -1
            show shou att at tr behind mc with dissolve:
                xzoom -.7
                yzoom .7
            voice "audio/voice/E2/D5/SS/80.ogg"
            ss "Tatsuo is down! We're coming over now--"
            voice "audio/voice/E2/D5/S4/Announcer/6.ogg"
            an "That's all of them! ACE-2049-11 are the winners!"
            play music "audio/music/Victory! (GAME VERSION).ogg" fadein 3
            $renpy.pause(1)
            show mayu mech at tl behind mc with dissolve:
                xzoom -.7
                yzoom .7
            show kaori mech at bl with dissolve:
                xzoom -1
            show shou mech behind mc:
                xzoom .7
            show mc mech at mm:
                xzoom 1
            with dissolve
            "Shou and I face Mayu and Kaori. Although their GEARs are banged up, it's nothing compared to the depowered mechs surrounding them."
            voice "audio/voice/E2/D5/SS/81.ogg"
            ss "Wow, you guys took them out in a two on three?"
            voice "audio/voice/E2/D5/KI/87.ogg"
            ki "Why do you sound surprised?"
            voice "audio/voice/E2/D5/MA/0-35.ogg"
            ma "Yeah, Shou."
            voice "audio/voice/E2/D5/SS/82.ogg"
            ss "No, I mean--I was thinking..."
            "There is no good outcome from this."
            # drop
            voice "audio/voice/E2/D5/SS/83.ogg"
            ss "... that you guys did a great job! Bravo!"
            voice "audio/voice/E2/D5/KI/88.ogg"
            ki "Now he's being condescending."
            voice "audio/voice/E2/D5/MA/0-36.ogg"
            ma "I know..."
            voice "audio/voice/E2/D5/SS/84.ogg"
            ss "No I wasn't!"
            voice "audio/voice/E2/D5/KI/89.ogg"
            ki "So we're liars?"
            voice "audio/voice/E2/D5/MA/0-37.ogg"
            ma "Hmph!"
            # storm
            voice "audio/voice/E2/D5/SS/85.ogg"
            ss "Ahhh!"
            "I shake my head. He fell right into that."
            jump E2D5S4_End
    
    
    label E2D5S4_Defeated:
        stop music fadeout 5
        voice "audio/voice/E2/D5/S4/Eagle/1.ogg"
        GEARpf "Energy at 0 percent. Eagle depowering."
        pf "?!"
        scene black with fade
        "As my GEAR kneels to the ground, my displays go black for a second before entering spectator mode. {w}Tatsuo is taken out shortly after my fall. The rest of my team engages the remaining targets."
        play ambient "audio/ambience/GEAR Cockpit.ogg" fadein 3
        scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        "I can't help but wonder why the overdrive mode didn't activate like last time."
        
        pf "Eagle, why did you not initiate the Emergency Power Core Protocol?"
        voice "audio/voice/E2/D5/S4/Eagle/2.ogg"
        GEARpf "Protocol EPC was unavailable."
        pf "What do you mean by \"it was unavailable\"?"
        voice "audio/voice/E2/D5/S4/Eagle/3.ogg"
        GEARpf "Requested diagnostic data unavailable."
        pf "That's really helpful, thanks."
        voice "audio/voice/E2/D5/S4/Eagle/4.ogg"
        GEARpf "Sarcasm detected."
        pf "An astute observation."
        voice "audio/voice/E2/D5/S4/Eagle/4.ogg"
        GEARpf "Sarcasm detected."
        pf "Okay, stop."
        voice "audio/voice/E2/D5/S4/Eagle/5.ogg"
        GEARpf "Affirmative."
        "I'll have to look into details about protocol EPC. It would have come in handy in a situation like this."
        
        voice "audio/voice/E2/D5/S4/Announcer/7.ogg"
        an "Match complete. ACE-2049-11 are the winners!"
        play music "audio/music/Victory! (GAME VERSION).ogg" fadein 3
        "I blink as the \"Victory\" prompt scrolls across my displays." 
    
        if E2D5S3_Distraction == "MC":
            scene bg campus arena day with dissolve
            "The crowd erupts into cheers. {w}Looks like the plan worked without a hitch!"
            voice "audio/voice/E2/D5/KI/90.ogg"
            ki "Good work everyone."
            voice "audio/voice/E2/D5/SS/86.ogg"
            ss "Especially Mr. Broseph! You kept them busy enough to let us do our thing and sweep up the rest."
            voice "audio/voice/E2/D5/MA/0-38.ogg"
            ma "Yes, thank you!"
            pf "Heh, no problem."
            stop ambient fadeout 3
            jump E2D5S4_End
    
        elif E2D5S3_Distraction == "Kaori":
            scene bg campus arena day with dissolve
            "The crowd erupts into cheers. {w}Looks like the plan worked for the most part, but I underestimated how well Tatsuo would do in a three on one."
            voice "audio/voice/E2/D5/KI/91.ogg"
            ki "How did you get depowered in a three on one when {i}you{/i} were part of the {i}three{/i} against the one?"
            "Before I have a chance to answer, Shou chimes in."
            voice "audio/voice/E2/D5/SS/87.ogg"
            ss "Kaori, you took out {i}two{/i} GEARs in a three on one as well."
            voice "audio/voice/E2/D5/KI/92.ogg"
            ki "Yes, but--"
            voice "audio/voice/E2/D5/SS/88.ogg"
            ss "No buts! Aren't you the one who said it's about the match and not the individual battle?"
            ki "..."
            scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            "Wow. {w}Did Shou really manage to leave Kaori speechless?"
            voice "audio/voice/E2/D5/SS/89.ogg"
            ss "Who cares about the details? The important thing is we won!"
            voice "audio/voice/E2/D5/MA/0-39.ogg"
            ma "Yeah, that's right!"
            voice "audio/voice/E2/D5/KI/93.ogg"
            ki "Well, that is true..."
            "Kaori composes herself."
            voice "audio/voice/E2/D5/KI/94.ogg"
            ki "Good job everyone, even you."
            pf "Thanks, I think?"
            stop ambient fadeout 3
            jump E2D5S4_End
    
        elif E2D5S3_Distraction == "Shou":
            scene bg campus arena day with dissolve
            "The crowd erupts into cheers. {w}Although they didn't fall for our trap, we were able to react quickly and steal the victory!"
            voice "audio/voice/E2/D5/SS/90.ogg"
            ss "Phew."
            voice "audio/voice/E2/D5/KI/95.ogg"
            ki "That could have gone better, but we responded well to the situation."
            voice "audio/voice/E2/D5/SS/91.ogg"
            ss "I'll say. Sorry that my insider information didn't pan out as expected. Broseph got depowered because of me."
            scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    
            menu:
                "We are a team.":
                    pf "We won the match. That's all that matters."
                    voice "audio/voice/E2/D5/SS/92.ogg"
                    ss "Yeah, that's true."
                    voice "audio/voice/E2/D5/MA/0-40.ogg"
                    ma "Mmhm!"
    
                "You set me up!":
                    pf "I trusted you, Shou."
                    voice "audio/voice/E2/D5/SS/93.ogg"
                    ss "I'm sorry!"
                    pf "{i}I trusted you{/i}!"
                    voice "audio/voice/E2/D5/KI/96.ogg"
                    ki "Don't be so dramatic! We still won."
                    pf "True."
                    voice "audio/voice/E2/D5/MA/0-41.ogg"
                    ma "That's right!"
    
                "Stay silent.":
                    voice "audio/voice/E2/D5/SS/94.ogg"
                    ss "Aren't you going to say anything?"
                    "I remain steadfast in my silence."
                    voice "audio/voice/E2/D5/SS/95.ogg"
                    ss "The silent treatment! Hah, that will never work on me--"
                    $renpy.pause(1)
                    voice "audio/voice/E2/D5/SS/96.ogg"
                    ss "COME ON, BROSEPH DON'T BE LIKE THAT."
                    voice "audio/voice/E2/D5/KI/97.ogg"
                    ki "I think I should do the same."
                    voice "audio/voice/E2/D5/SS/97.ogg"
                    ss "You guys are so mean to me."
                    voice "audio/voice/E2/D5/MA/0-42.ogg"
                    ma "Aw, there there..."
                    "Mayu's GEAR awkwardly pat's Emerald."
                    
            stop ambient fadeout 3
            jump E2D5S4_End
    
    
    label E2D5S4_End:
        "The announcer's voice catches us all by surprise."
        voice "audio/voice/E2/D5/S4/Announcer/8.ogg"
        an "Please exit the arena so we may prepare for the next battle!"
        stop music fadeout 5
        scene black with fade
        show bg battleground day with dissolve:
            alpha 1
            xzoom 1
            yzoom 1
            yoffset 25
            xoffset 225
            
        show mc mech at mm with dissolve:
            xoffset 100
        show mayu mech at tr behind mc:
            xoffset 100
            xzoom .7
            yzoom .7
        show shou mech at br:
            xoffset 100
        with dissolve
        
        show boss neu at bl with dissolve:
            yoffset -50
            xoffset -50
            xzoom -1
        show grunt neu at tr behind mayu:
            xoffset 100
            xzoom .5
            yzoom .5
        show grunt2 neu at tr behind mayu:
            xoffset 350
            xzoom .5
            yzoom .5
        show grunt3 neu at tr behind mayu:
            xoffset 550
            xzoom .5
            yzoom .5
            
        "Still in our GEARs, we make our way to exit when Tatsuo appears before us."
    
        play music "audio/music/Let's Get It Done! (GAME VERSION).ogg" fadein 3
        # note
        voice "audio/voice/E2/D5/S4/Tastuo/11.ogg"
        tk "A WELL FOUGHT BATTLE."
        # note
        voice "audio/voice/E2/D5/SS/98.ogg"
        ss "Yeah, man!"
        voice "audio/voice/E2/D5/S4/Tastuo/12.ogg"
        tk "THE BEAR HIBERNATES TO REGAIN ITS STRENGTH."
        voice "audio/voice/E2/D5/S4/Tastuo/13.ogg"
        tk "BUT WITH POWERFUL RESOLVE, WE WILL RETURN TO CHALLENGE THE KING OF THE WILD."
        show shou att with dissolve
        voice "audio/voice/E2/D5/SS/99.ogg"
        ss "We're up for a rematch anytime, Tatsuo!"
        show shou mech with dissolve
        "Shou and Tatsuo's GEARs shake hands."
        voice "audio/voice/E2/D5/S4/Tastuo/14.ogg"
        tk "THE SUN SETS AND SO WE DEPART."
        show boss att with dissolve
        voice "audio/voice/E2/D5/S4/Tastuo/15.ogg"
        tk "DUCKS, FLY TOGETHER!"
        # SLIDE BABY
        play sound "audio/sfx/GEAR Combat/Thruster Move.ogg" fadeout 1
        show boss att at bl, Shake(None, 1, dist=20) behind mc, shou:
            xzoom -1
            parallel:
                easeout 1 alpha 1.0
            parallel:
                easeout 1 xoffset 2000
        $renpy.pause(1)
        play sound2 "audio/sfx/GEAR Combat/Thruster Move.ogg" fadeout 1
        show grunt3 att at tr, Shake(None, 1, dist=10) behind mc, shou, mayu:
            xzoom -.5
            parallel:
                easeout 1 alpha 1.0
            parallel:
                easeout 1 xoffset 1750
        $renpy.pause(.75)
        play sound "audio/sfx/GEAR Combat/Thruster Move.ogg" fadeout 1
        show grunt2 att at tr, Shake(None, 1, dist=10) behind mc, shou, mayu:
            xzoom -.5
            parallel:
                easeout 1 alpha 1.0
            parallel:
                easeout 1 xoffset 1750
        $renpy.pause(1.5)
        play sound2 "audio/sfx/GEAR Combat/Thruster Move.ogg"
        show grunt att at tr, Shake(None, 1, dist=10) behind mc, shou, mayu:
            xzoom -.5
            parallel:
                easeout 1 alpha 1.0
            parallel:
                easeout 1 xoffset 1750
        "Tatsuo and his teammates all boost out of the arena in a \"V\" shape."
        show kaori mech at br behind shou:
            xoffset 750
            yoffset -100
            xzoom .9
            yzoom .9
            
        show kaori mech at br:
            parallel:
                easeout 1 alpha 1.0
            parallel:
                easeout 1 xoffset 250
        voice "audio/voice/E2/D5/KI/98.ogg"
        ki "I… I can't even."
    
        stop music fadeout 5
        #Fade to black
        scene black with fade
        $renpy.pause(2.5)
        scene bg campus arena day at Zoom((1920, 1080), (0, 0, 2376, 1180), (0, 0, 2376, 1180), 0) with dissolve
        play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    
        "My team and I meet up in the arena stands after exiting our GEARs."
        show kaori neu at r3:
            xzoom -1
        show mayu neu at l3
        show shou neu at cc
        with dissolve
        voice "audio/voice/E2/D5/KI/99.ogg"
        ki "This should help bump us into the top 20. \"Claw of the Wild\" were ranked 18th."
        pf "Well played."
    
        if E2D5S4_Gladiator == 1:
            show shou cur at cc
            "Shou whips around to face me."
            show question:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            show shou ske at cc
            voice "audio/voice/E2/D5/SS/100.ogg"
            ss "How did you manage to depower 3 of them?!"
            
            menu:
                "I tried my best.":
                    pf "Those practice sessions really paid off."
                    show shou smi at cc
            
                "Because I'm [pfull]!":
                    pf "It's what I do."
                    show shou smi at cc
            
                "They had 3 weak links.":
                    pf "Tatsuo was their team carry. The rest weren't as strong."
                    show shou smi at cc
            
            show kaori cur at r3
            show mayu smi at l3
            voice "audio/voice/E2/D5/KI/100.ogg"
            ki "I'll be honest, I didn't expect that from you."
            show kaori mis at r3
            "Kaori is in disbelief, but impressed nonetheless."
            show note:
                xoffset 230
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu hap at l3
            voice "audio/voice/E2/D5/MA/0-43.ogg"
            ma "Yeah! That was really amazing!"
            pf "Thanks."
            show kaori smi at r3
            show mayu smi at l3
            jump E2D5S4_Core
    
        elif E2D5S3_Distraction == "Kaori" and E2D5S4_Victory == 1:
            show note:
                xoffset 230
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu hap at l3
            voice "audio/voice/E2/D5/MA/0-44.ogg"
            ma "I think coming into the match with a strategy helped a lot."
            show note:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            show shou hap at cc
            voice "audio/voice/E2/D5/SS/101.ogg"
            ss "I'll say!"
            show kaori smi at r3
            show mayu smi at l3
            voice "audio/voice/E2/D5/KI/101.ogg"
            ki "That's why we need to do our homework on future teams. We were lucky that Shou was familiar with Tatsuo's playstyle."
            show shou smi at cc
            "We all nod in agreement."
            jump E2D5S4_Core
    
        elif E2D5S3_Distraction == "Shou" and E2D5S4_Victory == 1:
            show note:
                xoffset 230
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu hap at l3
            voice "audio/voice/E2/D5/MA/0-45.ogg"
            ma "Even though they didn't fall into our trap, Kaori saved us with her quick thinking!"
            show kaori smi at r3
            show mayu smi at l3
            voice "audio/voice/E2/D5/KI/102.ogg"
            ki "It's a team effort. You guys didn't panic and followed through with the adjusted tactics."
            
            if E1D4S4_FollowMatchPlan == 0:
                show kaori mis at r3
                "Kaori glances at me."
                voice "audio/voice/E2/D5/KI/103.ogg"
                ki "Which is a surprise coming from you."
                pf "Hey, as long as you don't sideline me, I'm willing to be a team player."
                show kaori thi at r3
                "She crosses her arms."
                
            show note:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            show shou hap at cc
            voice "audio/voice/E2/D5/SS/102.ogg"
            ss "We just have to keep competing like this and we'll be in the top 10 in no time!"
            show kaori smi at r3
            show shou smi at cc
            "We all nod in agreement."
            jump E2D5S4_Core
    
        elif E2D5S4_Victory == 0:
            show shou cur at cc
            voice "audio/voice/E2/D5/SS/103.ogg"
            ss "How's Eagle holding up?"
            
            menu:
                "It's seen better days.":
                    pf "Eh, I don't want to think too much about it."
                    show shou smi at cc
                    voice "audio/voice/E2/D5/SS/104.ogg"
                    ss "Fair enough."
            
                "Who cares? We have a sponsor now.":
                    pf "Does it really matter? Dasshu will take care of the damages."
                    show shou neu at cc
                    voice "audio/voice/E2/D5/SS/105.ogg"
                    ss "I suppose that's true..."
            
                "Scarred with battle wounds… exactly how it should be.":
                    pf "It's showing signs of a well fought battle."
                    show shou hap at cc
                    voice "audio/voice/E2/D5/SS/106.ogg"
                    ss "I like it! Builds character."
                    
            show mayu cur at l3
            voice "audio/voice/E2/D5/MA/0-46.ogg"
            ma "I'm actually a little surprised..."
            show shou smi at cc
            pf "What's up, Mayu?"
            show mayu thi at l3
            voice "audio/voice/E2/D5/MA/0-47.ogg"
            ma "Hm? I was just trying to think of why your overdrive mode didn't activate."
            show bulb:
                xoffset 1175
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori cur at r3
            "Kaori perks up."
            show kaori ske at r3
            show mayu neu at l3
            voice "audio/voice/E2/D5/KI/104.ogg"
            ki "Yeah, the parameters were the same when you were about to get depowered, except this time you {i}did{/i} get depowered."
            show shou thi at cc
            voice "audio/voice/E2/D5/SS/107.ogg"
            ss "Maybe we're missing something?"
            show kaori neu at r3
            pf "I'll have to look into it."
            show shou smi at cc
            voice "audio/voice/E2/D5/SS/108.ogg"
            ss "Hey! We have an engineer now who can help with that."
            show mayu hap at l3
            "Mayu beams."
            show exclamation:
                xoffset 230
                yoffset 135
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D5/MA/0-48.ogg"
            ma "That's right!"
            show mayu smi at l3
            jump E2D5S4_Valerie
    
    
    label E2D5S4_Core:
        show mayu thi at l3
        voice "audio/voice/E2/D5/MA/0-49.ogg"
        ma "Hm..."
        pf "What's up, Mayu?"
        show mayu cur at l3
        "Mayu glances at me."
        show mayu smi at l3
        voice "audio/voice/E2/D5/MA/0-50.ogg"
        ma "Oh, sorry. I was just thinking that your overdrive mode didn't activate this time."
        show bulb:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori cur at r3
        "Kaori perks up."
        show kaori neu at r3
        voice "audio/voice/E2/D5/KI/106.ogg"
        ki "Well, the steps leading up to that during the last match didn't happen this time around."
        show mayu thi at l3
        voice "audio/voice/E2/D5/MA/0-51.ogg"
        ma "That's true..."
        show shou ske at cc
        voice "audio/voice/E2/D5/SS/109.ogg"
        ss "But we still don't know for sure if it {i}would{/i} have activated either."
        show kaori thi at r3
        "Kaori crosses her arms, but looks thoughtful."
        voice "audio/voice/E2/D5/KI/105.ogg"
        ki "It would be useful if we could find out what triggers it."
        show mayu smi at l3
        show shou smi at cc
        pf "Agreed, I plan on looking into it."
        show kaori smi at r3
        voice "audio/voice/E2/D5/KI/107.ogg"
        ki "Maybe you can ask Valerie to help. She seems capable as an engineer."
        jump E2D5S4_Valerie
    
    
    label E2D5S4_Valerie:
        show kaori hap at r3
        voice "audio/voice/E2/D5/KI/108.ogg"
        ki "Speaking of which, I wonder if she was able to watch the match and I wonder if she noticed any more changes she can do to help improve our GEARs."
        show kaori smi at r3
        pf "Good thinking."
        "I pull out my phone to text Valerie but it looks like she already beat me to it."
        
        ### NOTE Bug - some of these chracters aren't showing properly with the font, turning into squares
        
        if E2D5S4_Victory == 0:
            vb "{i}Congrats on the win!! {w}I'm just a little sad Eagle got depowered! o(；△；)o{/i}"
        
        elif E2D5S4_Gladiator == 0:
            vb "{i}Wow! You were incredible!!! Congrats on the win! o(≧ ▽ ≦)o{/i}"
        
        elif E2D5S4_Victory == 1:
            vb "{i}Congrats on the win!! {w}You guys played well together! o(^ o ^)o{/i}"
        
        vb "Anyway, I'll be at the quad for a bit. You should come drop by~"
        pf "She's at the campus quad. We can meet up with her there."
        show shou mis at cc
        voice "audio/voice/E2/D5/SS/110.ogg"
        ss "Let's change out of these suits and go meet her."
        hide kaori
        hide mayu
        hide shou
        with dissolve
        stop music fadeout 5
        
        "We nod and make our way out of the arena stands."
        
        # fadeblack
        scene black with fade
        $renpy.pause(1.5)
        
        $ kaoOut = "sUniform"
        
        $ mayOut = "sUniform"
        
        $ shoOut = "sUniform"
        
        "Shou and I change into our uniforms and meet the girls outside."
        play ambient "audio/ambience/Campus.ogg" fadein 3
        scene bg campus main dusk with fade
        play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
        "Once we reach the quad, I easily spot Valerie with her light blonde hair. {w}I wonder if I stick out just as much?"
        show valerie smi at r3 with dissolve:
            xoffset 200
            xzoom -1
            
        show kaori neu at r1
        show shou neu at l1:
            xoffset -100
        show mayu neu at l3:
            xoffset -275
        with Dissolve(1)
            
        "She grins as we approach."
        show valerie hap at r3
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO24.ogg"
        vb "Oh hey, you came!"
        
        menu:
            "Hello!":
                pf "Hey, Valerie."
                show valerie smi at r3
                "She nods."
                voice "audio/voice/E2/D5/VB/ValerieE2D5REDO25.ogg"
                vb "Looks like you brought company."
                show kaori smi at r1
                show mayu smi at l3
                show shou smi at l1
                "Kaori and Mayu both greet her. Shou offers her a wave."
                voice "audio/voice/E2/D5/MA/0-52.ogg"
                ma "If it's not too much trouble, may we please ask you a couple of questions?"
        
            "I don't usually come so fast.":
                pf "I can come much slower for you next time."
                "I flash her a devilish grin."
                show shou cur at l1 with dissolve
                show shoBlush:
                    xoffset 1375
                    yoffset 125
                    xzoom .75
                    yzoom .75
                show valerie ner b1 at r3 with dissolve
                voice "audio/voice/E2/D5/VB/ValerieE2D5REDO26.ogg"
                vb "Oh my, not in front of the team."
                show valerie mis b1 with dissolve
                show kaori thi at r1
                show mayu thi at l3
                show shou sur b1 at l1 with dissolve
                "She pretends to be shy, but she's not fooling me. {w}Shou is speechless and fully red. Kaori and Mayu frown."
                voice "audio/voice/E2/D5/KI/109.ogg"
                ki "Why would you do that? If you came faster, you'd save time."
                show valerie sur b1 with dissolve
                show mayu neu at l3
                show shou thi b1 at l1
                voice "audio/voice/E2/D5/SS/111.ogg"
                ss "Oh my god."
                show valerie hap b1 at r3 with dissolve
                "Valerie and I glance at Kaori and then at each other before laughing."
                show shou hap at l1 with dissolve
                show question:
                    xoffset 890
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori ske at r1 with dissolve
                voice "audio/voice/E2/D5/KI/110.ogg"
                ki "W-What's so funny?!"
                show mayu sad at l3
                voice "audio/voice/E2/D5/MA/0-53.ogg"
                ma "I don't get it either..."
                show kaori dis at r1
                show shou smi at l1
                show valerie smi b1 at r3
                "After a couple of failed attempts, we manage to recompose ourselves. Kaori crosses her arms, still looking wary."
                show kaori neu at r1
                show mayu neu at l3
                voice "audio/voice/E2/D5/KI/111.ogg"
                ki "Anyway, Valerie, we'd like to ask you a couple of questions."
        
            "We have a couple of questions.":
                pf "Hi, there are a few things we'd like to ask you."
        
        show valerie hap at r3 with dissolve
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO27.ogg"
        vb "Sure! What's up?"
        voice "audio/voice/E2/D5/KI/112.ogg"
        ki "Did you watch the match?"
        show valerie smi at r3
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO28.ogg"
        vb "Of course! Actually, I wanted to talk with you guys about a few ideas I have in mind to improve your GEAR performance."
        show kaori cur at r1
        "Kaori looks pleasantly surprised."
        voice "audio/voice/E2/D5/KI/113.ogg"
        ki "Really?"
        show note:
            xoffset 1375
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO29.ogg"
        vb "Mmhm. I'm drafting up the plans for the improvements, but there are still a few calculations to do. I'll have a completed report done in a few days!"
        show kaori hap at r1
        show shou cur at l1
        voice "audio/voice/E2/D5/KI/114.ogg"
        ki "Oh, wow, that would be great."
        "Shou is just as surprised."
        show shou mis at l1
        voice "audio/voice/E2/D5/SS/112.ogg"
        ss "Someone managed to impress Kaori! I thought the day would never come."
        show vein:
            xoffset 890
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori ang at r1
        show valerie cur at r3
        voice "audio/voice/E2/D5/KI/115.ogg"
        ki "Shut up, Shou!"
        show kaori ann at r1
        show mayu smi at l3
        show valerie hap at r3
        "Valerie stifles a giggle with her hand. Mayu also cracks a smile."
        show kaori neu at r1
        show shou smi at l1
        "Kaori turns back to Valerie."
        voice "audio/voice/E2/D5/KI/116.ogg"
        ki "Did you watch the qualifier matches last week too?"
        show valerie smi at r3
        "Valerie nods."
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO30.ogg"
        vb "The \"overdrive mode\"... You're wondering how it works?"
        "That piqued my interest."
        pf "You know?"
        show valerie thi at r3
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO31.ogg"
        vb "Not yet. I was hoping I could research your core."
        show valerie mis at r3
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO32.ogg"
        vb "With your permission, of course."
        "She winks at me."
        "Although I don't appreciate her snooping, having her investigate this phenomenon will be a huge benefit."
        pf "With supervision, sure."
        show valerie dis at r3
        "Valerie pouts playfully."
        show storm:
            xoffset 1375
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO33.ogg"
        vb "Ohhh, fine."
        voice "audio/voice/E2/D5/KI/117.ogg"
        ki "Those are all the questions I had."
        show valerie neu at r3
        "An awkward silence settles.{w} Shou suddenly speaks up."
        show shou mis at l1
        voice "audio/voice/E2/D5/SS/113.ogg"
        ss "Alright, there's only one thing left to do."
        show kaori ske at r1
        voice "audio/voice/E2/D5/KI/118.ogg"
        ki "What's that?"
        show exclamation:
            xoffset 415
            yoffset 20
            xzoom .75
            yzoom .75
        show shou hap at l1
        voice "audio/voice/E2/D5/SS/114.ogg"
        ss "Celebrate our victory! Party at my place!"
        show valerie hap at r3
        "Valerie giggles in excitement."
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO34.ogg"
        vb "Count me in!"
        voice "audio/voice/E2/D5/SS/115.ogg"
        ss "That's the spirit!"
        show shou smi at l1
        show valerie smi at r3
        voice "audio/voice/E2/D5/SS/116.ogg"
        ss "What about the rest of you?"
        show dots:
            xoffset 890
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori neu at r1
        show mayu ner at l3
        "Simultaneously, Kaori and Mayu shake their heads."
        voice "audio/voice/E2/D5/MA/0-54.ogg"
        ma "I'm not really the partying type..."
        voice "audio/voice/E2/D5/KI/119.ogg"
        ki "I don't think so."
        show shou mis at l1
        voice "audio/voice/E2/D5/SS/117.ogg"
        ss "Come on, this is our first victory together… as a team."
        pf "Uh, didn't we win the last round?"
        "He spreads his arms wide, gesturing to everyone around him, and emphasises Valerie."
        show shou hap at l1
        show valerie cur at r3
        voice "audio/voice/E2/D5/SS/118.ogg"
        ss "As a team."
        show valerie hap at r3
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO35.ogg"
        vb "Aww, I'm part of the team."
        show kaori ske at r1
        show mayu wor at l3
        "Shou pulls all of us into a hug. Kaori immediately wriggles free and tries to protest, but Shou speaks before she can."
        show valerie smi at r3
        voice "audio/voice/E2/D5/SS/119.ogg"
        ss "I won't take no for an answer. As my father always says, \"a team that parties together, wins together\"."
        show mayu neu at l3
        voice "audio/voice/E2/D5/MA/0-55.ogg"
        ma "He doesn't say that."
        show shou mis at l1
        voice "audio/voice/E2/D5/SS/120.ogg"
        ss "Well, he could have in a past life or something."
        show shou smi at l1
        voice "audio/voice/E2/D5/SS/121.ogg"
        ss "Sooooo, does this mean we should go now?"
        show mayu smi at l3
        voice "audio/voice/E2/D5/MA/0-56.ogg"
        ma "I suppose if everyone's going I can go too."
        show storm:
            xoffset 890
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori neu at r1
        "Kaori sighs."
        voice "audio/voice/E2/D5/KI/120.ogg"
        ki "Fine, but only for a little bit."
        show shou cur at l1
        voice "audio/voice/E2/D5/SS/122.ogg"
        ss "And you're coming too, right, Mr. Broseph?"
        pf "Sure."
        show note:
            xoffset 415
            yoffset 20
            xzoom .75
            yzoom .75
        show shou smi at l1
        voice "audio/voice/E2/D5/SS/123.ogg"
        ss "Let's go then!"
        
        menu:
            "I should invite Yuuna.":
                pf "Hey, Shou, I'm going to text Yuuna. Maybe she'd like to go too."
                show shou hap at l1
                voice "audio/voice/E2/D5/SS/124.ogg"
                ss "Good idea! Then the whole team really will party together!"
                hide kaori
                hide mayu
                hide shou
                hide valerie
                with dissolve
                "When I check my phone, there's a message already waiting for me from Yuuna."
                "{i}Congratulations on your victory! Your GEARs looked so good out there btw ^^{/i}"
                "Heh. Holding back a smile, I reply to her text."
                "{i}Thanks! We're all going to Shou's dorm to celebrate. You should come!{/i}"
                "Yuuna responds immediately."
                "{i}I would, but I already have plans ^^;{/i}"
                "{i}Next time for sure! Have fun!{/i}"
        
            "Don't invite Yuuna.":
                "Yuuna briefly flashes across my mind, but I decide against inviting her. She was really uncomfortable around the team earlier and I don't want to put her in an awkward position."
                hide kaori
                hide mayu
                hide shou
                hide valerie
                with dissolve
                
        stop music fadeout 3
        scene black with fade
        stop ambient fadeout 3
        "Shou lets go of everyone and leads the way. Valerie keeps pace with him, while the rest of us hang back, a little unsure of what we just agreed to."
        
        #bg change
        # party ambient?
        play ambient "audio/ambience/Pilot Lounge.ogg" fadein 3 # Pilot Lounge fine for now
        # what music is good?
        scene bg campus dorm night with fade:
            xzoom .9
            yzoom .9
        play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
        show studentM extra at l3
        show studentM2 extra at r3
        with dissolve
        show shou smi at cc with dissolve
        "As soon as we step foot into the house, Shou is surrounded by his {i}brosephs{/i}, all of whom shower him with praises and congratulations."
        
        voice "audio/voice/E2/D5/SS/125.ogg"
        ss "Thanks guys! How's Tatsuo and company?"
        voice "audio/voice/E2/D5/S4/stu8m/1.ogg"
        stu8m "Tatsuo took them to a \"FORBIDDEN HOT SPRING TO RECOVER FLESH WOUNDS AND REINVIGORATE THEIR INNER CHI\"."
        show shou mis at cc
        voice "audio/voice/E2/D5/KI/121.ogg"
        ki "Oh god…"
        voice "audio/voice/E2/D5/SS/126.ogg"
        ss "That sounds like him!"
        show shou hap at cc
        "They burst into laughter."
        
        hide shou with dissolve
        hide studentM
        hide studentM2
        with dissolve
        
        "The place is already crowded with pilots from other dorms, and more keep filing in at a steady pace."
        
        "Everyone fans out. Mayu sticks close to Shou, while Valerie makes a dive for the kitchen. A dark-haired female pilot walks past us and greets Kaori. She seems really familiar… Was she checking the leaderboards while I was in the Pilot's Lounge?{w} Either way, Kaori scowls when she sees the girl, who just laughs and grabs Kaori's arm, dragging her into the throng of people."
        "I push my way past the living room and hear music coming from a short staircase leading to the lower level. It's dark, but strobes of coloured light flash from below. Sounds like there's a rave going on. I'm not sure about going down there..."
        
        "Carefully, I weave my way into the kitchen, narrowly avoiding a dousing from a fruity drink. When I arrive, I gawk at the cornucopia of alcohol. "
        "I help myself to…"
        
        menu:
            "Water.":
                $ E2D5S4_Drink = "Water"
                "I'm going to stick with water just to be on the safe side. There are a bunch of bottled waters in the cooler, so I grab one."
        
            "Surprise me.":
                "Besides the obscene amount of beer, there is also plum wine, sake, and whiskey available."
        
                menu:
                    "Plum wine.":
                        $ E2D5S4_Drink = "Wine"
                        "I've never actually had plum wine before. It's not that common in the States, and frankly, kind of girly. Still, I pour a small amount into a cup and hazard a taste."
                        "It's pleasantly sweet, and you can really taste the plums."
        
                    "Sake.":
                        $ E2D5S4_Drink = "Sake"
                        "In the back corner of the alcohol table sits a bottle of sake. Maybe this isn't supposed to be out and available for the guests? {w}Still, it is technically out in the open so it must be fair game."
                        "I pour myself a small amount, and briefly consider warming it up. That's a bit overkill at a party though. Instead, I appreciate the warmth of that first sip."
        
                    "Whiskey.":
                        $ E2D5S4_Drink = "Whiskey"
                        "Going for something a little more familiar, I check out the whiskey collection. Most people don't consider whiskey when they think of Japanese alcohol, but the spirit is popular here, and the Japanese actually distill some high quality whiskey."
                        "I pick a brand I'm familiar with and pour a small amount into my cup."
        
            "Beer.":
                "There is both a keg and cans of beer in the cooler."
        
                menu:
                    "Keg.":
                        $ E2D5S4_Drink = "KegBeer"
                        if MCStory != 2:
                            "I wonder if their kegs are the same as back home."
                            "Grabbing a cup, I fill it with beer from the keg. I take a sip, then grimace."
                            "Yup, exactly the same as back home."
        
                        else:
                            "I've never actually had beer from a keg before. I pour myself a cup and take a sip. Then choke as I try to gag and spit it out at the same time. {w}How can people drink this stuff?"
        
                    "Cooler.":
                        $ E2D5S4_Drink = "CoolerBeer"
                        if MCStory != 2:
                            "Harsh memories of keg parties back home bubble up and I relive the trauma all over again. Better stick with a can. I grab one of my favourites."
        
                        else:
                            "The cooler actually has a pretty varied selection. I choose one of my favourites, and take one last look at the keg. I do not trust kegs. If they aren't stored right they can be undrinkable."

        
        "Now that I have a drink, I should find my friends. Let's look for…"
        
        menu:
            "Kaori":
                jump E2D5KI
            "Valerie":
                jump E2D5VB
            "Mayu":
                jump E2D5MA
            "Shou":
                jump E2D5SS

                
                
                
                
                
label E2D5S4TATSUOCALLFIGHT:
$ qtetotal = 5
$ t_var = qtetotal
show screen timer_scr(place="E2D5S4_TATL1")

menu:
    "Strike!":
        jump E2D5S4_TATW1

    "Fail…":
        $ TATBATTLECOUNTER += 1
        jump E2D5S4_TATL1

    "Attack!":
        jump E2D5S4_TATW1

    "Miss…":
        $ TATBATTLECOUNTER += 1
        jump E2D5S4_TATL1

    "Slash!":
        jump E2D5S4_TATW1


label E2D5S4_TATL1:
    $ renpy.hide_screen ("timer_scr")
    
    show mc ready at bl, Shake(None, 1, dist=20):
        xoffset 0
        xzoom -1
        parallel:
            easeout .1 alpha 1.0
        parallel:
            easeout .1 xoffset 250
    $renpy.pause(.1)

    play sound meleeSound
    show mc attM at bl with Dissolve(.2):
        xoffset 400
            
            
    show boss att at br, Shake(None, 1, dist=20):
        xoffset 0
        parallel:
            easeout .1 alpha 1.0
        parallel:
            easeout .1 xoffset -250
    $renpy.pause(.1)

    play sound meleeSound
    show boss att at br with Dissolve(.2):
        xoffset -400

    show white with Dissolve(0.15):
    play sound2 hitSound
    hide white with Dissolve(0.25)
    
    show mc blo at bl, Shake(None, .5, dist=20):
        parallel:
            easeout .3 alpha 1.0
        parallel:
            easeout .3 xoffset 150
                
            
    "My sword misses its mark and grazes Tatsuo's side. He brushes off my attack then strikes back with a wide swing, aiming for my shoulder. I can't move fast enough to block his attack and I wince as my dashboard flashes warnings."
    "I can't let myself get hit again!"
    jump TATCON1




label E2D5S4_TATW1:
    $ renpy.hide_screen ("timer_scr")
    
    
    show mc ready at bl, Shake(None, 1, dist=20):
        xoffset 0
        xzoom -1
        parallel:
            easeout .1 alpha 1.0
        parallel:
            easeout .1 xoffset 250
    $renpy.pause(.1)

    play sound meleeSound
    show mc attM at bl with Dissolve(.2):
        xoffset 400

    show white with Dissolve(0.15):
    play sound2 hitSound
    hide white with Dissolve(0.25)
    
    show boss blo at br, Shake(None, .5, dist=20):
        parallel:
            easeout .3 alpha 1.0
        parallel:
            easeout .3 xoffset 100
    
    "My sword connects with Tatsuo's side and he's pushed back by the blow. Taking advantage of his moment of weakness, I swing again, but Tatsuo blocks at the last minute."
    jump TATCON1



label TATCON1:
"Tatsuo grips his sword and charges towards me!"


$ qtetotal = 5
$ t_var = qtetotal
show screen timer_scr(place="E2D5S4_TATL2")

menu:
    "Freeze…":
        $ TATBATTLECOUNTER += 1
        jump E2D5S4_TATL2

    "Trip…":
        $ TATBATTLECOUNTER += 1
        jump E2D5S4_TATL2

    "Dodge!":
        jump E2D5S4_TATW2

    "Evade!":
        jump E2D5S4_TATW2

    "Slow…": 
        $ TATBATTLECOUNTER += 1
        jump E2D5S4_TATL2

label E2D5S4_TATL2:
    $ renpy.hide_screen ("timer_scr")
    
    show boss att at br, Shake(None, 1, dist=20):
        xoffset 0
        parallel:
            easeout .1 alpha 1.0
        parallel:
            easeout .1 xoffset -400
    $renpy.pause(.1)

    play sound meleeSound
    show boss att at br with Dissolve(.2):
        xoffset -550

    show white with Dissolve(0.15):
    play sound2 hitSound
    hide white with Dissolve(0.25)
    

    show mc ready at bl, Shake(None, .5, dist=20):
        parallel:
            easeout .3 alpha 1.0
        parallel:
            easeout .3 xoffset -75
                
    "I try to block the attack but I'm a moment too late and his sword lands on my side."
    if TATBATTLECOUNTER == 1:
        "I dig my heels into the ground as Eagle is pushed back from the attack. My dashboard flashes in warning as my energy quickly depletes."
        "Another hit like that and I risk getting depowered!"
        jump TATCON2
        
    if TATBATTLECOUNTER == 2:
        "My energy levels plummet."
        return

label E2D5S4_TATW2:
    $ renpy.hide_screen ("timer_scr")
    
    show boss att at br, Shake(None, 1, dist=20):
        xoffset 0
        parallel:
            easeout .1 alpha 1.0
        parallel:
            easeout .1 xoffset -250
    $renpy.pause(.1)

    play sound meleeSound
    show boss att at br with Dissolve(.2):
        xoffset -400
        
    play sound2 dodSound
    show mc dod at bl with Dissolve(.45):
        parallel:
            easeout .5 alpha 1.0
        parallel:
            easeout .5 xoffset -150
            
    $renpy.pause(.25)
    play sound "audio/sfx/GEAR Combat/SMG.ogg"
    $renpy.pause(.05)
    play sound2 hitSound
    show boss blo at br, Shake(None, .5, dist=20):
        parallel:
            easeout .3 alpha 1.0
        parallel:
            easeout .3 xoffset -125
    
    "I sidestep out of the way, but Tatsuo recovers and swings again. Before he can attack, his shield shimmers as it takes damage from an energy round!"
    "Shou boosts back out of range again. I take advantage of the moment and swing my sword!"
    jump TATCON2


label TATCON2:


$ qtetotal = 5
$ t_var = qtetotal
show screen timer_scr(place="E2D5S4_TATL3")

menu:
    "Miss…":
        $ TATBATTLECOUNTER += 1
        jump E2D5S4_TATL3

    "Strike!":
        jump E2D5S4_TATW3

    "Hit!":
        jump E2D5S4_TATW3

    "Fail…":
        $ TATBATTLECOUNTER += 1
        jump E2D5S4_TATL3

    "Slash!":
        jump E2D5S4_TATW3

label E2D5S4_TATL3:
    $ renpy.hide_screen ("timer_scr")
    
    
    show boss att at br, Shake(None, 1, dist=20):
        xoffset 0
        parallel:
            easeout .1 alpha 1.0
        parallel:
            easeout .1 xoffset -400
    $renpy.pause(.1)

    play sound meleeSound
    show boss att at br with Dissolve(.2):
        xoffset -550

    show white with Dissolve(0.15):
    play sound2 hitSound
    hide white with Dissolve(0.25)
    

    show mc ready at bl, Shake(None, .5, dist=20):
        parallel:
            easeout .3 alpha 1.0
        parallel:
            easeout .3 xoffset -75
            
    
    "Our swords clash in a metallic ring as Tatsuo blocks my attack!"
    "Throwing his force against his weapon, he pushes me back and slices my side. My shields shimmer as it takes the damage."
    
    if TATBATTLECOUNTER == 1:
        "Ignoring the warnings from Eagle, I focus on Tatsuo and rebound by slashing his chest. His shield absorbs the damage. Before he can recover, a flurry of energy rounds fly straight at him and pelt his shield with rounds!"
        
        
        "I grin. Of course my teammates have my back!"
        
        show mc ready at bl, Shake(None, 1, dist=20):
            xoffset 0
            xzoom -1
            parallel:
                easeout .1 alpha 1.0
            parallel:
                easeout .1 xoffset 400
        $renpy.pause(.1)

        play sound meleeSound
        show mc attM at bl with Dissolve(.2):
            xoffset 550

        show white with Dissolve(0.15):
        play sound2 hitSound
        hide white with Dissolve(0.25)

        show boss neu at br, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset 150
        
        
        "While Tatsuo tries to evade the shots, I swing my sword high and slice right through his shield."
        "His GEAR goes dark as he is depowered!"
        $ E2D5S4_Victory = 1
        return

    if TATBATTLECOUNTER == 2:
        "My dashboard flashes wildly with warnings."
        return

label E2D5S4_TATW3:
    $ renpy.hide_screen ("timer_scr")
    
    
    show mc ready at bl, Shake(None, 1, dist=20):
        xoffset 0
        xzoom -1
        parallel:
            easeout .1 alpha 1.0
        parallel:
            easeout .1 xoffset 400
    $renpy.pause(.1)

    play sound meleeSound
    show mc attM at bl with Dissolve(.2):
        xoffset 550

    show white with Dissolve(0.15):
    play sound2 hitSound
    hide white with Dissolve(0.25)

    show boss neu at br, Shake(None, .5, dist=20):
        parallel:
            easeout .3 alpha 1.0
        parallel:
            easeout .3 xoffset 150
    "Without giving Tatsuo a chance to recover, I slash across his chest. He moves to block, but is a second too late. Then I swing my sword around and slash at his side."
    "Mustering up my energy, I raise my sword again and come down in a powerful blow!"
    "Tatsuo's GEAR flies back from the force before going dark."
    $ E2D5S4_Victory = 1
    return