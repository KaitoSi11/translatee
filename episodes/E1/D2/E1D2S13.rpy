label E1D2S13:
    
    $renpy.pause(1)
    scene bg homekaito main dusk with Dissolve(2.5)
    "As soon as I open the front door, I hear a clanging in the kitchen. {w}Nikki must be home. {w}Just as I predicted, she's stirring a pot, surrounded by a mess of appliances."
    play ambient "audio/ambience/Kitchen Cooking.ogg" fadein 1
    show nikki neu at cc with dissolve
    pf "Hey, Nikki."
    show nikki cur at cc with dissolve
    show exclamation:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    "She glances up in surprise."
    show nikki hap at cc
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 1
    voice "audio/voice/E1/D2/S13/Nikki/1.ogg"
    sf "Hey! You're home early."
    pf "Am I? It's right around dinner time. {w}What are you making?"
    show nikki smi at cc
    voice "audio/voice/E1/D2/S13/Nikki/2.ogg"
    sf "Guess!"
    "I try to peek into the pot but she hides it from me."
    show nikki mis at cc
    voice "audio/voice/E1/D2/S13/Nikki/3.ogg"
    sf "No cheating!"
    
    menu:
        "My nose knows.":
            "I breathe in deeply and pause to sort the aromas lingering in the air. The dominant scent is of tomatoes, followed by meat--beef to be specific, but also a hint of celery… basil…"
            pf "You're making bolognese!"
            show nikki smi at cc with dissolve
            "She laughs and shows me the simmering sauce in the pot."
            voice "audio/voice/E1/D2/S13/Nikki/4.ogg"
            sf "Good guess!"
            pf "It was no guess. The Super Smeller knows."
            "I solemnly tap my nose."
            show nikki ske at cc
            show drop:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S13/Nikki/5.ogg"
            sf "You're so weird. Who actually names their nose?"
            pf "Laugh all you want now, but you'll be singing a different tune when the Super Smeller gets you out of danger."
            show nikki cur at cc
            show question:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S13/Nikki/6.ogg"
            sf "And why would I be in danger?"
            pf "I don't know. Maybe your enemies are planning a sneak attack against you."
            show nikki smi at cc
            "She laughs again."
            show nikki mis at cc
            voice "audio/voice/E1/D2/S13/Nikki/7.ogg"
            sf "I don't have any enemies!"
            pf "Just give it time."
            voice "audio/voice/E1/D2/S13/Nikki/8.ogg"
            sf "Rude! I am very likeable."
            "She swats my arm, and it's my turn to laugh."
            show nikki neu at cc
    
        "{color=#00ff00}{b}I already know what the answer is anyway.{/b}{/color}" if (MCStory == 3):
            jump E1D2S13_MCStory1
            
        "I already know what the answer is anyway." if (MCStory != 3):
            label E1D2S13_MCStory1:
                pf "It's bolognese."
                show nikki cur at cc with dissolve
                "Nikki blinks in surprise."
                show question:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S13/Nikki/9.ogg"
                sf "How did you figure it out so quickly?"
                pf "It's simple. First, you're using a stockpot, which means it's most likely a soup or a sauce."
                pf "Second, you're wearing an apron, which means you're making something that is either messy or stains--or both."
                pf "The cutting board has leftover slivers of different vegetables, and is still wet with freshly cut tomato juices and seeds. The knife is still stained with tomato, which means this must be a tomato-heavy sauce."
                show nikki sur at cc
                pf "There's ground beef packaging in the trash, and considering the limited ingredients you'd be able to find in Japan, I figured the most likely dish you'd be making is bolognese."
                show drop:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                "Nikki had frozen during my speech, and stares at me with wide eyes. As my words sinks in and she begins to thaw, she pouts."
                show nikki dis at cc with dissolve
                voice "audio/voice/E1/D2/S13/Nikki/10.ogg"
                sf "That's not fair! You still lose."
                pf "What? Are you not making bolognese?"
                show nikki thi at cc
                voice "audio/voice/E1/D2/S13/Nikki/11.ogg"
                sf "No, I am, but you didn't follow the rules and {i}guess{/i}. You did some weird robotic analysis thing!"
                "I flash her a confident smirk."
                pf "Nah, I'm just playing. I didn't really analyze the kitchen."
                show nikki cur at cc
                voice "audio/voice/E1/D2/S13/Nikki/12.ogg"
                sf "Oh. Then how did you know?"
                pf "I just smelled it. This house smells so good!"
                show nikki smi at cc
                "Nikki giggles, and resumes stirring."
                voice "audio/voice/E1/D2/S13/Nikki/13.ogg"
                sf "Thanks."
                show nikki neu at cc
    
        "I didn't realise we were five years old again.":
            stop music fadeout 3
            pf "Just tell me."
            show nikki smi at cc
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 1
            voice "audio/voice/E1/D2/S13/Nikki/14.ogg"
            sf "No, guess! It's easy."
            pf "If it's so easy then why won't you just tell me?"
            show nikki hap at cc
            voice "audio/voice/E1/D2/S13/Nikki/15.ogg"
            sf "Because this way is more fun! C'mon, just one guess. You can smell it and figure it out."
            pf "I hate guessing games."
            show nikki mis at cc
            voice "audio/voice/E1/D2/S13/Nikki/16.ogg"
            sf "Just one guess!"
            "I crane my neck towards the pot again, but she blocks me."
            pf "Nikki--"
            "I duck towards the other side, faking her out, and manage to peek into the pot."
            show nikki sur at cc
            voice "audio/voice/E1/D2/S13/Nikki/17.ogg"
            sf "Hey!"
            pf "It's bolognese."
            show nikki dis at cc
            show storm:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            "She pouts and goes back to stirring."
            voice "audio/voice/E1/D2/S13/Nikki/18.ogg"
            sf "You're no fun."
            show nikki neu at cc
    
        "I want my baby back, baby back, baby back, baby back…":
            stop music fadeout 3
            pf "BBQ Sauce!"
            show nikki ske at cc
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 1
            show drop:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S13/Nikki/19.ogg"
            sf "Are you kidding me right now?"
            pf "Pizza!"
            show nikki dis at cc
            voice "audio/voice/E1/D2/S13/Nikki/20.ogg"
            sf "No, you don't cook pizza in a pot."
            pf "Okonomiyaki!"
            show nikki ann at cc
            show vein:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S13/Nikki/21.ogg"
            sf "Again, not something you cook in a pot."
            pf "Suckling pig!"
            show nikki sur at cc
            voice "audio/voice/E1/D2/S13/Nikki/22.ogg"
            sf "What--"
            pf "Oden!"
            show nikki dis at cc
            show storm:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S13/Nikki/23.ogg"
            sf "No--"
            pf "Shad Roe!"
            show nikki ske at cc
            voice "audio/voice/E1/D2/S13/Nikki/24.ogg"
            sf "How do you even know what Shad Roe is?"
            pf "Fugu!"
            show nikki cur at cc
            show dots:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            $renpy.pause(2.5)
            "She just looks at me."
            show nikki dis at cc
            voice "audio/voice/E1/D2/S13/Nikki/25.ogg"
            sf "Seriously?"
            pf "... Sooooo, that's a no?"
            show nikki ske at cc
            voice "audio/voice/E1/D2/S13/Nikki/26.ogg"
            sf "How exactly did you get into the most prestigious pilot program in the country?"
            show nikki neu at cc
            "I grin at her, and she grins back."
    
    stop music fadeout 3
    pf "I'm just glad you're the one cooking and not me. Everything you make is delicious! You really have a talent for cooking, you know?"
    show nikki mis at cc
    voice "audio/voice/E1/D2/S13/Nikki/27.ogg"
    sf "Oh, shut up."
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 1
    "She tries to hold back her smile, but fails."
    show nikki neu at cc
    pf "Did you go shopping after school today? I didn't know Uncle Kaito kept all these ingredients at home."
    voice "audio/voice/E1/D2/S13/Nikki/28.ogg"
    sf "Yeah, I did. Sushi yesterday was so good, but I wanted something more hearty today, you know?"
    "Hmm, to Nikki, \"hearty\" foods are \"comfort\" foods."
    pf "Does that mean you had a bad day at school?"
    show nikki cur at cc with dissolve
    "She blinks in surprise, then laughs."
    show nikki smi at cc
    show note:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S13/Nikki/29.ogg"
    sf "Of course not! It was great. I met a lot of people at the club fair they held after school. There are so many cool clubs! Did you know they have a kendo club? You definitely wouldn't find that back home!"
    show nikki hap at cc
    voice "audio/voice/E1/D2/S13/Nikki/29_1.ogg"
    sf "I think I'm going to try out for their dance team, though, maybe run for student government."
    pf "Wow, it sounds like you've had a pretty productive day."
    show nikki neu at cc
    "She quickly checks the pasta and nods."
    show nikki smi at cc
    voice "audio/voice/E1/D2/S13/Nikki/30.ogg"
    sf "Definitely! I'm a little disappointed they don't have a cooking club, but that's okay. They offer a cooking class, which I'm taking. Soon, I'll be an expert in Japanese cuisine!"
    pf "Maybe you can start a cooking club."
    show nikki hap at cc
    voice "audio/voice/E1/D2/S13/Nikki/31.ogg"
    sf "Oooh, maybe!"
    "I begin to set the table for three, when Nikki shakes her head."
    show nikki thi at cc
    voice "audio/voice/E1/D2/S13/Nikki/32.ogg"
    sf "Didn't you see Uncle Kaito's text? He'll be home late tonight."
    pf "I haven't been checking my phone."
    "Soon the table is set, and both Nikki and I have a full portion of pasta in front of us."
    show nikki neu at cc
    voice "audio/voice/E1/D2/S13/Nikki/33.ogg"
    sf "How was your first day?"
    
    if (E1D2S11_JoinedTheTeam == 1) and (E1D2S3_MetKaoriWasNice == 1):
        pf "My day was kind of weird. It started out horribly. {w}I almost ran over this girl on my way to school, but being the gentleman that I am--"
        show nikki smi at cc
        "Nikki snorts, and I pointedly ignore her."
        pf "--I stopped to help her. I'm lucky I did that too because when I was looking for a team to join, the only one looking for members was hers."
        show nikki ske at cc
        show question:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/34.ogg"
        sf "So she let you join?"
        pf "Yup."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/35.ogg"
        sf "Lucky you."
        pf "That's what I said."
    
    elif (E1D2S11_JoinedTheTeam == 1) and (E1D2S3_MetKaoriWasRudeYesHelmet == 1):
        pf "My day was kind of weird. It started out horribly. This crazy girl jumped out in front of my bike on my way to school, and then when I was looking for a team, the only team accepting members was {i}hers{/i}!"
        show nikki cur at cc
        voice "audio/voice/E1/D2/S13/Nikki/36.ogg"
        sf "Oh man! Did she let you join?"
        pf "Yeah, but only because she doesn't know I was the guy who almost ran her down."
        show nikki sur at cc
        show shocked:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/37.ogg"
        sf "You mean you didn't stop to help her?"
        pf "No… Why would I waste my time arguing with someone who is obviously in the wrong? I just hope she doesn't figure out it was me. That'd be awkward."
        show nikki ske at cc
        show drop:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/38.ogg"
        sf "Wooooow. You'd deserve whatever she throws at you."
    
    elif (E1D2S11_JoinedTheTeam == 1) and (E1D2S3_EncounteredKaori == 0):
        pf "It was alright. I managed to join a team, which was pretty lucky considering only one team was looking for members."
        show nikki hap at cc
        show note:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/39.ogg"
        sf "That's good! What are your teammates like?"
        pf "They're all pretty… distinct. One girl is slightly terrifying, another girl is so quiet I kind of forget she's there, and the guy who recruited me… well, he's a special snowflake."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/40.ogg"
        sf "I'm not sure I believe that {i}you're{/i} the most normal person there."
    
    elif (E1D2S11_JoinedTheTeam == 0) and (E1D2S3_MetKaoriWasRudeNoHelmet == 1):
        pf "It could have been better. On my way into school, this dumb girl tried to cross the street and basically jumped in front of my bike. And the best part? She was a complete jerk to me when I stopped to check on her."
        show nikki ske at cc
        show drop:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/41.ogg"
        sf "To be fair, you probably gave her a heart attack." 
        pf "That's her fault! My light was still green. {i}Her{/i} light was red."
        show nikki thi at cc
        voice "audio/voice/E1/D2/S13/Nikki/42.ogg"
        sf "Oh… well, even so…" 
        
        if (E1D2S10_EnoughRejection == 1):
            pf "And to make matters worse, when I tried to join a team, the {i}only{/i} team looking for another member was hers."
            show nikki cur at cc
            voice "audio/voice/E1/D2/S13/Nikki/43.ogg"
            sf "Ohhhh, man. How did that go?" 
            pf "As soon as she saw me she said no."
            
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/44.ogg"
        sf "Maybe you should stop running people over?" 
        pf "It's not like I do this for fun!"
        show nikki smi at cc
        "She just laughs." 
    
    elif (E1D2S11_JoinedTheTeam == 0) and (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
        pf "It was interesting... to say the least."
        show nikki cur at cc
        voice "audio/voice/E1/D2/S13/Nikki/51.ogg"
        sf "Sounds like a good story." 
        pf "Well... It started out with me nearly running over this girl."
        show nikki sur at cc
        show shocked:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/52.ogg"
        sf "You nearly ran someone over? I knew you drove too crazy on that bike." 
        pf "It wasn't my fault! She walked out in front of me."
        show nikki ske at cc
        voice "audio/voice/E1/D2/S13/Nikki/53.ogg"
        sf "Uh huh, is she okay?" 
        pf "She was fine... At least, I thought she was fine."
        show nikki dis at cc
        show drop:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/54.ogg"
        sf "You didn't stay to find out? Wow, jerk." 
        pf "Hey, she didn't seem hurt so I didn't think it was a big deal. But then I ended up running into her later that day. She's another pilot, and her team was the only one looking for a new member."
        show nikki ske at cc
        voice "audio/voice/E1/D2/S13/Nikki/55.ogg"
        sf "Ouch. Did she let you join? After all, it sounds like she didn't see you." 
        pf "Well, she was obsessing over finding out who nearly ran her over, so I felt bad for leaving the scene like I did. Maybe she'd actually gotten hurt or something. {w}So like an idiot I confessed and apologised to her. As expected, she was furious and refused to let me on the team."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/56.ogg"
        sf "I hate to say it, but it serves you right. That's karma."
        pf "That smug smile of yours makes me think you don't hate saying that."
        show nikki smi at cc
        voice "audio/voice/E1/D2/S13/Nikki/57.ogg"
        sf "No, you're right, I loved it!"  
    
    elif (E1D2S11_JoinedTheTeam == 0) and (E1D2S3_EncounteredKaori == 0):
        pf "It was okay. No luck finding a team, though."
        show nikki wor at cc
        show panic:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/45.ogg"
        sf "No?" 
        pf "One guy offered me a space, but to be honest, he was a bit... strange. I wasn't crazy about the idea of joining him."
        show nikki neu at cc
        voice "audio/voice/E1/D2/S13/Nikki/46.ogg"
        sf "Beggars can't be choosers." 
        pf "Yeah, I guess. I was hoping that another team was looking but nobody in the Pilot's Lounge was very helpful."
        show nikki smi at cc
        voice "audio/voice/E1/D2/S13/Nikki/47.ogg"
        sf "I'm sure you can try again tomorrow."
        pf "Yeah, but it would have been better if I'd found one today."
    
    show nikki cur at cc
    voice "audio/voice/E1/D2/S13/Nikki/48.ogg"
    sf "So, it sounds like finding a team today was super important."
    pf "Oh, yeah, the qualifier is on Friday."
    show nikki sur at cc
    show frightful:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S13/Nikki/49.ogg"
    sf "But that's in two days!"
    pf "I know. Everyone else knew this in advance and formed teams over the summer."
    show nikki wor at cc
    voice "audio/voice/E1/D2/S13/Nikki/50.ogg"
    sf "Well, that's not really fair."
    pf "Yeah, but it's fine."
    show nikki neu at cc
    
    if (E1D2S2_talkwithyuunayes == 1):
        pf "In other news, I met Yuuna, this really nice girl, on the bus today."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/58.ogg"
        sf "Ooooh, do you liiiiike her? Is she gonna be your giiirrrlllfriiiiend?"
        pf "Oh shut up. She was just really helpful."
        show nikki smi at cc
        voice "audio/voice/E1/D2/S13/Nikki/59.ogg"
        sf "Oh yeeaaaah?" 
    
    if (E1D2S2_YuunaComesWithYouPass == 1):
        pf "She showed me the way to the administrative office."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/60.ogg"
        sf "Because you can't get there on your own?" 
            
        if (E1D2S5_bribedforpass == 1) or (E1D2S5_flirtforpass == 1):
            pf "I could have, or I could have spent more time with a friendly girl."
            show nikki mis at cc
            voice "audio/voice/E1/D2/S13/Nikki/62.ogg"
            sf "Of course you would choose the girl."
            pf "You know me, always the charmer."
            show nikki smi at cc
            voice "audio/voice/E1/D2/S13/Nikki/63.ogg"
            sf "Yea... Sure..." 
            pf "Don't believe me? Well, guess who managed to snag a parking pass on charms alone."
            show nikki hap at cc
            voice "audio/voice/E1/D2/S13/Nikki/64.ogg"
            sf "Yuuna?"
            pf "Very funny."
            show nikki smi at cc
            "Nikki laughs."
    
        elif (E1D2S5_bribedforpass == 0) and (E1D2S5_flirtforpass == 0):
            pf "Well, it's a good thing she did because when the receptionist gave me a hard time, Yuuna stepped in and got me the parking pass."
            show nikki smi at cc
            voice "audio/voice/E1/D2/S13/Nikki/61.ogg"
            sf "You're right, she does sound helpful." 
    
            
    if (E1D2S2_talkwithyuunayes == 1) and (E1D2S2_YuunaComesWithYouPass == 0):
        pf "Yeah, she offered to help me if I needed anything. It's nice to have someone on campus willing to help."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/65.ogg"
        sf "She doesn't know what she got herself into!" 
        
        if (E1D2S4_GoingToGetPassNoYuuna == 1):
            #This is a different variable than E1D2S2_YuunaComesWithYouPass. This one is if you did talk to yuuna, then left her, but went to get a pass on your own
            pf "I probably should have asked her the way to the permit office. Although, I did find it eventually."
            show nikki cur at cc
            voice "audio/voice/E1/D2/S13/Nikki/66.ogg"
            sf "Did you get your pass?" 
    
            if (E1D2S5_gotbikepass == 1):
                pf "Of course, I'm smooth like that. Who would say no to this face?"
                show nikki mis at cc
                voice "audio/voice/E1/D2/S13/Nikki/67.ogg"
                sf "I do, all the time."
    
            if (E1D2S5_gotbikepass == 0):
                pf "No... The administrator was a serious ass. I have to fill out a bunch of forms online before I can get it."
                show nikki ske at cc
                voice "audio/voice/E1/D2/S13/Nikki/68.ogg"
                sf "That's annoying."
                
    show nikki smi at cc
    voice "audio/voice/E1/D2/S13/Nikki/69.ogg"
    sf "Sounds like you’ve had quite the day."
    stop ambient fadeout 3
    scene black with fade
    "The conversation continues and eventually lulls to a natural close. Soon both of our plates are polished clean."
    play ambient "audio/ambience/Night Crickets.ogg" fadein 1
    scene bg homekaito main night with Dissolve(2.5)
    $renpy.pause(1)
    pf "I am so full."
    show nikki mis at cc with dissolve
    voice "audio/voice/E1/D2/S13/Nikki/70.ogg"
    sf "Who told you to be such a pig?"
    show nikki neu at cc
    "I help her with clean-up."
    pf "I think I'm going to relax for a bit, then go to bed early tonight."
    show nikki smi at cc
    voice "audio/voice/E1/D2/S13/Nikki/71.ogg"
    sf "Yeah, me too. Goodnight!"
    pf "Night."
    hide nikki with dissolve
    stop music fadeout 3
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1 fadeout 1
    scene black with fade
    $renpy.pause(1)
    "We part ways and I head into my room."
    $renpy.pause(1)
    scene bg homekaito myroom night with fade
    
    if (E1D2S5_gotbikepass == 0):
        "It's too early to go to bed, so I'll start the process for getting a parking pass. {w}Who knows how long it'll take before they mail me one, and I'd like to get it sooner rather than later."
        "I log into my weblink and find the documents to request a permit. {w}It takes me longer than I expected to fill out all of the paperwork, and it leaves me exhausted. {w}Crawling into bed, I close my eyes and soon fall asleep."
    
    else:
        "It's too early to go to bed, but I'm mentally exhausted and don't feel up to doing much. {w}I browse the internet for a while, looking up nothing in particular, until my eyes feel heavy and I drift off to sleep."
    
    scene black with Dissolve(2.5)
    
    jump E1D3S1
