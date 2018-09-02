label E1D4S3:
     
    pf "Wait, before we go, how exactly do these matches work?"
    show kaori neu at r3
    voice "audio/voice/E1/D4/S3/Kaori/1.ogg"
    ki "It's based on how many points you accumulate. We'll be competing against pre-programmed AI GEARs--"
    show shou mis at cc
    voice "audio/voice/E1/D4/S3/Shou/1.ogg"
    ss "Who are like boss-level difficult to beat."
    voice "audio/voice/E1/D4/S3/Kaori/3.ogg"
    ki "--and our score is calculated by how many we beat, along with how well we fought overall. So things like accuracy, how many hits we take, tactics, teamwork--those are all added up."
    pf "So how many points are all of those things worth?"
    show shou hap at cc
    voice "audio/voice/E1/D4/S3/Shou/3.ogg"
    ss "They don't share with us the exact breakdown, but everyone knows that defeating the AI gives you a buttload of points!"
    show kaori ann at r3
    show exclamation:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S3/Kaori/5.ogg"
    ki "Now hurry up and get in your GEAR! We really need to practice before it's our turn."
    hide kaori with dissolve
    "She turns on her heel, and the rest of us disperse."
    
    stop music fadeout 3
    scene black with fade
    $renpy.pause(1)
    play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
    $renpy.pause(2.5)
    scene cg GEAR cockpit first1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    play sound "audio/sfx/Impacts/Luggage Drop.ogg"
    $renpy.pause(2.5)
    stop ambient fadeout 3
    play sound "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
    $renpy.pause(2.5)
    play sound "audio/sfx/GEAR/GEAR Boot Up 1.ogg"
    $renpy.pause(2.5)
    scene cg GEAR cockpit first2 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    play ambient "audio/ambience/GEAR Cockpit.ogg" fadein 1 fadeout 1
    $renpy.pause(2.5)
    play sound "audio/sfx/GEAR/GEAR Boot Up 2.ogg"
    $renpy.pause(2.5)
    scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    "After reaching my GEAR, I boot up the simulation."
    play sound "audio/sfx/GEAR/GEAR Virtual Training Simulator.ogg"
    #NOT COMPLETE YET, will need to figure out of this text is happening in the simulator or during the battle screen
    # "I vote in the cockpit" - Austin
    
    "The usual stats float across my screen, but something about them seems off."
    "Kaori's voice comes through the com."
    voice "audio/voice/E1/D4/S3/Kaori/2.ogg"
    ki "Where are your weapons?"
    pf "I don't know. Let me see if it's something in the settings."
    voice "audio/voice/E1/D4/S3/Kaori/4.ogg"
    ki "Why didn't you do a comprehensive check on your GEAR?"
    pf "I did. It doesn't scan weaponry since it's not part of the mech's core function."
    voice "audio/voice/E1/D4/S3/Kaori/6.ogg"
    ki "Your \"combat\" GEAR doesn't have weaponry set as a core function during checks?"
    "I've never run into this issue before, although she does make a good point. {w}I try every setting combination I can think of, but my weapons still aren't registering." 
    voice "audio/voice/E1/D4/S3/Shou/4.ogg"
    ss "Try waiting a minute. Sometimes there's a lag while your GEAR warms up."
    pf "There shouldn't be lag."
    "We wait anyway. {w}After a few minutes, it's clear my weapons aren't going to show up."
    pf "I don't know what's going on."
    voice "audio/voice/E1/D4/S3/Kaori/10.ogg"
    ki "Do you even have weapons?"
    pf "Of course I do!"
    voice "audio/voice/E1/D4/S3/Kaori/11.ogg"
    ki "Then where are they?"
    "Suddenly, Mayu's soft voice cuts through."
    voice "audio/voice/E1/D4/S3/Mayu/1.ogg"
    ma "Maybe they're still being processed at customs. I've heard that GEAR and their accessories are processed separately." 
    voice "audio/voice/E1/D4/S3/Shou/5.ogg"
    ss "That makes sense."
    pf "How long will that take to process?"
    voice "audio/voice/E1/D4/S3/Mayu/2.ogg"
    ma "I-I don't know."
    voice "audio/voice/E1/D4/S3/Kaori/12.ogg"
    ki "Too long! We need those weapons now."
    voice "audio/voice/E1/D4/S3/Shou/6.ogg"
    ss "Don't worry, it'll be okay." 
    voice "audio/voice/E1/D4/S3/Kaori/13.ogg"
    ki "No, it won't! How will he fight without weapons?" 
    pf "I'll figure something out. Let's just start the match. We're running out of time."
    voice "audio/voice/E1/D4/S3/Kaori/14.ogg"
    ki "Fine." 
    
    #Transition to "game world"
    stop ambient fadeout 3
    
    #show all mechs for the first time
    voice "audio/voice/E1/D4/S4/Kaori/1.ogg"
    ki "Everyone ready?"
    
    "Everyone's comm relay blinks green in affirmation."
    voice "audio/voice/E1/D4/S4/Kaori/2.ogg"
    ki "Alright, let's start!"
    
    
    
    scene black with fade
    
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 1
    show bg battleground day with dissolve:
        alpha 1
        xzoom 1
        yzoom 1
        yoffset 25
        xoffset 0
        
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

    show bg battleground day:
        parallel:
            easein 3.0 alpha 1.0
        parallel:
            easein 3.0 xoffset -200
            
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
            
    # ai mechs
    $renpy.pause(2.5)
    show aiR neu at tr with dissolve:
        xzoom .8
        yzoom .8
            
    show aiR2 neu at tl with dissolve:
        xzoom .8
        yzoom .8
            
    show aiM neu at mm with dissolve
            
    show aiM2 neu at br with dissolve
    
    $renpy.pause(1)
    
    scene bg battleground day with fade
    show mc mech at bl with dissolve:
        xzoom -1
    show aiM att at br with dissolve
    show mc ready at bl with dissolve:
        xzoom -1
        
        
        
        
        
        
        
    "We all get into position and square off to take on the AIs. My closest enemy charges me with its sword raised!"
    
    
    #$renpy.pause(1)
    ##Start simulated combat. You match up against an AI mech. You don't have any "attack" choices, just dodging and blocking.
    #$ enemy = "aiM"
    #$ D4Jetpack = 0
    #$ survived = 0
    #$ teamPractice = 0
    #$ mode = "retreat"
    #$ context = "E1D4S3_TeamPracticeComplete"
    
    #$ mcEnergyMax = 200
    #$ mcEnergy = 200
    #$ enemyHPMax = 100
    #$ enemyHP = 100
    
    #$ qtebase = 10
    #$ qtereaction = qteath + qtetrack + qtebase
    #$ qtetotal = qtereaction
    #$ t_var = qtereaction
    
    
    
    #show screen battle_screen
    #$renpy.pause(1)
    ##show screen timer_scrReaction(place="E1D4S3_TeamPracticeComplete")
    #jump qte_game
    # and jump here after finished
    
 
 
 
 
     
    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E1D4S3_L1")
    menu:
        "Juke!":
            jump E1D4S3_W1

        "Slow…":
            jump E1D4S3_L1

        "Dodge!":
            jump E1D4S3_W1

    label E1D4S3_W1:
        $ renpy.hide_screen ("timer_scr")
        
        show aiM att at br:
            xoffset 0
            parallel:
                easeout .1 alpha 1.0
            parallel:
                easeout .1 xoffset -250
        $renpy.pause(.1)

        play sound meleeSound
        show aiM att at br with Dissolve(.2):
            xoffset -400        
        
        play sound2 dodSound
        show mc dod at bl with Dissolve(.45):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -150
        
        "I barely manage to sidestep out of the way!"
        "This does not bode well…"
        jump E1D4S3_COMBATCONVER1

    label E1D4S3_L1:
        $ renpy.hide_screen ("timer_scr")
        
        show aiM att at br:
            xoffset 0
            parallel:
                easeout .1 alpha 1.0
            parallel:
                easeout .1 xoffset -250
        $renpy.pause(.1)

        play sound meleeSound
        show aiM att at br with Dissolve(.2):
            xoffset -400

        show white with Dissolve(0.15):
        play sound2 hitSound
        hide white with Dissolve(0.25)
        
        show mc blo at bl, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -150
                
                
        "I'm unprepared for the attacked and fumble to bring up my shields. The AI swings its sword and strikes me on the shoulder."
        "Eagle's dashboard goes wild by beeping and flashing warnings as my energy level plummets."
        "I can't let my guard down again. Another hit like that and I am done for!"
        jump E1D4S3_COMBATCONVER1


    label E1D4S3_COMBATCONVER1:
    "I retaliate with an uppercut and a punch to the solar plexus, which does some damage but nowhere near the crushing blow I received. The AI shakes off my attack and immediately swings again."


    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E1D4S3_L2")
    menu:
        "Freeze…":
            jump E1D4S3_L2

        "Defend!":
            jump E1D4S3_W2

        "Block!":
            jump E1D4S3_W2

    label E1D4S3_W2:
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
        show mc ready at bl with Dissolve(.2):
            xoffset 250

        play sound2 hitSound
        
        show aiM neu at br, Shake(None, .5, dist=10):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -100
                
        "I raise one arm in defense as its sword sends another wave of shimmers over my shield. Using my free hand I jab the AI in the side."
        "Just as before, Eagle takes an alarming amount of damage while my attack on the AI barely fazes it."
        $ E1D4S3_FakeFightWin = 1
        jump E1D4S3_TeamPracticeComplete

    label E1D4S3_L2:
        $ renpy.hide_screen ("timer_scr")
        "As the AI's sword connects, Eagle protests with a series of beeps and flashes warning me of dangerously low energy levels."
        "I barely have a moment to register the warnings before the AI swings at me again!"
        jump E1D4S3_TeamPracticeComplete
         
     
 
 
 
 
    
    
    label E1D4S3_TeamPracticeComplete:
        #play sound "audio/sfx/GEAR/GEAR Virtual Training Simulator.ogg"
        #$renpy.pause(2.5)
        $ renpy.hide_screen ("battle_screen")
        $ teamPractice = survived
        if E1D4S3_FakeFightWin == 0:
            #IF you do poorly
            show aiM att behind mc:
                easeout .35 xoffset -850
            $renpy.pause(.15)
            play sound "audio/sfx/GEAR Combat/Sword Double.ogg"
            $renpy.pause(.15)
            play sound "audio/sfx/GEAR Combat/Hit.ogg"
            show mc mech at bl, Shake(None, .5, dist=25) with dissolve
            $renpy.pause(.5)
            play sound "audio/sfx/GEAR Combat/Depower.ogg"
            hide mc with dissolve
            $renpy.pause(1.0)
            "Well, that was a bust. I was destroyed. In my defense, that was a pretty hopeless matchup since I was unarmed."
    
        if E1D4S3_FakeFightWin == 1:
            #IF you do well
            "I dodge and block most attacks. However, I can't return attacks and can only defend."
            show aiM att behind mc:
                easeout .35 xoffset -600
            $renpy.pause(.15)
            play sound "audio/sfx/GEAR Combat/Sword Double.ogg"
            $renpy.pause(.15)
            play sound "audio/sfx/GEAR Combat/Hit.ogg"
            show mc mech at bl, Shake(None, .5, dist=25) with dissolve:
                linear .4 xoffset -75
            $renpy.pause(.5)
            play sound "audio/sfx/GEAR Combat/Depower.ogg"
            hide mc with dissolve
            $renpy.pause(1.0)
            "With my energy core gradually depleted, it doesn't take much for the AI GEAR to wipe me out."
            
        
        #fade to finished simulation
        scene black with fade
        #scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        "Without a fourth teammate, my team barely manages to win."
    
    stop music fadeout 3
    scene black with fade
    
    play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg" fadein 1
    "We all shut off the simulator and climb out of our GEAR."
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 3
    play ambient "audio/ambience/Hangar.ogg" fadein 1
    $renpy.pause(1)
    
    scene bg campus hangar day with fade
    $renpy.pause(1)
    
    show mayu neu at l3
    show kaori dis at cc
    show shou neu at r3:
        xzoom -1
        xoffset 75
    with dissolve
    $renpy.pause(.5)
    "I start to head back towards the team, but they all get to me first."
    show kaori ang with dissolve
    show vein:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S3/Kaori/15.ogg"
    ki "We can't play a match like that! We hardly scored any points." 
    show kaori ann with dissolve
    voice "audio/voice/E1/D4/S3/Shou/7.ogg"
    ss "Don't worry, Kaori. I'm sure he'll have his equipment soon." 
    voice "audio/voice/E1/D4/S3/Kaori/16.ogg"
    ki "Not soon enough! The match is today."
    show kaori dis
    voice "audio/voice/E1/D4/S3/Kaori/16_1.ogg"
    ki "Maybe he shouldn't compete. We can tell them we have four team members, but one of our GEARs is in no condition to fight."
    show mayu dis with dissolve
    "Mayu looks at her determinedly."
    voice "audio/voice/E1/D4/S3/Mayu/3.ogg"
    ma "No, he has to. It's the only way." 
    show mayu neu with dissolve
    "Shou looks apologetically at me."
    show shou thi with dissolve
    show drop:
        xoffset 1250
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S3/Shou/8.ogg"
    ss "Look, maybe you should just hang back. Without weapons the AIs will ruin you." 
    pf "I can still help us gain points." 
    show kaori neu
    voice "audio/voice/E1/D4/S3/Kaori/17.ogg"
    ki "No, Shou is right. You have to hang back. That will maximize our qualifier points, which is what's important right now." 
    show shou cur with dissolve
    "Shou stares in shock."
    show shocked:
        xoffset 1250
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S3/Shou/9.ogg"
    ss "Did you just agree with me?" 
    show kaori ann
    show exclamation:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S3/Kaori/18.ogg"
    ki "Not now, Shou!" 
    show shou smi
    voice "audio/voice/E1/D4/S3/Shou/10.ogg"
    ss "You never agree with me!" 
    voice "audio/voice/E1/D4/S3/Kaori/19.ogg"
    ki "Idiot! Why do you keep saying that?" 
    
    "Just then, a group of engineers come toward us."
    hide shou
    hide mayu
    hide kaori
    with dissolve
    
    show studentM extra at l3:
        xoffset -100
    show kaori dis at cc:
        xoffset 75
        xzoom -1
    show shou neu at r3:
        xzoom -1
        xoffset 125
    with dissolve
    voice "audio/voice/E1/D4/S3/Engineer/1.ogg"
    eng1 "What are your GEARs still doing here?"
    show shou cur
    show question:
        xoffset 1250
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S3/Shou/11.ogg"
    ss "Say what?"
    voice "audio/voice/E1/D4/S3/Engineer/2.ogg"
    eng1 "They've got to be prepped for the next match."
    show kaori neu
    voice "audio/voice/E1/D4/S3/Kaori/20.ogg"
    ki "That means we're next. Let's go."
    pf "What about our GEARs?"
    voice "audio/voice/E1/D4/S3/Kaori/21.ogg"
    ki "The engineers will handle it."
    
    stop music fadeout 3.0
    stop ambient fadeout 3.0
    scene black with fade
    
    "They engineers disperse towards our GEARs. My team splits up to head to the locker rooms"
    "We quickly change into our combat uniforms. Luckily, I'd kept my old one from the States."
    "I follow Shou into the precombat room, which was a small room connecting the locker room and arena."
    
    
    
    $renpy.pause(1.0)
    
    $ shoOut = "Pilot"
    $ mayOut = "Pilot"
    $ kaoOut = "Pilot"
    play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 1
    scene bg campus battleroom day
    show shou smi at l3:
        xoffset -150
    with fade
    
    
    
    "The space feels cramped. Couches line the walls and a round table is in the center."
    
    
    show kaori neu at cc:
        xoffset 200
    show mayu neu at r3:
        xoffset 200
        xzoom -1
    with dissolve
    
    "I barely have time to take in the room when Kaori and Mayu walk in dressed in equally skin-tight suits, which hug their every curve."
    
    
    menu:
        "So sleek!":
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
            pf "Your suits are so cool!"
            show kaori ske 
            show mayu cur
            with dissolve
            show dots:
                xoffset 920
                yoffset 110
                xzoom .75
                yzoom .75
            show question:
                xoffset 1375
                yoffset 135
                xzoom .75
                yzoom .75
            "Kaori gives me a strange look. Mayu looks a little surprised."
            show mayu smi with dissolve
            voice "audio/voice/E1/D4/S3/Mayu/5.ogg"
            ma "Um, thank you?"
            pf "No problem. You two look great!"
            show kaori dis with dissolve
            "Kaori narrows her eyes."
            voice "audio/voice/E1/D4/S3/Kaori/23.ogg"
            ki "Okay…"
            "While most pilot suits don't differ much from each other, the Japanese models always have a more \"aerodynamic\" feel to them. This is the first time I've had a chance to see the suits up close and--"
            show kaori ang
            show shou cur
            with dissolve
            $renpy.pause(.5)
            show vein:
                xoffset 920
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Kaori/24.ogg"
            ki "Stop staring!!"
            show kaori dis
            pf "Wha…?"
            show mayu sur b1 with dissolve
            "Mayu's eyes widen, and she crosses her arms over her chest."
            show mayu ner b1
            show shoBlush:
                xoffset 1375
                yoffset 135
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Mayu/6.ogg"
            ma "I didn't think you were like that."
            pf "No, I just meant those suits look good on you."
            show kaori ann
            voice "audio/voice/E1/D4/S3/Kaori/25.ogg"
            ki "We got what you meant! And we don't appreciate your staring!"
            show storm:
                xoffset 920
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Kaori/25_01.ogg"
            ki "Come on, Mayu. Let's go before he says something else he regrets."
            hide kaori
            hide mayu
            with dissolve
            "She pulls Mayu close to her and the two of them head to the table."
            hide shou with dissolve
            show shou mis at cc with dissolve
            $renpy.pause(.5)
            stop music fadeout 5
            show shou mis
            voice "audio/voice/E1/D4/S3/Shou/12.ogg"
            ss "Rookie move, broseph."
            pf "No, seriously, I wasn't looking at them like that."
            pf "Wait, that didn't really come out right."
            "Shou just shakes his head."
            show shou cur
            voice "audio/voice/E1/D4/S3/Shou/13.ogg"
            ss "Everyone's got to wear these suits. You're making it weird."
            hide shou with dissolve
            "He follows them to the table."
    
        "Me likey.":
            $ E1D4S3_Stare = 1
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
            "Their uniforms leave nothing to the imagination. I eagerly watch the girls as they approach. Have I just died and gone to heaven?"
            show mayu cur
            show question:
                xoffset 1375
                yoffset 135
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Mayu/7.ogg"
            ma "Hello?"
            "..."
            show shou cur
            show mayu cur
            show kaori ang
            with dissolve
            $renpy.pause(.5)
            show exclamation:
                xoffset 920
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Kaori/26.ogg"
            ki "HEY!"
            show kaori ann
            "Kaori's angry eyes snap me out of my reverie. Her hands are on her hips."
            show vein:
                xoffset 920
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Kaori/27.ogg"
            ki "What do you think you're doing?"
            pf "I was just admiring your incredibly effective and intelligent distraction tactic."
            "Shou and the girls stare blankly at me."
            show kaori ske
            voice "audio/voice/E1/D4/S3/Kaori/28.ogg"
            ki "What?"
            pf "With you wearing these uniforms, the other team will be so distracted that they'll forget about the battle and give us the advantage."
            show mayu sur b1
            show kaori ann
            show shou smi
            with dissolve
            show shoBlush:
                xoffset 1375
                yoffset 135
                xzoom .75
                yzoom .75
            "Mayu brings up her arms to hide her chest, mortified. Kaori glares at me, and crosses her arms."
            show mayu ner b1 with dissolve
            voice "audio/voice/E1/D4/S3/Kaori/29.ogg"
            ki "How would the opposing team see us when we're {i}inside{/i} a giant robot?"
            pf "Uh…"
            show kaori dis
            voice "audio/voice/E1/D4/S3/Kaori/30.ogg"
            ki "Exactly. These suits are for functional purposes, nothing more. Don't be a pervert!"
            hide kaori
            hide mayu
            with dissolve
            "After scolding me, Kaori and Mayu circle the table."
            hide shou with dissolve
            show shou mis at cc with dissolve
            $renpy.pause(.5)
            stop music fadeout 5
            show shou mis
            "Shou shakes his head."
            voice "audio/voice/E1/D4/S3/Shou/14.ogg"
            ss "That was an amateur mistake, broseph."
            show shou hap
            show drooling:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Shou/15.ogg"
            ss "You've got to \"sneak a peek\" my man. Can't be so obvious about it."
            hide shou with dissolve
            "He claps me on the back after imparting his words of wisdom, then joins the girls at the table." 
    
        "No comment.":
            "We're all wearing pretty similar suits. I'm not a fan of how the material clings, but at least it provides ample movement and shock absorption, which I suppose is the point of them."
            hide kaori
            hide shou
            hide mayu
            with dissolve
            "The girls head directly to the table, and Shou joins them there."
    
        "Shou's care package drop zone appears to be flatlined.":
            hide kaori
            hide mayu
            with dissolve
            "The girls ignore us and head straight for the table."
            show shou neu at cc with dissolve
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
            "They aren't the only ones with a tight uniform. Shou's is pretty tight too. In fact..."
            pf "Uh, Shou."
            show question:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Shou/16.ogg"
            ss "What's up, broseph?"
            pf "Nothing, I was just wondering if you're feeling okay."
            show shou hap
            show note:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Shou/17.ogg"
            ss "Never better! Why?"
            pf "You sure you don't feel like something's missing?"
            show shou cur
            "His smile is replaced with confusion."
            voice "audio/voice/E1/D4/S3/Shou/18.ogg"
            ss "No… Should I be?"
            pf "Well, your fly is undone right now."
            show shou sur with dissolve
            show exclamation:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            "Startled, Shou glances down."
            stop music fadeout 5
            show shou cur
            voice "audio/voice/E1/D4/S3/Shou/19.ogg"
            ss "There's no zipper down there."
            pf "It looks like there's pretty much {i}nothing{/i} down there."
            "Shou turns his back to me."
            show shou sur b1 with dissolve
            show drop:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Shou/20.ogg"
            ss "Eyes up top, man! You don't violate another broseph like that..."
            hide shou with dissolve
            "Before I can react, Shou has already left and joined the girls at the table."
    
    
    "As I approach the table, Kaori hits a button on the side, which brings up a hologram of the arena battlefield."
    play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 1
    "Four impressive GEAR pop up on the right side of the field, and four smaller GEAR populate the other side."
    show kaori neu at r3:
        xzoom -1
        xoffset 200
    show shou neu at l3:
        xoffset -250
    show mayu neu at cc:
        xoffset -300
    with dissolve
    $renpy.pause(.5)
    "Kaori points to the right."
    voice "audio/voice/E1/D4/S3/Kaori/31.ogg"
    ki "These are the enemy AI GEAR we'll be battling."
    "She points to the other side."
    voice "audio/voice/E1/D4/S3/Kaori/32.ogg"
    ki "This is us."
    voice "audio/voice/E1/D4/S3/Kaori/33.ogg"
    ki "The AIs are programmed to be a challenge, so it's important that we stick to the plan and work together to take them out."
    show mayu dis
    "Mayu speaks up, her expression solemn." 
    voice "audio/voice/E1/D4/S3/Mayu/8.ogg"
    ma "The GEARs we are facing against are specifically engineered for ACE Academy qualifier matches. They change yearly to make sure they can't be beat using a systematic approach."
    
    "With a quick flick of her fingers, Mayu zooms into the AI GEAR holograph. Statistics on the AI's battle armaments and parts pop up beside the GEARs."
    voice "audio/voice/E1/D4/S3/Mayu/9.ogg"
    ma "It looks like we have two Class A close combat and two Class A long range support GEARs."
    "Kaori nods. Reaching her hand into the holographic field, she shuffles our GEARs into position on the map."
    show kaori thi
    voice "audio/voice/E1/D4/S3/Kaori/34.ogg"
    ki "Knowing all of that, Shou and I will blitz the melee GEARs to give Mayu some breathing room. She will focus on suppressive fire on their backline. That should give us enough time to finish off the two GEAR and engage for the remaining ones."
    "Mayu and Shou both nod in agreement. Kaori pulls the last GEAR towards the back edge of the map, then looks pointedly at me."
    show kaori neu
    show mayu neu
    voice "audio/voice/E1/D4/S3/Kaori/35.ogg"
    ki "This is where you will be. Don't get yourself killed."
    "I look at her flatly, but I don't dispute her."
    "The map flashes red and the door to the arena slides open."
    show shou smi
    "Shou's face lights up in excitement and he practically leaps towards the door."
    voice "audio/voice/E1/D4/S3/Shou/21.ogg"
    ss "That's our cue to get out there."
    voice "audio/voice/E1/D4/S3/Kaori/36.ogg"
    ki "Does everyone understand the plan?"
    "We all nod."
    voice "audio/voice/E1/D4/S3/Kaori/37.ogg"
    ki "Okay, then let's go."
    
    stop music fadeout 3.0
    stop ambient fadeout 3.0
    scene black with fade
    
    "Taking a deep breath, I follow Shou and the rest of my team to our readied GEARs."
    
    
    jump E1D4S4