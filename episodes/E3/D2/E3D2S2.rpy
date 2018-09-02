#
label E3D2S2:
    voice "audio/voice/E3/D2/S2/yuuna/1.ogg"
    ym "Hey everyone!"
    show yuuna hap at r1 with dissolve:
        xoffset -75
        xzoom -0.75
        yzoom 0.75
        
    show kaori cur
    show nikki cur:
        xzoom -0.75
    show shou sur
    show mayu cur
    with dissolve
    "We collectively turn around at the sound of Yuuna's voice. I want to respond to her, but my voice gets caught in my throat. {w}Never before have I been so thankful that the bikini was invented. Judging by the silence, everyone is as entranced as I am."
    show dots:
        xoffset 925
        yoffset 100
        xzoom .5
        yzoom .5
    show yuuna ner
    stop music fadeout 10
    "Yuuna fidgets under our gaze and automatically wraps an arm around herself."
    show yuuna wor
    voice "audio/voice/E3/D2/S2/yuuna/2.ogg"
    ym "Um… Is everything alright?"
    show nikki ner
    "Like everyone else, Nikki's gaze is fixated on Yuuna. She looks down at her own chest, then back at Yuuna, and sighs."
    show storm:
        xoffset 1250
        yoffset 160
        xzoom .5
        yzoom .5
    show nikki sad
    show mayu neu
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_047.ogg"
    sf "Life is so unfair."
    show panic:
        xoffset 925
        yoffset 100
        xzoom .5
        yzoom .5
    show yuuna sur b1
    voice "audio/voice/E3/D2/S2/yuuna/3.ogg"
    ym "W-What?"
    
    if E2MAS4_Completed == 0:
        show exclamation:
            xoffset 1550
            yoffset 110
            xzoom .5
            yzoom .5
        show kaori sur
        "Kaori snaps back to reality and hits me hard."
        show kaori ang at r3 with dissolve:
            xoffset 200
            xzoom -1
            yzoom 1
        show nikki sur
        # screen shake?
        play sound "audio/sfx/Human/light_punch.ogg"
        pf "Ow!"
        show mayu wor
        
        play music "audio/music/Baka! (GAME VERSION).ogg" fadein 5
        voice "audio/voice/E3/D2/S2/kaori/e3d2_Kao_06.ogg"
        ki "Stop being a pervert!"
        show kaori ann
        show nikki ner
        show yuuna wor b1
        
        menu:
            "I saw you looking.":
                pf "You were staring too!"
                show kaori ske b1
                voice "audio/voice/E3/D2/S2/kaori/e3d2_Kao_07.ogg"
                ki "N-No!"
                show kaori ske b2 with dissolve
                "Her cheeks flare, betraying her guilt."
                show tsuBlush:
                    xoffset 1375
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori thi b2
                voice "audio/voice/E3/D2/S2/kaori/e3d2_Kao_08.ogg"
                ki "I wouldn't do something like that!"
        
            "Don't be jealous.":
                pf "Sorry, Kaori, I didn't mean to make you feel left out. There was just so much excitement when you showed up that I didn't get a chance to… appreciate you."
                show kaori sur b1
                "Kaori throws an arm protectively around her chest."
                show kaori ang b2
                voice "audio/voice/E3/D2/S2/kaori/e3d2_Kao_09.ogg"
                ki "Don't look at me!"
                show kaori ann b2
                voice "audio/voice/E3/D2/S2/kaori/e3d2_Kao_10.ogg"
                ki "You are just as bad as that guy with the camera."
                pf "No, I'm not. You're {i}obviously{/i} not underage."
                show kaori thi b2
                "She turns away from me."
                show kaori ann b2
                voice "audio/voice/E3/D2/S2/kaori/e3d2_Kao_11.ogg"
                ki "S-Stop that!"
        
            "What's with the hitting?":
                "I rub at the sore spot."
                pf "Geez, Kaori, why do you always have to resort to violence?"
                show kaori dis
                "She crosses her arms."
                voice "audio/voice/E3/D2/S2/kaori/e3d2_Kao_12.ogg"
                ki "It's the only way to knock some sense into you."
                show nikki neu
                "Nikki nods along."
                voice "audio/voice/E3/D2/S2/nikki/Nikki_2_049.ogg"
                sf "Ain't that the truth."
                show kaori cur
                "Kaori looks at Nikki with interest."
                
        show kaori neu at r3 with dissolve:
            xoffset 200
            xzoom -0.75
            yzoom 0.75
        show nikki neu
        show yuuna sad b1
        "Yuuna tries to cover up, clearly mortified."
        voice "audio/voice/E3/D2/S2/yuuna/4.ogg"
        ym "You guys…"
        show mayu thi
        "Shou stands in a daze until Mayu pokes him."
        show shou cur
        voice "audio/voice/E3/D2/S2/mayu/Mayu-07.ogg"
        ma "I see."
        show shou ske
        voice "audio/voice/E3/D2/S2/shou/17.ogg"
        ss "Huh?"
        show mayu ner b1
        "She glances down and shuffles her feet."
        voice "audio/voice/E3/D2/S2/mayu/Mayu-08.ogg"
        ma "So that's what you like…"
        show shou wor b1
        voice "audio/voice/E3/D2/S2/shou/18.ogg"
        ss "N-No, that's not it! I like yours too!"
        show mayu cur b1
        "Mayu looks up at Shou with wide eyes, then covers herself with her hands."
        show shoBlush:
            xoffset 30
            yoffset 135
            xzoom .5
            yzoom .5
        show mayu sur b2
        voice "audio/voice/E3/D2/S2/mayu/Mayu-09.ogg"
        ma "Ah! S-Stop looking!"
        show shou sur b2
        "Shou's face burns red and he trips over his words."
        show kaori dis
        voice "audio/voice/E3/D2/S2/shou/19.ogg"
        ss "Wait! No! I didn't mean it like that! I promise I'm not looking!"
        show mayu cur b2
        "Mayu continues to stare at him with doe eyes."
        show panic:
            xoffset 315
            yoffset 20
            xzoom .5
            yzoom .5
        show shou wor b2
        stop music fadeout 5
        voice "audio/voice/E3/D2/S2/shou/20.ogg"
        ss "But not because yours aren't good, because they're great!"
        show kaori ann
        play sound "audio/sfx/Human/Hand Slap.ogg"
        show shou sur b1
        "Kaori marches over and whacks Shou on the back of the head."
        show shou win b1
        voice "audio/voice/E3/D2/S2/shou/21.ogg"
        ss "Ow!"
        show mayu wor b1
        "She hovers protectively over Mayu."
        show kaori dis
        show crying:
            xoffset 315
            yoffset 20
            xzoom .5
            yzoom .5
        show shou sad
        voice "audio/voice/E3/D2/S2/kaori/e3d2_Kao_13.ogg"
        ki "C'mon, Mayu."
        show mayu ner b1
        voice "audio/voice/E3/D2/S2/mayu/Mayu-10.ogg"
        ma "O-Okay…"
        
    else:
        show mayu neu at l3 with dissolve:
            xoffset -200
            xzoom 1
            yzoom 1
        show shou sur behind mayu
        with dissolve
        play sound "audio/sfx/Human/Poke Noise.ogg"
        "A gentle poke to my side snaps me back to reality."
        pf "Huh?"
        show mayu thi
        voice "audio/voice/E3/D2/S2/mayu/Mayu-11.ogg"
        ma "I see..."
        pf "See what?"
        show mayu ner b1
        "She glances down and shuffles her feet."
        voice "audio/voice/E3/D2/S2/mayu/Mayu-12.ogg"
        ma "So that's what you like..."
        
        menu:
            "N-No! You have it all wrong.":
                "I quickly shake my head."
                pf "No, I don't like them!"
                show yuuna sad
                "Yuuna frowns."
                pf "Wait, I mean I like them, but I like yours too!"
                show mayu cur b1
                show yuuna ner
                "Mayu looks at me with wide eyes, then quickly covers herself with her hands."
                show shoBlush:
                    xoffset 30
                    yoffset 135
                    xzoom .75
                    yzoom .75
                show mayu sur b2
                voice "audio/voice/E3/D2/S2/mayu/Mayu-13.ogg"
                ma "S-Stop!"
                show shou ske
                "Shou shakes his head."
                show mayu ner b2
                voice "audio/voice/E3/D2/S2/shou/22.ogg"
                ss "Broseph, have you learned nothing?"
                show kaori dis
                "The girls continue to watch me warily."
                pf "I'm not--"
                "I decide it's best not to say anything more just in case they spin it on me again. {w}I sigh."
                show mayu smi b1
                pf "Nevermind."
        
            "I can't fight how I've been biologically wired.":
                pf "Well, I mean given a choice, I would definitely--"
                show kaori ang at r3 with dissolve:
                    xoffset 200
                    xzoom -1
                    yzoom 1
                # screen shake?
                play sound "audio/sfx/Human/light_punch.ogg"
                "Kaori hits me hard on my shoulder."
                show mayu sur
                pf "Ow!"
                voice "audio/voice/E3/D2/S2/kaori/e3d2_Kao_14.ogg"
                ki "Stop being a pervert!"
                show kaori ann
                show mayu wor
                "She hovers protectively over Mayu."
                voice "audio/voice/E3/D2/S2/kaori/e3d2_Kao_15.ogg"
                ki "Don't listen to him Mayu, he's an idiot."
                show mayu neu
                "Mayu nods. They turn away after one last glare."
        
            "What are you talking about?":
                pf "Huh? I don't follow."
                show mayu thi b1
                voice "audio/voice/E3/D2/S2/mayu/Mayu-14.ogg"
                ma "Umm... you know..."
                pf "I really don't."
                show shocked:
                    xoffset 30
                    yoffset 135
                    xzoom .75
                    yzoom .75
                show mayu sur b1
                "Mayu's eyes widen."
                voice "audio/voice/E3/D2/S2/mayu/Mayu-15.ogg"
                ma "Really?"
                pf "Seriously, what are you talking about?"
                show mayu smi b1
                "She smiles."
                show drop:
                    xoffset 30
                    yoffset 135
                    xzoom .75
                    yzoom .75
                show mayu hap
                voice "audio/voice/E3/D2/S2/mayu/Mayu-16.ogg"
                ma "Nothing!"
        
    show kaori neu
    show mayu ner at l3:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show nikki smi
    show shou neu
    show yuuna ner
    with dissolve
    
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
    
    "Nikki grabs my arm and pulls me over to Yuuna, who still looks nervous."
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_050.ogg"
    sf "You're being so rude, big bro! You didn't even introduce me to your friend!"
    show nikki neu
    pf "Oh, right, this is my sister, Nikki."
    show yuuna smi
    "Yuuna smiles, clearly relieved."
    show mayu neu
    voice "audio/voice/E3/D2/S2/yuuna/5.ogg"
    ym "I'm Yuuna. Nice to meet you!"
    show nikki smi
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_051.ogg"
    sf "Nice to meet you too! Sorry about earlier…"
    show yuuna hap
    "Yuuna waves away the apology."
    voice "audio/voice/E3/D2/S2/yuuna/6.ogg"
    ym "It's fine."
    show nikki neu
    show yuuna smi
    voice "audio/voice/E3/D2/S2/yuuna/7.ogg"
    ym "So, where are we sitting?"
    "I'm about to answer when a sudden weight on my back throws me off balance."
    
    stop music fadeout 1
    
    
    $ qtebase = 3
    $ qtetotal = qteath + qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E3D2S2_Fall")
    
    menu:
        "{color=#00ff00}{b}Don't fall!{/b}{/color}" if MCStory == 1:
            $ renpy.hide_screen ("timer_scr")
            $ E3D2S2_Balance = 1
            
        "Don't fall!" if MCStory != 1:
            $ renpy.hide_screen ("timer_scr")
            $ E3D2S2_Balance = 1
    
        "Fall!":
            label E3D2S2_Fall:
                $ renpy.hide_screen ("timer_scr")
                $ E3D2S2_Balance = 0
    
        "Stumble!":
            $ renpy.hide_screen ("timer_scr")
            $ E3D2S2_Balance = 0
    
        "Yell!":
            $ renpy.hide_screen ("timer_scr")
            $ E3D2S2_Balance = 0
    
        "Stand!":
            $ renpy.hide_screen ("timer_scr")
            $ E3D2S2_Balance = 1
            
    show nikki cur
    show mayu cur
    show shou cur
    show yuuna sur
    
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 10
    
    if E3D2S2_Balance == 1:
        "I catch whoever is on my back as two slender arms snake around my neck. A lock of blonde hair falls before my eyes as Valerie presses her cheek against me."
    
    else:
        "With a yelp, I lose my footing and we both topple onto the sand, with her still on my back. A lock of blonde hair brushes my cheek as Valerie leans over to look at me."
        
    show valerie smi at l1
    show mayu neu
    show nikki ner
    show shou sur behind valerie
    show yuuna ner
    with dissolve
    voice "audio/voice/E3/D2/S2/valerie/E3D2L1.ogg"
    vb "Did you miss me?"
    show kaori ann at r3
    "Kaori marches over and confronts Valerie before I can respond."
    show shou cur
    voice "audio/voice/E3/D2/S2/kaori/e3d2_Kao_16.ogg"
    ki "What do you think you're doing?"
    show valerie hap
    voice "audio/voice/E3/D2/S2/valerie/E3D2L2.ogg"
    vb "Claiming my spot."
    show nikki dis
    "Nikki crosses her arms and pouts at Valerie."
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_052.ogg"
    sf "Do you always jump on the first guy you see?"
    "I'm surprised by the disapproval dripping in her voice."
    show valerie mis at l1:
        xoffset 50
        xzoom 0.75
        yzoom 0.75
        
    show kaori dis at r3
    show shou cur behind valerie
    with dissolve
    "Valerie slides off of me and gives me a wink."
    voice "audio/voice/E3/D2/S2/valerie/E3D2L3.ogg"
    vb "Just the cute ones."
    show shou hap
    show valerie smi
    "Shou grins."
    show nikki neu
    voice "audio/voice/E3/D2/S2/shou/23.ogg"
    ss "Then you should have jumped on me instead."
    show valerie cur
    "She presses a finger to her lips and looks innocently at Shou."
    voice "audio/voice/E3/D2/S2/valerie/E3D2L4.ogg"
    vb "Oh! I thought Mayu would have already done that."
    show mayu sur b1
    show shou sur b1
    voice "audio/voice/E3/D2/S2/mayu/Mayu-17.ogg"
    ma "Eh?!"
    voice "audio/voice/E3/D2/S2/shou/24.ogg"
    ss "We're just friends!"
    show mayu ner b1
    show shou ner b1
    "Mayu tries to hide the blush from her face, while Shou interjects."
    show valerie mis
    "Valerie grins impishly."
    voice "audio/voice/E3/D2/S2/valerie/E3D2L5.ogg"
    vb "Ohhh, well, if that's the case..."
    show shou cur
    show valerie hap
    "She jumps back to her feet."
    show mayu sur b1
    voice "audio/voice/E3/D2/S2/valerie/E3D2L6.ogg"
    vb "Get ready because you're next!"
    show shou sur b1
    voice "audio/voice/E3/D2/S2/shou/25.ogg"
    ss "W-Wha...?! Are you serious?"
    "Shou's face is a mixture of trepidation and hope as Valerie readies herself to leap."
    
    if E2MAS4_Completed == 0:
        stop music fadeout 1
        show exclamation:
            xoffset 30
            yoffset 135
            xzoom .5
            yzoom .5
        show mayu ang b1
        voice "audio/voice/E3/D2/S2/mayu/Mayu-18.ogg"
        ma "No!"
        $renpy.pause(1)
        show kaori cur
        show mayu sur b1
        show nikki cur
        show shou sur b2
        show valerie cur
        with dissolve
        show dots:
            xoffset 30
            yoffset 135
            xzoom .5
            yzoom .5
        "Everyone stares at Mayu, who is frozen, stunned by her own outburst."
        show mayu ner b1
        voice "audio/voice/E3/D2/S2/mayu/Mayu-19.ogg"
        ma "I-I mean… Um…"
        show mayu wor b2
        voice "audio/voice/E3/D2/S2/mayu/Mayu-20.ogg"
        ma "Mmmmmm...."
        show mayu win b2
        voice "audio/voice/E3/D2/S2/mayu/Mayu-21.ogg"
        ma "Mmmmmmmmmmm!"
        show confused:
            xoffset 30
            yoffset 135
            xzoom .5
            yzoom .5
        show mayu win b3
        show shou wor b1
        show valerie hap
        "Her cheeks steadily burn red as she struggles to find her words. {w}Valerie laughs and pats Mayu on the head."
        show note:
            xoffset 590
            yoffset 125
            xzoom .5
            yzoom .5
        voice "audio/voice/E3/D2/S2/valerie/E3D2L7.ogg"
        vb "I was just kidding! No need to get so worked up."
        show mayu sad b2
        "Mayu pouts."
        voice "audio/voice/E3/D2/S2/mayu/Mayu-22.ogg"
        ma "I-I wasn't worked up..."
        show kaori neu
        show mayu sad b1
        show nikki neu
        show shou ner
        show valerie cur
        
        play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
        
        "She gently moves away from Valerie, whose gaze is now firmly fixed on Yuuna."
        
    else:
        show valerie neu
        "Right before she jumps, Valerie pauses and glances at Mayu."
        show valerie ske
        voice "audio/voice/E3/D2/S2/valerie/E3D2L8.ogg"
        vb "Really?"
        show mayu cur
        "Mayu blinks."
        voice "audio/voice/E3/D2/S2/mayu/Mayu-23.ogg"
        ma "Huh?"
        show mayu neu
        show shou ske
        show valerie thi
        voice "audio/voice/E3/D2/S2/valerie/E3D2L9.ogg"
        vb "Oh, nevermind. Just kidding Shou, I already made my choice for today."
        show valerie mis
        "Valerie winks at me, and I blush."
        show shou sad
        voice "audio/voice/E3/D2/S2/shou/26.ogg"
        ss "Aw, you got my hopes up..."
        show shou neu
        show valerie hap
        "Valerie laughs and is about to reply when her attention locks onto Yuuna."

    show valerie sur
    show yuuna cur
    voice "audio/voice/E3/D2/S2/valerie/E3D2L10.ogg"
    vb "Oh my god!"
    "Valerie hops closer to Yuuna and leans towards her chest."
    show mayu neu
    show valerie mis
    voice "audio/voice/E3/D2/S2/valerie/E3D2L11.ogg"
    vb "Where have you been hiding these this whole time?"
    show yuuna sur b1
    "Yuuna's mouth hangs open in shock."
    show shou mis
    voice "audio/voice/E3/D2/S2/shou/27.ogg"
    ss "I would like to know this too."
    show kaori ann
    show shou sur
    "Kaori bats Shou on the arm."
    show vein:
        xoffset 1550
        yoffset 110
        xzoom .5
        yzoom .5
    show kaori ang
    ### VOICE - originally read "I thought I told you to stop being a pervert!" but voice gave "STOP. BEING. A. PERVERT."
    voice "audio/voice/E3/D2/S2/kaori/e3d2_Kao_17.ogg"
    ki "STOP. BEING. A. PERVERT."
    show kaori ann
    show shou win
    voice "audio/voice/E3/D2/S2/shou/28.ogg"
    ss "Ow! I'm sorry! I couldn't help it."
    show yuuna thi b1
    show shou sad
    "Yuuna's desperately trying to cover herself."
    show drop:
        xoffset 925
        yoffset 100
        xzoom .5
        yzoom .5
    voice "audio/voice/E3/D2/S2/yuuna/8.ogg"
    ym "Can we please focus on something else?"
    show mayu thi
    show shou neu
    show valerie smi
    voice "audio/voice/E3/D2/S2/mayu/Mayu-24.ogg"
    ma "Yeah, I think that's a good idea."
    show kaori neu
    show nikki smi
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_053.ogg"
    sf "Me too!"
    show shou thi
    voice "audio/voice/E3/D2/S2/shou/29.ogg"
    ss "Sure."
    show yuuna neu
    "Shou seems a little reluctant in his agreement."
    show mayu smi
    voice "audio/voice/E3/D2/S2/mayu/Mayu-25.ogg"
    ma "So, um, where are we going to sit?"
    show shou neu
    pf "Oh. Nikki and I already started setting up right here…"
    show nikki neu
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_054.ogg"
    sf "It's not too close and not too far from the water."
    show yuuna smi
    voice "audio/voice/E3/D2/S2/yuuna/9.ogg"
    ym "Sounds good to me."
    show shou smi
    "Everyone nods and begins to lay out their towels."
    
    #fade to black
    scene black with fade
    #fade in, all set up
    scene bg vacation beach day with fade:
        xzoom 1
        yzoom 1
        xalign .01
        yalign .99
        
    "We're lounging on our towels enjoying the sun, when a sharp squeal interrupts the tranquility."
    voice "audio/voice/E3/D2/S2/hstu3f/1_FHS.ogg"
    hstu3f "Nikki!"
    show nikki hap at cc with dissolve
    "Nikki bolts upright and waves to her friends as they race towards her."
    show highschoolgirl extra at l3
    show highschoolgirl2 extra at r3
    with dissolve
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_055.ogg"
    sf "You're here!"
    voice "audio/voice/E3/D2/S2/hstu3f/2_FHS.ogg"
    hstu3f "Of course. We said we were going to be, didn't we?"
    show nikki neu
    "The friend lowers her voice."
    voice "audio/voice/E3/D2/S2/hstu1f/1.ogg"
    hstu1f "Are you hanging out with your brother?"
    "Uh oh…"
    show nikki ske
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_056.ogg"
    sf "Yeah…?"
    voice "audio/voice/E3/D2/S2/hstu1f/2.ogg"
    hstu1f "Ooh, is he going to come with us to the temple?"
    show nikki dis
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_057.ogg"
    sf "No."
    voice "audio/voice/E3/D2/S2/hstu3f/3_FHS.ogg"
    hstu3f "Aww, why not?"
    show storm:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_058.ogg"
    sf "He's busy!"
    "The two girls stare at me."
    voice "audio/voice/E3/D2/S2/hstu3f/4_FHS.ogg"
    hstu3f "He doesn't look busy."
    "One of the friends kneels down and grabs my arm."
    pf "Hey!"
    voice "audio/voice/E3/D2/S2/hstu1f/3.ogg"
    hstu1f "You should come! It'll be so fun!"
    "The other friend grabs my other arm."
    voice "audio/voice/E3/D2/S2/hstu3f/5_FHS.ogg"
    hstu3f "Yeah! You can walk with me."
    voice "audio/voice/E3/D2/S2/hstu1f/4.ogg"
    hstu1f "What? No, I got here first!"
    "Oh god, not again…"
    voice "audio/voice/E3/D2/S2/hstu3f/6_FHS.ogg"
    hstu3f "So? He obviously prefers me."
    voice "audio/voice/E3/D2/S2/hstu1f/5.ogg"
    hstu1f "No! He--"
    show nikki ann
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_059.ogg"
    sf "What is wrong with you two?!"
    "Nikki steps in and drags the two girls off of me. They blink at her in surprise."
    voice "audio/voice/E3/D2/S2/hstu1f/6.ogg"
    hstu1f "I don't understand… Didn't you say you and he don't--"
    show vein:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_060.ogg"
    sf "Yes!"
    voice "audio/voice/E3/D2/S2/hstu1f/7.ogg"
    hstu1f "Then why are you so upset?"
    show nikki ang
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_061.ogg"
    sf "Because he's my brother!"
    "They look at each other and seem to come to an understanding."
    show nikki ann
    voice "audio/voice/E3/D2/S2/hstu3f/7_FHS.ogg"
    hstu3f "Ohhhh, he doesn't know."
    show nikki ske
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_062.ogg"
    sf "Huh?"
    pf "What don't I know?"
    voice "audio/voice/E3/D2/S2/hstu3f/8_FHS.ogg"
    hstu3f "That Nikki really mmmmff--"
    show nikki thi
    "Nikki claps her hand over her friend's mouth."
    show drop:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_063.ogg"
    sf "Haha what a couple of weirdos, am I right?"
    hide highschoolgirl
    hide highschoolgirl2
    with dissolve
    "She pulls the girls roughly to their feet, much to their dismay, and pushes them away from me."
    show nikki neu
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_064.ogg"
    sf "Gee, look at the time! We better get going!"
    show nikki smi
    voice "audio/voice/E3/D2/S2/nikki/Nikki_2_065.ogg"
    sf "I'll get a ride back with these two so I'll see you at home. Byeee!"
    hide nikki with dissolve
    "I hear faint protests from Nikki's friends as she hurries them away."
    
    jump E3D2S3
