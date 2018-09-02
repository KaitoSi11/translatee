#
label E3YMS2:
    
    #Evening 
    $ yuuOut = "sUniform"
    "I dial Yuuna's number."
    # sfx
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(2)
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    $renpy.pause(.25)
    voice "audio/voice/E3/Free/YM/S2/yuuna/25.ogg"
    ym "Hello?"
    pf "Hi, Yuuna. What are you up to this evening?"
    voice "audio/voice/E3/Free/YM/S2/yuuna/26.ogg"
    ym "I'm in the small auditorium in the drama center."
    pf "Oh, is there a play?"
    voice "audio/voice/E3/Free/YM/S2/yuuna/27.ogg"
    ym "Not quite. I'm attending a class run by the improv club. You should come!"
    
    menu:
        "Okay.":
            pf "That sounds like fun! I'll be right there."
            voice "audio/voice/E3/Free/YM/S2/yuuna/28.ogg"
            ym "Great! See you soon."
    
        "Maybe.":
            pf "I'm not sure. I've never done improv or any acting classes before."
            voice "audio/voice/E3/Free/YM/S2/yuuna/29.ogg"
            ym "That's okay, neither have I. We can learn together."
            pf "Well, alright, but you have to promise you won't make fun of me."
            voice "audio/voice/E3/Free/YM/S2/yuuna/30.ogg"
            ym "Only if you don't make fun of me."
            pf "Deal. I'll see you there soon."
    
        "No.":
            pf "Thanks, but that's not my thing. I'll catch you another time."
            voice "audio/voice/E3/Free/YM/S2/yuuna/31.ogg"
            ym "Oh, okay. No problem. See you later."
            "We hang up. Maybe I should hang out with someone else."
            #Loop back to evening choice menu
            #$ E3YMS2_Completed = 1
            call E3FreeTime from _call_E3FreeTime_4
            
    stop ambient fadeout 3
    scene black with fade
    stop music fadeout 3
    scene bg campus auditorium day with fade
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    "As soon as we hang up the phone I head to the drama center. {w}When I arrive, I spot Yuuna sitting towards the right of the room. As I head over, I run straight into someone!"
    #screen shake?
    show professorM2 extra at cc with dissolve
    pf "I'm sorry!"
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 1.ogg"
    sprof1 "Don't worry about it."
    "Wait a minute…"
    pf "Hey, I know you!"
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 2.ogg"
    sprof1 "Hm?"
    pf "Aren't you the instructor for the cooking club? You teach improv too?"
    "He laughs."
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 3.ogg"
    sprof1 "No, that's my twin brother."
    pf "Oh, I see…"
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 4.ogg"
    sprof1 "Anyway, have a seat. We're about to get started."
    
    hide professorM2 with dissolve
    show yuuna smi at l2 with dissolve
    
    "He marches to the front of the room while I sit beside Yuuna. She smiles in acknowledgement." 
    "The auditorium has about thirty people. Although I'd never considered improv before, I suppose it's something a lot of people are interested in."
    show yuuna neu
    show professorM2 extra at r2:
        xzoom -1
        
    with dissolve
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 5.ogg"
    sprof1 "Welcome to improv!"
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 6.ogg"
    sprof1 "For those of us who are new to this group, improv is live acting. Everything is made up in the moment--plot, characters, dialogue, everything. Every performance is unique and cannot be recreated in exactly the same way."
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 7.ogg"
    sprof1 "Okay, everyone partner up. We're going to have each team perform a skit."
    show yuuna smi
    "Yuuna and I nod at each other."
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 8.ogg"
    sprof1 "It doesn't matter if you're a newbie to improv or a veteran. The most important thing to remember is to go with the flow. Your partner might throw something completely wild at you, but that's okay. That's what makes improv fun."
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 9.ogg"
    sprof1 "You'll have a choice of scenarios on stage for each pair to choose from. Once the scene has been set, then the only rule is to do whatever comes to mind."
    stop music fadeout 5
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 10.ogg"
    sprof1 "So, any volunteers?"
    
    #QTE
    $ qtebase = 3
    $ qtetotal = qteath + qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E3YMS2_Silence")
    
    menu:
        "Me!":
            $ renpy.hide_screen ("timer_scr")
            play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
            "I raise my hand."
            pf "We volunteer as tribute!"
            show panic:
                xoffset 365
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna cur
            "Yuuna is startled, but doesn't object."
            voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 11.ogg"
            sprof1 "Wonderful! Come on up then."
            show yuuna ner
            pf "Are you ready?"
            "She seems nervous, but nods."
            show yuuna smi
            voice "audio/voice/E3/Free/YM/S2/yuuna/32.ogg"
            ym "As ready as I'll ever be, I guess."
            hide professorM2
            hide yuuna
            with dissolve
            "Together, we head onstage."
    
        "Keep your hand down.":
            label E3YMS2_Silence:
                $ renpy.hide_screen ("timer_scr")
                play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
                "I glance around the room, as does everyone other student. It's gone eerily quiet as everyone tries to stay unnoticed."
                "Yuuna touches my hand."
                show yuuna smi
                voice "audio/voice/E3/Free/YM/S2/yuuna/33.ogg"
                ym "Everyone seems to be just as nervous as we are. Maybe we should go first."
        
                menu:
                    "Sure.":
                        pf "Okay. At least when we go first there is nothing to compare our performance to."
                        show note:
                            xoffset 365
                            yoffset 100
                            xzoom .75
                            yzoom .75
                        show yuuna hap
                        voice "audio/voice/E3/Free/YM/S2/yuuna/34.ogg"
                        ym "Right!"
                        show yuuna smi
                        "She raises her hand."
                        voice "audio/voice/E3/Free/YM/S2/yuuna/35.ogg"
                        ym "We volunteer."
                        voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 12.ogg"
                        sprof1 "Good thing you volunteered when you did. I was just about to choose a \"volunteer\". Come on up."
                        hide professorM2
                        hide yuuna
                        with dissolve
                        "An audible sigh of relief ripples through the room as we head onstage."
        
                    "No.":
                        play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
                        pf "I'd rather watch another team do it first before going. I wouldn't know what to do up there."
                        show yuuna 
                        "Yuuna's hopeful smile drops."
                        show yuuna ner
                        voice "audio/voice/E3/Free/YM/S2/yuuna/36.ogg"
                        ym "I understand. I guess we can see if anyone will volunteer."
                        voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 13.ogg"
                        sprof1 "Ahem. You two in the right. You seem pretty chatty tonight. How about you take that enthusiasm onto the stage?"
                        show yuuna sur
                        "The instructor is pointing straight at us."
                        show panic:
                            xoffset 365
                            yoffset 100
                            xzoom .75
                            yzoom .75
                        voice "audio/voice/E3/Free/YM/S2/yuuna/37.ogg"
                        ym "O-Okay."
                        show yuuna ner
                        "Yuuna glances at me. I shrug and follow her onstage."
                        hide professorM2
                        hide yuuna
                        with dissolve
                        
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 14.ogg"
    sprof1 "You'll find the scenario options on the table over there. Once you've decided, read the scenario out loud for the rest of the class."
    
    "We walk over to the table in the corner of the stage."
    show yuuna neu at cc with dissolve
    voice "audio/voice/E3/Free/YM/S2/yuuna/38.ogg"
    ym "Which one do you want to do?"
    "I read the descriptions."
    
    menu:
        "You're at the beach, but you've gender-swapped.":
            pf "Gender swapped beach scene... So I have to play a girl and you have to play a guy?"
            voice "audio/voice/E3/Free/YM/S2/yuuna/39.ogg"
            ym "Yup."
            "It might be fun playing Yuuna…"
            pf "Let's do this one."
            show question:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna cur
            "She raises her eyebrow but doesn't disagree."
            show yuuna ner
            voice "audio/voice/E3/Free/YM/S2/yuuna/40.ogg"
            ym "If you like."
            show yuuna neu
            "After we select our description, I read it aloud for the class. The instructor then gives us the signal to begin."
            "Yuuna squares her shoulders and swaggers exaggeratedly on the stage."
            show yuuna hap
            voice "audio/voice/E3/Free/YM/S2/yuuna/41.ogg"
            ym "I love the beach! And doing manly things like… uh… swimming! Too bad my friend isn't here with me so we can swim together."
            show yuuna mis
            "Yuuna looks pointedly in my direction, indicating for me to join her in our skit."
            "I pretend to be shy and pitch my voice high."
            pf "Teehee, um, just a minute…"
            "There's a prop bin in the corner of the stage. I rummage through the bin, hoping to find something to use… {w}Aha!"
            show yuuna sur
            "I grab two balloons and stuff them underneath my blazer. A chorus of laughter reverberates in the room, but Yuuna's face is one of chagrin."
            pf "Sorry I'm late! I was getting ready."
            show yuuna ske
            "Yuuna gets back into character and instead of talking she just stares very obviously at my balloons."
            voice "audio/voice/E3/Free/YM/S2/yuuna/42.ogg"
            ym "That's not what I look like!... Is it?"
            "I cover my chest with an arm."
            show yuuna sur
            pf "Ahh! Stop being a pervert!"
            "Yuuna pretends to balk."
            show yuuna ner
            voice "audio/voice/E3/Free/YM/S2/yuuna/43.ogg"
            ym "N-No! That's not it! I was just admiring your swimsuit!"
            "I pout and continue to cover my \"chest\"."
            show yuuna thi
            voice "audio/voice/E3/Free/YM/S2/yuuna/44.ogg"
            ym "Um, anyway, uh, why don't we go swimming?"
            pf "I suppose if you want to we can."
            show yuuna mis
            voice "audio/voice/E3/Free/YM/S2/yuuna/45.ogg"
            ym "Race you there!"
            "She runs across the stage and mimes diving into the ocean. I follow slowly behind her and pretend to wade carefully into the shallow water."
            pf "Ahh! Oh no! As soon as I touched the water my top fell off!"
            "I hold the balloons close to my chest, but let my blazer fall to the ground, mimicking losing a bikini top."
            show shoBlush:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna sur b2
            "Yuuna's mouth drops open in shock."
    
            if MCStory == 3:
                "The audience might think she was still in character, reacting to my mishap, but I knew she was mortified I'd referenced what happened at our beach excursion."
    
            "I turn my back to Yuuna, but not before I see her bright red cheeks."
            pf "Don't look at me!"
            show yuuna mis b1
            "I peek at her out of the corner of my eyes. Her shocked expression suddenly melts into a cheeky smile."
            voice "audio/voice/E3/Free/YM/S2/yuuna/46.ogg"
            ym "Oh no! For some inexplicable reason, my nose has started bleeding!"
            pf "Hey! That's not what happened!"
            show yuuna hap b1
            "Yuuna grins, and this time it's my cheeks which turn red."
            "The audience has not stopped laughing since my balloon incident and didn't even notice my break in character."
    
        "You must declare your dying confession in the arms of your love.":
            pf "A deathbed confession! Can I be the one who's dying?"
            show yuuna smi
            voice "audio/voice/E3/Free/YM/S2/yuuna/47.ogg"
            ym "Sure, I'll follow your lead then."
            pf "Alright, let's do it."
            voice "audio/voice/E3/Free/YM/S2/yuuna/48.ogg"
            ym "Okay."
            show yuuna neu
            "After we select our description, I read it aloud for the class. The instructor then gives us the signal to begin."
            "Yuuna signals that she will follow my lead. I rush onto the stage, dodging imaginary arrows."
            pf "Arghh!"
            show yuuna ner
            "I clutch at my chest as one of the arrows \"hits\" me, and stumble around the stage before falling to my knees. My breath shortens into gasps as I slowly lay on my back."
            show exclamation:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna sur
            voice "audio/voice/E3/Free/YM/S2/yuuna/49.ogg"
            ym "Noooo!"
            "Yuuna races onto the stage and cradles my head in her lap."
            show yuuna wor
            voice "audio/voice/E3/Free/YM/S2/yuuna/50.ogg"
            ym "Stay with me!"
            "I gurgle faintly."
            pf "Y-Yuu...na…"
            show yuuna ner
            voice "audio/voice/E3/Free/YM/S2/yuuna/51.ogg"
            ym "Shh, don't talk. Everything will be okay."
            pf "T-There's something… I have… to tell… you."
            show yuuna wor
            voice "audio/voice/E3/Free/YM/S2/yuuna/52.ogg"
            ym "You can tell me when you're better!"
            pf "Come… closer…"
            show yuuna sad
            "She leans in. Her hair tickles my cheek. I whisper to her."
    
            menu:
                "Something meaningful.":
                    pf "I'm sorry… we couldn't have… more time together…"
                    show yuuna win
                    voice "audio/voice/E3/Free/YM/S2/yuuna/53.ogg"
                    ym "Don't talk like that!"
                    "I feign a coughing fit."
                    show yuuna wor
                    voice "audio/voice/E3/Free/YM/S2/yuuna/54.ogg"
                    ym "Save your voice."
                    pf "I'll always remember… the time we had…"
                    "After the words come out, I fall limp in her arms."
    
                "Something ridiculous.":
                    pf "Don't forget… to feed… my cat…"
                    show yuuna cur
                    voice "audio/voice/E3/Free/YM/S2/yuuna/55.ogg"
                    ym "What?"
                    pf "She'll only eat tuna… and not… the cheap stuff..."
                    show yuuna ner
                    "After the words come out, I fall limp in her arms."
    
                "It's too late. I'm dead!":
                    pf "I… I…"
                    "I groan one last time and then fall limp in her arms."
    
            show crying:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna win
            voice "audio/voice/E3/Free/YM/S2/yuuna/56.ogg"
            ym "No! Please, come back to me! What will I do without you?"
            show yuuna sad
            "She shakes me gently, but I don't stir."
            "Her voice grows thick."
            voice "audio/voice/E3/Free/YM/S2/yuuna/57.ogg"
            ym "I'll never forget you."
            "She pulls my face to her breast and hugs me."
    
            menu:
                "Stay in character.":
                    "Although I'm acutely aware of my nose nestled in her soft bosom, I remain still. After all, I'm supposed to be dead, and dead people don't move."
                    show yuuna cur
                    "After a moment, she tenses up as if she realises something."
    
                "And now I'm cured!":
                    "It's softer than any pillows I've ever laid my head on. This is what I imagine heaven feels like. I sigh happily."
                    pf "Whoa…"
                    show exclamation:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    show yuuna cur
                    "Yuuna blinks in surprise at my movement."
                    pf "I'm alive! It's a miracle!"
    
                "Help, I can't breathe.":
                    pf "Hlmph mme."
                    "My words are muffled by her soft bosom. This wouldn't be the worst way to die."
                    show exclamation:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    show yuuna cur
                    "Yunna glances at me in surprise."
    
            show shoBlush:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna wor b1
            voice "audio/voice/E3/Free/YM/S2/yuuna/58.ogg"
            ym "Oh!"
            show yuuna ner b2
            "She pushes me away as her face grows beet red."
            show yuuna ner b3
            "The audience laughs, causing her face to burn even redder."
    
    
        #"You are creating a visual novel.":
            #pf "Oh! Let's do this one! I already have an idea in mind."
            #show yuuna hap
            #"Yuuna grins."
            ### VOICE - missing lines through this whole bit
            #ym "I was hoping you'd say that. I have an idea too."
            #show yuuna smi
            #"After we select our description, I read it aloud for the class. The instructor then gives us the signal to begin."
            #pf "So, I've had an idea burning in my head for a while."
            #show yuuna cur
            #ym "An idea for what?"
            #pf "For a visual novel."
            #show yuuna smi
            #ym "Oh cool! I love those. What's your idea?"
            #pf "So, I've been thinking you know what there are no games of? Kendo."
            #show yuuna cur
            #"She blinks."
            #ym "Kendo…"
            #pf "Yeah! The main character is starting over at a new high school and needs to join a club, but the only club accepting members is the kendo club."
            #show yuuna thi
            #ym "That's a good start, but maybe instead of kendo you go for something that'll reach more audiences… something like…"
            #show dots:
                #xoffset 720
                #yoffset 100
                #xzoom .75
                #yzoom .75
            #$renpy.pause(0.5)
            #"She pauses."
            #$renpy.pause(1)
            #show bulb:
                #xoffset 720
                #yoffset 100
                #xzoom .75
                #yzoom .75
            #play sound "audio/sfx/UI or Plot Element/Lightbulb.ogg"
            #show yuuna sur
            #$renpy.pause(0.5)
            #ym "Robot battles!"
            #pf "Kendo battles…"
            #show yuuna hap
            #ym "Yeah! Who doesn't like robots?"
            #pf "Who doesn't like kendo?"
            #show yuuna neu
            #ym "It's a little old fashioned. You can appeal to more people with robots."
            #pf "Robots are a little too… real. It's like playing a game of your own life."
            #show yuuna ske
            #ym "Not everyone has a GEAR. Besides, you can always advance the science in your game to make it new."
            #pf "With kendo, you have more opportunities to explore traditions and culture of the world."
            #show yuuna mis
            #ym "Maybe we should ask the audience which game they'd prefer."
            #pf "Alright."
            #show yuuna smi
            #"We turn to the other students."
            #pf "Which game would you rather play?"
            #"They erupt into chattering, but I can't understand their responses. Finally, one voice rises above the others."
            #stu2m "It's obvious!"
            #show yuuna mis
            #"Yuuna smirks."
            #show note:
                #xoffset 720
                #yoffset 100
                #xzoom .75
                #yzoom .75
            #ym "I knew it!"
            #pf "What? That wasn't an answer."
            #ym "Sure it was."
            #pf "No…"
    
    "The student professor claps his hands."
    show professorM2 extra at r3 with dissolve:
        xzoom -1
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 15.ogg"
    sprof1 "Great job you too! Have either of you done improv before?"
    show yuuna cur b1
    "We shake our heads."
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 16.ogg"
    sprof1 "You're a natural!"
    show yuuna smi b1
    pf "Really?"
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 17.ogg"
    sprof1 "Yes! That was hilarious! You two have great chemistry together--you make an awesome team."
    show yuuna hap b1
    voice "audio/voice/E3/Free/YM/S2/yuuna/59.ogg"
    ym "Thank you!"
    pf "Yeah, thanks."
    hide professorM2 with dissolve
    show yuuna smi
    "Yuuna glows with excitement as we return to our seats."
    show heart:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/Free/YM/S2/yuuna/60.ogg"
    ym "We rocked it! Thanks for coming out and joining me."
    pf "No problem. This was a lot more fun than I expected it to be."
    voice "audio/voice/E3/Free/YM/S2/sprof1/Drama Professor 18.ogg"
    sprof1 "Alright, I've swapped out the scenarios on the table so we don't get any repeats. So who's next?"
    
    #fade out
    stop music fadeout 5
    scene black with fade
    "Yuuna and I watch the other teams perform their skits to the amusement of us all. By the time everyone had finished, my sides hurt from laughing so hard."
    stop ambient fadeout 3
    
    #end
    $ E3YMS2_Completed = 1

