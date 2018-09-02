#
label E3D2S1:
    
    #beep beep
    $ nikOut = renpy.random.choice(['sCasual2'])
    $ nikHairF = renpy.random.choice(['default'])
    $ nikHairB = renpy.random.choice(['default'])
    
    $renpy.pause(1)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1)
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(2.5)
    scene bg homekaito myroom day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    stop sound fadeout 1
    
    "I wake up energised and throw off the blankets before getting dressed. Since we're going directly to the beach, I decide to just wear my swim trunks and a shirt."
    scene bg homekaito main day with fade
    "Nikki is waiting for me downstairs. She's wearing a cover-up and has a bag slung over her shoulder."
    
    show nikki smi at cc with dissolve
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_001.ogg"
    sf "Finally!"
    pf "Hey, I'm on time for once!"
    show nikki ske at cc
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_002.ogg"
    sf "So? I've been awake for at least an hour."
    pf "Why'd you get up so early?"
    show nikki hap at cc
    "Nikki beams and fidgets with excitement."
    show note:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_003.ogg"
    sf "How could I sleep when I have such a fun day ahead of me?"
    "The bag jostles as she fidgets."
    pf "What's in the bag?"
    show nikki neu at cc
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_004.ogg"
    sf "Just beach stuff… extra clothes, towels, sunscreen… you know."
    pf "That's actually pretty smart."
    show nikki smi at cc
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_005.ogg"
    sf "I know."
    "Nikki pushes me towards the door."
    show nikki hap at cc
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_006.ogg"
    sf "Come on, let's go already!"
    pf "Alright! Let me just grab my keys."
    
    hide nikki with dissolve
    stop ambient fadeout 3
    scene black with fade
    
    "After collecting my things, Nikki and I climb on my bike and we hit the road."
    # music stop to change?
    stop music fadeout 3
    
    $renpy.pause(1)
    play ambient "audio/ambience/beach day.ogg" fadein 5
    $renpy.pause(1)
    scene bg vacation beach day with Dissolve(2.5):
        xzoom 1
        yzoom 1
        xalign .01
        yalign .99
    # music
    $renpy.pause(.5)
    
    #BEACH
    
    $ akiOut = "sSwimsuit"
    
    $ kaoOut = "sSwimsuit"
    $ kaoHairB = "default"
    $ kaoHairF = "default"
    
    $ mayOut = "sSwimsuit"
    
    $ meiOut = "sSwimsuit"
    
    $ shoOut = "sSwimsuit"
    
    $ valOut = "sSwimsuit"
    $ valHairB = "default"
    $ valHairF = "default"
    
    $ yuuOut = "sSwimsuit"
    $ yuuHairB = "default"
    $ yuuHairF = "default"
    
    "Nikki hops off my bike as soon as I park and sprints out towards the sand."
    pf "Wait!"
    "She either doesn't hear me or ignores me. {w}Of course that means I'm stuck carrying all the stuff. {w}With a sigh, I sling the bag over my shoulder and follow her."
    "As I walk on the sand, I scan the beach for my friends, but I don't see anyone I recognize. We must be the first ones here."
    
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
    
    show nikki smi at cc with dissolve
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_007.ogg"
    sf "Oh sun, how I've missed you!"
    pf "We've had sun back home too…"
    show nikki hap at cc
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_008.ogg"
    sf "It's not the same!"
    hide nikki with dissolve
    "She continues to skip and dance in the sand, then spins in a cartwheel. She grins at me."
    
    menu:
        "Let Nikki have her fun.":
            "I grin back and continue to trudge along behind her."
            show nikki ske at cc
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_009.ogg"
            sf "What are you doing? You don't have to carry all that stuff."
            pf "What about setting up?"
            show nikki smi at cc
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_010.ogg"
            sf "We can do that later. This is way more fun! Come on, come join me!"
            #(Jump menu)
    
        "You call that a cartwheel?":
            pf "Were you trying to do a cartwheel or a somersault?"
            show nikki cur at cc
            "Nikki pauses and crosses her arms."
            show nikki mis at cc
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_011.ogg"
            sf "You think you can do better?"
            #(Jump menu)
    
    
        "It's like having a puppy…":
            "I wait for Nikki to get tired, but she seems to have endless energy."
            pf "Nikki!"
            "She just laughs and does another cartwheel."
            show nikki hap at cc
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_012.ogg"
            sf "Come join me, bro!"
            pf "We should set up."
            show nikki neu at cc
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_013.ogg"
            sf "We can do that later."
            show nikki cur at cc
            "She pauses, then grins mischievously."
            show nikki mis at cc
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_014.ogg"
            sf "Or maybe you don't know how to do cartwheels?"
            pf "I know how."
            show note:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_015.ogg"
            sf "Prove it!"
            #(Jump menu)
    
    #(Menu)
    menu:
        "Okay!":
            pf "Alright then, stand back and let the master show you how it's done."
            show nikki neu at cc
            "I kick off my shoes and drop the bag."
    
            if MCStory == 1:
                "Windmilling my arms, I push my legs off the ground. They fly through the air in a graceful arc and land on solid ground while the momentum pulls me upright."
                pf "Voila!"
                show nikki smi at cc
                "Nikki shrugs."
                voice "audio/voice/E3/D2/S1/nikki/Nikki_2_016.ogg"
                sf "I guess that wasn't too bad."
                pf "It was a masterpiece!"
                show drop:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E3/D2/S1/nikki/Nikki_2_017.ogg"
                sf "I wouldn't go that far…"
            
            else:
                "Windmilling my arms, I push my legs off the ground and try to lift them in the air. They almost make it halfway before losing momentum and I fall to the side, off balance."
                show nikki smi at cc
                "Nikki's laugh rings in my ears."
                voice "audio/voice/E3/D2/S1/nikki/Nikki_2_018.ogg"
                sf "Good one, bro. You really showed me."
                pf "It worked better in my head."
                show nikki mis at cc
                voice "audio/voice/E3/D2/S1/nikki/Nikki_2_019.ogg"
                sf "If only the rest of you understood physics as well as your head does."
                
            show nikki neu at cc
            "As we both catch our breath, Nikki glances at the forgotten bag."
    
        "No.":
            pf "Eh, I'm good here."
            show nikki dis at cc
            "Nikki pouts and walks over."
            show storm:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_020.ogg"
            sf "Way to ruin the fun, Fun Police."
            pf "I didn't say you had to stop."
            show nikki wor at cc
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_021.ogg"
            sf "The moment's gone!"
            show nikki neu at cc
            "She glances around her."
            
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_022.ogg"
    sf "Let's just set up here."
    pf "Okay."
    hide nikki with dissolve
    $ nikOut = "sSwimsuit"
    "We each lay out a towel from the bag. Nikki pulls her cover-up over her head, revealing a frilly two-piece."
    show nikki neu at cc with dissolve
    
    menu:
        "Where's the rest of your swimsuit?":
            "Using the towel still in my hand, I try to wrap it around her."
            show nikki ske at cc
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_023.ogg"
            sf "What are you doing?!"
            pf "Uh, Nikki, some of your swimsuit is missing."
            show exclamation:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            show nikki sur at cc
            "She pushes me away."
            show nikki ang at cc
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_024.ogg"
            sf "Ah! Stop!"
            show nikki dis at cc
            pf "I can see your midriff!"
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_025.ogg"
            sf "You're overreacting. I mean, I'm not dressed like that girl."
            "She points to a woman in a barely-there string bikini. My eyes widen in horror as I unwittingly picture Nikki wearing {i}that{/i}."
            pf "Noooo! My innocent imouto!"
            show nikki thi at cc
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_026.ogg"
            sf "You are so weird sometimes."
    
        "You're wearing something sensible.":
            "I breathe a sigh of relief."
            pf "Oh good, you're wearing that."
            show nikki ske at cc
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_027.ogg"
            sf "Um, okay?"
            pf "No, it's a good thing. It's sturdy."
            show question:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_028.ogg"
            sf "What?"
            pf "What if you'd been wearing something like {i}that{/i}."
            show nikki dis at cc
            "I point to a woman wearing a string bikini."
            pf "Any guy could come by and \"accidentally\" pull on a string and then her whole top would… fall… off…"
            "My voice trails off as I imagine the strings slipping down the woman's shoulders, freeing her voluptuous breasts…"
            show storm:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            "Nikki wrinkles her nose."
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_029.ogg"
            sf "Um yeah, next time keep your weird fantasies to yourself."
    
        "Don't comment on it.":
            "I'm glad Nikki chose a sensible swimsuit. Sometimes it's hard to remember she's in high school, but it's only natural that she'll be wearing clothes that start to reflect that. At least she still has a sense of modesty."
            
    hide nikki with dissolve
    "As Nikki and I finish setting up, we're greeted by a familiar face."
    
    
    show mayu neu at l3:
        xoffset -250
    show shou hap at l2
    with dissolve
    
    show nikki neu at r2 with dissolve:
        xzoom -1
        
    voice "audio/voice/E3/D2/S1/shou/1.ogg"
    ss "Hey!"
    "A breathless Shou stands before us, carrying a large umbrella. Mayu stands beside him."
    pf "Hey Shou. Did you run all the way over here?"
    show drop:
        xoffset 365
        yoffset 20
        xzoom .75
        yzoom .75
    "He continues to gasp so Mayu answers for him."
    show mayu smi at l3
    voice "audio/voice/E3/D2/S1/mayu/Mayu-01.ogg"
    ma "Yeah, he saw you from the car and raced down here to say hi."
    pf "You didn't have to--"
    show shou smi at l2
    voice "audio/voice/E3/D2/S1/shou/2.ogg"
    ss "I thought I saw you with {i}another{/i} cute girl and had to get a closer look to be sure."
    show nikki smi b1 at r2
    show mayu neu at l3
    with dissolve
    stop music fadeout 3
    "Nikki giggles. I instinctively step in front of her."
    
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    
    show shou mis at l2
    voice "audio/voice/E3/D2/S1/shou/3.ogg"
    ss "Aren't you going to introduce me?"
    
    menu:
        "Don't hit on my sister!":
            pf "I don't like that tone you're taking..."
            show shou smi at l2
            voice "audio/voice/E3/D2/S1/shou/4.ogg"
            ss "You mean this very innocent and non-threatening tone?"
            pf "That's not the vibe I'm getting."
            show nikki neu b1 at r2
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_030.ogg"
            sf "Isn't he your friend? I'm sure you have nothing to worry about."
            show note:
                xoffset 365
                yoffset 20
                xzoom .75
                yzoom .75
            show shou hap at l2
            voice "audio/voice/E3/D2/S1/shou/5.ogg"
            ss "Yeah, the pretty lady gets it!"
            show regBlush:
                xoffset 1040
                yoffset 160
                xzoom .75
                yzoom .75
            show nikki smi b1 at r2
            "Nikki giggles again."
            show shou neu at l2
            pf "Nikki! Stop enjoying this!"
            stop music fadeout 3
            show nikki neu at r2 with dissolve
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_031.ogg"
            sf "Sometimes you just need to calm down, big bro."
    
        "Do you value your life?":
            pf "Not if you want to keep breathing."
            show frightful:
                xoffset 365
                yoffset 20
                xzoom .75
                yzoom .75
            show shou wor at l2
            show nikki ann at r2
            show mayu wor at l3
            with dissolve
            voice "audio/voice/E3/D2/S1/shou/6.ogg"
            ss "That's really intense…"
            show vein:
                xoffset 1040
                yoffset 160
                xzoom .75
                yzoom .75
            show nikki ang at r2
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_032.ogg"
            sf "Oh my god! Sometimes you are so embarrassing!"
            show nikki ann at r2
            pf "Hey, why are you taking his side?"
            show shou ner at l2
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_033.ogg"
            sf "He was just being nice."
            pf "He was creeping on my sister!"
            show mayu neu at l3
            show nikki dis at r2
            stop music fadeout 3
            voice "audio/voice/E3/D2/S1/nikki/Nikki_2_034.ogg"
            sf "I'm right here. You don't have to refer me in the third person."
    
        "No.":
            pf "Nope."
            show shou hap at l2
            voice "audio/voice/E3/D2/S1/shou/7.ogg"
            ss "C'mon, broseph, you already have all the girls falling for you. At least let me try with this cute one!"
            stop music fadeout 3
            pf "Don't talk about my sister like that!"
    
        "Do I need to whoop your ass again?" if E2D5SS_Completed == 1:
            pf "Remember what happened the last time you talked about my sister like that?"
            show shou wor at l2
            stop music fadeout 3
            "Shou immediately backs up."
            
    
    show shocked:
        xoffset 365
        yoffset 20
        xzoom .75
        yzoom .75
    show shou sur at l2
    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
    voice "audio/voice/E3/D2/S1/shou/8.ogg"
    ss "Your sister? Sorry! I didn't know!"
    show nikki smi at r2
    "I watch him warily as Nikki steps forward."
    show shou ner at l2
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_035.ogg"
    sf "Don't mind him. I'm Nikki."
    show nikki neu at r2
    show shou smi at l2
    voice "audio/voice/E3/D2/S1/shou/9.ogg"
    ss "I'm Shou and this is Mayu."
    
    if E2MAS4_Completed == 0:
        show mayu dis at l3
        "He glances at Mayu who has been standing in silence, then balks at the pout on her face."
        show shou ske at l2
        voice "audio/voice/E3/D2/S1/shou/10.ogg"
        ss "What's wrong?"
        show storm:
            xoffset 30
            yoffset 135
            xzoom .75
            yzoom .75
        show shou ske behind storm
        "She sighs."
        voice "audio/voice/E3/D2/S1/mayu/Mayu-02.ogg"
        ma "Nothing."
        show shou hap at l2
        voice "audio/voice/E3/D2/S1/shou/11.ogg"
        ss "Did you want to introduce yourself? Sorry about that."
        show mayu thi at l3
        "She sighs again."
        show shou neu at l2
        voice "audio/voice/E3/D2/S1/mayu/Mayu-03.ogg"
        ma "No, that's not it."
        show shou thi at l2
        "Shou scratches the back of his head."
        voice "audio/voice/E3/D2/S1/shou/12.ogg"
        ss "Huh, then what is it?"
        show mayu dis at l3
        "She continues to pout."
        voice "audio/voice/E3/D2/S1/mayu/Mayu-04.ogg"
        ma "It's nothing!"
        show nikki smi at r2
        "Nikki leans over to me and whispers."
        show nikki mis at r2
        voice "audio/voice/E3/D2/S1/nikki/Nikki_2_036.ogg"
        sf "They make an adorable couple!"
        show mayu neu at l3
        "I blink."
        pf "A couple?"
        show nikki neu at r2
        show shou cur at l2
        "Shou glances back at us."
        show shou smi at l2
        voice "audio/voice/E3/D2/S1/shou/13.ogg"
        ss "Us? Haha! No, no, we're just friends!"
        show mayu ner at l3
        "Mayu sighs again."
        voice "audio/voice/E3/D2/S1/mayu/Mayu-05.ogg"
        ma "Yeah… just friends…"
        show nikki smi at r2
        "Nikki leans over and whispers again."
        show nikki mis at r2
        voice "audio/voice/E3/D2/S1/nikki/Nikki_2_037.ogg"
        sf "He's so clueless!"
        show nikki smi at r2
        "Then she hits my arm."
        pf "Hey!"
        show nikki dis at r2
        voice "audio/voice/E3/D2/S1/nikki/Nikki_2_038.ogg"
        sf "Also, you weren't supposed to say that so loudly! What's the point of whispering if you're just going to blurt it out?"
        "I rub at the sore spot."
        pf "When did you get so strong?"
        
    else:
        show mayu smi
        voice "audio/voice/E3/D2/S1/mayu/Mayu-06.ogg"
        ma "Hi."
        "She smiles and gives a short wave."
        show nikki hap
        voice "audio/voice/E3/D2/S1/nikki/Nikki_2_039.ogg"
        sf "Hey!"
        
    stop music fadeout 3
    
    scene bg vacation beach day with dissolve:
        xzoom 1
        yzoom 1
        xalign 0.5
        yalign 0.8
        
    play music "audio/music/A Bad Feeling (GAME VERSION).ogg" fadein 5
    "Suddenly, we hear a shout in the distance. Following the source of the sound, I glance over and see Kaori hovering over a cowering man. He has his hands up defensively. Kaori snatches a camera out of his hands, fidgets with it, and throws it back at him. The man scoops up the camera, stumbles to his feet, and runs away."
    
    show nikki cur at r2:
        xoffset 50
        yoffset 35
        xzoom 0.75
        yzoom 0.75
    show mayu neu at l3:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show shou neu at l2 behind mayu:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    with dissolve
    
    "As the man flees, Kaori walks towards the water before chucking something into the waves. {w}We stare dumbfounded, watching the scene unfold."
    show shou ske at l2
    "Kaori spots us as she turns away from the water and stomps towards us. I can practically see the steam rising out of her ears. {w}Shou sighs."
    show shou thi at l2
    voice "audio/voice/E3/D2/S1/shou/14.ogg"
    ss "Well, it was nice knowing you guys…"
    show mayu ner at l3
    "Mayu nods."
    show nikki ner at r2
    stop music fadeout 5
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_040.ogg"
    sf "Aren't you overreacting a little?"
    show nikki ner at r2:
        xzoom 0.75
    "Nikki's voice wavers as Kaori approaches, betraying her confidence."
    show kaori ann at r3:
        xoffset 200
        xzoom -0.75
        yzoom 0.75
    show mayu neu at l3
    show shou neu at l2
    with dissolve
    pf "Hey Kaori…"
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
    show vein:
        xoffset 1550
        yoffset 110
        xzoom .5
        yzoom .5
    voice "audio/voice/E3/D2/S1/kaori/e3d2_Kao_01.ogg"
    ki "Can you believe that guy?"
    "Her voice trembles from anger."
    pf "What happened?"
    show kaori ang at r3
    show mayu ner at l3
    show shou ner at l2
    voice "audio/voice/E3/D2/S1/kaori/e3d2_Kao_02.ogg"
    ki "That {i}pervert{/i} was taking pictures of younger girls! I made him promise never to do it again, then took out his memory card and threw it into the ocean for good measure."
    show nikki cur at r2
    show kaori ann at r3
    "Nikki eyes Kaori with wonder, then elbows me."
    show nikki dis at r2
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_041.ogg"
    sf "Wow, she's not scary at all! At least now like you described her..."
    show kaori dis at r3
    "Kaori whirls on me, a fierce scowl plastered on her face. When she notices Nikki, her expression softens to one of curiosity."
    show question:
        xoffset 1550
        yoffset 110
        xzoom .5
        yzoom .5
    show kaori cur at r3
    show mayu neu at l3
    show shou neu at l2
    voice "audio/voice/E3/D2/S1/kaori/e3d2_Kao_03.ogg"
    ki "Who are you?"
    show nikki hap at r2
    "Nikki beams."
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_042.ogg"
    sf "Oh, I'm Nikki."
    show kaori neu at r3
    "Kaori continues to stare until Nikki points to me."
    show nikki smi at r2
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_043.ogg"
    sf "His sister."
    show kaori ske at r3
    "Kaori raises an eyebrow."
    voice "audio/voice/E3/D2/S1/kaori/e3d2_Kao_04.ogg"
    ki "Really? Wow, you're lucky you two look nothing alike."
    show nikki neu at r2
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_044.ogg"
    sf "Thanks."
    pf "Thanks."
    show kaori neu at r3
    show mayu cur at l3
    show nikki cur at r2
    show shou smi at l2
    "We answer simultaneously."
    "Nikki and I blink at each other in surprise, then speak at the same time."
    show nikki ske at r2
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_045.ogg"
    sf "What's that supposed to mean?"
    pf "What's that supposed to mean?"
    show mayu smi at l3
    "Shou laughs."
    show shou mis at l2
    voice "audio/voice/E3/D2/S1/shou/15.ogg"
    ss "I'm pretty sure Kaori meant Nikki's lucky she doesn't look like you."
    pf "Thanks for having my back, bro."
    show shou hap at l2
    voice "audio/voice/E3/D2/S1/shou/16.ogg"
    ss "No problem, broseph!"
    show nikki smi at r2
    "Nikki giggles."
    show note:
        xoffset 1250
        yoffset 195
        xzoom .5
        yzoom .5
    voice "audio/voice/E3/D2/S1/nikki/Nikki_2_046.ogg"
    sf "I like Kaori!"
    show kaori cur b1 at r3 with dissolve
    "Kaori stammers out her reply as her cheeks tinge pink."
    show kaori smi b1 at r3
    show shou smi at l2
    voice "audio/voice/E3/D2/S1/kaori/e3d2_Kao_05.ogg"
    ki "Oh! Ah, thanks."
    
    jump E3D2S2

