#
label E3MAS3:
    
    $ mayOut = renpy.random.choice(['sFashion'])
    #Weekend
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(2)
    "I call up Mayu but she doesn't answer. {w}I guess she must be busy…"
    $renpy.pause(1)
    play sound [ "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg" ]
    play sound2 "audio/sfx/Technology/Phone Alarm.ogg"
    "Suddenly, my phone flashes with a call back from Mayu."
    stop sound
    stop sound2
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    $renpy.pause(.5)
    pf "Hey, Mayu."
    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-72.ogg"
    ma "Were you just calling me?"
    pf  "Yeah."
    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-73.ogg"
    ma "Oh, I was just calling you too."
    pf "Haha, no wonder you didn't answer."
    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-74.ogg"
    ma "Yeah…"
    "She falls silent."
    pf "Is something wrong?"
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-75.ogg"
    ma "I… I don't know what to do."
    pf "What do you mean?"
    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-76.ogg"
    ma "I don't know… I'm so confused…"
    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-77.ogg"
    ma "I saw her again with Shou and he was laughing at something she said."
    pf "Who?"
    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-78.ogg"
    ma "I don't know! I've seen them together a few times now and she's--"
    "She takes a deep breath."
    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-79.ogg"
    ma "I'm sorry."
    "Even though she hasn't outright said it, it's obvious that Mayu is worried that Shou's become interested in someone else."
    pf "Mayu, I get it."
    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-80.ogg"
    ma "You do?"
    pf "Yeah."
    "She pauses."
    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-81.ogg"
    ma "Do you think it's nothing?"
    pf "I don't know."
    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-82.ogg"
    ma "Has Shou told you anything?"
    pf "No..."
    "She falls silent, and when she speaks again her voice trembles."
    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-83.ogg"
    ma "Maybe it's time I give up..."
    
    menu:
        "I like Mayu, but she should be with Shou." if MCStory != 3 and E3D4KI_Embraced == 0:
            jump E3MAS3_Shou
            
        "{color=#00ff00}{b}I like Mayu, but she should be with Shou.{/b}{/color}" if MCStory == 3 and E3D4KI_Embraced == 0:
            label E3MAS3_Shou:
                $ E3MAS3_RomanticMock = 1
                "I try to push my feelings for Mayu aside. Her heart is with my best broseph and I don't want to get between two people I care about."
                pf "You shouldn't give up."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-84.ogg"
                ma "R-Really?"
                pf "You should tell Shou how you really feel."
                "She hesitates."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-85.ogg"
                ma "I don't know…"
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-86.ogg"
                ma "What if he doesn't like me back?"
                pf "He does."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-87.ogg"
                ma "How do you know?"
                pf "He'd be a fool not to."
                "She's silent again and I wonder if I've made her blush. Maybe I shouldn't have said that."
                pf "What I mean is you two have known each other since forever. There's no way he doesn't feel the same way about you."
                jump E3MAS3_Mock
    
        "Yes, she should be with me instead." if E3D4KI_Embraced == 0:
            "I care about Mayu so much, and my feelings for her continue to grow the more time we spend together. Now that Shou has found someone else, I can tell Mayu how I feel."
            pf "If Shou hasn't told you how he feels by now he never will. You've given him so many opportunities, and it looks like he doesn't see you as more than a friend."
            pf "As much as I like Shou, you deserve better than him, Mayu."
            pf "You deserve a guy who knows right away that you're worth his attention."
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-88.ogg"
            ma "I don't understand…"
            pf "I haven't said anything out of respect for Shou and your feelings for him, but… {w}Mayu, I really like you."
            ### VOICE - line missing
            voice "audio/voice/MISSING/BATCH8/Missing Mayu-02.ogg"
            
            ma "W-What?"
            "I can hear the shock in her voice. Did she really have no idea?"
            pf "I can't help it. The more I learn about you, the stronger my feelings become. We like the same books and we play music so well together. You're so smart, especially when it comes to strategies and tactics."
            "She's quiet."
            pf "I'd like to give us a chance, if you're willing…"
            "She doesn't respond, and my heart sinks. Just as I'm about to give up hope, she speaks."
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-89.ogg"
            ma "I-It's true, we do have a lot in common. You went to the comic book store with me when I knew Shou would laugh at me…"
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-90.ogg"
            ma "And I do have a really good time with you when we hang out together..."
            "A spark of hope ignites in my chest, making me bold."
            pf "Let's go on a date."
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-91.ogg"
            ma "A date?"
            pf "Yeah. We both like each other, right? Let's meet at the cafe on campus."
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-92.ogg"
            ma "I--Um…"
            $renpy.pause(1)
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-93.ogg"
            ma "Okay. Let's do it."
            "I hear the resolve in her voice, and I smile."
            pf "Great! I'll see you there!"
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-94.ogg"
            ma "Y-Yeah, see you there!"
            "She sounded a lot more excited when we hung up. {w}Is this happening for real? I've waited patiently for this moment and I can't believe it's finally happening."
            "She likes me too. My stomach flutters. This is my chance to show her just how much she means to me. I can't screw it up!"
            jump E3MAS3_Real
    
        "No, she should tell Shou how she feels.":
            pf "Mayu, look, if you wait for Shou to come around, you'll wait forever. You have to tell him how you feel."
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-95.ogg"
            ma "I don't know if I can do that."
            pf "Why not?"
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-96.ogg"
            ma "What if he doesn't feel the same way? I don't want to risk us not being friends."
            pf "Do you really think your friendship is so fragile that something like this would tear you apart forever? At least this way you'll get an answer from him."
            pf "You don't want to feel like this every time you see him with a girl, right?"
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-97.ogg"
            ma "No, I don't like being this way..."
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-98.ogg"
            ma "I guess you're right."
            jump E3MAS3_Mock
    
    # Date Labels
    
    label E3MAS3_Real:
        
        "I check myself in the mirror again to make sure I look good and run my fingers through my hair. {w}Hm, maybe I should change my shirt? {w}No, I'll be fine."
        stop music fadeout 5
        scene black with fade
        "Satisfied, I hop on my bike and drive to campus."
        play ambient "audio/ambience/Desert Maid Cafe.ogg" fadein 3
        scene bg store ramen day with fade
        "I'm the first one to arrive at the cafe so I order a water while I wait for Mayu. {w}My heart pounds in my chest as the seconds tick by."
        $renpy.pause(0.5)
        scene black with fade
        $renpy.pause(1)
        scene bg store ramen day with fade
        $renpy.pause(0.5)
        "After about fifteen minutes she still hasn't arrived and I begin to worry. I hope she didn't change her mind..."
        "I decide to text her."
        "{i}Hey I'm at the table in the back right corner{/i}"
        $renpy.pause(1)
        play sound [ "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg" ]
        play sound2 "audio/sfx/Technology/Phone Alarm.ogg"
        "As I'm about to put away my phone, Mayu calls me."
        stop sound
        stop sound2
        play sound "audio/sfx/Technology/Phone Answer.ogg"
        pf "Hey!"
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-99.ogg"
        ma "Hey… so, um, I got your text but I don't see you…"
        pf "I'm in the back. Hold on, let me go to the front."
        "I walk to the entrance, but I don't see her."
        pf "Where are you?"
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-100.ogg"
        ma "I'm sitting in a booth…"
        pf "I don't see you…"
        pf "Wait. Are you at the cafe in front of the bookstore?"
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-101.ogg"
        ma "No, I'm at the one that's right by the arcade."
        "I forgot there was more than one cafe on campus!"
        pf "No wonder I don't see you."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-102.ogg"
        ma "Am I at the wrong place? I'm sorry!"
        pf "No, it's okay. Give me a second and I'll come to you."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-103.ogg"
        ma "N-No, it's my fault. I can go to you."
        pf "No, I should have specified. Just stay there, okay?"
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-104.ogg"
        ma "Okay…"
        stop ambient fadeout 3
        scene black with fade
        "I race out of the cafe as soon as I hang up the phone and head over to the other cafe. This is not the impression I wanted to make."
        play ambient "audio/ambience/Desert Maid Cafe.ogg" fadein 3
        scene bg campus cafe day with fade
        "I immediately spot Mayu reading the menu at a booth and slide into the seat across from her. She smiles when she sees me."
        play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
        show mayu smi at cc with dissolve
        pf "Sorry about that."
        show mayu sur
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-105.ogg"
        ma "No, I'm sorry!"
        
        if E1D5S1_EventShou == 1 or E1D5S1_EventMayu == 1:
            pf "I remember this place. We were here with Shou last time."
            show mayu smi
            "Mayu nods."
            show drop:
                xoffset 720
                yoffset 135
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-106.ogg"
            ma "Yeah, I'm sorry. Shou and I come here all the time so I just assumed this is the one you meant."
            pf "It's my fault. I'm sorry."
            "Why am I apologising so much? Get a grip on yourself, [pfirst]!"
        
        else:
            pf "I didn't know there was another cafe nearby."
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-107.ogg"
            ma "Yeah, Shou and I come here all the time. It's a lot better than the other one on campus."
            show drop:
                xoffset 720
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu wor
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-108.ogg"
            ma "I'm sorry I didn't tell you!"
            pf "No, it's not your fault."
            
        show mayu neu
        "We fall silent."
        pf "So, um, have you ordered yet?"
        "She shakes her head."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-109.ogg"
        ma "I was waiting for you."
        "I grab one of the menus on the table and take a look. {w}I'm not hungry after my big breakfast, but it'd be rude to just sit here without eating. Maybe choosing the cafe wasn't the best idea..."
        pf "Hmm, what's good here?"
        show mayu hap
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-110.ogg"
        ma "I really like their omurice!"
        pf "Is that what you're going to get?"
        show mayu smi
        "She nods."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-111.ogg"
        ma "Shou likes their croquettes."
        
        menu:
            "Omurice sounds good.":
                $ E3MAS3_Order = "Omurice"
                pf "I'll the omurice too, then."
                show mayu cur
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-112.ogg"
                ma "You like that too?"
                pf "Yeah. My mom used to make it for me a lot as a kid."
                show mayu smi
                "Mayu smiles."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-113.ogg"
                ma "My mom did too."
        
            "Croquettes are yummy.":
                $ E3MAS3_Order = "Croquettes"
                pf "Shou knows what's up. I'll get croquettes too."
                show mayu mis
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-114.ogg"
                ma "Sometimes he'll even get two orders of them because he thinks one is too small."
                pf "He does eat an ungodly amount of food."
                show mayu smi
                "Mayu giggles."
        
            "Eh, neither of these sound great…":
                $ E3MAS3_Order = "Katsu"
                pf "Hm…"
                "I study the menu some more. There's nothing that really stands out so I randomly select one."
                pf "I'll get the miso katsu."
                show mayu cur
                "Mayu seems surprised."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-115.ogg"
                ma "Oh, I've never tried that one."
                show mayu smi
                pf "I'll let you know if it's good."
        
        "We place our orders and then fall back into silence."
        show mayu ner
        # leaving these two lines seperate is probably the best, making sure that MC goes first
        pf "So--"
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-116.ogg"
        ma "How--"
        show mayu sur
        "We talk at the same time, then stop. Then speak simultaneously again."
        show mayu wor
        # this one can be changed to "Both of us" if deemed better
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-117.ogg"
        ma "Sorry, go ahead."
        pf "Sorry, you go."
        show mayu smi
        "Mayu grins nervously."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-118.ogg"
        ma "Please, go ahead."
        pf "Um, I was just going to ask if you've had a chance to read your manga yet."
        show mayu neu
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-119.ogg"
        ma "Not yet. My father was visiting this week. He just left earlier today."
        pf "How was that?"
        show mayu thi
        "Mayu shrugs."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-120.ogg"
        ma "It was the same as usual. He seems satisfied with my grades and our team performance."
        pf "Does he watch our matches?"
        show mayu neu
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-121.ogg"
        ma "Yeah. Not in person, but he will review the footage and will critique our performance."
        
        menu:
            "Constructive criticism is always good.":
                pf "Getting that kind of feedback must be really helpful."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-122.ogg"
                ma "Yes, of course."
                "She seems a little wistful."
                pf "You don't like it?"
                show mayu ner
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-123.ogg"
                ma "I-I do, but… well…"
                show dots:
                    xoffset 720
                    yoffset 135
                    xzoom .75
                    yzoom .75
                "She pauses."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-124.ogg"
                ma "Sometimes I wish I could enjoy my classes more here at ACE."
                pf "What do you mean?"
                show mayu neu
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-125.ogg"
                ma "Father will usually correct a lot of what I'm learning and sometimes it feels pointless to even go to classes at all." 
        
            "Wow, overbearing much?":
                pf "Wait, so he has someone record our matches just so he can tell you everything we're doing wrong?"
                pf "That's taking it to the next level."
                show mayu cur b1
                "Mayu's cheeks redden."
                show mayu ner b1
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-126.ogg"
                ma "I-It's not that bad. He just wants to make sure I'm growing as a pilot."
                pf "Well yeah, but that's why you're studying at ACE."
                show mayu neu b1
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-127.ogg"
                ma "Yes, but getting specific feedback is helpful too. When we review the footage together I can see the mistakes and can keep that in mind for next time."
                pf "Sure, but why does {i}he{/i} specifically have to tell you? I know about his reputation and that he's a great Akemi, but doesn't he trust your professors?"
                show dots:
                    xoffset 720
                    yoffset 135
                    xzoom .75
                    yzoom .75
                show mayu ner
                "She hesitates."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-128.ogg"
                ma "I've wondered about that too…"
        
            "Can we get some of that footage?":
                pf "So he's recorded every match we've had so far?"
                show mayu cur
                "She blinks."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-129.ogg"
                ma "Um, yeah."
                pf "Do you think he can give feedback for all of us? I'd be curious to hear what a distinguished Akemi has to say."
                show mayu ner
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-130.ogg"
                ma "I suppose…"
                "She doesn't seem thrilled by my request."
                pf "I mean, only if you're comfortable. He seems to already come to ACE a lot so I thought it might not be too inconvenient."
                show mayu wor
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-131.ogg"
                ma "No, that's not it. He'd be happy to share his thoughts with the team."
                pf "Then what's wrong?"
                show mayu ner
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-132.ogg"
                ma "I… Sometimes I wonder why he had me enroll in ACE instead of just training me himself. He corrects a lot of what I've learned in class anyway."
        
        pf "Have you asked him about it?"
        show exclamation:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        show mayu sur
        "Her eyes widen."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-133.ogg"
        ma "No! Of course not."
        pf "Why not?"
        show mayu ner
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-134.ogg"
        ma "It's complicated…"
        pf "How--"
        "I'm interrupted by the arrival of our food."
        show mayu neu
        "The waitress places our orders in front of us, then leaves."
        show mayu sad
        "Mayu frowns at her plate."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-135.ogg"
        ma "Oh. They forgot to add the ketchup on mine."
        
        if E3MAS3_Order == "Omurice":
            "I glance at my plate which has a distinct red squiggle over my omelette."
            pf "Mine has it. We can trade."
            show mayu neu
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-136.ogg"
            ma "No, that's okay."
        
        pf "I can go ask the waitress to fix it."
        show mayu wor
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-137.ogg"
        ma "No, no, I don't want to be a bother. It's okay if there's no sauce. I don't mind."
        "I glance at her skeptically."
        pf "Are you sure?"
        show mayu ner
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-138.ogg"
        ma "Yeah..."
        stop music fadeout 20
        "She seems a little disappointed though."
        
        menu:
            "Find a waitress anyway.":
                pf "I'll be right back. I'm going to find the waitress."
                show panic:
                    xoffset 720
                    yoffset 135
                    xzoom .75
                    yzoom .75
                show mayu wor
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-139.ogg"
                ma "N-No! Really--"
                pf "They made a mistake so they should fix it."
                "Before Mayu can protest again, I flag down the waitress and explain to her what the problem is. She's apologetic, and quickly returns with a ketchup bottle and places it on the table."
                show mayu ner b2
                "Mayu's face is beet red as she mumbles her thanks. When she tries to squeeze the ketchup onto her omelette, nothing comes out."
                show drop:
                    xoffset 720
                    yoffset 135
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-140.ogg"
                ma "Oh no…"
                pf "Here, let me help."
                "She hands me the bottle and I try to squeeze the contents out, but to no avail. I slap the bottom a few times, and after a particularly hard slap, a slosh of red sauce bloops out of the bottle and splashes everywhere."
                show shoBlush:
                    xoffset 720
                    yoffset 135
                    xzoom .75
                    yzoom .75
                show mayu sur b2
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-141.ogg"
                ma "Ah!"
                "Mayu lets out a yelp of surprise as a fleck of ketchup flies onto her shirt."
                pf "I'm sorry!"
                show mayu wor b2
                "I grab a napkin and am about to pat it to Mayu's shirt when she pushes me away."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-142.ogg"
                ma "No! T-Thank you, but I-I've got it. I'll be right back."
                "My eyes widen in horror as I realise what I was about to do. The stain was on the left side of her chest…"
                hide mayu with dissolve
                "She scoots out of the booth and hurries into the restroom."
                "I breathe out heavily as I try to keep my composure. {w}Ater a few minutes, Mayu returns."
                show mayu neu b1 at cc with dissolve
                pf "Are you okay?"
                "She nods."
                "I don't mention the stain that's still prevalent on her shirt."
        
            "If she says she's okay, then she's okay.":
                "I shrug."
                pf "If you say so."
                show mayu neu
                "I take a bite of my food and Mayu takes a bite of hers."
        
        "We silently pick at our food. I wrack my brain, trying to think of something to say. Why am I suddenly blanking? Am I that nervous?"
        show mayu ner
        "Mayu pokes uncomfortably at her food. {w}After a while, we both put down our chopsticks."
        pf "So, um, are you doing anything after this?"
        show mayu neu
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-143.ogg"
        ma "Actually..."
        pf "Oh… you have plans?"
        show mayu ner
        "Mayu looks away."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-144.ogg"
        ma "Y-Yeah."
        show mayu neu
        "The waitress comes by to clear our plates and leaves the check. I automatically reach into my pocket for my wallet, and my blood runs cold."
        "Oh no. Please tell me I did not just forget my wallet!"
        "Mayu has her card at the ready and looks at me expectantly. My face feels like it's on fire as my cheeks burn."
        pf "I'm so sorry… I can't believe this happened, but I forgot my wallet…"
        show mayu cur
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-145.ogg"
        ma "O-Oh… um, that's okay. I don't mind paying for both of us."
        pf "I'll make it up to you."
        show mayu smi
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-146.ogg"
        ma "You don't have to. Really, it's okay."
        
        if E3MAS2_Paid == 1:
            show mayu hap
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-147.ogg"
            ma "After all, you did buy me my newest manga. It's my turn to return the favour."
            
        "She smiles at me, but it still doesn't make me feel any better."
        pf "Thanks, Mayu."
        hide mayu with dissolve
        "The waitress gives me a look of disapproval while Mayu pays for our meals. I wish I could merge with the floor and disappear."
        
        stop ambient fadeout 3
        scene black with fade
        $renpy.pause(0.5)
        play ambient "audio/ambience/Campus Road.ogg" fadein 3
        scene bg campus intersection dusk with fade
        
        "Once we're outside, Mayu faces me and smiles."
        show mayu smi at cc with dissolve
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-148.ogg"
        ma "Um, thanks for today."
        pf "Yeah, thanks for hanging out with me."
        pf "I can walk you to your dorm."
        show mayu cur b1
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-149.ogg"
        ma "That's okay."
        pf "Please, it's no trouble."
        show mayu smi b1
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-150.ogg"
        ma "Oh, um, sure. If you want."
        
        stop ambient fadeout 3
        scene black with fade
        $renpy.pause(0.5)
        play ambient "audio/ambience/Campus.ogg" fadein 3
        scene bg campus main dusk with fade
        
        "It's a short walk from the cafe to her dorm. When we arrive she turns to me and she smiles again."
        show mayu smi at cc with dissolve
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-151.ogg"
        ma "Thanks again."
        "I lean in to hug her just as she brings her hand up to wave. She blinks in surprise."
        show mayu sur b1
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-152.ogg"
        ma "Oh! Sorry..."
        pf "Sorry, uh…"
        show mayu neu b1
        "It's her turn to lean in while I raise up my hand."
        pf "Oops, wait--"
        show mayu ner b1
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-153.ogg"
        ma "Um…"
        "We pull apart and settle on waving."
        show mayu smi b1
        pf "See you later."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-154.ogg"
        ma "Yeah, see you…"
        hide mayu with dissolve
        "She turns into her dorm and hurries inside. As I walk back to my bike, I try to figure out what went wrong. When we hang out just as friends we have so much fun together. She's relaxed and we don't have trouble talking. Was it just nerves?"
        scene black with fade
        "I don't know why I kept freezing up either, but it's obvious this date was a disaster. I have a feeling that I might have blown my chances with her…"
        stop ambient fadeout 3
        "Maybe we aren't meant to be together…"
        "That last thought lingers with me as I drive myself home."
        $ E3MAS3_RealCompleted = 1
        # check connection to E3D6S2
        # end
        jump E3D6S2
    
    label E3MAS3_Mock:
        
        "..."
        "She's gone silent."
        pf "Mayu? Are you still there?"
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-155.ogg"
        ma "Yeah…"
        pf "What's wrong?"
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-156.ogg"
        ma "W-Well, now I'm worried about what would happen if he says yes…"
        pf "He'll probably want to go on a date."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-157.ogg"
        ma "A d-date?!"
        pf "Well yeah… That's what you do when you're a couple."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-158.ogg"
        ma "Ahhh…"
        "Based on that nervous sound, I bet she's blushing. I can't help but smile."
        pf "Are you nervous?"
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-159.ogg"
        ma "I-I've never been on a date before. What am I supposed to do?"
        pf "Just be yourself. It's not much different than if you're hanging out as friends."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-160.ogg"
        ma "But what if I say something stupid?"
        pf "You'll be fine."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-161.ogg"
        ma "I don't think I can do this. I'm too nervous!"
        pf "You can do this, Mayu."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-162.ogg"
        ma "I can't! I'm so embarrassed!"
        "Her voice trembles again."
        pf "Do you want to practice with me?"
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-163.ogg"
        ma "W-What?"
        pf "You can pretend I'm Shou and we're on a date. That way you'll know what to do and you won't have to be nervous."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-164.ogg"
        ma "I don't know..."
        pf "Think of it like a simulation match to practice for the real battle!"
        "She chuckles softly."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-165.ogg"
        ma "You would do that for me?"
        pf "Of course."
        "She hesitates."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-166.ogg"
        ma "If it's not too much trouble, I think that would be very helpful."
        pf "Sure, it's no problem."
        pf "Should we meet at the cafe?"
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-167.ogg"
        ma "Um, well, there's usually a lot of people there…"
        pf "Hm…"
        "I don't want to suggest her dorm. I doubt she'd be okay with that. There's no one home, but I wonder if she'll get the wrong impression if I suggest my own house. {w}I guess there's only one way to find out."
        pf "You can come over to my house if you like."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-168.ogg"
        ma "Y-Your house?!"
        pf "We can stay in the kitchen and pretend we're at a restaurant. Nobody is home at the moment so you don't have to worry about people staring."
        "She's quiet."
        pf "If you're not comfortable that's okay too--"
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-169.ogg"
        ma "Okay."
        pf "Okay?"
        "She takes a deep breath."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-170.ogg"
        ma "Y-Yeah, we can go to your house."
        "I give her the address."
        pf "I'll see you in a few minutes, then?"
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-171.ogg"
        ma "Yeah, see you soon."
        "We hang up, and I try to clean up the house a little more before Mayu arrives."
        stop music fadeout 3
        scene black with fade
        scene bg homekaito main day with fade
        "I pace restlessly around the house, checking for nothing and everything. Why am I so jittery? We are just two friends hanging out together… as friends… in my house… alone..."
        # sfx?
        "The sound of the doorbell startles me and my heart beats frantically."
        "It's just Mayu. Your friend."
        "I open the door and Mayu smiles nervously at me."
        show mayu smi at cc with dissolve
        pf "Hey, come on in."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-172.ogg"
        ma "Thanks."
        "She slowly steps inside and glances about the living room."
        play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-173.ogg"
        ma "You have a beautiful home."
        pf "Thanks, it's not really mine."
        show mayu cur
        "She looks at me curiously."
        pf "I mean, it's my uncle's."
        show mayu neu
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-174.ogg"
        ma "Oh, right."
        "We stand awkwardly in the doorway."
        pf "Uh, okay. So, I guess what kind of date do you want to pretend to go on?"
        show mayu ner
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-175.ogg"
        ma "Ummm…"
        "She seems unsure."
        pf "Would you like to go to dinner with me? The restaurant is really close. Right around the corner, actually."
        "I point to the kitchen."
        show mayu smi
        "Mayu grins."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-176.ogg"
        ma "That sounds lovely."
        "I lead her towards the kitchen."
        pf "I hope they have space for a last minute reservation."
        show note:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        "Mayu giggles as she slides into a seat at the table."
        pf "Would you like a water or anything to drink?"
        "She shakes her head."
        show mayu mis
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-177.ogg"
        ma "I thought you were supposed to be my date, not my waiter."
        "I blink at her joke. Mayu seems a lot more relaxed than when she walked in, which helps me relax too. I grin and slide into the seat opposite her."
        pf "You're right. How rude of me."
        show mayu neu
        "There's another pause. Mayu fidgets in her seat."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-178.ogg"
        ma "Um…"
        pf "Hm?"
        show mayu ner
        "I glance at her, and she shies away from my gaze. She twists her hands in her lap and looks around the kitchen."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-179.ogg"
        ma "Umm…"
        "Suddenly, she sighs."
        show mayu sad
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-180.ogg"
        ma "I'm hopeless!"
        pf "Why do you say that?"
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-181.ogg"
        ma "We've only just started and I already have nothing to say…"
        pf "Just relax. Don't think about it so hard."
        show mayu wor
        "Mayu takes a deep breath."
        show storm:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        show mayu sad
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-182.ogg"
        ma "I still don't know what to say…"
        pf "It's okay, let the conversation flow naturally. You and Shou hang out all the time, right?"
        show mayu neu
        "She nods."
        pf "Being on a date isn't much different than hanging out as friends."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-183.ogg"
        ma "Okay…"
        pf "What do you and Shou usually talk about?"
        show mayu thi
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-184.ogg"
        ma "Umm, I don't know…"
        "She wrinkles her brow."
        
        if (E3MAS3_RomanticMock == 0):
            ##LINE MISSING voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-.ogg"
            voice "audio/voice/MISSING/BATCH8/Missing Mayu-03.ogg"
            
            ma "I-I can't think of anything! But I know we talk when we're together."
        
        if (E3MAS3_RomanticMock == 1):
            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-185.ogg"
            ma "I-I can't think of anything! But now that I think about it, it's usually Shou who does all the talking…"
        
        pf "Don't worry. Let's just start talking and see where the conversation takes us."
        pf "How about we start with…"
        
        menu:
            "Music.":
                pf "So, have you played any music on your violin lately?"
                show mayu cur
                "Mayu blinks in surprise."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-186.ogg"
                ma "You want to talk about music?"
                pf "Well, sure. After all, I know that you like that."
                show mayu neu
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-187.ogg"
                ma "Y-Yeah..."
                show mayu ner
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-188.ogg"
                ma "Sorry! I was just surprised because Shou never has much to say about music."
                pf "Oh, um, do you not want to talk about this then?"
                show mayu sur
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-189.ogg"
                ma "No, it's okay!"
                show mayu ner b1
                "She blushes and twists the tablecloth in her hands."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-190.ogg"
                ma "I actually started composing a new song for us…"
                pf "Really?"
                show mayu neu b1
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-191.ogg"
                ma "I was thinking about Mitsuki joining the band and I got inspired. We can do a lot with her voice."
                pf "Does that mean you've been working on parts for all of us?"
                show mayu smi b1
                "Mayu nods."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-192.ogg"
                ma "I hope to have it completed before our next practice session. I don't know if it's any good though!"
                "I'm impressed. We've free-played during our jams many times before, always feeding off of each other, but this is the first time she's written down her ideas in composition."
                pf "I'm sure it will be."
        
            "Books.":
                pf "Have you had a chance to start your new manga?"
                show mayu smi
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-193.ogg"
                ma "Actually, I did."
                "She smiles."
                pf "How do you like it?"
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-194.ogg"
                ma "It started off a little bit slow because they were introducing a lot of characters, but now that they're finally focusing on the main character it's gotten very interesting."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-195.ogg"
                ma "She joined the symphony orchestra after graduating high school and quickly moved up to first chair. I've just gotten to the point where her mother is sick."
                pf "Oh no…"
                show mayu neu
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-196.ogg"
                ma "Yeah, she moved out of her hometown because of her job, but since her mom is sick she feels obligated to move back home."
                pf "What about her job?"
                show mayu sad
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-197.ogg"
                ma "She'll have to quit…"
                pf "That's a tough decision."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-198.ogg"
                ma "Yeah."
                pf "What would you choose?"
                show mayu cur
                "She blinks at me in surprise."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-199.ogg"
                ma "Oh--Um--Well, I'd choose family, of course."
                show mayu neu
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-200.ogg"
                ma "What about you?"
            
                menu:
                    "Family.":
                        "Well, considering the fact that after my parents' death I dropped everything and followed Nikki to Japan, I think the answer is obvious."
                        pf "I'd choose family too. It's easier to start over when you have people who already love and support you."
                        show mayu smi
                        "Mayu smiles."
                        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-201.ogg"
                        ma "I think that would be true too."
            
                    "Career.":
                        "It's my life to live and I need to think about what that means for my future."
                        pf "I'd probably choose my career, to be honest."
                        show mayu cur
                        "Mayu blinks."
                        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-202.ogg"
                        ma "How come?"
                        show mayu neu
                        pf "Family is important, but I can't live my life based upon the wants and needs of other people. I only have one life and I need to live it the way I want."
                        pf "It'd be hard to give up my dream, especially after I've achieved it."
                        show mayu ner
                        "Mayu looks down."
                        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-203.ogg"
                        ma "I see… I'm a little envious of that mindset."
                        "I forgot that Mayu is following in her family's footsteps, putting her music second to her piloting career."
                        pf "Of course, that choice is not for everyone, and it's not wrong to choose something else."
                        show mayu neu
                        "She nods."
            
                    "I'd make it work.":
                        "I shrug."
                        pf "I'd find a way to balance work and my family obligations."
                        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-204.ogg"
                        ma "It's not always that easy…"
                        pf "No, but it's not impossible either."
                        show mayu ner
                        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-205.ogg"
                        ma "I suppose not…"
            
                show mayu cur
                "Mayu looks at me a little strangely."
                pf "What is it?"
                show panic:
                    xoffset 720
                    yoffset 135
                    xzoom .75
                    yzoom .75
                show mayu sur b1
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-206.ogg"
                ma "Sorry! I didn't mean to stare."
                show mayu ner b1
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-207.ogg"
                ma "It's just… Shou never asks about what I'm reading. He's not very interested in books."
                show mayu smi b1
        
            "Food.":
                pf "Well, if this were a real restaurant you would have a menu. If you really can't think of anything to talk about you can always fall back on food."
                show mayu smi
                "She seems to relax a bit."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-208.ogg"
                ma "That's true."
                pf "Um, I kind of already ate the leftovers, but… how about some snacks?"
                "I scoot out of my chair and rummage through the cabinets."
                pf "We've got senbei, mochi, Pooki, peanut butter cuppes--"
                show mayu cur
                "Mayu blinks."
                show question:
                    xoffset 720
                    yoffset 135
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-209.ogg"
                ma "Peanut butter cuppes?"
                pf "Yeah, they're a really popular candy in the States! Nikki loves them and can eat a whole bag by herself. I think she might have a problem…"
                show mayu smi
                "Mayu giggles."
                pf "I'm not sure where she found these, but they're really good. Do you want one?"
                show mayu sur
                "Her eyes widen."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-210.ogg"
                ma "Oh, no, I can't!"
                pf "Don't worry, Nikki won't notice if she's missing one or two."
                show mayu wor
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-211.ogg"
                ma "Sorry, I can't because I'm allergic to peanuts."
                "I blink."
                pf "Really?"
                show mayu neu
                "She nods."
                pf "Sorry! I had no idea."
                show mayu smi
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-212.ogg"
                ma "It's okay."
                pf "Well, would you like a different snack?"
                show mayu neu
                "She shakes her head."
                voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-213.ogg"
                ma "Thanks, but I ate earlier."
                "I nod."
                show mayu smi
                pf "No problem. I did too."
        
        "Mayu seems to be in better spirits now that I've gotten her talking."
        pf "That wasn't so bad, right?"
        show mayu hap
        "She smiles."
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-214.ogg"
        ma "No, it was nice, actually."
        pf "I'm glad. Let's see… what else do people do on dates…"
        show mayu cur
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-215.ogg"
        ma "Go to movies?"
        pf "Yes! Good idea."
        pf "I'll take care of the check, and then we can head over to the \"movie theater\"."
        show mayu smi
        "Mayu giggles."
        show note:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-216.ogg"
        ma "Thank you."
        show mayu cur b1
        "I hold out my arm for her to take, which she does after a moment's hesitation."
        show mayu smi b1
        "Her cheeks turn pink and she looks away, but there's a smile on her lips. {w}We walk the few steps back into the living room and I lead her to the couch."
        pf "We've got a lot of different movies and shows. Is there something in particular you feel like watching?"
        show mayu thi
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-217.ogg"
        ma "Hmmm…"
        "I try to remember which genres Mayu like…"
        
        label E3MAS3_GenreChoice:
            
            menu:
                "Fantasy." if MCStory != 3:
                    jump E3MAS3_Fantasy
                    
                "{color=#00ff00}{b}Fantasy.{/b}{/color}" if MCStory == 3:
                    label E3MAS3_Fantasy:
                        
                        if E2D5MA_MayuScene == 1:
                            "I remember during the party at Shou's place that Mayu told me she likes to read fantasy books. Maybe her tastes in movies are similar."
                        
                        pf "I think Nikki downloaded the latest {i}Harriett Pilot{/i} movie too."
                        show exclamation:
                            xoffset 720
                            yoffset 135
                            xzoom .75
                            yzoom .75
                        show mayu cur
                        "She perks up."
                        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-218.ogg"
                        ma "Is that the one about Harry's granddaughter?"
                        pf "I think so. Have you read the book?"
                        show mayu smi
                        "Mayu nods."
                        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-219.ogg"
                        ma "Yeah, I was a little skeptical because this is the author's daughter who's revived the series, but I was pleasantly surprised. It keeps you on your toes as much as the original series did!"
            
                        if MCStory == 2:
                            pf "I agree to a certain extent. I feel as if the daughter is trying to overcompensate on world building, and sometimes includes features or items that feel a little forced. But her character relationships are very solid."
                            show mayu ske
                            "Mayu cocks her head to the side as she ponders what I said."
                            show mayu neu
                            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-220.ogg"
                            ma "Hm, yeah, I can see where you're coming from…"
                        
                        else:
                            pf "I read it too and I thought it was good."
            
                        pf "Should we watch this then?"
                        show mayu hap b1
                        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-221.ogg"
                        ma "Yes, please!"
                        show shoBlush:
                            xoffset 720
                            yoffset 135
                            xzoom .75
                            yzoom .75
                        show mayu sur b2
                        "She blushes at her outburst."
                        show mayu ner b2
                        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-222.ogg"
                        ma "I-I mean, if you want to that's fine with me."
                        $ E3MAS3_Genre = "Fantasy"
            
                "Horror.":
                    pf "Let's see what horror titles I have."
                    show mayu sur
                    "Mayu's eyes widen."
                    show frightful:
                        xoffset 720
                        yoffset 135
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-223.ogg"
                    ma "H-Horror?!"
                    pf "You don't like that?"
                    show mayu thi
                    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-224.ogg"
                    ma "I-I… um, it's okay…"
                    "The worry in her eyes is evident and she plays with the seam of her shirt."
                    pf "Sorry, I chose it because it's a common movie genre for dates."
                    show mayu cur
                    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-225.ogg"
                    ma "Really? How come?"
            
                    menu:
                        "It's kind of embarrassing to say.":
                            pf "Well… uh…"
                            show mayu neu
                            "\"Because there's a good chance she'll want to cuddle or be close to the guy if she gets scared.\". {w}It sounds a lot creepier if I say that outloud."
                            "My cheeks burn and I can't look Mayu in the eyes."
                            pf "I'm not sure."
                            show mayu ske
                            "She seems confused."
            
                        "You'll see!":
                            pf "let's watch a horror film and you'll know why!"
                            show mayu neu
                            "Mayu seems unsure."
            
                        "I'll tell her the truth.":
                            pf "A lot of times the girl will want to be close to the guy when she gets scared."
                            show mayu neu
                            voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-226.ogg"
                            ma "Oh…"
                            "She seems unsure."
            
                    pf "We don't have to watch one if you don't want to. What do you usually like to watch?"
                    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-227.ogg"
                    ma "I like fantasy, but…"
                    show mayu ner
                    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-228.ogg"
                    ma "I-If these are the types of movies couples watch on dates, then maybe we should watch it."
                    show mayu smi
                    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-229.ogg"
                    ma "After all, the whole point is to get me comfortable with going on dates."
                    pf "True, okay."
                    $ E3MAS3_Genre = "Horror"
            
                "Romantic comedy." if E3MAS3_RomCom != 1:
                    pf "Do you like romantic comedies?"
                    show mayu smi
                    "Mayu smiles."
                    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-230.ogg"
                    ma "I don't watch too many of them, but some of them are nice."
                    pf "I'm pretty sure Nikki has almost every single rom-com ever created. We can watch one of those."
                    show mayu ner b1
                    "Mayu seems a little nervous."
                    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-231.ogg"
                    ma "Won't it be a little… um…"
                    pf "A little what?"
                    show mayu ner b2
                    "She begins to blush."
                    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-232.ogg"
                    ma "Um… a little…"
                    show dots:
                        xoffset 720
                        yoffset 135
                        xzoom .75
                        yzoom .75
                    "I wait for her to finish, but she gives up."
                    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-233.ogg"
                    ma "I don't know."
                    pf "We don't have to watch it if you don't want to. I thought maybe you'd like it."
                    show mayu wor b2
                    voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-234.ogg"
                    ma "It might be too embarrassing…"
                    show mayu smi b1
                    pf "Okay, we'll pick something else."
                    $ E3MAS3_RomCom = 1
                    jump E3MAS3_GenreChoice
        
        "After selecting the movie, I stream it to my TV and Mayu and I settle into the couch to watch."
        
        #black screen
        scene black with fade
        "We end up chatting through most of the movie anyway. Mayu is all smiles and she laughs at my jokes… even the stupid ones! As predicted, once she was comfortable and relaxed, the conversation flowed easily."
        
        stop music fadeout 5
        if E3MAS3_Genre == "Fantasy":
            "We got into an in depth discussion about whether or not magic and GEARs could really be used together like in the {i}Harriett Pilot{/i} books. At one point, Mayu moved her arm and accidentally knocked over the remote. We both reached for it at the same time and our hands touched. I'd never seen her face so red before."
        
        elif E3MAS3_Genre == "Horror":
            "The film featured a family who was haunted by the ghost of their deceased child. When the ghost first popped onto the screen, Mayu was so startled she clung to my arm and hid her face. When she noticed what she'd done, her face turned bright red and she quickly created space between us on the couch."
            
        scene bg homekaito main dusk with fade
        "We continue to chat long after the movie is over, and before we realise it, the sun is beginning to set."
        show mayu cur b1 at cc with dissolve
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-235.ogg"
        ma "Ah! It's getting pretty late."
        "I glance at the time in surprise. I can't believe it's already been a few hours. It only feels like we've been together for a couple of minutes."
        play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 5
        show mayu smi b1
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-236.ogg"
        ma "I had a nice time, although I'm not sure if I actually learned much about what to expect on a date."
        show regBlush:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        show mayu smi b2
        "Mayu looks at me and blushes."
        "I pretend to look disappointed in myself."
        pf "I've failed as a teacher."
        show mayu wor b2
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-237.ogg"
        ma "Don't say that! I just was not a good student..."
        
        if (E3MAS3_RomanticMock == 1):
            "To my surprise, her gaze locks onto mine and she doesn't look away."
            "My heart pounds in my chest as the blood rushes to my face. Mayu's face is just as red."
            
        play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
        "A loud vibration interrupts us. Mayu pulls out her phone."
        show mayu sad b1
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-238.ogg"
        ma "Oh no! I forgot I promised my father I was going to send him a report of our match this week. I told him I'd get it to him today it but I haven't started it yet..."
        "I nod."
        pf "Alright, don't let me keep you."
        
        "She looks apologetic as she stands up to gather her things."
        show mayu smi b1
        voice "audio/voice/E3/Free/MA/S3/mayu/Mayu Arc-239.ogg"
        ma "Thanks again."
        "I smile."
        pf "No problem."
        hide mayu with dissolve
        "Mayu heads out before it gets too late. {w}This was the most fun I've had in a long time."
        stop music fadeout 7
        scene black with fade
        if (E3MAS3_RomanticMock == 1):
            $ mayrelatonship = 1
            "Still, I wonder what would have happened if the phone call hadn't interrupted us..."
            "I try to shrug away the thought."
        
        "The \"date\" might not have gone the way I'd planned, but I'd still consider it a success. Mayu managed to feel comfortable in a more intimate setting, and hopefully she picked up a few tricks too!"
        $ E3MAS3_MockCompleted = 1
        # check connection to E3D6S2
        # end
        jump E3D6S2

