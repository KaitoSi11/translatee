#
label E2D2S4:
    
    $ nikOut = "sUniform"
    #evening choice end

    scene black with fade
    stop ambient fadeout 3
    stop music fadeout 3
    $renpy.pause(2.5)
    play ambient "audio/ambience/Night Crickets.ogg" fadein 1
    scene bg homekaito main night with fade
    
    "As soon I get home, Nikki jumps off the couch and greets me."
    
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 1
    show nikki hap at cc with dissolve
    voice "audio/voice/E2/D2/S4/Nikki/1.ogg"
    sf "There you are! What took you so long?"
    pf "What?"
    show nikki neu at cc
    "She has her hands on her hips and taps her foot impatiently. {w}Did I forget we had plans tonight?"

    menu:
        "Run!":
            "I drop my stuff on the floor and open the front door, when Nikki grabs my collar."
            show nikki wor at cc
            show panic:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D2/S4/Nikki/2.ogg"
            sf "Hey! Where are you going?"
            "Losing my balance, I fall backwards. Nikki's face hovers above me."
            pf "It's not my fault! Don't be angry!"
            show nikki ske at cc
            voice "audio/voice/E2/D2/S4/Nikki/3.ogg"
            sf "Why did you run?"
            pf "I forgot we had plans."
            show question:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D2/S4/Nikki/4.ogg"
            sf "Huh? We didn't make plans."
            pf "Oh…"
            show nikki neu at cc
            "Nikki helps me get back on my feet."
            pf "Then why were you waiting for me?"
    
        "Turn it around on her.":
            "I cross my arms and mimic her impatience."
            pf "The better question is: what took {i}you{/i} so long?"
            show nikki cur at cc
            voice "audio/voice/E2/D2/S4/Nikki/5.ogg"
            sf "Uhh?"
            show nikki ske at cc
            voice "audio/voice/E2/D2/S4/Nikki/6.ogg"
            sf "What are you talking about?"
            show confused:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            pf "What are {i}you{/i} talking about?"
            show nikki neu at cc
            voice "audio/voice/E2/D2/S4/Nikki/7.ogg"
            sf "I've been waiting forever for you to come home!"
            "Home? {w}Oh, I guess we didn't have plans."
            pf "Why?"
    
        "Play it cool.":
            pf "I'm no later than usual."
            show nikki neu at cc
            voice "audio/voice/E2/D2/S4/Nikki/8.ogg"
            sf "So? I've still been waiting forever for you to come home!"
            pf "Really? You usually come home around the same time that I do. How come you came back so early this time?"

    show nikki smi at cc
    show note:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D2/S4/Nikki/9.ogg"
    sf "Well, I have some exciting news!"
    "Nikki sits down on the couch and I follow her."
    show nikki neu at cc
    pf "What is it?"
    voice "audio/voice/E2/D2/S4/Nikki/10.ogg"
    sf "Remember when you suggested I start a cooking club at school?"
    pf "Yeah."
    show nikki smi at cc
    voice "audio/voice/E2/D2/S4/Nikki/11.ogg"
    sf "I took your advice and spoke with the school administration and they loved the idea! I already have a teacher who has agreed to sponsor the club, and a few of my classmates have approached me asking if they could join."
    pf "That's awesome, Nikki!"
    show nikki hap at cc
    voice "audio/voice/E2/D2/S4/Nikki/12.ogg"
    sf "I know! I was thinking of structuring it so that we can learn a new dish each week and anyone can share a dish so it's not just me leading everything."
    voice "audio/voice/E2/D2/S4/Nikki/13.ogg"
    sf "Our first meeting is next week and I thought I could start us off by teaching something simple and non-Japanese."
    show nikki cur at cc with dissolve
    "She pauses, and looks thoughtfully at me."
    show nikki neu at cc
    voice "audio/voice/E2/D2/S4/Nikki/14.ogg"
    sf "What do you think I should make?"

    menu:
        "Sushi.":
            pf "Sushi."
            show nikki dis at cc
            voice "audio/voice/E2/D2/S4/Nikki/15.ogg"
            sf "I said {i}not{/i} Japanese."
            pf "Oh, um, California rolls?"
            show nikki ann at cc
            show storm:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D2/S4/Nikki/16.ogg"
            sf "Not what I meant!"
    
        "Sandwich.":
            pf "Make sandwiches. Everyone loves sandwiches."
            show nikki ske at cc
            voice "audio/voice/E2/D2/S4/Nikki/17.ogg"
            sf "Yeah, because everyone already knows how to make them."
            pf "Maybe they know how to make normal sandwiches, but not necessarily the fancy tiny ones that are gone in one bite."
            show nikki cur at cc
            voice "audio/voice/E2/D2/S4/Nikki/18.ogg"
            sf "You mean, finger sandwiches?"
            pf "Geez, Nikki, that's morbid."
    
        "Salad.":
            pf "Salad. That's what you girls like to eat, isn't it?"
            show nikki thi at cc
            voice "audio/voice/E2/D2/S4/Nikki/19.ogg"
            sf "It's not just girls in this club. There is one guy who signed up."
            pf "Heh, you know why he did, right?"
            show nikki cur at cc
            voice "audio/voice/E2/D2/S4/Nikki/20.ogg"
            sf "Because he wants to learn how to cook?"
            "Because as the only guy in an all-girls group he'll be an automatic chick magnet."
            pf "... Yes, that's it."
            pf "But yeah, salad I guess. Or maybe like a boiled potato..."
            
    show nikki ske at cc
    voice "audio/voice/E2/D2/S4/Nikki/21.ogg"
    sf "Let me guess, those are the only foods you can make."
    pf "Of course not! I know how to make mac and cheese."
    show nikki mis at cc
    voice "audio/voice/E2/D2/S4/Nikki/22.ogg"
    sf "Heating stuff from a box... that's not cooking."
    pf "I can make spaghetti."
    voice "audio/voice/E2/D2/S4/Nikki/23.ogg"
    sf "Uh-huh, maybe you should join our club!"
    pf "And that is my cue to leave."
    show nikki wor at cc
    show crying:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D2/S4/Nikki/24.ogg"
    sf "No, don't go! I was just kidding!"
    "I laugh."
    pf "I know, but I've got some studying I need to do anyway."
    show nikki sad at cc
    voice "audio/voice/E2/D2/S4/Nikki/25.ogg"
    sf "Okay…"
    pf "Congratulations on getting your club started! I bet it'll end up being the most popular club in your school."
    show nikki neu at cc
    voice "audio/voice/E2/D2/S4/Nikki/26.ogg"
    sf "Ha, thanks. I don't know if that's a good thing or not. I like having a smallish-sized group so we can all interact easily, but having a larger group means more exposure to new foods…"
    show nikki smi at cc
    voice "audio/voice/E2/D2/S4/Nikki/27.ogg"
    sf "Anyway, that's getting way ahead of ourselves."
    pf "Yeah, you still need to decide what you're going to do for your first meeting."
    show nikki mis at cc
    voice "audio/voice/E2/D2/S4/Nikki/28.ogg"
    sf "Some help you've been!"
    "I laugh and begin to head upstairs."
    pf "You know you still love me."
    show nikki smi at cc
    voice "audio/voice/E2/D2/S4/Nikki/30.ogg"
    sf "That's what you think."
    show note:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    "She waves goodbye anyway."
    
    scene black with fade
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
    stop music fadeout 3
    $renpy.pause(2.5)
    scene bg homekaito myroom night with fade
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 1
    
    "Once in my room, I settle down at my desk and begin collecting research and statistics I can present at the interview. I want to be well-informed, especially if I'm going to be representing my team."
    "Wait. {w}Did Kaori or Mayu ever respond to my text?"
    "A quick check of my phone shows me they did. {w}I open Mayu's text first."
    "{i}I hope it doesn't cause you much trouble if I don't go but I have a previous engagement and can't make it. Best of luck!{/i}"
    "I shrug. At least she was nice about it. {w}Next, I open Kaori's text."
    "{i}Why did you schedule the interview so soon?? Of course I can't make it! Don't mess this up!{/i}"
    "Thanks for the vote of confidence, Kaori."
    "At least Yuuna will be there to back me up."
    "I read over my notes a few more times until I'm confident about what I'll say. Then I head to bed early so I can be well rested tomorrow."
    
    stop music fadeout 3
    scene black with fade
    stop ambient fadeout 3
    
    jump E2D3S1
