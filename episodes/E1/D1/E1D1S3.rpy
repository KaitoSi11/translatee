label E1D1S3:
    
    #Ambience Suburbs
    pf "..."
    
    $renpy.pause(1)
    voice "audio/voice/E1/D1/S3/Kaito/2.ogg"
    hk "Welcome home!"
    
    play ambient "audio/ambience/Night Crickets.ogg" fadein 1
    scene white with fade
    scene bg homekaito main night with Dissolve(2.5)
    $renpy.pause(1)
    
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 1
    
    "This place is the opposite of the cozy-yet-cramped apartment I expected. Instead, I feel like I've just walked into the cover of a home decor magazine."
    
    show kaito smi at r2 with dissolve:
        xzoom -1
    voice "audio/voice/E1/D1/S3/Kaito/3.ogg"
    hk "You guys hungry? Dinner should be here soon."
    
    show nikki hap at l2 with dissolve
    voice "audio/voice/E1/D1/S3/Nikki/1.ogg"
    sf "Sweet! What are we having?"
    show kaito mis at r2
    voice "audio/voice/E1/D1/S3/Kaito/4.ogg"
    hk "Well, I figured it’d be good to expose you to some {i}true{/i} Japanese cuisine!"
    pf "Which is?"
    show kaito hap at r2
    voice "audio/voice/E1/D1/S3/Kaito/5.ogg"
    hk "Sushi, of course! 100\% bonafide {i}nigirizushi to makizushi{/i}!"
    show kaito smi at r2
    
    $ E1D1S3_mcdoesntlikesushi = 0
    
    menu:
        "Sushi!":
            pf "Great! I love sushi."
            
            show kaito hap at r2
            show nikki smi at l2
            
            "Kaito grins."
            voice "audio/voice/E1/D1/S3/Kaito/6.ogg"
            hk "Your American sushi can't even begin to compare to the {i}authentic{/i} stuff."
               
        "Sounds good.":
            pf "I could do with some cold, raw fish."
            
            show kaito smi at r2
            show nikki ske at l2
            show drop:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            $renpy.pause(1)
            voice "audio/voice/E1/D1/S3/Nikki/2.ogg"
            sf "Somehow, when you say it, it doesn't sound so appetizing anymore..."
            "Kaito lets out a hearty laugh."
    
        "Damnit, I hate raw fish.":
            $ E1D1S3_mcdoesntlikesushi = 1
            pf "Sushi? Hmm..."
            
            show kaito mis at r2
            show nikki smi at l2
            
            "Kaito winks at me."
            voice "audio/voice/E1/D1/S3/Kaito/7.ogg"
            hk "Don’t worry, kiddo, not everything is sashimi. Trust me, you'll love it!"
            "I'm still not convinced."
            
    show kaito smi at r2
    show nikki neu at l2
    
    voice "audio/voice/E1/D1/S3/Kaito/8.ogg"
    hk "By the way, your things came in a few days ago. I put them in your rooms. Why don't you two go upstairs and start unpacking while I get dinner ready."
    pf "Sounds good."
    
    show nikki smi at l2
    
    "Nikki nods and we head upstairs together."  
    
    scene black with fade
    
    pf "..."
    
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
    
    $renpy.pause(2)
         
    #BG My Room
    scene bg homekaito myroom night packed with fade
    
    $ kaiOut = "sCasual"
    
    "The hallway upstairs is narrower than the one back home, but Kaito's house is not small. {w}Nikki heads into the first room on the right. {w}My room is right beside hers, and Kaito's is further down the hall."                                                     
            
    "Even with all of the boxes lying around, I'm surprised by how spacious my room is. It might even be larger than my dorm room at CINY."
    
    "I head over to the wall and sit on the edge of my bed. Thank goodness Kaito had the beds made before we arrived. {w}I don't even remember which box holds my linens. {w}Maybe it's this one?"
    
    "I pull the nearest box towards me and rip open the top. Just clothes in here. May as well start putting some of this away, though."
    
    "I've just emptied the box when Kaito's voice echoes from downstairs."
            
    voice "audio/voice/E1/D1/S3/Kaito/9.ogg"
    hk "{b}HEY GUYS! FOOD’S HERE!{/b}"
    
    scene black with fade
    #The Alpha build does a cool "persona-y" sliding transition of this, but for now we'll just fade
    "—After Dinner—"
    
    
    #BG Uncle Kaitos Home
    scene bg homekaito main night with fade
    
    show kaito smi at r2:
        xzoom -1
    show nikki win at l2
    with dissolve
    show storm:
        xoffset 365
        yoffset 160
        xzoom .75
        yzoom .75
    $renpy.pause(1)
    voice "audio/voice/E1/D1/S3/Nikki/3.ogg"
    sf "Ugh, I'm stuffed..."
    
    show nikki neu at l2
    
    menu:
        "OM NOM NOM!":
            if (E1D1S3_mcdoesntlikesushi == 0):
                "I eagerly reach for more even after both Nikki and Kaito have put down their chopsticks."
                
                show kaito cur at r2
                show exclamation:
                    xoffset 1040
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D1/S3/Kaito/10.ogg"
                hk "You weren't kidding about liking sushi..."
                
                show nikki hap at l2
                voice "audio/voice/E1/D1/S3/Nikki/4.ogg"
                sf "You should see him at an all-you-can-eat buffet! It’s like watching a vacuum cleaner, if vacuum cleaners could eat."
                "I  finish the last piece and heave a satisfied sigh."
                
                show kaito smi at r2
                voice "audio/voice/E1/D1/S3/Kaito/11.ogg"
                hk "So, what’s the verdict on {i}authentic{/i} sushi?"
                pf "Hmm... not bad."
                
                show nikki mis at l2
                voice "audio/voice/E1/D1/S3/Nikki/5.ogg"
                sf "\"Not bad\" he says with a mouth full of sushi and rice all over his face!"
                
                show kaito hap at r2
                show nikki smi at l2
                
                "Nikki and Kaito seem amused as I brush away the rice on my face."
                         
            else:
                "I eagerly reach for more even after both Nikki and Kaito have put down their chopsticks."
                
                show kaito ske at r2
                show question:
                    xoffset 1040
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D1/S3/Kaito/12.ogg"
                hk "Are you sure you don’t like sushi?"
                
                show nikki sur at l2
                show shocked:
                    xoffset 365
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D1/S3/Nikki/6.ogg"
                sf "Wow. He’s really wolfing it down!"
                "I finish the last piece and stifle a burp."
                
                show kaito cur at r2
                voice "audio/voice/E1/D1/S3/Kaito/13.ogg"
                hk "So, what'd you think?"
                pf "It's okay."
                
                show kaito mis at r2
                
                "Kaito sees right through my attempt to play it cool and smiles in triumph."
                
        "I'm feeling full too...":
            pf "Ditto."
            
            show kaito hap at r2
            
            "Kaito eats the last piece of sushi and washes it down with some green tea."
            show note:
                xoffset 1040
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D1/S3/Kaito/14.ogg"
            hk "Ahhh, that hit the spot!"
    
    show kaito smi at r2
    show nikki neu at l2
    with dissolve
    
    "Kaito leans back in his chair, resting his hands behind his head."
    voice "audio/voice/E1/D1/S3/Kaito/15.ogg"
    hk "So, what was CINY like?"
    
    pf "The usual. Exams, a messy dorm room, a part-time job."
    
    show nikki hap at l2
    voice "audio/voice/E1/D1/S3/Nikki/7.ogg"
    sf "And you still managed to save enough money to buy yourself a bike."
    
    pf "True. I could have bought it sooner if maintaining a GEAR wasn't such a money sink."
    
    show kaito cur at r2
    show nikki neu at l2
    voice "audio/voice/E1/D1/S3/Kaito/16.ogg"
    hk "Oh, you're still using your original GEAR?"
    
    pf "Yup."
    
    show kaito ske at r2
    voice "audio/voice/E1/D1/S3/Kaito/17.ogg"
    hk "Is it giving you trouble? You should probably replace it if it needs that many fixes."
    
    "Everyone says that, but when I think about all the time I spent with Dad… {w}I'm not ready to put those memories aside, especially now that they can never be replaced. {w}Besides, Dad was great at what he did. I know there's still plenty of fight left in that mech."
            
    pf "I guess, but Dad and I worked on it together. A lot of blood, sweat, and tears went into it and I'm not quite ready to give up on all of that hard work."
    
    show kaito neu at r2
    show nikki hap at l2
    voice "audio/voice/E1/D1/S3/Nikki/8.ogg"
    sf "It's true. Especially that one time when butterfingers here dropped the torch. Remember that? There was {i}a lot{/i} of blood--"
    
    pf "{b}Nikki!{/b}"
    
    show nikki smi at l2
    
    "She smiles sweetly at me."
    
    show nikki mis at l2
    voice "audio/voice/E1/D1/S3/Nikki/9.ogg"
    sf "What? I'm just backing you up, big bro."
    
    show kaito hap at r2
    
    "Uncle Kaito laughs."
    
    show kaito smi at r2
    show nikki neu at l2
    voice "audio/voice/E1/D1/S3/Kaito/18.ogg"
    hk "I understand. It should be arriving at the academy any day now. All you'll have to do is present the proper ID to claim it."
    
    show kaito sur at r2
    show exclamation:
        xoffset 1040
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D1/S3/Kaito/19.ogg"
    hk "Oh yeah, that reminds me..."
    
    "Uncle Kaito jumps to his feet and grabs something off a nearby table. {w}He returns with a packet of papers, which he hands to Nikki."
    
    show kaito neu at r2
    voice "audio/voice/E1/D1/S3/Kaito/20.ogg"
    hk "Here are your transfer papers. They're already filled out and all the docs you need are in there. All you have to do is hand this to the headmaster first thing tomorrow morning."
    
    show nikki hap at l2
    voice "audio/voice/E1/D1/S3/Nikki/10.ogg"
    sf "Okay! Thanks, Uncle."
    
    show kaito smi at r2
    voice "audio/voice/E1/D1/S3/Kaito/21.ogg"
    hk "Here."
    
    "He hands each of us a SIM card."
    voice "audio/voice/E1/D1/S3/Kaito/22.ogg"
    hk "Put these SIM cards into your phones. I've already added credit to them to start you off."
    
    show kaito neu at r2
    show nikki smi at l2
    
    "Kaito looks over at me."
    voice "audio/voice/E1/D1/S3/Kaito/23.ogg"
    hk "And you took care of your transfer stuff?"
    
    show bg homekaito main night:
        linear .30 yoffset -50
        linear .30 yoffset 0
        linear .30 yoffset -50
        linear .30 yoffset 0
        
    show kaito neu:
        linear .30 yoffset -70
        linear .30 yoffset 0
        linear .30 yoffset -70
        linear .30 yoffset 0
    
    show nikki smi:
        linear .30 yoffset -70
        linear .30 yoffset 0
        linear .30 yoffset -70
        linear .30 yoffset 0
    
    
    "I nod."
    
    show kaito smi at r2
    voice "audio/voice/E1/D1/S3/Kaito/24.ogg"
    hk "Great."
    
    "I pop the new SIM card into my phone."

    "After a moment of waiting, the phone boots up to an empty contacts list. I quickly exchange numbers with Nikki and Uncle Kaito. I can add the rest of my old contacts later."
    voice "audio/voice/E1/D1/S3/Kaito/25.ogg"
    hk "Don't hesitate to call me if you need anything."
    
    pf "We won't."
    
    show nikki neu at l2 with dissolve
    $renpy.pause(1)
    
    "The conversation lulls into a silence."
    
    pf "Hey, Nikki, we should probably unpack a bit before the jet lag takes over."
    
    show nikki smi at l2
    voice "audio/voice/E1/D1/S3/Nikki/11.ogg"
    sf "Good idea."
    voice "audio/voice/E1/D1/S3/Kaito/1.ogg"
    hk "Alright. Don't stay up too late, though. You both have a long day ahead of you tomorrow."
    
    "We excuse ourselves from the table and head upstairs."
    
    scene black with fade
    
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
    
    stop music fadeout 3
    
    $renpy.pause(3)
    
    jump E1D1S4
