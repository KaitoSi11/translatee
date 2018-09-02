#
label E3D2S4:
    
    #fade in
    
    $renpy.pause(1.5)
    play ambient "audio/ambience/beach evening.ogg" fadein 5
    scene bg vacation beach dusk with Dissolve(2.5)
    
    "The sun kisses the horizon, spilling orange light over the waves."
    
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
    
    "Akira and Mei left right after the splash war to join their friends. {w}Valerie is lounging on her towel, trying to soak up the last of the dying rays while reading from her ereader. {w}Yuuna sits on the sand, watching the waves lap at her feet. {w}Kaori looks thoughtful as she sits in her fold-up chair, tossing and catching an inflatable beach ball."
    "Shou and Mayu are missing… I'm not sure where they went."
    "The day is winding down and it'll be dark soon."
    
    #call SocialLink_Check
    
    menu:
        "Let's head home.":
            pf "Hey, it's going to get dark soon. Maybe we should start packing up."
            "Kaori and Valerie glance at the sky."
            show valerie smi at l2 with dissolve
            voice "audio/voice/E3/D2/S4/valerie/E3D2L24.ogg"
            vb "Mm, I suppose so. I doubt I'll get any tanner than I am now."
            show kaori smi at r2 with dissolve:
                xzoom -1
            voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_31.ogg"
            ki "Good idea. I'll go get Yuuna."
            pf "I'll find Shou and Mayu and let them know we're leaving."
            hide kaori
            hide valerie
            with dissolve
            jump E3D2S5
    
        "I want to spend a little more time with [highSocialLink]" if highSocialLink != "None":
            if highSocialLink == "Valerie":
                "I sit down beside Valerie."
                show valerie neu at cc
                pf "What are you reading?"
                show valerie smi at cc
                "Valerie grins and shows me her e-reader. I squint at the text."
                "{i}\"Oh Pierre, you shouldn't have come.\" Danielle sighed while staring longingly into Pierre's eyes, deep brown like rich chocolate.{/i}"
                "{i}\"I had to see you again,\" he said, clutching her hand to his impeccably chiseled pecs.{/i}"
                "{i}\"But what if he sees us!\" Danielle couldn't bear to think of what she'd do if anything happened to Pierre.{/i}"
                "{i}\"I don't care! The thought of being without you is too painful.\" He drew her in close and Danielle melted into Pierre's sturdy chest.{/i}"
    
                menu:
                    "That's…nice?":
                        pf "You have interesting taste in books."
                        show valerie ske at cc
                        voice "audio/voice/E3/D2/S4/valerie/E3D2L25.ogg"
                        vb "Does that mean you liked it?"
                        pf "Uh, it's not really my thing, but I'm sure if I'd read it from the beginning it'd be more enjoyable."
                        show note:
                            xoffset 720
                            yoffset 125
                            xzoom .75
                            yzoom .75
                        show valerie hap at cc
                        "Valerie laughs."
                        voice "audio/voice/E3/D2/S4/valerie/E3D2L26.ogg"
                        vb "No, it wouldn't."
                        pf "You mean you don't like it?"
                        show valerie ann at cc
                        voice "audio/voice/E3/D2/S4/valerie/E3D2L27.ogg"
                        vb "Ugh, no, this is awful!"
                        pf "Then why are you reading it?"
    
                    "We could make our own romance.":
                        pf "Let me guess--if I read any further I'll discover that the two of them will rip off each other's clothes and engage in the throes of passion?"
                        show valerie thi at cc
                        "Valerie pretends to pout."
                        show valerie ske at cc
                        voice "audio/voice/E3/D2/S4/valerie/E3D2L28.ogg"
                        vb "Wow, spoilers! Have you read one of these before?"
                        pf "You know, you don't have to read about someone else's romance. We could make our own romance right here."
                        show valerie hap at cc
                        voice "audio/voice/E3/D2/S4/valerie/E3D2L29.ogg"
                        vb "Oh, but you're wrong. I do have to read this."
                        "She didn't even acknowledge my suggestion. {w}I sigh."
                        pf "Why?"
    
                    "What has been seen cannot be unseen.":
                        pf "I wish I could unread what I just read."
                        show note:
                            xoffset 720
                            yoffset 125
                            xzoom .75
                            yzoom .75
                        show valerie hap at cc
                        "Valerie laughs."
                        voice "audio/voice/E3/D2/S4/valerie/E3D2L30.ogg"
                        vb "Aw, it wasn't {i}that{/i} bad!"
                        pf "It really was. You like that kind of thing?"
                        show valerie thi at cc
                        voice "audio/voice/E3/D2/S4/valerie/E3D2L31.ogg"
                        vb "Not particularly."
                        pf "Then why are you reading it?"
    
                show valerie smi at cc
                voice "audio/voice/E3/D2/S4/valerie/E3D2L32.ogg"
                vb "It's what you do when you go to the beach. In fact, the only thing missing right now is a fruity cocktail and a cute boy to bring it to me."
                pf "Sorry, I don't have any fruity cocktails on me."
                show valerie hap at cc
                voice "audio/voice/E3/D2/S4/valerie/E3D2L33.ogg"
                vb "Too bad. I guess these novels will have to do."
                pf "I'm not sure reading trashy romance novels at the beach is a thing."
                show valerie neu at cc
                voice "audio/voice/E3/D2/S4/valerie/E3D2L34.ogg"
                vb "No? Maybe it's just something I picked up from my aunt. She used to take me to fun places like the zoo or the beach when my mom was too… {i}busy{/i}."
                show dots:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                "That last word was emphasised with bitterness."
                show valerie smi at cc
                voice "audio/voice/E3/D2/S4/valerie/E3D2L35.ogg"
                vb "Anyway, as soon as we got to the beach, she'd sit beneath the umbrella and open up her novels while I'd build a sandcastle or something."
                pf "Sandcastle sounds way more fun to be honest."
                show valerie mis at cc
                voice "audio/voice/E3/D2/S4/valerie/E3D2L36.ogg"
                vb "It is. I should be doing that instead."
                "She glances at the darkening sky."
                show valerie smi at cc
                voice "audio/voice/E3/D2/S4/valerie/E3D2L37.ogg"
                vb "Although, I doubt building a sand castle is easy in the dark."
                pf "I guess we should start packing up."
                pf "I'll go get Shou and Mayu."
                show valerie hap at cc
                voice "audio/voice/E3/D2/S4/valerie/E3D2L38.ogg"
                vb "Alright, I'll tell Kaori and Yuuna."
                hide valerie with dissolve
                jump E3D2S5
    
            elif highSocialLink == "Yuuna":
                "I walk over to Yuuna."
                show yuuna neu at cc
                pf "Hey, Yuuna. What are you up to?"
                show yuuna sur at cc
                "She squints up at me, then smiles."
                show yuuna hap at cc
                voice "audio/voice/E3/D2/S4/yuuna/23.ogg"
                ym "Watching the fish swim."
                show yuuna smi at cc
                voice "audio/voice/E3/D2/S4/yuuna/24.ogg"
                ym "When I was little, my family took me on vacation to a beach where the fish would nibble at our toes. I felt like a mermaid swimming while the fish followed me."
                pf "Oh, so you do know how to swim."
                show yuuna cur at cc
                "Yuuna glances at me with a curious expression."
                voice "audio/voice/E3/D2/S4/yuuna/25.ogg"
                ym "Of course. Why wouldn't you think so?"
                pf "You just seemed really nervous about going into the water earlier today."
                show yuuna ner at cc
                "She hugs herself."
                voice "audio/voice/E3/D2/S4/yuuna/26.ogg"
                ym "Well, obviously I had my reasons for being nervous, but actually, I used to love swimming in the ocean when I was younger."
                show yuuna smi at cc
                voice "audio/voice/E3/D2/S4/yuuna/27.ogg"
                ym "I used to race and win all the time."
                pf "Well, how about we race?"
                show yuuna thi at cc
                voice "audio/voice/E3/D2/S4/yuuna/28.ogg"
                ym "I don't know if that's such a good idea…"
    
                $ E3D2S4_SwimFast = 0
                
                menu:
                    "Don't be scared.":
                        pf "It's okay if you're scared to lose…"
                        show yuuna dis at cc
                        voice "audio/voice/E3/D2/S4/yuuna/29.ogg"
                        ym "I wouldn't lose."
                        pf "Then what's holding you back? Your swimsuit?"
                        show drop:
                            xoffset 720
                            yoffset 100
                            xzoom .75
                            yzoom .75
                        "She seems uneasy."
                        pf "It stayed on for the rest of the time we were moving around in the water. I doubt you'll have anymore trouble."
                        show yuuna neu at cc
                        voice "audio/voice/E3/D2/S4/yuuna/30.ogg"
                        ym "Hm, that's true… Okay! You're on!"
                        show yuuna smi at cc
    
                    "Girls can't swim fast anyway.":
                        $ E3D2S4_SwimFast = 1
                        pf "I'm sure it's really intimidating to go against someone like me anyway."
                        show yuuna ske at cc
                        voice "audio/voice/E3/D2/S4/yuuna/31.ogg"
                        ym "Someone like you?"
                        pf "You know… a guy."
                        show yuuna dis at cc
                        "Yuuna pushes herself to her feet and wades into the water."
                        show yuuna mis at cc
                        voice "audio/voice/E3/D2/S4/yuuna/32.ogg"
                        ym "Oh yeah? I'll race you, and I'll beat you!" 
    
                    "We don't have to.":
                        "I shrug."
                        pf "It was just a suggestion. It's getting late anyway, so maybe we should head back."
                        show yuuna smi at cc
                        "Yuuna nods."
                        voice "audio/voice/E3/D2/S4/yuuna/33.ogg"
                        ym "You're right."
                        pf "I'll go get Shou and Mayu. Why don't you tell Valerie and Kaori?"
                        voice "audio/voice/E3/D2/S4/yuuna/34.ogg"
                        ym "Okay."
                        jump E3D2S5
    
                pf "Okay, how about the first one to that rock wins?"
                pf "Ready?"
                "Yuuna nods."
                hide yuuna with dissolve
                "At my signal, we push off."
    
                if MCStory == 1:
                    "We're neck and neck at the start, but as the race continues I'm able to gain a little more distance. It's a close race, but I end up reaching the rock first."
                    show yuuna smi at cc with dissolve
                    voice "audio/voice/E3/D2/S4/yuuna/35.ogg"
                    ym "I guess I'm out of practice."
                    "She smiles as she catches her breath."
                    pf "You stayed close to me the whole time."
    
                else:
                    "We're neck and neck at the start, but as the race continues she's able to gain a little more distance. It's a close race, but Yuuna ends up reaching the rock first."
    
                    if E3D2S4_SwimFast == 1:
                        show yuuna mis at cc with dissolve
                        voice "audio/voice/E3/D2/S4/yuuna/36.ogg"
                        ym "How's that for not being able to swim fast?"
                        "I gasp between breaths."
                        pf "Too fast…"
                        show yuuna hap at cc
                        "Yuuna giggles."
                    else:
                        show yuuna hap at cc with dissolve
                        pf "Looks like you've still got it!"
                        show yuuna smi at cc
                        "She smiles as she catches her breath."
                        voice "audio/voice/E3/D2/S4/yuuna/37.ogg"
                        ym "It was a close race."
    
                show yuuna cur at cc
                "She glances at the sky overhead."
                show yuuna smi at cc
                voice "audio/voice/E3/D2/S4/yuuna/38.ogg"
                ym "It's getting dark. Maybe we should head back."
                pf "Yeah, I'll get Shou and Mayu."
                show yuuna hap at cc
                voice "audio/voice/E3/D2/S4/yuuna/39.ogg"
                ym "Okay, I'll tell Valerie and Kaori."
                hide yuuna with dissolve
                "I nod and we swim back to shore."
                jump E3D2S5
    
            elif highSocialLink == "Kaori":
                "I walk over to Kaori."
                show kaori neu at cc with dissolve
                pf "Hey, Kaori. What are you up to?"
                "In response, she throws the ball at me!"
    
                if MCStory == 1:
                    "The ball travels slowly in the air and lands gracefully in my hands."
                    show kaori smi
                    voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_32.ogg"
                    ki "Nice catch."
                    pf "Thanks."
    
                else:
                    
                    $ qtebase = 3
                    $ qtetotal = qteath + qtebase
                    $ t_var = qtetotal
                    show screen timer_scr(place="E3D2S4_Freeze")
                    
                    menu:
                        "Freeze...":
                            label E3D2S4_Freeze:
                                $ renpy.hide_screen ("timer_scr")
                                "Startled, I'm too slow to react and the ball hits my face before it lands in my hands."
                                show kaori dis at cc
                                "Kaori frowns."
                                voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_33.ogg"
                                ki "I thought you'd able to catch that."
                                pf "You caught me by surprise."
    
                        "Miss...":
                            $ renpy.hide_screen ("timer_scr")
                            "I reach out my hands but the ball floats gently onto the sand."
                            show kaori ske at cc
                            "Kaori frowns as I pick it up."
                            voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_34.ogg"
                            ki "That wasn't a hard throw..."
                            pf "I guess I misjudged it."
    
                        "Catch!":
                            $ renpy.hide_screen ("timer_scr")
                            "The ball travels slowly in the air and lands gracefully in my hands."
                            show kaori smi
                            voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_35.ogg"
                            ki "Nice catch."
                            pf "Thanks."
    
                show kaori neu at cc
                "She seems distracted."
                pf "Are you okay?"
                voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_36.ogg"
                ki "...Yeah."
                "She doesn't say anymore, but instead, looks out towards the ocean. While she's not paying attention, I toss the ball back to her. As expected, it bounces off of her chest before she catches it."
                show kaori ske at cc
                voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_37.ogg"
                ki "Wha…?"
                show kaori ann at cc
                voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_38.ogg"
                ki "Hey! Don't throw things when I'm not looking!"
                show kaori ann at cc
                "She hurls the ball back at me. Instead of catching it, I volley it back."
                show kaori cur at cc
                "Kaori blinks in surprise, but her reflexes kick in and she leaps out of her chair to return it."
                hide kaori with dissolve
                "We continue to volley the ball back and forth, hitting it further and further away from each other so the other person has to scramble to return it. Once the ball hits the ground we stop."
    
                if MCStory == 1:
                    "Although Kaori kept me on my toes, I barely feel winded. Instead, I feel invigorated."
    
                else:
                    "My breathing is heavy as I sit down to rest. Kaori did not go easy on me. She made sure I was running around the whole time."
    
                "Kaori collects the ball and comes beside me."
                show kaori smi at cc
                voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_39.ogg"
                ki "Thanks."
                pf "For what?"
                show kaori ske at cc
                voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_40.ogg"
                ki "Do I need to spell it out for you?"
                pf "Uh…"
                show storm:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori dis at cc
                "She sighs."
                voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_41.ogg"
                ki "For playing volleyball--or whatever that was--with me."
                pf "Oh, sure."
                pf "Were you hoping to play with the group?"
                show kaori neu at cc
                "She shrugs."
                voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_42.ogg"
                ki "I thought maybe it was something we could do. My sisters and I would play every time we came to the beach. It just feels off to come here and not play."
                pf "I'm glad I could help."
                show kaori smi at cc
                voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_43.ogg"
                ki "Normally, we'd play in the water, but I guess this will have to do."
                "She glances at the sky."
                show kaori neu at cc
                voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_44.ogg"
                ki "It's getting dark so we should probably head back."
                pf "Oh, okay. I'll go get Shou and Mayu."
                show kaori smi at cc
                voice "audio/voice/E3/D2/S4/kaori/e3d2_Kao_45.ogg"
                ki "Alright, I'll tell Valerie and Yuuna."
                hide kaori with dissolve
                jump E3D2S5
    
            elif highSocialLink == "Mayu":
                "I wonder where Mayu went..."
                
                scene black with fade
                scene bg vacation beach dusk with fade
                
                "I explore the beach, and it doesn't take long for me to find her sitting on a rock cliff, her feet dangling in the water."
                show mayu neu at cc with dissolve
                "She glances up at me as I sit beside her."
                show mayu smi
                voice "audio/voice/E3/D2/S4/mayu/Mayu-31.ogg"
                ma "Oh, hi."
                pf "Hello."
                "We both watch the sun dip low in the sky, gently touching the trail of fire reflected in the water. Mayu's eyes glitter from sunlight as a peaceful smile graces her lips. She looks like the picture of tranquility."
                show mayu cur
                "Mayu notices me staring, and I try to ignore the heat in my cheeks."
                
                menu:
                    "Avert your eyes.":
                        show mayu ner b1
                        "As soon as our eyes meet, we both look away."
                        show drop:
                            xoffset 720
                            yoffset 135
                            xzoom .75
                            yzoom .75
                        voice "audio/voice/E3/D2/S4/mayu/Mayu-32.ogg"
                        ma "I-I'm sorry!"
                        pf "N-No, that was my fault! I was staring."
                        show mayu cur b1
                        "Wait, that didn't come out right. She responds with surprise."
                        voice "audio/voice/E3/D2/S4/mayu/Mayu-33.ogg"
                        ma "Oh..."
                        show mayu wor b1
                        voice "audio/voice/E3/D2/S4/mayu/Mayu-34.ogg"
                        ma "Is there something on my face?"
                        "She pats her cheeks."
                
                    "Hold her gaze.":
                        show mayu ner b1
                        "As our eyes meet, she averts her gaze."
                        ### VOICE - need to split the audio
                        voice "audio/voice/E3/D2/S4/mayu/Mayu-35.ogg"
                        ma "Umm..."
                        show question:
                            xoffset 720
                            yoffset 135
                            xzoom .75
                            yzoom .75
                        voice "audio/voice/E3/D2/S4/mayu/Mayu-35_01.ogg"
                        ma "Is something the matter?"
                
                pf "No, nothing like that."
                show mayu cur b1
                voice "audio/voice/E3/D2/S4/mayu/Mayu-36.ogg"
                ma "O-Oh. What is it?"
                
                menu:
                    "The sunset was pretty.":
                        pf "I was just admiring the sunset."
                        show mayu hap
                        "Her wide smile returns."
                        show note:
                            xoffset 720
                            yoffset 135
                            xzoom .75
                            yzoom .75
                        voice "audio/voice/E3/D2/S4/mayu/Mayu-37.ogg"
                        ma "Isn't it beautiful? I love the soothing sound of the ocean and how the water stretches as far as the eye can see."
                        show mayu smi
                        "She closes her eyes, taking it all in."
                
                    "You look perfect in this light.":
                        pf "I wish I had a camera right now to capture this moment."
                        show mayu smi b1
                        voice "audio/voice/E3/D2/S4/mayu/Mayu-38.ogg"
                        ma "It is a beautiful sunset, isn't it?"
                        pf "Yes, but it can't compare to the way you look right now."
                        show mayu sur b2
                        "Mayu's cheeks turn bright red."
                        show mayu thi b2
                        voice "audio/voice/E3/D2/S4/mayu/Mayu-39.ogg"
                        ma "W-Wha? I don't know about that."
                        show mayu smi b2
                        "Mayu smiles, but looks away."
                        voice "audio/voice/E3/D2/S4/mayu/Mayu-40.ogg"
                        ma "But if you had a camera then Kaori might come and take it away."
                        "I laugh."
                        pf "It would be worth the risk."
                        show regBlush:
                            xoffset 720
                            yoffset 135
                            xzoom .75
                            yzoom .75
                        show mayu ner b2
                        "Mayu's blush deepens."
                
                    "Nothing at all":
                        pf "Really, it's nothing."
                        show mayu neu
                        voice "audio/voice/E3/D2/S4/mayu/Mayu-41.ogg"
                        ma "O-Oh. Okay, if you say so."
                        
                show mayu win b1
                # shake animation on her?
                "Mayu shivers as a breeze blows by. She hugs her knees and leans closer to me."
                show mayu smi b1
                
                menu:
                    "Lean in closer too.":
                        "I also lean in close and we end up bumping heads."
                        play sound "audio/sfx/Human/Poke_1.ogg"
                        show mayu win b1
                        voice "audio/voice/E3/D2/S4/mayu/Mayu-42.ogg"
                        ma "Ow!"
                        show mayu sad b1
                        pf "Ah, I'm so sorry!"
                        show mayu cur b1
                        "Mayu looks up at me."
                        show mayu smi b1
                        voice "audio/voice/E3/D2/S4/mayu/Mayu-43.ogg"
                        ma "No, it's okay."
                        jump E3D2S4_Shou
                
                    "Stay where I'm at.":
                        "I stay put as she leans into to me."
                        
                        label E3D2S4_Shou:
                            
                            "Her face is inches from my own. My heart races."
                            show mayu smi b2
                            "We both blink at each other, I can see her cheeks tinge with colour and I'm sure mine are too. She hasn't pulled away though..."
                            voice "audio/voice/E3/D2/S4/shou/41.ogg"
                            ss "MAYU, BROSEPH!"
                            show shocked:
                                xoffset 720
                                yoffset 135
                                xzoom .75
                                yzoom .75
                            show mayu sur b2
                            show shou smi at l3 with dissolve
                            "We both jump apart from each other as Shou approaches."
                            voice "audio/voice/E3/D2/S4/shou/42.ogg"
                            ss "I was wondering where you two went."
                            show mayu wor b2
                            voice "audio/voice/E3/D2/S4/mayu/Mayu-44.ogg"
                            ma "Um, we were just...watching the sunset..."
                            show dots:
                                xoffset 720
                                yoffset 135
                                xzoom .75
                                yzoom .75
                            show mayu ner b2
                            show shou ske
                            "She trails off and stares at the ground."
                            pf "Yeah, we wanted to catch it while we still can."
                            show mayu neu b1
                            "Mayu nods."
                            show shou hap
                            voice "audio/voice/E3/D2/S4/shou/43.ogg"
                            ss "Oh cool! When we were younger, Mayu and I used to check out the sunset while our parents talked. Too bad I missed it this time."
                            show mayu ner
                            voice "audio/voice/E3/D2/S4/mayu/Mayu-45.ogg"
                            ma "Y-Yeah…"
                            "She glances at Shou's smiling face and a shadow of guilt seems to pass over her own face."
                            show shou smi
                            voice "audio/voice/E3/D2/S4/shou/44.ogg"
                            ss "Anyway, I think the gang wants to head out since it's getting late."
                            pf "Right."
                            hide mayu
                            hide shou
                            with dissolve
                
                    "Scoot  away.":
                        "I scoot away, keeping the distance between us. Mayu doesn't seem to have noticed. I guess she only leaned in to stay warm."
                        pf "It's getting cold… Maybe we should head back?"
                        voice "audio/voice/E3/D2/S4/mayu/Mayu-46.ogg"
                        ma "Sure."
                        show mayu cur
                        "As we stand, Shou jogs towards us."
                        show shou hap at l3 with dissolve
                        voice "audio/voice/E3/D2/S4/shou/45.ogg"
                        ss "Eyyo!"
                        show mayu neu
                        pf "Shou! Where were you?"
                        show shou smi
                        voice "audio/voice/E3/D2/S4/shou/46.ogg"
                        ss "Oh, nowhere. Just trying to pick up some chicks."
                        show storm:
                            xoffset 720
                            yoffset 135
                            xzoom .75
                            yzoom .75
                        show mayu thi
                        "I think I hear Mayu sigh."
                        pf "Any luck?"
                        show shou mis
                        ### VOICE - missing line
                        voice "audio/voice/MISSING/BATCH2/2.ogg"
                        ss "You know me!"
                        pf "So, no?"
                        show mayu neu
                        show shou sad
                        "He sighs."
                        voice "audio/voice/E3/D2/S4/shou/47.ogg"
                        ss "Ehehehe... no."
                        show shou smi
                        voice "audio/voice/E3/D2/S4/shou/48.ogg"
                        ss "Anyways, let's meet up with the rest of the group."
                        show mayu smi
                        "Mayu and I nod."
                        hide mayu
                        hide shou
                        with dissolve
                        
                scene black with fade
                $renpy.pause(1)
                scene bg vacation beach dusk with fade
                show kaori neu at l3:
                    xoffset -100
                show mayu neu at r3:
                    xoffset 100
                    xzoom -1
                show shou smi at r2:
                    xzoom -1
                show valerie smi at cc
                show yuuna neu at l2 behind valerie
                with dissolve
                "Everyone was waiting for us when we rejoined the group."
                pf "You guys didn't pack up yet?"
                show yuuna smi
                ym "We figured we'd do it together since we wanted to walk to the parking lot together anyway."
                show mayu smi
                "Mayu smiles."
                voice "audio/voice/E3/D2/S4/mayu/Mayu-47.ogg"
                ma "Thanks for waiting."
                show kaori smi
                show yuuna hap
                "Yuuna nods."
                
                jump E3D2S5_Mayu
    
            elif highSocialLink == "Shou":
                "I wonder where Shou went."
                jump E3D2S5

