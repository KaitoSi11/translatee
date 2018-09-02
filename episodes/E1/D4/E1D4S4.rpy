label E1D4S4:
    
    
    #Show school arena
    scene white with fade
    scene bg campus arena day with Dissolve(2.5)
    "While in our GEAR, we walk into the circular arena."
    "Students, sponsors, professors, and other general spectators fill the stadium. A large screen displays our every move for those sitting in the back.{w} A hush falls over the crowd as we get into place."
    "The energy is a bit lower than usual for a live match… {w}Probably because this is technically still an examination."
    play music "audio/music/Fight Song 1 (GAME VERSION).ogg" fadein 1
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
    "Across from us, the four enemy AIs enter."
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
    voice "audio/voice/E1/D4/S4/Kaori/3.ogg"
    ki "Everyone good?"
    
    "The coms light up green again."
    $ E1D4S4matchPlan = 0

    
    menu:
        "The best way to help is if I stick with the plan. With me out of sight, I won't risk putting them into compromising positions that can cause loss of field advantage.":
            $ E1D4S4_FollowMatchPlan = 1
            scene bg campus arena day with fade
            "Following Kaori's plan, I hang back, away from the action."
            "My teammates get into position. Mayu falls behind Shou and Kaori, who lead the attack."
            "Kaori and Shou weave between the melee mechs and run interference, alternating blasts and defenses as distractions. Mayu darts from cover to cover, until she's in position. Then she lines up a sniper shot for the melee AI." 
            "For a while, they're able to keep up a rhythm."
            scene bg battleground day with fade
            $renpy.pause(.25, hard=True)
            show mayu mech at bl:
                xzoom -1
            show aiM att at br
            with dissolve
            
            show mayu att with dissolve
            $renpy.pause(.25)
            play sound "audio/sfx/GEAR Combat/Sniper.ogg"
            $renpy.pause(.5)
            play sound "audio/sfx/GEAR Combat/Hit.ogg"
            show aiM att at br, Shake(None, 1, dist=15)
            show aiM neu at br, Shake(None, 1, dist=15) with dissolve
            "A sudden high powered rail beam from Mayu instantly depowers one of the melee AIs."
            voice "audio/voice/E1/D4/S4/Shou/1.ogg"
            ss "Nice one, Mayu!"
            play sound "audio/sfx/GEAR Combat/Depower.ogg"
            hide aiM with dissolve
            voice "audio/voice/E1/D4/S4/Kaori/4.ogg"
            ki "Three more to go."
            show aiR att at tr behind mayu with dissolve:
                xzoom .7
                yzoom .7
            pf "Mayu, look out!"
            "The ranged AI locks onto Mayu. She runs for the only available cover, but doesn't make it in time."
            show shou att at cc behind mayu with dissolve:
                xzoom -.85
                yzoom .85
            "Just before the blast hits her, Shou intercepts the shot, taking the damage himself."
            play sound "audio/sfx/GEAR Combat/Rifle.ogg"
            $renpy.pause(.35)
            show shou att at cc, Shake(None, 1, dist=15) behind mayu
            show shou mech at cc, Shake(None, 1, dist=15) behind mayu with dissolve
            voice "audio/voice/E1/D4/S4/Shou/2.ogg"
            ss "Argh!"
            show mayu mech at bl with dissolve
            voice "audio/voice/E1/D4/S4/Mayu/1.ogg"
            ma "Shou!"
            voice "audio/voice/E1/D4/S4/Shou/6.ogg"
            ss "Sorry, I'm down."
            play sound "audio/sfx/GEAR Combat/Depower.ogg"  
            hide shou with dissolve
            voice "audio/voice/E1/D4/S4/Kaori/5.ogg"
            ki "Hyaahh!"
            show mayu mech at bl:
                parallel:
                    easein 1.5 alpha 1.0
                parallel:
                    easein 1.5 xoffset -1500
            play sound "audio/sfx/GEAR Combat/Sword Single.ogg"  
            show kaori att at tl with dissolve:
                xzoom -.7
                yzoom .7
            "Kaori dashes towards the range GEAR and takes it out with a single powerful swing."
            play sound "audio/sfx/GEAR Combat/Hit.ogg"  
            show aiR att at tr, Shake(None, 1, dist=15) with dissolve:
                xzoom .7
                yzoom .7
                xoffset 200
            $renpy.pause(1)
            show aiR neu at tr with dissolve:
                xzoom .7
                yzoom .7
                xoffset 0
            $renpy.pause(1)
            play sound "audio/sfx/GEAR Combat/Depower.ogg" 
            hide aiR with dissolve
            show kaori mech at tl with dissolve:
                xzoom -.7
                yzoom .7
            $renpy.pause(1)
            scene black with fade
            scene bg battleground day with fade
            show kaori mech at tr with dissolve:
                xzoom -.7
                yzoom .7
            show mayu mech at bl with dissolve:
                xzoom -1
            voice "audio/voice/E1/D4/S4/Mayu/2.ogg"
            ma "There's a Class A melee GEAR inbound for my location."
            voice "audio/voice/E1/D4/S4/Kaori/6.ogg"
            ki "Got it!"
            show kaori mech at tr with dissolve:
                xzoom .7
                yzoom .7
            show aiM att at mm with dissolve
            "As Kaori races towards her, Mayu dodges a swing from the enemy mech."
            play sound "audio/sfx/GEAR Combat/Sword Double.ogg" 
            play sound2 "audio/sfx/GEAR Combat/Dodge.ogg" 
            show mayu mech at bl:
                parallel:
                    easeout .75 alpha 1.0
                parallel:
                    easeout .75 xoffset -1300
            show aiM att at mm:
                parallel:
                    easeout .75 alpha 1.0
                parallel:
                    easeout .75 xoffset -1300
            $renpy.pause(1.5)
            voice "audio/voice/E1/D4/S4/Mayu/3.ogg"
            ma "Kaori, what's your ETA?"
            show kaori mech at tr with dissolve:
                xzoom .8
                yzoom .8
            voice "audio/voice/E1/D4/S4/Kaori/7.ogg"
            ki "Almost there--"
            pf "My radar just pinged. {w}The ranged GEAR is--Kaori!"
            show aiR att at tl with dissolve:
                xzoom -.7
                yzoom .7
            play sound2 "audio/sfx/GEAR Combat/Rifle.ogg" 
            $renpy.pause(.4)
            play sound "audio/sfx/GEAR Combat/Hit.ogg" 
            show kaori mech at tr, Shake(None, 1, dist=15) with dissolve:
                xzoom .8
                yzoom .8
                xoffset 150
                easeout .5 xoffset 250
            voice "audio/voice/E1/D4/S4/Kaori/8.ogg"
            ki "Kyaah!"
            "A flurry of beams zaps through Kaori's shield and depowers her GEAR. {w}The AI mech must have had repositioned itself to Kaori's minimally defended arc. {w}I don't think I've ever seen programmed GEARs do something so strategic."
            play sound "audio/sfx/GEAR Combat/Depower.ogg" 
            hide kaori with dissolve
            hide mayu
            hide aiM
            $renpy.pause(1.0)
            voice "audio/voice/E1/D4/S4/Mayu/4.ogg"
            ma "Sorry, I'm down too... I'm not kitted to handle melee engagements..."
            scene black with fade
            "With the rest of my team depowered, the remaining AI GEAR slowly turn to face me."
            scene bg battleground day with fade
            show mc mech at bl with dissolve:
                xzoom -1
            pf "So… about that plan…"
            show aiR att at tr with dissolve:
                xzoom .8
                yzoom .8
            show aiM att at br with dissolve
            voice "audio/voice/E1/D4/S4/Shou/3.ogg"
            ss "Um, maybe you can try to negotiate with them?"
            voice "audio/voice/E1/D4/S4/Kaori/9.ogg"
            ki "Stop joking around! We still need to boost our score. Go deal as much damage as you can."
            pf "Easier said than done."
            show mc ready at bl with dissolve:
                xzoom -1
            "I mumble to myself as I ready my fists for the impending combat."
    
            #"Gameplay, with only dodge/block options"
            # This just means just doing the reaction game with only dodge/block visuals/sounds
            #$ E1D4S4matchPlan = 0
            #$ survived = 0
            #$ context = "E1D4S4_MatchPlanComplete"
            #$ enemy = "aiM"
            #$ mode = "retreat"
            
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
            #show screen timer_scrReaction(place="E1D4S4_MatchPlanComplete")
            #jump qte_game
            # and jump here after finished
            
            
            
            
            "The AI GEARs waste no time and boost towards me with their weapons raised."

            
            label E1D4S4Combat1Loopback:
           
            
            $ qtetotal = 5
            $ t_var = qtetotal
            show screen timer_scr(place="E1D4S4_L1")
            menu:
                "Dodge!" if E1D4S4_LOOPINGMENU1 == 0:
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
                    
                    "Their blades swing through air as I dodge out of the way. While the first AI recovers from its miss, I punch it in the side. Its shield barely even shimmers from the impact!"
                    "The GEAR then smashes the butt of its sword into me, catching me off guard and causing more damage than I would have liked."
                    
                    show mc mech at bl:
                        xoffset 0
                    show aiM neu at br:
                        xoffset 0
                    with dissolve
                    $E1D4S4_LOOPINGMENU1=1
                    jump E1D4S4Combat1Loopback

                "Block!" if E1D4S4_LOOPINGMENU2 == 0:
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
                        xoffset 150
                        parallel:
                            easeout .3 alpha 1.0
                        parallel:
                            easeout .3 xoffset 0
                
                    "I raise my arm and strengthen my shield to block the attack, but I'm still driven back from the force of the double blow. Digging my heels into the ground, I barely have time to register the next oncoming attack!"
                    
                    show mc mech at bl:
                        xoffset 0
                    show aiM neu at br:
                        xoffset 0
                    with dissolve
                    $E1D4S4_LOOPINGMENU2=1
                    jump E1D4S4Combat1Loopback

                "Evade!" if E1D4S4_LOOPINGMENU3 == 0:
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
                            
                            
                    "I sidestep out of the way and their swords slice through empty air. Taking advantage of their moment for recovery, I land a punch to the side of one of the AIs, but my attack barely registers."
                    "The second AI strikes me, catching me unaware, and my shield flashes dangerously from the blow."
                    "This is not good!"
                    "The two AI quickly recover and aim for another attack!"
                    
                    show mc mech at bl:
                        xoffset 0
                    show aiM neu at br:
                        xoffset 0
                    with dissolve
                    $E1D4S4_LOOPINGMENU3=1
                    jump E1D4S4Combat1Loopback

                "Slow…":
                    label E1D4S4_L1:
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
                        xoffset 150
                        parallel:
                            easeout .3 alpha 1.0
                        parallel:
                            easeout .3 xoffset 0
                            
                            
                    "I'm too slow to react and my heels dig into the ground as I'm pushed back from the force of their attacks. My shield shimmers as it absorbs the blow."

            
            
            label E1D4S4_MatchPlanComplete:
                $renpy.pause(1.0)
                $ renpy.hide_screen ("battle_screen")
                $ E1D4S4matchPlan = survived
                show aiM neu at br with dissolve:
                    xoffset 0
                show mc ready at bl with dissolve:
                    xzoom -1
            "This is like our training match all over again. {w}I'm only able to hold out for a short time as most of my core energy is used to dodge two GEARs at once."
    
    
        "YOLO.":
            scene black with fade
            # show team, dissolve MC to disappear
            show bg battleground day with dissolve
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
            show mc ready at bl with dissolve
            pf "This is Eagle. I'm going in!"
            play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
            show mc ready at bl, Shake(None, 1, dist=20) behind kaori:
                xzoom -1
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1750
            $renpy.pause(.75)
            voice "audio/voice/E1/D4/S4/Kaori/10.ogg"
            ki "What?!"
            hide mc
            voice "audio/voice/E1/D4/S4/Mayu/5.ogg"
            ma "Wait--!"
            voice "audio/voice/E1/D4/S4/Shou/4.ogg"
            ss "Uh-oh."
            scene black with fade
            # show centered bg with mc shielding 
            show bg battleground day with dissolve:
                xzoom 1
                yzoom 1
                xoffset 0
                yoffset 0
            show mc ready at cc behind shou with dissolve:
                xzoom -.85
                yzoom .85
            "With my thrusters maxed, I boost into combat, fists ready to start scrapping metal."
            play sound "audio/sfx/GEAR Combat/Rifle.ogg"
            show mc blo at cc behind shou with Dissolve(.25):
                xzoom -.85
                yzoom .85
                
            play sound2 [ "audio/sfx/GEAR Combat/Block.ogg", "audio/sfx/GEAR Combat/Block.ogg", "audio/sfx/GEAR Combat/Block.ogg" ]
            show mc blo at cc, Shake(None, 1.5, dist=8) behind shou:
                xoffset 75
                xzoom -.85
                yzoom .85
            $renpy.pause(.20)
            play sound3 [ "audio/sfx/GEAR Combat/Block.ogg", "audio/sfx/GEAR Combat/Block.ogg" ]
            
            "A barrage of laser fire pours down on me. Eagle recommends evasive manoeuvres, but I ignore them and continue barrelling forward."
            voice "audio/voice/E1/D4/S4/EagleAI/10.ogg"
            GEARpf "Energy shield sustaining critical damage."
            # easin of shou and mayu at same time, stay by your side
            play sound "audio/sfx/GEAR Combat/SMG.ogg"
            "Suddenly, a wave of beams fly past me."
            show mayu att at tl behind mc with dissolve:
                xzoom -.7
                yzoom .7
            show shou att at bl with dissolve:
                xzoom -1
                yzoom 1
                
            "Mayu and Shou also boost at max speed, catching up with me, and provide suppressive fire. Kaori trails behind, conserving her energy."
            # show 2 enemy ai
            show aiR att at tr behind mc with dissolve:
                xzoom .7
                yzoom .7
            show aiM att at br with dissolve
            # slide mc offscreen further ahead
            play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
            show mc ready at cc, Shake(None, 1, dist=20) behind aiM:
                xzoom -.85
                yzoom .85
                xoffset 150
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1250
            $renpy.pause(1.0)
            "The opponents switch focus from me to my teammates."
            hide mc with dissolve
            # show melee ai getting rekt
            play sound2 "audio/sfx/GEAR Combat/SMG.ogg"
            $renpy.pause(.25)
            
            play sound "audio/sfx/GEAR Combat/Sniper.ogg"
            
            $renpy.pause(.35)
            play sound3 "audio/sfx/GEAR Combat/Hit.ogg"
            show aiM att at br, Shake(None, 1, dist=15) with dissolve
            play sound3 "audio/sfx/GEAR Combat/Depower.ogg"
            show aiM neu at br, Shake(None, 1, dist=15) with dissolve
            "The supportive fire from my teammates takes out a melee AI GEAR. Unfortunately, the excessive usage of energy on the thrusters alone critically weakens their shield output."
            hide aiM with dissolve
            # show mayu and shou getting rekt
            play sound3 "audio/sfx/GEAR Combat/Rifle.ogg"
            show mayu att at tl, Shake(None, 1, dist=15) behind shou:
                xzoom -.8
                yzoom .8
            show shou att at bl, Shake(None, 1, dist=15):
                xzoom -1
            with dissolve
            
            play sound "audio/sfx/GEAR Combat/Hit.ogg"
            $renpy.pause(.1)
            play sound2 "audio/sfx/GEAR Combat/Hit.ogg"
            show mayu mech at tl, Shake(None, 1, dist=15) behind shou:
                xzoom -.8
                yzoom .8
            show shou mech at bl, Shake(None, 1, dist=15):
                xzoom -1
            with dissolve
            
            "They do not last long under fire."
            play sound "audio/sfx/GEAR Combat/Depower.ogg"
            voice "audio/voice/E1/D4/S4/Mayu/6.ogg"
            ma "Sorry, I'm down."
            hide mayu with dissolve
            play sound "audio/sfx/GEAR Combat/Depower.ogg"
            voice "audio/voice/E1/D4/S4/Shou/5.ogg"
            ss "Same..."
            hide shou with dissolve
            # mc with his oppenents
            scene black with fade
            scene bg battleground day with dissolve
            show aiR neu at tr with dissolve:
                xzoom .8
                yzoom .8
            show aiM neu at br with dissolve
            "I finally reach my target!"
            show mc ready at bl with dissolve:
                xzoom -1
            pf "Alright let's do this--"
            "Suddenly, Eagle stops responding."
    
    voice "audio/voice/E1/D4/S4/EagleAI/11.ogg"
    GEARpf "Shields offline. Power core at 1\%."
    show mc mech at bl with dissolve:
        xzoom -1
    pf "{i}This is not good.{/i}"
    show aiM att at br with dissolve
    "The AI melee GEAR raises its blade."
    "Eagle's not responding..."
    stop music fadeout 3
    "Is this really how it'll end?"
    show aiM att at br with dissolve:
        parallel:
            easeout 1.0 alpha 1.0
        parallel:
            easeout 1.0 xoffset -500
    scene black with Dissolve(.5)
    $renpy.pause(2.0, hard=True)
    voice "audio/voice/E1/D4/S4/EagleAI/12.ogg"
    GEARpf "Emergency Power Core Protocol sequence initiated."
    play sound "audio/sfx/GEAR Combat/Overdrive Phase 1.ogg"
    scene white with Dissolve(.5)
    "In my cockpit, all the lights shine on at once. Statistics and numbers I've never seen before scroll across my displays."
    $ knockback = 0
    play sound2 "audio/sfx/GEAR Combat/Overdrive Phase 2.ogg"
    $ renpy.pause(1.0, hard=True)
    $ renpy.pause(1.4)
    "!!"
    
    play sound "audio/sfx/GEAR Combat/Overdrive Phase 3.ogg"
    $ persistent.gpix[7][0] = 1

    scene cg GEAR overdrive first with Shake((0, 0, 0, 0), 2.5, dist=20):
        xalign 0.5
        yalign 0.5
        xzoom 1.1
        yzoom 1.1
        
    "A thunderous boom catches my attention and a surge of explosive energy shoves the attacking AI GEAR ten feet away. I look out and see a shallow crater around Eagle."


    scene bg battleground day
    show aiR neu at tr:
        xzoom .8
        yzoom .8
    show aiM att at mm
    show mco blo at bl:
        xzoom -1
        xoffset 150
    with Dissolve(.05)
    
    #play sound "audio/sfx/GEAR Combat/Overdrive Phase 3.ogg"
    show aiR neu at tr, Shake(None, 1, dist=10):
        xzoom .8
        yzoom .8
        xoffset 200
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset 300
    show aiM att at mm, Shake(None, 1, dist=15):
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset 450
    with Shake((0, 0, 0, 0), 1.0, dist=10)
    #"A thunderous boom catches my attention and a surge of explosive energy shoves the attacking AI GEAR ten feet away. I look out and see a shallow crater around Eagle."
    $renpy.pause(0.5)
    voice "audio/voice/E1/D4/S4/EagleAI/13.ogg"
    GEARpf "Protocol sequence complete. Energy output over 9000."
    play music "audio/music/Raycrash (GAME VERSION).ogg" fadein 1
    show mco mech at bl with Dissolve(1.5):
        xzoom -1
        xoffset 0
    show aiM neu with dissolve
    $ renpy.pause(.25)

    pf "What."
    
    show aiM att at br with Dissolve(1):
        xoffset 0
    voice "audio/voice/E1/D4/S4/EagleAI/14.ogg"
    GEARpf "No external weaponry detected. Activating Energy Fists."
    play sound "audio/sfx/GEAR Combat/Energy Fist Activation.ogg"
    show mco neuFist with Dissolve(2.5):
        xoffset -150
        xzoom -1
    "Eagle's arms glow faintly."
    
    voice "audio/voice/E1/D4/S4/EagleAI/15.ogg"
    GEARpf "Engaging enemy GEAR."
    hide aiR with dissolve
    $ context = "E1D4S4_FirstTarget"
    $ enemy = "aiM"
    $ mode = "overdrive"
    $ survived = 0
    
    $ mcEnergyMax = 9000
    $ mcEnergy = 9000
    $ enemyHPMax = 500
    $ enemyHP = 500
    
    $ qtebase = 10
    $ qtereaction = qteath + qtetrack + qtebase
    $ qtetotal = qtereaction
    $ t_var = qtereaction
    
    $ E1D4S4Score = 0
    #"Simulator starts, only good options, even if you time out, only good options."
    # This means only using attack/dodge visuals/sounds, no blocks. Use 'survived' to add to this sequence's score
    show screen battle_screen
    #show screen timer_scrReaction(place="E1D4S4_FirstTarget")
    jump qte_game
    label E1D4S4_FirstTarget:
        $ knockback = 0
        $renpy.pause(1)
        hide aiM with dissolve
        $ renpy.hide_screen ("battle_screen")
        show mco neuFist at bl with dissolve:
            xzoom -1
            xoffset 0
        $renpy.pause(1)
        show aiR neu at br with dissolve:
            xzoom 1
            yzoom 1
            
        voice "audio/voice/E1/D4/S4/EagleAI/16.ogg"
        GEARpf "GEAR destroyed. Engaging secondary target."

    $ qtebase = 10
    $ qtereaction = qteath + qtetrack + qtebase
    $ qtetotal = qtereaction
    $ t_var = qtereaction
    
    $ mcEnergyMax = 9000
    $ mcEnergy = 9000
    $ enemyHPMax = 500
    $ enemyHP = 500
    
    $ context = "E1D4S4_SecondTarget"
    $ enemy = "aiR"
    #$ survived = 0
    #"Simulator starts, only good options, even if you time out, only good options."
    # This means only using attack/dodge visuals/sounds, no blocks. Use 'survived' to add to this sequence's score
    show screen battle_screen
    #show screen timer_scrReaction(place="E1D4S4_SecondTarget")
    jump qte_game
    label E1D4S4_SecondTarget:
        $ knockback = 0
        $renpy.pause(1)
        hide aiR with dissolve
        show mco neuFist at bl with dissolve:
            xzoom -1
            xoffset 0
        $renpy.pause(1)
        $ renpy.hide_screen ("battle_screen")
        pf "This is awesome!"
        voice "audio/voice/E1/D4/S4/EagleAI/17.ogg"
        GEARpf "Power core can no longer sustain output. Eagle de-powering."
        show mco mech with dissolve
        $renpy.pause(.5)
        
    $ E1D4S4Score += survived
    stop music fadeout 5
    # Let's make a total score for the episode's story
    $ E1Score = 0
    # and add all the possible scores they could've gotten so far
    #$ E1Score = E1D4S4Score + E1D4S4matchPlan + teamPractice + practiceScore
    
    if (E1D4S4_FollowMatchPlan == 1):
        pf "Whew... just barely managed to pull that off."
    
    else:
        show bg battleground day:
            linear .5 xoffset 200
        show mco mech at bl:
            xzoom -1
            linear .5 xoffset 1000

        show aiM att at bl:
            xoffset -1000
            xzoom -1
            easeout .5 xoffset 0
        pf "Wait! There's still one left!"
        
        show aiM att at bl behind mco:
            easeout .5 xoffset 400
        "The final target charges my unresponsive GEAR."
        show kaori att at bl behind aiM:
            xoffset -1000
            xzoom -1
            easeout .25 xoffset -100
        play sound "audio/sfx/GEAR Combat/Sword Single.ogg"
        
        $renpy.pause(.25)
        show aiM att at bl, Shake(None, 1, dist=15) behind mco:
            easeout .5 xoffset 400
        play sound2 "audio/sfx/GEAR Combat/Hit.ogg"
        

        voice "audio/voice/E1/D4/S4/Kaori/5.ogg"
        ki "Hyahh!"
        
        play sound2 "audio/sfx/GEAR Combat/Depower.ogg"
        hide aiM with dissolve
        
        "Kaori appears and takes out the GEAR with one swooping blow."
        show kaori mech at bl with dissolve
    $renpy.pause(.25)
    
    play music "audio/music/Victory! (GAME VERSION).ogg"
    $renpy.pause(.5)
    voice "audio/voice/E1/D4/S4/ACE Academy Announcer/1.ogg"
    an "Qualifer match complete. Please exit the arena with your GEAR."
    $renpy.pause(1)
    "The crowd is quiet for a moment, before erupting in deafening cheers."
    $renpy.pause(1.0)
    #fade to black, fade in arena BG with pilot sprites
    scene black with Dissolve(2.5)
    $renpy.pause(1)
    stop music fadeout 3
    $renpy.pause(1)
    scene bg campus arena day at Zoom((1920, 1080), (0, 0, 2376, 1180), (0, 0, 2376, 1180), 0) with Dissolve(2.5)
    
    $ mcEnergyMax = 200
    $ mcEnergy = 200
    
    jump E1D4S5