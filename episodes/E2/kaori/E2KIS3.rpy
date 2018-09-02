#
label E2KIS3:
    
    $ kaoOut = "sUniform"
    
    #Event 3 - Afternoon Choice (>65 Points) EXCEPT DAY 5
    stop ambient fadeout 3
    stop music fadeout 3   
    "I should check up on Eagle and see how bad the damage really is. Hopefully it'll still be in fighting form even without the repairs from a sponsor."
    scene black with fade
    $renpy.pause(1)
    play ambient "audio/ambience/Hangar.ogg" fadein 3
    scene bg campus hangar day with fade
    "When I arrive in the Hangar, I see a familiar face. Kaori is circling her GEAR with a critical eye."
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
    show kaori neu at cc with dissolve
    "I guess we had the same idea."
    
    pf "Hey, Kaori."
    "She nods at me."
    pf "How does it look?"
    show kaori thi at cc
    "Kaori looks solemn."
    voice "audio/voice/E2/Free/KI/43.ogg"
    ki "It could be better. The damage is mostly cosmetic, but there is some damage here and here which could impact performance."
    "She points to the areas on her GEAR."
    show kaori neu at cc
    voice "audio/voice/E2/Free/KI/44.ogg"
    ki "This will reduce overall acceleration and top speed. It hurts the aerodynamic nature of Aura."
    pf "Aura?"
    voice "audio/voice/E2/Free/KI/45.ogg"
    ki "Yeah, Aura, the name of my GEAR."
    "I suddenly remember a conversation I had with Shou regarding GEARs and their genders."
    
    menu:
        "Is it a \"he\"?":
            pf "Is Aura a male GEAR?"
            show kaori ske at cc
            voice "audio/voice/E2/Free/KI/46.ogg"
            ki "Huh? Male? Why would it be male?"
            pf "Er."
            show kaori thi at cc
            "Kaori turns to face Aura."
            show question:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/Free/KI/47.ogg"
            ki "How in the world does that look like a \"he\" to you?"
            pf "I suppose you're right. So it's a \"she\" then?"
            show kaori neu at cc
            "Kaori nods."
    
        "Is it a \"she\"?":
            pf "Is Aura a female?"
            show kaori smi at cc
            voice "audio/voice/E2/Free/KI/48.ogg"
            ki "Well, the GEAR is an embodiment of a pilot so, yes."
    
        "Is it an \"it\"?":
            pf "Is Aura an \"it\"?"
            show kaori ske at cc
            "She raises an eyebrow."
            voice "audio/voice/E2/Free/KI/49.ogg"
            ki "What do you mean by \"it\"?"
            pf "You know, being an inanimate object and all, it doesn't have a gender..."
            show kaori neu at cc
            voice "audio/voice/E2/Free/KI/50.ogg"
            ki "No, GEARs are the embodiment of a pilot, so I would say they are referred to as the gender of the pilot."
            pf "Shou calls his a \"her\"."
            show kaori ske at cc
            voice "audio/voice/E2/Free/KI/51.ogg"
            ki "You're using Shou as an example of what a normal person thinks?"
            pf "Point taken."
    
    pf "I'm a little surprised Aura has a gender. I didn't take you as a sentimental person."
    show kaori neu at cc
    "She looks calm but her voice gets a little defensive."
    voice "audio/voice/E2/Free/KI/52.ogg"
    ki "What's that suppose to mean?"
    pf "I mean, I get that the GEAR is shaped like a female for the purpose of sponsorship and to appeal to spectators, but..."
    "I trail off, unsure how to verbalise my question without offending. How do you ask someone about the boobs of their GEAR? {w}Luckily, Kaori seems to understand."
    show kaori cur at cc
    voice "audio/voice/E2/Free/KI/53.ogg"
    ki "This frame is smaller for better agility and the..."
    show kaori thi b1 at cc with dissolve
    "She looks at the chest area of Aura. Her face flushes."
    voice "audio/voice/E2/Free/KI/54.ogg"
    ki "... extra storage space contains emergency energy packs for the thrusters in case the core temporarily overheats. Their... um... location just happened to be there for the best weight distribution of the GEAR."
    "Aura sounds no-nonsense and efficient. They really do embody their pilots."
    pf "I suppose that makes sense."
    show kaori neu at cc with dissolve
    stop music fadeout 5
    "She nods."
    "We both continue reviewing her GEAR. {w}The silence only grows more and more awkward."
    stop music fadeout 10
    pf "So, how did you come up with the name? {w}If I didn't know any better, I would think it was named after the anime {i}Ninja Ranger{/i}. The one in pink was also called \"Aura\"!"
    show dots:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori dis at cc with dissolve
    "Kaori glares at me."
    voice "audio/voice/E2/Free/KI/55.ogg"
    ki "... Yeah, so? It {i}is{/i} named after her."
    
    menu:
        "Are you serious?":
            pf "For real?"
            show kaori neu at cc
            voice "audio/voice/E2/Free/KI/56.ogg"
            ki "Why is that so bad?"
            pf "I just never thought you'd be into anime."
    
        "Good joke, you almost had me.":
            pf "Haha! good one."
            show kaori ann at cc
            "Kaori scowls."
            voice "audio/voice/E2/Free/KI/57.ogg"
            ki "What's so funny?"
            pf "You, watching anime."
            "I visualise that for a second before bursting out laughing again."
            show vein:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            play sound "audio/sfx/Human/light_punch.ogg" fadein 1
            with Shake((0, 0, 0, 0), .5, dist=5)
            "Kaori slugs me on the shoulder, bringing me back to reality."
    
        "There's no way.":
            "I raise an eyebrow in question."
            pf "You? Into anime?"
            
    show kaori ske at cc
    voice "audio/voice/E2/Free/KI/58.ogg"
    ki "What's so hard to believe about me liking anime?"
    "Now that I think about it, I didn't really consider what sort of hobbies Kaori has. Although, anime would be on my list of \"probably not\" or \"impossible\" for her."
    
    $renpy.pause(.5)
    
    show kaori neu with dissolve
    
    $renpy.pause(1.0)
    
    "..."
    "....."
    
    pf "Actually, isn't \"Aura\" the Ranger of Honor?"
    show kaori cur at cc
    "She blinks in surprise."
    voice "audio/voice/E2/Free/KI/59.ogg"
    ki "How did you know that?"
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    pf "I might be into anime as well."
    show kaori ske at cc
    voice "audio/voice/E2/Free/KI/60.ogg"
    ki "Really? That's a surprise."
    pf "\"What's so hard to believe about me liking anime\"?"
    show kaori thi b1 at cc with dissolve
    "Kaori blushes in embarrassment."
    voice "audio/voice/E2/Free/KI/61.ogg"
    ki "I guess we were both making unfair assumptions."
    show dots:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    "..."
    show kaori cur b1 at cc
    "She looks at her GEAR before facing me again."
    voice "audio/voice/E2/Free/KI/62.ogg"
    ki "Um, so... which is your favourite ranger?"
    "Her speech is halted, as if she's too embarrassed to even ask the question."
    
    ### NOTE - this is a new variable for the E3.5/E4 release
    $ E2KIS3_Ranger = "Justice"
    
    ### NOTE - the text highlighting here is not consistent with the new vision for the highlighting's purpose
    
    menu:
        "Justice":
            $ E2KIS3_Ranger = "Justice"
            pf "Balance, the Ranger of Justice."
            show kaori hap b1 at cc
            voice "audio/voice/E2/Free/KI/63.ogg"
            ki "Balance!"
            show shiny:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/Free/KI/64.ogg"
            ki "He was so cool! Always leading the way for the other rangers!"
    
        "Knowledge" if MCStory != 2:
            jump E2KIS3_Knowledge
    
        "{color=#00ff00}{b}Knowledge{/b}{/color}" if MCStory == 2:
            label E2KIS3_Knowledge:
                $ E2KIS3_Ranger = "Knowledge"
                pf "Tome, the Ranger of Knowledge."
                show note:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori hap b1 at cc
                voice "audio/voice/E2/Free/KI/65.ogg"
                ki "The Ranger of Knowledge! He was always integral to solving the mysteries!"

        "Emotion" if MCStory != 3:            
            jump E2KIS3_Emotion
        
        "{color=#00ff00}{b}Emotion{/b}{/color}" if MCStory == 3:
            label E2KIS3_Emotion:
                $ E2KIS3_Ranger = "Emotion"
                pf "Sense, the Ranger of Emotion."
                show kaori smi b1 at cc
                voice "audio/voice/E2/Free/KI/66.ogg"
                ki "Sense was amazing."
                pf "Of course, he was always so understanding of others."
                show note:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori hap b1 at cc
                voice "audio/voice/E2/Free/KI/67.ogg"
                ki "I know, and he'd know just the right things to say or do to help anyone!"
    
        "Power" if MCStory != 1:
            jump E2KIS3_Power
    
        "{color=#00ff00}{b}Power{/b}{/color}" if MCStory == 1:
            label E2KIS3_Power:
                $ E2KIS3_Ranger = "Power"
                pf "Forte, the Ranger of Power."
                show kaori cur b1 at cc
                voice "audio/voice/E2/Free/KI/68.ogg"
                ki "Oh Forte..."
                pf "Uh...?"
                voice "audio/voice/E2/Free/KI/69.ogg"
                ki "Those muscles..."
                $renpy.pause(1.0)
                show drooling:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                $renpy.pause(.33)
                show kaori smi b3 at cc with Dissolve(1.0)
                "Kaori sighs, dreamy-eyed."
                pf "What."
                show kaori sur b3 at cc with dissolve
                "She snaps out of it."
                show panic:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E2/Free/KI/70.ogg"
                ki "I-I mean, muscles for strength! N-Not the physical attraction of muscles. Well, not that I'm saying they weren't--"
                show kaori cur b2 at cc with dissolve
                "She stops before finishing the thought."
                show kaori ner b2 at cc with dissolve
                voice "audio/voice/E2/Free/KI/71.ogg"
                ki "L-Like the functionality of muscles!"
                show drop:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori thi b2 at cc with dissolve
                voice "audio/voice/E2/Free/KI/72.ogg"
                ki "You know... for strength? He was the team's \"muscles\"... it's a figure of speech!"
    
        "Honor":
            $ E2KIS3_Ranger = "Honor"
            pf "Aura, the Ranger of Honor."
            show kaori ske b1 at cc
            voice "audio/voice/E2/Free/KI/73.ogg"
            ki "You're just saying that because she's my favourite."
            pf "No, I'm not. She always did the right thing no matter how difficult the decision."
            show note:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori hap b1 at cc
            voice "audio/voice/E2/Free/KI/74.ogg"
            ki "I know! No matter the circumstance, she'd always do what was most honorable. That type of conviction is admirable!"
            
    $renpy.pause(1)
    show kaori cur b2 at cc with dissolve
    "I stare at Kaori in surprise. I don't think I've ever seen her so animated.{w} She blinks at my astonishment before her face reddens."
    show tsuBlush:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori thi b2 at cc
    voice "audio/voice/E2/Free/KI/75.ogg"
    ki "Well, I mean, if you're into that."
    show kaori smi b1 at cc with dissolve
    "I let out a chuckle. Kaori smiles."
    pf "I'm glad I was able to learn something new about you."
    show kaori cur b2 at cc with dissolve
    "Her cheeks redden even further."
    voice "audio/voice/E2/Free/KI/76.ogg"
    ki "Umm, don't make it sound like that."
    "She shuffles her feet and avoids my gaze."
    show regBlush:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori smi b2 at cc
    voice "audio/voice/E2/Free/KI/78.ogg"
    ki "... But it is a little nice knowing you like anime too."
    $renpy.pause(1)
    stop music fadeout 5
    scene black with fade
    $renpy.pause(1)
    "We spend some more time together at the hangar before she has to head out for her class."
    $ E2KIS3_Completed = 1
    stop ambient fadeout 3
    $renpy.pause(1)
    
    #end

