#
label E3D3S1:
    
    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "sUniform"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sUniform"
    
    $ nikHairF = "default"
    $ nikHairB = nikHairF
    $ nikOut = "sCasual2"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "sUniform"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sUniform"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sUniform"

    $ meiHairB = "default"
    $ meiOut = "sUniform"
    $ meiHairF = "default"
    
    $ day = 3
    $ timeSpent = "none"
    $renpy.pause(1)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1)
    #beep beep beep
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(2.5)
    stop sound fadeout 1
    scene bg homekaito myroom day with fade
    "My alarm sounds, waking me up. I turn it off and prepare for the day. {w}After a quick breakfast, I drive to school and head to class."
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(1)
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 3
    scene bg campus auditorium day with fade
    play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 3
    show professorM extra at cc with dissolve
    voice "audio/voice/E3/D3/S1/profm/1.ogg"
    profm "Good morning everyone. I have some good news! Because so many of you did well on the pop quiz from last week, we're going to have another one!"
    "A chorus of groans circles around the classroom."
    voice "audio/voice/E3/D3/S1/profm/2.ogg"
    profm "I knew you'd all be excited."
    hide professorM with dissolve
    "Everyone gradually falls silent as the TA's hand out the quiz."
    
    if MCStory == 2:
        "I breezed through the last quiz and I'll breeze through this one too. {w}Once the paper lands on my desk, I scribble in the correct answers. This material is all stuff I've already learned. {w}After a few minutes, I turn in my completed test to the professor."
        show professorM extra at cc with dissolve
        voice "audio/voice/E3/D3/S1/profm/3.ogg"
        profm "Done already? You still have plenty of time if you want to check your work."
        pf "Yep, it's been checked."
        "The professor glances skeptically at my paper. Then does a double take as he recognises my name."
        show exclamation:
            xoffset 720
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/D3/S1/profm/4.ogg"
        profm "Oh! You're the student who got perfect marks on the last quiz."
        "I nod."
        "He offers me a smile."
        voice "audio/voice/E3/D3/S1/profm/5.ogg"
        profm "Thank you."
        hide professorM with dissolve
    
    else:
        "As soon as I receive mine, I begin."
        "{i}Are GEARs designed to look like a specific gender? If so, explain why.{/i}"
        
        menu:
            "No, they aren't.":
                "{i}Gears do not have a gender and as such, any implications indicating this would be incorrect.{/i}"
                "I'm not exactly sure if that was the right answer. Oh well!"
        
            "Yes, only if used for War Games.":
                "{i}A significant part of the GEAR entertainment industry is aesthetic appeal and showmanship. Due to the popular notion that the GEAR embodies the pilot, many mechas are designed in a fashion to represent this idea.{/i}"
                "This sparked quite the conversation when GEARs were first introduced for recreational use. It does pay off to pay attention to the news!"
                
            "Yes, because boobs.":
                "{i}The voluptuous nature of breasts transcends beyond being a mere piece of machinery.{/i}"
                "What an easy question, sheesh." 
        
        "After completing the test, I turn it in to the professor."
    
    "Soon everyone has turned in their paper."
    show professorM extra at cc with dissolve
    voice "audio/voice/E3/D3/S1/profm/6.ogg"
    profm "Everyone awake now? Good. In today's lesson…"
    
    #fade out
    stop music fadeout 5
    scene black with fade
    $renpy.pause(1)
    #fade in
    
    show professorM extra at cc with dissolve
    voice "audio/voice/E3/D3/S1/profm/7.ogg"
    profm "Class dismissed."
    "I gather my things and file out of the classroom with everyone else."
    stop ambient fadeout 3
    scene black with fade
    
    "Once I'm outside, my legs take me towards the Hangar. I need to practice. My chat with Akira last Monday has been on my mind ever since. Our team has been on a really good streak, but are we strong enough to beat Akira's team?"
    play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
    "I swipe myself into the Hangar and shake my head free of these thoughts."
    play ambient "audio/ambience/Hangar.ogg" fadein 3
    "We have to beat Onna-Bugeisha first."
    
    scene bg campus hangar day with fade
    "I pass Aura on my way to Eagle and hear voices raised in a heated argument."
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
    show kaori ann at l2
    show mei wor at r2:
        xzoom -1
    with dissolve
    "Kaori glares at Mei, who looks exasperated."
    voice "audio/voice/E3/D3/S1/mei/MeiEp3_Line_8.ogg"
    ms "I always have your best interests at heart!"
    show kaori dis
    voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (2).ogg"
    ki "That's not true."
    show mei ner
    voice "audio/voice/E3/D3/S1/mei/MeiEp3_Line_9.ogg"
    ms "When have I not?"
    show kaori ann
    voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (3).ogg"
    ki "Have you already forgotten about what happened with Ryouta?"
    show mei sur
    "Mei looks taken aback."
    show mei dis
    voice "audio/voice/E3/D3/S1/mei/MeiEp3_Line_10.ogg"
    ms "Really? You're bringing that up? How was I supposed to know he'd react that way?"
    show kaori ang
    show mei ann
    voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (1).ogg"
    ki "You weren't supposed to tell him at all!"
    show kaori ann
    show mei dis
    voice "audio/voice/E3/D3/S1/mei/MeiEp3_Line_11.ogg"
    ms "Maybe not, but I was trying to help."
    show vein:
        xoffset 365
        yoffset 110
        xzoom .75
        yzoom .75
    "Kaori's face contorts in anger."
    show kaori ang
    voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (4).ogg"
    ki "I was humiliated in front of the entire school! Is that what you call {i}helping{/i}?"
    show kaori ann
    show mei dis
    voice "audio/voice/E3/D3/S1/mei/MeiEp3_Line_12.ogg"
    ms "That's not fair. You know that wasn't my intention. And how Ryouta handled the situation... best friends don't treat each other like that."
    show kaori dis
    voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (5).ogg"
    ki "I know."
    show mei sad
    "Mei falters at Kaori's piercing stare."
    voice "audio/voice/E3/D3/S1/mei/MeiEp3_Line_13.ogg"
    ms "Kaori..."
    show kaori ann
    voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (6).ogg"
    ki "Well, none of that would have happened in the first place if you had just kept my secret a {i}secret{/i}. It was all {i}your{/i} fault."
    show mei wor
    "Mei blinks rapidly."
    show mei ann
    voice "audio/voice/E3/D3/S1/mei/MeiEp3_Line_14.ogg"
    ms "I can't talk to you when you're like this. You need some time to calm down. Maybe then you'll listen to reason."
    show kaori ang
    voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (7).ogg"
    ki "Don't you dare!"
    show kaori sur
    hide mei
    with dissolve
    "Mei spins on her heel and walks away, her footsteps echoing behind her."
    voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (8).ogg"
    ki "Mei!"
    show storm:
        xoffset 365
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori ang
    voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (9).ogg"
    ki "Arrgh!"
    hide kaori with dissolve
    stop music fadeout 5
    "Kaori lets out a scream of frustration into her hands. As she turns around, she notices me."
    show kaori neu at cc with dissolve
    voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (10).ogg"
    ki "How long have you been there?"
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    
    $ E3D3S1_Lie = 0
    
    menu:
        "I just got here.":
            pf "Not long at all."
            voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (11).ogg"
            ki "What did you hear?"
            pf "Nothing."
            show kaori dis
            "Kaori narrows her eyes."
            pf "Okay, just enough to watch Mei storm off."
            "She continues to stare at me."
            pf "Okay, and a little about some guy named Ryouta… but that's it!"
            show vein:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (12).ogg"
            ki "It's rude to eavesdrop."
            pf "I'm sorry, I wasn't trying to."
    
        "Long enough to enjoy the show.":
            pf "So, let me see if I got this right--Mei told some big secret of yours to this Ryouta guy who humiliated you in front of the whole school?"
            show exclamation:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori sur
            "Kaori's eyes widen, then she crosses her arms."
            show kaori ang
            voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (13).ogg"
            ki "Why were you eavesdropping?"
            show kaori ann
            pf "I don't think it counts as eavesdropping when you're shouting louder than all the mechanical whirring in here."
            show drop:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori thi
            voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (14).ogg"
            ki "W-Well, you still shouldn't have listened!"
    
        "I didn't hear anything.":
            $ E3D3S1_Lie = 1
            pf "I don't listen to things that don't concern me."
            show kaori ske
            voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (15).ogg"
            ki "You didn't hear any of that?"
            pf "It's none of my business."
            show kaori neu
            "Kaori's anger softens. She seems to appreciate that answer."
    
    
    
    if MCStory == 3:
        "Obviously this is a sensitive subject. As much as I'd like to know who Ryouta is, what happened between them, and what part Mei has to play in all of this, Kaori looks upset enough as it is. Pushing her will make her close up to me even more."
        
        pf "So, what were you doing in here anyway? Before the argument."
        show kaori neu
        "Kaori shrugs."
        voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (16).ogg"
        ki "Checking on Aura."
        show kaori ske
        voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (17).ogg"
        ki "What are you doing here?"
        pf "I thought I'd practice with Eagle."
        show kaori neu
        voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (18).ogg"
        ki "Oh."
        show dots:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        "An uncomfortable silence settles in."
    
    else:
        pf "So, what was that about anyway?"
    
        if E3D3S1_Lie == 1:
            show kaori ske
            "Kaori eyes me suspiciously."
            voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (19).ogg"
            ki "I thought you didn't hear anything."
            "My cheeks flare as I look away."
            
        show kaori thi
        voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (20).ogg"
        ki "It was nothing."
        pf "Who's Ryouta?"
        show kaori neu
        voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (21).ogg"
        ki "Nobody you know."
        pf "Does he go here?"
        show kaori dis
        voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (22).ogg"
        ki "No."
        pf "So who is he then?"
        show kaori ann
        voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (23).ogg"
        ki "He is {i}none of your business{/i}."
        show storm:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/D3/S1/kaori/E3_D3_Kaori (24).ogg"
        ki "Besides, you've already heard all about it when you were listening in on a {i}private{/i} conversation."
        pf "Uh… no, that's not--"
    
    #phone buzzing
    play sound [ "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg" ]
    "My phone buzzes."
    "Saved by the bell!... Well, buzz, I guess."
    stop music fadeout 5
    pf "Sorry, I better get this."
    show kaori neu
    "Kaori nods. She looks just as relieved as I am."
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    hide kaori with dissolve
    "I accept the call and walk further away from Kaori."
    pf "Hello?"
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E3/D3/S1/yuuna/1.ogg"
    ym "Hey!"
    pf "Hi Yuuna."
    voice "audio/voice/E3/D3/S1/yuuna/2.ogg"
    ym "I hope I didn't catch you at a bad time..."
    pf "No, no, this is perfect."
    voice "audio/voice/E3/D3/S1/yuuna/3.ogg"
    ym "Okay, so your account manager with Dasshu reached out to me. He'll be close to campus later today and would like to meet with you."
    pf "Oh! Yeah, definitely. I'm not sure what everyone's schedules look like--"
    voice "audio/voice/E3/D3/S1/yuuna/4.ogg"
    ym "Wait! He wants to meet with just {i}you{/i}."
    
    menu:
        "Is this another interview?":
            pf "Um, is this going to be like the Warptech interview?"
            voice "audio/voice/E3/D3/S1/yuuna/5.ogg"
            ym "No, it'll be a much more casual conversation. He wants to talk about your GEAR, not your team performance."
            #removed a bunch of lines because it says they played one match but that's incorrect
            #voice "audio/voice/E3/D3/S1/yuuna/6.ogg"
            #voice "audio/voice/E3/D3/S1/yuuna/7ogg"
            pf "That sounds good."
    
        "Uh huh, I'll bet he wants to \"get to know me better\".":
            pf "Does he want to get to know me better?"
            voice "audio/voice/E3/D3/S1/yuuna/8.ogg"
            ym "Yeah--"
            pf "That's flattering, but he's not really my type."
            voice "audio/voice/E3/D3/S1/yuuna/9.ogg"
            ym "What?"
            pf "What?"
            voice "audio/voice/E3/D3/S1/yuuna/10.ogg"
            ym "He wants to learn more about your GEAR."
            pf "Oh… So, not me?"
            voice "audio/voice/E3/D3/S1/yuuna/11.ogg"
            ym "Well, I guess some of it is about you? But mostly it'll be about Eagle."
            "Why do I feel a little disappointed by that?"
            pf "Eagle?"
            voice "audio/voice/E3/D3/S1/yuuna/12.ogg"
            ym "He's impressed by how well your GEAR has been able to hold out against some of the newer models."
    
        "Am I in trouble?":
            pf "Did I do something wrong?"
            voice "audio/voice/E3/D3/S1/yuuna/13.ogg"
            ym "No, not at all! He has some questions about your GEAR."
            pf "Why? What's wrong with Eagle?"
            voice "audio/voice/E3/D3/S1/yuuna/14.ogg"
            ym "Nothing, he's impressed by it! He wants to know how your outdated American GEAR is able to outperform even the newest Japanese models."
            pf "Outdated…"
            voice "audio/voice/E3/D3/S1/yuuna/15.ogg"
            ym "Not in a bad way! It's just not new."
            
    voice "audio/voice/E3/D3/S1/yuuna/16.ogg"
    ym "So, will you meet him?"
    pf "Sure."
    voice "audio/voice/E3/D3/S1/yuuna/17.ogg"
    ym "Great! You can meet him at the cafe after lunch."
    pf "Alright, I'll be there. Thanks, Yuuna."
    voice "audio/voice/E3/D3/S1/yuuna/18.ogg"
    ym "No problem!"
    # sfx
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    "After saying goodbye, she hangs up."
    
    "By the time I end the call, Kaori is nowhere in sight. That's probably for the best, honestly. Our chat didn't end on such a great note."
    scene black with fade
    "Since I came here to practice, I climb into Eagle and start up a simulated match."
    #timeskip
    $renpy.pause(1)
    stop music fadeout 5
    scene bg campus hangar day with fade
    "After I've practiced a few rounds, I shut down the simulators and climb out of Eagle. I can tell my reaction times are improving. I'm sure with a little more practice I'll be ready to face Onna-Bugeisha."
    
    stop ambient fadeout 3
    scene black with fade
    play ambient "audio/ambience/Pilot Lounge.ogg" fadein 3
    scene bg campus lounge day with fade
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
    "Since I have some extra time, how do I want to spend the rest of my afternoon?"
    
    #Afternoon choice
    $ freeTime = "afternoon"
    call E3FreeTime from _call_E3FreeTime_1
    
    jump E3D3S2
