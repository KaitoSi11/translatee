#
label E2VBS4:
    
    
    
    
    #INTEGRATE WITH HER CHOICE IN THE MORNING
    "I go to call Valeries number when I notice a text message that came in earlier today."
    "It's from Valerie."
    "{i}Heyyy, I'm heading over to the park in just a bit. I'll meet you there soon to finish up that assignment!{/i}"
    "...She didn't even confirm with me before going. What if I was unavailable?"
    "Though I suppose she probably intends to finish the assignment one way or another."
    "I better head out then."
    
    jump E2D6S1_Nikki
    
    
    
    
    #Weekend Event
    
label E2VBS4_Continued:
    
    $ valHairF = "default"
    $ valHairB = "default"
    $ valOut = "sDate"
    
    play ambient "audio/ambience/Morning.ogg" fadein 3
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    scene bg isokaze park day with fade:
        yoffset -50
        xoffset -100
    "I park my bike and text Valerie that I'm at the entrance of the park."
    "Although she responds that she's close, it's still another 10 minutes before she arrives dressed in a skirt and heels. {w}She greets me playfully."
    show valerie smi at cc with dissolve
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO98.ogg"
    vb "I hope you weren't waiting too long."
    pf "No… What's the deal with your outfit?"
    show question:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie cur at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO99.ogg"
    vb "Hm? This is what you're supposed to wear on a date."
    
    menu:
        "You mean she was serious this whole time?!":
            pf "A-A date?"
            show valerie hap at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO100.ogg"
            vb "Of course! That's what we agreed upon isn't it?"
            pf "Um, well, I didn't think--"
            show valerie smi at cc
            "I feel the heat flush my face. Valerie smiles."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO101.ogg"
            vb "Oh my, are you blushing?"
            pf "No!"
            show valerie hap at cc
            "All that does is make my face redder. {w}Valerie giggles."
    
        "Check her out.":
            "I eye her up and down, my eyes locking somewhere in the upper section of her body."
            show valerie mis at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO102.ogg"
            vb "What are you looking at~?"
            
            menu:
                "Look away!":
                    pf "Nothing!"
                    show valerie ske at cc
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO103.ogg"
                    vb "You were looking at me."
                    pf "No!--I mean, that is a really nice… shirt."
                    show valerie smi at cc
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO104.ogg"
                    vb "You think so? What's nice about it?"
                    pf "Uh… the colour?"
                    show valerie hap at cc
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO105.ogg"
                    vb "Suure…"
                    show note:
                        xoffset 720
                        yoffset 125
                        xzoom .75
                        yzoom .75
                    "Valerie giggles."
    
                "Continue to admire the greatest assets in silence.":
                    show valerie cur at cc
                    
                    
                    show bg isokaze park day:
                        parallel:
                            linear 1.5 xzoom 1.5
                        parallel:
                            linear 1.5 yzoom 1.5
                        parallel:
                            linear 1.5 yoffset -200
                        parallel:
                            linear 1.5 xoffset 150
                            
                        
                    
                    show valerie cur:
                        parallel:
                            linear 1.5 xzoom 1.5
                        parallel:
                            linear 1.5 yzoom 1.5
                        parallel:
                            linear 1.5 yoffset -450
                            
                    $renpy.pause(1.5, hard=True)
                        
                    "My gaze... it cannot be averted! Those supple humps are simply--"
                    show valerie smi at cc:
                        linear 1.0 yoffset -50
                        
                    show bg isokaze park day:
                        linear 1.0 yoffset -100
                        
                    $renpy.pause(1.0, hard=True)
                        
                    "A delicate finger pushes up my chin until I'm looking at Valerie's smiling face."
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO106.ogg"
                    vb "I think that's long enough."
                    
                    show bg isokaze park day:
                        parallel:
                            linear .66 xzoom 1
                        parallel:
                            linear .66 yzoom 1
                        parallel:
                            linear .66 yoffset -50
                        parallel:
                            linear .66 xoffset -100
                            
                        
                    
                    show valerie smi:
                        parallel:
                            linear .66 xzoom 1
                        parallel:
                            linear .66 yzoom 1
                        parallel:
                            linear .66 yoffset -0                 
                    
                    $renpy.pause(.66, hard=True)
                    $renpy.pause(.5)
                    pf "How about a few more minutes?{w} Like ten."
                    show valerie hap at cc
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO107.ogg"
                    vb "You don't get that privilege until at least the third date."
                    "I sulk."
    
                "Mosquito bites.":
                    pf "Apparently, not much."
                    show shoBlush:
                        xoffset 720
                        yoffset 125
                        xzoom .75
                        yzoom .75
                    show valerie sur b1 at cc with dissolve
                    "Valerie reddens, though I'm not sure if it's from embarrassment or anger. She immediately covers herself with both hands."
                    show vein:
                        xoffset 720
                        yoffset 125
                        xzoom .75
                        yzoom .75
                    show valerie ang b1 at cc
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO108.ogg"
                    vb "Rude! My eyes are up here!"
                    show valerie ann b1 with dissolve
                    "I shrug."
                    show valerie neu with dissolve
                    "Thankfully for me, she rebounds quickly from being upset."
    
        "What an impractical outfit.":
            pf "You realise we're going to be walking, right?"
            show valerie smi at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO109.ogg"
            vb "Sure."
            pf "...So did you bring a change of shoes?"
            show valerie hap at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO110.ogg"
            vb "Of course not. Nothing else matches this outfit!"
            "Not quite what I meant."
    
    pf "Okay, well, we should get started."
    show valerie smi at cc with dissolve
    "She nods."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO111.ogg"
    vb "What did you have in mind?"
    pf "The assignment wants us to find the pillars of town which are in the heart of the park. So I guess we should start walking."
    show valerie hap at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO112.ogg"
    vb "Good idea!"


    "She grabs my hand and leads me deeper into the park. {w}As we continue to walk, her pace wanes."
    pf "You okay?"
    show valerie mis at cc with dissolve
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO113.ogg"
    vb "Of course!"
    "Valerie smiles, but I can tell she's uncomfortable."
    
    menu:
        "Offer her your arm.":
            "I hold out my arm for her to take."
            pf "Here, you can lean on me for support."
            show valerie wor at cc
            "She shakes her head."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO114.ogg"
            vb "Honestly, I'm fine."
            show exclamation:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie sur at cc
            "Suddenly, her ankle wobbles."
    
            menu:
                "Steady her!":
                    "I wrap my arm around her and hold her steady as she regains her balance."
                    show valerie ner b1 at cc with dissolve
                    "She glances at me in surprise, and I think I see a blush on her cheeks."
                    show regBlush:
                        xoffset 720
                        yoffset 125
                        xzoom .75
                        yzoom .75
                    show valerie smi b1 at cc with dissolve
                    "Then her usual smile returns to her face, and she snakes an arm around my own, leaning slightly into me."
                    "Now it's my turn to blush."
    
                "Don't do anything.":
                    show valerie ner at cc
                    "Valerie steadies herself before she can fall, and continues to walk."
                    show valerie mis at cc
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO115.ogg"
                    vb "Come on! Try to keep pace."
                    "She smirks."
    
        "Leave her be.":
            "I shrug. If she says she's fine, then I guess she's fine."
                    

                    
    "Soon, we reach a large fountain. In the center stands a statue of a woman who seems to grow out of the water. {w}Tears trickle from her eyes and water flows down from a giant pearl in her hands. {w}Sea creatures cling to her dress, which looks to made of foam. Surrounding the fountain are four stone columns."
    "Valerie breathes a sigh of wonder."
    show valerie cur at cc with dissolve
    stop music fadeout 5
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO116.ogg"
    vb "She's beautiful, but she looks so sad."
    pf "I wonder who she is…"
    show valerie neu at cc
    "As Valerie continues to gaze at the statue, I circle the fountain for a plaque."
    pf "Ah! {w}It says she is popularly known as \"Umiko\" and she is the protector of the island."
    show question:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO117.ogg"
    vb "What does she protect them from?"
    hide valerie with dissolve
    "I squint at the plaque."
    pf "She was a villager from Isokaze and was married to a fisherman. He was a good man and the two of them were happy, but no matter how hard they tried, she was unable to conceive a child."
    pf "One day, her husband came home with an usually large catch. As he sorted through the fish, he found a young boy tangled in his net. Thinking it a gift from the gods, he wrapped the child in a blanket and brought him home to his wife."
    pf "Umiko was thrilled and immediately took to the child like her own son. The boy was extremely curious about the world above the sea and happily adopted Umiko as his mother."
    show valerie neu at cc
    "Valerie kneels beside me."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO118.ogg"
    vb "But the boy was the son of the dragon king, who transformed into a human and came on land to collect his son and bring him back to the sea."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO119.ogg"
    vb "But as his gaze landed on Umiko, whose face was wet with tears, he fell in love and wished to take her back to his palace beneath the waves."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO120.ogg"
    vb "Umiko refused, angering the king. He reverted to his dragon form and called upon the ocean waves to swallow the village. One way or the other, she would be with him in the sea."
    show valerie dis at cc
    "Valerie pauses and wrinkles her nose."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO121.ogg"
    vb "Of course a man throws a temper tantrum because he can't get his way."
    
    menu:
        "What do you mean \"of course\"?":
            pf "Not all men are like that."
            show valerie mis at cc
            "She looks at me, then breaks into a smile."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO122.ogg"
            vb "Well, alright, I know one man who isn't."
            pf "I'm sure you know more than just one."
            show valerie smi at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO123.ogg"
            vb "Nope, just one."
    
        "Pretty sure it's the women who throw tantrums.":
            pf "What about women who like to \"punish\" men so they can get their way?"
            show valerie neu at cc
            "Valerie feigns innocence."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO124.ogg"
            vb "I don't know what you're talking about."
            pf "Uh huh."
            show valerie smi at cc
            "Still, a smile threatens her lips."
    
        "It's just a story.":
            pf "No need to get so worked up. It's not even real. I mean, everyone knows dragons don't exist."
            show valerie neu at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO125.ogg"
            vb "It's real to the people of this island. Otherwise this statue wouldn't exist."
            "She gestures to the fountain."
            pf "I guess."
            
    hide valerie with dissolve
    "I turn back to the plaque."
    pf "As Umiko watched the destruction of the waves, she agreed to join the dragon king. Among protests from her husband, she threw herself into the ocean. Then the servants of the king dragged Umiko down to the palace."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO126.ogg"
    vb "The servants must be the sea creatures. That's why they're clinging to her dress."
    "I nod."
    pf "Still, the dragon king continued to flood the island to ensure Umiko would never be tempted to return to the surface."
    pf "Unable to watch her people suffering, while the king slept, Umiko dislodged the pearl which granted the dragon his power from his chest, and swallowed it."
    show valerie wor at cc with dissolve
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO127.ogg"
    vb "Ew."
    pf "Yeah."
    show valerie neu at cc
    "Valerie continues reading."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO128.ogg"
    vb "Since then, Umiko continues to protect the village from the dragon king's wrath, and in return, the people throw a festival in her honor."
    
    menu:
        "Poor Umiko.":
            pf "That's really sad."
            show valerie cur at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO129.ogg"
            vb "Why?"
            pf "All Umiko wanted was to be a mother, and the child which she thought was a blessing was more like a curse."
            show valerie smi at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO130.ogg"
            vb "Well, at least now that she lives in the sea, she {i}can{/i} be a mother."
            pf "You think so? I think as long as she has the dragon king's power, she can never let her guard down."
            show valerie neu at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO131.ogg"
            vb "I don't mean a mother for the dragon child. She's more like the mother of Isokaze."
            pf "I suppose that's true…"
            show valerie smi at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO132.ogg"
            vb "It's not quite what she wanted but at least her sacrifice wasn't in vain. Clearly the people love her."
    
        "Whoa! With power like that I'd be unstoppable!":
            pf "Man, if I had the pearl, I'd be a force to be reckoned with!"
            show valerie mis at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO133.ogg"
            vb "Oh yeah? And what would you do with it?"
    
            menu:
                "With God as my witness, we'll never go hungry again!":
                    pf "Obviously I'd use it ensure a great harvest every year. Starvation will be a thing of the past."
                    show valerie hap at cc
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO134.ogg"
                    vb "Aw, look at you with your big heart."
                    pf "Isn't that what anyone would do?"
    
                "Wet T-shirt contests!":
                    pf "Wet T-shirt contests all day every day!"
                    show drop:
                        xoffset 720
                        yoffset 125
                        xzoom .75
                        yzoom .75
                    show valerie ske at cc
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO135.ogg"
                    vb "Wow, you didn't even pause to think about it."
                    pf "Well, it is the most obvious choice."
    
                "I am the storm.":
                    pf "I'd lightning strike down my enemies."
                    show valerie thi at cc
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO136.ogg"
                    vb "I'm not sure the pearl controls the weather."
                    pf "It controls water, right? Rain is just evaporated water."
                    show drop:
                        xoffset 720
                        yoffset 125
                        xzoom .75
                        yzoom .75
                    show valerie hap at cc
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO137.ogg"
                    vb "Yeeaah... that might be pushing it."
    
            pf "Although, if Umiko has the dragon's power… where do you think she is now?"
            show valerie neu at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO138.ogg"
            vb "Still in the ocean. She has to keep an eye on the dragon king so he doesn't pull anymore tricks."
            pf "So she's spending the rest of her life hiding from the dragon? She should just strike him down with his own power!"
            show valerie hap at cc
            "Valerie giggles."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO139.ogg"
            vb "Good idea. You should tell her that!"
    
        "This story has no ending.":
            pf "That's the end of the story?"
            show valerie smi at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO140.ogg"
            vb "Yeah."
            pf "But what happened next?"
            show valerie hap at cc
            "Valerie giggles."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO141.ogg"
            vb "I had no idea you were so interested!"
            pf "I'm not, but you can't {i}not{/i} end a story."
            show valerie smi at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO142.ogg"
            vb "There is an ending. She uses the power of the sea to protect her village."
            pf "That's a cop out ending. Why didn't the dragon just take back his pearl? Or strike her down or something?"
            pf "Or is he dead? Maybe the pearl was the source of his power."
            show valerie mis at cc
            "Valerie looks amused."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO143.ogg"
            vb "For someone who isn't interested, you sure have a lot of questions."
            pf "...None of this makes any sense."
            show valerie smi at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO144.ogg"
            vb "Maybe we can look up the rest of the story in the library."
            "I shrug."
            pf "If you want."
            
    show valerie neu at cc with dissolve
    "Valerie stares at the fountain, but I can't read the expression on her face."
    pf "What did you think about the story?"
    show valerie sad at cc
    "She looks unusually solemn."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO145.ogg"
    vb "She was put in an unfair situation and did what she felt she needed to do. It's very admirable, but it's also sad. Once the dragon king showed up, Umiko's life was no longer her own to live."
    show valerie neu at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO146.ogg"
    vb "But at least she hasn't been forgotten."
    
    pf "That's true... {w}I'm curious about the festival they throw in her honor. Do you know anything about it?"
    show valerie thi at cc
    "She shakes her head."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO147.ogg"
    vb "Maybe we'll learn more about her in class."
    
    pf "Speaking of class… we should probably get started on those pillars."
    show exclamation:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie sur at cc
    "Valerie snaps to attention."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO148.ogg"
    vb "Right!"
    hide valerie with dissolve
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    "We wander the corners of the fountain where each pillar stands. A word is carved into each one of them: {i}benevolence, achievement, honor, and virtue{/i}."
    "I pull out my phone and take a picture of each column."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO149.ogg"
    vb "Oooh, are you keeping a memento of our date because you're having such a good time?"
    show valerie mis at cc
    pf "It's not a date."
    show note:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie hap at cc
    "Valerie just laughs."
    pf "And no, I'm doing the assignment. The next step is to define what we think each pillar means."
    show valerie smi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO150.ogg"
    vb "Hmm… okay."
    pf "Any ideas?"
    show valerie cur at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO151.ogg"
    vb "For which one?"
    
    label E2VBS4_Questions:
        
        if E2VBS4_Answers == 4:
            jump E2VBS4_Convergence
            
        menu:
            "Benevolence." if E2VBS4_Benevolence == 0:
                $ E2VBS4_Benevolence = 1
                $ E2VBS4_Answers += 1
                pf "Benevolence."
                show valerie smi at cc
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO152.ogg"
                vb "I think, just like its definition, it's a reminder to do kindly unto others."
                pf "Kind of like Umiko's sacrifice… She put her own wants and needs aside to take care of her village."
                show valerie thi at cc
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO153.ogg"
                vb "I don't know how much of it was sacrifice since she was {i}forced{/i} into it."
                pf "Technically she did have a choice. She could either go with him into the ocean or die with everyone on the shore."
                show valerie neu at cc
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO154.ogg"
                vb "...That's not much of a choice."
                pf "Still counts!{w} Lawyered!"
                show valerie dis at cc
                "Valerie frowns as she crosses her arms."
                pf "Calm down, Kaori."
                show valerie hap at cc
                "Valerie bursts out laughing."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO155.ogg"
                vb "She does that quite a bit doesn't she..."
                jump E2VBS4_Questions
        
            "Achievement." if E2VBS4_Achievement == 0:
                $ E2VBS4_Achievement = 1
                $ E2VBS4_Answers += 1
                pf "Achievement."
                show valerie smi at cc
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO156.ogg"
                vb "I think it means we mustn't squander the life we are given. Each goal we achieve--be it small or large--brings us one step closer to fulfillment."
                pf "After all, you never know when a dragon king will fall in love with you..."
                show valerie sad at cc
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO157.ogg"
                vb "... And ruin your life forever."
                pf "...{w}Well, then."
                jump E2VBS4_Questions
        
            "Fortitude." if E2VBS4_Fortitude == 0:
                $ E2VBS4_Fortitude = 1
                $ E2VBS4_Answers += 1
                pf "Fortitude."
                show valerie smi at cc
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO158.ogg"
                vb "It's pretty straightforward. It's perseverance, and I think it's mostly geared towards mental and emotional perseverance instead of physical. Even when times are hard, we must remember to keep moving forward and to always have hope."
                show valerie thi at cc
                "Valerie looks thoughtful."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO159.ogg"
                vb "I wonder if Umiko's husband always hoped that she would come back to him or if he gave up on her."
                pf "I don't know."
                show valerie ner at cc
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO160.ogg"
                vb "I think he probably gave up as soon as the dragon king set his sights on her."
                pf "I wouldn't be so sure about that."
                show valerie neu at cc
                "Valerie just shrugs."
                jump E2VBS4_Questions
        
            "Abstinence." if E2VBS4_Abstinence == 0:
                $ E2VBS4_Abstinence = 1
                $ E2VBS4_Answers += 1
                pf "Abstinence."
                show valerie ske at cc
                "Valerie smirks."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO161.ogg"
                vb "Nope."
                pf "It's not about sex."
                show valerie mis at cc
                "She winks."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO162.ogg"
                vb "I know. It's about self-restraint. Especially during times of low supplies, people should strive to control their indulgences."
                pf "I'm sure this became a pillar back when the village suffered from floods and bad harvests, like in Umiko's story."
                show valerie hap at cc
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO163.ogg"
                vb "I agree."
                jump E2VBS4_Questions
        
            "Nevermind.":
                pf "Actually, don't worry about it. I got this."
                show valerie cur at cc
                "She seems surprised."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO164.ogg"
                vb "You sure?"
                pf "Yup!"
                show valerie neu at cc with dissolve
                jump E2VBS4_Convergence
    
    #menu comes up once more without the option you chose first time.
    #Menu can show up 4 times, each without the options you chose before
    label E2VBS4_Convergence:
        
        $renpy.pause(.5)
        if E2VBS4_Answers == 0:
            show valerie ske at cc with dissolve
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO165.ogg"
            vb "Someone's confident about the project!"
            "I shrug."
            pf "It all seems straight-forward enough."
            show valerie smi at cc
            "Valerie grins." 
        
        elif E2VBS4_Answers < 4:
            show valerie ske at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO166.ogg"
            vb "Is that it?"
            pf "Yeah, thanks for explaining. That helps a lot."
            show valerie smi at cc
            "Valerie smirks."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO167.ogg"
            vb "That's what I'm here for."
        
        else:
            show valerie hap at cc
            "Valerie looks amused."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO168.ogg"
            vb "Well, the rest of the project should be a breeze now that I've done all the hard work."
            pf "That wasn't my intention! I was just curious what your interpretation of the words are and if they are the same as mine."
            show valerie mis at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO169.ogg"
            vb "Of course."
            "She winks."
            "But I really am just curious…"
    
        pf "Since we've gotten all our pictures, let's head back."
        show valerie neu at cc
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO170.ogg"
        vb "Sure."
        "Valerie nods, and starts walking. {w}Suddenly she stumbles."
        stop music fadeout 1.5
        show exclamation:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        show valerie sur at cc with dissolve
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO171.ogg"
        vb "Ah!"
        # sfx?
        hide valerie with dissolve
        "I rush to her."
        pf "What happened? Are you okay?"
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO172.ogg"
        vb "No!"
        show valerie win at cc
        "She holds up the remains of her shoe."
        show crying:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO173.ogg"
        vb "My heel broke!"
        pf "What."
        show valerie sad at cc
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO174.ogg"
        vb "Do you know how hard it is to find the perfect pair of heels?"
        pf "I can honestly say that I do not."
        show valerie ner at cc
        "She sighs, slips off her broken shoe, and balances on one foot."
        pf "Maybe we should head back. We got the pictures and can finish the rest of the project later."
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO175.ogg"
        vb "Yeah."
        show valerie sad at cc
        "She hesitates, reluctant to let her bare foot touch the ground."
        $ persistent.gpix[54][0] = 1
        $ persistent.gpix[55][0] = 1
        pf "I have a solution."
        
    
        if MCStory == 1:
            scene black with fade
            vb "!"
            play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 2.0
            show cg valerie broken heel1 with Dissolve(2.5):
                xalign 0.5
                yalign 0.5
                xzoom 0.5
                yzoom 0.5
            $ renpy.pause(.5)
            "Before Valerie can react, I position my arms under her back and legs, and lift her in my arms. She lets out a small yelp of surprise, then smirks."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO176.ogg"
            vb "Are you trying to impress me?"
            pf "What gives you that idea?"
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO177.ogg"
            vb "You literally just swept me off my feet."
    
            menu:
                "That's not what I meant!":
                    pf "I-It's not like that! You just seemed like you needed help."
                    show cg valerie broken heel2 with dissolve:
                        xalign 0.5
                        yalign 0.5
                        xzoom 0.5
                        yzoom 0.5
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO178.ogg"
                    vb "Mmhm, and how come you didn't just offer a piggy-back ride like most people?"
                    pf "Oh… I figured this would be more comfortable for you since it's less likely you'll slip."
                    "Valerie grins, and throws her arms around my neck."
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO179.ogg"
                    vb "You're right, I do feel more secure."
                    "I try to ignore the heat in my cheeks."
    
                "Are you impressed?":
                    pf "I thought you would have realised by now that I'm not like most people."
                    show cg valerie broken heel2 with dissolve:
                        xalign 0.5
                        yalign 0.5
                        xzoom 0.5
                        yzoom 0.5
                    "She grins. There's a mischievous glint in her eye."
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO180.ogg"
                    vb "That's true. Most people would have asked a girl before putting their hands on her."
                    pf "Oh sorry, I can put you back down--"
                    show cg valerie broken heel1 with dissolve:
                        xalign 0.5
                        yalign 0.5
                        xzoom 0.5
                        yzoom 0.5
                    "I begin to lower her legs, but Valerie squeals and hugs my neck."
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO181.ogg"
                    vb "Nope! This is fine."
    
                "Do you want me to drop you?":
                    pf "I picked you up and I can put you right back down."
                    show cg valerie broken heel2 with dissolve:
                        xalign 0.5
                        yalign 0.5
                        xzoom 0.5
                        yzoom 0.5
                    "Valerie grins."
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO182.ogg"
                    vb "That wouldn't be too bad as long as you pick me up again."
                    pf "Maybe."
    
    
        else:
            pf "I'll carry you, okay?"
            show valerie cur with dissolve
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO183.ogg"
            vb "No, you don't have to. I can walk…"
            "She puts down a tentative foot and takes a couple of uneven steps."
            scene black with fade
            "I sling an arm around her waist."
            play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 2.0
            show cg valerie broken heel1 with Dissolve(2.5):
                xalign 0.5
                yalign 0.5
                xzoom 0.5
                yzoom 0.5
            $renpy.pause(.5)
            #pf "Trust me, it'll be fine."
            show cg valerie broken heel2 with dissolve:
                xalign 0.5
                yalign 0.5
                xzoom 0.5
                yzoom 0.5
            "She glances at me."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO184.ogg"
            vb "Uh, what are you doing?"
            pf "Picking you up."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO185.ogg"
            vb "Wouldn't it be easier for me to jump on your back?"
    
            menu:
                "This way you won't slip.":
                    pf "I suppose if you really want to do that we can… I just figured this way you had less chance of slipping."
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO186.ogg"
                    vb "Ohhh, thinking ahead!"
    
                "Only the princess treatment for you.":
                    pf "That's no way to treat a princess!"
                    "Valerie giggles."
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO187.ogg"
                    vb "I like the way you think."
    
                "This is easier for me.":
                    pf "I can carry you easier this way."
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO188.ogg"
                    vb "Are you sure? I would think this is harder…"
                    pf "It's either this or the fireman's carry."
                    "Valerie tugs on her skirt, covering more of her legs."
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO189.ogg"
                    vb "You shouldn't try to peek at my underwear!"
                    pf "...This it is then."
    
            "She doesn't protest as I lift her in my arms."
    
        "Valerie falls silent, and I can't help but wonder what she is thinking. Without her sharp tongue, she seems strangely vulnerable."
        scene black with fade
        #stop ambient fadeout 3
        $renpy.pause(1)
        #play ambient "audio/ambience/Campus Road.ogg" fadein 3
        scene bg campus intersection dusk with fade
        #play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
        "Once we reach my bike, her eyes grow wide."
        show valerie sur at cc with dissolve
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO190.ogg"
        vb "{i}That's{/i} your bike?"
        "...For a second, I'd forgotten about the rainbow sparkles."
        pf "It doesn't usually look like this."
        show valerie hap at cc
        "Valerie doesn't even try to hold her in laughter."
        show note:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO191.ogg"
        vb "Hahaha!"
        "Tears form in her eyes."
        show valerie mis at cc
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO192.ogg"
        vb "Uh huh, are you sure you don't have any experience picking out heels?"
        pf "It sounds to me like you're able to walk on your own now, so--"
        show panic:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        show valerie sur at cc
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO193.ogg"
        vb "No! I'm sorry!"
        show valerie ner at cc
        "Valerie clings to me, and buries her face in my shirt, trying to calm her laughter."
        show valerie neu at cc
        "Once she's calmed down, I gently place her on the back of my bike and climb on in front of her. Without my prompting, she wraps her arms around me. {w}I'm suddenly glad she can't see my face."
        pf "It seems like this isn't your first time on a bike."
        show valerie smi at cc
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO194.ogg"
        vb "No, my mother had a boyfriend who drove a motorcycle back in France, so I got used to riding one."
        pf "\"Had\"?"
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO195.ogg"
        vb "Yes."
        stop ambient fadeout 3
        scene black with fade
        "Valerie doesn't offer up an explanation, so I start the engine and head back to ACE. {w}She leans on me the entire ride back."
        $renpy.pause(1)
        "Soon, I'm parking my bike at ACE."
        scene bg campus main dusk with fade
        pf "I can take you to your dorm."
        "As I slide off, I hold out my arms, but Valerie shakes her head. She hops off the bike and flashes me her usual smirk."
        show valerie mis at cc
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO196.ogg"
        vb "It's only our first date… way too early to be bringing boys into my room."
        pf "It's not a date."
        show valerie smi b1 at cc with dissolve
        "She smiles and kisses me on the cheek."
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO197.ogg"
        vb "Thank you for taking me home."
    
        menu:
            "!!":
                "My cheeks burn and I suddenly can't remember how to speak."
                pf "Oh, uh, sure."
                show valerie hap b1 at cc
                "Valerie giggles."
    
            "Maybe she'll give me another kiss…":
                pf "Do I also get a \"thank you\" for carrying you?"
                show valerie mis b1 at cc
                "Valerie smirks."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO198.ogg"
                vb "As a matter of fact, you do."
                "I ready myself for another kiss, but it never comes."
    
            "Ignore the kiss.":
                "She's French… they're more affectionate than Americans. I'm sure it means nothing and shouldn't make it weird."
                pf "It was no problem."
    
        show valerie hap b1 at cc
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO199.ogg"
        vb "I'll have the project done tonight."
        show valerie smi b1 at cc
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO200.ogg"
        vb "This is my way of thanking you for being such a gentleman."
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO201.ogg"
        vb "You can look everything over and turn it in."
        pf "Wait, you're not doing all of it are you?"
        show valerie mis at cc with dissolve
        "Valerie merely smirks."
        
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO202.ogg"
        vb "Anyway, this was nice. Let's do it again sometime."
        pf "Yeah, I'd like that."
        show valerie smi at cc
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO203.ogg"
        vb "I will wear sturdier shoes."
        pf "I'd like that too."
        show heart:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        show valerie hap at cc with dissolve
        $renpy.pause(1.0)
        hide valerie with dissolve
        "She laughs, and slips the other shoe off her foot. Then she waves goodbye as she heads back to her dorm."
        scene black with fade
        stop music fadeout 5
        "I still don't think it's fair for Valerie to do the whole project herself, but if that's what she wants then I can't stop her. I'll just be sure to help with revisions. {w}I hop back on my bike and head home."
        stop ambient fadeout 3
        $renpy.pause(2.5)
        $ E2VBS4_Completed = 1
        jump E2D6S2
        #end

