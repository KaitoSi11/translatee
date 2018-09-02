label E1D3S1:
    
    
    $renpy.pause(1)
    #morning sounds
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1)
    #black background fade in/out 
    scene bg homekaito myroom blurry with Dissolve(2.5)
    "The sun shines through my curtains and across my face."
    scene black with fade
    "I keep my eyes shut and turn over in my bed trying to force myself back asleep, but the more I try to return to sleep, the more awake I become."
    $renpy.pause(1)
    "What time is it?"
    scene bg homekaito myroom blurry with fade
    "My clock flashes \"6:30\". I still have another half an hour before my alarm goes off. {w}I should get back to sleep."
    scene black with fade
    "I curl deeper into my blankets but soon get bored. The only time I ever naturally wake up this early is when I have jet lag. I'm not sure if this is a blessing or a curse. {w}I guess I may as well get ready."
    scene bg homekaito myroom day with fade
    "I quickly change into my uniform and head downstairs…"
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
    scene black with fade
    $renpy.pause(3)
    #bg change
    scene bg homekaito main day with fade
    "... to an empty kitchen."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    "It's weird being the first one up. Usually Nikki is doing her thing in the kitchen."
    "I'll catch up on some reading while I wait for her. She should be up soon anyway."
    play sound "audio/sfx/Technology/Payment Beep Success.ogg"
    "I pull up the news app on my phone. The front page doesn't have anything too interesting... {w}until I spot an article on Aludian Enterprises."
    
    "{i}Aludian Enterprises has officially announced their intentions to sponsor an up-and-coming team in the coming \"War Games\". {w}The rapidly expanding R&D company is gaining a lot of attention in the field of cenorobotics, and they're putting pressure on established innovators, such as Vector Industries and Paragon Weaponry.{/i}"
    "{i}Much of their success can be attributed to CEO Donnie Roos, who was a top graduate in the Pilot Program at ACE Academy, and a visionary when it comes to modern and functional designs for GEAR.{/i}"
    
    "Hm, I don't think I've heard of these guys before. Must be a local company who hasn't quite expanded to the States yet. Sounds like they're making a name for themselves, though."
    "The time on my phone reads \"6:57\". I listen for any signs of life upstairs, but the house is still."
    play sound "audio/sfx/Human/Stomach Grumble.ogg"
    #stomach grumble
    "I better grab something to eat before I need to go. It doesn't seem like Nikki's coming down anytime soon."
    play sound "audio/sfx/Technology/Payment Beep Success.ogg"
    "My phone flashes to the next article--a headline on Dasshu. {w}That should be good!"
    play sound "audio/sfx/Technology/Phone Projection.ogg"
    "I push the button shaped like a film projector on the bottom of the page, and the text projects on the nearest surface. Then I place my phone in a dock on the table so the text shines on the kitchen table."
    "I grab a couple of slices of bread and stick them in the toaster. As I wait for my toast to finish, I sit at the table and read the article."
    
    "{i}Khanaku Dishtaru, CEO of Dasshu, made an unscheduled appearance at the memorial service yesterday for Yuudai Misaki. A year ago, the community was shocked by the unexpected death of ACE Academy's most promising pilot. {w}The family was honored that the mighty mogul took the time to show his respects to their son, and concurrently, postponed the unveiling of Dasshu's new line of energy drinks. {w}The introduction has been rescheduled to take place next week--{/i}"
    stop music fadeout 3
    voice "audio/voice/E1/D3/S1/Nikki/1.ogg"
    sf "What're you reading?"
    show nikki neu at cc with dissolve
    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 1
    menu:
        "AHHH!":
            pf "Ahh!"
            show nikki cur at cc with dissolve
            "I jump in surprise and nearly fall off my chair as I try to turn towards her. She looks at me strangely."
            show nikki ske at cc
            show question:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/2.ogg"
            sf "Geez, what's your problem?"
            pf "You scared me!"
            show nikki mis at cc
            show shiny:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/3.ogg"
            sf "Why? Were you looking at hentai or something?"
            pf "What? No! Of course not!"
            show nikki smi at cc
            "She laughs at my horrified expression and walks past me."
            show nikki mis at cc
            voice "audio/voice/E1/D3/S1/Nikki/4.ogg"
            sf "I know! I Know! You're reading the news; I can see it on the table. Booooring! You know that makes you officially old, right? Only old people read the news for fun."
    
        "How can your feet make no sound?":
            pf "Geez, Nikki! You startled me. Make some noise when you walk!"
            show nikki smi at cc
            "She laughs."
            voice "audio/voice/E1/D3/S1/Nikki/5.ogg"
            sf "But that would totally ruin my chances of surprising you."
            pf "No more of that please. I'm going to have to tie some bells around your neck so I can hear you coming… like people do for cats."
            show nikki cur at cc
            voice "audio/voice/E1/D3/S1/Nikki/6.ogg"
            sf "Are you comparing me to a cat?"
            pf "That's a thing, isn't it?"
            show nikki ske at cc
            voice "audio/voice/E1/D3/S1/Nikki/7.ogg"
            sf "Umm?"
            pf "You know, like neko girls--"
            show nikki dis at cc
            show drop:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/8.ogg"
            sf "Oh my god! Stop it, you perv!"
            pf "What?"
            show nikki ann at cc
            voice "audio/voice/E1/D3/S1/Nikki/9.ogg"
            sf "Yea... I don't need to know about your weird little fantasies!"
            pf "That's not--"
            show nikki dis at cc
            voice "audio/voice/E1/D3/S1/Nikki/10.ogg"
            sf "So you don't think a girl would look super cute with cat ears?"
            pf "... No…"
            "But now that I'm imagining it… I definitely wouldn't say no."
            show nikki mis at cc
            voice "audio/voice/E1/D3/S1/Nikki/11.ogg"
            sf "Wipe that drool off your face."
            "I instinctively wipe at my chin, but nothing's there."
            show nikki smi at cc
            "Nikki just laughs and heads past me."
    
        "Nothing!":
            show nikki cur at cc
            "I instinctively turn off the projection. She tries to peek over my shoulder, but I darken the screen. The last thing I need so early in the morning is Nikki making fun of me for reading the news."
            show nikki ske at cc with dissolve
            show question:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/12.ogg"
            sf "Why are you being so weird?"
            pf "I'm not!"
            show nikki sad at cc
            voice "audio/voice/E1/D3/S1/Nikki/13.ogg"
            sf "Then why won't you show me?"
            pf "It's not interesting. Trust me, you won't like it."
            show nikki win b1 at cc with dissolve
            show shoBlush:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/14.ogg"
            sf "Ew!"
            pf "What?"
            show nikki dis b1 at cc
            voice "audio/voice/E1/D3/S1/Nikki/15.ogg"
            sf "Did I just catch you watching hentai?"
            pf "No!"
            show nikki dis b1 at cc
            voice "audio/voice/E1/D3/S1/Nikki/16.ogg"
            sf "This is the kitchen. We {i}eat{/i} here--"
            pf "It's not hentai! Look!"
            "I turn my phone back on and try to show her the article, but she covers her eyes."
            show nikki win b1 at cc
            show drop:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/17.ogg"
            sf "Stop! I don't want to see it!"
            pf "Look! It's not hentai! Just look!"
            "I shove the phone in her face, but she twists away from me."
            voice "audio/voice/E1/D3/S1/Nikki/18.ogg"
            sf "Nooo!"
            pf "Look, damnit, look!"
            show nikki sad b1 at cc with dissolve
            "She doesn't close her eyes fast enough and catches a peek at my article."
            show nikki smi at cc with dissolve
            "Then she ceases her struggling and begins laughing instead."
            pf "Huh?"
            show nikki mis at cc
            voice "audio/voice/E1/D3/S1/Nikki/19.ogg"
            sf "I knew it wasn't hentai, you dummy."
            pf "Then why--."
            show nikki hap at cc
            show note:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/20.ogg"
            sf "Because that reaction, priceless!"
            show nikki smi at cc
            "She continues laughing as she heads past me."
            "Little sisters…"
            
    stop music fadeout 3
    $renpy.pause(1)
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    show nikki cur at cc with dissolve
    "Nikki glances at my toast, which had popped up while we were talking."
    voice "audio/voice/E1/D3/S1/Nikki/21.ogg"
    sf "Your toast is burned."
    pf "What!"
    "I leap out of my chair and stand beside her."
    pf "It's not burned."
    show nikki ner at cc
    "She flips it over to reveal a dark side of charcoal."
    pf "Oh…"
    show nikki smi at cc
    voice "audio/voice/E1/D3/S1/Nikki/22.ogg"
    sf "You're so hopeless! How did you survive in college without me?"
    pf "I ate in the cafeteria."
    show nikki mis at cc
    voice "audio/voice/E1/D3/S1/Nikki/23.ogg"
    sf "That explains it."
    "She throws away the toast and pulls out two yogurts from the fridge."
    show nikki neu at cc
    voice "audio/voice/E1/D3/S1/Nikki/24.ogg"
    sf "Well, since you botched breakfast, we'll have to make do with a quick snack if we don't want to be late."
    "I accept the yogurt she hands me, and we both finish them in record time. {w}Then we grab our things and head out the door."
    show nikki hap at cc with dissolve
    show exclamation:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S1/Nikki/25.ogg"
    sf "Are you able to give me a ride today? The bus yesterday was so crowded!"  
    
    if (E1D2S7_BullyFightWin == 1):
        $ E1D3S1_BikeImpounded = 1
        "I look a bit sheepish."
        pf "Sorry Nikki, my bike is still at school." 
        show nikki cur at cc
        voice "audio/voice/E1/D3/S1/Nikki/26.ogg"
        sf "Why?" 
        pf  "Well… because it was impounded." 
        show nikki ske at cc
        "Nikki raises an eyebrow."
        show question:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S1/Nikki/27.ogg"
        sf "... What did you do?" 
        "I'm not going to tell her about the fight so I think up a quick excuse." 
        pf "Uh… I just parked it in the wrong place; nothing big. I'll get the bike back today. The office was closed by the time I tried to grab it." 
        show nikki mis at cc
        "Nikki snorts."
        voice "audio/voice/E1/D3/S1/Nikki/28.ogg"
        sf "Why am I not surprised you managed to get in trouble on your first day?"
        "If she only knew…"
        pf "Heh, you know me…"
        show nikki neu at cc
        voice "audio/voice/E1/D3/S1/Nikki/29.ogg"
        sf "Okay, guess I'll see you tonight then."
        hide nikki with dissolve
        "She waves and heads towards the bus stop. I do the same."
        jump E1D3S2
        
    elif (E1D2S5_gotbikepass == 1):
        menu: 
            "You just want to show off your {i}pilot{/i} big brother. Of course I'll take you!":
                $ E1D3S1_BikeDrove = 1
                "I flash her a confident grin." 
                pf "Hoping to make friends by having a cool big brother?"
                show nikki thi at cc with dissolve
                "Nikki rolls her eyes."
                show drop:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S1/Nikki/30.ogg"
                sf "More like I don't want to be squished between the smelly old lady and fat guy again." 
                pf "Mhm… I'm sure that's it."
                show nikki ske at cc
                voice "audio/voice/E1/D3/S1/Nikki/31.ogg"
                sf "If you're going to be like this then I'm just going to take the bus…"
                stop music fadeout 3
                "She turns away and I laugh."
                play music "audio/music/Open Road (GAME VERSION).ogg" fadein 1 fadeout 1
                show nikki cur at cc
                pf "I'm kidding, Nikki. C'mon, I'll take you to school." 
                play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 1 fadeout 1
                scene black with fade
                $renpy.pause(2.5)
                play sound "audio/sfx/Vehicles/Bike Screech.ogg" fadein 1 fadeout 1
                jump E1D3S3
    
            "Hell no, woman! My bike is for the ladies.": 
                $ E1D3S1_BikeDrove = 1
                pf "No way! I don't want people to see me riding around with my kid sister."
                show nikki ske at cc
                show question:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S1/Nikki/32.ogg"
                sf "Kid? Are you serious?" 
                pf "Dead serious."
                show nikki dis at cc
                "I pat her on the head like a child." 
                pf "You still need to learn your way around the city. It wouldn't do you any good for me to drive you around."
                show nikki ann at cc
                voice "audio/voice/E1/D3/S1/Nikki/33.ogg"
                sf "Oh please, like that's the reason. You're just being a jerk." 
    
                menu: 
                    "Maybe I should give her a ride…":
                        stop music fadeout 3
                        pf "Okay, okay. I'll take you."
                        play music "audio/music/Open Road (GAME VERSION).ogg" fadein 1 fadeout 1
                        show nikki hap at cc
                        "Nikki smiles."
                        show note:
                            xoffset 720
                            yoffset 160
                            xzoom .75
                            yzoom .75
                        voice "audio/voice/E1/D3/S1/Nikki/34.ogg"
                        sf "Thank you!" 
                        pf "Am I still a jerk?" 
                        show nikki thi at cc with dissolve
                        show nikki neu at cc with dissolve
                        voice "audio/voice/E1/D3/S1/Nikki/35.ogg"
                        sf "Hmm… I guess not. But don't hold your breath. You'll do something else before the day is done."
                        pf "Great…" 
                        play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 1 fadeout 1
                        scene black with fade
                        $renpy.pause(2.5)
                        play sound "audio/sfx/Vehicles/Bike Screech.ogg" fadein 1 fadeout 1
                        jump E1D3S3
    
                    "Screw it! I'm a jerk!":
                        "I wink at her and head for my bike."
                        pf "Have a good day at school!" 
                        hide nikki with dissolve
                        "Nikki grumbles her response as she trudges towards the bus stop."
                        "Now I can impress the ladies with my slick bike." 
                        jump E1D3S4
        
                
            "I'm actually taking the bus.": 
                $ E1D3S1_BusRide = 1
                pf "I was going to catch the bus again today."
                show nikki ske at cc
                "Nikki frowns, hands planted on her hips."
                show question:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S1/Nikki/36.ogg"
                sf "Why? Don't you have your bike?"
                pf "Yeah, but I don't know if I want to take it today."
                show nikki wor at cc with dissolve
                "Suddenly, her hand is on my forehead."
                pf "Uhh… what are you doing?"
                show nikki sad at cc
                voice "audio/voice/E1/D3/S1/Nikki/37.ogg"
                sf "Checking if you're ill. You {i}always{/i} prefer to take your bike."
                show nikki cur at cc with dissolve
                "I remove her hand from my face."
                pf "I'm fine. I just think it would be good to get to know the city."
                show nikki ske at cc
                "Nikki just stares at me with the most skeptical look I've ever seen."
    
                if (E1D2S2_talkwithyuunayes == 1):
                    show nikki hap at cc with dissolve
                    "Then her face lights up in a playful smile."
                    voice "audio/voice/E1/D3/S1/Nikki/38.ogg"
                    sf "You're hoping to see that girl again, aren't you?" 
                    pf "No, no. I really think the bus is a good idea." 
                    show nikki smi at cc
                    show shiny:
                        xoffset 720
                        yoffset 160
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D3/S1/Nikki/39.ogg"
                    sf "Suuuuure you do. Whatever. Anyways, I'll see you tonight I guess."
                    hide nikki with dissolve
                    "I try to protest, but she already left for her bus stop."
                    jump E1D3S2
    
                else:
                    show nikki thi at cc
                    "Then she shrugs."
                    voice "audio/voice/E1/D3/S1/Nikki/40.ogg"
                    sf "Fine, if you don't want to tell me then I don't want to know. But I guess that means your bike is up for grabs, right?"
                    pf "What?"
                    show nikki mis at cc
                    voice "audio/voice/E1/D3/S1/Nikki/41.ogg"
                    sf "Well, you're not going to take it… So, does that mean I can?"
                    $renpy.pause(1)
                    "My heart stops."
                    pf "What?!"
                    show nikki smi at cc
                    "Nikki bursts out laughing."
                    show note:
                        xoffset 720
                        yoffset 160
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D3/S1/Nikki/42.ogg"
                    sf "You should have seen your face! Anyway, have a good day. I'll see you later tonight?"
                    hide nikki with dissolve
                    "She turns and heads for her bus stop. Once the shock wears off, I head for mine." 
                    jump E1D3S2
    
    
    else:
        $ E1D3S1_BusRide = 1
        pf "Sorry Nikki, I'm not taking my bike today. I don't have a parking pass yet."
        show nikki wor at cc
        voice "audio/voice/E1/D3/S1/Nikki/43.ogg"
        sf "Ohhh, how long will it take before you get one?"
        pf "I'm not sure, but hopefully soon."
        show nikki mis at cc
        voice "audio/voice/E1/D3/S1/Nikki/44.ogg"
        sf "Well, for the sake of your sanity, I hope it's not too long!"
        pf "Thanks… I think?"
        show nikki smi at cc
        "Nikki laughs."
        voice "audio/voice/E1/D3/S1/Nikki/45.ogg"
        sf "I'll see you later, 'kay?"
        pf "Yeah, see you."
        hide nikki with dissolve
        "She waves and heads for her bus stop while I head for mine."
        jump E1D3S2

