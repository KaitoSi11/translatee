#
label E2D5S2:
    
    stop music
    stop ambient
    play ambient "audio/ambience/Desert Maid Cafe.ogg" fadein 5
    scene bg campus cafe day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    
    "I stop to grab a coffee at the campus cafe and sip slowly at the hot liquid."
    "Repairs should be done by now. Time to go meet everyone. {w}I finish the drink and make my way to the Hangar."
    stop ambient fadeout 3
    scene black with fade
    play ambient "audio/ambience/Pilot Lounge.ogg" fadein 3
    scene bg campus lounge day with fade
    
    $ kaoOut = "sUniform"
    $ mayOut = "sUniform"
    $ shoOut = "sUniform"
    $ yuuOut = "sUniform"

    
    show yuuna neu at cc with dissolve
    stop music fadeout 5
    "As promised, Yuuna is waiting for me in front of the Hangar doors."
    play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
    "After a quick greeting, I swipe open the entrance. A different guard from last night sits in front of the doors."
    stop ambient fadeout 3
    scene black with fade
    "He barely glances at us as I lead Yuuna into the Hangar and towards my GEAR."
    play ambient "audio/ambience/Hangar.ogg" fadein 3
    # no music, i think
    scene cg GEAR hangar first with fade
    "Once it comes into view, I freeze. The magnificent beauty that is a restored Eagle nearly brings a tear to my eye. {w}I circle it, but can't detect even a scratch on its armour. If I didn't know any better, I would have never guessed this GEAR had just gone through a battle."
    voice "audio/voice/E2/D5/Yuuna/33.ogg"
    ym "Wow, they really did a good job, didn't they? It doesn't even look like the same robot."
    "Realising what she just said, she quickly backtracks."
    voice "audio/voice/E2/D5/Yuuna/34.ogg"
    ym "Not that your GEAR didn't look good before! I just meant from the battle. It looks better than it did yesterday--"
    "I cut her off with a laugh."
    pf "It's okay, I get it. And I agree."
    "She nods, looking a little relieved."
    stop music fadeout 5
    scene bg campus hangar day with fade
    "Kaori is the first to arrive. She darts straight to her GEAR, and does a complete inspection. {w}Shou and Mayu trickle in after her, then split up and do their own inspection of their robots."
    show yuuna neu at r3 with dissolve:
        xoffset 200
        xzoom -1
    "Yuuna and I wait patiently for them to gather around us."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    show kaori neu at r1 with dissolve
    show shou neu at l1 with dissolve:
        xoffset -100
    show mayu neu at l3 with dissolve:
        xoffset -275
    voice "audio/voice/E2/D5/KI/1.ogg"
    ki "The repairs… you got us a sponsor?"
    pf "I didn't--Yuuna did."
    show yuuna smi at r3
    "At the mention of her name, Yuuna waves to everyone."
    pf "Yuuna, this is Kaori, Shou, and Mayu."
    show kaori smi at r1 with dissolve
    show shou smi at l1 with dissolve
    show mayu smi at l3 with dissolve
    "Each person nods when their name is called."
    pf "Everyone, this is Yuuna, my contact from the SBA. She's the one who somehow snagged us a sponsor in the nick of time."
    show kaori cur at r1
    show question:
        xoffset 890
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D5/KI/2.ogg"
    ki "Who is it?"
    pf "Uh…"
    show kaori neu at r1
    "I have no idea. Luckily, Yuuna helps me out before I make too much of a fool of myself."
    show yuuna neu at r3
    voice "audio/voice/E2/D5/Yuuna/35.ogg"
    ym "It's Dasshu."
    show mayu cur at l3
    show shou cur at l1
    "Shou and Mayu glance at each other in surprise, and Kaori takes a longer look at Yuuna."
    show kaori ske at r1
    voice "audio/voice/E2/D5/KI/3.ogg"
    ki "... You're the Misaki girl, right?"
    stop music fadeout 5
    show yuuna ner at r3
    "Yuuna fidgets slightly, clearly uncomfortable under Kaori's gaze."
    voice "audio/voice/E2/D5/Yuuna/36.ogg"
    ym "Y-Yes."
    show kaori neu at r1
    voice "audio/voice/E2/D5/KI/4.ogg"
    ki "Then Dasshu must be--"
    show yuuna neu at r3
    voice "audio/voice/E2/D5/Yuuna/37.ogg"
    ym "Yes."
    "Kaori just nods."
    show mayu smi at l3
    "Mayu's voice is soft but kind."
    voice "audio/voice/E2/D5/MA/0-01.ogg"
    ma "Thank you so much for what you've done. We really appreciate it."
    show shou smi at l1
    voice "audio/voice/E2/D5/SS/1.ogg"
    ss "Yeah, we understand how difficult this must have been for you."
    "Even Shou is unusually solemn."
    show yuuna smi at r3
    voice "audio/voice/E2/D5/Yuuna/38.ogg"
    ym "It's really no problem at all. I was just doing my job."
    pf "Oh, I didn't know you guys knew Yuuna."
    show shou cur at l1
    voice "audio/voice/E2/D5/SS/2.ogg"
    ss "We don't--"
    show drop:
        xoffset 1375
        yoffset 100
        xzoom .75
        yzoom .75
    "Yuuna laughs nervously."
    show yuuna thi at r3
    show shou neu at l1
    voice "audio/voice/E2/D5/Yuuna/39.ogg"
    ym "Anyway, it was really nice meeting you all, but I need to get going."
    "She doesn't look anyone in the eye and seems impatient to leave."
    pf "You should stay."
    show yuuna ner at r3
    show mayu neu at l3
    voice "audio/voice/E2/D5/Yuuna/40.ogg"
    ym "Thanks, but I've got some errands to run and I'm sure you'll want to test out your GEARs before the match. I'll be there to cheer you guys on, though!"
    hide yuuna with dissolve
    stop music fadeout 5
    "With a hasty goodbye, she rushes out of view."
    
    if MCStory == 3:
        "Hm, I wonder what was about. The team's demeanor changed as soon as they heard our sponsor's name. {w}Maybe there's history between Yuuna and Dasshu?"
    
    else:
        "That was a little strange. {w}I hope we didn't offend her."
        
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
    
    hide shou
    hide kaori
    hide mayu
    with dissolve
    
    show kaori thi at r3:
        xzoom -1
    show mayu neu at l3:
        xoffset 0
    show shou neu at cc:
        xoffset 0
    with dissolve
    voice "audio/voice/E2/D5/KI/5.ogg"
    ki "That's one thing taken care of."
    show kaori neu at r3
    "Kaori looks straight at me."
    voice "audio/voice/E2/D5/KI/6.ogg"
    ki "I hope you know how to activate that override mode thing. We'll plan our strategy around you using it."
    
    menu:
        "I still don't know how to.":
            pf "I tweaked around with the settings, but… {w}it was an anomaly."
            show kaori ske at r3
            voice "audio/voice/E2/D5/KI/7.ogg"
            ki "So you don't know how to initiate it?"
            pf "Exactly."
            show kaori neu at r3
    
        "No foreplay before turning it on?":
            pf "I can't just do that on-demand, y'know. It takes care and attention."
            show shou mis at cc
            voice "audio/voice/E2/D5/SS/3.ogg"
            ss "I never knew you were so needy."
            pf "Low-blow, man."
            show note:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            show shou hap at cc
            show kaori ann at r3
            "We both grin. Kaori looks annoyed."
            show vein:
                xoffset 1175
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D5/KI/8.ogg"
            ki "Can you idiots try and focus for 10 seconds?"
            show shou neu at cc
            pf "Look, I really don't know how to initiate it."
    
        "Not possible.":
            pf "I can't."
            show kaori ske at r3
            voice "audio/voice/E2/D5/KI/9.ogg"
            ki "What do you mean \"I can't\"?"
            pf "It means what you're asking for cannot be done."
            show kaori dis at r3
            "Kaori frowns."
            pf "It's not just a button I can press. I don't know how it activates."
            
    show shou ske at cc
    voice "audio/voice/E2/D5/SS/4.ogg"
    ss "Maybe we can just do what you did last time?"
    show mayu thi at l3
    "Mayu shakes her head."
    show shou neu at cc
    voice "audio/voice/E2/D5/MA/0-02.ogg"
    ma "Last time it activated when his energy level got low. I don't think it would be a good idea to risk that, especially against a non-AI team."
    show storm:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori thi at r3
    "Kaori sighs."
    show mayu neu at l3
    voice "audio/voice/E2/D5/KI/10.ogg"
    ki "Mayu's right."
    show kaori neu at r3
    voice "audio/voice/E2/D5/KI/11.ogg"
    ki "What about your weapons?"
    pf "Yeah about that--"
    
    "A voice interrupts me."
    
    show bg campus hangar day:
        linear .33 xoffset -220
    show kaori:
        linear .33 xoffset -375
    show mayu:
        linear .33 xoffset -375
    show shou:
        linear .33 xoffset -375
    
    $renpy.pause (.5)
    # engineer sprite? guard again, i think
    show guard extra at r3 with dissolve:
        xzoom -1
        xoffset 200
    voice "audio/voice/E2/D5/S2/eng1m/1.ogg"
    eng1m "Hi, are you the owner of this GEAR?"
    "He points to Eagle."
    "Whoa, how long has this guy been standing there?"
    
    pf "Uh, yeah."
    voice "audio/voice/E2/D5/S2/eng1m/2.ogg"
    eng1m "Your weapons cleared customs. Please sign here."
    "He holds out a tablet with an \"x\" indicating where I should sign."
    show mayu cur at l3
    show shou cur at cc
    "I glance at my team, but they're all as dumbfounded as I am."
    pf "Okay…"
    show mayu neu at l3
    show shou neu at cc
    "After signing on the tablet, I give the device back to him."
    
    pf "Talk about a convenient coincidence!"
    
    voice "audio/voice/E2/D5/S2/eng1m/3.ogg"
    eng1m "... What? We've been emailing you for the last four days asking you to claim your weaponry. I'm only here because obviously you don't know what to do and I want to close this work ticket."
    stop music fadeout 5
    hide guard with dissolve
    
    
    show bg campus hangar day:
        linear .66 xoffset 0
    show kaori:
        linear .66 xoffset 0
    show mayu:
        linear .66 xoffset 0
    show shou:
        linear .66 xoffset 0
        
        
        
    $renpy.pause(.66)
    show kaori dis at r3:
        xzoom -1
    
    show dots:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    show mayu smi at l3
    show note:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou mis at cc
    "I fall silent. Shou lets out a snicker and Kaori facepalms."
    
    pf "Sorry, my bad."
    
    "After ensuring the signature on his tablet processes, he nods and leaves."
    
    #play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 5
    
    pf "Well, I have weapons now."
    
    show kaori neu at r3
    show shou smi at cc
    voice "audio/voice/E2/D5/KI/12.ogg"
    ki "Finally. Go configure your GEAR and join us in the simulation when you're ready. We'll get started with a warm-up."
    
    "I nod."
    
    
    pf "I'll see you guys in a bit."
    hide kaori
    hide mayu
    hide shou
    with dissolve
    
    "I head to Eagle and make my way into the cockpit."
    
    #Into the cockpit and stuff
    stop ambient fadeout 1.5
    scene black with fade
    
    $renpy.pause(1.0)

    
    scene cg GEAR cockpit first2 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    $renpy.pause(.5)
    play ambient "audio/ambience/GEAR Cockpit.ogg" fadein 1
    play sound "audio/sfx/GEAR/GEAR Boot Up 2.ogg"
    #$renpy.pause(1.5)
    scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    
    voice "audio/voice/E2/D5/S2/Eagle/1.ogg"
    GEARpf "Gear initialization sequence completed."
    ### VOICE - no line recorded for this?
    #play music "audio/music/Inventory (GAME VERSION).ogg" fadein 3
    voice "audio/voice/E2/D5/S2/Eagle/2.ogg"
    GEARpf "Loading GEAR layout screen."
    
    ### DISHU UPDATE ### for removal of inventory screen
    
    ### NOTE Items
    #Open inventory system with the basic equipment there Mini-tutorial and w/e is needed. this is gameplay stuff.
    
    #$ inv.unequip("defaultKatana")
    #$ inv.remove("defaultKatana")
    #$ inv.unequip("defaultPistol")
    #$ inv.remove("defaultPistol")
    
    #$ inv.add("e004")
    
    #$ invStance = "default"
    #$ invLoadout = "default"
    
    #$ inv.add("defaultCore")
    #$ inv.add("defaultFrame")
    #$ inv.add("defaultThruster")
    
    #$ inv.add("defaultBuster")
    #$ inv.add("defaultDaggers")
    #$ inv.add("defaultKatana")
    #$ inv.add("defaultPistol")
    #$ inv.add("defaultRifle")
    #$ inv.add("defaultSMG")
    #$ renpy.block_rollback()
    
    #label E2D5S2_Inventory:
    #    call screen inventory_screen
    #    
    #    if "defaultCore" in inv.equipped.values() and "defaultFrame" in inv.equipped.values() and "defaultThruster" in inv.equipped.values():
    #        
    #        if "defaultBuster" in inv.equipped.values() or "defaultDaggers" in inv.equipped.values() or "defaultKatana" in inv.equipped.values():
    #            
    #            if "defaultPistol" in inv.equipped.values() or "defaultRifle" in inv.equipped.values() or "defaultSMG" in inv.equipped.values():
    #                
    #                pf "Alright, all set. Please save configuration."
    #                
    #            else:
    #                "{i}Make sure you equip a weapon to your ranged slot in your GEAR!{/i}"
    #                jump E2D5S2_Inventory
    #            
    #        else:
    #            "{i}Make sure you equip a weapon to your melee slot in your GEAR!{/i}"
    #            jump E2D5S2_Inventory
    #            
    #    else:
    #        
    #        "{i}Make sure you equip a core, a frame, and a thruster to your GEAR!{/i}"
    #        jump E2D5S2_Inventory
            
        
    #$ renpy.block_rollback()
    
    "I navigate through my GEAR options and configure it to my preference."
    "After a little bit of time, everything seems to be where it should be."
    pf "Eagle, save configurations and set as default."
    stop music fadeout 3
    voice "audio/voice/E2/D5/S2/Eagle/3.ogg"
    GEARpf "Completed."
    voice "audio/voice/E2/D5/S2/Eagle/4.ogg"
    GEARpf "You have a pending virtual simulation request."
    pf "Please start it up."
    stop music fadeout 5
    voice "audio/voice/E2/D5/S2/Eagle/5.ogg"
    GEARpf "In progress."
    "I wait as Eagle connects me into my team's virtual simulation match."
    stop ambient fadeout 3
    
    #Fade into simulation
    scene white with dissolve
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 10
    scene bg battleground day with dissolve
    show mc mech at bl with dissolve:
        xzoom -1
    
    voice "audio/voice/E2/D5/SS/5.ogg"
    ss "Ah! There's Mr. Broseph."
    pf "Yep."
    ### NOTE Placeholder animations, would like to use player's equipped weapons
    # also it seems fine to have mc on his own, they are about to tell him to "let's see what you can do solo"
    #show mc ready at bl with dissolve
    show mc attR at bl with dissolve
    "I direct Eagle to grab its weapons and test them out."
    voice "audio/voice/E2/D5/MA/0-03.ogg"
    ma "It looks like your equipment registered just fine."
    show mc attM at bl with dissolve
    pf "Mhm. I'm ready for a fight!"
    voice "audio/voice/E2/D5/KI/13.ogg"
    ki "Good. Let's see what you can do solo so we can baseline your abilities."
    show mc mech at bl with dissolve
    
    menu:
        "I'll give it my best.":
            pf "Sounds good to me."
    
        "1v1? Just how I like it.":
            pf "Let me show you how it's done."
    
        "...":
            "I stay silent as I'm focused on the impending duel."
    
    voice "audio/voice/E2/D5/KI/14.ogg"
    ki "Let's match you up with a level 48 AI program."
    voice "audio/voice/E2/D5/SS/6.ogg"
    ss "Level 48?"
    voice "audio/voice/E2/D5/MA/0-04.ogg"
    ma "That seems a bit high for just a match to gauge his abilities..."
    voice "audio/voice/E2/D5/KI/15.ogg"
    ki "Why? All of us can beat that on our own."
    voice "audio/voice/E2/D5/SS/7.ogg"
    ss "Yeah, but not on our first try. We lost numerous times before learning its pattern."
    $ E2D5S2_Spirit = 0
    
    menu:
        "I'm up for it!":
            $ E2D5S2_Spirit = 1
            show mc ready at bl with dissolve
            pf "I don't mind the challenge. Go ahead."
            voice "audio/voice/E2/D5/KI/16.ogg"
            ki "See Shou? At least he's willing to try something hard."
            voice "audio/voice/E2/D5/SS/8.ogg"
            ss "Maybe {i}you{/i} should try something hard!"
            voice "audio/voice/E2/D5/KI/17.ogg"
            ki "W-What did you say?!"
            voice "audio/voice/E2/D5/MA/0-05.ogg"
            ma "O-oh my..."
            "Kaori's GEAR points its blade at Emerald."
            voice "audio/voice/E2/D5/SS/9.ogg"
            ss "Wait! I didn't mean it to sound like that!"
            "Bam!"
            "Simulation" "Emerald Destroyed."
            voice "audio/voice/E2/D5/SS/10.ogg"
            ss "... Okay, maybe I deserved that."
            show mc mech at bl with dissolve
            pf "Uh, so about that Level 48 AI..."
            voice "audio/voice/E2/D5/KI/18.ogg"
            ki "Shut up! I'm loading it now."
            "Kaori disabled her video feed but I can guarantee her cheeks are burning."
    
        "Level 48? Change that to level 50.":
            $ E2D5S2_Spirit = 2
            show mc ready at bl with dissolve
            pf "Level 48 is nothing, change it to 50."
            voice "audio/voice/E2/D5/MA/0-06.ogg"
            ma "Wha...!"
            voice "audio/voice/E2/D5/SS/11.ogg"
            ss "Are you serious?"
            pf "Yeah, let's get on with it already."
            voice "audio/voice/E2/D5/SS/12.ogg"
            ss "I don't know if it's such a good idea--"
            voice "audio/voice/E2/D5/KI/19.ogg"
            ki "Whatever, I'm loading it since he thinks he can handle it."
    
        "Maybe a bit lower wouldn't hurt.":
            pf "An easier match would let me first get used to my weaponry."
            voice "audio/voice/E2/D5/KI/20.ogg"
            ki "...Are you serious?"
            voice "audio/voice/E2/D5/MA/0-07.ogg"
            ma "It's okay if he has to warm up first, Kaori."
            voice "audio/voice/E2/D5/KI/21.ogg"
            ki "Fine. we'll start it at level 45 then."
            pf "Okay."
            
    stop music fadeout 3
    "My teammates' GEARs vanish as they enter spectator mode. {w}A few seconds later, an enemy GEAR prompts on my radar."
    show aiM neu at br with dissolve
    play music "audio/music/Fight Song 1 (GAME VERSION).ogg" fadein 3
    pf "Alright Eagle, let's show them what we've got."
    voice "audio/voice/E2/D5/S2/Eagle/6.ogg"
    GEARpf "Combat mode activated."
    
    
    
    
    
    #$ context = "E2D5S2_FirstPractice"
    #$ enemy = "aiM"
    #$ mode = "default"
    #$ survived = 0
    
    ### NOTE Placeholder MC stats here until inventory implementation
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
    #show screen timer_scrReaction(place="E2D5S2_FirstPractice")
    #jump qte_game
    
    
    
    
    

    $renpy.pause(.25)


    show mc attR with Dissolve(.45)
    play sound rangeSound
    $renpy.pause(.15)
    "I begin by equipping my rifle and blasting the AI with energy rounds. The rounds mostly connect, bouncing off the edges of the shield."
    "Something must be wrong with the aim... I'm not that bad of a shot!"
    "Well, I can't use those."
    "I swich in my sword and grin. I'm just as lethal with a blade anyway!"
    show mc attM with dissolve
    "Raising my sword, I take a striking stance."
    "..."
    show mc mech with dissolve
    "My blade isn't powering up?!"

    "I barely have time to register what happened, when I see a sword charging at me!"

    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E2D5S2_L1")
                
    menu:
        "Block!":
            jump E2D5S2_W1

        "Slow…":
            jump E2D5S2_L1

        "Freeze…":
            jump E2D5S2_L1

        "Dodge!":
            jump E2D5S2_W1

        "Fail…":
            jump E2D5S2_L1

    label E2D5S2_L1:
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
                
                
        "My shields shimmer as they take the brunt of the attack and my dashboard flashes in warning. My energy is dangerously low! These higher-leveled AIs are no joke!"
        jump E2D5S2_COMBATCONV
        
    label E2D5S2_W1:
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
            
        play sound2 dodSound
        show mc dod at bl with Dissolve(.45):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -150
            
        "I block the attack just in time, but still eat up a lot of damage. These higher-leveled AIs are no joke!"
        jump E2D5S2_COMBATCONV
        
    label E2D5S2_COMBATCONV:
    
    
    show aiM neu att at br, Shake(None, 1, dist=20):
        xoffset 0
        parallel:
            easeout .1 alpha 1.0
        parallel:
            easeout .1 xoffset -600
    $renpy.pause(.1)

    play sound meleeSound
    show aiM att at br with Dissolve(.2):
        xoffset -800

    show white with Dissolve(0.15):
    play sound2 hitSound
    hide white with Dissolve(0.25)
    
    show mc blo at bl, Shake(None, .5, dist=20):
        parallel:
            easeout .3 alpha 1.0
        parallel:
            easeout .3 xoffset -300
    
    
    "The AI charges me again and I'm forced to block. For the rest of the match, I'm stuck in a defensive position as all of my weapons do very little damage."
    
    
    show aiM neu att at br, Shake(None, 1, dist=20):
        xoffset 0
        parallel:
            easeout .1 alpha 1.0
        parallel:
            easeout .1 xoffset -800
    $renpy.pause(.1)

    play sound meleeSound
    show aiM att at br with Dissolve(.2):
        xoffset -1000

    show white with Dissolve(0.15):
    play sound2 hitSound
    hide white with Dissolve(0.25)
    
    show mc ready at bl, Shake(None, .5, dist=20):
        parallel:
            easeout .3 alpha 1.0
        parallel:
            easeout .3 xoffset -450
    
    play sound Depowered
    hide mc with dissolve
    
    "It's not long before my energy is drained and I get depowered."





    
    
    
    
    
    label E2D5S2_FirstPractice:
        $ renpy.hide_screen ("battle_screen")
        stop music fadeout 5
        show aiM neu at br with dissolve
        # depower sfx?
        #show mc mech at bl with dissolve:
        #    xzoom -1
    
    if E2D5S2_Spirit == 1:
        #Enter a match but your weapons basically do no damage, you get depowered
        "My weaponry barely did any damage!"
        play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
        "Kaori sighs through the intercom."
        voice "audio/voice/E2/D5/KI/22.ogg"
        ki "I mean, I didn't expect much, but that was really bad."
        pf "My equipment wasn't functioning properly."
        voice "audio/voice/E2/D5/SS/13.ogg"
        ss "Really? What happened?"
        pf "I'm not sure. I'm doing a check now."
    
    elif E2D5S2_Spirit == 2:
        #Enter a match but your weapons basically do no damage, you get depowered
        "What the crap was that? My aim was true but Eagle wasn't responding properly."
        play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
        voice "audio/voice/E2/D5/SS/14.ogg"
        ss "Yeah man, level 50 is a bit {i}too{/i} intense."
        pf "Eagle's equipment wasn't responding properly!"
        voice "audio/voice/E2/D5/KI/23.ogg"
        ki "That's your excuse?"
        pf "No, I'm serious."
        voice "audio/voice/E2/D5/MA/0-08.ogg"
        ma "His attacks and aim didn't seem natural... I think it is something else..."
        voice "audio/voice/E2/D5/KI/24.ogg"
        ki "Run a scan on Eagle."
        pf "On it now."
    
    else:
        #Enter a match but your weapons basically do no damage, you get depowered
        "Something's up with Eagle, the controls didn't feel right."
        play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
        voice "audio/voice/E2/D5/MA/0-09.ogg"
        ma "Umm... At least it was a good attempt?"
        voice "audio/voice/E2/D5/KI/26.ogg"
        ki "No, that was bad."
        pf "I know, something's up with Eagle."
        voice "audio/voice/E2/D5/KI/27.ogg"
        ki "Like, really bad."
        pf "I get it, geez. Give a minute. I'm doing a scan to see what's wrong."
    
    
    "My team waits patiently as I run some diagnostic tools."
    "..."
    play ambient "audio/ambience/GEAR Cockpit.ogg" fadein 1
    scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    pf "Ah I think I got it!"
    voice "audio/voice/E2/D5/KI/29.ogg"
    ki "Hm?"
    pf "It looks like the equipment wasn't calibrated after customs did their in-depth examination. That's why the aim and attacks were off."
    voice "audio/voice/E2/D5/SS/15.ogg"
    ss "Is it something you can fix?"
    pf "Not exactly, there are some hardware tweaks that need to be done, but I think this may require an engineer..."
    voice "audio/voice/E2/D5/SS/16.ogg"
    ss "Mm, I suppose that makes sense. GEARs also need the occasional \"tire rotation and oil change\" to make sure they function well."
    voice "audio/voice/E2/D5/KI/30.ogg"
    ki "That's great, but in case you didn't notice, we don't have an engineer."
    pf "I think I might know someone, I'll meet you guys in the Hangar."
    "The lights flash green on my teammates comm screens and they disconnect from the simulator."
    
    stop music fadeout 2
    
    jump E2D5S3

