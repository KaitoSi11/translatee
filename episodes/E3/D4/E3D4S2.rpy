#
label E3D4S2:
    
    
    $ E3D4S2_Duelist = 0
    $ E3D4S2_Takedown = 0
    $ E3D4S2_Interfered = 0
    $ E3D4S2_Waited = 0
    
    # arena ambient?
    scene bg campus arena day with fade
    
    "We enter the arena from one side while Onna-Bugeisha enters from the other."
    
    play music "audio/music/Fight Song 1 (GAME VERSION).ogg" fadein 3
    voice "audio/voice/E3/D4/S2/an/1.ogg"
    an "Welcome everyone! Are you all ready for another fantastic match?!"
    
    "The crowd erupts into a loud cheer."
    voice "audio/voice/E3/D4/S2/an/2.ogg"
    an "Good, because we have an amazing one lined up for you! Onna-Bugeisha versus ACE-2049-11!"
    
    show bg battleground day with dissolve:
        alpha 1
        xzoom 1
        yzoom 1
        yoffset 25
        xoffset -225
            
    show bugeisha neu at tl:
        xzoom .8
        yzoom .8
    show bugeisha2 neu at tr:
        xzoom .8
        yzoom .8
    show onna neu at mm
    show bugeisha3 neu at br
    with dissolve
    
    "Everyone's comms are open as we await the sound-off. Mei's team get into position and wait with relaxed confidence."
    show bg battleground day:
        parallel:
            easein 3.0 alpha 1.0
        parallel:
            easein 3.0 xoffset 225
            
    show bugeisha neu at tl:
        xzoom .8
        yzoom .8
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset 1500
    show bugeisha2 neu at tr:
        xzoom .8
        yzoom .8
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset 1500
    show onna neu at mm:
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset 1300
    show bugeisha3 neu at br:
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset 1300
            
    $renpy.pause(2.5)
    show shou mech at tr with dissolve:
        xzoom -.8
        yzoom .8
            
    show mayu mech at tl with dissolve:
        xzoom -.8
        yzoom .8
            
    show kaori mech at mm with dissolve:
        xzoom -1
            
    show mc mech at bl with dissolve:
        xzoom -1
    
    "As we also get into formation, the tension I felt from before intensifies. This no longer feels as {i}friendly{/i} of a match as I thought it'd be."
    
    # sfx?
    "As soon as the sound-off blares, Mei's team dashes straight towards us. A faint shimmer surrounding their GEAR reveals a hefty frontal shield."
    voice "audio/voice/E3/D4/S2/kaori/e3d4_Kao_21.ogg"
    ki "Mayu!"
    show mayu att with dissolve
    voice "audio/voice/E3/D4/S2/mayu/Mayu-08.ogg"
    ma "On it."
    
    "Mayu raises her gun and takes aim while the three of us position to protect her."
    play sound "audio/sfx/GEAR Combat/Sniper.ogg"
    "A heavy round flies into one of the GEARs in the distance. {w}Although the shot connects, it disperses into a hexagon of shimmers."
    # emote? panic
    voice "audio/voice/E3/D4/S2/shou/15.ogg"
    ss "What?!"
    show mayu mech with dissolve
    voice "audio/voice/E3/D4/S2/mayu/Mayu-09.ogg"
    ma "Their shields! They're tailored to deal with rail rounds. I need the shield to be weakened so that my shot can penetrate and force an immediate depower."
    voice "audio/voice/E3/D4/S2/kaori/e3d4_Kao_22.ogg"
    ki "Affirmative. I'll stay back and protect. You two go aggressive and focus on knocking out their shield."
    show mc attR with dissolve
    pf "Let's go."
    show shou att with dissolve
    voice "audio/voice/E3/D4/S2/shou/16.ogg"
    ss "Roger that! Switching to EMP rounds now."
    play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
    show mc attR at bl, Shake(None, 1, dist=20) behind kaori:
        xzoom -1
        parallel:
            easeout .5 alpha 1.0
        parallel:
            easeout .5 xoffset 1750
    
    $renpy.pause(1)
    play sound "audio/sfx/GEAR Combat/Rifle.ogg"
    $renpy.pause(0.5)
    play sound2 "audio/sfx/GEAR Combat/SMG.ogg"
    scene black with fade
    scene bg campus arena day with fade
    "Shou and I boost forward, spraying a hail of energy rounds."
    
    "The enemy team takes evasive maneuvers. Mei breaks away while the other three continue racing towards Mayu."
    show bg battleground day with dissolve:
        alpha 1
        xzoom 1
        yzoom 1
        yoffset 25
        xoffset 225
        
    show mayu att at tl:
        xzoom -.8
        yzoom .8
    show kaori mech at mm:
        xzoom -1
    with dissolve
    $renpy.pause(0.5)
    show bugeisha att at tr with dissolve:
        xoffset 400
        xzoom .75
        yzoom .75
        
    play sound "audio/sfx/GEAR Combat/Sniper.ogg"
    $renpy.pause(1)
    play sound2 "audio/sfx/GEAR Combat/Hit.ogg"
    show bugeisha att at tr, Shake(None, .25, dist=15) with Dissolve(.25)
    show bugeisha neu at tr, Shake(None, .25, dist=15) with Dissolve(.25)
    play sound "audio/sfx/GEAR Combat/Depower.ogg"
    $renpy.pause(0.5)
    hide bugeisha with dissolve
    "The closest enemy GEAR takes the brunt of the damage, and its front barrier drops. Mayu takes advantage of the vulnerability and aims a shot at the GEAR, instantly depowering it."
    voice "audio/voice/E3/D4/S2/shou/17.ogg"
    ss "Nice! One down."
    voice "audio/voice/E3/D4/S2/mayu/Mayu-10.ogg"
    ma "I have two of them approaching me. Kaori--"
    play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
    show kaori att at mm, Shake(None, 1, dist=20):
        xzoom -1
        parallel:
            easeout .5 alpha 1.0
        parallel:
            easeout .5 xoffset 1750
    show mayu mech with dissolve
    voice "audio/voice/E3/D4/S2/mayu/Mayu-11.ogg"
    ma "Kaori!"
    # CG? 
    $ persistent.gpix[9][0] = 1
    show cg GEAR mei clash with dissolve:
        xalign 0.5
        yalign 0.5
        xzoom 1
        yzoom 1
    "Aura has already left her position and sprints towards Mei."
    voice "audio/voice/E3/D4/S2/shou/19.ogg"
    ss "What are you doing?! You have to protect Mayu!"
    voice "audio/voice/E3/D4/S2/kaori/e3d4_Kao_23.ogg"
    ki "I am! I'm taking out Mei so she can't attack!"
    voice "audio/voice/E3/D4/S2/mayu/Mayu-12.ogg"
    ma "That wasn't the plan!"
    voice "audio/voice/E3/D4/S2/kaori/e3d4_Kao_24.ogg"
    ki "You two cover her."
    voice "audio/voice/E3/D4/S2/shou/20.ogg"
    ss "We're not in position to-"
    voice "audio/voice/E3/D4/S2/mayu/Mayu-13.ogg"
    ma "Ack!"
    voice "audio/voice/E3/D4/S2/shou/21.ogg"
    ss "She's already engaged, let's go!"
    
    scene bg battleground day with dissolve:
        alpha 1
        xzoom 1
        yzoom 1
        yoffset 25
        xoffset 225
        
    show shou att at tl:
        xzoom -.8
        yzoom .8
    show mc ready at bl:
        xzoom -1
    with dissolve
    "Shou and I boost back to Mayu... but it's too late."
    voice "audio/voice/E3/D4/S2/mayu/Mayu-14.ogg"
    ma "I've been depowered."
    "Her voice is lethally calm. This can't be good."
    show bugeisha neu at tr:
        xzoom .8
        yzoom .8
    show bugeisha2 att at br
    with dissolve
    "The two enemy GEARs shift to Shou and I."
    voice "audio/voice/E3/D4/S2/shou/22.ogg"
    ss "Two on two, but not much distance. Play this out carefully."
    "For once, Shou is serious."
    scene black with fade

    #Match against 2 AIs.
    
    $ E3D4S2_Duelist = 1
    scene bg battleground day with fade
    show mc ready at bl with dissolve:
        xzoom -1
    show bugeisha att at br with dissolve
    
    
    
    #$ comradeKaori = 0
    #$ comradeMayu = 0
    #$ comradeShou = 0
    
    #$ context = "E3D4S2_1st"
    #$ enemy = "bugeisha"
    #$ mode = "default"
    #$ survived = 0
    #$ score = 0
    
    #$ mcEnergyMax = 200
    #$ mcEnergy = 200
    
    #$ enemyHPMax = 200
    #$ enemyHP = 200
        
    #show screen battle_screen
    #$renpy.pause(1)
    #jump qte_game
    #label E3D4S2_1st:
    #    $ renpy.hide_screen ("battle_screen")
    #    if mcEnergy > 0:
    #        $ context = "E3D4S2_2nd"
    #        play sound "audio/sfx/GEAR Combat/Depower.ogg"
    #        hide bugeisha with dissolve
    #        $renpy.pause(1)
    #        show mc mech at bl with dissolve:
    #            xoffset 0
    #            xzoom -1
    #        $ enemyHP = 200
    #        show bugeisha neu at br with dissolve:
    #            xoffset 0
    #            yoffset 0
    #            xzoom 1
    #            yzoom 1
    #        show mc ready with dissolve
    #        show screen battle_screen
    #        $renpy.pause(1)
    #        jump qte_game
    #        
    #        label E3D4S2_2nd:
    #            $ renpy.hide_screen ("battle_screen")
    #            if mcEnergy >= 0:
    #                $ E3D4S2_Duelist = 1
    #            else:
    #                $ E3D4S2_Duelist = 0
    #            
    #    else:
    #        $ E3D4S2_Duelist = 0
    
    
    
    
        
        
    "The GEARs split their focus and one of them charges towards me me while the other boosts towards Shou. I boost away and take aim..."

    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E3C1E1_L1")
    menu:
        "Freeze...":
            $ E3C1E1_C += 1
            jump E3C1E1_L1

        "Hit!":
            jump E3C1E1_W1

        "Fire!":
            jump E3C1E1_W1

        "Fail...":
            $ E3C1E1_C += 1
            jump E3C1E1_L1
                
        "Miss...":
            $ E3C1E1_C += 1
            jump E3C1E1_L1


    label E3C1E1_W1:
        $ renpy.hide_screen ("timer_scr")

        show mc attR with Dissolve(.45)
        play sound rangeSound
        play sound2 hitSound
        
        show bugeisha blo at br, Shake(None, 1, dist=20):
        
        
        "My aim is true and a blast of energy rounds collides with her GEAR. She stumbles back from the hit while I create more distance between us."
        #"Another hit like that and she'll be done for!"
        jump E3CONVERGENCE_1

    label E3C1E1_L1:
        $ renpy.hide_screen ("timer_scr")
        
        show mc attR with Dissolve(.45)
        play sound rangeSound
        $renpy.pause(.25)
        
        play sound2 dodSound
        $renpy.pause(.25)
        show bugeisha att at br, Shake(None, 1, dist=20):
            xoffset 0
            parallel:
                easeout .1 alpha 1.0
            parallel:
                easeout .1 xoffset -250
        $renpy.pause(.1)

        play sound meleeSound
        show bugeisha att at br with Dissolve(.2):
            xoffset -400

        show white with Dissolve(0.15):
        play sound2 hitSound
        hide white with Dissolve(0.25)
        
        show mc blo at bl, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -150
        
        "I react too slowly and my shot flies off the mark. She slashes me and I end up taking the hit. My dashboard flashes warnings as my shield shimmers. That was a stronger hit than expected. I can't take another one of those!"
        jump E3CONVERGENCE_1
        
    label E3CONVERGENCE_1:
    play sound2 dodSound
    show mc dod at bl, Shake(None, .25, dist=15):
        xoffset 0
    show bugeisha neu at br:
        xoffset 0
    with dissolve
        
    "Before she can strike again, I move away to create more distance between us."
    "I raise my guns for another shot…"

    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E3C1E1_L2")
    menu:
        "Shoot!":
            jump E3C1E1_W2

        "Miss...":
            $ E3C1E1_C += 1
            jump E3C1E1_L2

        "Slow...":
            $ E3C1E1_C += 1
            jump E3C1E1_L2

        "Fail...":
            $ E3C1E1_C += 1
            jump E3C1E1_L2

        "Fire!":
            jump E3C1E1_W2







    label E3C1E1_L2:
        $ renpy.hide_screen ("timer_scr")
        "She's too fast for me and is already on my heels before I can get the shot in. She swings her sword and her attack connects."

        if E3C1E1_C == 1:
        
        
            show bugeisha att at br, Shake(None, 1, dist=20):
                xoffset 0
                parallel:
                    easeout .1 alpha 1.0
                parallel:
                    easeout .1 xoffset -250
            $renpy.pause(.1)

            play sound meleeSound
            show bugeisha att at br with Dissolve(.2):
                xoffset -400

            show white with Dissolve(0.15):
            play sound2 hitSound
            hide white with Dissolve(0.25)
            
            show mc blo at bl, Shake(None, .5, dist=20):
                parallel:
                    easeout .3 alpha 1.0
                parallel:
                    easeout .3 xoffset -150
                
                
            "My shield shimmers as it absorbs the blow. I can't take another hit like that!"
            "She's fast, so I have to be faster."
            
            
            play sound2 dodSound
            show mc dod at bl, Shake(None, .25, dist=15):
                xoffset 0
            show bugeisha neu at br:
                xoffset 0
            with dissolve
            
            "Before she can attack again, I boost back and weave around the arena."
            jump E3CONVERGENCE_2
            
        if E3C1E1_C == 2:
        
        
            show bugeisha att at br, Shake(None, 1, dist=20):
                xoffset 0
                parallel:
                    easeout .1 alpha 1.0
                parallel:
                    easeout .1 xoffset -250
            $renpy.pause(.1)

            play sound meleeSound
            show bugeisha att at br with Dissolve(.2):
                xoffset -400

            show white with Dissolve(0.15):
            play sound2 hitSound
            hide white with Dissolve(0.25)
            
            show mc mech at bl, Shake(None, .5, dist=20):
                parallel:
                    easeout .3 alpha 1.0
                parallel:
                    easeout .3 xoffset -150
                    
            $renpy.pause(1.0)
            play sound Depowered
            $renpy.pause(.5)
            "Her attack connects and my shield disappears as my GEAR is depowered."
            
            jump E3CombatMasterConvDEPOWER

    label E3C1E1_W2:
        $ renpy.hide_screen ("timer_scr")
        
        show mc attR with Dissolve(.45)
        play sound rangeSound
        play sound2 hitSound
        
        show bugeisha blo at br, Shake(None, 1, dist=20):
        
        "She tries dodge but is too slow and my shots pellet her shield. She's pushed back from the force of the blow, but once she gets her bearings, she boosts right back towards me."
        
        play sound2 dodSound
        show mc dod at bl, Shake(None, .25, dist=15):
            xoffset 0
        show bugeisha att at br:
            xoffset 0
        with dissolve
        
        "As she approaches, I boost away from her and weave around the arena, forcing her to chase me." 
        jump E3CONVERGENCE_2


    label E3CONVERGENCE_2:
    "I steady my aim…"


    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E3C1E1_L3")
    menu:
        "Fire!":
            jump E3C1E1_W3

        "Target!":
            jump E3C1E1_W3

        "Miss…":
            $ E3C1E1_C += 1
            jump E3C1E1_L3

        "Shoot!":
            jump E3C1E1_W3

        "Fail…":
            $ E3C1E1_C += 1
            jump E3C1E1_L3

    label E3C1E1_W3:
        $ renpy.hide_screen ("timer_scr")
        
        show mc attR with Dissolve(.45)
        play sound rangeSound
        play sound2 hitSound
        
        show bugeisha neu at br, Shake(None, 1, dist=20):
        
        $renpy.pause(1.0)
        play sound Depowered
        $renpy.pause(.5)
        
        hide bugeisha with dissolve
        
        "She's too slow to dodge and my shot strikes right through her shield. Her GEAR can't support the hit and she's depowered."
        "I look over at Shou just in time to see an enemy GEAR strike!"

            
        pf "Watch out!"

        play sound2 dodSound
        show mc ready at bl, Shake(None, .5, dist=10) with Dissolve(.45):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 650
                
        #$renpy.pause(.10)
        play sound rangeSound
        show mc attR at bl, Shake(None, .5, dist=10) with Dissolve(.45)
        
        
        "I boost closer and shoot again."
        play sound2 hitSound
        "The round connects with the GEAR just as her attack connects with Shou."
        
        play sound Depowered
        $renpy.pause(.15)
        play sound2 Depowered
        
        "Shou blocks just a second too late and he's depowered, but because she wasn't expecting my attack, she left herself vulnerable and is also depowered."
        jump E3CombatMasterConv

    label E3C1E1_L3:
        $ renpy.hide_screen ("timer_scr")
        
        show mc attR with Dissolve(.45)
        play sound rangeSound
        $renpy.pause(.25)
        
        play sound2 dodSound
        $renpy.pause(.25)
        show bugeisha att at br, Shake(None, 1, dist=20):
            xoffset 0
            parallel:
                easeout .1 alpha 1.0
            parallel:
                easeout .1 xoffset -250
        $renpy.pause(.1)

        play sound meleeSound
        show bugeisha att at br with Dissolve(.2):
            xoffset -400

            
        "My shots miss her as she dodges out of the way. Damn, she's getting too close!"
        
        play sound2 dodSound
        show mc dod at bl, Shake(None, .25, dist=15):
            xoffset 0
        show bugeisha neu at br:
            xoffset 0
        with dissolve
            
        "She swings at me, but misses as I boost away."
        if E3C1E1_C == 1:
            "Her GEAR starts to wane as she continues to chase me around the arena. Her energy levels must be weakening and she's trying to conserve energy for another attack… but I won't give her that opportunity!"
            
            
                
            show mc attR with Dissolve(.45)
            play sound rangeSound
            play sound2 hitSound
            
            show bugeisha neu at br, Shake(None, 1, dist=20):
            
            $renpy.pause(1.0)
            play sound Depowered
            $renpy.pause(.5)
            
            "Spotting an opening, I quickly take the shot and the round pierces through her shield, instantly depowering her."
            jump E3CombatMasterConv

        if E3C1E1_C == 2:
        
            show bugeisha att at br, Shake(None, 1, dist=20):
                xoffset 0
                parallel:
                    easeout .1 alpha 1.0
                parallel:
                    easeout .1 xoffset -250
            $renpy.pause(.1)

            play sound meleeSound
            show bugeisha att at br with Dissolve(.2):
                xoffset -400

            show white with Dissolve(0.15):
            play sound2 hitSound
            hide white with Dissolve(0.25)
            
            show mc mech at bl, Shake(None, .5, dist=20):
                parallel:
                    easeout .3 alpha 1.0
                parallel:
                    easeout .3 xoffset -150
                    
            $renpy.pause(1.0)
            play sound Depowered
            $renpy.pause(.5)
            
            "As I try to focus on her again, she gets in close and slashes my side. Her attack connects and she follows through with an overhead slash. Eagle becomes depowered."
            jump E3CombatMasterConvDEPOWER

        
    label E3CombatMasterConvDEPOWER:
        hide mc with dissolve
        "Once I'm decommissioned, the enemy GEAR refocuses on Shou, but Shou is ready for her."
        
        play sound "audio/sfx/GEAR Combat/SMG.ogg"
        $renpy.pause(.15)
        play sound2 "audio/sfx/GEAR Combat/SMG.ogg"
        
        $renpy.pause(.25)
        
        play sound3 hitSound
        play sound2 Depowered
        
        "Before she can attack she's pelted with two energy rounds. They both crush through her shield instantly depowering her."
        hide bugeisha with dissolve
        "Glancing behind Shou, I see the second enemy GEAR is already darkened from being depowered."
        $ E3D4S2_Duelist = 0
        jump E3CombatMasterConv
    
    
  
    
    label E3CombatMasterConv:
    if E3D4S2_Duelist == 1:
        #play sound "audio/sfx/GEAR Combat/Depower.ogg"
        hide bugeisha with dissolve
        #show mc mech at bl with dissolve:
        #    xoffset 0
        #    xzoom -1
        "Mei is the only remaining enemy GEAR."
        voice "audio/voice/E3/D4/S2/shou/23.ogg"
        ss "One more GEAR and the match is ours!"
        pf "On it."
        play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
        show mc ready at bl, Shake(None, 1, dist=20):
            xzoom -1
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 1750
        "I boost towards Kaori and Mei who are locked in a duel."
    
    
    
    else:
        #play sound "audio/sfx/GEAR Combat/Depower.ogg"
        hide bugeisha
        hide mc
        with dissolve
        #play sound2 "audio/sfx/GEAR Combat/Depower.ogg"
        "We take out both GEARs, but I'm depowered during the engagement."
        show shou att at mm with dissolve:
            xzoom -1
            yzoom 1
            xoffset -600
        voice "audio/voice/E3/D4/S2/shou/24.ogg"
        ss "We pulled that off."
        pf "No time to relax yet. We still have one more GEAR before the match is over."
        voice "audio/voice/E3/D4/S2/shou/25.ogg"
        ss "Right! I got this."
        play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
        show shou att at mm, Shake(None, 1, dist=20):
            xzoom -1
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 1750
        "Emerald boosts towards Kaori and Mei who are locked in a duel."
        
        
        
    show cg GEAR mei clash with dissolve:
        xalign 0.5
        yalign 0.5
        xzoom 1
        yzoom 1
    voice "audio/voice/E3/D4/S2/kaori/e3d4_Kao_25.ogg"
    ki "Hiyyaahhh!"
    "Aura strikes with vigor, but is parried. Mei retaliates with a wide swing, which Kaori barely manages to block."
    
    if E3D4S2_Duelist == 1:
        pf "I'm here."
    
    else:
        voice "audio/voice/E3/D4/S2/shou/26.ogg"
        ss "Alright, let's take this win home!"
        
    ### VOICE - originally read "No! Don't interfere!" but voice only gave 2nd part
    voice "audio/voice/E3/D4/S2/kaori/e3d4_Kao_26.ogg"
    ki "Don't interfere!"
    pf "Huh?"
    voice "audio/voice/E3/D4/S2/shou/27.ogg"
    ss "What...?"
    ma "!"
    pf "What do you mean \"don't interfere\"?"
    voice "audio/voice/E3/D4/S2/kaori/e3d4_Kao_27.ogg"
    ki "Let me handle this!"
    voice "audio/voice/E3/D4/S2/mayu/Mayu-15.ogg"
    ma "Kaori! This isn't a simulation, this is a real match!"
    voice "audio/voice/E3/D4/S2/shou/28.ogg"
    ss "Yeah, what you're saying--"
    voice "audio/voice/E3/D4/S2/kaori/e3d4_Kao_28.ogg"
    ki "Mei is going down in a one on one. She won't have any excuses this way!"
    voice "audio/voice/E3/D4/S2/mayu/Mayu-16.ogg"
    ma "This is a team match. You can't put a win in jeopardy because you want to make this personal!"
    
    
    if E3D4S2_Duelist == 1:
        "What should I do?"
    
        menu:
            "Don't interfere.":
                scene bg battleground day with fade
                show onna att at tl with dissolve:
                    xoffset 400
                    xzoom -0.75
                    yzoom 0.75
                show kaori att at tr behind onna with dissolve:
                    xoffset 350
                    xzoom 0.75
                    yzoom 0.75
                show mc mech at bl with dissolve:
                    xzoom -1
                "I cut Eagle's engines."
                voice "audio/voice/E3/D4/S2/mayu/Mayu-17.ogg"
                ma "What are you doing?!"
                voice "audio/voice/E3/D4/S2/shou/29.ogg"
                ss "..."
                "Mei notices my engine is off, and she lunges towards Eagle!"
                play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
                show onna att at mm with dissolve:
                    xoffset 0
                    xzoom 1
                    yzoom 1
    
                #QTE
                $ qtebase = 3
                $ qtetotal = qteath + qtebase
                $ t_var = qtetotal
                show screen timer_scr(place="E3D4S2_Still")
                
                menu:
                    "Take it...":
                        label E3D4S2_Still:
                            $ renpy.hide_screen ("timer_scr")
                            "I keep Eagle still."
                            $ E3D4S2_Takedown = 0
    
                    "Defend!":
                        $ renpy.hide_screen ("timer_scr")
                        $ E3D4S2_Waited = 1
                        jump E3D4S2_Mei
    
            "Engage Mei.":
                $ E3D4S2_Interfered = 1
                scene bg battleground day with fade
                show onna att at tl with dissolve:
                    xoffset 400
                    xzoom -0.75
                    yzoom 0.75
                show kaori att at tr behind onna with dissolve:
                    xoffset 250
                    xzoom 0.75
                    yzoom 0.75
                show mc mech at bl with dissolve:
                    xzoom -1
                    
                # exclamation emote on Mei ???
                $renpy.pause(1)
                play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
                show onna att at mm with dissolve:
                    xoffset 0
                    xzoom 1
                    yzoom 1
                label E3D4S2_Mei:
                    show mc ready with dissolve
                    "Eagle bursts into action."
                    voice "audio/voice/E3/D4/S2/kaori/e3d4_Kao_29.ogg"
                    ki "What are you doing?!"
                    pf "I'm not just going to sit here and let her take me out!"

                    #QTE
                    $ qtebase = 3
                    $ qtetotal = qteath + qtebase
                    $ t_var = qtetotal
                    show screen timer_scr(place="E3D4S2_Fail")
                    
                    menu:
                        "Parry!":
                            $ renpy.hide_screen ("timer_scr")
                            $ E3D4S2_Takedown = 1
                        "Miss...":
                            $ renpy.hide_screen ("timer_scr")
                            $ E3D4S2_Takedown = 0
                        "Strike back!":
                            $ renpy.hide_screen ("timer_scr")
                            $ E3D4S2_Takedown = 1
                        "Fail...":
                            label E3D4S2_Fail:
                                $ renpy.hide_screen ("timer_scr")
                                $ E3D4S2_Takedown = 0
                        "Juked...":
                            $ renpy.hide_screen ("timer_scr")
                            $ E3D4S2_Takedown = 0
    
    
        if E3D4S2_Takedown == 0:
            scene white with fade
            "I barely register Aura chasing after us. All I can see is Mei's blade, ignited with energy. Her shield shimmers as it fades away."
            play sound "audio/sfx/GEAR Combat/Sword Single.ogg"
            "{i}{b}Swoosh!{/b}{/i}"
            play sound "audio/sfx/GEAR Combat/Hit.ogg"
            $renpy.pause(0.5)
            play sound "audio/sfx/GEAR Combat/Depower.ogg"
            scene black with fade
            "In one clean swing, I am depowered."
            play sound "audio/sfx/GEAR Combat/Depower.ogg"
            "..."
            "Wait, Mei is depowered too?"
            scene bg battleground day with fade
            show onna att at mm
            show kaori att at tr behind onna:
                xzoom 0.75
                yzoom 0.75
            show mc mech at bl:
                xzoom -1
            with dissolve
            "Aura is still in her final stance, her blade extended. She must have hit Mei at the same time Mei hit me."
            show onna neu with dissolve
            voice "audio/voice/E3/D4/S2/shou/30.ogg"
            ss "She summoned all her remaining power into her final attack so she could go for a direct GEAR depower."
            voice "audio/voice/E3/D4/S2/mayu/Mayu-18.ogg"
            ma "Mei knew she wouldn't win a two on one. She went for the safest points."
            voice "audio/voice/E3/D4/S2/mayu/Mayu-19.ogg"
            ma "Which was the {i}smartest{/i} play for their overall team."
            "That wasn't subtle at all."
            show kaori mech with dissolve
            "Aura's blade lowers, but Kaori doesn't speak. Shou and Mayu fall silent too."
        
        else:
            show mc attM with dissolve
            play sound "audio/sfx/GEAR Combat/Sword Single.ogg"
            "Anticipating her swing, I sidestep using my thrusters and counter attack with my own blade."
            play sound "audio/sfx/GEAR Combat/Hit.ogg"
            show onna att at mm, Shake(None, .25, dist=15) with Dissolve(.25)
            play sound "audio/sfx/GEAR Combat/Depower.ogg"
            show onna neu at mm, Shake(None, .25, dist=15) with Dissolve(.25)
            $renpy.pause(0.5)
            "With no shield activated on her back arc, my swing completely depowers her GEAR."
            show kaori mech
            hide onna
            with dissolve
            voice "audio/voice/E3/D4/S2/shou/31.ogg"
            ss "Nice one!"
            show mc mech with dissolve
            "Shou's the only one to speak."
            voice "audio/voice/E3/D4/S2/shou/32.ogg"
            ss "...Guys?"
            show kaori mech with dissolve:
                xzoom -0.75
            "Mayu and Kaori are both silent. Aura sheathes her blade and exits the arena."
    
    else:
        scene bg battleground day with fade
        show onna att at mm with dissolve:
            xoffset -50
            xzoom -1
            yzoom 1
        show kaori att at br behind onna with dissolve:
            xoffset 100
            xzoom 1
            yzoom 1
        show shou mech at tl behind onna with dissolve:
            xoffset -300
            xzoom -0.75
            yzoom 0.75
        "Shou hesitates. Mei takes another swing while Kaori is distracted. Aura stumbles back as she blocks."
        voice "audio/voice/E3/D4/S2/shou/33.ogg"
        ss "I'm assisting!"
        voice "audio/voice/E3/D4/S2/kaori/e3d4_Kao_30.ogg"
        ki "Don't you {i}dare{/i}!"
        show shou att with dissolve
        "Emerald takes position opposite Aura, trapping Mei in between them."
        show kaori mech
        show onna neu
        with dissolve
        "Mei looks at her two possible targets: Kaori with her blade ready and Shou with his guns trained on her."
        voice "audio/voice/E3/D4/S2/kaori/e3d4_Kao_31.ogg"
        ki "Stay out of this, Shou!"
        show onna att
        show kaori att
        with dissolve
        "Mei dashes towards Aura, who is slightly closer than Emerald. As soon as she moves, Emerald lets loose a hail of bullets."
        play sound "audio/sfx/GEAR Combat/SMG.ogg"
        $renpy.pause(0.5)
        play sound "audio/sfx/GEAR Combat/Hit.ogg"
        show onna att at mm, Shake(None, .25, dist=15) with Dissolve(.25)
        play sound "audio/sfx/GEAR Combat/Depower.ogg"
        show onna neu at mm, Shake(None, .25, dist=15) with Dissolve(.25)
        $renpy.pause(0.5)
        "He strikes Mei in the back arc and depowers her before she can even reach Aura."
        show kaori mech with dissolve:
            xzoom 1
        "Aura sheaths her blade and exits the arena."
        
    stop music fadeout 5
    scene bg campus arena day with dissolve
    voice "audio/voice/E3/D4/S2/an/3.ogg"
    an "ACE-2049-11 are the winners! Congratulations!"
    
    "The crowd roars to life, but their excitement doesn't penetrate the friction clouding our team."
    voice "audio/voice/E3/D4/S2/an/4.ogg"
    an "I hate to rush our competing teams, but we have another match in just a few minutes. Please clear the arena!"
    
    "Mei's team heads back to their pre-combat room, as we head to ours."
    
    #Fade into black screen
    stop ambient fadeout 3
    scene black with fade
    
    jump E3D4S3
