#
label E2YMS1:
    
    $ yuuOut = "sTennis"
    $ yuuHairF = "pony"
    $ yuuHairB = "pony"
    
    # Event 1 - Evening Choice (>30 Points)

    "I feel like doing something active, but I don't just want to lift weights. {w}I've heard the recreation center always has lots of activities going on. There's bound to be something there I can do."
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(1)
    # gym ambient?
    scene bg campus gym day with fade
    "As I walk in, the first thing I notice is how much natural light shines into the room. The facility is huge, but it doesn't feel overwhelming."
    "There are signs leading to the different gymnasiums, and even a pool. There's a locker room nearby, and I take advantage of the facility to change into my gym clothes."
    stop music fadeout 10
    "As I continue to explore, I spot tennis courts filled with students playing matches. A few students crowd the sidelines, waiting for a court to be open. {w}Yuuna is among them. She's standing alone, stretching out her arms."
    play music "audio/music/Day Out (GAME VERSION).ogg"
    "I head over and greet her."
    show yuuna neu at cc with dissolve
    pf "Hey, Yuuna."
    show exclamation:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show yuuna sur at cc with dissolve
    voice "audio/voice/E2/Free/YM/S1/1.ogg"
    ym "Hi!"
    "She seems surprised."
    show yuuna cur at cc
    voice "audio/voice/E2/Free/YM/S1/2.ogg"
    ym "I didn't expect to see you here."
    pf "I didn't expect to be here, to be honest."
    show yuuna smi at cc
    "She chuckles."
    pf "So, you play tennis?"
    voice "audio/voice/E2/Free/YM/S1/3.ogg"
    ym "A little, just for fun."
    show yuuna cur at cc
    voice "audio/voice/E2/Free/YM/S1/4.ogg"
    ym "Do you play?"
    
    if MCStory == 1:
        pf "Not exactly. I mostly play contact sports."
        show yuuna neu at cc
        voice "audio/voice/E2/Free/YM/S1/5.ogg"
        ym "Oh, Okay."
        pf "My freetime is usually spent, you know, fighting with giant robots."
        show yuuna smi at cc
        "Yuuna giggles softly."
    
    elif MCStory == 2:
        pf "No, I've never had much time for sports. Schoolwork takes priority."
        show yuuna neu at cc
        "Yuuna nods in understanding."
        pf "That and the whole GEAR thing... but it is nice to do something different once in a while."
        show yuuna smi at cc
        voice "audio/voice/E2/Free/YM/S1/6.ogg"
        ym "Of course!"
    
    elif MCStory == 3:
        pf "I'd only play if someone invited me to… not so much on my own."
        show yuuna neu at cc
        voice "audio/voice/E2/Free/YM/S1/7.ogg"
        ym "I see."
        pf "But I do enjoy the game."
    
    pf "So have you been waiting long for a court to free up?"
    show yuuna smi at cc
    voice "audio/voice/E2/Free/YM/S1/8.ogg"
    ym "Not too long. Plus I'm next on the waitlist so once a court opens up I'll be able to play."
    pf "Who are you playing against?"
    show yuuna neu at cc
    "She shrugs."
    voice "audio/voice/E2/Free/YM/S1/9.ogg"
    ym "Anyone who's available."
    pf "How about you and I play a game then?"
    
    ### NOTE Points - "IF high points with Yuuna:"
    # temporarily set to 0
    if yuuromance > 0:
        show yuuna ner b1 at cc with dissolve
        "She suddenly seems shy."
        show yuuna smi b1 at cc
    else:
        show yuuna smi at cc
        
    voice "audio/voice/E2/Free/YM/S1/10.ogg"
    ym "Sure, but I have to warn you, I'm a bit rusty. I haven't played much this season!"
    
    menu:
        "Let's have a fun match.":
            pf "For a game between friends, who the better player is doesn't matter just as long as we're having fun."
            show note:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna hap b1 at cc with dissolve
            voice "audio/voice/E2/Free/YM/S1/11.ogg"
            ym "I agree. I'm sure this will be a good match either way."
    
        "That just means it's a better chance for me to win!":
            pf "If I see you struggling then I'll take it easy on you."
            show yuuna sur b1 at cc with dissolve
            voice "audio/voice/E2/Free/YM/S1/12.ogg"
            ym "Oh! Please don't do that. I want you to play your best regardless."
            pf "Okay, if you insist."
            show yuuna smi b1 at cc
    
        "We'll be evenly matched then.":
            pf "That's okay since I haven't really played."
            show yuuna hap b1 at cc with dissolve
            voice "audio/voice/E2/Free/YM/S1/13.ogg"
            ym "This'll be fun!"
    
        "{color=#00ff00}{b}Don't be modest!{/b}{/color}" if MCStory == 3:
            pf "I think you're just being modest. I bet you're a really skilled player who consistently wipes the floor with your opponents."
            show yuuna cur b1 at cc with dissolve
            "She blinks in surprise."
            voice "audio/voice/E2/Free/YM/S1/14.ogg"
            ym "Thanks, but what gives you that impression?"
            "I shrug."
            pf "Just a feeling that I have."
            show yuuna hap b1 at cc
            voice "audio/voice/E2/Free/YM/S1/15.ogg"
            ym "You must have a lot of faith in me."
    
    "I can't play with no equipment though…"
    pf "Is there somewhere I can borrow a racket?"
    show yuuna smi at cc with dissolve
    voice "audio/voice/E2/Free/YM/S1/16.ogg"
    ym "I actually have an extra you can use."
    pf "Great, thanks."
    
    "A court opens up and Yuuna and I take our place on opposite sides."
    pf "Since you're feeling a little anxious, why don't you serve first?"
    show yuuna ner at cc
    voice "audio/voice/E2/Free/YM/S1/17.ogg"
    ym "Oh, no, that's okay--"
    pf "Please, I insist."
    show yuuna smi at cc
    stop music fadeout 3
    "She smiles her thanks, and nods."
    hide yuuna with dissolve
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 5
    "As we settle into place, I give my racket a few experimental swings. {w}Once ready, I nod."
    "Yuuna tosses the ball into the air, and pulls back her arm."
    $ persistent.gpix[65][0] = 1
    scene cg yuuna tennis 1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    ### NOTE SFX
    "With a resounding crack, her racket connects with the ball in a powerful serve. {w}The ball whizzes towards me at lightning speed!"
    
    #Stupidly small QTE (timeout same as missed)
    $ qtebase = 2
    $ qtetotal = qteath + qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E2YMS1_Tennis1")
    menu:
        "Miss...":
            label E2YMS1_Tennis1:
                $ renpy.hide_screen ("timer_scr")
                "It speeds past me in a blur, too fast for me to catch it."
    
        "Whiff...":
            $ renpy.hide_screen ("timer_scr")
            "It speeds past me in a blur, too fast for me to catch it."
    
        "Return!":
            $ renpy.hide_screen ("timer_scr")
            "I barely manage to clip the ball!"
            "It lobs over the net but veers out of bounds."
    
    "What the heck was that?"
    scene bg campus gym day with fade
    show yuuna wor at cc with dissolve
    show panic:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/Free/YM/S1/18.ogg"
    ym "I'm sorry!"
    "I glance at Yuuna's worried face and snap out of my daze."
    pf "It's fine. I wasn't expecting that, but I'll be expecting your next one."
    show yuuna smi at cc
    "She smiles, then prepares for her next serve."
    show yuuna hap at cc
    voice "audio/voice/E2/Free/YM/S1/19.ogg"
    ym "15-love."
    hide yuuna with dissolve
    "She bounces the ball a few times, preparing herself before the serve. Then she throws it overhead."
    scene cg yuuna tennis 1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    "Her next serve is just as powerful. {w}The ball zooms towards me!"
    
    #Stupidly small QTE (timeout same as missed)
    show screen timer_scr(place="E2YMS1_Tennis2")
    menu:
        "Miss...":
            label E2YMS1_Tennis2:
                $ renpy.hide_screen ("timer_scr")
                "The ball looms close before I'm able to react. I swing wildly and graze it with the edge of my racket!"
        
        "Return!":
            $ renpy.hide_screen ("timer_scr")
            "I catch it with the tip of my racket."
        
        "Fail...":
            $ renpy.hide_screen ("timer_scr")
            "The ball looms close before I'm able to react. I swing wildly and graze it with the edge of my racket!"
        
        "Hit!":
            $ renpy.hide_screen ("timer_scr")
            "I catch it with the tip of my racket."
        
        "Whiff...":
            $ renpy.hide_screen ("timer_scr")
            "The ball looms close before I'm able to react. I swing wildly and graze it with the edge of my racket!"
    
    "The ball flies erratically but makes it over the net. Yuuna smoothly parries it back."
    
    "The longer we play, the more I'm able to keep up a volley. Yuuna's face is set in deep concentration, but she easily counters my hits every time the ball flies over the net."
    
    "If this is how she plays when she's out of practice, then I'm not sure I'm ready to face her at her peak."
    
    scene black with fade
    stop music fadeout 5
    
    if MCStory == 1:
        "Once the element of surprise is gone and I'm more used to Yuuna's plays, I manage to keep up with her fairly well. {w}In the end, she wins the match 6-4."
    
    else:
        "Still, the game is over before I know it. {w}I couldn't compare to her and she won 6-2."
        
    scene bg campus gym day with fade
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    show yuuna hap at cc with dissolve
    voice "audio/voice/E2/Free/YM/S1/20.ogg"
    ym "That was a good game! You did really well!"
    show yuuna smi at cc with dissolve
    
    if MCStory == 1:
        pf "Thanks, but I was still no match for you."
    
    else:
        pf "You're being too kind. That was clearly a one-sided game."
    
    pf "I'm not sure I believe that you're out of practice. You were amazing out there!"
    show regBlush:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show yuuna smi b1 at cc with dissolve
    "Yuuna's cheeks are flushed from both the match and from embarrassment."
    voice "audio/voice/E2/Free/YM/S1/21.ogg"
    ym "Ah, thank you, but I really don't deserve such praise."
    pf "You have nothing to be embarrassed about. Even at your worst you're still better than me."
    show yuuna hap b1 at cc
    voice "audio/voice/E2/Free/YM/S1/22.ogg"
    ym "That's not true!"
    
    pf "Are you part of the school league?"
    show yuuna neu at cc with dissolve
    "She shakes her head no."
    pf "You should really consider trying out."
    show yuuna cur at cc
    voice "audio/voice/E2/Free/YM/S1/23.ogg"
    ym "You think so?"
    pf "Definitely."
    show yuuna smi at cc
    "She seems pleased, but shrugs."
    voice "audio/voice/E2/Free/YM/S1/24.ogg"
    ym "Thanks, but I'm not sure I have time for that kind of commitment."
    
    # dont have any extra sprites wearing gym clothes
    # so no sprites here for now
    voice "audio/voice/E2/Free/YM/S1/stu8m/1.ogg"
    stu8m "Hey, are you guys finished?"
    show exclamation:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show yuuna sur at cc
    "We turn and face a pair of students walking onto the court."
    show yuuna hap at cc
    voice "audio/voice/E2/Free/YM/S1/25.ogg"
    ym "Oh yes, we just finished."
    stop music fadeout 5
    ### VOICE - missing line?
    voice "audio/voice/E2/missing/stu3f/1.ogg"
    stu3f "Actually, we were wondering if you two would be interested in a doubles match."
    show yuuna cur at cc
    pf "Doubles match?"
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 5
    "Yuuna and I glance at each other, and both break into grins."
    show yuuna mis at cc
    show note:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/Free/YM/S1/26.ogg"
    ym "Sounds like fun!"
    pf "Yeah, let's do it."
    voice "audio/voice/E2/Free/YM/S1/stu8m/2.ogg"
    stu8m "Great, you guys can serve first. Good luck!"
    hide yuuna with dissolve
    "I retrieve the ball and toss it to Yuuna. She catches it and preps to serve."
    "I don't think these two know what they're in for!"
    $ E2YMS1_Completed = 1
    
    #end
