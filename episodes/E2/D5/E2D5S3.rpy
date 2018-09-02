#
label E2D5S3:
    
    $ valOut = "sUniform"

    stop ambient fadeout 5
    scene black with fade
    
    "After jumping out of my cockpit, I reunite with my team and dial Valerie's number."
    play ambient "audio/ambience/Hangar.ogg" fadein 3
    scene bg campus hangar day with fade
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(2.5)
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    $renpy.pause(1.0)
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO1.ogg"
    vb "Hello?"
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    pf "Hey."
    "I can practically hear the smile in her voice."
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO2.ogg"
    vb "I knew you'd call."
    pf "How?"
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO3.ogg"
    vb "Just a hunch."
    pf "Was it something you saw in my GEAR last night?"
    "She laughs."
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO4.ogg"
    vb "Call it an engineer's intuition."
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO5.ogg"
    vb "So, I'm guessing something's not working right and you're in need of an engineer."
    pf "Um, yeah actually."
    
    if E2D4S3_EngineerGet == 1:
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO6.ogg"
        vb "Maybe you should ask your engineer to take a look."
        pf "Oh, she's busy."
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO7.ogg"
        vb "Busy not existing?"
        pf "Uh..."
        "She laughs at my hesitation."
    
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO8.ogg"
    vb "Luckily, I can help."
    pf "Thanks, Valerie. Come meet us by Eagle."
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO9.ogg"
    vb "Okay, I'll be there in a few minutes."
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    "She hangs up."
    stop music fadeout 2.0
    
    scene black with fade
    $renpy.pause(1)
    scene bg campus hangar day with fade
    show kaori neu at r1 with dissolve
    show shou neu at l1 with dissolve:
        xoffset -100
    show mayu neu at l3 with dissolve:
        xoffset -275
        
    "We don't have to wait long before Valerie arrives. I wave her over and she stands right beside me."
    show valerie smi at r3 with dissolve:
        xoffset 200
        xzoom -1
    show shou neu at l1
    pf "Thanks for coming."
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    show valerie hap at r3
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO10.ogg"
    vb "Of course, I wouldn't leave you hanging when you need me."
    show shou thi at l1
    "She smiles broadly. {w}Shou coughs."
    show valerie smi at r3
    pf "Right, so this is the team."
    show shou neu at l1
    "I point to each of of them in turn."
    pf "This is Mayu, Shou, and Kaori."
    show mayu smi at l3
    show shou smi at l1
    "Both Mayu and Shou wave while Kaori nods."
    pf "Everyone, this is--"
    show valerie hap at r3
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO11.ogg"
    vb "I'm Valerie. I watched your match during the qualifiers and was impressed by all of you. It's great to finally meet you."
    show note:
        xoffset 415
        yoffset 20
        xzoom .75
        yzoom .75
    show shou mis at l1
    voice "audio/voice/E2/D5/SS/17.ogg"
    ss "Believe me, it is great to meet you too."
    show mayu cur at l3
    show valerie mis at r3
    "Mayu glances at Shou, while Valerie smirks."
    show kaori ske at r1
    show mayu ner at l3
    show shou smi at l1
    voice "audio/voice/E2/D5/KI/31.ogg"
    ki "So, you're an engineer?"
    show valerie smi at r3
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO12.ogg"
    vb "That's right."
    show kaori neu at r1
    "Kaori points to Eagle."
    show mayu neu at l3
    voice "audio/voice/E2/D5/KI/32.ogg"
    ki "Are you able to calibrate his weaponry?"
    pf "Yeah, my equipment just passed through customs and the calibrations are off."
    show valerie hap at r3
    show shiny:
        xoffset 1375
        yoffset 125
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO13.ogg"
    vb "Leave it to me."
    hide valerie with dissolve
    hide kaori with dissolve
    "She saunters over to Eagle's terminal and turns it on. Kaori follows closely behind her and watches her work. {w}Occasionally she'll ask a question which Valerie will happily answer."
    "Shou, Mayu, and I hang back to give her space to work."
    show shou mis at l1
    voice "audio/voice/E2/D5/SS/18.ogg"
    ss "I don't know where you found such a hot engineer, but thank you for bringing her here."
    
    menu:
        "I met her in class.":
            pf "She found me, actually. We have our Foreign Exchange class together."
            show crying:
                xoffset 415
                yoffset 20
                xzoom .75
                yzoom .75
            show shou sad at l1
            voice "audio/voice/E2/D5/SS/19.ogg"
            ss "Aww man, that's not an open course. You're lucky."
    
        "She's into me.":
            pf "She gave me her number on the first day of class."
            show shocked:
                xoffset 415
                yoffset 20
                xzoom .75
                yzoom .75
            show shou ner at l1
            voice "audio/voice/E2/D5/SS/20.ogg"
            ss "Seriously, man? I wish a girl would come out of nowhere and give me her number… Especially if she looks like {i}that{/i}!"
    
        "I've seen hotter.":
            pf "Eh… I guess she's alright."
            show question:
                xoffset 415
                yoffset 20
                xzoom .75
                yzoom .75
            show shou ske at l1
            voice "audio/voice/E2/D5/SS/21.ogg"
            ss "Are you blind?"
            
    show mayu sad at l3
    "Mayu pouts and then sighs."
    show shou neu at l1
    pf "You alright, Mayu?"
    show mayu thi at l3
    voice "audio/voice/E2/D5/MA/0-10.ogg"
    ma "Yeah, I'm fine."
    hide mayu with dissolve
    show shou ske at l1
    "But she joins the girls right after answering. {w}Shou and I exchange a glance."
    pf "What's up with her?"
    show shou neu at l1
    voice "audio/voice/E2/D5/SS/22.ogg"
    ss "I don't know."
    pf "Was it something we said?"
    show shou thi at l1
    voice "audio/voice/E2/D5/SS/23.ogg"
    ss "Hmm… Must be that time of the month again."
    
    if E2D5S1_Nikki == 1:
        pf "Women's cycles really do sync up. My sister is on hers too."
        show shou ner at l1
        voice "audio/voice/E2/D5/SS/24.ogg"
        ss "I'm so sorry, broseph."
    
    else:
        show shou cur at l1
        "Instinctively, we both back further away from the girls."
        show shou ner at l1
        voice "audio/voice/E2/D5/SS/25.ogg"
        ss "I think we dodged a bullet there."
        pf "Probably."
    
    #fade to black
    scene black with fade
    $renpy.pause(1)
    
    "Valerie not only calibrated my weapons, she also tweaked the rest of the team's GEARs to improve everyone's performance."
    
    #bg
    scene bg campus hangar day with fade
    show kaori neu at r1 with dissolve
    show shou neu at l1 with dissolve:
        xoffset -100
    show mayu neu at l3 with dissolve:
        xoffset -275
    show valerie smi at r3 with dissolve:
        xoffset 200
        xzoom -1
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO14.ogg"
    vb "Well, that about does it."
    show kaori cur at r1
    voice "audio/voice/E2/D5/KI/33.ogg"
    ki "I didn't know that changing one small setting will increase my power by 10 percent."
    show valerie hap at r3
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO15.ogg"
    vb "Yup! Trust me, you'll notice the difference in your match today."
    show kaori mis at r1
    "Kaori seems impressed."
    show valerie smi at r3
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO16.ogg"
    vb "Your GEARs are all ready to go, so I'm going to head out. I've still got some things to get done if I want to catch your match."
    show kaori smi at r1
    show mayu smi at l3
    show shou smi at l1
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO17.ogg"
    vb "Let me know how all of your equipment feel when you test them out again. If I need to do some more tweaking I will." 
    pf "Sure, thanks again for doing all this."
    show valerie hap at r3
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO18.ogg"
    vb "It was my pleasure!"
    show note:
        xoffset 1375
        yoffset 125
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO19.ogg"
    vb "Good luck at the match! I will be cheering for you!"
    hide valerie with dissolve
    "She waves goodbye then leaves."
    show shou hap at l1
    voice "audio/voice/E2/D5/SS/26.ogg"
    ss "I can't wait to test out those changes she made! She said she increased my speed. Those guys will eat my dust out there!"
    show mayu hap at l3
    voice "audio/voice/E2/D5/MA/0-11.ogg"
    ma "I watched her improve the coolant in my weaponry. She does seem very knowledgable about GEARs."
    show kaori mis at r1
    stop music fadeout 2.5
    stop ambient fadeout 2.5
    voice "audio/voice/E2/D5/KI/34.ogg"
    ki "Okay, now that everyone's GEARs have been improved and weapons recalibrated, let's try out those changes in the simulator."
    hide kaori
    hide mayu
    hide shou
    with dissolve
    
    #Black screen mech noises
    
    scene black with fade
    $renpy.pause(1.0)
    
   
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 10
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
    
    "Within minutes, we are back in the virtual arena."
    
    voice "audio/voice/E2/D5/KI/35.ogg"
    ki "Alright, we don't have too much time so we'll do a team match."
    
    if E2D5S2_Spirit == 2:
        pf "Darn, I was looking forward to scrapping that level 50 AI."
    
    else:
        pf "Sounds good."
    
    voice "audio/voice/E2/D5/SS/27.ogg"
    ss "What's the plan this time?"
    voice "audio/voice/E2/D5/KI/36.ogg"
    ki "No plan. Being able to improvise during a match is important. Keep communications open so we can change tactics accordingly."
    voice "audio/voice/E2/D5/SS/28.ogg"
    ss "Okay."
    voice "audio/voice/E2/D5/KI/37.ogg"
    ki "I'll load in a premade AI team now."
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
    "The simulation boots up a team of enemy GEARs."
    
    voice "audio/voice/E2/D5/KI/38.ogg"
    ki "Let's go!"
    scene black with fade
    "We spread out and each face our own targets. Looks like I'm not the only one who wants to see what the new calibrations can do!"
    
    scene bg battleground day with dissolve
    show mc mech at bl with dissolve:
        xzoom -1
    show aiM neu at br with dissolve
    
    $ E2D5S3_PracticeWon = 0
    #Combat, fairly easy match
    
    #$ context = "E2D5S3_2ndPractice"
    #$ enemy = "aiM"
    #$ mode = "default"
    #$ survived = 0
    #$ score = 0
    
    #$ mcEnergyMax = 200
    #$ mcEnergy = 200
    
    #if E2D5S2_Spirit == 2:
    #    $ enemyHPMax = 225
    #    $ enemyHP = 225
        
    #elif E2D5S2_Spirit == 1:
    #    $ enemyHPMax = 200
    #    $ enemyHP = 200
        
    #else:
    #    $ enemyHPMax = 175
    #    $ enemyHP = 175
        
    #show screen battle_screen
    #$renpy.pause(1)
    #jump qte_game
    
    
    



    "I face my opponent and go for my rifle. The enemy charges me so I take aim!"

    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E2D5S3_L1")
    menu:
        "Fire!":
            jump E2D5S3_W1
            
        "Freeze…":
            jump E2D5S3_L1

        "Wait…":
            jump E2D5S3_L1

        "Shoot!":
            jump E2D5S3_W1

        "Miss…":
            jump E2D5S3_L1


    label E2D5S3_W1:
        $ renpy.hide_screen ("timer_scr")
        
        
        show mc attR with Dissolve(.45)
        play sound rangeSound
        play sound2 hitSound
        
        show aiM att at br, Shake(None, 1, dist=20):
        
        "Before my enemy can get close, I shoot one test shot and hit it in the chest. The AI is pushed back from the force of my blast!"
        "Yes! We are back in business!"
        jump E2D5S3_COMBCONV

    label E2D5S3_L1:
        $ renpy.hide_screen ("timer_scr")
        
        
        show mc attR with Dissolve(.45)
        play sound rangeSound
        play sound2 hitSound
        
        show aiM blo at br, Shake(None, .5, dist=10):
        
        
        "I fumble my shot and miss as the enemy quickly approaches. Luckily, I dodge its sword just in time and shoot another blast, which connects. The AI's shield shimmers as it takes damage."
        "That was close! But it looks like my weapons are finally working."
        jump E2D5S3_COMBCONV
        

    label E2D5S3_COMBCONV:
    "Just to be sure, I run through my other weapons. Everything seems to be in working order."
    "As I settle on my long sword, I see the looming shadow of an attack!"


    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E2D5S3_L2")
    menu:
        "Freeze…":
            jump E2D5S3_L2

        "Wait…":
            jump E2D5S3_L2

        "Dodge!":
            jump E2D5S3_W2

        "Stumble…":
            jump E2D5S3_L2

        "Block!":
            jump E2D5S3_W2


    label E2D5S3_L2:
        $ renpy.hide_screen ("timer_scr")
        
        
        show aiM neu att at br, Shake(None, 1, dist=20):
            xoffset 0
            parallel:
                easeout .1 alpha 1.0
            parallel:
                easeout .1 xoffset -400
        $renpy.pause(.1)

        play sound meleeSound
        show aiM att at br with Dissolve(.2):
            xoffset -600

        show white with Dissolve(0.15):
        play sound2 hitSound
        hide white with Dissolve(0.25)
        
        show mc blo at bl, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -150
        
        "I try to block but the AI feigns the attack and strikes my other side. My dashboard flashes red warning lights as my energy is nearly drained from absorbing the blow."
        
        play sound meleeSound
        
        show aiM att at br, Shake(None, .25, dist=10):
            xoffset -800
        show mc attM at bl, Shake(None, .25, dist=10):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -150
        with Dissolve(.2)
            
        show white with Dissolve(0.15):
        play sound2 hitSound
        hide white with Dissolve(0.25)
        
                
        
        "I swing my sword in a wide arc and connect with its side, but at the same time, the AI strikes again and my GEAR goes dark."
        play sound Depowered
        hide mc with dissolve
        jump E2D5S3_CONVERGEB1

    label E2D5S3_W2:
        $ renpy.hide_screen ("timer_scr")
        
        show aiM neu att at br, Shake(None, 1, dist=20):
            xoffset 0
            parallel:
                easeout .1 alpha 1.0
            parallel:
                easeout .1 xoffset -400
        $renpy.pause(.1)

        play sound meleeSound
        show aiM att at br with Dissolve(.2):
            xoffset -600

        show white with Dissolve(0.15):
        play sound2 hitSound
        hide white with Dissolve(0.25)
        
        show mc blo at bl, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -150
        
        "I quickly block the attack and parry with a strike of my own! I feign an attack to the right, and when the AI moves to block, I change sides and strike above instead."
        
        play sound meleeSound
        
        show aiM att at br, Shake(None, .25, dist=10):
            xoffset -800
        show mc attM at bl, Shake(None, .25, dist=10):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -150
        with Dissolve(.2)
            
        show white with Dissolve(0.15):
        play sound2 hitSound
        hide white with Dissolve(0.25)
        
        "The AI does not move fast enough and absorbs the blow. Before it can recover, I slice it again from below, and the AI goes dark."
        
        play sound Depowered
        hide aiM with dissolve
        $ E2D5S3_PracticeWon = 1
        jump E2D5S3_CONVERGEB1

    label E2D5S3_CONVERGEB1:
    "Soon, the match is over."

    
    
    
    
    
    
    hide aiM with dissolve
    show mc mech at bl with dissolve:
        xoffset 0
        xzoom -1
    if E2D5S3_PracticeWon == 1:
        pf "Looks like things are working perfectly on my end."
    
    else:
        "The calibration was successful, but I still need to practice more."
        pf "My equipment is all good. Looks like my calibrations are fine now."
    
    voice "audio/voice/E2/D5/SS/29.ogg"
    ss "Same here. The tweak Valerie made might look small on paper, but the extra speed feels a lot better."
    voice "audio/voice/E2/D5/MA/0-12.ogg"
    ma "My rifle cooldown period also dropped about half a second!"
    voice "audio/voice/E2/D5/KI/39.ogg"
    ki "Good. Between the GEAR repairs and calibration upgrades, we should have a strong performance today."
    
    stop music fadeout 5
    scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    "Suddenly, a notification pops up on my screen."
    
    "ACE Notification" "Hello ACE-2049-11 Pilot, your battle is scheduled to begin soon. Please exit your GEAR so it may undergo pre-match preparation."
    
    pf "Hey, did you guys just receive a message too?"
    voice "audio/voice/E2/D5/SS/30.ogg"
    ss "Yeah. That reminds me, we completely forgot to pick a team name!"
    voice "audio/voice/E2/D5/SS/31.ogg"
    ss "ACE-2049-11 doesn't go well on a t-shirt."
    voice "audio/voice/E2/D5/KI/40.ogg"
    ki "We can choose a name later. Mayu and I will meet you guys in the Pre-combat room."
    voice "audio/voice/E2/D5/SS/32.ogg"
    ss "Okay."
    pf "Sounds good."
    
    #Fade black
    stop ambient fadeout 5
    scene cg GEAR cockpit first1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    $renpy.pause(1)
    play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
    $renpy.pause(1)
    scene black with fade
    play sound "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
    #cockpit exiting noises
    #after they go to the war room
    # do we have ambient for war room?
    "We quickly hop out of our GEARs and separate into our corresponding change rooms. {w}Once we've changed into our pilot suits, we meet in front of the holo-table in the precombat room."
    $ shoOut = "Pilot"
    $ mayOut = "Pilot"
    $ kaoOut = "Pilot"
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
    scene bg campus battleroom day
    show shou neu at l3:
        xoffset -150
    with fade
    show kaori neu at cc:
        xoffset 200
    show mayu neu at r3:
        xoffset 200
        xzoom -1
    with dissolve
    voice "audio/voice/E2/D5/SS/33.ogg"
    ss "Do we know who we're matched against?"
    voice "audio/voice/E2/D5/KI/41.ogg"
    ki "No."
    pf "They don't tell you at ACE who you'll play?"
    show mayu thi at r3
    "Mayu shakes her head."
    show drop:
        xoffset 1375
        yoffset 135
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D5/MA/0-13.ogg"
    ma "No, they do... I think it's just been a busy week for us so we didn't check."
    show kaori thi at cc
    show mayu neu at r3
    voice "audio/voice/E2/D5/KI/42.ogg"
    ki "Yeah, getting a sponsor was our top priority. I didn't have time to research our opponent."
    show shou mis at l3
    voice "audio/voice/E2/D5/SS/34.ogg"
    ss "Guess we're all finding out now then!"
    show kaori neu at cc
    "Kaori nods as she flips through the menus on the holo-table."
    voice "audio/voice/E2/D5/KI/43.ogg"
    ki "Let's see here..."
    show exclamation:
        xoffset 920
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori cur at cc
    voice "audio/voice/E2/D5/KI/44.ogg"
    ki "Ah!"
    stop music fadeout 2.0
    voice "audio/voice/E2/D5/KI/45.ogg"
    ki "ACE-2049-11 vs..."
    show kaori dis at cc
    show exclamation:
        xoffset 80
        yoffset 20
        xzoom .75
        yzoom .75
    show shou sur at l3
    "Kaori suddenly deflates while Shou perks up with excitement."
    voice "audio/voice/E2/D5/SS/35.ogg"
    ss "YES."
    show shou hap at l3
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 2.0
    pf "ACE-2049-11 vs Claw of the Wild?"
    voice "audio/voice/E2/D5/SS/36.ogg"
    ss "You're in for a treat, broseph!"
    pf "Well, you seem excited, but Kaori looks less than pleased."
    show kaori ann at cc
    show shou mis at l3
    voice "audio/voice/E2/D5/SS/37.ogg"
    ss "Nah, that's just her default expression."
    show kaori ang at cc
    voice "audio/voice/E2/D5/KI/46.ogg"
    ki "Shut up! Idiot. Of course you like \"Claw of the Wild\"."
    show kaori ann at cc
    pf "... Can someone please fill me in?"
    show mayu cur at r3
    voice "audio/voice/E2/D5/MA/0-14.ogg"
    ma "Um, well, the leader of that team is in the same dorm as Shou. Tatsuo Kimura."
    pf "Oh ok. But that still doesn't explain why Kaori--"
    show mayu wor at r3
    show vein:
        xoffset 920
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D5/KI/47.ogg"
    ki "Because he's even more annoying than Shou."
    show shou ske at l3
    "Shou crosses his arms."
    voice "audio/voice/E2/D5/SS/38.ogg"
    ss "So rude. Tatsuo and I are incredibly pleasant."
    show mayu smi at r3
    voice "audio/voice/E2/D5/MA/0-15.ogg"
    ma "Maybe we should plan for the match while we still have time...?"
    show kaori cur at cc
    show shou cur at l3
    "We all glance at Mayu."
    show panic:
        xoffset 1375
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu ner at r3
    voice "audio/voice/E2/D5/MA/0-16.ogg"
    ma "I-I mean if it's not too much trouble."
    show kaori neu at cc
    show shou smi at l3
    stop music fadeout 3
    ### VOICE - she says "Wind" instead of "Wild"
    voice "audio/voice/E2/D5/KI/48.ogg"
    ki "She's right. I'll pull up what information I can on \"Claw of the Wild\"."
    show mayu neu at r3
    # sfx?
    "We wait while Kaori sets up the playing field on the hologram. Soon both our GEARs and the enemy's GEARs populate the field."
    voice "audio/voice/E2/D5/KI/49.ogg"
    ki "Okay, done. Shou, do you have some insight on them?"
    show shou thi at l3
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
    "Shou scrunches his brows."
    voice "audio/voice/E2/D5/SS/39.ogg"
    ss "The team is basically Tatsuo. If we can take him out, then the rest won't be much of a challenge without his leadership."
    show mayu cur at r3
    voice "audio/voice/E2/D5/MA/0-17.ogg"
    ma "If he's calling the shots, wouldn't he be hanging back in a safe position?"
    show shou neu at l3
    voice "audio/voice/E2/D5/SS/40.ogg"
    ss "It's not his style. He'll be the one charging in head-first."
    show mayu neu at r3
    
    menu:
        "That seems like a tactical error.":
            pf "Maybe we can use that to our advantage?"
            show kaori mis at cc
            "Kaori nods."
    
        "I like his style." if E1D4S4_FollowMatchPlan == 0:
            pf "Sounds like an excellent thing to do."
            show kaori thi at cc
            voice "audio/voice/E2/missing/kaori/ofcourse_Kaori.ogg"
            ki "Of course {i}you'd{/i} think that."
            pf "Hey, it worked for me."
            show kaori dis at cc
            voice "audio/voice/E2/D5/KI/50.ogg"
            ki "Only because of that core overdrive thing which--for the record--you still don't know how to use."
            "I cross my arms defiantly, even though she's right."
            show kaori neu at cc
            "Kaori refocuses on the hologram."
    
        "Keep listening silently.":
            pf "..."
            show mayu ske at r3
            voice "audio/voice/E2/D5/MA/0-18.ogg"
            ma "Is it possible to plan around that?"
            show kaori mis at cc
            "Kaori nods."
            show mayu neu at r3
    
    voice "audio/voice/E2/D5/KI/51.ogg"
    ki "We can setup a trap and focus target him when he rushes in."
    # sfx?
    show kaori neu at cc
    "We watch as Kaori maps out our plan of operation."
    show shou smi at l3
    voice "audio/voice/E2/D5/SS/41.ogg"
    ss "Hmm, this might actually work."
    show mayu smi at r3
    voice "audio/voice/E2/D5/MA/0-19.ogg"
    ma "I agree."
    
    menu:
        "The plan is good.":
            pf "Sounds fine to me."
    
        "What if Shou's intel is wrong?":
            pf "What if Tatsuo doesn't charge in?"
            show shou ner at l3
            "Shou pretends to be wounded."
            voice "audio/voice/E2/D5/SS/42.ogg"
            ss "Are you doubting me, broseph?"
            
            if E1D4S4_FollowMatchPlan == 0:
                pf "People do unexpected things all the time."
                show shou mis at l3
                voice "audio/voice/E2/D5/SS/43.ogg"
                ss "Hehe, that's true."
                
            else:
                pf "We should think consider it a possibility, just in case."
                show shou neu at l3
                voice "audio/voice/E2/D5/SS/44.ogg"
                ss "Fair enough."
            
            voice "audio/voice/E2/D5/KI/52.ogg"
            ki "Either way, our positioning will be safe."
            show kaori mis at cc
            voice "audio/voice/E2/D5/KI/53.ogg"
            ki "Even if they don't charge in, we can protect Mayu while she withers them down with long range firepower."
            pf "Alright."
            
    show mayu neu at r3
    voice "audio/voice/E2/D5/MA/0-20.ogg"
    ma "I think his teammates will work hard to protect him if they see what we're doing."
    show shou thi at l3
    voice "audio/voice/E2/D5/SS/45.ogg"
    ss "Hmm, that's true."
    show dots:
        xoffset 1375
        yoffset 135
        xzoom .75
        yzoom .75
    show dots2:
        xoffset 80
        yoffset 20
        xzoom .75
        yzoom .75
    show kaori neu at cc
    "We think for a moment."
    voice "audio/voice/E2/D5/KI/54.ogg"
    ki "One of us can divert their attention at the start of the match to get them to separate."
    show shou ske at l3
    voice "audio/voice/E2/D5/SS/46.ogg"
    ss "Huh? One person against three GEARs? That's a suicide mission."
    voice "audio/voice/E2/D5/KI/55.ogg"
    ki "It's about winning the match Shou, not the individual battle. This sets us up with a favourable trade."
    show mayu cur at r3
    show shou neu at l3
    voice "audio/voice/E2/D5/MA/0-21.ogg"
    ma "That makes sense, but who'll be the decoy?"
    #show kaori ner at cc
    #show mayu ner at r3
    #show shou ner at l3
    "We look at each other. Whoever is picked will surely get depowered, but hopefully they can keep the enemy distracted long enough for Tatsuo to be taken out."
    

    menu:
        "I'll do it.":
            $ E2D5S3_Distraction = "MC"
            pf "I got this."
            show kaori neu at cc
            show mayu sur at r3
            show shou sur at l3
            voice "audio/voice/E2/D5/SS/47.ogg"
            ss "Really?"
            voice "audio/voice/E2/D5/MA/0-22.ogg"
            ma "Are you sure?"
            "I nod."
            show mayu smi at r3
            show shou smi at l3
            pf "You guys have competed together before and know how to play off each other's strengths to defeat Tasuo."
            show kaori neu at cc
            "Kaori crosses her arms."
            voice "audio/voice/E2/D5/KI/56.ogg"
            ki "Just remember that your goal is to delay them from covering Tatsuo."
            
            if E1D4S4_FollowMatchPlan == 0:
                show vein:
                    xoffset 920
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori dis at cc
                voice "audio/voice/E2/D5/KI/57.ogg"
                ki "You better stick to the plan this time."
                pf "I'll keep them off you guys as long as I can."
    
        "It should be Koari.":
            $ E2D5S3_Distraction = "Kaori"
            pf "You can do it, Kaori."
            show kaori neu at cc
            show mayu neu at r3
            show shou neu at l3
            "Kaori crosses her arms."
            voice "audio/voice/E2/D5/KI/58.ogg"
            ki "As long as you're clear with the plan."
            show mayu smi at r3
            voice "audio/voice/E2/D5/MA/0-23.ogg"
            ma "Yes."
            show shou smi at l3
            voice "audio/voice/E2/D5/SS/48.ogg"
            ss "Mhm."
            pf "Yup."
            show kaori mis at cc
            "She nods."
            voice "audio/voice/E2/D5/KI/59.ogg"
            ki "Okay, I'll buy you guys time."
    
    
        "Send Shou!":
            $ E2D5S3_Distraction = "Shou"
            pf "Shou's got it."
            show confused:
                xoffset 80
                yoffset 20
                xzoom .75
                yzoom .75
            show shou sur at l3
            voice "audio/voice/E2/D5/SS/49.ogg"
            ss "Whaaaa? What?"
            show kaori neu at cc
            voice "audio/voice/E2/D5/KI/60.ogg"
            ki "Agreed."
            show shou ske at l3
            "Shou scratches the back of his head."
            voice "audio/voice/E2/D5/SS/50.ogg"
            ss "Are you guys serious? Sending me on the suicide mission..."
            show drop:
                xoffset 920
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori ske at cc
            voice "audio/voice/E2/D5/KI/61.ogg"
            ki "Don't make it sound so grim."
            show mayu wor at r3
            "Mayu sniffles."
            show shou ner at l3
            voice "audio/voice/E2/D5/SS/51.ogg"
            ss "Mayu?"
            show kaori neu at cc
            show crying:
                xoffset 1375
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu sad at r3
            voice "audio/voice/E2/D5/MA/0-24.ogg"
            ma "I'll miss you..."
            show shou wor at l3
            "Shou steps back, panic washing over his face."
            show panic:
                xoffset 80
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D5/SS/52.ogg"
            ss "Hey! Don't say stuff like that!"
            show kaori mis at cc
            "I think I see Kaori crack a small smile at Mayu's acting. At least I hope it's just an act--it's pretty convincing."
            voice "audio/voice/E2/D5/KI/62.ogg"
            ki "Anyways. Keep them off us as long as you can, and we'll make a sweeping advance after depowering Tatsuo."
            show shou thi at l3
            voice "audio/voice/E2/D5/SS/53.ogg"
            ss "Fine. I'll keep them busy for you guys."
            show mayu smi at r3
            voice "audio/voice/E2/D5/MA/0-25.ogg"
            ma "Thank you, Shou."
    
        "Make it Mayu.":
            $ E2D5S3_Distraction = "Kaori"
            pf "Mayu can do it."
            show kaori ske at cc
            show confused:
                xoffset 1375
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu sur at r3
            show shou ske at l3
            voice "audio/voice/E2/D5/MA/0-26.ogg"
            ma "E-Eh?"
            show mayu ner at r3
            voice "audio/voice/E2/D5/MA/0-27.ogg"
            ma "I mean I will if that's what you want..."
            show kaori ann at cc
            "Kaori glares at me."
            voice "audio/voice/E2/D5/KI/63.ogg"
            ki "Are you stupid? She's geared to provide firing support."
            "Oops."
            show kaori neu at cc
            show shou neu at l3
            voice "audio/voice/E2/D5/KI/64.ogg"
            ki "Anyway, I'll do it as long as you guys know what to do."
            show mayu smi at r3
            show shou smi at l3
            "The three of us nod."
    
        "Stay silent.":
            $ E2D5S3_Distraction = "Kaori"
            "There's an awkward pause."
            show kaori neu at cc
            voice "audio/voice/E2/D5/KI/65.ogg"
            ki "Okay, I'll keep them distracted while you guys handle Tatsuo. You guys understand the plan?"
            show mayu smi at r3
            show shou smi at l3
            "We all nod."
            
    show kaori cur at cc
    show mayu cur at r3
    show shou cur at l3
    stop music fadeout 3
    "As if on cue, the map flashes red as the arena entrance doors slide open."
    show shou mis at l3
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E2/D5/SS/54.ogg"
    ss "Alright! Time to \"Shou\" them what we got!"
    show storm:
        xoffset 920
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori dis at cc
    show mayu hap at r3
    "Kaori lets out a sigh."
    voice "audio/voice/E2/D5/KI/66.ogg"
    ki "...You said \"{i}Shou{/i}\" in your head, didn't you?"
    show mayu smi at r3
    show shou smi at l3
    voice "audio/voice/E2/D5/SS/55.ogg"
    ss "Ummmmmmmm."
    show shou hap at l3
    voice "audio/voice/E2/D5/SS/56.ogg"
    ss "Maybe."
    show note:
        xoffset 1375
        yoffset 135
        xzoom .75
        yzoom .75
    "Mayu stifles a giggle. If anything, you can always count on Shou to keep team morale up!"
    show kaori neu at cc
    pf "Let's go."
    
    hide kaori with dissolve
    hide mayu with dissolve
    hide shou with dissolve
    scene black with fade
    
    # Switch to arena
    
    jump E2D5S4
