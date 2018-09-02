#
label E2MAS1:
    
    $ mayOut = "sUniform"
    
    # Event 1 - Afternoon Choice (>30 Points)
    
    stop ambient fadeout 3
    scene black with fade
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 3
    scene bg campus library day with fade
    
    "I go to the library to study. {w}I sit down at a secluded desk between the stacks of books."
    stop music fadeout 3
    "After a couple of minutes, I think I hear a muffled thumping, as if someone is trying to quiet their jumping."
    show mayu thi at cc with dissolve
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    "Following the noise to a nearby stack, I see Mayu balancing on her toes trying to reach a book on the top shelf."
    show mayu cur at cc
    "Her fingers barely graze the ledge of the shelf. She tries a dainty hop, but still fails to reach the book."
    show storm:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu dis at cc
    "As she sighs, she pouts and readies herself to try again."
    
    $ qtebase = 3
    $ qtetotal = qteath + qtebase
    $ t_var = qtetotal
    
    menu:
        "Let her try again.":
            "Stifling a laugh, I watch Mayu hop again."
            show mayu thi at cc
            "This time, as she grasps at air, her hand knocks the shelf, toppling the wrong book. {w}The book falls dangerously close to her face!"
            
            show screen timer_scr(place="E2MAS1_LibraryStare")
            menu: #timed
                "Stare...":
                    label E2MAS1_LibraryStare:
                        stop music fadeout 5
                        $ renpy.hide_screen ("timer_scr")
                        ### NOTE SFX
                        show mayu sur at cc, Shake(None, .1, dist=10) with Dissolve(.1):
                            parallel:
                                easein .1 alpha 1.0
                        "Before I can react, the book lands on her head then slides to the ground."
                        show mayu win at cc
                        "Mayu scrunches her face and rubs at her head."
                        # crying emote
                        show crying:
                            xoffset 720
                            yoffset 135
                            xzoom .75
                            yzoom .75
                        ma "Ow…"
    
                "Catch!" if MCStory != 1:
                    stop music fadeout 5
                    $ renpy.hide_screen ("timer_scr")
                    show exclamation:
                        xoffset 720
                        yoffset 135
                        xzoom .75
                        yzoom .75
                    show mayu sur at cc
                    "I shoot out from the stacks and intercept the book right before it lands on Mayu's head. She blinks up at me in surprise."
    
                "{color=#00ff00}{b}Catch!{/b}{/color}" if MCStory == 1:
                    stop music fadeout 5
                    $ renpy.hide_screen ("timer_scr")
                    show exclamation:
                        xoffset 720
                        yoffset 135
                        xzoom .75
                        yzoom .75
                    show mayu sur at cc
                    "I shoot out from the stacks and intercept the book right before it lands on Mayu's head. She blinks up at me in surprise."
    
                "Warn!":
                    stop music fadeout 5
                    $ renpy.hide_screen ("timer_scr")
                    pf "Mayu! Look out!"
                    # exclamation
                    show exclamation:
                        xoffset 720
                        yoffset 135
                        xzoom .75
                        yzoom .75
                    show mayu sur at cc
                    "Mayu dodges just before the book lands on her head."
    
                "Fall...":
                    stop music fadeout 5
                    $ renpy.hide_screen ("timer_scr")
                    ### NOTE SFX
                    show mayu sur at cc, Shake(None, .1, dist=10) with Dissolve(.1):
                        parallel:
                            easein .1 alpha 1.0
                    "I try to leap to Mayu's rescue but lose my footing and fall on my face. I hear a small yelp as the book strikes Mayu on the head."
                    show mayu win at cc
                    "Mayu scrunches her face and rubs at her head."
                    show crying:
                        xoffset 720
                        yoffset 135
                        xzoom .75
                        yzoom .75
                    ### VOICE - missing
                    ma "Ow…"
    
                "Miss...":
                    stop music fadeout 5
                    $ renpy.hide_screen ("timer_scr")
                    ### NOTE SFX
                    show mayu sur at cc, Shake(None, .1, dist=10) with Dissolve(.1):
                        parallel:
                            easein .1 alpha 1.0
                    "I leap out to catch the book, but grab empty air! I hear a small yelp as the book strikes Mayu on the head."
                    show mayu win at cc
                    "Mayu scrunches her face and rubs at her head."
                    show crying:
                        xoffset 720
                        yoffset 135
                        xzoom .75
                        yzoom .75
                    ma "Ow…"
    
            
            pf "Are you okay?"
            show mayu smi at cc
            "She nods. She's a little shaken but smiles at me anyway."
            show mayu cur at cc
            "I easily pull out the book that she needs. Mayu blinks at me as I hand it to her."
    
        "Intervene.":
            stop music fadeout 5
            show mayu cur at cc
            "Stifling a laugh, I walk over and easily pull out the book that she needs. Mayu blinks at me as I hand it to her."
            
    show mayu hap at cc
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E2/Free/MA/S1/0-01.ogg"
    ma "Oh, thank you!"
    show mayu ner at cc
    "She hugs the book to her chest, and stares shyly at the ground."
    pf "No problem. It seemed like you could use some help there."
    show mayu ner b1 at cc with dissolve
    "Her cheeks redden as she nods. {w}I take another look at the book she's holding."
    pf "Hey, isn't that a Piloting 101 textbook?"
    show mayu neu b1 at cc
    voice "audio/voice/E2/Free/MA/S1/0-02.ogg"
    ma "Yeah."
    pf "I thought so. I guess you're working on the assignment now?"
    show mayu cur b1 at cc
    voice "audio/voice/E2/Free/MA/S1/0-03.ogg"
    ma "Um, yeah…"
    show question:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    "She gives me a strange look."
    pf "Er, I only know this because I have to retake Piloting 101. I'm not stalking you or anything."
    show mayu ner b1 at cc
    voice "audio/voice/E2/Free/MA/S1/0-04.ogg"
    ma "Oh, okay. That's good to know."
    "There's a long pause. Mayu refuses to make eye contact with me, and I'm worried I might have scared her when she suddenly speaks."
    show mayu thi b1 at cc
    voice "audio/voice/E2/Free/MA/S1/0-05.ogg"
    ma "Why do you have to take Piloting 101 again?"
    show mayu sur b2 at cc with dissolve
    "As soon as the words leave her mouth, her eyes grow wide and her blush deepens."
    show mayu wor b2 at cc
    voice "audio/voice/E2/Free/MA/S1/0-06.ogg"
    ma "I'm sorry! I didn't mean to be rude."
    "I can't help but grin at her reaction."
    pf "No, don't worry, it's a normal question."
    pf "Basically, my credit from CINY didn't transfer. Apparently some of the material is different here for the introductory course, but so far, everything we've covered has been the same."
    show mayu neu b1 at cc with dissolve
    voice "audio/voice/E2/Free/MA/S1/0-07.ogg"
    ma "Oh, I see."
    pf "Yeah. That said, since I've taken this class before, if you ever need help feel free to ask me."
    show mayu smi b1 at cc
    "She smiles."
    voice "audio/voice/E2/Free/MA/S1/0-08.ogg"
    ma "That would be great."
    show mayu ner at cc with dissolve
    "We stand in silence again. She seems like she wants to ask me something but is too shy to say it."
    
    menu:
        "Offer to help her now.":
            pf "Would you like any help now?"
            show mayu smi at cc
            voice "audio/voice/E2/Free/MA/S1/0-09.ogg"
            ma "Ah! S-Sure… but only if it's not too much trouble."
            pf "Of course not! I always have time for my friends."
            show mayu sur b1 at cc with dissolve
            show mayu thi b1 at cc with dissolve
            "Her eyes meet mine when I say \"friend\" before she quickly looks away again. Another blush stains her cheeks."
            show mayu smi b1 at cc
            "Despite that, she smiles and nods. {w}We sit down at the desk together and I go over my notes with her."
            jump E2MAS1_Help
    
        "I know exactly what she wants to ask me.":
            pf "Yes, Mayu, of course I'll help you!"
            show panic:
                xoffset 720
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu sur at cc
            voice "audio/voice/E2/Free/MA/S1/0-10.ogg"
            ma "Eh?!"
            show mayu ner at cc
            voice "audio/voice/E2/Free/MA/S1/0-11.ogg"
            ma "N-No! I couldn't ask that of you."
            pf "Too late, this is going to happen."
            show mayu smi at cc
            "I walk over to my desk and pat the seat beside me. Mayu hesitates, then smiles, and sits beside me."
            voice "audio/voice/E2/Free/MA/S1/0-12.ogg"
            ma "Thanks…"
            jump E2MAS1_Help
    
        "I think she wants to be left alone.":
            pf "Okay, well, I'll let you get back to studying."
            show mayu sur at cc
            voice "audio/voice/E2/Free/MA/S1/0-13.ogg"
            ma "Oh! O-Okay…"
            pf "Good luck."
            stop music fadeout 5
            show mayu ner at cc
            voice "audio/voice/E2/Free/MA/S1/0-14.ogg"
            ma "Thanks, you too."
            "I go back to my desk and continue studying."
            scene black with fade
            stop ambient fadeout 3
            $renpy.pause(1)
            #end
            return
    
label E2MAS1_Help:
    show mayu neu at cc with dissolve
    "As we settle at the desk, I pull out my tablet and Mayu pulls out a spiral notebook. {w}She opens her textbook and flips to the correct page, then opens her notebook to a fresh page, her pencil at the ready, as she begins to read the text."
    "I watch her curiously as she meticulously writes her notes in fine print."
    show mayu cur at cc with dissolve
    show mayu ner b1 at cc with dissolve
    "After a couple of minutes, she looks up and our eyes meet for a second before she looks away. A blush stains her cheeks."
    voice "audio/voice/E2/Free/MA/S1/0-15.ogg"
    ma "Um." 
    pf "Are you {i}writing{/i} your notes?"
    show drop:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    "Mayu seems self-conscious."
    voice "audio/voice/E2/Free/MA/S1/0-16.ogg"
    ma "Oh, um, yeah…"

    menu:
        "That's really cool!":
            pf "That's awesome."
            show mayu sur at cc with dissolve
            "She blinks, surprised."
            voice "audio/voice/E2/Free/MA/S1/0-17.ogg"
            ma "Y-You don't think it's weird?"
            show mayu cur at cc
            "I shake my head."
            pf "No way! People are too dependent on technology these days anyway."
            "I notice my tablet."
            pf "Including me."
            show mayu smi at cc
            "Mayu smiles."
            voice "audio/voice/E2/Free/MA/S1/0-18.ogg"
            ma "For me, I just learn better when I write it down."

        "Did we flashback to the year 2000?":
            pf "I didn't realise anyone still did that. It's kind of an antiquated method."
            show mayu wor at cc
            "Mayu frowns, and fidgets uncomfortably."
            voice "audio/voice/E2/Free/MA/S1/0-19.ogg"
            ma "I-I know it's a little weird…"
            pf "Using a tablet is more efficient. You can type a lot faster than when you write, which is especially helpful during lectures when the professor talks kind of fast."
            show mayu ner at cc
            voice "audio/voice/E2/Free/MA/S1/0-20.ogg"
            ma "That's true, but I'm more comfortable writing things down. I feel like I understand the material better when I have to pay attention to what I'm noting."

        "To each their own.":
            "I shrug."
            pf "Whatever works for you."
            show mayu cur at cc
            "Mayu blinks."
            voice "audio/voice/E2/Free/MA/S1/0-21.ogg"
            ma "This doesn't seem strange to you?"
            pf "It's different, but hey, you do what you need to do."
            show mayu smi at cc
            "Mayu smiles."
            voice "audio/voice/E2/Free/MA/S1/0-22.ogg"
            ma "I find it's easier for me to write things down than to type it out."

    pf "Really?"
    stop music fadeout 5
    show mayu neu at cc
    "She nods."
    pf "How'd you get into that habit?"
    play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 5
    show mayu thi at cc
    voice "audio/voice/E2/Free/MA/S1/0-23.ogg"
    ma "I wasn't allowed to have electronics when I was growing up."
    "I can't remember the last time I was without my tablet."
    pf "How did you survive?!"
    show mayu smi at cc
    "Mayu giggles."
    voice "audio/voice/E2/Free/MA/S1/0-24.ogg"
    ma "Well, it wasn't so bad. I think that's where I got my love of books. I wasn't allowed to play games very often, but Father always encouraged reading."
    voice "audio/voice/E2/Free/MA/S1/0-25.ogg"
    ma "He said that he didn't want me to get distracted from my studies, so that's why I wasn't allowed to have a tablet."
    pf "It sounds like your father takes your education very seriously."
    voice "audio/voice/E2/Free/MA/S1/0-26.ogg"
    ma "He does. I was in high school when I got my first tablet, but by then I was so used to using a pen and paper that typing out my notes felt unnatural."
    stop music fadeout 5
    pf "Well, the one upside to writing all the time is that your handwriting is really neat. {w}I wouldn't be able to read my notes if I wrote everything down."
    show mayu hap at cc
    "Mayu giggles."
    voice "audio/voice/E2/Free/MA/S1/0-27.ogg"
    ma "I'm sure that's not true!"
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    pf "I read somewhere once that a person's handwriting can say a lot about them."
    show mayu cur at cc
    voice "audio/voice/E2/Free/MA/S1/0-28.ogg"
    ma "Oh really?"
    pf "Well, your characters are all very neat and small. Your strokes are slightly rounded, not angular or spiky."
    show question:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/Free/MA/S1/0-29.ogg"
    ma "What does that mean?"
    
    menu:
        "You are an introvert." if MCStory != 2:
            $ mayfriend += 3
            # + high relationship points
            pf "It means you tend to be more shy and avoid confrontation. You also have a tendency to be more creative."
            show mayu smi at cc
            "Mayu seems pleased."
            show note:
                xoffset 720
                yoffset 135
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/Free/MA/S1/0-30.ogg"
            ma "That actually sounds accurate."
            pf "The handwriting doesn't lie."
    
        "{color=#00ff00}{b}You are an introvert.{/b}{/color}" if MCStory == 2:
            $ mayfriend += 3
            # + high relationship points
            pf "It means you tend to be more shy and avoid confrontation. You also have a tendency to be more creative."
            show mayu smi at cc
            "Mayu seems pleased."
            show note:
                xoffset 720
                yoffset 135
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/Free/MA/S1/0-30.ogg"
            ma "That actually sounds accurate."
            pf "The handwriting doesn't lie."
    
    
        "You are an extrovert.":
            # no relationship points
            pf "It means you tend to be more outspoken and you also have a tendency to be more systematic and impatient."
            show mayu sad at cc
            "Mayu frowns."
            voice "audio/voice/E2/Free/MA/S1/0-31.ogg"
            ma "Hmm."
            "Actually, that doesn't sound much like her. I must have made a mistake."
    
        "You are gullible.":
            $ mayfriend += 1
            # + low relationship points
            pf "It means you like to believe a lot of things."
            show mayu ske at cc
            "She furrows her brow in confusion, and I can't help but laugh."
            pf "I have no idea what it means. I don't really believe handwriting is an indicator of personality."
            show mayu smi at cc
            voice "audio/voice/E2/Free/MA/S1/0-32.ogg"
            ma "I suppose you're right."
            show mayu neu at cc
            "Mayu smiles faintly, but seems a little disappointed."
    
    pf "Anyway, we should focus on the assignment."
    show mayu cur at cc
    voice "audio/voice/E2/Free/MA/S1/0-33.ogg"
    ma "Right!"
    show mayu ner at cc
    "She turns back to her text and I return to mine. {w}As I'm reading, I can see Mayu glancing at me out of the corner of my eye."
    voice "audio/voice/E2/Free/MA/S1/0-34.ogg"
    ma "Um…"
    "I look up."
    pf "Hm?"
    show mayu ner b1 at cc with dissolve
    voice "audio/voice/E2/Free/MA/S1/0-35.ogg"
    ma "Ah, well, d-do you think you could explain this passage to me?"
    
    if MCStory == 3:
        "It's a passage on core maintenance, which judging by how well her GEAR held up last battle, I'm certain she already knows."
    
    "I grin."
    pf "Of course."
    show mayu smi at cc with dissolve
    $renpy.pause(1)
    $ E2MAS1_Completed = 1
    
    stop music fadeout 5
    scene black with fade
    "I continue to help her until her assignment is complete."
    stop ambient fadeout 3
    #end
