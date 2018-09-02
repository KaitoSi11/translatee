#
label E2SSS2:
    
    #Event 2- Afternoon Choice
    $ shoOut = "sUniform"
    
    #bg School
    "Maybe Shou’s down to hang for a bit."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(2.5)
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    "I call him, but the phone rings for a while before it connects."
    pf "Hey, Shou--"
    ### VOICE - these lines currently aren't mixed for the phone sound
    voice "audio/voice/E2/Free/SS//S2/fbro1/1.ogg"
    fbro1 "Hello, you have reached 1-800-GET-SWOL. How may I help you today?"
    
    menu: 
        "Say what now?":
            pf "What?"
            voice "audio/voice/E2/Free/SS//S2/fbro1/2.ogg"
            fbro1 "You've reached the SWOLL hot-line. Please address your questions or concerns after the beep."
            "...How do I even begin to respond?"
            ### VOICE - no line recorded for this?
            fbro1 "Beeeeep."
            pf "This is Shou's number, right?"
            voice "audio/voice/E2/Free/SS//S2/fbro1/3.ogg"
            fbro1 "This is his number, yep."
            pf "Is he there? Can you put him on?"
            voice "audio/voice/E2/Free/SS//S2/fbro1/4.ogg"
            fbro1 "Shou's not here, bro. Sorry."
            pf "Any idea when he'd be back?"
            voice "audio/voice/E2/Free/SS//S2/fbro1/5.ogg"
            fbro1 "Probably in a few-- Oh speak of the bro."
    
        "Yeah, how much for an order of swoll?":
            pf "I’d like to make five orders of swoll, please."
            voice "audio/voice/E2/Free/SS//S2/fbro1/6.ogg"
            fbro1 "Thank you for your patronage. That will be one 400lbs deadlift, ten reps of 50lbs curls, and a gallon of strawberry flavored whey."
            pf "You guys have really raised the prices since my last order."
            voice "audio/voice/E2/Free/SS//S2/fbro1/7.ogg"
            fbro1 "Sorry customerbro, the economy just isn't what it used to be."
            pf "I hear you, but as a loyal customer, I deserve a discount."
    
        "I’m looking for Shou.":
            pf "Who is this? Where's Shou?"
            voice "audio/voice/E2/Free/SS//S2/fbro1/8.ogg"
            fbro1 "Shou’s taking care of business in the bathroom, so he might take a while."
            pf "What?"
    
    "..."
    "I hear movement on the line."
    voice "audio/voice/E2/Free/SS/79.ogg"
    ss "Hey! Sorry about that. One of the guys picked up the phone while I was in the bathroom."
    pf "It's okay. {w}Do you have a class right now?"
    voice "audio/voice/E2/Free/SS/80.ogg"
    ss "Nope."
    pf "Let's do something."
    voice "audio/voice/E2/Free/SS/81.ogg"
    ss "Sure! You still on campus?"
    pf "Yeah, why?"
    voice "audio/voice/E2/Free/SS/82.ogg"
    ss "You should come over and meet the brosephs."
    pf "Sure, I'll be there in a few."
    
    #fade to Fraternity
    stop music fadeout 3
    scene black with fade
    stop ambient fadeout 3
    $renpy.pause(1)
    # pilot lounge ambient might work here
    play ambient "audio/ambience/Pilot Lounge.ogg" fadein 3
    scene bg campus dorm day with fade
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
    "Shou opens the door and I am assaulted by the stench of cheap sapporo."
    show shou mis at cc with dissolve
    voice "audio/voice/E2/Free/SS/83.ogg"
    ss "Welcome to mi casa!"
    pf "Your casa smells like beer and sweat."
    show shou smi at cc
    voice "audio/voice/E2/Free/SS/84.ogg"
    ss "That, my friend, is the scent of {i}men{/i}."
    
    menu:
        "I never knew!":
            pf "I guess having a sister means I never got this memo."
            show shou hap at cc
            "Shou grins."
            voice "audio/voice/E2/Free/SS/85.ogg"
            ss "Just stick with me and we'll have you bro-ing in no time!"
    
        "Is that what I smell like?":
            "I take a surreptitious whiff of myself."
            pf "Real men smell like soap. How else do you expect a lady to get close to you?"
            show exclamation:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            show shou sur at cc
            "Shou's eyes go wide."
            voice "audio/voice/E2/Free/SS/86.ogg"
            ss "So {i}that's{/i} what I've been doing wrong! I'm learning so much."
            show shou hap at cc
            "He grins."
    
        "No, that is just stink.":
            pf "Men who need a shower."
            show shou cur at cc
            "Shou sniff himself."
            show note:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            show shou hap at cc
            voice "audio/voice/E2/Free/SS/87.ogg"
            ss "Still fresh!"
            
    hide shou with dissolve
    "I follow Shou through the house when suddenly a ball flies at my face!"
    voice "audio/voice/E2/Free/SS/S2/fbro2/1.ogg"
    fbro2 "Bro watch out!"
    
    #QTE - IF timeout, jump "Just take the hit...":
    $ qtebase = 3
    $ qtetotal = qteath + qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E2SSS2_Freeze")
    
    menu:
        "{color=#00ff00}{b}Catch!{/b}{/color}" if MCStory == 1:
            $ renpy.hide_screen ("timer_scr")
            # sfx?
            "My arm shoots out and I catch the ball mid-air."
            voice "audio/voice/E2/Free/SS/S2/fbro2/2.ogg"
            fbro2 "Duuuuude, that was sick!"
            show bully3 extra at l3
            show bully2 extra at r3:
                xzoom -1
            with dissolve
            "A couple of Shou’s dormmates run up to me."
            fbro3 "Good reflexes, man!"
            show shou neu at cc with dissolve
    
        "Catch!" if MCStory != 1:
            $ renpy.hide_screen ("timer_scr")
            # sfx?
            "My arm shoots out and I catch ball mid-air."
            voice "audio/voice/E2/Free/SS/S2/fbro2/2.ogg"
            fbro2 "Duuuuude, that was sick!"
            show bully3 extra at l3
            show bully2 extra at r3:
                xzoom -1
            with dissolve
            "A couple of Shou’s dormmates run up to me."
            fbro3 "Good reflexes, man!"
            show shou neu at cc with dissolve
    
        "Fumble!":
            $ renpy.hide_screen ("timer_scr")
            # sfx? screen shake?
            "I reach out to grab the ball and my fingers brush against it. It rebounds off my chest before I catch it."
            show bully3 extra at l3
            show bully2 extra at r3:
                xzoom -1
            with dissolve
            voice "audio/voice/E2/Free/SS/S2/fbro2/3.ogg"
            fbro2 "Ayyy! You caught it, bro!"
            pf "Yeah, but just barely."
            show shou neu at cc with dissolve
    
        "Dodge!":
            $ renpy.hide_screen ("timer_scr")
            # sfx?
            "I duck out of the way as the ball crashes behind me."
            pf "Whew! Wha--"
            "The ball ricochets off the wall and comes hurtling towards me again. I intercept it before it can do any more damage."
            show shou cur at cc with dissolve
            voice "audio/voice/E2/Free/SS/88.ogg"
            ss "Wow, lucky."
            pf "No luck required."
            show bully3 extra at l3
            show bully2 extra at r3:
                xzoom -1
            with dissolve
    
        "Freeze...":
            label E2SSS2_Freeze:
                $ renpy.hide_screen ("timer_scr")
                # sfx? screen shake?
                "Before I know it, my head is throbbing."
                pf "Oof-- ow…"
                show bully3 extra at l3
                show bully2 extra at r3:
                    xzoom -1
                with dissolve
                voice "audio/voice/E2/Free/SS/S2/fbro2/4.ogg"
                fbro2 "Are you okay, bro?"
                fbro3 "Sorry man, protein hard at work."
                pf "Don’t worry about it… I’m fine… I think."
                voice "audio/voice/E2/Free/SS/S2/fbro2/5.ogg"
                fbro2 "You don’t look fine. Bro, do you even lift?"
                pf "Do I-- what?"
                fbro3 "If you got more gains on you then that ball would've just glanced off your muscles."
                pf "Right…"
                show shou neu at cc with dissolve
                
    voice "audio/voice/E2/Free/SS/S2/fbro2/6.ogg"
    fbro2 "Wait. Shou, isn’t this guy the pilot on your team?"
    show shou hap at cc
    voice "audio/voice/E2/Free/SS/89.ogg"
    ss "Yep, that’s right."
    fbro3 "Bro."
    voice "audio/voice/E2/Free/SS/S2/fbro2/7.ogg"
    fbro2 "Bro."
    show shou smi at cc
    
    #the next two are at the same time
    voice "audio/voice/E2/Free/SS/S2/fbro2/8.ogg"
    "Both" "Bro!"
    #fbro2 "Bro!"
    #fbro3 "Bro!"
    
    voice "audio/voice/E2/Free/SS/S2/fbro2/9.ogg"
    fbro2 "We watched the qualifiers. You were awesome!"
    fbro3 "The way you took out those two GEARs with your bare fists was badass!"
    
    menu:
        "It was a close call.":
            if E1D4S4_FollowMatchPlan == 0:
                pf "Yeah, but we only won thanks to Kaori."
                show shou mis at cc
                voice "audio/voice/E2/Free/SS/90.ogg"
                ss "Sure, but who else can say that took down two GEARs with no armaments?"
    
            else:
                pf "I didn’t really have much of a choice. The rest of my team went down."
                show shou hap at cc
                voice "audio/voice/E2/Free/SS/91.ogg"
                ss "And you won us the match! I hope you know we owe our rank to you."
                pf "I guess you’re right."
    
    
        "I had it in the bag!":
            pf "I know, I was pretty awesome, wasn’t I?"
            pf "When I saw my teammates go down, I knew it was up to me. My GEAR powered up like a boss and I just cleaned house."
            voice "audio/voice/E2/Free/SS/S2/fbro2/10.ogg"
            fbro2 "Up high, dude!"
            "I high-five the guy."
    
        "I’m only going to get better from here.":
            pf "I'm not going to settle for anything less than first in the rankings."
            fbro3 "That’s the right attitude, man! Yeah!" 
            voice "audio/voice/E2/Free/SS/S2/fbro2/11.ogg"
            fbro2 "When you're number one, give us a shout out, bro!"
            pf "Count on it."
            
    hide bully2
    hide bully3
    hide shou with dissolve
    "We continue down the hall towards Shou’s room, leaving his brosephs back to their game of indoor football."
    "Everywhere I turn there's at least an empty beer bottle. The trash cans are spilling with trash, and there are take-out boxes left in random areas."
    pf "Quite the place you got here."
    show shou mis at cc with dissolve
    voice "audio/voice/E2/Free/SS/92.ogg"
    ss "You like it? It feels really genuine, doesn’t it?"
    pf "Maybe a little too \"genuine\"..."
    # drop
    show shou hap at cc
    voice "audio/voice/E2/Free/SS/93.ogg"
    ss "I guess it can be kind of overwhelming. I really do like it here, though."
    stop ambient fadeout 2.0
    $ renpy.pause(1.0)
    scene bg campus dormroom day with fade:
        xzoom .75
        yzoom .75
    "Shou opens the door to his room, and I'm relieved by how clean it is. There are a few clothes and books scattered about the room, but nothing on the floor."
    "His room is decorated with posters of scantily-clad action movie heroines and video game warriors. There's a huge TV facing his bed and he has a multitude of gaming platforms set up around it."
    "I take a seat on his bed while Shou sits at his desk."
    pf "Why do you like it here so much?"
    show shou mis at cc with dissolve
    voice "audio/voice/E2/Free/SS/94.ogg"
    ss "I'm surrounded by my brothers! What's not to like?"
    pf "You have any real bros?"
    show shou smi at cc
    voice "audio/voice/E2/Free/SS/95.ogg"
    ss "Yeah, just one. He's older."
    pf "How much older? Does he go to ACE, too?"
    show shou hap at cc
    voice "audio/voice/E2/Free/SS/96.ogg"
    ss "No, he’s waaaay older!"
    pf "Do you miss him?"
    show shou smi at cc
    "Shou shrugs."
    voice "audio/voice/E2/Free/SS/97.ogg"
    ss "I suppose I do… but not so much in a brotherly way. He was more of a father to me than my father was. He's currently working overseas, though."
    
    menu:
        "Does he visit often?":
            pf "Do you get to see him much?"
            show shou thi at cc
            voice "audio/voice/E2/Free/SS/98.ogg"
            ss "Um, not really. We usually only see him once a year."
            pf "I guess living so far away can make visiting difficult."
            show shou smi at cc
            "Shou nods. He doesn't seem too bothered by it."
    
        "He's got a brother-complex!":
            pf "Bro-con."
            show shou ner at cc
            voice "audio/voice/E2/Free/SS/99.ogg"
            ss "Don’t go calling me a bro-con!"
            pf "I can see it all so clearly. The absence of an older brother figure has left a void so dark in your heart that you find yourself compensating for it by living in a house full of bros!"
            show question:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            show shou ske at cc
            voice "audio/voice/E2/Free/SS/100.ogg"
            ss "Where do you come up with this stuff?"
    
        "That explains a lot actually.":
            pf "No wonder you're so happy to live in a house full of guys."
            show question:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            show shou ske at cc
            voice "audio/voice/E2/Free/SS/101.ogg"
            ss "Uhh--what?"
            pf "You've got enough brothers to last a lifetime."
            show shou hap at cc
            "Shou grins."
            show note:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/Free/SS/102.ogg"
            ss "Isn't it great?"
            
    show shou smi at cc
    voice "audio/voice/E2/Free/SS/103.ogg"
    ss "Anyway, enough about my family! Since you’re here, how about a few matches?"
    show shou mis at cc
    "Shou tosses me a controller."
    pf "You’re on!"
    scene black with fade
    stop music fadeout 5
    $renpy.pause(1)
    "I kick Shou's ass at video games until he has to leave for class."
    $ E2SSS2_Completed = 1
    stop ambient fadeout 3
    $renpy.pause(1)
    
    #Scene Ends

