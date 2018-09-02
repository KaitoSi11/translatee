#
label E4D2S1:
    
    $ kaoHairF = "tied"
    $ kaoHairB = kaoHairF
    $ kaoOut = "outdoor"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "outdoor"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "outdoor"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "outdoor"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "Camp No Bag"
    
    $ day = 2
    $ timeSpent = "none"
    $renpy.pause(1)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1)
    #beep beep beep
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(2.5)
    stop sound
    scene bg homekaito myroom day with fade
    
    "I wake up at the first sound of my alarm and jump out of bed. I need to meet my friends at the train station so we can all head over to the hot springs together, and I'd rather not be the last one there. They might leave without me. {w}Just kidding--no they wouldn't… {w}would they?"
    "Either way, I throw on some clothes and race to pack up what I need."
    $renpy.pause(1)
    play ambient "audio/ambience/Train Station.ogg" fadein 3
    scene bg travel trainstation day with fade
    "After grabbing a quick breakfast, I hop on my bike and drive to the train station. {w}I haven't been back here since my arrival to Isokaze. It's exactly the same as I remember it. People bustle back and forth and the whole station is blanketed with the buzz of conversations."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    "For some reason, the familiarity is comforting."
    
    "I purchase my ticket and find Kaori, Mayu, Valerie, and Yuuna are already waiting on the platform."
    show yuuna neu at l3 with dissolve:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show mayu neu at l2 behind yuuna with dissolve:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show valerie neu at l1 with dissolve:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show kaori neu at r1 with dissolve:
        xoffset -75
        xzoom -0.75
        yzoom 0.75
    pf "Hey."
    show mayu smi
    show valerie smi
    show yuuna smi
    "Yuuna and Valerie wave as I approach while Mayu smiles and Kaori nods in greeting."
    voice "audio/voice/E4/Yuuna/E4/D2/1.ogg"
    ym "You made it."
    pf "So did you."
    "I glance around us."
    pf "Where's Shou?"
    show storm:
        xoffset 925
        yoffset 110
        xzoom .5
        yzoom .5
    show kaori dis
    voice "audio/voice/MISSING/BATCH5/k_redo_12.ogg"
    ki "Running late, like usual."
    voice "audio/voice/E4/Mayu/D2/Mayu D2-01.ogg"
    ma "He'll be here."
    pf "I hope so… He has all our tickets."
    show kaori ann
    "Kaori gives me a look."
    pf "I mean, of course he'll be here!"
    show kaori dis
    "She crosses her arms but otherwise falls silent. Even Yuuna looks worried as she checks the time. We've still got a few minutes before the train comes."
    "As the seconds tick by, even I'm beginning to lose hope. Thankfully, Shou soon appears."
    show kaori dis:
        xzoom 0.75
        yzoom 0.75
    show shou smi at r3:
        xoffset 100
        xzoom -0.75
        yzoom 0.75
    with dissolve
    voice "audio/voice/E4/Shou/d2/1 Copy.ogg"
    ss "Hey guys! Ready to get our heat on?"
    show mayu neu
    show yuuna thi
    show valerie ske
    "We stare at Shou."
    show shou thi
    voice "audio/voice/E4/Shou/d2/2 Copy.ogg"
    ss "Uh, that came out wrong."
    pf "Yeah…"
    show shou hap
    "He looks around, a wide grin on his face."
    show mayu smi
    show yuuna neu
    show valerie neu
    voice "audio/voice/E4/Shou/d2/3 Copy.ogg"
    ss "Awesome! The gang's all here!"
    "The laborious roar of engines is heard before the train is sighted. Shou points to the approaching train."
    show shou smi
    voice "audio/voice/E4/Shou/d2/4 Copy.ogg"
    ss "Just in time too, because there's the train."
    voice "audio/voice/MISSING/BATCH5/k_redo_13.ogg"
    ki "You were cutting it really close, Shou."
    show note:
        xoffset 1475
        yoffset 20
        xzoom .5
        yzoom .5
    show shou mis
    voice "audio/voice/E4/Shou/d2/5 Copy.ogg"
    ss "I'm right on time!"
    "Everyone quiets down as we get ready to board. We settle into our seats and enjoy the ride."
    
    stop ambient fadeout 3
    #black screen
    scene black with fade
    $renpy.pause(1)
    play ambient "audio/ambience/Morning.ogg" fadein 3
    scene bg vacation nature day with fade
    "When we arrive, we step off the train and stretch our legs. There's a beautiful hotel in the distance and the hot springs are tucked in the mountains behind it."
    show shou smi at l3 with dissolve
    voice "audio/voice/E4/Shou/d2/6 Copy.ogg"
    ss "Alright! Here we are safe and sound. Let's go check-in first."
    hide shou with dissolve
    "Shou leads the way to the hotel and we trail behind, enjoying the scenery. I breathe in deeply, letting the crisp mountain air fill my lungs. Just being here already helps me feel rejuvenated!"
    scene black with fade
    stop ambient fadeout 3
    "We enter the hotel and the front desk agent gives us the keys to our rooms. Valerie and Yuuna are bunking together while Kaori and Mayu share a room. Obviously, that leaves Shou and I to share the last room."
    "The girls disappear into their rooms, but not before agreeing to meet right outside the hotel in ten minutes. Shou and I enter our room. He immediately flops onto the bed closest to the window."
    ### NOTE - do we have a BG planned for this?
    scene bg vacation hotel day with fade # not perfect, but what was suggested
    show shou mis at cc with dissolve
    voice "audio/voice/E4/Shou/d2/7 Copy.ogg"
    ss "I claim this bed!"
    
    menu:
        "I'll take the other bed.":
            pf "Alright, I'm fine with this bed."
            "I drop my bag onto the bed closest to the wall and doorway."
            pf "I don't like being next to the window anyway. Even with the curtains closed I still feel too exposed."
            show shou ner
            voice "audio/voice/E4/Shou/d2/8 Copy.ogg"
            ss "Exposed?"
            pf "Like if I were to open the curtains a face would be staring in."
            show shou wor
            "Shou looks warily at the window."
            show drop:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Shou/d2/9 Copy.ogg"
            ss "Don't say things like that! Do you want me to have nightmares?"
            pf "Sorry!"
    
        "That's my bed.":
            pf "Why did you just jump on my bed?"
            show shou hap
            voice "audio/voice/E4/Shou/d2/10 Copy.ogg"
            ss "You can't have this bed. I claimed it!"
            "I nod solemnly, my face grave."
            pf "There's only one way to settle this."
            show shou ske
            voice "audio/voice/E4/Shou/d2/11 Copy.ogg"
            ss "Are you saying what I think you're saying?"
            "I nod."
            show shou mis
            voice "audio/voice/E4/Shou/d2/12 Copy.ogg"
            ss "I won't go easy on you."
            pf "Best two out of three?"
            show shou hap
            voice "audio/voice/E4/Shou/d2/13 Copy.ogg"
            ss "Right."
            "We both hold up fists and get in position for rock, paper, scissors."
            show shou mis
            voice "audio/voice/E4/Shou/d2/14 Copy.ogg"
            ss "Jan ken pon!"
            pf "Jan ken pon!"
            "I throw out paper and Shou throws out rock."
            show panic:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            show shou wor
            voice "audio/voice/E4/Shou/d2/15 Copy.ogg"
            ss "No!"
            pf "That bed is as good as mine."
            show shou smi
            voice "audio/voice/E4/Shou/d2/16 Copy.ogg"
            ss "It's not over yet."
            "We get into position again."
            show shou mis
            voice "audio/voice/E4/Shou/d2/17 Copy.ogg"
            ss "Jan ken pon!"
            pf "Jan ken pon!"
            "This time Shou throws out rock and I throw out scissors."
            show shou hap
            voice "audio/voice/E4/Shou/d2/18 Copy.ogg"
            ss "Ha! You won't take that bed away from me so easily."
            pf "We'll see."
            "We're both tied 1-1 and this last round will determine the winner. We ready ourselves one last time…"
            show shou mis
            voice "audio/voice/E4/Shou/d2/19 Copy.ogg"
            ss "Jan ken pon!"
            pf "Jan ken pon!"
    
            # QTE
            $ qtebase = 3
            $ qtetotal = qteath + qtebase
            $ t_var = qtetotal
            show screen timer_scr(place="E4D2S1_Default")
            
            menu:
                "Rock!":
                    $ renpy.hide_screen ("timer_scr")
                    "I throw down rock while Shou throws down scissors."
                    jump E4D2S1_Win
                
                "Paper!":
                    $ renpy.hide_screen ("timer_scr")
                    "I throw down paper while Shou throws down scissors."
                    jump E4D2S1_Lose
            
                "Scissors!":
                    $ renpy.hide_screen ("timer_scr")
                    "I throw down scissors while Shou also throws down scissors."
                    "We immediately go again."
                    
                    # QTE
                    $ qtebase = 3
                    $ qtetotal = qteath + qtebase
                    $ t_var = qtetotal
                    show screen timer_scr(place="E4D2S1_Default")
                    
                    menu:
                        "Rock!":
                            label E4D2S1_Default:
                                $ renpy.hide_screen ("timer_scr")
                                "I throw down rock while Shou throws down paper."
                                jump E4D2S1_Lose
                        
                        "Paper!":
                            $ renpy.hide_screen ("timer_scr")
                            "I throw down paper while Shou throws down scissors."
                            jump E4D2S1_Lose
                        
                        "Scissor!":
                            $ renpy.hide_screen ("timer_scr")
                            "I throw down scissors while Shou throws down paper."
                            jump E4D2S1_Win
    
            label E4D2S1_Win:
                show shocked:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                show shou sur
                voice "audio/voice/E4/Shou/d2/20 Copy.ogg"
                ss "Noooo! How could this happen?"
                pf "Destiny is on my side."
                show shou sad
                "Shou sighs deeply as he slides off the bed."
                
                menu:
                    "Let Shou keep the bed.":
                        "I can't help feeling a little guilty. Do I really want to sleep in this bed so badly?"
                        pf "Hey, if you really want the bed you can have it."
                        show shou smi at l3 with dissolve
                        voice "audio/voice/E4/Shou/d2/21 Copy.ogg"
                        ss "No way, broseph! You earned the bed."
                        "Shou settles onto the other bed, squirms around a bit, then grins."
                        show shou hap
                        voice "audio/voice/E4/Shou/d2/22 Copy.ogg"
                        ss "This one will work just fine."
                        "I shrug."
                        pf "If you say so."
                        jump E4D2S1_Conver
                    
                    "I won this bed fair and square.":
                        show shou sad at l3 with dissolve
                        "I wait for Shou to get off the bed before settling in."
                        pf "Ahhh, so comfy."
                        show shou thi
                        voice "audio/voice/E4/Shou/d2/23 Copy.ogg"
                        ss "Only because I already softened it up for you."
                        show shou neu
                        "He settles onto the other bed, squirms around a bit, then grins."
                        show shou smi
                        voice "audio/voice/E4/Shou/d2/24 Copy.ogg"
                        ss "This one's even more comfortable than the other. You can keep that bed."
                        pf "Oh, I will."
                        jump E4D2S1_Conver
            
            label E4D2S1_Lose:
                pf "I was so close!"
                show shou hap
                "Shou grins."
                voice "audio/voice/E4/Shou/d2/25 Copy.ogg"
                ss "What I didn't tell you was that I was the Jan Ken Pon champ back in high school."
                pf "You had way too much time on your hands."
                show note:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                show shou mis
                voice "audio/voice/E4/Shou/d2/26 Copy.ogg"
                ss "Says the guy who lost."
                "Shou flops back down onto the bed, while I set my bag onto mine."
                jump E4D2S1_Conver
                
    label E4D2S1_Conver:
    scene black with fade
    stop music fadeout 3
    $renpy.pause(1)
    play ambient "audio/ambience/Morning.ogg" fadein 3
    scene bg vacation nature day with fade
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
    show shou neu at r3 with dissolve:
        xoffset 100
        xzoom -0.75
        yzoom 0.75
    "Once we've had a chance to rest and put down our things, we head down into the lobby and wait outside. The girls trickle in a few minutes later."
    show yuuna neu at l3 with dissolve:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show mayu neu at l2 behind yuuna  with dissolve:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show valerie neu at l1 with dissolve:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show kaori neu at r1 behind shou with dissolve:
        xoffset -75
        xzoom -0.75
        yzoom 0.75
    pf "Should we go for a soak now?"
    show shou smi
    voice "audio/voice/E4/Shou/d2/27 Copy.ogg"
    ss "We'll want to save that for tonight. Trust me, it's way more relaxing at the end of the day."
    pf "What should we do instead?"
    show shou thi
    voice "audio/voice/E4/Shou/d2/28 Copy.ogg"
    ss "Hmm…"
    show shou neu
    show mayu wor
    "Shou pulls out the tickets and studies the text on there."
    voice "audio/voice/E4/Mayu/D2/Mayu D2-02.ogg"
    ma "Um, what about…"
    show dots:
        xoffset 315
        yoffset 135
        xzoom .5
        yzoom .5
    show mayu ner
    "Mayu's voice trails off."
    pf "What about what?"
    show mayu neu
    voice "audio/voice/E4/Mayu/D2/Mayu D2-03.ogg"
    ma "What if we toured the gardens?"
    "She points to a side clearing of blossoms and trees."
    show heart:
        xoffset 30
        yoffset 100
        xzoom .5
        yzoom .5
    show yuuna hap
    show valerie smi
    voice "audio/voice/E4/Yuuna/E4/D2/2.ogg"
    ym "They look really pretty!"
    show shou smi
    show mayu smi
    voice "audio/voice/E4/Shou/d2/29 Copy.ogg"
    ss "We get a discounted price for the tours too since we already have tickets to the hot springs."
    show yuuna smi
    show valerie hap
    "Valerie jumps excitedly."
    show note:
        xoffset 590
        yoffset 125
        xzoom .5
        yzoom .5
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L1.ogg"
    vb "Let's do it then!"
    show kaori cur
    hide valerie
    with dissolve
    "She races towards the gardens."
    show shocked:
        xoffset 925
        yoffset 110
        xzoom .5
        yzoom .5
    show kaori sur
    voice "audio/voice/E4/Kaori/D2/Kaori_19_d1.ogg"
    ki "Wait! Don't just run off like that!"
    hide kaori with dissolve
    hide shou
    hide mayu
    hide yuuna
    with dissolve
    "Kaori takes off after her as the rest of us scramble to catch up."
    
    $renpy.pause(0.5)
    scene bg isokaze park2 day with dissolve
    
    "Luckily, we arrive right before the next scheduled tour and we are all able to secure a spot with the group. The tour guide leads us on a gravel path and speaks non-stop about the history of the garden and each plant that we see."
    
    if MCStory == 2:
        "I listen intently as he talks about the original lord who commissioned the garden as a way to show off his status and wealth. I remember learning about this same guy in our Foreign International Bridging class so it's extra cool to be standing in his garden."
        "The guide's lecture on each plant that we pass is far less engaging, though, and my attention wanes."
    
    else:
        "The history stuff is kind of cool. I wish I had the money to commission my own garden paradise, but does this guy really have to go into detail about every single plant?"
        
    scene bg vacation nature day with dissolve
    
    
    
    "I survey the flowers and trees around me. Bright petals of colour sway gently in the breeze and a few of them float towards our feet. I wonder how they keep this place so green at this time of year…"
    
    if kaorelatonship == 1:
        jump E4D2KI
    elif mayrelatonship == 1:
        jump E4D2MA
    elif valrelatonship == 1:
        jump E4D2VB
    elif yuurelatonship == 1:
        jump E4D2YM
    else:
        jump E4D2SS

