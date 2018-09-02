#
label E2D6S2:
    
    #((JUMP BACK FROM WEEKEND END))
    
    $ kaiOut = "sCasual"
    
    play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    scene bg homekaito main night with fade
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
    show kaito mis at cc with dissolve
    "When I arrive home, Uncle Kaito is staring at the phone with a silly grin on his face."
    
    menu:
        "He seems happy.":
            pf "You seem to be in a good mood, Uncle Kaito."
            show exclamation:
                xoffset 720
                yoffset 5
                xzoom .75
                yzoom .75
            show kaito cur at cc with dissolve
            $renpy.pause(.5)
            show kaito smi at cc with dissolve
            "Kaito is startled by my voice, but quickly regains his cheery attitude."
            voice "audio/voice/E2/D6/S2/Kaito/1.ogg"
            hk "As a matter of fact, I am."
            pf "Any reason why?"
            show kaito hap at cc
    
        "Stare at him with the same grin!":
            "I step into his view and look at him with the same goofy grin."
            show exclamation:
                xoffset 720
                yoffset 5
                xzoom .75
                yzoom .75
            show kaito cur at cc with dissolve
            $renpy.pause(.5)
            show kaito ske at cc with dissolve
            "Kaito snaps back to reality and looks at me weirdly."
            voice "audio/voice/E2/D6/S2/Kaito/2.ogg"
            hk "What's that look for?"
            pf "I could ask you the same thing."
            show kaito hap at cc
    
        "Greet him normally.":
            pf "Hey, Uncle Kaito."
            show kaito smi at cc
            "He glances at me."
            voice "audio/voice/E2/D6/S2/Kaito/3.ogg"
            hk "You're back! How was your day?"
            pf "Good. Seems like yours was good too."
            show kaito hap at cc
            "Kaito smiles even broader."
            
    voice "audio/voice/E2/D6/S2/Kaito/4.ogg"
    hk "I just got off the phone with Yuki and I am saved!"
    pf "Saved?"
    show kaito smi at cc
    voice "audio/voice/E2/D6/S2/Kaito/5.ogg"
    hk "She called me today and apologised for going against our agreement."
    "Pieces of our last conversation resurface in my memory."
    pf "Ah, the agreement you made when you two separated."
    "Uncle Kaito nods."
    show kaito hap at cc
    voice "audio/voice/E2/D6/S2/Kaito/6.ogg"
    hk "She says that she can make the restaurant opening ceremony after all."
    pf "See! Everything worked out."
    show kaito smi at cc
    voice "audio/voice/E2/D6/S2/Kaito/7.ogg"
    hk "Yeah, I don't know what I was so worried about. Yuki has always been reliable and a true friend. Even after we separated, she was always there when I needed her."
    
    menu:
        "Sounds like you still care for her.":
            pf "It seems like you care really deeply for her."
            show kaito mis at cc
            voice "audio/voice/E2/D6/S2/Kaito/8.ogg"
            hk "Well, of course, I did love her."
            pf "Maybe you still do."
    
        "Kaito and Yuki sitting in a tree!":
            pf "Oooh, sounds like somebody has a crush!"
            show kaito mis at cc
            "Kaito raises an eyebrow."
            voice "audio/voice/E2/D6/S2/Kaito/9.ogg"
            hk "Technically, she is still my wife."
            pf "You looooove her!"
    
        "She still digs you.":
            pf "I think Aunt Yuki still has feelings for you, Uncle Kaito."
            show kaito mis at cc
            voice "audio/voice/E2/D6/S2/Kaito/10.ogg"
            hk "Of course she does. We still like each other."
            pf "No, I mean, she still loves you. Why else would she do that for you?"
            show kaito smi at cc
            voice "audio/voice/E2/D6/S2/Kaito/11.ogg"
            hk "We're still friends."
            pf "I think you might have feelings for her too."
            
    show kaito ske at cc
    voice "audio/voice/E2/D6/S2/Kaito/12.ogg"
    hk "Who do you think you are, the love doctor?"
    pf "I'm just saying--"
    show kaito neu at cc
    voice "audio/voice/E2/D6/S2/Kaito/13.ogg"
    hk "This is the way things are between Yuki and I, and this is how it needs to stay."
    pf "If you say so."
    show kaito smi at cc
    voice "audio/voice/E2/D6/S2/Kaito/14.ogg"
    hk "So, I don't want to hear any more out of you."
    pf "Alright, I trust your judgement."
    show kaito mis at cc
    voice "audio/voice/E2/D6/S2/Kaito/15.ogg"
    hk "You're grounded if you keep this up, mister!"
    pf "What? No!"
    show note:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    "Uncle Kaito laughs."
    voice "audio/voice/E2/D6/S2/Kaito/16.ogg"
    hk "I'm just messing with you."
    
    show kaito cur at cc
    voice "audio/voice/E2/D6/S2/Nikki/29.ogg"
    sf "Hello~!"
    show kaito smi at l2
    show nikki neu at r2:
        xzoom -1
    with dissolve
    "We both turn to see Nikki wearing her signature smile. As she glances over at me, her smile falters."
    show nikki sad at r2
    voice "audio/voice/E2/D6/S2/Nikki/30.ogg"
    sf "Before you say it, I'll go clean up your bike."
    show kaito ske at l2
    voice "audio/voice/E2/D6/S2/Kaito/17.ogg"
    hk "Clean up his bike?"
    show drop:
        xoffset 1040
        yoffset 160
        xzoom .75
        yzoom .75
    pf "You don't want to know."
    show kaito smi at l2
    "Kaito grins."
    voice "audio/voice/E2/D6/S2/Kaito/18.ogg"
    hk "Well, I have a bit of free time now and I'm in the mood to celebrate. Do you guys want to watch something on Netflicks?"
    show nikki hap at r2
    "Nikki perks up at the idea, then stares pleadingly at me."
    pf "Nikki--"
    show nikki sad at r2
    "Before I have a chance to speak, she pouts her lips and looks at me with puppy dog eyes."
    pf "You know that won't work."
    show crying:
        xoffset 1040
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D6/S2/Nikki/31.ogg"
    sf "...P-Please?"
    show nikki win at r2
    "Her voice chokes up."
    
    menu:
        "IT'S FUTILE TO RESIST. GIVE IN.":
            pf "Okay, fine. You can stay for {i}one{/i} episode."
            
    show nikki hap at r2
    "Nikki beams."
    show note:
        xoffset 1040
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D6/S2/Nikki/32.ogg"
    sf "Yay! Thanks bro."
    show kaito hap at l2
    "Kaito laughs at our exchange as we settle onto the couch."
    voice "audio/voice/E2/D6/S2/Kaito/19.ogg"
    hk "You are going to be in real trouble kiddo if you give in so easily to the ladies."
    show nikki mis at r2
    voice "audio/voice/E2/D6/S2/Nikki/33.ogg"
    sf "Only for me!"
    show kaito smi at l2
    "Nikki leans against me and snuggles into a comfortable position."
    pf "...What are you doing?"
    show nikki smi at r2
    voice "audio/voice/E2/D6/S2/Nikki/34.ogg"
    sf "Shush pillow."
    "I think about protesting but realise how useless that'd be."
    show kaito mis at l2
    "Kaito notices my sigh of resignation and grins."
    voice "audio/voice/E2/D6/S2/Kaito/20.ogg"
    hk "Haha! Forget about being in trouble, you're already doomed."
    show nikki neu at r2
    "I shrug. You think I'd be immune to her witchcraft after seventeen years of this..."
    show kaito smi at l2
    voice "audio/voice/E2/D6/S2/Kaito/21.ogg"
    hk "What do you guys want to watch?"
    
    label E2D6S2_Netflicks:
        menu:
            "Gear of Thrones." if E2D6S2_Thrones == 0:
                pf "{i}I am Stennis of House Gearatheon, First of my Name, King of the Andols and the First Men, Lord of the Eight Kingdoms, and Guardian of the Realm.{/i}"
                show kaito hap at l2
                voice "audio/voice/E2/D6/S2/Kaito/22.ogg"
                hk "Gear of Thrones!"
                show nikki ske at r2
                "We grin at each other while Nikki looks perplexed."
                show question:
                    xoffset 1040
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E2/D6/S2/Nikki/35.ogg"
                sf "We're watching Gear of Thrones?"
                pf "Actually, this isn't exactly a \"family\" show."
                show kaito cur at l2
                voice "audio/voice/E2/D6/S2/Kaito/23.ogg"
                hk "Agreed."
                show nikki neu at r2
                "Nikki sighs in relief."
                voice "audio/voice/E2/D6/S2/Nikki/36.ogg"
                sf "Oh good, because I've already seen it."
                show drop:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                show kaito ske at l2
                voice "audio/voice/E2/D6/S2/Kaito/24.ogg"
                hk "...I think we need to discuss what's appropriate for you to watch young lady."
                show nikki thi at r2
                voice "audio/voice/E2/D6/S2/Nikki/37.ogg"
                sf "I watched it with my friends for the story. We skipped the {i}other{/i} parts."
                pf "{size=12}Those were the best parts.{/size}" #SMALL FONT
                show kaito ner at l2
                "Uncle Kaito nudges me."
                show nikki neu at r2
                pf "I mean, let's choose something else."
                $ E2D6S2_Thrones = 1
                #LOOP BACK BUT CAN'T CHOOSE THIS ANYMORE
                jump E2D6S2_Netflicks
        
            "Two and a Half Gears":
                pf "A recently divorced GEAR technician and his son move in with his older brother who writes GEAR commercial jingles for a living."
                show nikki hap at r2
                voice "audio/voice/E2/D6/S2/Nikki/38.ogg"
                sf "Oh, I loved this show!"
                show kaito ske at l2
                voice "audio/voice/E2/D6/S2/Kaito/25.ogg"
                hk "{i}Loved?{/i}"
                show drop:
                    xoffset 1040
                    yoffset 160
                    xzoom .75
                    yzoom .75
                show nikki thi at r2
                voice "audio/voice/E2/D6/S2/Nikki/39.ogg"
                sf "Yeah, it all went downhill after they replaced Charles Sheine with Axeton Koocher."
                show nikki smi at r2
                voice "audio/voice/E2/D6/S2/Nikki/40.ogg"
                sf "But I wouldn't mind watching some of the earlier episodes!"
                show kaito smi at l2
        
            "GEARs and Recreation.":
                pf "The local GEARs and Recreation department of Pawnie is always good for a laugh!"
                show kaito mis at l2
                voice "audio/voice/E2/D6/S2/Kaito/26.ogg"
                hk "You can't watch this without eating a Calzone."
                show note:
                    xoffset 1040
                    yoffset 160
                    xzoom .75
                    yzoom .75
                show nikki mis at r2
                voice "audio/voice/E2/D6/S2/Nikki/41.ogg"
                sf "Maybe you should {i}Treat Yo Self{/i} to one."
                show kaito hap at l2
                "We all laugh together."
        
            "How I met your Gear." if E2D6S2_How == 0:
                pf "What if we watch How I met your GEAR--"
                show exclamation:
                    xoffset 1040
                    yoffset 160
                    xzoom .75
                    yzoom .75
                show nikki ang at r2
                voice "audio/voice/E2/D6/S2/Nikki/42.ogg"
                sf "NO!"
                show question:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                show kaito sur at l2
                show nikki ann at r2
                "Kaito and I are both startled by Nikki's reaction."
                show nikki dis at r2
                voice "audio/voice/E2/D6/S2/Nikki/43.ogg"
                sf "9 seasons for the worst ending of all time!"
                show kaito cur at l2
                show storm:
                    xoffset 1040
                    yoffset 160
                    xzoom .75
                    yzoom .75
                "Nikki huffs."
                show dots:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                "Kaito blinks."
                show kaito ske at l2
                voice "audio/voice/E2/D6/S2/Kaito/27.ogg"
                hk "Well if you feel that strongly about it, let's choose something else."
                $ E2D6S2_How = 1
                #LOOP BACK BUT CAN'T CHOOSE THIS ANYMORE
                jump E2D6S2_Netflicks
        
            "That 70's GEAR.":
                pf "A group of teenage pilots get into all sorts of shenanigans--"
                show nikki smi at r2
                voice "audio/voice/E2/D6/S2/Nikki/44.ogg"
                sf "GOOD DAY!"
                show kaito cur at l2
                pf "--while growing up in--"
                show exclamation:
                    xoffset 1040
                    yoffset 160
                    xzoom .75
                    yzoom .75
                show nikki mis at r2
                voice "audio/voice/E2/D6/S2/Nikki/45.ogg"
                sf "I SAID GOOD DAY!"
                pf "Are you channeling your inner Fezze?"
                show kaito hap at l2
                "Uncle Kaito laughs."
                voice "audio/voice/E2/D6/S2/Kaito/28.ogg"
                hk "Yup, I think that's Nikki's way of saying she's ready to watch this."
                show nikki smi at r2
                "Nikki grins and nods."
        
            "The Big GEAR Theory.":
                pf "Two genius GEAR engineers' lives are turned upside down when a blonde bombshell moves in next door."
                show nikki hap at r2
                voice "audio/voice/E2/D6/S2/Nikki/46.ogg"
                sf "Oh! I love this show."
                pf "Mhm. Especially the scientific parts, they are actually more accurate than expected."
                show nikki mis at r2
                voice "audio/voice/E2/D6/S2/Nikki/47.ogg"
                sf "Of course {i}you{/i} care about that."
                pf "Nikki..."
                show note:
                    xoffset 1040
                    yoffset 160
                    xzoom .75
                    yzoom .75
                show nikki smi at r2
                voice "audio/voice/E2/D6/S2/Nikki/48.ogg"
                sf "What? It's a compliment"
                show kaito hap at l2
                voice "audio/voice/E2/D6/S2/Kaito/29.ogg"
                hk "I don't mind watching this either."
        
            "House of GEARs.":
                pf "A former GEAR pilot will do everything he can to become the president of the United States!"
                show kaito cur at l2
                voice "audio/voice/E2/D6/S2/Kaito/30.ogg"
                hk "Ooh, I was able to catch the first two episodes... it was quite intriguing."
                show nikki ske at r2
                voice "audio/voice/E2/D6/S2/Nikki/49.ogg"
                sf "Seriously? This show is so boring."
                "I gently pat Nikki on the head."
                show kaito neu at l2
                pf "When you're older, you'll appreciate good television."
                show storm:
                    xoffset 1040
                    yoffset 160
                    xzoom .75
                    yzoom .75
                show nikki dis at r2
                voice "audio/voice/E2/D6/S2/Nikki/50.ogg"
                sf "If I ever actually start liking House of GEARs, you can officially declare my youth over."
                show kaito ske at l2
                voice "audio/voice/E2/D6/S2/Kaito/31.ogg"
                hk "So you don't want to watch it?"
                show nikki neu at r2
                voice "audio/voice/E2/D6/S2/Nikki/51.ogg"
                sf "Well it looks like you two want to, so I'll watch it too."
                show kaito mis at l2
                "Kaito smiles."
                voice "audio/voice/E2/D6/S2/Kaito/32.ogg"
                hk "I'd say she's already quite mature for her age."
        
            "Breaking GEAR.":
                pf "A Cenorobotics professor who is diagnosed with cancer gets caught up in the world of mechamphetamines to support his family financially after he's gone."
                show exclamation:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                show kaito cur at l2
                voice "audio/voice/E2/D6/S2/Kaito/33.ogg"
                hk "Oh! This is my favourite show of all time! Do you guys remember when--"
                show nikki sur at r2
                voice "audio/voice/E2/D6/S2/Nikki/52.ogg"
                sf "Ah!"
                pf "NO!"
                show kaito neu at l2
                show nikki dis at r2
                "Nikki and I each put a hand over Kaito's mouth."
                pf "No spoilers!"
                show storm:
                    xoffset 1040
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E2/D6/S2/Nikki/53.ogg"
                sf "Yeah, we haven't finished yet!"
                show kaito ner at l2
                "Kaito nods and we remove our hands."
                show drop:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E2/D6/S2/Kaito/34.ogg"
                hk "Okay sure."
                show kaito mis at l2
                voice "audio/voice/E2/D6/S2/Kaito/35.ogg"
                hk "... So that probably means you don't want to know that--"
                show nikki sur at r2
                "Nikki quickly covers her ears."
                show nikki ang at r2
                show vein:
                    xoffset 1040
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E2/D6/S2/Nikki/54.ogg"
                sf "No!"
                show nikki ann at r2
                pf "STAHP!"
                show kaito hap at l2
                voice "audio/voice/E2/D6/S2/Kaito/36.ogg"
                hk "Haha! This is great. I'll stop now."
                show nikki dis at r2
                "We both glare at Kaito suspiciously."
                show kaito smi at l2
                voice "audio/voice/E2/D6/S2/Kaito/37.ogg"
                hk "Let's watch it. You won't hear any spoilers from me."
                show nikki neu at r2
        
            "Modern GEAR.":
                pf "Let's watch Modern GEAR!"
                show nikki hap at r2
                voice "audio/voice/E2/D6/S2/Nikki/55.ogg"
                sf "Oh yes! I love how they explore the dynamics of each family. It's funny to see how each of them react to things."
                show kaito mis at l2
                voice "audio/voice/E2/D6/S2/Kaito/38.ogg"
                hk "W-T-F."
                show dots:
                    xoffset 1040
                    yoffset 160
                    xzoom .75
                    yzoom .75
                show nikki cur at r2
                "Nikki and I turn to face Kaito, completely stunned at what he just said."
                show kaito ske at l2
                voice "audio/voice/E2/D6/S2/Kaito/39.ogg"
                hk "Why the face?"
                show kaito hap at l2
                "Kaito cracks up at his own joke."
                show nikki ske at r2
                voice "audio/voice/E2/D6/S2/Kaito/40.ogg"
                hk "Haha!"
                pf "...Are you serious?"
                show drop:
                    xoffset 1040
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E2/D6/S2/Nikki/56.ogg"
                sf "Oh god, he's a real life Fill Dunfee."
                show kaito mis at l2
                voice "audio/voice/E2/D6/S2/Kaito/41.ogg"
                hk "Okay, let's watch this. L-O-L."
                show nikki ner at r2
                "Nikki cringes. I shrug."
        
            "Agents of G.E.A.R.":
                pf "Rogue GEARs with special powers are tracked by the secret organization, \"Agents of G.E.A.R.\"."
                show kaito ske at l2
                voice "audio/voice/E2/D6/S2/Kaito/42.ogg"
                hk "You actually want to watch this? I found it to be a bit boring."
                pf "You have to watch up to the mid-season. Most of it was just filler until their movie counterpart released."
                show question:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                show kaito cur at l2
                voice "audio/voice/E2/D6/S2/Kaito/43.ogg"
                hk "Oh really? Hmm, maybe it's worth giving it a second chance. Nikki?"
                show nikki smi at r2
                voice "audio/voice/E2/D6/S2/Nikki/57.ogg"
                sf "I don't mind watching this."
                show kaito smi at l2
        
        pf "Then it's settled."
        "Kaito navigates through Netflicks and selects the show."
        
        #Fade to black
        stop music fadeout 3
        scene black with fade
        $renpy.pause(1)
        
        scene bg homekaito main night with fade
        play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 3
        
        show kaito smi at cc with dissolve
        "After binge watching a few episodes, Kaito stretches and pushes off the couch."
        show note:
            xoffset 720
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/D6/S2/Kaito/44.ogg"
        hk "That was a great break!"
        show kaito hap at cc
        voice "audio/voice/E2/D6/S2/Kaito/45.ogg"
        hk "I have to get some work done before midnight though."
        pf "Alright."
        show kaito smi at cc
        voice "audio/voice/E2/D6/S2/Kaito/46.ogg"
        hk "Don't stay up too late you two."
        show nikki smi at r3:
            xzoom -1
        voice "audio/voice/E2/D6/S2/Nikki/58.ogg"
        sf "Okay!"
        hide kaito with dissolve
        "Kaito retreats into the kitchen where his laptop and papers are scattered."
        
        show nikki neu at cc with dissolve:
            xzoom 1
        "Nikki heaves a long sigh."
        show nikki thi at cc
        voice "audio/voice/E2/D6/S2/Nikki/59.ogg"
        sf "Well… I guess it's time for me to clean off your bike…"
        show nikki sad at cc
        "Before she can point her sad eyes at me, I shake my head."
        pf "You can do it tomorrow."
        show nikki hap at cc
        "She immediately brightens up."
        show note:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/D6/S2/Nikki/60.ogg"
        sf "Okay!"
        show nikki smi at cc
        voice "audio/voice/E2/D6/S2/Nikki/61.ogg"
        sf "In that case, I'm going to get started on my homework."
        pf "Hah, homework."
        
        if MCStory == 2:
            show nikki dis at cc
            voice "audio/voice/E2/D6/S2/Nikki/62.ogg"
            sf "Yes, homework. Not all of us automatically ace exams y'know!"
            "I shrug."
            pf "I can't help it. Let me know if you need help though."
        
        else:
            show nikki dis at cc
            voice "audio/voice/E2/D6/S2/Nikki/63.ogg"
            sf "It's my senior year! I need to maintain my grades to get into a good school."
            "She has a point."
            pf "Alright. Let me know if you need any help."
            
        show nikki neu at cc
        voice "audio/voice/E2/D6/S2/Nikki/64.ogg"
        sf "Thanks. It's nothing too difficult, just a lot of questions to go through."
        pf "Mmkay."
        
        scene black with fade
        "We both nod, say our goodnights to Kaito, and head to our rooms."
        
        play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
        $renpy.pause(2.5)
        scene bg homekaito myroom night with fade
        
        "I spend the rest of the evening relaxing, until it's time to sleep."
        play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
        "As I crawl into bed, my phone buzzes. I open up a text from Shou."
        "{i}Heyo! Guess what holiday is coming up next month! I'll give you a hint… we're all going to the beach! You interested?{/i}"
        "A holiday in which we all go to the beach? I have no idea what that holiday is, but I already like it."
        "I text back."
        "{i}You know it!{/i}"
        stop music fadeout 5
        scene black with fade
        stop ambient fadeout 3
        $renpy.pause(1)
        
        #jump E2END
        jump E3D1S1