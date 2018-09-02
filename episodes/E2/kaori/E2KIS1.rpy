#
label E2KIS1:
    
    $ kaoHairF = "default"
    $ kaoHairB = "default"
    $ kaoOut = "sUniform"
    
    # Event 1 - Afternoon Choice
    
    #sfx stomach growl
    play sound "audio/sfx/Human/Stomach Grumble.ogg"
    "My stomach complains loudly for food. Hopefully nobody else heard that!"
    
    if freeTime == "D2Afternoon":
        "A tough work-out always builds up an appetite."
    
    else:
        "At least I have plenty of time to grab lunch before my next class."
    
    "There's a cafeteria on campus which I've eaten at a couple times. The food is cheap and surprisingly good--way better than the cafeteria food in CINY--but the options are limited. I've heard the Pilot's Lounge has some decent options, and their daily specials incorporate cuisine from other cultures. It might be worth a look."
    
    "I navigate to the Lounge."
    
    #Black Screen
    stop ambient fadeout 3
    scene black with fade
    play ambient "audio/ambience/Pilot Lounge.ogg" fadein 3
    scene bg campus lounge day with fade
    
    "Luckily there isn't a line. I hope that's because I beat the lunch rush and not because the food is bad. {w}Pushing those thoughts aside, I walk up to the bar."
    show receptionist extra at cc with dissolve
    voice "audio/voice/E2/missing/bartender/bartender kaori arc_01.ogg"
    barm "Hello, what'll you have?"
    "Hm… {w}I study the limited menu on the wall. Behind the bartender is a chalkboard with the daily special written down: cheeseburger with fries."
    
    $ E2KIS1_Food = 0
    
    menu:
        "Something healthy would be good.":
            $ E2KIS1_Food = 1
            "I'm not seeing what I want…"
            pf "Hi. What healthy options do you have?"
            voice "audio/voice/E2/missing/bartender/bartender kaori arc_02.ogg"
            barm "Healthy? I can get you a protein bar."
            pf "Thanks, but I meant for an actual meal. Do you have a salad?"
            "The bartender raises an eyebrow."
            voice "audio/voice/E2/missing/bartender/bartender kaori arc_03.ogg"
            barm "Sure, it's called the burger salad. You get a burger without the buns or pattie."
            pf "..."
            "He doesn't have to be a jerk about it."
            voice "audio/voice/E2/missing/bartender/bartender kaori arc_04.ogg"
            barm "Take the hint, kid."
            "I consider going somewhere else, when my stomach growls again in protest."
            pf "Fine, I'll just have the special."
    
        "Hell yeah! Burger and fries.":
            $ E2KIS1_Food = -1
            "It must be my lucky day! I've been craving a good burger ever since I landed in Japan."
            pf "I'll have the burger with fries."
    
        "I don't have a preference.":
            "I don't care what I eat as long as there is food in my belly."
            pf "I'll just have whatever the special is."
    
    voice "audio/voice/E2/missing/bartender/bartender kaori arc_05.ogg"
    barm "House special burger and fries coming up."
    voice "audio/voice/E2/missing/bartender/bartender kaori arc_06.ogg"
    barm "That'll be 8.73 credits."
    play sound "audio/sfx/Technology/Payment Beep Success.ogg"
    $renpy.pause(1)
    hide receptionist with dissolve
    "After paying, I move over to the side and wait for my lunch."
    "Within a few minutes, he slides over a tray with a juicy burger and a mound of fries."
    
    if E2KIS1_Food ==1:
        "That looks like a heart attack just waiting to happen. Oh well, I suppose I'll just treat today as my cheat day."
    
    else:
        "I can't wait to start eating this beast of a burger!"
    
    "Picking up my tray, I scan the pilot's lounge for an empty table. Most are occupied by single students focused on their own food or studies."
    "As I'm debating whether or not to join a random student, I spot a girl with reddish-orange hair sitting alone. {w}It's Kaori!"
    "I breathe out a sigh of relief and make my way over to her."
    
    show kaori neu at cc with dissolve
    pf "Hey."
    show kaori cur at cc
    show exclamation:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    "She looks up at me."
    voice "audio/voice/E2/Free/KI/1.ogg"
    ki "Oh, hi."
    pf "Mind if I sit here?"
    show kaori neu at cc
    "She shakes her head."
    pf "Thanks."
    "I place my tray next to her bento and sit down. Kaori refocuses on her meal and eats in silence."
    $renpy.pause(1)
    show dots:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    $renpy.pause(1)
    "..."
    "This is pretty awkward."
    
    menu:
        "Speak up.":
            if freeTime == "D2Afternoon":
                if MCStory == 1:
                    pf "So... do you think Shou will be okay?"
                    show kaori ske at cc
                    show question:
                        xoffset 720
                        yoffset 110
                        xzoom .75
                        yzoom .75
                    "She raises an eyebrow."
                    voice "audio/voice/E2/Free/KI/2.ogg"
                    ki "Huh?"
                    pf "He looked like he was dying today."
                    show kaori thi at cc
                    "Kaori shrugs."
                    voice "audio/voice/E2/Free/KI/3.ogg"
                    ki "Maybe if he watched what he ate he would be more fit."
                    pf "Mm."
                    show kaori neu at cc
    
            else:
                pf "So... How are things?"
                voice "audio/voice/E2/Free/KI/4.ogg"
                ki "Good."
                "She doesn't even bother looking at me."
                pf "Um, and what do you think about the weather today?"
                voice "audio/voice/E2/Free/KI/5.ogg"
                ki "Adequate."
                "This is seriously like pulling teeth. I shouldn't be surprised though, It's Kaori after all. Small talk is not her forte."
    
        "Stay quiet.":
            "Whatever, it's Kaori. She'll probably freak out if I try to talk to her while she's eating.{w} Something like \"stop distracting me while i'm busy! Idiot.\"."
            
    "I pick up a ketchup packet and squeeze the contents over my fries."
    show kaori cur at cc
    voice "audio/voice/E2/Free/KI/6.ogg"
    ki "You're really eating {i}that{/i}?"
    
    if freeTime == "D2Afternoon":
        show kaori ske at cc
        voice "audio/voice/E2/Free/KI/7.ogg"
        ki "Especially after Phy Ed?"
    
    pf "Huh?"
    show kaori neu at cc
    "Kaori has finally looked up from her food and examines my meal."
    voice "audio/voice/E2/Free/KI/8.ogg"
    ki "Burgers are very unhealthy. They are full of fat and very high in calories."
    show kaori thi at cc
    ### VOICE - line is misread, "and the average meal holds the amount of sodium and average person needs"
    voice "audio/voice/E2/Free/KI/9.ogg"
    ki "The fries are even worse! Those are just empty carbs, and the average meal holds twice the amount of sodium an average person needs in a day."
    
    menu:
        "I wanted something healthy." if E2KIS1_Food == 1:
            pf "This wasn't my first pick, but I doubt it's {i}that{/i} bad."
    
        "It tastes delicious!":
            pf "That's what makes it tastes so good!"
    
        "You're exaggerating.":
            pf "You make it sound like I will drop dead as soon as I take a bite."
            
    show kaori dis at cc
    show storm:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    "Kaori leans back in disappointment and shrugs."
    voice "audio/voice/E2/Free/KI/10.ogg"
    ki "Whatever, it's your choice."
    "I glance at her bento. It has an assortment of simple maki rolls."
    
    if E2KIS1_Food == 1:
        "Even though I said I wanted something healthier, I wouldn't be excited to eat what she's having."
    
    else:
        "I'm just glad I'm eating this instead of that."
    
    pf "Well, sometimes it's nice to eat something tasty for a change."
    
    #transition into CG
    $ persistent.gpix[25][0] = 1
    $ persistent.gpix[26][0] = 1
    $ persistent.gpix[27][0] = 1
    $ persistent.gpix[28][0] = 1
    scene cg kaori force eating1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with Dissolve(1.5)
    
    $ renpy.pause(.33)
    "She frowns in irritation."
    voice "audio/voice/E2/Free/KI/11.ogg"
    ki "What makes you think my bento isn't tasty?!"
    "I take another look at it, then smirk."
    pf "You don't need to get so defensive. I'm sure it's healthy, but that thing barely looks seasone--"
    stop music fadeout 1.0
    play sound "audio/sfx/Human/Poke_1.ogg"
    scene cg kaori force eating2 at Zoom((1920, 1080), (0, 0, 3840, 2160), (170, 180, 1920, 1080), 0.3)
    $ renpy.pause(.5)
    pf "--Oouuf!"
    scene cg kaori force eating2 at Zoom((1920, 1080), (170, 180, 1920, 1080), (0, 0, 3840, 2160), 0.5)
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 10
    $ renpy.pause(1.0)
    "Kaori shoves a maki roll into my mouth while I'm mid-sentence!"
    voice "audio/voice/E2/Free/KI/12.ogg"
    ki "Don't judge it until you've tried it!"
    "..."
    "....."
    "!!"
    "Wow, this is surprisingly delicious!"
    "It's light with simple ingredients, but each bite is still packed with flavour."
    scene cg kaori force eating3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    "Kaori quickly retracts her chopsticks. Once she realises what she's done, her cheeks flush."
    
    menu:
        "That actually was pretty good.":
            pf "Hey, you have a talent for cooking."
            "Her cheeks turn crimson. She tries to hide her face in her bento while assuming an air of nonchalance as she resumes eating."
            voice "audio/voice/E2/Free/KI/13.ogg"
            ki "Thanks, or whatever."
            "She's still pretty awkward when it comes to compliments, but something about that is kind of cute."
    
        "You win this time.":
            pf "I will admit, that was not bad."
            "She waves a hand dismissively."
            voice "audio/voice/E2/Free/KI/14.ogg"
            ki "Next time, don't jump to conclusions."
            "I grudgingly admit that Kaori is right. Although I would have never guessed she'd be such a talented cook."
    
        "Huh, I guess I was wrong.":
            pf "I take it back. That was pretty tasty."
            "Kaori nods, satisfied."
            voice "audio/voice/E2/Free/KI/15.ogg"
            ki "Maybe next time you won't be so dismissive of my advice."
            "I figured Kaori liked to eat healthy, but I hadn't realised she cared about taste as well as nutrition."
    
        "Give me another piece!":
            "I open my mouth wide."
            pf "Aaaaaa~"
            
            ### NOTE Points - "if high points with Koari:"
            # temporarily set to 0
            if kaoromance > 0:
                scene cg kaori force eating4 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
                "Kaori's face reddens even more."
                voice "audio/voice/E2/Free/KI/16.ogg"
                ki "W-What are you doing?"
                pf "Feed me again!"
                voice "audio/voice/E2/Free/KI/17.ogg"
                ki "What do you mean {i}again{/i}? I wasn't feeding you!"
                pf "Don't be so shy, Kaori. Come on!"
                pf "Aaaaaaaaaaaaaa~~"
                "As I lean my head closer, she scoots to the far end of the booth."
                voice "audio/voice/E2/Free/KI/18.ogg"
                ki "S-Stop acting weird!"
                "Her voice cracks with embarrassment as she buries her face in her bento box."
            
            else:
                scene cg kaori force eating4 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
                "She slugs me on the shoulder."
                voice "audio/voice/E2/Free/KI/19.ogg"
                ki "Stop being an idiot."
                "I rub my fresh bruise."
                pf "Aww, so mean."
            
    $renpy.pause(1)
    scene black with fade
    stop music fadeout 5
    $renpy.pause(1)
    "We end up finishing our meals in silence, but I'm glad I was able to learn a little bit more about Kaori."
    $ E2KIS1_Completed = 1
    stop ambient fadeout 3
    $renpy.pause(1)
    #end

