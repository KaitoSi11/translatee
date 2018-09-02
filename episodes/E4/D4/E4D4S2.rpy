#
label E4D4S2:
    
    #Arena
    # ambient?
    scene bg campus arena day with fade
    
    "Most matches during reading week are pretty quiet in terms of audience, but today the auditorium is filled with as many people if not more than a typical match."
    
    play music "audio/music/Fight Song 1 (GAME VERSION).ogg" fadein 5
    
    voice "audio/voice/E4/Announcer/D4/1.ogg"
    an "Two undefeated teams, but only one will continue their winning streak!"
    scene bg battleground day with dissolve:
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
        
    voice "audio/voice/E4/Announcer/D4/2.ogg"
    an "Entering first is ACE-2049-11--"
    "The crowd thunders to life. I stare out into the sea of people as they jump and wave from their seats. The difference from the polite applause we received when we started is surreal."
    "Their energy fuels me and I can't hold back my grin. If this is a taste of what it's like to compete in the big leagues, then count me in!"
    voice "audio/voice/E4/Announcer/D4/3.ogg"
    an "--versus the team who requires no introduction... REBORN!"
    "The stadium rumbles from all of the cheering. {w}The underdog versus the university's pride… I'd put aside my studying to watch a match like that too."
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
            
    $renpy.pause(1.5)
    
    show reborn neu at tr with dissolve:
        xoffset 425
        xzoom .8
        yzoom .8
            
    show reborn2 neu at tl with dissolve:
        xoffset 200
        xzoom .8
        yzoom .8
            
    show akira mech at mm with dissolve:
        xoffset -400
            
    show reborn3 neu at br with dissolve:
        xoffset 500
    
    "REBORN enters the stadium. Their GEAR's sparkle underneath the lights--a sleek and pristine image of the modernity of Aludian."
    voice "audio/voice/E4/Announcer/D4/4.ogg"
    an "Are you all ready for this legendary showdown?!"
    scene bg campus arena day with dissolve
    "The crowd goes wild."
    voice "audio/voice/E4/Announcer/D4/5.ogg"
    an "Then let's not delay this anymore!"
    voice "audio/voice/E4/Announcer/D4/6.ogg"
    an "AND..."
    voice "audio/voice/E4/Announcer/D4/7.ogg"
    an "BEGIN!"
    
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
        
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_22.ogg"
    ki "Let's go! Stick to the plan and be vocal."
    voice "audio/voice/E4/Shou/d4/16 Copy.ogg"
    ss "Roger."
    show mc ready with dissolve
    pf "Got it."
    voice "audio/voice/E4/Mayu/D4/Mayu D4-12.ogg"
    ma "Okay!"
    
    show mc ready at bl, Shake(None, 1, dist=20) behind kaori:
        xzoom -1
        parallel:
            easeout .5 alpha 1.0
        parallel:
            easeout .5 xoffset 1750
    $renpy.pause(1)
    scene black with fade
    
    "I jet away from the rest of my team as they circle Akira's team."
    "As if looking in a mirror, Akira's team follows suit. They boost towards the rest of my team as Akira stays put."
    #use akira CG here
    $ persistent.gpix[10][0] = 1
    scene cg GEAR akira solo with fade
    "His GEAR shifts into fighting stance. He brandishes his scythe and activates the energy blade."
    "He was waiting for me! Did he anticipate our plans or did he just want to fight me one on one?"
    "Either way, it doesn't matter. All that matters now is that I'm here and Akira's here. My teammates' voices fade into the background as they coordinate their attacks against the rest of REBORN. All of my focus is on Phoenix."
    
    menu:
        "This will be a glorious duel!":
            "My heart races. A clean duel between myself and the top ACE pilot... {w}It's time to see what I'm really made of."
            "I grab the Eagle's controls. My hands are sweaty but my nerves have steadied. My adrenaline is pumping and I'm itching to begin."
        
        "Size him up first.":
            "Still keeping some distance between us, I stop my thrusters. I read my weapons and stare down Phoenix."
            "The crowd ignites at the sight of our impending showdown."
            "Alright Akira, let's see what makes you so popular!"
        
        "Engage Phoenix.":
            "I'm poised to strike and do not hesitate."
    
    scene bg battleground day with fade
    show akira mech at br with dissolve:
        xoffset -250
        
    "I max Eagle's thrusters and dash forward. Phoenix braces for the attack."
    
    # QTE
    $ E4D4S2_QTELossCount = 0
    
    $ qtebase = 3
    $ qtetotal = qteath + qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E4D4S2_QTE1L")
    
    menu:
        "Strike!":
            jump E4D4S2_QTE1W
        
        "Miss...":
            $ E4D4S2_QTELossCount += 1
            jump E4D4S2_QTE1L
        
        "Whiff...":
            $ E4D4S2_QTELossCount += 1
            jump E4D4S2_QTE1L
        
        "Slash!":
            jump E4D4S2_QTE1W
        
        "Connect!":
            jump E4D4S2_QTE1W
    
    label E4D4S2_QTE1W:
        $ renpy.hide_screen ("timer_scr")
        
        show mc ready at bl, Shake(None, 1, dist=20):
            xoffset -1500
            xzoom -1
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 250
        $renpy.pause(.5)
        #
        play sound meleeSound
        if "defaultBuster" in list(inv.equipped.values()):
            $ mcEnergy -= 10
            show mc attM at bl with Dissolve(.45):
                xoffset 400   # +150
        elif "defaultKatana" in list(inv.equipped.values()):
            show mc attM at bl with Dissolve(.45):
                xoffset 300 # +50
        else:
            show mc attM at bl with Dissolve(.45):
                xoffset 250 # +0
            
        show white with Dissolve(0.25):
            xalign 0.5
            yalign 0.5
        play sound2 hitSound
        hide white with Dissolve(0.15)
        
        show akira att at br, Shake(None, 1, dist=20):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 250
                
        "I deliver a powerful blow. With its scythe raised, Phoenix parries, but still gets knocked back from the sheer force of my attack."
        jump E4D4S2_QTE2
    
    label E4D4S2_QTE1L:
        $ renpy.hide_screen ("timer_scr")
        
        show mc ready at bl, Shake(None, 1, dist=20):
            xoffset -1500
            xzoom -1
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 250
        $renpy.pause(.5)
        #
        play sound meleeSound
        if "defaultBuster" in list(inv.equipped.values()):
            show mc attM at bl with Dissolve(.45):
                xoffset 400   # +150
        elif "defaultKatana" in list(inv.equipped.values()):
            show mc attM at bl with Dissolve(.45):
                xoffset 300 # +50
        else:
            show mc attM at bl with Dissolve(.45):
                xoffset 250 # +0
            
        show white with Dissolve(0.25):
            xalign 0.5
            yalign 0.5
        play sound2 "audio/sfx/GEAR Combat/Block.ogg"
        hide white with Dissolve(0.15)
        
        show akira att at br, Shake(None, 1, dist=20):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 250
                
        $renpy.pause(1)
        show akira att at br, Shake(None, 1, dist=20):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -250
                
        play sound "audio/sfx/GEAR Combat/Sword Single.ogg"
        $renpy.pause(.5)
        play sound2 hitSound
        show mc blo at bl, Shake(None, 1, dist=20) with Dissolve(.45):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -100
                
        play sound bloSound
        $renpy.pause(1)

        "As I swing my blade, Phoenix boosts to the side, dodging the attack, and swings his scythe against the side of Eagle."
        "The shockwave sends me tumbling back. Thankfully, my shield took the brunt of the force but I won't be able to sustain another hit like that."
    
    label E4D4S2_QTE2:
        "Phoenix dashes towards me, winding up his scythe for a carving!"
        # QTE
    
    $ qtebase = 3
    $ qtetotal = qteath + qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E4D4S2_QTE2L")
    
    menu:
        "Slow...":
            $ E4D4S2_QTELossCount += 1
            jump E4D4S2_QTE2L
        
        "Dodge!":
            jump E4D4S2_QTE2W
        
        "Sluggish...":
            $ E4D4S2_QTELossCount += 1
            jump E4D4S2_QTE2L
        
        "Trip...":
            $ E4D4S2_QTELossCount += 1
            jump E4D4S2_QTE2L
        
        "Boost!":
            jump E4D4S2_QTE2W
    
    label E4D4S2_QTE2W:
        $ renpy.hide_screen ("timer_scr")
        
        show akira att at br, Shake(None, 1, dist=20):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -250
                
        play sound "audio/sfx/GEAR Combat/Sword Single.ogg"
        
        show mc dod at bl with Dissolve(.45):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -250
                
        play sound2 dodSound
        $renpy.pause(1)
        
        if "defaultPistol" in list(inv.equipped.values()):
            show mc attR with Dissolve(.45):
                xoffset 75
        elif "defaultRifle" in list(inv.equipped.values()):
            show mc attR with Dissolve(.45)
        else:
            show mc attR with Dissolve(.45)
            
        play sound rangeSound
        
        play sound2 hitSound
        
        show akira blo at br, Shake(None, 1, dist=20):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -250
                
        play sound bloSound
        "My reflexes kick into motion and I send energy to my side thrusters. With a rumble of my engines, I dodge to the side and send a powerful strike towards Phoenix. Its shield shimmers to protect the GEAR, but it looks like he took a decent hit to his energy reserve."
        jump E4D4S2_QTE3
    
    label E4D4S2_QTE2L:
        $ renpy.hide_screen ("timer_scr")
        if E4D4S2_QTELossCount == 2:
            show akira att at br, Shake(None, 1, dist=20):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset -1500
                    
            play sound "audio/sfx/GEAR Combat/Sword Single.ogg"
            $renpy.pause(.25)
            play sound2 hitSound
            
            show mc blo at bl, Shake(None, 1, dist=20) with Dissolve(.45):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset -1500
                    
            play sound bloSound
            
        else:
            show akira att at br, Shake(None, 1, dist=20):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset -250
                    
            play sound "audio/sfx/GEAR Combat/Sword Single.ogg"
            $renpy.pause(.25)
            play sound2 hitSound
            
            show mc blo at bl, Shake(None, 1, dist=20) with Dissolve(.45):
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset -150
                    
            play sound bloSound
            
        $renpy.pause(1)
        
        "In one smooth motion, Phoenix closes the gap between us and slices me in a horizontal swing. Too slow to react, Eagle and I are sent tumbling back as my shield shimmers."
        
        if E4D4S2_QTELossCount == 1:
            "My shield will not be able to sustain another hit like that."
        elif E4D4S2_QTELossCount == 2:
            scene black with fade
            "A bright red warning flashes across my screen warning me that my energy reserve is in the single digits. {w}This is not good!"
            jump E4D4S2_OverLoss
            
    label E4D4S2_QTE3:
        scene bg campus arena day with dissolve
        
    "I fall into defense and circle Akira, who circles me. We're both waiting for the other to make a move. Akira is the first to break the circle. As soon as he activates his thrusters, so do I."
    scene bg battleground day with dissolve
    "We boost towards each other at incredible speed, our weapons leading the way!"
    show white with dissolve:
        xalign 0.5
        yalign 0.5

    if "defaultBuster" in list(inv.equipped.values()):
        show mc attM at bl behind white:
            xoffset 0   # +150
            xzoom -1
    elif "defaultKatana" in list(inv.equipped.values()):
        show mc attM at bl behind white:
            xoffset -100 # +50
            xzoom -1
    else:
        show mc attM at bl behind white:
            xoffset -150 # +0
            xzoom -1

    show akira att at mm behind white:
        xoffset 150
        
    $renpy.pause(0.25)
    play sound meleeSound
    play sound2 "audio/sfx/GEAR Combat/Sword Single.ogg"
    hide white with Dissolve(1)
    play sound hitSound
    "Our energy blades collide in a loud ringing which rends the air. I grit my teeth, and push with all my might as our blades stay locked in a battle of wills."
    
    $ E4D4S2_WonDuel = 0
    
    # QTE
    $ qtebase = 3
    $ qtetotal = qteath + qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E4D4S2_QTE3L")
    
    menu:
        "Weakness...":
            $ E4D4S2_QTELossCount += 1
            jump E4D4S2_QTE3L
        
        "Get overpowered...":
            $ E4D4S2_QTELossCount += 1
            jump E4D4S2_QTE3L
        
        "Parry!":
            jump E4D4S2_QTE3W
        
        "Fail...":
            $ E4D4S2_QTELossCount += 1
            jump E4D4S2_QTE3L
        
        "Give in...":
            $ E4D4S2_QTELossCount += 1
            jump E4D4S2_QTE3L
    
    label E4D4S2_QTE3W:
        $ renpy.hide_screen ("timer_scr")
        "Sweat beads on my forehead while I continue to control Eagle. Channeling all of my strength, a yell escapes my lips as I force his scythe up and spin out of the way to land a swing at his back."
        show mc attM at bl, Shake(None, 1, dist=20):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 450
                
        $renpy.pause(.25)
        play sound hitSound
        show akira blo at mm, Shake(None, 1, dist=20) with Dissolve(.45):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset 350
                
        play sound2 bloSound
        "The hit registers and Akira's shield shimmers dangerously."
        pf "Yes!"
        "If I keep this up, I think I can win!"
        jump E4D4S2_OverWin
    
    label E4D4S2_QTE3L:
        $ renpy.hide_screen ("timer_scr")
        
        show akira att at mm, Shake(None, 1, dist=20):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -350
                
        $renpy.pause(.25)
        play sound hitSound
        show mc blo at bl, Shake(None, 1, dist=20) with Dissolve(.45):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -250
                
        play sound2 bloSound
        "A surge of energy from Phoenix rams Eagle. In one sweeping motion, he spins and the scythe's long blade smashes against my front shield."
        scene black with fade
        "My energy power reaches sub 5 percent from that attack and a \"Critical Warning\" flashes across my screen."
        jump E4D4S2_OverLoss
    
    label E4D4S2_OverWin:
        $ E4D4S2_WonDuel = 1
        show mc mech with dissolve:
            xoffset 0
        "I can't tell if I can hear the roar of the crowd or if that's the blood thundering in my ears in time with the pounding of my heart."
        show akira att with dissolve
        "Before I have a chance to catch my breath, Phoenix boosts towards me. His scythe points at me, ready for an attack. I steady my blade for a parry, when its thrusters change at the last moment and the scythe switches angles!"
        show akira att Shake(None, 1, dist=20):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -500
                
        $renpy.pause(.25)
        play sound hitSound
        show mc blo at bl, Shake(None, 1, dist=20) with Dissolve(.45):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -250
                
        play sound2 bloSound
        "I manage to block some of the force with my blade but it's at an awkward angle. Phoenix swipes wide again."
        
        menu:
            "Too fast...":
                 $ E4D4S2_WonDuel = 1
                #(empty choice)
            "Can't block...":
                 $ E4D4S2_WonDuel = 1
                #(empty choice)
            "Unparryable...":
                 $ E4D4S2_WonDuel = 1
                #(empty choice)
                
        show akira att at mm, Shake(None, 1, dist=20):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -1500
                
        $renpy.pause(.25)
        play sound hitSound
        show mc blo at bl, Shake(None, 1, dist=20):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -1500
                
        play sound2 bloSound
        "The scythe smashes into Eagle's side. Phoenix is about to swing again! Akira is attacking far more aggressively now than when we began. Was he just taking it easy to gauge my ability?"
        scene black with fade
        "Well, I won't be underestimated! If he thinks he's about to swing for the win, he'll be sorely disappointed!"
        jump E4D4S2_Overdrive
    
    
    label E4D4S2_OverLoss:
        $ E4D4S2_WonDuel = 0
        "I refuse to lose so easily. Looks like it's now or never!"
        jump E4D4S2_Overdrive
    
    label E4D4S2_Overdrive:
        stop music fadeout 5
        play sound "audio/sfx/GEAR Combat/Overdrive Phase 1.ogg"
        "I flip on the overdrive mode and pray it works."
        scene white with dissolve
        play sound "audio/sfx/GEAR Combat/Overdrive Phase 2.ogg"
        "The familiar shifting of noises and motions sounds in my cockpit and my heart threatens to beat right out of my chest in anticipation."
        
        play sound "audio/sfx/GEAR Combat/Overdrive Phase 3.ogg"
        scene cg GEAR overdrive first with Shake((0, 0, 0, 0), 2.5, dist=20):
            xalign 0.5
            yalign 0.5
            xzoom 1.1
            yzoom 1.1
        
        play music "audio/music/Raycrash (GAME VERSION).ogg" fadein 3
        "An eruption of energy explodes from Eagle and I'm once again looking at my energy reserve sitting well over 9000."
        "I let out a small whoop of relief and excitement. I feel just as pumped and rejuvenated as Eagle!"
        "I have 3 minutes on the clock, but let's see if Phoenix can even last that long!"
        "My fists glow softly from the overwhelming energy. Channeling that energy, I ready myself to attack when something collides with Eagle and forces me to slide back."
        play sound "audio/sfx/GEAR Combat/Energy Fist Activation.ogg"
        stop music fadeout 1
        scene white with fade
        "...!"
        play music "audio/music/Fight Song 2 (GAME VERSION).ogg" fadein 3
        "Phoenix's wings extend and his entire GEAR is surrounded by a swirl of red energy!"
        "What? Can Akira's GEAR enter overdrive mode too?! How is this possible?"
        "Phoenix races towards me, snapping me out of my thoughts."
    
    if E4D4S2_WonDuel == 1:
        $ persistent.gpix[11][0] = 1
        scene cg GEAR final clash with dissolve
        "Phoenix maxes its thrusters and leaps in the air. As it spirals down, I raise my arm and our fists collide. Waves of energy ripple away from us. Still clutching my blade in my other hand, I strike. Phoenix rolls to the side then dashes back towards me with his scythe raised."
        "Our blades clash in a parry."
        "Since we're both in overdrive mode, it looks like we're back on equal footing. I clench my jaw. This did not go well for me when we were simply on pilot skill."
        "How should I play this?"
        
        # QTE
        $ qtebase = 3
        $ qtetotal = qteath + qtebase
        $ t_var = qtetotal
        show screen timer_scr(place="E4D4S2_FTW")
    
        menu:
            "Go for the win!":
                label E4D4S2_FTW:
                    $ renpy.hide_screen ("timer_scr")
                    $ E4D4S2_WonDuel = 0
                    "I strengthen my resolve. I can do this… I {i}know{/i} it!"
                    "My hands grip the controls tightly and command Eagle to charge Akira."
                    "I raise my blade above my head for a vertical slash, but Phoenix raises his left hand and stops me by unleashing a barrier of crackling red energy."
                    "The shield knocks Eagle back, but I recalibrate quickly and enable my thrusters to catch me before I topple over."
                    "Phoenix barrels towards me once again."
                    jump E4D4S2_FinalLoss
            
            "Delay tactics--stick to the plan!":
                $ renpy.hide_screen ("timer_scr")
                "When in doubt, follow the plan. I need to keep Akira out of play for as long as I can."
                "I alter my energy output to play defensively and raise my blade in case I need to block or parry."
                "I cautiously watch Phoenix, who activates again and rushes towards me."
                "With my defensive protocol enabled, I easily parry his blow and return to my defensive stance."
                "Phoenix charges forward again, swinging the scythe to the right, which I manage to block. Without a second's hesitation, Phoenix spins and lands an energy fist into Eagle's front arc."
                "My shield shimmers as it absorbs the blow... a blow which otherwise could have taken out a GEAR in one strike."
                "I keep a watchful eye on my stats. I won't be able to delay him for too long before he'll wear me down."
                "That's okay. Stay focused! I block blow after blow. Those which make it through my defense are absorbed by my shield."
                "Even with no energy output on offense or thrusters, Akira's skillful attacks are rapidly connecting and depleting my overdrive reserve."
                "It looks like I won't be able to sustain any more attacks after this..."
                "Phoenix charges towards me one last time as I brace for the final blow."
                "..."
                "!"
                "Phoenix hovers on top of me mid-swing, but the red glow has disappeared."
                "In fact, all of its energy is gone! Did it just get depowered?"
                "This is very reminiscent of how Eagle suddenly depowers after overdrive mode. This is way too similar to be coincidence." 
                "Although Phoenix can't move, Eagle still can. I glance at the timer. Only 45 seconds have passed."
                scene bg campus arena day with fade
                "A wane smile graces my lips. Looks like Eagle's core is still one of a kind."
                voice "audio/voice/E4/Shou/d4/17 Copy.ogg"
                ss "Akira is depowered?!"
                voice "audio/voice/E4/Mayu/D4/Mayu D4-13.ogg"
                ma "What?"
                voice "audio/voice/E4/Kaori/D4/Kaori_D4_23.ogg"
                ki "Are you serio--ah!"
                scene bg battleground day with fade:
                    xalign 0.99
                show mco attFist at mm with dissolve
                "Right! There's still a match going on. No time for dilly-dallying!"
                show mco attFist at mm, Shake(None, 1, dist=20):
                    parallel:
                        easeout .5 alpha 1.0
                    parallel:
                        easeout .5 xoffset -1750
                "With my overdrive mode still good for about 2 minutes, I speed towards my teammates and assess the damage."
                scene black with fade
                "Shou and Mayu were depowered, but they took out one of the opposing GEARs and dealt decent damage to the others."
                scene bg battleground dusk with fade:
                    xalign 0.01
                show kaori mech at mm with dissolve:
                    xoffset 125
                    xzoom -1
                show reborn neu at br with dissolve:
                    xoffset 550
                show reborn2 att at bl with dissolve:
                    xoffset -550
                    xzoom -1
                "Aura is struggling to hold off two GEARs at once. Her armour is riddled with dents and dings--she's definitely seen better days!"
                show mco attFist at mm, Shake(None, 1, dist=20):
                    xoffset 1750
                    parallel:
                        easeout .5 alpha 1.0
                    parallel:
                        easeout .5 xoffset -125
                pf "I'm here."
                "With Eagle and Aura back to back, we both ready ourselves."
                voice "audio/voice/E4/Kaori/D4/Kaori_D4_24.ogg"
                ki "We can still do this."
                
                menu:
                    "Show them what Eagle's Overdrive can do.":
                        pf "Of course. Let's go!"
                        
                scene bg campus arena dusk with dissolve
                "I spawn an energy shield in front of us to block the incoming shots as Kaori charges in, safe behind the protective wall."
                "As soon as we are within melee range, we engage the remaining GEARs. My shield wavers as Kaori duels one of REBORN, but it hardly matters."
                "Her blades are a blur as they slice through the air and she soon has the opposing GEAR on the defensive."
                "My opponent can barely withstand Eagle's overdrive attacks, and although he managed to get a few strikes in, I ultimately depower him. My overdrive mode expires shortly after, so I turn my attention to Kaori's battle."
                scene bg battleground dusk with dissolve
                show kaori mech at bl with dissolve:
                    xzoom -1
                show reborn neu at br with dissolve:
                    xoffset 250
                "Even though both her and REBORN's GEAR are damaged, Aura is in much worse condition from the battle before."
                
                menu:
                    "You can do it!":
                        pf "There's only one left! You got this!"
                        voice "audio/voice/E4/Shou/d4/18 Copy.ogg"
                        ss "That's right!"
                        voice "audio/voice/E4/Mayu/D4/Mayu D4-14.ogg"
                        ma "Go Kaori!"
                    
                    "Don't let us down.":
                        pf "Eagle down, do your thing Aura."
                        "I see the green affirmative light pulsate from Kaori's comm. She's in the zone now."
                    
                    "Stay quiet. She knows what to do.":
                        "I stay quiet and watch in silence. Neither Shou nor Mayu make a sound either. A focused Kaori is an unstoppable Kaori."
                        
                show kaori att with dissolve
                "Aura readjusts and readies her weapon as does the other GEAR."
                scene bg campus arena dusk with dissolve
                "They charge each other in a clashing of blades! They seem evenly matched in their struggle, until Aura uses a sudden burst of energy to overwhelm the opponent and knocks its blade away. Then she strikes."
                "The blow depowers the enemy GEAR, but depowers Kaori as well. She used all her remaining energy to deal the final blow!"
                stop music fadeout 5
                "The arena is eerily quiet. Even the announcer is silent."
                voice "audio/voice/E4/Announcer/D4/8.ogg"
                an "...Hold on, folks. We'll have to check the replay on that."
                "The air is thick in my cockpit. I'm acutely aware of how my breath comes in ragged pants. Please let us be victorious!"
                "An image projects on the stadium billboard. Aura and the REBORN GEAR's blades are locked. I hold my breath as the video unfolds."
                "Aura forces the enemy blade away and strikes. The GEAR depowers and only one second later, Aura depowers… which means…"
                play music "audio/music/Victory! (GAME VERSION).ogg" fadein 3
                voice "audio/voice/E4/Announcer/D4/9.ogg"
                an "ACE-2049-11 CONTINUES THEIR UNDEFEATED STREAK!"
                "The ground shakes beneath my feet as the stadium rumbles with cheers and applause."
                pf "We…won?"
                voice "audio/voice/E4/Shou/d4/19 Copy.ogg"
                ss "We did it, broseph!"
                "Kaori lets out a loud cheer as Mayu laughs."
                "I stare out into crowd, hardly able to register what's going on. The people, the noises, the acrid smell of burnt metal… it's sensory overload."
                "But… we did it… we actually did it!"
    
    elif E4D4S2_WonDuel == 0:
        label E4D4S2_FinalLoss:
            scene cg GEAR final clash with dissolve
            "Its energy fist collides with Eagle, shaking me so hard, my head whips back. Before I have a chance to regain my bearings, Phoenix's scythe swipes me and knocks Eagle back again as my shield shimmers from the blow." 
            "Without a moment's rest, Phoenix returns the swing with a wide blow, extending the handle so the blade can cut further." 
            "Another explosion of energy knocks me back as the blade and my shield connect." 
            "I skid to a stop only to block another strike. Phoenix's attacks are non-stop!"
            "With both of us in overdrive mode, this doesn't feel any different than how the match was going originally."
            "Despite my efforts to change the tide of the battle, I'm forced to play defensively and Akira is able to depower Eagle..."
            "...and himself."
            "Wait--Phoenix is depowered?! Did I do something? {w}No, I only blocked that last attack and it was still strong enough to depower me. Maybe Akira channeled all his energy into that attack."
            "Checking the timer, I see that only 45 seconds have passed."
            "...Or maybe, he just ran out of juice."
            scene black with fade
            "Assuming I don't get manually depowered, overdrive mode on Eagle lasts 3 minutes, but Phoenix can only sustain 45 seconds… very curious..."
            voice "audio/voice/E4/Shou/d4/20 Copy.ogg"
            ss "Crap, I'm down."
            "Shou's voice pulls me out of my thoughts. I refocus my attention on the match."
            "Shou and Mayu were taken out but they did depower one GEAR. Aura struggles to hold off two GEARs at once."
            voice "audio/voice/E4/Mayu/D4/Mayu D4-15.ogg"
            ma "The situation is looking dire..."
            voice "audio/voice/E4/Shou/d4/21 Copy.ogg"
            ss "I guess that means we need to go for points then."
            voice "audio/voice/E4/Kaori/D4/Kaori_D4_25.ogg"
            ki "Agreed..."
            "Looks like REBORN's subs are no pushovers, even without Akira's support. They also anticipated our strategy and counter-played us. I suppose there's a reason they're always number one."
            "Aura charges the two remaining GEARs."
            "They send a volley of shots, which Aura is mostly able to avoid, but the hits she does take seem to cause decent damage."
            "As Aura approaches the first GEAR, her shield disappears and she readies her blade. She must have drained it completely and is channeling that energy into her strike. {w}She is ready to go down swinging!"
            voice "audio/voice/E4/Kaori/D4/Kaori_D4_26.ogg"
            ki "Hiyaaa!"
            stop music fadeout 3
            "Aura depowers as soon as her blade connects... but so does one of the enemy GEARs!"
            "In the end, the last GEAR left standing is one of REBORN."
            scene bg campus arena dusk with fade
            voice "audio/voice/E4/Announcer/D4/10.ogg"
            an "That was close..."
            voice "audio/voice/E4/Announcer/D4/11.ogg"
            an "...but in the end, it looks like REBORN's winning streak will continue!"
            play music "audio/music/Let's Get It Done! (GAME VERSION).ogg" fadein 3
            "The crowd erupts into cheers."
            voice "audio/voice/E4/Announcer/D4/12.ogg"
            an "But how about ACE-2049-11's performance?!"
            "The crowd cheers even louder."
            voice "audio/voice/E4/Announcer/D4/13.ogg"
            an "Talk about giving REBORN a run for their money!"
            "I stare in wonder at the animated audience. Although we didn't win, it warms my heart to see the strong support of the crowd."
            scene bg battleground dusk with dissolve
            "My teammates are silent through the comms. It's no surprise that REBORN won the match, but that doesn't make this loss sting any less."
    
    jump E4D4S3
