#
label E2D2S2:

    $ shoOut = "sGym"
    "We quickly change into our uniforms, then Shou and I head towards the gym."
    scene white with fade
    scene bg campus gym day with dissolve
    $renpy.pause(1)
    "Even with all of the training equipment inside, the space still feels huge. Flags and banners from past victories hang on the walls and ceiling."

    "Typical of ACE Academy, everything looks pristine."
    
    voice "audio/voice/E2/D2/Shou/13.ogg"
    ss "Helloooo?"
    play music "audio/music/Bright New Day (GAME VERSION).ogg"
    show shou cur at cc with dissolve
    "Shou's voice snaps me back to reality."

    pf "Yeah, what's up?"
    show shou ske at cc
    voice "audio/voice/E2/D2/Shou/14.ogg"
    ss "Geez! Zoning out like that when I'm asking you such an important question... It's almost like you don't care."
    pf "Sorry, what did you ask?"
    show shou smi at cc
    voice "audio/voice/E2/D2/Shou/15.ogg"
    ss "What's your favourite flavor of dango?"
    "I think he and I have different definitions of what is an \"important\" question."
    pf "Uhh, I suppose it's--"
    "Something in my peripheral vision distracts me from answering."
    pf "Woah!"
    "A group of girls enter the gym wearing nothing but their panties and a t-shirt! This can't be right. {w}I rub my eyes but the magical sight remains in full focus."
    pf "What's going on?"
    show shou cur at cc
    voice "audio/voice/E2/D2/Shou/16.ogg"
    ss "Huh?"
    pf "The girls over there are just walking around in their panties!"
    show shiny:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou sur at cc with dissolve
    $renpy.pause(1)
    show shou neu at cc
    "Shou glances excitedly, but deflates a second later."
    show shou ske at cc
    voice "audio/voice/E2/D2/Shou/17.ogg"
    ss "What are you talking about, broseph?"
    pf "How are you not seeing this?"
    show question:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D2/Shou/18.ogg"
    ss "See what? Girls wearing their gym uniforms?"
    pf "It's incredibly revealing!"
    show shou neu at cc
    show dots:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    "Shou stares for a moment."
    voice "audio/voice/E2/D2/Shou/19.ogg"
    ss "I still don't get it. That's what they've always worn... ever since elementary school..."
    show shou thi at cc
    voice "audio/voice/E2/D2/Shou/20.ogg"
    ss "... Actually, now that you mention it..."
    show shou thi b1 at cc with dissolve
    "I watch as Shou's face reddens."
    show shou sur b1 at cc
    show shocked:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D2/Shou/21.ogg"
    ss "My god! What have you done?"
    show shou wor b1 at cc
    show panic:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D2/Shou/22.ogg"
    ss "... I won't be able to focus in this class anymore!"
    pf "Come on, I couldn't have been the only one seeing this."
    show shou sur b1 at cc
    voice "audio/voice/E2/D2/Shou/23.ogg"
    ss "You were! I was desensitized to this from childhood because my memories never associated this attire with perversion, and thus, there was nothing to be perverted about!"
    pf "What the heck are you talking about?"
    show shou wor b1 at cc
    show confused:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D2/Shou/24.ogg"
    ss "I DON'T KNOW, MAN. I'M TOO DISTRACTED TO THINK CLEARLY."
    $renpy.pause(1)
    stop music fadeout 3
    voice "audio/voice/E2/D2/S2/Kaori/14.ogg"
    ki "What are you two yelling about?"
    
    $ kaoOut = "sGym"
    $ kaoHairF = "tied"
    $ kaoHairB = "tied"
    
    hide shou with dissolve
    
    show kaori neu at l2
    show shou cur at r2:
        xzoom -1
    with dissolve
    "We both spin around and see Kaori. She's also wearing what no one in their right mind would dub a gym \"uniform\". {w}Her porcelain legs are completely free of blemish, and the way the material shows off her body makes it clear she works hard to stay fit."
    show kaori cur at l2
    voice "audio/voice/E2/D2/S2/Kaori/15.ogg"
    ki "Uh..."

    menu:
        "How can she wear something like this?!":
            play music "audio/music/Isnt This Nice (GAME VERSION).ogg"
            pf "I never expected you to wear something so revealing, Kaori."
            show kaori ske at l2
            "She quirks an eyebrow, her hand instinctively going to her hip."
            voice "audio/voice/E2/D2/S2/Kaori/16.ogg"
            ki "Huh? What are you talking about?"
            pf "Your pants...{w} Or rather, the lack thereof."
            show dots:
                xoffset 365
                yoffset 110
                xzoom .75
                yzoom .75
            "She looks down for a second before shooting me an unimpressed glare."
            show kaori dis at l2
            voice "audio/voice/E2/D2/S2/Kaori/17.ogg"
            ki "This gym uniform offers the most range of motion."
            pf "I... suppose that makes sense. {w}What do you think, Shou?"
            show confused:
                xoffset 1040
                yoffset 20
                xzoom .75
                yzoom .75
            "Shou doesn't respond. I'm sure he's been zoned out for the last few minutes just staring at her. Kaori shifts uncomfortably, tucking one leg behind the other."
            show kaori ang at l2
            voice "audio/voice/E2/D2/S2/Kaori/18.ogg"
            ki "Shou!"
            show kaori ann at l2
            "Kaori stomps forward and slugs Shou on the arm."
            show kaori ang at l2
            show shou sur at r2
            voice "audio/voice/E2/missing/kaori/stop_Kaori.ogg"
            ki "Stop!"
            show shou wor at r2
            voice "audio/voice/E2/D2/Shou/25.ogg"
            ss "H-Hey! Why are you only mad at me? He was doing it too!"


            if E1D4S3_Stare == 1:
                "Shou glances at me. I grin before repeating his own words back to him."
                pf "You've got to \"sneak a peek\", my man. Can't be so obvious about it."

            show kaori ang at l2
            show vein:
                xoffset 365
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D2/S2/Kaori/19.ogg"
            ki "He's just an idiot. {i}You{/i} are doing it because you're a pervert!"
            show kaori ann at l2
            show shou neu at r2
            "Shou crosses his arms defiantly."
            voice "audio/voice/E2/D2/Shou/26.ogg"
            ss "{i}Just{/i} because I admire the female figure from a safe distance away without their knowledge does not make me a pervert!"
            pf "...You're really not helping your case."
            show shou smi at r2

        "Swiggity swooty, I'm coming for that booty.":
            play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 3
            "Shou and I continue to stare. She steps back in confusion."
            show kaori ske at l2
            voice "audio/voice/E2/D2/S2/Kaori/20.ogg"
            ki "What's wrong with you guys?"
            pf "Uh, Kaori."
            voice "audio/voice/E2/D2/S2/Kaori/21.ogg"
            ki "Hm?"
            pf "I think you dropped your hairband."
            show question:
                xoffset 365
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D2/S2/Kaori/22.ogg"
            ki "Huh? I didn't bring a hairband."
            pf "Then what's that?"
            # something visual to this?
            "I point to the floor behind her. She turns around revealing a delectably fine backside."
            show shoBlush:
                xoffset 1040
                yoffset 20
                xzoom .75
                yzoom .75
            show shou sur b1 at r2 with dissolve

            ss "!!"
            show kaori dis at l2
            voice "audio/voice/E2/D2/S2/Kaori/23.ogg"
            ki "I don't see anything."
            show shou smi at r2 with dissolve
            "I offer a fist bump to Shou, who happily reciprocates."
            pf "Sorry, my mistake."
            show kaori ske at l2
            "Kaori turns to face us. She raises an eyebrow at our grinning faces, slightly irritated."
            voice "audio/voice/E2/D2/S2/Kaori/24.ogg"
            ki "You two are acting weirder than normal..."

        "Her exercise routine is yielding superb results.":
            play music "audio/music/Bright New Day (GAME VERSION).ogg"
            "If I ever had any doubt about Kaori's physical prowess, I don't have them anymore."
            pf "It must take hard work and discipline to have a body like yours."
            show kaori dis b1 at l2 with dissolve
            "She frowns as a hand instantly goes to her side. The only thing betraying her unimpressed expression is the slight pink creeping into her cheeks."
            voice "audio/voice/E2/D2/S2/Kaori/25.ogg"
            ki "Are you really trying to hit on me with a line like that?"

            menu:
                "No, just giving credit where it's due.":
                    pf "You can take it however you want. It's just impressive to see someone diligent with their training."
                    show kaori thi b2 at l2 with dissolve
                    show tsuBlush:
                        xoffset 365
                        yoffset 110
                        xzoom .75
                        yzoom .75
                    "Kaori crosses her arms as the pink on her cheek deepens."
                    voice "audio/voice/E2/D2/S2/Kaori/26.ogg"
                    ki "Thanks, I guess."
                    show shou smi at r2

                "Of course!":
                    pf "Depends, is it working?"
                    voice "audio/voice/E2/D2/S2/Kaori/27.ogg"
                    ki "No."
                    pf "Not even a little?"
                    #show kaori neu at l2
                    voice "audio/voice/E2/D2/S2/Kaori/28.ogg"
                    ki "Not even at all."
                    pf "That's cold."
                    show kaori smi b1 at l2 with dissolve
                    "Despite her shut down, the corner of her lips tug into a faint smile."
                    show shou smi at r2

                "Ha, you wish.":
                    pf "Don't flatter yourself."
                    voice "audio/voice/E2/D2/S2/Kaori/29.ogg"
                    ki "Good, one perverted idiot is enough."
                    show kaori ann at l2 with dissolve
                    show shou neu at r2 with dissolve
                    "Kaori's gaze flicks to Shou. He crosses his arms defensively."
                    voice "audio/voice/E2/D2/Shou/28.ogg"
                    ss "Why you gotta be so rude? Don't you know I'm human too?"
                    show shou smi at r2

        "She must be a fetish model." if (E1D4S3_Stare == 1):
            play music "audio/music/Baka! (GAME VERSION).ogg"
            pf "Ooooooohhh!"
            voice "audio/voice/E2/D2/S2/Kaori/30.ogg"
            ki "Huh?"
            pf "Let me guess, you have a maid outfit and a naughty nurse costume hidden in your closet too? {w}This is all starting to make sense. First it was your pilot outfit and now gym uniform... {w}I just never would have thought someone like Kaori would be in that line of work."
            show kaori sur b1 at l2 with dissolve
            show shoBlush:
                xoffset 365
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori sur b2 at l2 with dissolve
            "Kaori's mouth hangs opens as her face reddens."
            show kaori ang b3 at l2 with dissolve
            voice "audio/voice/E2/D2/S2/Kaori/31.ogg"
            ki "W-Wha...What are you saying?! Y-You are a special kind of idiot to say something so perverted!"
            show kaori ann b2 at l2 with dissolve
            show shou mis b1 at r2 with dissolve
            voice "audio/voice/E2/D2/Shou/29.ogg"
            ss "You know, it is starting to make a lot more sense now."
            show shou hap b1 at r2
            "With eyes closed, Shou rubs his chin as if he's contemplating some great revelation."
            # shake animation?
            play sound "audio/sfx/Human/Med_Punch.ogg"
            show shou sur at r2
            with Shake((0, 0, 0, 0), .7, dist=10)
            "{i}WHAM!{/i}"
            show shou win at r2
            "{color=#FFBF00}[pfull]{/color} // {color=#01DF3A}Shou Shinjirou{/color}" "Ouch!"
            show kaori ang b2 at l2
            voice "audio/voice/E2/D2/S2/Kaori/32.ogg"
            ki "This is a new low, even for you!"
            show kaori ann b2 at l2
            show shou neu at r2
            "Even with her hostile glare, Kaori's blushy, pouty face is strangely cute."

            menu:
                "Apologize for being mean.":
                    pf "Sorry, Kaori, it was just a joke."
                    show kaori dis b1 at l2 with dissolve
                    voice "audio/voice/E2/D2/S2/Kaori/33.ogg"
                    ki "Well, it wasn't a funny one."
                    pf "I know, I know. Sorry again."
                    voice "audio/voice/E2/D2/Shou/31.ogg"
                    ss "Yeah, me too."
                    show kaori thi b1 at l2
                    voice "audio/voice/E2/D2/S2/Kaori/34.ogg"
                    ki "Fine, whatever."
                    
                "Pat the little cutie on the head!":
                    pf "D'awww, sowwie Kaowee."
                    "I go to pat Kaori on the head--"
                    with Shake((0, 0, 0, 0), .5, dist=4)
                    pf "Ack!"
                    show shocked:
                        xoffset 1040
                        yoffset 20
                        xzoom .75
                        yzoom .75
                    show shou sur at r2
                    "--when a surging pain in my wrist stops me. Kaori grabs my arm before it reaches her, and puts me in a painful lock."
                    show kaori ang b1 at l2 with dissolve
                    voice "audio/voice/E2/D2/S2/Kaori/35.ogg"
                    ki "I'll show you sorry!"
                    show kaori ann at l2
                    with Shake((0, 0, 0, 0), .5, dist=4)
                    "She nudges her hand forward causing another rush of pain to flow through me."
                    pf "Okay! I'm sorry for real!"
                    show frightful:
                        xoffset 1040
                        yoffset 20
                        xzoom .75
                        yzoom .75
                    show shou wor at r2
                    voice "audio/voice/E2/D2/Shou/32.ogg"
                    ss "Yes, me too! Just please spare the unenlightened fool!"
                    "I rub my aching wrist as soon as she releases my arm."
                    pf "Remind me never to mess with you again."
                    show kaori dis at l2
                    voice "audio/voice/E2/D2/S2/Kaori/36.ogg"
                    ki "At least you're learning."
                    show shou neu at r2
                    "She's a feisty one, I'll give her that."

    # pause and music change?
    stop music fadeout 3
    $renpy.pause(1)
    
    show kaori neu at l2 with dissolve
    show dots:
        xoffset 1040
        yoffset 20
        xzoom .75
        yzoom .75
    show dots2:
        xoffset 365
        yoffset 110
        xzoom .75
        yzoom .75
    
    $renpy.pause(1)
    "A few moments go by as we wait for class to start."
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 1
    pf "By the way, have you guys thought about what we should do for sponsorship?"
    voice "audio/voice/E2/D2/Shou/33.ogg"
    ss "Not quite."
    voice "audio/voice/E2/D2/S2/Kaori/37.ogg"
    ki "No."
    show shou sur at r2
    "Shou and I both glance at Kaori in surprise, and she crosses her arms."
    show kaori ske at l2
    voice "audio/voice/E2/D2/S2/Kaori/38.ogg"
    ki "What?"
    show shou cur at r2
    voice "audio/voice/E2/D2/Shou/34.ogg"
    ss "You're usually on top of this stuff."
    show kaori thi at l2
    voice "audio/voice/E2/D2/S2/Kaori/39.ogg"
    ki "I've been busy! This team isn't the only thing I focus on."
    show shou neu at r2
    "Before Shou can say anything else, I intervene."
    pf "That's okay. I might have a lead anyway."
    show kaori cur at l2
    voice "audio/voice/E2/D2/S2/Kaori/40.ogg"
    ki "Really?"
    "She doesn't need to sound so surprised."
    pf "Yeah. You know the SBA?"
    show kaori neu at l2
    "They both nod."
    pf "I know somebody who works for them. She's agreed to help us find a sponsor."
    show shou smi at r2
    "Shou claps me on the back."
    show shou mis at r2
    voice "audio/voice/E2/D2/Shou/35.ogg"
    ss "This is why I chose {i}you{/i} to join our team! You make things happen."
    pf "Are you sure it's not because I was the only person available?"
    show kaori mis at l2
    "Kaori snorts, but Shou is unfazed."
    show shou hap at r2
    voice "audio/voice/E2/D2/Shou/36.ogg"
    ss "That too."
    show shou smi at r2
    "Shou is about to speak again when Kaori shushes him."
    show kaori neu at l2
    voice "audio/voice/E2/D2/S2/Kaori/41.ogg"
    ki "Be quiet! Class is about to start."
    "The professor waits for the room to quiet down before he begins the class."
    ### NOTE SFX - coach whistle blowing?
    stop music fadeout 5
    #Gym Class Start
    scene black with fade
    #timeskip
    $renpy.pause(2.5)
    #Gym Class End
    scene bg campus gym day with fade

    "The professor dismisses the class, and the three of us file out together."
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1

    if MCStory != 1:
        show shou sad at r2 with dissolve:
            xzoom -1
        "My muscles are already fatigued and my limbs tremble. I know I'm going to be sore tomorrow."
        show shou win at r2
        "Shou groans."
        show crying:
            xoffset 1040
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/D2/Shou/37.ogg"
        ss "My legs feel like they're on fire."
        show shou sad at r2
        "I grunt in sympathy, too tired to respond."
        show kaori neu at l2 with dissolve
        "Kaori power-walks ahead of us."
        voice "audio/voice/E2/D2/S2/Kaori/42.ogg"
        ki "Class wasn't that hard."
        show shou neu at r2
        "Shou and I stare at each other. I whisper to him."
        pf "How is she doing that right now?"
        voice "audio/voice/E2/D2/Shou/38.ogg"
        ss "She's a cyborg, a human-mecha hybrid."
        pf "Makes sense to me."

    elif MCStory == 1:
        show kaori neu at l2 with dissolve
        "I haven't had such a fantastic workout since coming to Japan. I'm totally in my element. {w}Kaori keeps pace with me, looking just as refreshed as I do."
        voice "audio/voice/E2/D2/Shou/39.ogg"
        ss "I am dead. 'Tis the end for me. I bid you good morrow."
        show shou win at r2 with dissolve:
            xzoom -1
        "I look back and see Shou sluggishly trailing behind us."
        pf "Uh, what's up with him?"
        "Kaori doesn't even look back."
        show kaori dis at l2
        show shou sad at r2
        voice "audio/voice/E2/D2/S2/Kaori/43.ogg"
        ki "Serves him right. That's what happens when you pig out on junk food all day."
        show shou wor at r2
        voice "audio/voice/E2/D2/Shou/40.ogg"
        ss "I promise I'll work harder!"
        show kaori thi at l2
        voice "audio/voice/E2/D2/S2/Kaori/44.ogg"
        ki "He always says that, but he never does."
        show crying:
            xoffset 1040
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/D2/Shou/41.ogg"
        ss "Goodbye, cruel world!"
        show shou sad at r2
        pf "... Seriously, I think we should check on him."
        voice "audio/voice/E2/D2/S2/Kaori/45.ogg"
        ki "Fine."
        voice "audio/voice/E2/D2/Shou/42.ogg"
        ss "My broseph, I don't know how you're keeping up with Kaori. That is unpossible."
        show kaori dis at l2
        voice "audio/voice/E2/D2/S2/Kaori/46.ogg"
        ki "{i}Impossible.{/i}"
        show shou neu at r2
        voice "audio/voice/E2/D2/Shou/43.ogg"
        ss "That's what I said."
        "I scratch the back of my head."
        pf "It's not really that tough. You just have to keep working at it until it gets easier."
        show kaori mis at l2
        "Kaori looks over at me, I think she looks... impressed?"
        pf "Anyways, let's get out of here."
        "Shou nods and summons up a second wind as we make our way to the exit."

    stop music fadeout 3
    scene black with fade
    play ambient "audio/ambience/Campus.ogg" fadein 1
    
    $ kaoOut = "sUniform"
    $ kaoHairF = renpy.random.choice(['default'])
    $ kaoHairB = kaoHairF
    
    $ shoOut = "sUniform"
    
    scene bg campus building day with fade
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
    show kaori neu at l2
    show shou neu at r2:
        xzoom -1
    with dissolve
    "Once we're outside, Shou waves goodbye."
    show shou smi at r2
    voice "audio/voice/E2/D2/Shou/44.ogg"
    ss "Well that was fun. I got some stuff to take care of, though. I'll catch you on the flip-side, Kaori, Mr. Broseph."
    voice "audio/voice/E2/D2/S2/Kaori/47.ogg"
    ki "Same. I'll talk to you guys later."
    "We all say goodbye."

    hide kaori
    hide shou
    with dissolve
    
    scene black with fade
    $renpy.pause(1)
    scene bg campus main day with fade

    $ freeTime = "afternoon"
    
    call E2FreeTime from _call_E2FreeTime_6

    jump E2D2S3
