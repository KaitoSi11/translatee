label E1D3S4:
    
    "I pull up the schedule on my phone and check my first class: GEAR Arsenal 201. {w}The building isn't too far away either."
    scene bg campus building day with fade
    stop ambient fadeout 3
    "I soon reach the building."
    scene bg campus auditorium day with fade
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 1
    "The classroom is about half the size of the lecture hall for my Piloting 101 class. {w}For some reason, this is a comfort to me, probably because it reminds me of the class sizes at CINY."
    play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 1
    "I take a seat near the back of the room just as the professor enters."
    show professorM2 extra at cc with dissolve
    voice "audio/voice/E1/D3/S4/Prof/1.ogg"
    prof1m "Good morning, class. Welcome to GEAR Arsenal 201. I'm sure you're all tired of hearing the same welcome spiel so I won't even bother with it. Instead, we're going to dive straight into the material."
    voice "audio/voice/E1/D3/S4/Prof/2.ogg"
    prof1m "Question: Who can name one of the leading companies in GEAR weapon manufacturing?"
    
    menu:
        "Potato Shooter Incorporated.":
            pf "Potato Shooter Incorporated!"
            "The class erupts into laughter."
            show drop:
                xoffset 675
                yoffset 50
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Prof/3.ogg"
            prof1m "Very funny. A real company would be Paragon Weaponry."
    
        "{color=#00ff00}{b}Paragon Weaponry.{/b}{/color}" if (MCStory == 2):
            jump E1D3S4_MCStory1
        
        "Paragon Weaponry." if (MCStory != 2):
            label E1D3S4_MCStory1:
            "Before I have a chance to answer, another student chimes in."
            voice "audio/voice/E1/D3/S4/stu8m/2.ogg"
            stu8m "Vector Industries!"
            voice "audio/voice/E1/D3/S4/Prof/4.ogg"
            prof1m "Sorry, incorrect."
            pf "Paragon Weaponry."
            show note:
                xoffset 675
                yoffset 50
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Prof/5.ogg"
            prof1m "Very good!"
            voice "audio/voice/E1/D3/S4/stu8m/3.ogg"
            stu8m "Why isn't it Vector?"
            voice "audio/voice/E1/D3/S4/Prof/6.ogg"
            prof1m "Vector deals with thrusters and manoeuvrability whereas Paragon deals with weaponry… Hence the name \"Paragon Weaponry\"."
    
        "Dasshu.":
            pf "Dasshu."
            voice "audio/voice/E1/D3/S4/Prof/7.ogg"
            prof1m "That would be incorrect. Dasshu has only recently begun investing in the Cenorobotics field. However, their core business is still energy drinks. A correct answer would be Paragon Weaponry."
    
        "Aludian Enterprises.":
            pf "Aludian Enterprises."
            voice "audio/voice/E1/D3/S4/Prof/8.ogg"
            prof1m "Not quite. While Aludian Enterprises is certainly creating waves in the media, they are by no means a leading company. An example of an industry veteran would be Paragon Weaponry."
    voice "audio/voice/E1/D3/S4/Prof/9.ogg"
    prof1m "Their recent area of study has shown that..."
    
    "He goes into the details of Paragon Weaponry's R&D and the future of beam weaponry for the remainder of class."
    stop music fadeout 3
    $renpy.pause(1)
    scene black with fade
    #time passes, class ends
    $renpy.pause(1)
    scene bg campus auditorium day with fade
    $renpy.pause(1)
    show professorM2 extra at cc with dissolve
    voice "audio/voice/E1/D3/S4/Prof/10.ogg"
    prof1m "That's all the time we have for today. You'll find this week's readings and assignments on your weblink. Have a good day!"
    hide professorM2 extra with dissolve
    play sound "audio/sfx/Human/Class End.ogg"
    "Students scramble to collect their things before hurrying out of the room. {w}I think I'll go back to the hangar. This class has inspired me to go have a proper look at my GEAR."
    stop ambient fadeout 3
    scene black with fade
    play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
    $renpy.pause(2.5)
    play ambient "audio/ambience/Hangar.ogg" fadein 1 fadeout 1
    #scene bg campus hangar day with dissolve
    "I take the path through the Pilot's Lounge and follow the tunnels until I reach my GEAR."
    scene cg GEAR hangar first with fade
    play sound "audio/sfx/GEAR/GEAR Elevator.ogg"
    $renpy.pause(2.5)
    "Pulling down the ladder beside my docking station, I climb up to the top, which is about level with the chest section of my robot."
    scene black with fade
    play sound [ "audio/sfx/GEAR/GEAR Cockpit Open.ogg"]
    "I unlock the chest cavity. With a mechanical roar, it splits open in separating panels, revealing a lowered seat. {w}I easily hop into the seat, and breathe in the comforting scent of metal and plastic. It faintly reminds me of new-car smell."
    $renpy.pause(1)

    $ persistent.gpix[4][0] = 1
    $ persistent.gpix[5][0] = 1
    $ persistent.gpix[6][0] = 1
    scene cg GEAR cockpit first1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with Dissolve(2.5)
    $renpy.pause(1)
    play sound "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
    stop ambient fadeout 3
    "Once I'm settled, I trigger the closing sequence. As the chest panels return, my seat scoops me further into my GEAR until I'm nestled in the darkness of the cockpit."
    $renpy.pause(1)
    play sound "audio/sfx/GEAR/GEAR Boot Up 1.ogg"
    $renpy.pause(1.5)
    scene cg GEAR cockpit first2 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with Dissolve(1.5)
    $renpy.pause(1.5)
    "I initiate the boot up sequence. The cockpit glows a faint red, then flickers into life, and I can't help but smile at the familiarity of it all. {w}The bright glow of the panels illuminate the interior until there isn't a trace of a shadow left. Statistics blink around me in a series of rapid numbers and diagrams."
    $renpy.pause(1.5)
    play sound "audio/sfx/GEAR/GEAR Boot Up 2.ogg"
    $renpy.pause(1.5)
    scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with Dissolve(2.5)
    play ambient "audio/ambience/GEAR Cockpit.ogg" fadein 1 fadeout 1
    $renpy.pause(1)
    voice "audio/voice/E1/D3/S4/EagleAI/1.ogg"
    GEARpf "Gear initialization sequencing complete."
    
    "The familiar voice of my GEAR feels like a warm welcome from an old friend."
    
    pf "Eagle, please run a comprehensive check."
    
    voice "audio/voice/E1/D3/S4/EagleAI/2.ogg"
    GEARpf "System in progress..."
    
    "Nothing to do now but wait. {w}The lights along my display pulse with changing colours as the check progresses. It flows through warm colours: red, orange, yellow, before illuminating the cockpit with a bright green."
    $renpy.pause(1)
    voice "audio/voice/E1/D3/S4/EagleAI/3.ogg"
    GEARpf "All system functions: normal."
    
    voice "audio/voice/E1/D3/S4/EagleAI/4.ogg"
    GEARpf "Unknown docking station detected."
    
    pf "Register the current dock as home station."
    $renpy.pause(1)
    voice "audio/voice/E1/D3/S4/EagleAI/5.ogg"
    GEARpf "Completed."
    
    voice "audio/voice/E1/D3/S4/EagleAI/6.ogg"
    GEARpf "Recommendation: please update system calibration configuration."
    
    "This is recommended all the time. Whenever we change locations, Eagle will request a recalibration of the system. Even the slightest difference in air pressure can trigger an inaccuracy."
    
    "At least the process is easy. All I have to do is make sure I correctly follow sequential number order so Eagle can achieve the necessary internal calculations." 
    
    pf "Alright, start up the process."
    voice "audio/voice/E1/D3/S4/EagleAI/7.ogg"
    GEARpf "Calibration sequence initiating..."
    play sound "audio/sfx/GEAR/GEAR Virtual Training Simulator.ogg"
    # Let's set our variables so the game knows where we are at
    #$ firstCalibration = 0
    #$ context = "E1D3S4_SystemCalibrationLoopback"
    # 6 and 6
    #$ numBase = 6
    #$ numLimit = 6
    # We will now display the numbers minigame. Hopefully, the if statements for the variables will take us back to where we need to be.
    #jump numbers_game
    # If all goes well, it should jump back here vvv
    #label E1D3S4_SystemCalibrationLoopback:
        
    #    if firstCalibration == 0:
    #        voice "audio/voice/E1/D3/S4/EagleAI/8.ogg"
    #        GEARpf "Calibration sequence failed. Please try again."
    #        jump numbers_game
            
    #    else:
    #        voice "audio/voice/E1/D3/S4/EagleAI/9.ogg"
    #        GEARpf "Calibration successful."
    #        pf "Perfect."
  
    "I give it a few minutes as Eagle automatically adjusts itself."
    "..."
    "....."
    voice "audio/voice/E1/D3/S4/EagleAI/9.ogg"
    GEARpf "Calibration successful."
    pf "Perfect."  
    
    "Everything seems to be in order."
    $renpy.pause(1)
    stop ambient fadeout 3
    scene cg GEAR cockpit first1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    $renpy.pause(1)
    play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
    $renpy.pause(1)
    "After one last look, I shut down my GEAR and unlock the chest cavity again."
    scene black with fade
    play ambient "audio/ambience/Hangar.ogg" fadein 1
    play sound "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
    "Once I hop out, the panels slide back in place, until I hear the faint click of them locking."
    scene cg GEAR hangar first with fade
    if (E1D2S11_JoinedTheTeam == 0):
        play sound "audio/sfx/GEAR/GEAR Elevator.ogg"
        "I use the elevator and make my way to the ground. {w}As I stand alone in the quiet of the empty hangar, I feel a twinge of homesickness."
        play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 1
        "I expected ACE to be different from CINY, but I wasn't quite prepared for the reaction towards my GEAR. {w}It's no surprise that Japan's advancements in the field of Cenorobotics outweigh those of the States, but our machinery was built to last."
    
        "My GEAR may not be the newest model or packed with the latest weaponry or accessories, but I'm confident in its ability to fight."
    
        "A doubt wiggles into my train of thought. {w}Maybe it was a mistake to come here. I could have stayed at CINY. I was making high grades and had a group of friends I could rely on. I'd spend my afternoons practicing instead of sitting in a hangar... {w}just me and that weirdo from yesterday--"
        stop music fadeout 3
        "I do a double take as Shou walks steadily towards me."
    
    if (E1D2S11_JoinedTheTeam == 1):
        play sound "audio/sfx/GEAR/GEAR Elevator.ogg"
        "As I turn towards the elevator, I spot Shou waving at me. I nimbly make my way down and stand beside him."
        $renpy.pause(2.5)
        
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
    scene bg campus hangar day with fade
    show shou smi at cc with dissolve
    voice "audio/voice/E1/D3/S4/Shou/1.ogg"
    ss "Mr. Broseph."
    pf "Hey, how's it going?"
    show shou hap at cc
    voice "audio/voice/E1/D3/S4/Shou/2.ogg"
    ss "Good. Is this your \"go-to\" hangout place? This is the second time I've run into you here."
    pf "Heh, I guess it's starting to be. What are you doing here?"
    stop music fadeout 3
    show shou mis at cc
    voice "audio/voice/E1/D3/S4/Shou/3.ogg"
    ss "I just thought I'd pay a visit to my GEAR. It helps when I keep her company for a bit. Keeps her spirits up."
    
    menu:
        "That's why I only go for male GEAR.":
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 1
            pf "This is just further proof that females of all types are high maintenance."
            show shou cur at cc
            "Shou blinks, then laughs."
            show shou hap at cc with dissolve
            voice "audio/voice/E1/D3/S4/Shou/4.ogg"
            ss "Tell me about it. I take it your GEAR is a \"he\" then?"
            pf "I never really considered it to be either \"he\" or \"she\"."
            show shou mis at cc
            show bulb:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Shou/5.ogg"
            ss "Ahh, so it's a \"ze\"!"
            pf "Huh?"
            show shou smi at cc
            voice "audio/voice/E1/D3/S4/Shou/6.ogg"
            ss "You know, gender neutral."
            pf "Oh, well, sort of. I just call it an \"it\"."
            stop music fadeout 3
            show shou cur at cc
            voice "audio/voice/E1/D3/S4/Shou/7.ogg"
            ss "Oh, that too."
    
        "Her? You mean a girl?":
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 1
            pf "Is there a girl you're keeping captive in your GEAR?"
            show shou hap at cc with dissolve
            "Shou laughs."
            voice "audio/voice/E1/D3/S4/Shou/8.ogg"
            ss "If only… Unfortunately, no girl ever goes near my GEAR."
            show shou smi at cc
            "He sighs wistfully, while I try very hard to keep a straight face."
            pf "I'm so sorry."
            stop music fadeout 3
            show shou sad at cc with dissolve
            show crying:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Shou/9.ogg"
            ss "Me too."
    
        "Inanimate objects don't have genders.":
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 1
            pf "Her?"
            show shou smi at cc
            voice "audio/voice/E1/D3/S4/Shou/10.ogg"
            ss "Yeah."
            pf "... Your girlfriend?"
            show shou hap at cc with dissolve
            "Shou laughs."
            voice "audio/voice/E1/D3/S4/Shou/11.ogg"
            ss "No, my GEAR."
            pf "Your GEAR is a \"she\"?"
            show shou mis at cc
            voice "audio/voice/E1/D3/S4/Shou/12.ogg"
            ss "Yeah! What's yours?"
            pf "My GEAR."
            show shou smi at cc
            voice "audio/voice/E1/D3/S4/Shou/13.ogg"
            ss "Right, a \"she\" or a \"he\"?"
            pf "An \"it\"."
            show shou cur at cc
            voice "audio/voice/E1/D3/S4/Shou/14.ogg"
            ss "Ohhh."
            show dots:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            "He pauses."
            show shou smi at cc
            voice "audio/voice/E1/D3/S4/Shou/15.ogg"
            ss "Well, thanks anyway."
            pf "For what?"
            show shou mis at cc
            voice "audio/voice/E1/D3/S4/Shou/16.ogg"
            ss "For thinking it was possible for me to have a girlfriend."
            stop music fadeout 3
            pf "Well, then."
            
    show shou smi at cc with dissolve
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
    voice "audio/voice/E1/D3/S4/Shou/17.ogg"
    ss "So what were you doing here?"
    pf "Just checking to make sure everything's working fine."
    show shou hap at cc
    voice "audio/voice/E1/D3/S4/Shou/18.ogg"
    ss "And does it?"
    pf "Yeah."
    show shou cur at cc with dissolve
    "He glances curiously at my GEAR."
    show shou mis at cc
    voice "audio/voice/E1/D3/S4/Shou/19.ogg"
    ss "How about a simulator match?"
    "I shrug. It'd be nice to get a feel for how things are done at ACE."
    pf "Sure."
    show shou smi at cc
    voice "audio/voice/E1/D3/S4/Shou/20.ogg"
    ss "We can both use the basic robot program. That way, all accessories and weapons will be the same and it'll be based on skill alone."
    pf "May the best man win."
    #show shou hap at cc with dissolve
    #hide shou with dissolve
    scene black with fade
    play sound "audio/sfx/GEAR/GEAR Elevator.ogg"
    $renpy.pause(2.5)
    #scene cg GEAR hangar first at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    #$renpy.pause(2.5)
    "He grins and races in the opposite direction. I see him pause by a green GEAR before I get back into my own."
    play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
    $renpy.pause(1.5)
    scene cg GEAR cockpit first1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    #play sound "audio/sfx/Impacts/Luggage Drop.ogg"
    $renpy.pause(1.5)
    stop ambient fadeout 3
    play sound "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
    $renpy.pause(1.5)
    play sound "audio/sfx/GEAR/GEAR Boot Up 1.ogg"
    $renpy.pause(1.5)
    scene cg GEAR cockpit first2 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    play ambient "audio/ambience/GEAR Cockpit.ogg" fadein 1
    $renpy.pause(1.5)
    play sound "audio/sfx/GEAR/GEAR Boot Up 2.ogg"
    #$renpy.pause(2.5)
    scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    "Once I'm settled in the cockpit, I switch on the open network configuration."
    stop music fadeout 3
    play sound "audio/sfx/GEAR/GEAR Virtual Training Simulator.ogg"
    "Immediately, a request from Shou comes in, and I accept. After we're connected, we boot up our virtual training simulation program."
    stop ambient fadeout 3
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 1
    #Open up rapid mini-game part so the mechs and such appear but no QTE yet
    
    
   
    
    scene bg battleground day with Dissolve(2.5)
    show mc mech at bl with dissolve:
        xzoom -1
    show shou mech at br with dissolve
    show shiny:
        xoffset 1200
        yoffset 50
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S4/Shou/30.ogg"
    ss "Oh! Very fancy. I haven't seen an American style GEAR up close before."
    
    pf "Mhm."
    
    "I experiment with my GEAR controls and watch in amusement as it makes the same movements within the simulator."
    "Simulators are freakishly accurate at emulating the real thing, but it still can't quite replicate the feeling of live matches. {w}You can't feel every impact or even the slightest shift in motion within a VTS."
    voice "audio/voice/E1/D3/S4/Shou/31.ogg"
    ss "As you can see, both of us are kitted with the same standard equipments. You have your energy shield for blocking, thrusters for movement, a ranged weapon, and a close combat weapon."
    
    "I evaluate my GEAR and find all the components he mentioned."
    
    pf "Any particular reason why we aren't playing from our personal arsenal?"
    voice "audio/voice/E1/D3/S4/Shou/32.ogg"
    ss "This will level the playing field. We'll have to win by skill alone."
    
    pf "Trying to see what I'm made of?"
    
    "Shou just grins."
    voice "audio/voice/E1/D3/S4/Shou/33.ogg"
    ss "Remember, you have to use the right tool at the right time. There's usually more than one right move you can make, but you have to think fast!"
    
    menu:
        "Alright, thanks!":
            pf "So the trick is to just react accordingly."
            voice "audio/voice/E1/D3/S4/Shou/34.ogg"
            ss "You got it!"
    
        "This isn't my first time.":
            pf "I'm no stranger to penetrating a GEAR with my beamblade."
            "Shou snorts out a laugh."
            voice "audio/voice/E1/D3/S4/Shou/35.ogg"
            ss "I hope you soften them up first with some shots."
            "I can't stop the grin on my face."
    
        "Let's get on with it.":
            pf "Why are we still talking? Can I shoot you yet?"
            show note:
                xoffset 1175
                yoffset 50
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Shou/36.ogg"
            ss "I'm loving the enthusiasm."
    
    #"Once the match starts, I'll have to react to his moves in a rapid succession until the battle is over. {w}Whatever the right move is, I'll have to play that out carefully. Accuracy is the key."
    voice "audio/voice/E1/D3/S4/Shou/37.ogg"
    ss "Are you ready?"
    pf "Yup."
    voice "audio/voice/E1/D3/S4/Shou/38.ogg"
    ss "Let's do this!"
    
    
    
    $ survived = 0
    $ practiceScore = 0
    
    $ mcEnergyMax = 200
    $ mcEnergy = 200
    $ enemyHPMax = 200
    $ enemyHP = 200
    
    $ qtebase = 10
    $ qtereaction = qteath + qtetrack + qtebase
    $ qtetotal = qtereaction
    $ t_var = qtereaction
    
    
    #$ inv.add("defaultCore")
    #$ inv.add("defaultFrame")
    #$ inv.add("defaultThruster")
    #$ inv.add("defaultBuster")
    #$ inv.add("defaultRifle")
    
    #$ inv.equip("defaultCore")
    #$ inv.equip("defaultFrame")
    #$ inv.equip("defaultThruster")
    #$ inv.equip("defaultBuster")
    #$ inv.equip("defaultRifle")
    
    
    
    #show screen battle_screen
    # Start rapid combat sequence, there is no failure state
    #$ context = "E1D3S4_ShouPracticeComplete"
    #$ enemy = "shou"
    #$ mode = "default"
    #$renpy.pause(1)
    #jump qte_game
    # And jump back here after timer ends
    
    
 


    "My hands fall naturally into place and grip the controls. I can't stop the smile that spreads across my face as my heart beats faster in anticipation."
    "I've missed this."
    "Eagle shifts into a fighting stance and holds out his gun, while Shou activates his thrusters and points his double guns at me."



    $ E1C1E1_C = 0

    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E1C1E1_L1")
    menu:
        "Dodge!":
            jump E1C1E1_W1

        "Slow…":
            $ E1C1E1_C += 1
            jump E1C1E1_L1

        "Evade!":
            jump E1C1E1_W1

    label E1C1E1_L1:
        $ renpy.hide_screen ("timer_scr")
        
        
        show shou att with Dissolve(.45):
            xoffset 0
        play sound "audio/sfx/GEAR Combat/SMG.ogg"
        $renpy.pause(.35)
        
        play sound2 hitSound
        
        show mc blo at bl, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -75
                
                
        "I'm too slow to react and can't move out of the way, but I raise my shields in the nick of time and absorb the hit."
        "Still, my dashboard flashes in warning. I took way too much damage! I should try to minimize the hits I take… there's no way I can survive another full hit."
        jump E1COMBATCONVERGENCE1

    label E1C1E1_W1:
        $ renpy.hide_screen ("timer_scr")
        
        
        show shou att with Dissolve(.45):
            xoffset 0
        play sound "audio/sfx/GEAR Combat/SMG.ogg"
        $renpy.pause(.05)
        
        play sound2 dodSound
        show mc dod at bl with Dissolve(.45):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -150

        
        
        "I dash out of the way and his attack misses its mark. I equip one of my guns and return fire. He dodges, but my shot still grazes him and he takes some damage."
        jump E1COMBATCONVERGENCE1

    label E1COMBATCONVERGENCE1:
    "As I boost forward, Shou moves back to keep the distance between us. He shoots again, but his aim is not accurate and I weave away. With my gun in hand, I take aim…"

    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E1C1E1_L2")
    menu:
        "Shoot!":
            jump E1C1E1_W2

        "Fire!":
            jump E1C1E1_W2

        "Miss…":
            $ E1C1E1_C += 1
            jump E1C1E1_L2


    label E1C1E1_L2:
        $ renpy.hide_screen ("timer_scr")
        
        
        show shou att with Dissolve(.45):
            xoffset 0
        play sound "audio/sfx/GEAR Combat/SMG.ogg"
        $renpy.pause(.35)
        
        play sound2 hitSound
        
        show mc blo at bl, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -75
                
                
        "My hand wavers and Shou easily dodges the shot, then fires back. I dash out of the way, but I'm not fast enough and I wince as I take another hit."
        if E1C1E1_C == 1:
            "My shield sucks up energy as it absorbs each attack, and I'm in dangerously low territory now. I don't think I can withstand another hit like that."
            jump E1COMBATCONVERGENCE2
        if E1C1E1_C == 2:
        
            play sound Depowered
            show mc mech with dissolve:
                xoffset -200
            
            "My shields disappear as my GEAR goes dark."
            jump E1D3S4_ShouPracticeComplete

    label E1C1E1_W2:
        $ renpy.hide_screen ("timer_scr")
        

        show mc attR with Dissolve(.45)
        play sound rangeSound
        play sound2 hitSound
        
        show shou blo at br, Shake(None, 1, dist=20):
        
        
        "My aim is true and Shou's shield shimmers as it absorbs the shot. Judging by how deep of a shimmer, it looks like he took a significant amount of damage!"
        jump E1COMBATCONVERGENCE2


    label E1COMBATCONVERGENCE2:
    "Since Shou likes using ranged weapons, I better close the distance and force him into a melee battle! I boost forward..."


    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E1C1E1_L3")
    menu:
        "Miss…":
            $ E1C1E1_C += 1
            jump E1C1E1_L3

        "Slash!":
            jump E1C1E1_W3

        "Strike!":
            jump E1C1E1_W3

        "Trip…":
            $ E1C1E1_C += 1
            jump E1C1E1_L3

        "Attack!":
            jump E1C1E1_W3

    label E1C1E1_W3:
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
        
        show shou mech at br, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset 150
                
 
        "I switch to my sword mid-boost and swing the blade in a high arc. Shou tries to block with his guns and my sword lands on them with a loud crack."
        "We struggle in a battle of wills, and sweat beads down my face. A loud roar escapes my lips as I channel my strength into my attack… and break through Shou's defense!"
        
        play sound Depowered
        
        "As my sword falls through, Shou's GEAR goes dark."
        $ E1C1_WON = 1
        jump E1D3S4_ShouPracticeComplete

    label E1C1E1_L3:
        $ renpy.hide_screen ("timer_scr")
        
        
        
        show shou att with Dissolve(.45):
            xoffset 0
        play sound "audio/sfx/GEAR Combat/SMG.ogg"
        $renpy.pause(.35)
        
        play sound2 hitSound
        
        show mc ready at bl, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -75
        
        
        "I switch to my sword mid-boost and swing the blade in a high arc, but Shou fires at me as soon as I start to move. With my defenses down, I'm unprepared to block his shots and I take another hit to my shield!"
        "My dashboard flashes in warning, but I try to ignore it and keep a clear head. When I'm within striking range of Shou, my sword flies to his side and connects with his shield."
        
        play sound Depowered
        
        "He parries with a close-range shot which I'm unable to block, and I'm ultimately depowered."
        jump E1D3S4_ShouPracticeComplete







 
    
    
    label E1D3S4_ShouPracticeComplete:
        play sound "audio/sfx/GEAR/GEAR Virtual Training Simulator.ogg"
        $renpy.pause(2.0)
        $ renpy.hide_screen ("battle_screen")
        $ practiceScore = survived
        scene black with fade
        stop music fadeout 3
        play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
        $renpy.pause(1)
        play ambient "audio/ambience/Hangar.ogg" fadein 1
        "With the match over, I shut down my GEAR and get back on the ground."
        play sound "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
        $renpy.pause(2.5)
        scene bg campus hangar day with fade
        play sound "audio/sfx/GEAR/GEAR Elevator.ogg"
        $renpy.pause(2.5)
        "After a few minutes, Shou appears."
        show shou neu at cc with dissolve
        
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
    if (E1D2S11_JoinedTheTeam == 1):
        if E1C1_WON == 0:
            pf "So, about that match--"
            show shou mis at cc with dissolve
            voice "audio/voice/E1/D3/S4/Shou/39.ogg"
            ss "It's all good, man. I'm sure you've been busy with the whole moving thing and all."
            pf "Yeah, I'll have to be more focused for the next matches."
            show shou smi at cc
            "Shou nods."
    
        else:
            show shou hap at cc with dissolve
            show note:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Shou/46.ogg"
            ss "Not bad! I knew I made a good choice with you. I've got a sixth sense for these things."
            pf "Heh, thanks. You're not so bad yourself."
    
    if (E1D2S11_JoinedTheTeam == 0):
        if E1C1_WON == 0:
            pf "Well then."
            show shou mis at cc with dissolve
            voice "audio/voice/E1/D3/S4/Shou/40.ogg"
            ss "I think you just need to get into the swing of things."
            pf "Yeah, probably. At least now that I know what to expect, I'll be able to handle myself better."
            show shou smi at cc
            "Shou nods."
    
        else:
            show shou hap at cc with dissolve
            show note:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Shou/21.ogg"
            ss "Not bad! You could definitely hold your own for the qualifiers."
            pf "Thanks."
    
        show shou mis at cc
        voice "audio/voice/E1/D3/S4/Shou/22.ogg"
        ss "How did team hunting go?"
    
        if (E1S2D10_AskedOtherTeams == 1):
            pf "Not as well as I expected."
            show shou sad at cc
            voice "audio/voice/E1/D3/S4/Shou/23.ogg"
            ss "Bummer. Most teams come together over the summer so they're well prepared for the qualifier."
            pf "Yeah, I think you mentioned that last time. Still, I thought there'd be either more new people who hadn't found a team, or more teams with missing members."
            show shou mis at cc
            voice "audio/voice/E1/D3/S4/Shou/24.ogg"
            ss "Well, my offer still stands…"
    
        if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
            pf "I actually haven't gotten a chance to talk to the other pilots yet."
            show shou thi at cc with dissolve
            voice "audio/voice/E1/D3/S4/Shou/25.ogg"
            ss "Ah, well, look, I know things with Kaori didn't exactly go smoothly, but the offer to join our team is still open."
            pf "I'm pretty sure Kaori would have a heart attack if she found out I joined."
            show shou smi at cc
            voice "audio/voice/E1/D3/S4/Shou/48.ogg"
            ss "Kaori will understand that if she wants to participate in the qualifiers, you'll have to join. You joining benefits us as much as it benefits you."
    
        "I don't have any other choice and the qualifier is tomorrow."
        pf "Sure, I'll join."
        show shou hap at cc with dissolve
        "Shou breaks into his usual grin."
        show note:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S4/Shou/26.ogg"
        ss "Awesome! Trust me, this is going to be good!"
    
        if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
            pf "So you're sure Kaori will be okay with this?"
            show shou smi at cc with dissolve
            "He smiles reassuringly."
            voice "audio/voice/E1/D3/S4/Shou/27.ogg"
            ss "Don't worry, I'll talk to her."
            
    show shou cur at cc
    voice "audio/voice/E1/D3/S4/Shou/28.ogg"
    ss "Anyway, we'll want to meet up tomorrow before the qualifiers to practice, so what's your number?"
    show shou smi at cc
    "We quickly exchange numbers."
    pf "So… I guess I should go and get some stuff done."
    show shou hap at cc
    voice "audio/voice/E1/D3/S4/Shou/47.ogg"
    ss "Yeah, me too. Well, I'll see you later then!"
    
    menu:
        "Wait, let's play another match!":
            pf "Shou, wait!"
            show shou cur at cc with dissolve
            show question:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            "He pauses, and looks at me curiously."
            pf "How about a rematch?"
            show shou mis at cc with dissolve
            "He grins."
            voice "audio/voice/E1/D3/S4/Shou/29.ogg"
            ss "Hell yeah! Same rules as before?"
            pf "Let's do it."
            hide shou with dissolve
            "He runs back to his GEAR and I get back into mine."
            scene black with fade
            #fade to black
            $renpy.pause(2.5)
            "After practicing for a while it was time to head our separate ways."
            stop music fadeout 3
            # fill in whatever needs to be here for S8
            $ E1D3S4_PlayedAnotherWithShou = 1
            jump E1D3S8
    
        "I need to study.":
            stop music fadeout 3
            pf "Bye."
            hide shou with dissolve
            "As I watch him leave, I decide to head to the library."
            scene black with fade
            stop ambient fadeout 3
            $renpy.pause(1)
            scene bg campus library day with fade
            play ambient "audio/ambience/Ace Academy Library.ogg" fadein 1
            "I've only gotten assignments for one class so far, but I don't want to fall behind. {w}Plus, if I get my work done now, then I can do whatever I want over the weekend."
            jump E1D3S6
    
        "The pilot's lounge always has something going on.":
            pf "Bye."
            hide shou with dissolve
            stop ambient fadeout 3
            scene bg campus lounge day with fade
            play ambient "audio/ambience/Pilot Lounge.ogg" fadein 1
            play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
            "I head back towards the pilot's lounge. So far, every time I've passed through the lounge it has been full of students. {w}I'm sure I'll either meet someone cool or find something interesting to do there."
            $ E1D3S4_WentToThePilotsLounge = 1
            jump E1D3S5
