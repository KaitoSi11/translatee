#
label E2SSS4:
    
    #Weekend
    # What's the best outfit for this? I feel like he might wear something more formal but it is also the weekend...
    $ shoOut = "sCasual"
    
    "Maybe Shou is free to hang out."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(1)
    stop sound
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    "I dial his number and he picks up immediately."
    pf "Hey--"
    voice "audio/voice/E2/Free/SS/158.ogg"
    ss "Broseph! Perfect timing!"
    pf "Really?"
    voice "audio/voice/E2/Free/SS/159.ogg"
    ss "My company is hosting a big auto show. Want to come check it out?"
    "There are voices overlapping each other so it's a little hard to hear."
    voice "audio/voice/E2/Free/SS/160.ogg"
    ss "I can get you backstage passes!"
    
    menu:
        "Wow, first that expensive car and now backstage passes!":
            pf "Does this event have something to do with why that car was at your shop?"
            voice "audio/voice/E2/Free/SS/161.ogg"
            ss "Yeah! We were fixing it up and getting it pretty for the show. The rest of the cars here are just as impressive."
            pf "Awesome! Count me in."
    
        "I hope those are free backstage passes.":
            pf "They're free?"
            voice "audio/voice/E2/Free/SS/162.ogg"
            ss "Of course broseph, you know I'd hook you up!"
            pf "Alright, cool. I'll be over in a few."
            voice "audio/voice/E2/Free/SS/163.ogg"
            ss "See you soon."
    
        "Like I said before, cars aren’t really my thing.":
            pf "I saw the car at your shop last time, so I think I’ve seen them all."
            voice "audio/voice/E2/Free/SS/164.ogg"
            ss "They have motorcycles too..."
            "That got my attention."
            pf "Okay, you talked me into it. I'm on my way."
    
    jump E2D6S1_Nikki
    
    #day 6
    label E2SSS4_Continued:
        
        $ shoOut = "sCasual"
        # Why is this line even here... ?_?; it makes no sense
        #"We say our goodbyes and I get ready to leave."
        
        $renpy.pause(2.5)
        play ambient "audio/ambience/Mall.ogg" fadein 3
        # No good bgs to have a car show but these sometimes can take place in malls, so the mall bg is the current best pick
        scene bg mall main day with fade
        play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
        #fade into Auto Show
        "As I walk into the building I can't get over how… shiny everything is. Spotlights reflect off of nearly every surface. {w}Shou greets me right away."
        show shou hap at cc with dissolve
        voice "audio/voice/E2/Free/SS/165.ogg"
        ss "You made it!"
        pf "Yeah."
        show shou mis at cc
        "He gestures to the cars on display."
        voice "audio/voice/E2/missing/shou/1.ogg"
        ss "Pretty cool, right?"
        pf "This is awesome! And you're working right now?"
        show shou smi at cc
        voice "audio/voice/E2/Free/SS/166.ogg"
        ss "Yeah, I'm on-call. That's why I have time to look around."
        pf "How long has it taken you to prepare for this event?"
        show drop:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        show shou hap at cc
        voice "audio/voice/E2/Free/SS/167.ogg"
        ss "Well, this past week has been the busiest with all the last minute fixes, but I know it took the team months to put all this together."
        "I look up at the company banners hanging above their cars: FROD Engines, Voltswagon, Poshe, were among the names I recognised."
        show shou smi at cc
        voice "audio/voice/E2/Free/SS/168.ogg"
        ss "Anyway, we're the sponsored detailing company for a few of the manufacturers participating in this show and they requested for us to be here. That's why I get to participate."
        pf "They requested you by name?"
        show exclamation:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        show shou cur at cc
        "I say it as a joke but Shou looks surprised."
        voice "audio/voice/E2/Free/SS/169.ogg"
        ss "Yeah, actually, how'd you know?"
        pf "Wait--Seriously?"
        show shou smi at cc
        voice "audio/voice/E2/Free/SS/170.ogg"
        ss "Yeah, I've been handling almost all of the detail work and I've got a pretty relationship with our clients."
        show shou mis at cc
        voice "audio/voice/E2/Free/SS/171.ogg"
        ss "How do you think I scored those backstage passes?"
        pf "I hadn't thought about it…"
        show shou smi at cc
        "It's kind of weird to think of Shou as anyone other than my goofy teammate, but after listening to him talk about work, I realise this job is important to him. {w}It also sounds like his co-workers trust him and see him as responsible enough to take care of their clients."
        show note:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        show shou mis at cc
        voice "audio/voice/E2/Free/SS/172.ogg"
        ss "But I'm pretty sure you didn't come here just to hear me talk. Let's check out some of the vehicles! Anything in particular you wanna see?"
        
        menu:
            "Track cars.":
                pf "I want to see some racecars."
                show shou cur at cc
                voice "audio/voice/E2/Free/SS/173.ogg"
                ss "I didn't take you for a racer."
                pf "I just like really fast cars."
                show shiny:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                show shou hap at cc
                voice "audio/voice/E2/Free/SS/174.ogg"
                ss "I like to watch races for the crashes!"
                pf "If I want to see something crash I'd just ask you to pilot your GEAR."
                show shou dis at cc
                voice "audio/voice/E2/Free/SS/175.ogg"
                ss "Very funny."
                scene black with fade
                "We go to check out the fastest cars the show has to offer."
        
            "Exotic.":
                pf "Show me the most exotic cars on the floor!"
                show shou smi at cc
                voice "audio/voice/E2/Free/SS/178.ogg"
                ss "Hmm, exotic cars would have to be the Lambdaghini or Forraris."
                pf "Aw yeah, I just want to run my hands on them."
                show shou mis at cc
                voice "audio/voice/E2/Free/SS/176.ogg"
                ss "Yo, calm down there, hot shot. You can look but don't touch!"
                show crying:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                show shou sad at cc
                voice "audio/voice/E2/Free/SS/177.ogg"
                ss "...Just like with women."
                "I nod solemnly."
                scene black with fade
                "Shou and I go to check out the exotic cars of the venue."
        
            "Bikes.":
                pf "I'd like to see some bikes from Suzakis and Dugati."
                show shou cur at cc
                voice "audio/voice/E2/Free/SS/179.ogg"
                ss "You really like bikes, don't you?"
                pf "Who doesn't?"
                show shou smi at cc
                voice "audio/voice/E2/Free/SS/180.ogg"
                ss "Good point."
                scene black with fade
                "Shou and I head to the motorcycles."
        
            "Tuned cars.":
                pf "Introduce me to the top high performance cars."
                show bulb:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                show shou cur at cc
                voice "audio/voice/E2/Free/SS/181.ogg"
                ss "Oh, I know some cars that will knock you off your feet. Literally."
                pf "Why literally?"
                show shou mis at cc
                voice "audio/voice/E2/Free/SS/182.ogg"
                ss "Because some people tweak their cars so much, you can feel the ground shake when they run the ignition."
                scene black with fade
                "Shou and I go to test his theory."
        
            "Vintage.":
                pf "I'm interested in seeing classic cars."
                show shou hap at cc
                voice "audio/voice/E2/Free/SS/183.ogg"
                ss "What are you, my grandpa?"
                pf "I just have sophisticated tastes."
                show drop:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                show shou ske at cc
                voice "audio/voice/E2/Free/SS/184.ogg"
                ss "Okay, now you really are talking like my grandpa."
                scene black with fade
                "Shou leads the way to some old classics. Some of them are real rarities!"
        
            "Luxury.":
                pf "I want to see luxury cars."
                show note:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                show shou mis at cc
                voice "audio/voice/E2/Free/SS/185.ogg"
                ss "Oh, fancy pants. Let's be on our merry way shall we?"
                scene black with fade
                "We check out the luxury vehicles from Rolling-Roys and Panther. {w}One of the showcases includes a built-in automated espresso machine in the passenger seat."
                
        $renpy.pause(1)
        scene bg mall main day with fade
        "We return to the main floor after checking out the vehicles."
        show shou smi at cc with dissolve
        pf "So how come you didn't invite Kaori or Mayu to this?"
        show shou thi at cc
        voice "audio/voice/E2/Free/SS/186.ogg"
        ss "They’re not into this sort of stuff at all. Kaori would probably try to point out ways to \"fix up\" the different cars here and piss off the wrong people in the process."
        pf "And Mayu?"
        show shou neu at cc
        voice "audio/voice/E2/Free/SS/187.ogg"
        ss "She doesn't like humongous crowds of people. And since I’m on-call, I’d end up leaving her alone for solid pockets of time."
        show drooling:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        show shou cur at cc
        "Shou's gaze lands on two bombshells checking out a car."
        show shou hap at cc
        voice "audio/voice/E2/Free/SS/188.ogg"
        ss "Speaking of which… Duty calls, broseph!"
        hide shou with dissolve
        scene black with dissolve
        stop music fadeout 3
        "He makes a beeline towards the girls, then acts casual as he leans against the car."
        scene bg mall main day with fade
        show highschoolgirl extra at r3:
            xzoom -1
            xoffset 300
        show highschoolgirl2 extra at r2:
            xzoom -1
            xoffset 100
        with dissolve
        show shou mis at cc with dissolve
        play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
        stu3f "So, like, is the car yours?"
        voice "audio/voice/E2/Free/SS/189.ogg"
        ss "Maybe."
        "Suddenly, the girls seem more interested."
        stu4f "Oooh, really?"
        show shou hap at cc
        "Shou grins from ear to ear."
        voice "audio/voice/E2/Free/SS/190.ogg"
        ss "I actually do all the detailing myself."
        "He pats the car affectionately."
        stu3f "Wow, that looks really good!"
        stu4f "It’s so pretty!"
        show shou mis at cc
        voice "audio/voice/E2/Free/SS/191.ogg"
        ss "You think so? It's not as pretty as you--"
        # what is "dr"? Driver?
        voice "audio/voice/E2/Free/SS/S4/Driver/1.ogg"
        dr "Ladies, admiring the view?"
        show receptionist extra at l3 with dissolve
        show exclamation:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        show shou sur at cc with dissolve
        "A man with light hair saunters over. His shirt looks more expensive than my tablet. {w}Shou whirls around and stands to attention."
        show shou wor at cc
        voice "audio/voice/E2/Free/SS/192.ogg"
        ss "Oh! Uh, hello, sir. Are you enjoying the show?"
        "The man stares straight at the girls and grin."
        voice "audio/voice/E2/Free/SS/S4/Driver/2.ogg"
        dr "I am now."
        show shou ner at cc
        "The two girls giggle."
        stu3f "Are you the owner?"
        voice "audio/voice/E2/Free/SS/S4/Driver/3.ogg"
        dr "Yes, I am."
        stu4f "Your car is so impressive!"
        voice "audio/voice/E2/Free/SS/S4/Driver/4.ogg"
        dr "You like that one? Then this next one will blow you away."
        hide receptionist with dissolve
        hide highschoolgirl
        hide highschoolgirl2
        with dissolve
        "He throws an arm around each girl and leads them away."
        show shou sad at cc
        "Shou sighs."
        show storm:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/Free/SS/193.ogg"
        ss "I was so close!"
        pf "Maybe you should get yourself a nice ride instead of pretending you have one."
        "A staff member passes through, inspecting the cars, and halts in front of the one next to us."
        show guard extra at r3 with dissolve:
            xzoom -1
        mec1m "What the... Shou!"
        show panic:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        show shou sur at cc
        voice "audio/voice/E2/Free/SS/194.ogg"
        ss "Y-Yes?!"
        mec1m "There's a handprint on the hood of this car!"
        show shou ner at cc
        "He points to the vehicle, his finger shaking from the sheer sight of the offense."
        show shou wor at cc
        voice "audio/voice/E2/Free/SS/195.ogg"
        ss "I'll take care of it!"
        show shou ner at cc
        mec1m "Good, thank you."
        hide guard with dissolve
        stop music fadeout 3
        show drop:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/Free/SS/196.ogg"
        ss "Sorry, broseph. Work to do."
        "Shou grabs a cloth and wipes away the handprint, then repolishes the hood."
        play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
        "The driver circles back with the girls and grins smugly as he watches Shou work on his car. Then he leads the girls to another one of his vehicles. {w}Shou heaves a big sigh."
        
        menu:
            "Cheer up.":
                pf "Don't sweat it, man."
                show shou sad at cc
                voice "audio/voice/E2/Free/SS/197.ogg"
                ss "Easy for you to say… You weren't just humiliated."
                pf "Clearly the only thing those girls are interested in is his money."
                show shou ner at cc
                voice "audio/voice/E2/Free/SS/198.ogg"
                ss "You think so?"
                pf "Most definitely."
                show shou neu at cc
                "I nod."
        
            "Maybe we should mess with the car.":
                pf "That guy seems like a bit of a douche."
                show shou thi at cc
                voice "audio/voice/E2/Free/SS/199.ogg"
                ss "When you're around rich people long enough you get used to dealing with them."
                pf "Let's not get used to it and do something to his car instead."
                show shou neu at cc
                voice "audio/voice/E2/Free/SS/200.ogg"
                ss "I appreciate it, broseph, but this stuff doesn't bother me anymore."
                "I'm not convinced, but I don't push it."
        
            "They're not worth the fuss.":
                pf "If they are going for a guy like that, then they're not worth it."
                show shou mis at cc
                voice "audio/voice/E2/Free/SS/201.ogg"
                ss "Hah, I suppose that's true."
                
        show shou smi at cc
        voice "audio/voice/E2/Free/SS/202.ogg"
        ss "Anyway, I need to go make my rounds and make sure all the cars are still okay. You should enjoy the rest of the show."
        pf "Sure."
        show note:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        show shou hap at cc
        voice "audio/voice/E2/Free/SS/203.ogg"
        ss "If you're still around afterwards, we can hang out some more."
        hide shou with dissolve
        "He waves before hurrying off."
        
        menu:
            "Stay and check out the show.":
                "I walk around the floor some more, admiring all the cars. Maybe one day one of these cars will live in my garage…"
                "After a while, there's a commotion in the back near the Voltswagons and all the staff rush to take care of it."
                "I can't really make out what happened, but I keep hearing the word {i}emissions{/i}."
                stop music fadeout 3
                scene black with fade
                "Shou seems like he'll occupied for a while, so I hop back on my bike and head home."
        
        
            "Go home.":
                stop music fadeout 3
                scene black with fade
                "I've pretty much seen everything I wanted to see and Shou is clearly busy, so I hop back on my bike and go home."
                
        $ E2SSS4_Completed = 1
        stop ambient fadeout 3
        $renpy.pause(1)
        jump E2D6S2
        #End Scene

