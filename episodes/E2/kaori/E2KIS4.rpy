#
label E2KIS4:
    
    $ kaoOut = "sCute"
    $ kaoHairB = kaoHairF
    
    $ migGlasses = 1
    
    #WEEKEND EVENT
    
    "I'm kind of hungry. Nikki will probably have food downstairs… {w}but lately I've been craving the sushi Kaori made."
    "I really should make an effort to eat healthier, and those rolls seem simple enough to make. I mean, if Kaori can do it, then so can I. {w}I'll ask her how she made them and maybe I'll surprise Nikki by making lunch… that's edible."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(1)
    "I call up Kaori, and there's a flood of noise when she answers."
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    $renpy.pause(1)
    voice "audio/voice/E2/Free/KI/79.ogg"
    ki "What is it?"
    pf "Hello to you to."
    voice "audio/voice/E2/Free/KI/80.ogg"
    ki "Oh, right, hi. What's up?"
    pf "Remember the maki sushi you made for lunch?"
    voice "audio/voice/E2/Free/KI/81.ogg"
    ki "Yeah."
    pf "How did you make them?"
    voice "audio/voice/E2/Free/KI/82.ogg"
    ki "Oh, it's really easy. You need rice, nori, vinegar--"
    "The voices in the background are getting so loud I can barely hear Kaori."
    pf "You're kind of cutting off. Where are you?"
    voice "audio/voice/E2/Free/KI/83.ogg"
    ki "I'm in the mall. Actually, I'm in the store grabbing groceries. If you come by I can just show you what ingredients to get."
    pf "Okay, I'll head over."
    voice "audio/voice/E2/Free/KI/84.ogg"
    ki "Hurry! I'm only here for a little bit and then I'm gone."
    pf "Where are you going?"
    play sound "audio/sfx/Technology/Phone Answer.ogg" fadein 1
    "But she already hung up the phone. {w}Oh well. I better get to the mall before she leaves."
    
    #back to day 6
    jump E2D6S1_Nikki
    
    label E2KIS4_Continued:

        $ kaoOut = "sCute"
        $ kaoHairF = renpy.random.choice(['banded'])
        $ kaoHairB = kaoHairF

        $ migGlasses = 1
        
        
        
        $renpy.pause(2.5)
        play ambient "audio/ambience/Mall.ogg" fadein 3
        # No good bgs to "display produce" but they are in the mall, so the mall bg is the current best pick
        scene bg mall main day with fade
        play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
        "I park my bike in the lot and make my way into the building. The supermarket is tucked into a corner of the sprawling mall. There's no way Kaori will be walking the aisles full of processed snacks, so I head directly to the produce aisle. Just as I guessed, I spot Kaori picking out vegetables."
        show kaori cur at cc with dissolve
        "She glances at me as I approach."
        voice "audio/voice/E2/Free/KI/85.ogg"
        ki "Ah, you made it."
        show kaori neu at cc
        pf "Yeah."
        "Her cart is filled with different fruits and vegetables. I caught her just in time! It looks like she's almost ready to check out."
        
        voice "audio/voice/E2/Free/KI/86.ogg"
        ki "So, what type of sushi do you want to make?"
        
        menu:
            "Cucumber rolls.":
                $ E2KIS4_Sushi = "Cucumber"
                pf "Kappamaki."
                show note:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori mis at cc
                voice "audio/voice/E2/Free/KI/87.ogg"
                ki "Good choice. These are really light but still keep you full."
                "She hands me a cucumber out of her shopping cart."
                show kaori smi at cc
                voice "audio/voice/E2/Free/KI/88.ogg"
                ki "Here, take this one. It's really fresh."
        
                menu:
                    "No, I couldn't!":
                        pf "That's okay! You already did all the work to pick it out so you should keep it. I'll grab my own."
                        "I walk over to the cucumbers and randomly select one. Normally I'd just throw it in my basket, but under Kaori's watchful gaze I feel like I should do more."
                        show kaori ske at cc
                        "I hold it up towards the light."
                        pf "Yup, this one looks good."
                        show kaori thi at cc
                        "Kaori sighs, but there's also a trace of a smile on her lips."
                        show kaori smi at cc
                        voice "audio/voice/E2/Free/KI/89.ogg"
                        ki "You should squeeze it gently to test firmness. As long as it's firm and doesn't feel soft or bend it should be okay."
        
                        menu:
                            "Thanks for the advice.":
                                pf "Oh, right. Thanks."
        
                            "That's what she said!":
                                pf "That's what she said."
                                show kaori ske at cc
                                "She furrows her brow, then it hits her."
                                show storm:
                                    xoffset 720
                                    yoffset 110
                                    xzoom .75
                                    yzoom .75
                                show kaori dis at cc
                                voice "audio/voice/E2/Free/KI/90.ogg"
                                ki "Oh grow up!"
                                "Whatever, that was pure gold."
        
                            "I know.":
                                pf "I knew that. I was just testing you."
                                show question:
                                    xoffset 720
                                    yoffset 110
                                    xzoom .75
                                    yzoom .75
                                show kaori ske at cc
                                "She raises a skeptical eyebrow."
        
                        "A gentle squeeze confirms that this one is good, so I put it in my basket."
                        hide kaori with dissolve
        
                    "Okay! Are these all for me?":
                        "I eagerly take it from her and throw it in my basket."
                        show kaori cur at cc
                        pf "Cool thanks! You got any rice in there too?"
                        show kaori sur at cc
                        voice "audio/voice/E2/Free/KI/91.ogg"
                        ki "Eh?!"
                        "I shuffle items around in her cart, looking for ingredients I need."
                        show kaori ang at cc
                        with Shake((0, 0, 0, 0), .5, dist=5)
                        "Suddenly, a fist collides with my arm."
                        pf "Ow!"
                        show vein:
                            xoffset 720
                            yoffset 110
                            xzoom .75
                            yzoom .75
                        show kaori ann at cc
                        voice "audio/voice/E2/Free/KI/92.ogg"
                        ki "Why are you shopping out of my cart when you have the whole store to choose from?"
                        "I rub at my arm."
                        pf "Geez, why'd you offer that to me if you're just going to get mad?"
                        show kaori ang at cc
                        voice "audio/voice/E2/Free/KI/93.ogg"
                        ki "Maybe next time I won't!"
                        show tsuBlush:
                            xoffset 720
                            yoffset 110
                            xzoom .75
                            yzoom .75
                        show kaori ann b1 at cc with dissolve
                        $renpy.pause(1)
                        hide kaori with dissolve
                        "With a huff, she turns away, but not before I catch a hint of pink in her cheeks."
                
                    "I don't need your charity.":
                        pf "Uhh, I think I know how to pick out my own vegetables."
                        show kaori cur b1 at cc with dissolve
                        "Kaori reddens and turns away."
                        show kaori ann b1 at cc
                        voice "audio/voice/E2/Free/KI/94.ogg"
                        ki "Fine! It wasn't for you anyway."
                        pf "Then why did you offer it--"
                        show vein:
                            xoffset 720
                            yoffset 110
                            xzoom .75
                            yzoom .75
                        show kaori ang b1 at cc
                        voice "audio/voice/E2/Free/KI/95.ogg"
                        ki "Shut up!"
                        show kaori ann b1 at cc
                        voice "audio/voice/E2/Free/KI/96.ogg"
                        ki "Just pick out your cucumber."
                        "I shrug, and grab one without looking. When I'm about to place it in my basket, Kaori takes the cucumber out of my hand and replaces it with a firm, green one."
                        show kaori thi b1 at cc
                        voice "audio/voice/E2/Free/KI/97.ogg"
                        ki "This one is better."
                        pf "Uh, thanks."
                        show tsuBlush:
                            xoffset 720
                            yoffset 110
                            xzoom .75
                            yzoom .75
                        $renpy.pause(2.5)
                        hide kaori with dissolve
                        "She doesn't make eye contact and her cheeks are still burning."
        
            "Tuna rolls.":
                $ E2KIS4_Sushi = "Tuna"
                pf "Tekkamaki. I still need my protein!"
                "Kaori nods."
                voice "audio/voice/E2/Free/KI/98.ogg"
                ki "We'll have to inspect the sashimi closely to make sure it's very fresh."
                pf "How do we do that?"
                show kaori smi at cc
                voice "audio/voice/E2/Free/KI/99.ogg"
                ki "Easiest way to tell if a fish isn't fresh is by how strongly it smells, and the flesh will still be moist. But if it's been properly iced it should be fine."
        
                menu: 
                    "I won't get worms, will I?":
                        pf "Er… I won't get sick from eating it, right?"
                        show kaori cur at cc
                        "Kaori blinks."
                        voice "audio/voice/E2/Free/KI/100.ogg"
                        ki "Have you never had raw fish before?"
                        pf "I have, but only in restaurants…"
                        show kaori ske at cc
                        voice "audio/voice/E2/Free/KI/101.ogg"
                        ki "Where do you think restaurants get their fish?"
                        pf "Uh… from fishermen?"
                        show kaori neu at cc
                        voice "audio/voice/E2/Free/KI/102.ogg"
                        ki "And who supplies the market with fish?"
                        pf "Also fishermen?"
                        show kaori mis at cc
                        "..."
                        pf "Ohhh."
                        "Kaori smirks as understanding dawns on me."
                        hide kaori with dissolve
        
                    "I want the freshest possible!":
                        pf "Frozen? No, I want it fresh off the boat!"
                        show kaori mis at cc
                        "She snorts."
                        voice "audio/voice/E2/Free/KI/103.ogg"
                        ki "Then you should go catch it yourself."
                        pf "Hmm… {w}Good idea!"
                        show kaori ske at cc
                        "Kaori catches my collar as I turn around."
                        voice "audio/voice/E2/Free/KI/104.ogg"
                        ki "Do you want my help or not?"
                        pf "Er, yes."
                        show kaori smi at cc
                        voice "audio/voice/E2/Free/KI/105.ogg"
                        ki "Then come on!"
                        hide kaori with dissolve
        
                    "All fish stinks.":
                        pf "That'll be hard considering all fish stinks."
                        show kaori ske at cc
                        "Kaori gives me a weird look."
                        voice "audio/voice/E2/Free/KI/106.ogg"
                        ki "If you don't like fish then why do you want tekkamaki?"
                        pf "I never said I didn't like fish. It just smells."
                        show kaori neu at cc
                        voice "audio/voice/E2/Free/KI/107.ogg"
                        ki "Hm…"
                        hide kaori with dissolve
        
                "We wander over to the seafood section and Kaori selects a couple of tuna filets for me."
        
            "Uhh, whatever you had last time.":
                $ E2KIS4_Sushi = "Whatever"
                show kaori ske at cc
                "Kaori raises an eyebrow."
                voice "audio/voice/E2/Free/KI/108.ogg"
                ki "I had an assortment for lunch that day. You want to make all of them?"
                pf "Sure."
                show kaori neu at cc
                "She shrugs."
                voice "audio/voice/E2/Free/KI/109.ogg"
                ki "Okay, follow me."
                hide kaori with dissolve
                "I trail behind her as she expertly picks out all the necessary ingredients and places them in my basket."
        
        "As Kaori gathers everything I will need, she imparts step-by-step instructions for how to cook and assemble them."
        show kaori neu at cc with dissolve
        voice "audio/voice/E2/Free/KI/110.ogg"
        ki "Got it?"
        pf "Yeah, I think so."
        show kaori smi at cc
        voice "audio/voice/E2/Free/KI/111.ogg"
        ki "Good. Anyway, that's everything and I have to get going so let's check-out."
        "Wasting no time, she drags me to the check-out counter so we can pay. I patiently wait for the clerk to finish bagging all our items."
        pf "Here, let me hold your bags."
        show kaori cur at cc
        "Kaori begins to protest, but I grab her bags before she can."
        show kaori thi at cc
        voice "audio/voice/E2/Free/KI/112.ogg"
        ki "F-Fine! But only because you want to."
        stop ambient fadeout 5
        # no outside mall bg, so we'll have to be creative with the parking lots
        scene black with fade
        "I nod, holding my bags in one hand and hers in the other. She silently leads me out of the store, then pauses right outside the mall entrance."
        play ambient "audio/ambience/Parking Lot.ogg" fadein 3
        scene bg campus parking day empty with fade
        show kaori neu at cc
        voice "audio/voice/E2/Free/KI/113.ogg"
        ki "Thanks, but I can carry it from here."
        pf "It's okay. Did you take the bus? I'll carry it to the bus stop for you."
        stop music fadeout 5
        show exclamation:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori cur at cc with dissolve
        $renpy.pause(1)
        show kaori thi at cc with dissolve
        voice "audio/voice/E2/Free/KI/114.ogg"
        ki "No!"
        "She snatches the bags from one of my hands."
        show kaori neu at cc
        voice "audio/voice/E2/Free/KI/115.ogg"
        ki "Thanks, but I'll see you later!"
        hide kaori with dissolve
        pf "Okay, bye…"
        "I'm barely able to reply before she runs off."
        "She seems to be in a hurry. I wonder where she's going… {w}Well, it doesn't matter."
        
        if E2KIS4_Sushi == "Tuna":
            "I better get home so my fish doesn't spoil."
        
        else:
            "I'm starving! Time to get home and make this delicious meal. Nikki will be so impressed!"
        
        "As I balance out my bags between my hands, I spot a purple eggplant in one of them."
        "Huh? I didn't get an eggplant… {w}Oh no! {w}These are Kaori's bags! That means she has mine!"
        "I need to catch her before it's too late! {w}My legs begin pumping before I even finish the thought."
        $renpy.pause(1)
        play music "audio/music/Stress (GAME VERSION).ogg" fadein 3

        "As I race towards the bus stop, I spot that fancy white car from the other day with the same man from before leaning against it. Kaori runs toward him."
    
        show kaori neu at r1:
        show miguel neu at r3:
            xoffset 150
        with dissolve
        
        if MCStory == 1:
            "I skid to a sharp stop and step behind a parked car, making sure I'm out of view."
        
        else:
            "My legs tangle as I try to suddenly stop and I stumble noisily behind a parked car. I peek out to see the man hasn't moved. Whew! Nobody heard me."
            
            
        #show miguel hap

        "The man splits into a wide smile when he sees Kaori and he envelopes her into another hug. Then he plants a kiss on her cheek. Kaori embraces him back."
        
        if E2KIS2_Response == "Boyfriend":
            "I knew it! He {i}is{/i} her boyfriend!"
        
        else:
            menu:
                "She's not in her right mind!":
                    "He's clearly brainwashed her! There's no other way to explain how he's still intact."
                    "That means she's in trouble, and I need to help her!"
        
                "What is up with bizzaro Kaori?":
                    "I try to imagine what would happen if I not only tried to embrace Kaori, but also tried to kiss her… and I can't help but wince. Instinctively, I go to protect my family jewels."
            
                "He's too familiar with her.":
                    "I don't like how familiar he is with her… It doesn't seem right. I need to get to the bottom of this to make sure Kaori's not being taken advantage of." 
        
        hide miguel with dissolve
        hide kaori with dissolve
        "The man takes the grocery bags and places them in the car, then both he and Kaori climb inside."
        #stop ambient fadeout 3
        scene black with dissolve
        "I dive out of my hiding place and sprint to my bike. {w}I can't let them out of my sight!"
        scene bg campus intersection day with fade
        "Luckily, I'm parked close enough to spot them exiting the parking lot. I keep a good distance between us as I speed down the road behind them."
        "I try to keep a car between us to block me from view, but every so often a vehicle will switch lanes, leaving me exposed. Still, the white car doesn't change pace or give any indication it knows it's being followed. {w}I must be better at this than I thought!"
        scene black with fade
        stop music fadeout 5
        $renpy.pause(1)
        play ambient "audio/ambience/Morning.ogg" fadein 3
        scene bg isokaze shrine dusk with fade:
            xzoom .8
            yzoom .8
        "After a while, the car turns into a weathered driveway. The driveway is attached to an older house with a wide, fenced-in yard. Children ranging in age from 3 to 10 play in the yard. {w}Is this a school of some sort?"
        
        play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 10
        show kaori smi at cc with dissolve
        "I linger back and watch as Kaori exits the car. As soon as she does, the younger children swarm over to hug her legs. Kaori laughs when she sees the kids and opens her arms wide to return their hugs."
        show heart:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori hap b1 at cc with dissolve
        "A bright smile graces her face and she's warm and gentle as she herds the kids back into the yard. The older children greet her with respect, but it's clear they're just as happy to see her. {w}This is such a different Kaori from the one I know… and even though she'd kill me if she ever found out I saw this side of her, I'm glad I did."
        
        menu:
            "Leave before she sees me.":
                stop music fadeout 5
                "Speaking of which, I should leave now if I'd like to avoid the wrath of Kaori! I can return her groceries to her later."
                scene black with fade
                stop ambient fadeout 5
                "Quietly, I wheel my bike around and sneak off before she is able to spot me. {w}I think about Kaori and the kids my entire drive home." 
                $renpy.pause(1)
                #day 6
                jump E2D6S2
        
            "Return her groceries.":
                "Kicking my bike into park, I grab the grocery bags and walk over to the house."
                stop music fadeout 5
                show exclamation:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori sur at cc with dissolve
                $renpy.pause(1)
                show kaori neu at cc with dissolve
                "As I come into view, surprise flickers across Kaori's face, before it's replaced by an emotionless mask."
                "She waits for me in the driveway."
                voice "audio/voice/E2/Free/KI/116.ogg"
                ki "What are you doing here? Are you spying on me?"
                "I hand her the groceries."
                pf "No, our bags got mixed up. These are yours."
                play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
                show kaori cur at cc
                "With a wary look, she peeks into the bags."
                show kaori ner at cc
                voice "audio/voice/E2/Free/KI/117.ogg"
                ki "Oh..."
                "For a second she seems at a loss for how to react. Then her familiar glare returns."
                show kaori ann at cc
                voice "audio/voice/E2/Free/KI/118.ogg"
                ki "Well, you shouldn't have followed me without my knowledge like some sort of creep!"
        
                menu:
                    "You're right.":
                        pf "I'm sorry. I tried to catch you in the parking lot, but I was too slow."
                        show kaori dis at cc
                        voice "audio/voice/E2/Free/KI/119.ogg"
                        ki "You were watching me in the parking lot too?"
                        pf "Yeah--I mean no! I went to find my bike and saw you leaving."
        
                    "It's okay if it's for a good cause.":
                        pf "It's not creepy if it's for a legit reason."
                        show kaori dis at cc
                        "She crosses her arms."
                        voice "audio/voice/E2/Free/KI/120.ogg"
                        ki "You mean to return these bags to me?"
                        pf "Exactly! I'm such a good samaritan."
                        show kaori ske at cc
                        voice "audio/voice/E2/Free/KI/121.ogg"
                        ki "You could have swapped bags with me back at the mall."
                        pf "No way. You ran off in a hurry and I lost you."
                        show kaori dis at cc
                        voice "audio/voice/E2/Free/KI/122.ogg"
                        ki "If you lost me, how'd you follow me?"
                        pf "Easy, I found you again in the parking lot when I was looking for my bike."
        
                    "Geez, so ungrateful.":
                        "What is she getting so angry about? I'm the one who went out of my way to do something nice."
                        pf "A \"thank you\" would be appreciated."
                        show storm:
                            xoffset 720
                            yoffset 110
                            xzoom .75
                            yzoom .75
                        voice "audio/voice/E2/Free/KI/123.ogg"
                        ki "I'm not going to thank you for spying on me."
                        pf "Hey, if you hadn't left in such a hurry earlier, I could have returned these back in the parking lot."
                        show kaori dis at cc
                        "She crosses her arms."
                        voice "audio/voice/E2/Free/KI/124.ogg"
                        ki "So basically, you've been following me since the parking lot."
                        pf "No, once you ran I went to find my bike."
        
                stop music fadeout 5
                pf "Speaking of which, I'm surprised you didn't notice me following you at all."
        
                if E1D2S3_EncounteredKaori == 1:
                    pf "Although, it's not the first time you didn't see me coming until I was already there."
                    show vein:
                        xoffset 720
                        yoffset 110
                        xzoom .75
                        yzoom .75
                    "Kaori clenches her fists"
                    show kaori ann at cc
                    voice "audio/voice/E2/Free/KI/125.ogg"
                    ki "I'm going to pretend you didn't say that."
                    show kaori thi at cc
        
                else:
                    show kaori thi at cc
                    "Kaori frowns in thought."
        
                voice "audio/voice/E2/Free/KI/126.ogg"
                ki "Your bike is white, right? You must have been really discreet because I didn't see it at all."
                play music "audio/music/Baka! (GAME VERSION).ogg" fadein 5
                show kaori neu at cc
                voice "audio/voice/E2/Free/KI/127.ogg"
                ki "Although, now that you mention it, there was this really weird-looking bike that would occasionally pop into view… but it was clearly a girl's so I know that… wasn't…you..."
                show kaori cur at cc
                show dots:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                "Her voice trails off when she notices my expression. {w}Her hand flies to her mouth and she seems to be concentrating hard on holding something in."
                pf "What?"
                show kaori smi at cc with dissolve
                "She shakes her head. Avoiding my eyes, her gaze flickers all around me. When they land on my bike behind me, the floodgates open and her laugh rings across the yard."
                show kaori hap at cc with dissolve
                voice "audio/voice/E2/Free/KI/128.ogg"
                ki "Hahaha! That was {i}you{/i}?"
                "I mumble an affirmation."
                show kaori mis at cc
                voice "audio/voice/E2/Free/KI/129.ogg"
                ki "Oh my god! Hahaha!"
                pf "Yeah, yeah, laugh it up."
                show note:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori hap at cc
                "She gasps for breath as her laughter continues. Her eyes are even tearing up."
                pf "Okay, it's not {i}that{/i} funny…"
                show kaori mis at cc
                "After a few more breaths, Kaori finally calms down."
                stop music fadeout 5
                voice "audio/voice/E2/Free/KI/130.ogg"
                ki "That's a good look for you."
                pf "Very funny."
        
                voice "audio/voice/E2/missing/miguel/miguel_01.ogg"
                "Mysterious Man" "Kaori? What is so funny?"
                show kaori cur at cc
                show miguel mis at r3 with dissolve:
                    xzoom -1
                "The man walks over and gives Kaori a questioning look when he sees me."
                play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 10
                show kaori smi at cc
                voice "audio/voice/E2/Free/KI/131.ogg"
                ki "Oh, this is my teammate from school."
                show miguel sur at r3
                show exclamation:
                    xoffset 1150
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E2/missing/miguel/miguel_02.ogg"
                "Mysterious Man" "Ah! A friend of Kaori's!"
                show miguel hap at r3
                "His face splits into a huge grin and he hurries over to plant a kiss on each of my cheeks."
                show kaori mis at cc
                "Kaori watches in amusement as I can only stand in shock."
                show miguel smi at r3
                voice "audio/voice/E2/missing/miguel/miguel_03.ogg"
                mv "I am Miguel Vazquez, but please call me Uncle Miguel."
                voice "audio/voice/E2/missing/miguel/miguel_04.ogg"
                mv "So happy to meet you!"
                pf "Uh, hello, I'm [pfirst]."
                "I flash Kaori a confused look."
                show kaori smi at cc
                voice "audio/voice/E2/Free/KI/132.ogg"
                ki "He's my uncle."
                show miguel mis at r3
                voice "audio/voice/E2/missing/miguel/miguel_05.ogg"
                mv "Yes. Kaori doesn't let me meet her friends so you must be very special."
                voice "audio/voice/E2/missing/miguel/miguel_06.ogg"
                mv "Her boyfriend?"
                show kaori sur b1 at cc with dissolve
                voice "audio/voice/E2/Free/KI/133.ogg"
                ki "No!"
        
                menu:
                    "B-Boyfriend?!":
                        "I put up my hands defensively."
                        show kaori neu b1 at cc with dissolve
                        pf "N-No! Nothing like that!"
                        show miguel sur at r3
                        voice "audio/voice/E2/missing/miguel/miguel_07.ogg"
                        mv "Why not? You don't like her?"
                        show kaori thi b2 at cc with dissolve
                        pf "Well, I didn't say that--"
                        show note:
                            xoffset 1150
                            yoffset 5
                            xzoom .75
                            yzoom .75
                        show miguel hap at r3
                        voice "audio/voice/E2/missing/miguel/miguel_08.ogg"
                        mv "So you do like her!"
        
                    "Of course we're a couple!":
                        show kaori cur b1 at cc with dissolve
                        pf "I've always known we have a special bond, Kaori."
                        "I lean in close to her."
                        show question:
                            xoffset 720
                            yoffset 110
                            xzoom .75
                            yzoom .75
                        show kaori ske b2 at cc with dissolve
                        voice "audio/voice/E2/Free/KI/134.ogg"
                        ki "H-Huh?"
                        pf "And even your uncle can see it too. We shouldn't deny this attraction any longer!"
                        show kaori sur b2 at cc with dissolve
                        voice "audio/voice/E2/Free/KI/135.ogg"
                        ki "I-Idiot! You're delusional!"
                        show tsuBlush:
                            xoffset 720
                            yoffset 110
                            xzoom .75
                            yzoom .75
                        show kaori thi b2 at cc
                        "But she can't stop the blush from staining her cheeks."
                        show note:
                            xoffset 1150
                            yoffset 5
                            xzoom .75
                            yzoom .75
                        show miguel hap at r3
                        voice "audio/voice/E2/missing/miguel/miguel_09.ogg"
                        mv "That was so beautiful! Bravo!"
        
                    "She wishes.":
                        show kaori neu at cc with dissolve
                        "I snort."
                        pf "Definitely not."
                        show kaori dis at cc
                        "Kaori frowns and crosses her arms."
                        voice "audio/voice/E2/Free/KI/136.ogg"
                        ki "Obviously, because I don't date idiots."
                        pf "You don't date, period."
                        show kaori ann b1 at cc with dissolve
                        voice "audio/voice/E2/Free/KI/137.ogg"
                        ki "What's that suppose to mean?!"
                        show note:
                            xoffset 1150
                            yoffset 5
                            xzoom .75
                            yzoom .75
                        show miguel hap at r3
                        voice "audio/voice/E2/missing/miguel/miguel_10.ogg"
                        mv "Ah, already bickering like a married couple… so precious."
        
                show shoBlush:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori sur b2 at cc with dissolve
                voice "audio/voice/E2/Free/KI/138.ogg"
                ki "Uncle!"
                show kaori ner b2 at cc
                "Kaori's face is beet red."
                voice "audio/voice/E2/Free/KI/139.ogg"
                ki "Don't you have kids to help or something?"
                show miguel smi at r3
                "Miguel is unperturbed and chuckles."
                voice "audio/voice/E2/missing/miguel/miguel_11.ogg"
                mv "Okay, okay, I understand. I will let you lovebirds have some space."
                show kaori ann b2 at cc
                voice "audio/voice/E2/Free/KI/140.ogg"
                ki "We're not lovebirds!"
                show miguel mis at r3
                "He winks as he goes to join the children."
                hide miguel with dissolve
                $renpy.pause(1)
                show kaori thi b1 at cc with dissolve
                show dots:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                "Kaori and I stand in silence and she fidgets with her hands. Her face is still bright red and she can't look me in the eyes. {w}After a moment, the silence grows too heavy and we speak at the same time."
                show kaori neu at cc with dissolve
                voice "audio/voice/E2/Free/KI/141.ogg"
                ki "Ignore him--"
                pf "So your uncle, huh?"
                show kaori cur at cc
                "She blinks at me."
                pf "He's pretty, uh, affectionate."
                show kaori neu at cc
                voice "audio/voice/E2/Free/KI/142.ogg"
                ki "Oh yeah. He's Spanish and that's how they greet each other in Spain. It took a while for me to get used to it too."
                pf "That explains a lot. How did he and your aunt meet?"
                show kaori smi at cc
                voice "audio/voice/E2/Free/KI/143.ogg"
                ki "In university, he studied in Japan. That's why his Japanese is so good too."
        
                show kaori neu at cc
                "We lapse into silence again. {w}Kaori returns to the white car and hands me my groceries."
                voice "audio/voice/E2/Free/KI/144.ogg"
                ki "Thanks for bringing these by, I guess."
                show kaori smi at cc
                voice "audio/voice/E2/Free/KI/145.ogg"
                ki "You should probably get going. I have to get back to the kids."
                pf "What exactly is this place?"
                show kaori cur at cc
                "She hesitates, then sighs in resignation."
                show kaori neu at cc
                voice "audio/voice/E2/Free/KI/146.ogg"
                ki "Uh... It's a daycare and tutoring center. My uncle runs it and I come by to help out."
        
                menu:
                    "I knew you were a softie.":
                        pf "The kids seem to really like you."
                        show kaori smi at cc
                        voice "audio/voice/E2/Free/KI/147.ogg"
                        ki "Well, I have been coming by since high school."
                        pf "You must be like a big sister to them."
                        show note:
                            xoffset 720
                            yoffset 110
                            xzoom .75
                            yzoom .75
                        voice "audio/voice/E2/Free/KI/148.ogg"
                        ki "Yeah, they're all really good kids. Smart too."
        
                    "Mommy material!":
                        pf "I had no idea you liked kids so much."
                        show kaori thi at cc
                        voice "audio/voice/E2/Free/KI/149.ogg"
                        ki "So? What if I do?"
                        "I nod, satisfied."
                        pf "You will make a great mother one day."
                        show kaori sur b1 at cc with dissolve
                        voice "audio/voice/E2/Free/KI/150.ogg"
                        ki "What?!"
                        pf "But will you make a fine wife too?"
                        show kaori ang b1 at cc
                        voice "audio/voice/E2/Free/KI/151.ogg"
                        ki "Shut up!"
                        ### NOTE Points - "IF high points with Kaori:"
                        # temporarily set to 0
                        if kaoromance > 0:
                            show tsuBlush:
                                xoffset 720
                                yoffset 110
                                xzoom .75
                                yzoom .75
                            show kaori thi b2 at cc with dissolve
                            "I see the blush creep on her cheeks before she turns away."
        
                    "That's so unlike you.":
                        pf "I'm surprised the kids like you so much."
                        show kaori ske at cc
                        voice "audio/voice/E2/Free/KI/152.ogg"
                        ki "What does that mean?"
                        pf "You just aren't exactly the most warm and nurturing person."
                        show kaori dis at cc
                        "She crosses her arms."
                        voice "audio/voice/E2/Free/KI/153.ogg"
                        ki "I shouldn't have to nurture people my age."
                        "I suppose that's valid."
        
                pf "Still, how did you get involved?"
                show kaori neu at cc with dissolve
                voice "audio/voice/E2/Free/KI/154.ogg"
                ki "I started coming here as a co-op for class credit, and now I can't imagine my life without them."
                show kaori smi at cc
                "I watch Kaori as she speaks. Her expression is soft as her voice is warm."
                voice "audio/voice/E2/Free/KI/155.ogg"
                ki "Most of these kids have parents who work all the time, and it's obvious these kids are lonely. They might act out or struggle in school, but all they really want is for someone to care about them."
                voice "audio/voice/E2/Free/KI/156.ogg"
                ki "This place might not be the most glamorous, but Uncle cares about every single kid who walks through those doors, and they care about him."
                show kaori dis at cc
                "Then her voice hardens."
                voice "audio/voice/E2/Free/KI/157.ogg"
                ki "Anyway, if you tell anyone about this, I will destroy you."
                pf "Noted."
        
                show kaori cur at cc
                "The kids wave at Kaori and call out for her to join them. With minimal urging from Miguel, they sing \"Ms. Itami and Mr. Boyfriend sitting in a tree! K-I-S-S-I-N-G!\"."
                show kaori sur b1 at cc with dissolve
                "Miguel laughs at Kaori's mortification."
                show kaori ner b2 at cc
                pf "Uh, I better go."
                "Her face is completely red."
                show drop:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E2/Free/KI/158.ogg"
                ki "Yes, please."
                hide kaori with dissolve
                "I head back to my bike as Kaori runs towards the children. They scatter around the yard, squealing in laughter."
                "Kaori puts on a hard exterior, but she's not as cold as she pretends to be."
                stop music fadeout 5
                "I glance back for one more glimpse of Kaori's smile before driving off."
                $ E2KIS4_Completed = 1
                scene black with fade
                stop ambient fadeout 3
                $renpy.pause(1)
                
                jump E2D6S2

