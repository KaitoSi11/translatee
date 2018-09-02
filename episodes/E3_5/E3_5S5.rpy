#
label E3_5S5:
    
    #((Convergence from any of the paths or alone))
    
    #fade to black
    scene black with fade
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    scene bg campus lounge night with fade
    "Once we've all reconvened at the bar, we order our drinks and find an open table among the couches."
    
    #Open image again
    show shou smi at l3 with dissolve:
        xoffset -100
        xzoom 0.75
        yzoom 0.75
    show mayu neu at l2 behind shou with dissolve:
        xoffset 125
        xzoom 0.75
        yzoom 0.75
    show valerie dis at l1 with dissolve:
        xoffset 250
        xzoom 0.75
        yzoom 0.75
    show kaori neu at r1 with dissolve:
        xoffset 100
        xzoom -0.75
        yzoom 0.75
    show yuuna smi at r3 with dissolve:
        xoffset 100
        xzoom -0.75
        yzoom 0.75
        
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L18.ogg"
    vb "It's so unfair that I still can't have anything alcoholic!"
    # storm
    "Valerie pouts and puts an arm around Mayu."
    show valerie mis
    show mayu cur
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L19.ogg"
    vb "Isn't that right?"
    show mayu ner
    "Mayu speaks softly."
    voice "audio/voice/E4/Mayu/D0/Mayu D0-28.ogg"
    ma "Umm, I don't want to drink even if I could..."
    show valerie ske
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L20.ogg"
    vb "Really? You have to at least try it once!"
    "I feel Shou elbow my side."
    voice "audio/voice/E4/Shou/d0/32 Copy Copy.ogg"
    ss "If she's this excitable normally, I wonder how'd she'd act when drunk."
    
    if valrelatonship == 1:
        "A slow grin spreads across my face."
        pf "Wouldn't you like to know."
        "Shou looks surprised."
        voice "audio/voice/E4/Shou/d0/33 Copy Copy.ogg"
        ss "You mean...?!"
        "I wink."
        pf "Don't worry about it."
    
    else:
        pf "I don't even want to imagine the trouble she'd get all of us into."
        "Shou laughs."
        voice "audio/voice/E4/Shou/d0/34 Copy Copy.ogg"
        ss "True that, Broseph!"
        
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L21.ogg"
    vb "Hey! Enough with your private conversation! Let's play a game!"
    show mayu neu
    "Yuuna perks up."
    voice "audio/voice/E4/Yuuna/E4/D0/19.ogg"
    ym "Oh! That sounds like fun."
    show kaori smi
    show mayu hap
    "Mayu nods excitedly. Even Kaori seems interested."
    voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_23.ogg"
    ki "Okay. What game were you thinking, Valerie?"
    show valerie smi
    voice "audio/voice/MISSING/BATCH4/Valerie/ValE4Redos/ValE4Redo1.ogg"
    vb "Well, In honor of Shou's cosplay of Yozuke--"
    show shou sur
    voice "audio/voice/E4/Shou/d0/35 Copy Copy.ogg"
    ss "Not Yozuke!"
    show mayu sur
    "Mayu looks surprised."
    voice "audio/voice/E4/Mayu/D0/Mayu D0-29.ogg"
    ma "Really? I thought you were Yozuke this entire time."
    "Shou slumps on the table."
    show shou sad
    voice "audio/voice/E4/Shou/d0/36 Copy Copy.ogg"
    ss "Not you too, Mayu."
    # panic
    show mayu wor
    voice "audio/voice/E4/Mayu/D0/Mayu D0-30.ogg"
    ma "I'm sorry! It's just, you portray him perfectly..."
    show mayu ner
    voice "audio/voice/E4/Mayu/D0/Mayu D0-31.ogg"
    ma "...W-With that outfit, I mean."
    voice "audio/voice/E4/Yuuna/E4/D0/20.ogg"
    ym "Wasn't Yozuke also the comic relief?"
    show kaori mis
    voice "audio/voice/MISSING/BATCH5/k_redo_11.ogg"
    ki "And a pervert."
    pf "It's like someone copy and pasted that character and changed the name to Shou."
    show mayu neu
    "The group nods. Shou groans."
    show shou thi
    voice "audio/voice/E4/Shou/d0/37 Copy Copy.ogg"
    ss "You guys are killin' me here."
    "Yuuna looks at Valerie."
    voice "audio/voice/E4/Yuuna/E4/D0/21.ogg"
    ym "What game were you thinking about?"
    show shou smi
    # note
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L22.ogg"
    vb "The King's Game!"
    pf "The King's Game?"
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L23.ogg"
    vb "Mhm! It's easy. We number chopsticks and give one of them a special symbol. Whoever picks the symbol is the king!"
    show kaori smi
    voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_24.ogg"
    ki "Oh, that sounds easy enough."
    voice "audio/voice/E4/Yuuna/E4/D0/22.ogg"
    ym "What can the king do?"
    show valerie mis
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L24.ogg"
    vb "The better question is what the king {i}can't{/i} do. He will command one of the numbers to do something, and his order is absolute!"
    show mayu sur
    voice "audio/voice/E4/Mayu/D0/Mayu D0-35.ogg"
    ma "E-Eh?!"
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L25.ogg"
    vb "Don't worry, it's a lot of fun!"
    show kaori neu
    voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_25.ogg"
    ki "Well, I guess it couldn't hurt to try it..."
    show valerie cur
    show mayu cur
    "Everyone looks at Kaori in surprise. She's the last person we would expect to agree to a game like this. She blinks at us."
    show kaori ske
    voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_26.ogg"
    ki "What? It's only us playing. I'm sure no one is going to make an unreasonable command."
    show kaori dis
    "Kaori glares at Shou."
    voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_27.ogg"
    ki "Right?"
    show mayu neu
    show valerie neu
    "Shou shifts uncomfortably."
    voice "audio/voice/E4/Shou/d0/38 Copy Copy.ogg"
    ss "R-Right!"
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L26.ogg"
    vb "Then it's settled!"
    show kaori neu
    "Valerie grabs some chopsticks and marks them with numbers, and then marks one of them with a colour. She shuffles them on the table then holds them in her hand so the marks are covered."
    show valerie mis
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L27.ogg"
    vb "Let the games begin!"
    "My heart races in anticipation as we all grab a stick."
    show valerie neu
    "I turn mine over and see the coloured marking! Lucky! I watch as the rest of my friends turn theirs over. {w}Kaori wears her best poker face. If I didn't already have the king's stick, I wouldn't know what she had in her hand. Shou's face is one of bitter disappointment. I wonder what he had planned as king..."
    show mayu smi
    "Mayu breathes a sigh of relief. I guess she didn't want to be king. Valerie seems indifferent about her stick--she probably would be happy as either king or subject. {w}Yuuna looks around the table."
    voice "audio/voice/E4/Yuuna/E4/D0/23.ogg"
    ym "Who's the king?"
    "I offer my glorious crown... er, chopstick."
    voice "audio/voice/E4/Shou/d0/39 Copy Copy.ogg"
    ss "Broseph's got it! What is your command, your majesty?"
    "Let's think for a moment..."
    
    pf "I command..."
    
    menu:
        "Number 1 to give me a kiss!":
            pf "Number one to give me a kiss on the lips!"
            show kaori ner b1
            show mayu neu
            "Everyone quickly checks their numbers. Some of them sigh in relief while others wait in anticipation."
            voice "audio/voice/E4/Shou/d0/40 Copy Copy.ogg"
            ss "Whew, it's not me!"
            pf "Thank god for that."
            "That would have been weird."
            pf "Who is it then?"
            # movement?
            show kaori ner b2
            "Kaori stands so quickly her chair wobbles. Her face is bright red."
            voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_28.ogg"
            ki "I want a redraw!"
            # exclamation
            show valerie hap
            voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L28.ogg"
            vb "THE KING'S ORDERS ARE ABSOLUTE!"
            "The rest of the group murmur their agreements with Valerie. I guess nobody wants to take Kaori's place."
            show kaori sur b2
            voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_29.ogg"
            ki "W-What! Come on!"
            
            if kaorelatonship == 1:
                voice "audio/voice/E4/Shou/d0/41 Copy Copy.ogg"
                ss "What's the big deal? Aren't you two dating?"
                # shoBlush
                show kaori sur b3
                "Kaori's blush deepens."
                show kaori wor b3
                voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_30.ogg"
                ki "S-Shut up!"
        
            "Mayu sighs."

            voice "audio/voice/MISSING/BATCH8/Missing Mayu-05.ogg"
            ma "I'm disappointed by you, Kaori..."
            show kaori ske b2
            voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_31.ogg"
            ki "Huh?"
            "Mayu looks down."
            show valerie mis
            voice "audio/voice/E4/Mayu/D0/Mayu D0-33.ogg"
            ma "I always looked up to you and knew I could trust you because you always keep your word..."
            show kaori wor b2
            voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_32.ogg"
            ki "A-Ah!"
            # crying
            voice "audio/voice/E4/Mayu/D0/Mayu D0-34.ogg"
            ma "B-But now... I..."
            "I think I hear faint sniffles."
            show kaori win b2
            voice "audio/voice/E4/Kaori/D0/Kaori_34.ogg"
            ki "Argh!"
            # vein
            show kaori ang b2
            voice "audio/voice/E4/Kaori/D0/Kaori_35.ogg"
            ki "Fine!"
            "Mayu looks up with dry eyes and a smile on her face as if nothing happened. {w}She's devious!"
            show valerie ske
            "Luckily, Kaori was too focused on me to notice Mayu, but judging by everyone else's expressions, they are all just as surprised by her performance as I am."
            show kaori ann b2 with dissolve:
                xzoom -1
                yzoom 1
            "Kaori marches up to me."
            pf "Why hello there."
            voice "audio/voice/E4/Kaori/D0/Kaori_36.ogg"
            ki "Shut up! Don't make this worse than it is."
            show kaori neu b2
            "She sits down next to me and places both her hands on the space between us on the chair. She looks at me, then closes her eyes and aims for my cheek."
    
            if kaorelatonship == 1:
                # QTE - otherwise it defaults to else
                
                $ qtebase = 3
                $ qtetotal = qteath + qtebase
                $ t_var = qtetotal
                show screen timer_scr(place="E3_5S5_Kissed")
                
                menu:
                    "Turn and kiss her on the lips.":
                        $ renpy.hide_screen ("timer_scr")
                        "As she leans in, I turn my face so her lips meet mine."
                        show kaori sur b3
                        "Kaori quickly opens her eyes and pulls back."
                        voice "audio/voice/E4/Kaori/D0/Kaori_37.ogg"
                        ki "Y-You! W-Why! Don't just...I can't...you--"
                        show kaori win b3
                        "Kaori hits my chest, but her face is bright red and she avoids eye contact with me. She shifts uncomfortably and breathes out in a huff. I never knew I could make Kaori speechless!"
                        # heart
                        show valerie hap
                        voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L29.ogg"
                        vb "Kaori is so adorable when she's like this!"
                        show kaori ann b3
                        voice "audio/voice/E4/Kaori/D0/Kaori_38.ogg"
                        ki "Shut up!"
                        voice "audio/voice/E4/Yuuna/E4/D0/24.ogg"
                        ym "Aww, she is!"
                        show kaori ang b3
                        voice "audio/voice/E4/Kaori/D0/Kaori_40.ogg"
                        ki "SHUT UP!"
                        show kaori ann b3
                        voice "audio/voice/E4/Shou/d0/42 Copy Copy.ogg"
                        ss "I always knew she--"
                        # shake shou?
                        "Kaori smacks Shou hard on the arm."
                        voice "audio/voice/E4/Shou/d0/43 Copy Copy.ogg"
                        ss "THEY ALL SAID SOMETHING! WHY AM I THE ONLY ONE BEING ASSAULTED?"
                        show kaori ang b2
                        voice "audio/voice/E4/Kaori/D0/Kaori_41.ogg"
                        ki "Because you're an idiot!"
                        show kaori ann b2
                        "The group bursts into laughter."
                        show kaori thi b2 at r1 behind yuuna with dissolve:
                            xoffset 100
                            xzoom -0.75
                            yzoom 0.75
                        # tsuBlush
                        "Kaori sits down, arms crossed and pouty, but I know her well enough to know she is actually happy underneath that angry facade."
            
            else:
                label E3_5S5_Kissed:
                    
                    if kaorelatonship == 1:
                        $ renpy.hide_screen ("timer_scr")
                        
                    "I wait in anticipation but she barely pecks my cheek before leaning back."
                    show kaori thi b2
                    voice "audio/voice/E4/Kaori/D0/Kaori_42.ogg"
                    ki "There."
                    
                    if kaorelatonship == 0:
                        "My face heats up, but I try to stay cool."
                        
                    show valerie dis
                    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L30.ogg"
                    vb "That's not on the lips! You have to follow instructions."
                    show kaori ske b2
                    voice "audio/voice/E4/Kaori/D0/Kaori_43.ogg"
                    ki "W-What?"
                    show valerie mis
                    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L31.ogg"
                    vb "Here, let me show you."
                    show valerie mis with dissolve:
                        xzoom 1
                        yzoom 1
                    "My heart starts racing as I see Valerie approach..."
                    "...But sinks when she sits next to Kaori instead."
                    show kaori ner b2
                    voice "audio/voice/E4/Kaori/D0/Kaori_44.ogg"
                    ki "Um..."
                    show valerie smi
                    "Valerie gently strokes Kaori's cheek and stares deeply into her eyes."
                    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L32.ogg"
                    vb "Kaori..."
                    show kaori cur b3 with dissolve
                    "Kaori's face turns bright red. She swats at Valerie's hand before scooting away."
                    # shoBlush CLOSE
                    show kaori sur b3
                    voice "audio/voice/E4/Kaori/D0/Kaori_45.ogg"
                    ki "W-Wha... What do you think you're doing?!"
                    "Valerie scoots forward closing the space between them."
                    show valerie mis b1
                    show kaori ner b3
                    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L33.ogg"
                    vb "The trick is to get her all hot and bothered..."
                    "Kaori shoots up from the couch."
                    show kaori win b3
                    voice "audio/voice/E4/Kaori/D0/Kaori_46.ogg"
                    ki "Stop being a pervert, Valerie!"
                    # note CLOSE
                    show kaori ann b3
                    show valerie hap b1
                    "Valerie starts laughing and claps her hands excitedly."
                    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L34.ogg"
                    vb "Success!"
                    show kaori ske b2 with dissolve
                    voice "audio/voice/E4/Shou/d0/44 Copy Copy.ogg"
                    ss "Damnit!"
                    pf "What?"
                    "Shou pulls out his phone and reluctantly types into it."
                    voice "audio/voice/E4/Shou/d0/45 Copy Copy.ogg"
                    ss "Twenty credits, as promised."
                    show valerie mis
                    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L35.ogg"
                    vb "Thank you!"
                    voice "audio/voice/E4/Yuuna/E4/D0/25.ogg"
                    ym "...What's that all about?"
                    show kaori ner b2
                    voice "audio/voice/E4/Shou/d0/46 Copy Copy.ogg"
                    ss "We had a bet on who Kaori would say \"Stop being a pervert!\" to first."
                    show valerie smi
                    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L36.ogg"
                    vb "Thanks for playing!"
                    show valerie hap at l1 behind kaori with dissolve:
                        xoffset 250
                        xzoom 0.75
                        yzoom 0.75
                    "The group looks at each other before bursting into laughter."
                    show kaori ann b2
                    voice "audio/voice/E4/Kaori/D0/Kaori_47.ogg"
                    ki "I hate you guys!"
                    show kaori thi b2 at r1 behind yuuna with dissolve:
                        xoffset 100
                        xzoom -0.75
                        yzoom 0.75
                    # tsuBlush
                    "Kaori sits down and pouts, but I can tell she's only doing that for show."
        
        "Number 2 to give me a tight hug!":
            pf "Number 2 must give me a hug!"
            "Yuuna blinks."
            voice "audio/voice/E4/Yuuna/E4/D0/26.ogg"
            ym "Oh, that would be me."
            "She looks at me, then blushes."
            voice "audio/voice/E4/Shou/d0/47 Copy Copy.ogg"
            ss "You lucky bastard."
            show kaori ske
            show valerie hap
            "Valerie snorts, but Kaori and Mayu look confused."
            voice "audio/voice/E4/Kaori/D0/Kaori_48.ogg"
            ki "Why? It's a hug between friends. It's nothing unusual."
            if yuurelatonship == 1:
                "Not exactly between {i}friends{/i}, but that's not it..."
            voice "audio/voice/E4/Shou/d0/48 Copy Copy.ogg"
            ss "You don't understand at all."
            # question
            voice "audio/voice/E4/Kaori/D0/Kaori_49.ogg"
            ki "What?!"
            voice "audio/voice/MISSING/BATCH2/11.ogg"
            ss "Don't worry about it."
            show valerie mis
            voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L37.ogg"
            vb "Enough talk! Hurry up already!"
            show kaori neu
            "Valerie smirks. {w}Yuuna and I stand up and approach each other."
            voice "audio/voice/E4/Yuuna/E4/D0/27.ogg"
            ym "Uh, so I will, umm..."
            pf "Yeah, okay, and I'll go here..."
            "We awkwardly lean in the same direction then switch again and still almost collide with each other. This is a lot harder with people watching!"
            voice "audio/voice/E4/Yuuna/E4/D0/28.ogg"
            ym "Okay, here just..."
            "Yuuna wraps her arms around my waist and places her head on my shoulder. As I embrace her, I can't ignore the soft pressure against my chest."
            
            if yuurelatonship == 1:
                "I feel her kiss my left cheek--the one which faces away from the group."
            
            "My face reddens."
            "I can hear Shou muttering something under his breath about being jealous."
            "Yuuna and I untangle from each other. We've hugged before but to do it in front of a group is still embarrassing."
            
            if kaorelatonship == 1:
                "Yuuna looks at me and gives me a sly wink."
                
            # heart
            show valerie hap
            voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L38.ogg"
            vb "Aww, that was so cute!"
            voice "audio/voice/E4/Shou/d0/49 Copy Copy.ogg"
            ss "LET'S PLAY AGAIN."
            show kaori cur
            "We are all surprised by Shou's outburst."
            voice "audio/voice/E4/Shou/d0/50 Copy Copy.ogg"
            ss "I WILL BE KING!"
            show kaori smi
            "Everyone bursts into laughter."
            show valerie mis
            voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L39.ogg"
            vb "You wish!"
        
        "Number 3 to give me a massage!":
            pf "Number 3, I need a massage!"
            voice "audio/voice/E4/Mayu/D0/Mayu D0-32.ogg"
            ma "E-Eh?!"
            show valerie cur
            "As one, everyone stares at Mayu. She blushes under our collective gaze."
            voice "audio/voice/E4/Mayu/D0/Mayu D0-36.ogg"
            ma "B-But...I...Umm..."
            show valerie mis
            voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L40.ogg"
            vb "The king's orders... ARE ABSOLUTE!"
            "Mayu shuffles her feet uncomfortably, then nods."
            voice "audio/voice/E4/Mayu/D0/Mayu D0-37.ogg"
            ma "I guess I don't have a choice..."
            voice "audio/voice/E4/Mayu/D0/Mayu D0-38.ogg"
            ma "Okay."
            "Her face scrunches with determination as she joins me on the couch. I turn around so my back is facing her."
            "I can feel the presence of her hands hovering above my back."
            voice "audio/voice/E4/Mayu/D0/Mayu D0-39.ogg"
            ma "So, do I just…?"
            "Soft hands touch my shoulders and gently begin rubbing them."
            "I sigh contentedly as the tension slowly leaves my body with every movement of her hands. This is some professional grade relaxation I'm feeling!"
            voice "audio/voice/E4/Mayu/D0/Mayu D0-40.ogg"
            ma "...Like this?"
            "I barely register her words through the bliss I am feeling, and nod slowly."
            show valerie sur
            voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L41.ogg"
            vb "Wow, Mayu!"
            voice "audio/voice/E4/Mayu/D0/Mayu D0-41.ogg"
            ma "Eh?!"
            show valerie cur
            voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L42.ogg"
            vb "How are you doing that? He's like pudding in your hands!"
            voice "audio/voice/E4/Mayu/D0/Mayu D0-42.ogg"
            ma "Oh, um... I used to work as a masseuse..."
            show kaori cur
            voice "audio/voice/E4/Kaori/D0/Kaori_50.ogg"
            ki "What? Really?"
            voice "audio/voice/E4/Mayu/D0/Mayu D0-43.ogg"
            ma "N-Not a licensed masseuse! I worked part-time as an assistant..."
            show valerie smi
            voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L43.ogg"
            vb "You're incredible! Please teach me how to do it!"
            show kaori neu
            voice "audio/voice/E4/Mayu/D0/Mayu D0-44.ogg"
            ma "Ah! I can try, but I'm really not that good..."
            
            if mayrelatonship == 0:
                voice "audio/voice/E4/Shou/d0/51 Copy Copy.ogg"
                ss "She's just being modest. Her massages are the best."
                "Mayu's cheeks burn."
                voice "audio/voice/E4/Mayu/D0/Mayu D0-45.ogg"
                ma "S-Shou!"
                voice "audio/voice/E4/Shou/d0/52 Copy Copy.ogg"
                ss "Oh whoops, was I not suppose to say that out loud?"
                show kaori smi
                show valerie hap
                "Shou scratches the back of his head. The group looks at each other before laughing."
            
            else:
                pf "I could definitely get used to this."
                "Mayu's cheeks redden."
                voice "audio/voice/E4/Mayu/D0/Mayu D0-46.ogg"
                ma "I... umm..."
                "Her voice trails off."
                # heart
                show valerie hap
                voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L44.ogg"
                vb "Oh my gosh, she is just the cutest thing ever!"
                "Mayu stops her massaging."
                pf "Aww, over already?"
                show mayu smi
                voice "audio/voice/E4/Mayu/D0/Mayu D0-47.ogg"
                ma "Yup."
                show kaori smi
                "I should have specified the minutes in my command. I was really enjoying that! The group notices my pout and starts laughing."
        
        "Number 4 to sit on my lap!":
            pf "Number 4, come hither unto my lap!"
            show valerie hap
            "Before anyone even has a chance to check their chopsticks, Valerie stands up."
            # note
            voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L45.ogg"
            vb "Yay! That's me!"
            show valerie mis
            "She looks at me, then grins impishly."
            "Uh-oh."
            show valerie mis with dissolve:
                xzoom 1
                yzoom 1
            "Her hips sway mesmerizingly as she walks over to me. She gently moves my legs away from the table towards the edge of the seat. Then slowly lowers herself onto my lap, her legs dangling off of one side as her arms snake around my neck."
            show valerie hap
            voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L46.ogg"
            vb "Is this seat taken?"
            "She squeezes me tighter as she adjusts herself to sit closer to me... and dangerously close to another area."
            
            if kaorelatonship == 1:
                show kaori ner
                voice "audio/voice/E4/Kaori/D0/Kaori_51.ogg"
                ki "T-That's enough!"
                show kaori wor b1 with dissolve:
                    xzoom -1
                    yzoom 1
                "Kaori shoots out of her seat and practically leaps over to us."
                show valerie ske
                voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L47.ogg"
                vb "Aw, don't be like that Kaori. I'm only following the king's command."
                # vein CLOSE
                show kaori ann b1
                voice "audio/voice/E4/Kaori/D0/Kaori_52.ogg"
                ki "Get off of him!"
                "Kaori glares daggers at Valerie, who seems unphased. She merely sighs as she reluctantly unwraps herself from around me."
                # storm CLOSE
                show valerie neu
                voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L48.ogg"
                vb "Fine, fine."
                show kaori ann b1 at r1 with dissolve:
                    xoffset 100
                    xzoom -0.75
                    yzoom 0.75
                "Kaori sits back down but doesn't lessen her glare."
                show valerie hap at l1 behind kaori with dissolve:
                    xoffset 250
                    xzoom 0.75
                    yzoom 0.75
                "Valerie chuckles as she returns to her seat. She's sneaky!"
                # tsuBlush
                show kaori thi b2
                "I look at Kaori who looks back at me. Her face reddens and she quickly looks away."
                show kaori smi b2
                "The group bursts into laughter. Their enthusiasm is infectious and Kaori quickly recomposes herself."
            
            elif mayrelatonship == 1:
                voice "audio/voice/E4/Mayu/D0/Mayu D0-48.ogg"
                ma "Valerie."
                show valerie smi
                "Valerie grins."
                voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L49.ogg"
                vb "Yeees--"
                # frightful CLOSE
                show valerie sur
                "When she sees Mayu, Valerie's words get stuck in her throat and her eyes widen. She jumps off of me and forces out a laugh."
                show valerie ner at l1 behind kaori with dissolve:
                    xoffset 250
                    xzoom 0.75
                    yzoom 0.75
                voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L50.ogg"
                vb "Haha! All in good fun, right?"
                "I glance at Mayu. She seems normal... What is Valerie seeing that I'm not?"
                voice "audio/voice/E4/Mayu/D0/Mayu D0-49.ogg"
                ma "Right."
                "Valerie rushes back to her seat and quickly downs her drink. She looks like she's just seen a ghost!"
                voice "audio/voice/E4/Mayu/D0/Mayu D0-50.ogg"
                ma "Let's play again?"
                show kaori smi
                "The group looks at each other in confusion, which ultimately devolves into laughter."
            
            elif yuurelatonship == 1:
                voice "audio/voice/E4/Yuuna/E4/D0/29.ogg"
                ym "No!"
                show valerie neu
                "Valerie turns to Yuuna, whose face is red."
                voice "audio/voice/E4/Yuuna/E4/D0/30.ogg"
                ym "I think you've sat there long enough."
                show valerie ske
                voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L51.ogg"
                vb "Uh-oh, are you getting jealous?"
                voice "audio/voice/E4/Yuuna/E4/D0/31.ogg"
                ym "Ah!"
                "Yuuna's blush deepens."
                show valerie mis
                voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L52.ogg"
                vb "I'm just following the king's orders. Right, king?"
                pf "Huh?"
                "Yuuna looks pointedly at me."
                voice "audio/voice/E4/Yuuna/E4/D0/32.ogg"
                ym "Well?!"
                "I'm not sure what she wants from me…"
                pf "...Well...?"
                show valerie hap
                "She crosses her arms and pouts. Valerie giggles before removing herself from me. Then returns to her seat."
                show valerie hap at l1 behind kaori with dissolve:
                    xoffset 250
                    xzoom 0.75
                    yzoom 0.75
                # heart
                voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L53.ogg"
                vb "D'aww, you two are the cutest!"
                "I try to catch Yuuna's eye but she refuses to look at me. What did I do?"
                show kaori smi
                "The group bursts out laughing. Yuuna looks at me again and even though she tries to stay annoyed, I can see a trace of a smile breaking through."
            
            elif valrelatonship == 1:
                menu:
                    "Get risque with her too.":
                        show valerie cur b1
                        "I wrap an arm around Valerie's sides and tug her close. She's initially surprised but quickly snuggles into me."
                        pf "Comfortable?"
                        # regBlush CLOSE
                        show valerie smi b1
                        voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L54.ogg"
                        vb "Better than any chair."
                        "She looks up at me, pulling me deep into her eyes of blue. Our surroundings blur out of focus and all I can see is her… and her pink lips… soft and kissable… probably tasting like her strawberry lip gloss… {w}I instinctively lean in..."
                        show kaori cur b2
                        show mayu cur b2
                        show yuuna cur b2
                        with dissolve
                        show shou sur b2 with dissolve
                        voice "audio/voice/E4/Shou/d0/53 Copy Copy.ogg"
                        ss "Broseph!"
                        show valerie sur b2
                        show shou cur b2
                        with dissolve
                        "Shou's voice jolts me back to reality. Valerie and I whip around to face the rest of the group. All of the girls stare at anything but us, their cheeks burning red. Even Shou looks uncomfortable."
                        show valerie neu b2
                        show kaori thi b1
                        voice "audio/voice/E4/Shou/d0/54 Copy Copy.ogg"
                        ss "I think that's enough."
                        "Valerie sighs, then unwraps herself from me."
                        voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L55.ogg"
                        vb "If you insist."
                        show valerie smi b2
                        "She sits beside me and wraps her arm around mine."
                        # heart CLOSE
                        voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L56.ogg"
                        vb "I guess this will have to do for now."
                        voice "audio/voice/E4/Mayu/D0/Mayu D0-51.ogg"
                        ma "L-Let's play again?"
                        "Mayu stares at Shou. I think I know why she wants to play again."
                        show kaori smi
                        "Apparently, the group does too because the girls start snickering. Mayu blushes."
                        voice "audio/voice/E4/Mayu/D0/Mayu D0-52.ogg"
                        ma "What?!"
                        show valerie hap b2
                        "We all burst out laughing."
                    
                    "I think that's enough.":
                        pf "Valerie."
                        jump E3_5S5_Awkward
            
            else:
                label E3_5S5_Awkward:
                    "My cheeks burn. Is it hot in here or is it just me?"
                    "Valerie laughs playfully, clearly amused by my embarrassment."
                    show kaori cur b1
                    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L57.ogg"
                    vb "Really? I thought you'd last a little longer than that."
                    show valerie hap at l1 behind kaori with dissolve:
                        xoffset 250
                        xzoom 0.75
                        yzoom 0.75
                    "She unwraps herself from me and returns to her seat. The other girls stare at Valerie. From their deep blushes, I can't tell whether they're impressed or angry."
        
        "Number 5 to count to ten!":
            pf "Number 5 must count to 10."
            show valerie dis
            "Valerie pouts."
            # question
            voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L58.ogg"
            vb "Really? That's it?"
            pf "Um… in English?"
            show shou hap
            "Shou grins excitedly."
            # note
            voice "audio/voice/E4/Shou/d0/55 Copy Copy.ogg"
            ss "No problem, I can do that easily!"
            show valerie ann
            voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L59.ogg"
            vb "That's no fun! I want to vote for a new king."
            # drop
            show yuuna thi
            voice "audio/voice/E4/Yuuna/E4/D0/33.ogg"
            ym "Um, Valerie, you don't vote for kings."
            # movement?
            "Valerie snatches the coloured chopstick from my hand."
            show valerie hap
            voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L60.ogg"
            vb "Usurped then!"
            show kaori smi
            show mayu smi
            show yuuna hap
            "I blink, slightly dazed. Did I just get dethroned? {w}The rest of the group laughs."
            
    #fade to black
    scene black with fade
    "We played a few more rounds of The King's Game, and Shou never once drew the coloured stick! {w}Watching his frustration as some of us became repeat kings was an endless source of amusement."
    stop music fadeout 5
    "I wonder if his luck is really that bad or if a certain blonde was rigging the game for her own amusement…"
    "When it became late, we all said our goodbyes and headed out."
    "I stifle a yawn as I enter the quiet house. Tip-toeing into my room, I quickly get ready for bed and fall asleep with a smile on my face. {w}Best Halloween ever!"
    
    ### E3.5 Release?
    #jump E3_5END
    
    ### E4 Release?
    jump E4D1S1
