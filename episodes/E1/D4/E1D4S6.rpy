label E1D4S6:
    
    scene bg homekaito main dusk with fade
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 1
    "Both Uncle Kaito and Nikki are lounging on the couch when I get home. I plop down in a nearby chair."
    show kaito smi at l2
    show nikki hap at r2:
        xzoom -1
    with dissolve
    show exclamation:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S6/Nikki/1.ogg"
    sf "You're finally home! I was getting worried."
    pf "Sorry, the qualifiers ran later than I expected."
    show nikki neu at r2
    voice "audio/voice/E1/D4/S6/Kaito/2.ogg"
    hk "That's right! Today was the big day. How'd it go?"
    
    menu:
        "We scored big!":
            pf "It was hard, but I'm confident we got a high score!"
            show kaito hap at l2
            show nikki hap at r2
            with dissolve
            "Nikki jumps out of her seat to hug me, while Uncle Kaito grins from ear to ear."
            show heart:
                xoffset 1050
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Nikki/2.ogg"
            sf "Yay! I never doubted you for a second."
            show note:
                xoffset 365
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Kaito/3.ogg"
            hk "Proud of you, kid! I knew you could do it."
            show nikki neu at r2
            pf "Thanks, guys."
            show kaito smi at l2
    
        "Please, it's me.":
            pf "It was just against AI GEAR... not even a challenge."
            show kaito mis at l2
            "Uncle Kaito fists bumps me."
            show note:
                xoffset 365
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Kaito/4.ogg"
            hk "That's how we do it!"
            "Nikki rolls her eyes but laughs anyway."
            show nikki smi at r2
            show heart:
                xoffset 1050
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Nikki/3.ogg"
            sf "You guys are so lame, but still, congrats! That's a big achievement."
            pf "Thanks, guys."
            show kaito smi at l2
    
        "It could have gone better.":
            pf "We did alright…"
            show nikki hap at r2
            show heart:
                xoffset 1050
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Nikki/4.ogg"
            sf "That's awesome! Congratulations!"
            show kaito cur at l2
            voice "audio/voice/E1/D4/S6/Kaito/5.ogg"
            hk "That's good, isn't it?"
            show nikki neu at r2
            pf "Yeah."
            show kaito ske at l2
            show question:
                xoffset 365
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Kaito/6.ogg"
            hk "So why don't you seem happy about it?"
            pf "I feel like it was more to do with luck than skill."
            show nikki sad at r2
            "Nikki frowns."
            show kaito neu at l2
            show drop:
                xoffset 1050
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Nikki/5.ogg"
            sf "Why do you think that? Did you fight hard?"
            pf "Yeah."
            voice "audio/voice/E1/D4/S6/Kaito/7.ogg"
            hk "Did your team fight hard?"
            pf "Well, yeah."
            show nikki neu at r2
            voice "audio/voice/E1/D4/S6/Nikki/6.ogg"
            sf "Then you're being too hard on yourself."
            show kaito smi at l2
            voice "audio/voice/E1/D4/S6/Kaito/8.ogg"
            hk "Your sister's right. Sounds like a fair win to me."
            pf "I suppose you're right."

    voice "audio/voice/E1/D4/S6/Kaito/9.ogg"
    hk "So, I guess your team was happy they brought you on, weren't they?"
    
    if (E1D4S4_FollowMatchPlan == 0):
        pf "Sort of."
        show nikki cur at r2
        voice "audio/voice/E1/D4/S6/Nikki/7.ogg"
        sf "What does that mean?"
        pf "My weapons are missing because they haven't cleared customs yet, so the team wanted me to just hang around in the back and keep out of the way."
        show kaito cur at l2
        show nikki ske at r2
        show storm:
            xoffset 1050
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S6/Nikki/8.ogg"
        sf "That doesn't seem very team-like of them."
        pf "Exactly! I'm a participant, not a spectator! So I participated. When the match started I darted out and took out two AIs on my own."
        show kaito hap at l2
        show nikki smi at r2
        "Nikki grins excitedly and Kaito laughs."
        voice "audio/voice/E1/D4/S6/Kaito/10.ogg"
        hk "Sounds about right."
        show nikki neu at r2
        pf "At first, Kaori was super pissed that I didn't follow her orders, but they all ended up just being really curious about my core."
    
    else:
        pf "Absolutely! Because my weapons haven't cleared through customs they asked me to stay out of the way."
        show kaito cur at l2
        show nikki wor at r2
        "Nikki pouts."
        voice "audio/voice/E1/D4/S6/Nikki/9.ogg"
        sf "That doesn't seem fair."
        pf "It's alright. I understood, so I held back. They did really well and took out two of the AIs before they were struck down. Then I managed to take out the other two, much to the surprise of everyone."
        show kaito hap at l2
        "Uncle Kaito laughs."
        voice "audio/voice/E1/D4/S6/Kaito/11.ogg"
        hk "That's my boy!"
        show nikki neu at r2
        pf "But afterwards was kind of strange. Everyone was really interested in my core."
        
    show kaito cur at l2
    show question:
        xoffset 365
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S6/Kaito/12.ogg"
    hk "What's wrong with your core?"
    pf "I don't know."
    show nikki cur at r2
    show question:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S6/Nikki/10.ogg"
    sf "Did you ever notice anything weird about it back at CINY?"
    pf "No…"
    show kaito ner at l2
    show nikki smi at r2
    voice "audio/voice/E1/D4/S6/Nikki/11.ogg"
    sf "Then I wouldn't worry about it."
    stop music fadeout 3
    pf "Yeah, I guess you're right."
    $renpy.pause(1)
    scene black with fade
    $renpy.pause(2.5)
    scene bg homekaito main night with fade
    $renpy.pause(1)
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 1
    show kaito neu at l2
    show nikki neu at r2
    with dissolve
    "Uncle Kaito stands and stretches."
    voice "audio/voice/E1/D4/S6/Kaito/13.ogg"
    hk "I'm going to grab a drink. You want some food? We left you a plate."
    pf "Yeah, that'd be great!"
    "I begin to stand when Kaito stops me."
    show kaito smi at l2
    voice "audio/voice/E1/D4/S6/Kaito/14.ogg"
    hk "I'll get it."
    pf "Thanks."
    hide kaito with dissolve
    "I turn to Nikki."
    pf "So, how was your day?"
    show nikki hap at r2 with dissolve
    voice "audio/voice/E1/D4/S6/Nikki/12.ogg"
    sf "Pretty good. Did I tell you that I auditioned for the dance team? Well, I got in!"
    pf "That's great, Nikki!"
    show nikki smi at r2
    voice "audio/voice/E1/D4/S6/Nikki/13.ogg"
    sf "I'm really excited about it! But I'm a little worried 'cause... I haven't danced since--"
    stop music fadeout 3
    show nikki ner at r2 with dissolve
    $renpy.pause(1)
    show nikki thi at r2 with dissolve
    play music "audio/music/Slow Day (GAME VERSION).ogg" fadein 1
    show dots:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    "Her voice chokes up and she glances away."
    pf "I know. And they would be so proud that you're doing it again."
    show nikki smi at r2 with dissolve
    "She smiles sadly."
    voice "audio/voice/E1/D4/S6/Nikki/14.ogg"
    sf "It feels weird knowing they won't be there to watch any of my competitions. Mom never missed a show. And remember how Dad used to make a poster with my name, and he'd wave it around like an idiot?"
    "I can't help but laugh at the memory."
    show nikki ner b1 at r2 with dissolve
    voice "audio/voice/E1/D4/S6/Nikki/15.ogg"
    sf "Ugh, I remember being {i}so{/i} embarrassed."
    pf "Yeah, you used to tell him the wrong dates for your competitions hoping he wouldn't show up."
    show nikki smi b1 at r2
    voice "audio/voice/E1/D4/S6/Nikki/16.ogg"
    sf "I know, but he always did! He'd wave that poster and cheer louder than anyone else and all I could think about was how I wanted to crawl into a hole and die."
    show nikki sad at r2
    voice "audio/voice/E1/D4/S6/Nikki/17.ogg"
    sf "But I think about it now and… I would give anything to see one of his posters again--"
    show nikki win at r2
    "Her voice cracks and she rubs her eyes. I scoot closer and wrap my arms around her."
    voice "audio/voice/E1/D4/S6/Nikki/18.ogg"
    sf "I'm sorry."
    show nikki sad at r2
    pf "I miss them too. But hey, you've still got me."
    voice "audio/voice/E1/D4/S6/Kaito/15.ogg"
    hk "And lucky for you, I'm an expert poster maker."
    show kaito smi at l2 with dissolve
    show nikki cur at r2
    "We both glance up at Uncle Kaito as he sets the plate of food down in front of me. Nikki lets out a weak laugh."
    show nikki smi at r2
    voice "audio/voice/E1/D4/S6/Nikki/19.ogg"
    sf "You've got some tough shoes to fill."
    show kaito mis at l2
    voice "audio/voice/E1/D4/S6/Kaito/16.ogg"
    hk "I'm up for the challenge."
    show nikki neu at r2
    "She smiles, and wipes at her eyes one last time."
    stop music fadeout 3
    show heart:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S6/Nikki/20.ogg"
    sf "Thanks, guys."
    show kaito hap at l2
    "Uncle Kaito smiles back."
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 1
    voice "audio/voice/E1/D4/S6/Kaito/17.ogg"
    hk "So, movie night tonight?"
    pf "I'm game."
    show nikki hap at r2
    show note:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S6/Nikki/21.ogg"
    sf "Me too!"
    show kaito smi at l2
    show note:
        xoffset 365
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S6/Kaito/18.ogg"
    hk "Great, what do we feel like watching?"
    show nikki neu at r2
    
    label E1D4S6_MovieChoiceLoop:
    
        menu:
            "{i}The GEARfather{/i}":
                pf "An aging patriarch of the black market GEAR syndicate transfers control of his empire to his reluctant son."
                show kaito hap at l2
                show exclamation:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/19.ogg"
                hk "Alright! You can never get too much Don Gearleone."
                pf "That's what I'm saying!"
                show nikki cur at r2
                voice "audio/voice/E1/D4/S6/Nikki/22.ogg"
                sf "I've never seen this movie before."
                show kaito sur at l2 with dissolve
                "Both Uncle Kaito and I shout in disbelief."
                show shocked:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                #player and Hitoshi Kaito line should be together 
                "Both of us" "What?!"
                show kaito mis at l2
                voice "audio/voice/E1/D4/S6/Kaito/21.ogg"
                hk "\"I'll make him a cogwheel he can't refuse\"."
                show nikki thi at r2
                "Nikki shakes her head."
                show kaito ske at l2
                voice "audio/voice/E1/D4/S6/Nikki/23.ogg"
                sf "Errr... Nope."
                pf "Okay, we have to watch it now."
        
            "{i}The Sixth GEAR{/i}":
                pf "A young boy is haunted by a dark secret: he is visited by ruined GEAR."
                show nikki win at r2
                show crying:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/24.ogg"
                sf "Ughhh, nooo we are not watching this movie AGAIN."
                pf "C'mon, it's a classic!"
                show kaito mis at l2
                voice "audio/voice/E1/D4/S6/Kaito/22.ogg"
                hk "\"I see dead GEARs\"."
                pf "Ha! See? Uncle Kaito gets it."
                show nikki dis at r2
                show storm:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/25.ogg"
                sf "Fine, fine. I can tell when I'm outvoted, but next time, I get to pick the movie."
                show kaito smi at l2
                voice "audio/voice/E1/D4/S6/Kaito/23.ogg"
                hk "That's only fair."
                show nikki mis at r2
                "Nikki wears a mischievous grin. Uh oh, what did we just agree to?"
        
            "{i}The Lord of the GEARs{/i}":
                pf "A short-pilot and his companions set out on a journey to destroy the One GEAR."
                show nikki hap at r2
                show exclamation:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/26.ogg"
                sf "Ooooh, yes! Aragear is soooo dreamy!"
                pf "He's a badass."
                show kaito mis at l2
                voice "audio/voice/E1/D4/S6/Kaito/24.ogg"
                hk "Come on, this movie is so much more than just Aragear. \"One GEAR to rule them all, One GEAR to find them; One GEAR to bring them all and in the darkness bind them\"."
                show nikki smi at r2
                "Nikki bursts out laughing."
                voice "audio/voice/E1/D4/S6/Nikki/27.ogg"
                sf "Oh my god, Uncle, you're a nerd!?"
                show kaito hap at l2
                "He grins."
                show note:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/25.ogg"
                hk "Guilty as charged."
        
            "{i}Raiders of the Lost GEAR{/i}":
                pf "A renowned archeologist is recruited to find the GEAR of the covenant."
                show kaito ske at l2
                "Uncle Kaito looks lost."
                voice "audio/voice/E1/D4/S6/Kaito/26.ogg"
                hk "Not sure I've seen this one, bud."
                show nikki cur at r2
                show shocked:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/28.ogg"
                sf "Really, Uncle Kaito? It's really popular in America."
                pf "Yeah! \"The Bible speaks of the GEAR leveling mountains and laying waste in entire regions. An army that carries the GEAR before it... is invincible\"."
                show kaito neu at l2
                show drop:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/27.ogg"
                hk "Nope, doesn't ring a bell."
                show nikki smi at r2
                voice "audio/voice/E1/D4/S6/Nikki/29.ogg"
                sf "Ooh, we should watch this then."
        
            "{i}The Hunger GEARs{/i}":
                pf "Catniece Neverdeen voluntarily takes her younger sister's place in the Hunger GEARs, a televised fight to the death in which teenagers are chosen at random to compete."
                show nikki hap at r2
                show exclamation:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/30.ogg"
                sf "I love this movie! I never pegged you as someone who like it though."
                pf "Are you kidding? \"May the cogs be ever in your favour\"."
                show nikki smi at r2
                voice "audio/voice/E1/D4/S6/Nikki/31.ogg"
                sf "Yes!"
                pf "What do you think, Uncle?"
                show kaito hap at l2
                "Uncle Kaito smiles at us."
                voice "audio/voice/E1/D4/S6/Kaito/28.ogg"
                hk "Sure, why not?"
        
            "{i}Jurassic GEAR{/i}":
                pf "During a preview tour, a theme park suffers a major power breakdown that allows its cloned dino-GEAR exhibits to run amok."
                show kaito mis at l2
                voice "audio/voice/E1/D4/S6/Kaito/29.ogg"
                hk "I'm always up to watch some dinosaurs terrorize people."
                show nikki hap at r2
                voice "audio/voice/E1/D4/S6/Nikki/32.ogg"
                sf "\"Hold onto your butts\"!"
                show kaito cur at l2 with dissolve
                show dots:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                "We both stare at her."
                show nikki mis at r2
                voice "audio/voice/E1/D4/S6/Nikki/33.ogg"
                sf "What? It's a quote from the movie."
                pf "Still a bit unexpected."
                show kaito neu at l2
                voice "audio/voice/E1/D4/S6/Kaito/30.ogg"
                hk "Just a bit."
        
            "{i}Snakes on a GEAR{/i}":
                pf "A military pilot takes on a GEAR full of deadly and poisonous snakes, which were deliberately released to kill him and stop him from testifying against a mob boss."
                show nikki ske at r2
                voice "audio/voice/E1/D4/S6/Nikki/34.ogg"
                sf "This movie was kind of dumb."
                pf "Are you kidding? Jamuel L. Sackson was such a badass! \"I have had it with these mother--\""
                show kaito mis at l2
                voice "audio/voice/E1/D4/S6/Kaito/31.ogg"
                hk "We get it."
                pf "You guys don't like this movie?"
                show kaito neu at l2
                voice "audio/voice/E1/D4/S6/Kaito/32.ogg"
                hk "It's alright. Are you sure it's appropriate for Nikki?"
                show nikki ann at r2
                show vein:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/35.ogg"
                sf "I'm not a little kid!"
                show kaito hap at l2
                "Uncle Kaito puts his hands up in defeat."
                show drop:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/33.ogg"
                hk "I'm sorry!"
                show nikki smi at r2
                "Nikki grins."
                voice "audio/voice/E1/D4/S6/Nikki/36.ogg"
                sf "Anyway, I've seen it before. I'll watch it if we have to."
                show kaito smi at l2
                voice "audio/voice/E1/D4/S6/Kaito/34.ogg"
                hk "Okay, well, it's up to you then, bud."
                pf "I say we're watching it."
        
            "{i}I, Cenorobot{/i}":
                pf "A technophobic pilot investigates a GEAR that may have been wrecked by a fellow GEAR, which leads to a larger threat to humanity."
                show kaito mis at l2
                show exclamation:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/35.ogg"
                hk "Great choice! A powerful movie. \"Human beings have dreams. Even dogs have dreams, but you, you are just a machine. An imitation of life. Can a GEAR write a symphony? Can a GEAR turn a... canvas into a beautiful masterpiece\"?"
                show nikki mis at r2
                voice "audio/voice/E1/D4/S6/Nikki/37.ogg"
                sf "\"Can you\"?"
                show kaito smi at l2
                pf "Haha, Nikki, you like this movie too?"
                show nikki hap at r2
                show exclamation:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/38.ogg"
                sf "Of course! What's not to like?"
        
            "{i}Fifty Shades of GEAR{/i}" if (E1D4S6_FiftyShadesLoopback == 0):
                $ E1D4S6_FiftyShadesLoopback = 1
                pf "Literature student Anesthesia Iron's life changes forever when she meets a powerful, rich billionaire GEAR tycoon. I heard it's got some steamy scenes--"
                "I regret it as soon as the words leave my mouth. What possessed me to request this movie?"
                show kaito ske at l2
                show nikki ske at r2
                "Uncle Kaito gives me a strange look."
                show drop:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/37.ogg"
                hk "I'm going to have to decline this one."
                show nikki ner at r2
                show drop:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/39.ogg"
                sf "No offense, but this is probably the last movie I'd ever want to watch with family."
                pf "Yeah, you're right, I'm not sure what I was thinking."
                jump E1D4S6_MovieChoiceLoop
        
            "Anything with Ceonardo DiLaprio!":
                ### NOTE - new as of Ep4 release
                $ E1D4S6_Ceonardo = 1
                pf "Let's watch a Ceonardo DiLaprio movie."
                show nikki mis at r2
                voice "audio/voice/E1/D4/S6/Nikki/40.ogg"
                sf "You are weirdly obsessed with him, you know that?"
                pf "No, he's just a really talented actor."
                show nikki smi at r2
                voice "audio/voice/E1/D4/S6/Nikki/41.ogg"
                sf "Mmhm, sure, a \"talented\" actor who hasn't won a Moscar yet."
                pf "How dare you! Everyone knows the Moscars are rigged!"
                "Uncle Kaito nods."
                show kaito mis at l2
                voice "audio/voice/E1/D4/S6/Kaito/38.ogg"
                hk "To be fair, he {i}should{/i} have won at least two by now."
                show nikki mis at r2
                sf "Oh no, you too, Uncle Kaito?"
                show kaito hap at l2
                "He just laughs."
                show bulb:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/39.ogg"
                hk "So, Ceonardo DiLaprio… How about {i}The GEAR of Wall Street{/i}?"
                show nikki hap at r2
                show bulb:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/42.ogg"
                sf "We should watch {i}Jomeo and Ruliet{/i}! He was so good in that!"
                
                label E1D4S6_MovieChoiceLoopCeonardo:
                    menu:
                        "{i}GEAR of Wall Street{/i} with Nikki?!" if (E1D4S6_CeonardoLoopback == 0):
                            $ E1D4S6_CeonardoLoopback = 1
                            pf "Actually, I'm not sure that's the best choice, Uncle."
                            show kaito neu at l2 with dissolve
                            show dots:
                                xoffset 365
                                yoffset 5
                                xzoom .75
                                yzoom .75
                            $renpy.pause(1)
                            show nikki cur at r2 with dissolve
                            show confused:
                                xoffset 1050
                                yoffset 160
                                xzoom .75
                                yzoom .75
                            "He looks thoughtfully at Nikki, then nods. Nikki appears confused but goes with it."
                            jump E1D4S6_MovieChoiceLoopCeonardo
            
                        "Let's watch {i}Jomeo and Ruliet{/i}.":
                            pf "We can watch {i}Jomeo and Ruliet{/i}."
                            show nikki smi at r2
                            show note:
                                xoffset 1050
                                yoffset 160
                                xzoom .75
                                yzoom .75
                            voice "audio/voice/E1/D4/S6/Nikki/44.ogg"
                            sf "Yay!"
                            show kaito smi at l2
                            voice "audio/voice/E1/D4/S6/Kaito/40.ogg"
                            hk "It is one of his best movies."
            
                        "I don't like either of these choices.":
                            pf "I'm not feeling either of those tonight. Let's watch {i}GEARception{/i}."
                            show kaito cur at l2
                            show exclamation:
                                xoffset 365
                                yoffset 5
                                xzoom .75
                                yzoom .75
                            voice "audio/voice/E1/D4/S6/Kaito/41.ogg"
                            hk "Oh! That's a good one!"
                            show nikki thi at r2
                            voice "audio/voice/E1/D4/S6/Nikki/45.ogg"
                            sf "I hate the ending. Did it stop spinning or not?"
                            show kaito smi at l2
                            voice "audio/voice/E1/D4/S6/Kaito/1.ogg"
                            hk "No way, that would ruin it."
                
    pf "Anyway, I'll go find the movie so we can watch."
    #fade to black
    scene black with fade
    stop music fadeout 3
    "We enjoy the cinematic experience late into the night--a great ending to a great day."
    
    jump E1D5S1