#
label E2D5S1:
    
    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "sUniform"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sUniform"
    
    $ nikHairF = "default"
    $ nikHairB = nikHairF
    $ nikOut = "sUniform"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "sUniform"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sUniform"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sUniform"
    
    $ day = 5
    $ timeSpent = "none"
    
    $renpy.pause(2.5)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(2.5)
    #beep beep beep
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(1)
    #fade in
    scene bg homekaito myroom day with fade
    stop sound fadeout 1
    "I turn off my alarm and roll out of bed. Time to get ready for class."
    scene bg homekaito main day with fade
    "As I head downstairs, I feel uneasy. {w}Today will be our first match. I really hope Yuuna was able to work her magic and get us a sponsor…"
    "Nikki is rummaging in the living room, and I smile when I see her. Even when I'm stressed or worried, Nikki always seems to know how to put my mind at ease."
    show nikki dis at cc with dissolve
    pf "Hey, Nikki, just the person I was hoping to see--"
    voice "audio/voice/E2/D5/S1/Nikki/1.ogg"
    sf "Look, If you're hungry, you'll have find your own food. I don't have time to cook today."
    play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 5
    "She doesn't pause to look at me when she speaks, but continues gathering what she needs for the day."
    "Hm… {w}Not quite the welcome I was expecting…"
    pf "You okay?"
    show storm:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D5/S1/Nikki/2.ogg"
    sf "Yes. Just in a hurry."
    pf "Oh, do you need a ride to school?"
    show nikki ske at cc
    "She freezes, then whirls on me."
    show nikki ang at cc
    voice "audio/voice/E2/D5/S1/Nikki/3.ogg"
    sf "Oh, {i}now{/i} you offer me a ride? A little too late for that!"
    show nikki ann at cc
    "She throws her books into her bag."
    
    $ E2D5S1_Nikki = 0
    
    menu:
        "She doesn't seem okay…":
            $ E2D5S1_Nikki = 2
            pf "Are you sure you're okay?"
            show nikki dis at cc
            voice "audio/voice/E2/D5/S1/Nikki/4.ogg"
            sf "Yes, why wouldn't I be?"
            pf "I don't know. Did something happen?"
            show dots:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            "She just stares at me."
            "Uh, did I do something? Why is she looking at me like it's my fault?"
            show nikki thi at cc
            "When I don't answer, Nikki sighs."
    
        "Uh oh, is it that time of the month again?":
            $ E2D5S1_Nikki = 1
            "When Aunt Flow comes here, that's my cue to disappear."
            "The best way to handle this situation is to just smile and nod."
            pf "Okay, well, let me know if you change your mind… {w}We can stop by the store and get you some chocolate."
            show nikki ske at cc
            "She furrows her brows in confusion, then her eyes open wide in understanding."
            show nikki ang at cc
            voice "audio/voice/E2/D5/S1/Nikki/5.ogg"
            sf "Oh my god! That's not it!"
            show nikki ann at cc
            pf "Sure, sure, I know."
            "I wink at her."
            show vein:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D5/S1/Nikki/6.ogg"
            sf "Ughh."
    
        "What crawled up her butt and died?":
            "I have enough to deal with already. I don't have time for Nikki's games."
            pf "Fine."
            show nikki ann at cc
            voice "audio/voice/E2/D5/S1/Nikki/7.ogg"
            sf "Fine!"
            
    show nikki dis at cc
    voice "audio/voice/E2/D5/S1/Nikki/8.ogg"
    sf "I need to get to school. I'll see you later."
    stop music fadeout 3
    hide nikki with dissolve
    "She's out of the door before I can say goodbye."
    "That was weird. {w}Shrugging, I head into the kitchen to whip up a quick breakfast. Hopefully she's in a better mood the next time I see her."
    stop ambient fadeout 3
    scene black with fade
    "After eating, I hop on my bike and drive to school."
    
    #bg change
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 3
    scene bg campus auditorium day with fade
    "Yuuna is already in class when I arrive. She waves as I walk in, and I sit beside her."
    show yuuna neu at cc with dissolve
    pf "Hey, Yuuna."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    show yuuna hap at cc
    voice "audio/voice/E2/D5/Yuuna/1.ogg"
    ym "Hey!"
    "She wears a wide grin and fidgets with excitement."
    pf "You seem like you're in a good mood."
    voice "audio/voice/E2/D5/Yuuna/2.ogg"
    ym "I am!"
    show yuuna smi at cc
    "She pauses."
    voice "audio/voice/E2/D5/Yuuna/3.ogg"
    ym "Aren't you?"
    pf "Uh, I guess so."
    show yuuna neu at cc
    voice "audio/voice/E2/D5/Yuuna/4.ogg"
    ym "I thought you'd be a little more excited than that."
    pf "Really? How come?"
    show yuuna thi at cc
    "She seems confused."
    voice "audio/voice/E2/D5/Yuuna/5.ogg"
    ym "Uh, well, I guess I just assumed that this had been hard for you, and I thought I'd helped bring you some relief."
    pf "What?"
    show yuuna neu at cc
    voice "audio/voice/E2/D5/Yuuna/6.ogg"
    ym "What?"
    pf "W-What are you talking about?"
    voice "audio/voice/E2/D5/Yuuna/7.ogg"
    ym "You know--I found you a sponsor."
    pf "Ohhhh… {w}That's amazing! How did you manage that?"
    show yuuna mis at cc
    voice "audio/voice/E2/D5/Yuuna/8.ogg"
    ym "I called in a favour, but that doesn't matter. I've already set up your account with them and repairs are underway."
    show yuuna smi at cc
    voice "audio/voice/E2/D5/Yuuna/9.ogg"
    ym "They started as soon as the paperwork was signed, so your GEARs will be as good as new in time for the match today."
    pf "I don't know how to thank you."
    show yuuna hap b1 at cc with dissolve
    "She blushes."
    voice "audio/voice/E2/D5/Yuuna/10.ogg"
    ym "You don't have to. I promised I'd find you one, and I always keep my promises."
    
    ### NOTE Points - "IF high points with Yuuna:"
    # temporarily set to 0
    if yuuromance > 0:
        pf "I don't know what I'd do without you. You're a lifesaver."
        show regBlush:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna smi b2 at cc with dissolve
        "Yuuna's blush deepens and she seems pleased by my words."
    
    else:
        pf "The team and I really appreciate you doing this for us."
    
    show yuuna smi at cc with dissolve
    pf "You should come meet the team before the match. We can share the good news together."
    voice "audio/voice/E2/D5/Yuuna/11.ogg"
    ym "Sure, as long as I won't intrude on anything."
    pf "You won't."
    "She nods."
    
    pf "So, I know we won't get our scores back this class, but how do you think we did on the project?"
    
    if E1D5S1_EventYuuna == 0:
        ### NOTE FreeTime - "IF did not do weekend event and PFIntel == 0:"
        if MCStory != 2:
            show yuuna thi at cc
            "Yuuna looks thoughtful."
            voice "audio/voice/E2/D5/Yuuna/12.ogg"
            ym "Hmm, I think we had a really strong topic and will do well."
            pf "Yeah... I'm sorry we didn't get a chance to meet this weekend and work on the project together."
            show yuuna smi at cc
            "She smiles and waves away my apology."
            voice "audio/voice/E2/D5/Yuuna/13.ogg"
            ym "That's okay. You still did your part, which was helpful."
            "She's being really nice about this, but I know I didn't work as hard on the project as she did. I should probably make it up to her another time."
            
            ### NOTE FreeTime - "ELIF did not go to weekend event and PFIntel == 1:"
        else:
            show yuuna mis at cc
            voice "audio/voice/E2/D5/Yuuna/16.ogg"
            ym "You know what? I think we'll get a great mark."
            show yuuna thi at cc
            "She turns sheepish and looks away."
            voice "audio/voice/E2/D5/Yuuna/17.ogg"
            ym "I'm actually a little surprised."
            pf "How come?"
            show yuuna neu at cc
            voice "audio/voice/E2/D5/Yuuna/18.ogg"
            ym "Well, since we weren't able to find time to meet over the weekend I wasn't sure how much time we'd be able to put into it."
            pf "Heh, I was a bit surprised when you sent me your entire section on Sunday."
            show yuuna smi at cc
            voice "audio/voice/E2/D5/Yuuna/19.ogg"
            ym "Haha, I was surprised when you finished your half first. We completed the project before the weekend even ended!"
            "She smiles warmly at me."
            show yuuna hap at cc
            voice "audio/voice/E2/D5/Yuuna/20.ogg"
            ym "I'm really glad I was able to have you as my partner."
            "Now I'm the one feeling a little shy."
            pf "I really enjoyed working with you too. Glad I didn't disappoint."
            show yuuna smi at cc
            "She smiles."
    
    else:
        ### NOTE FreeTime - "ELIF did weekend event and PFIntel == 0:"
        if MCStory != 2:
            show yuuna hap at cc
            voice "audio/voice/E2/D5/Yuuna/14.ogg"
            ym "I think we'll get a really high mark!"
            pf "Yeah? I hope so. We worked really hard on it."
            show yuuna smi at cc
            "She nods."
            voice "audio/voice/E2/D5/Yuuna/15.ogg"
            ym "I feel really confident about it. I'm happy we were able to meet over the weekend and finish the project together. I think it made a huge difference than if we worked separately."
            pf "Me too."
            "And getting to spend some time alone with her was an added bonus."
            
            ### NOTE FreeTime - "ELIF did weekend event and PFIntel == 1:"
        else:
            $ E2D5S1_Praise = 1
            show yuuna hap at cc
            voice "audio/voice/E2/D5/Yuuna/21.ogg"
            ym "I'm sure we did really well!"
            pf "Yeah, me too. We worked great together over the weekend and I'm glad I had someone who was as interested in the project as I was."
            show yuuna smi at cc
            voice "audio/voice/E2/D5/Yuuna/22.ogg"
            ym "I feel the same way. Our discussions helped us build really strong arguments and I'm sure we'll get a high mark."
            pf "Those are some pretty confident words."
            show yuuna smi b1 at cc with dissolve
            "Yuuna blushes."
            show regBlush:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D5/Yuuna/23.ogg"
            ym "I guess I'm just feeling lucky to have such a great partner."
            "I can't help but grin at her words."
    
    $renpy.pause(.5)
    stop music fadeout 3
    hide yuuna with dissolve
    $renpy.pause(.5)
    "As our conversation winds to a close, the professor comes in and starts the class."
    
    #time skip
    scene black with fade
    $renpy.pause(2.5)
    play sound "audio/sfx/Human/Class End.ogg"
    scene bg campus auditorium day with fade
    "The professor wraps up the lesson, and students begin to file out of the classroom."
    
    ### NOTE FreeTime - "IF did weekend event and PFIntel == 1:"
    if E2D5S1_Praise == 1:
        show professorF extra at r2 with dissolve:
            xzoom -1
        "As I'm about to leave, the professor stops me."
        voice "audio/voice/E2/D5/S1/prof2f/1.ogg"
        prof2f "Do you have a minute? Ms. Misaki, if you could kindly join us as well."
        show yuuna cur at l2 with dissolve
        "Yuuna and I glance at each other. {w}I whisper to her."
        pf "Do you know what this is about?"
        show yuuna ner at l2
        "She shakes her head."
        "We obediently follow the professor back to her desk, ignoring the curious looks of our departing classmates."
        show yuuna neu at l2
        voice "audio/voice/E2/D5/S1/prof2f/2.ogg"
        prof2f "I had a chance to look over your paper…"
        "She pauses, then breaks into a huge smile."
        play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
        voice "audio/voice/E2/D5/S1/prof2f/3.ogg"
        prof2f "And I loved it!"
        show yuuna smi at l2
        "Both Yuuna and I wear matching grins."
        voice "audio/voice/E2/D5/S1/prof2f/4.ogg"
        prof2f "In fact, I think it's worthy for publication in the {i}Cenorobotics Journal{/i}, and I wanted to ask for your permission to submit it."
        show yuuna cur at l2
        "Yuuna's mouth hangs slightly open in amazement. Even though she predicted our project would be great, I don't think even she had considered it would be this great."
        pf "If you think it's good enough for submission then I would be happy to have it submitted."
        show yuuna smi at l2
        "Yuuna nods."
        voice "audio/voice/E2/D5/Yuuna/24.ogg"
        ym "I'd also be happy to have it submitted."
        voice "audio/voice/E2/D5/S1/prof2f/5.ogg"
        prof2f "Great! Stop by my office hours when you two have a chance and we can go over edits. Once that's all done, I'll handle the submission paperwork, so you two don't have to worry about any of the logistical details."
        voice "audio/voice/E2/D5/S1/prof2f/6.ogg"
        prof2f "Congratulations, and I hope you will keep up your hard work."
        voice "audio/voice/E2/D5/Yuuna/25.ogg"
        ym "Thank you, Professor."
        pf "Thank you."
        hide professorF with dissolve
        show yuuna smi at cc with dissolve
        "As we are dismissed, we gather up our belongings."
        show yuuna hap at cc
        voice "audio/voice/E2/D5/Yuuna/26.ogg"
        ym "Can you believe it? I knew we'd do well, but I didn't dream we'd do that well!"
        "Yuuna's excitement is infectious as a bright smile lights up her face."
        pf "Yeah, it seems a little hard to believe."
        show yuuna smi at cc
        show note:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/D5/Yuuna/27.ogg"
        ym "This just proves we make a great team."
        pf "Maybe we'll have more opportunities to work together."
        show yuuna smi b1 at cc with dissolve
        voice "audio/voice/E2/D5/Yuuna/28.ogg"
        ym "I hope so."
        stop music fadeout 3
        hide yuuna with dissolve
        "We head out of class together."
        "I can tell today is going to be a great day!"
    
    else:
        "I gather up my belongings and head out of class."
    
    stop ambient fadeout 3
    scene bg campus building day with fade
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
    play ambient "audio/ambience/Campus.ogg" fadein 3
    "I want to text my team, but when I reach into my pocket I find empty air."
    "Damn. {w}My phone's still in my GEAR... {w}which is still undergoing repairs..."
    show yuuna neu at cc with dissolve
    "Yuuna walks beside me."
    pf "How much longer do you think it will be until the repairs are done?"
    show yuuna thi at cc
    voice "audio/voice/E2/D5/Yuuna/29.ogg"
    ym "Hm... probably most of the afternoon. That's how long it usually takes, if I remember correctly."
    pf "Okay."
    show yuuna ner at cc
    voice "audio/voice/E2/D5/Yuuna/30.ogg"
    ym "Is something wrong?"
    "I don't want to tell her my phone is in there. That might bring up some awkward questions about what it's doing in there. {w}I recall the team's reaction from yesterday and am confident in my decision to avoid the topic."
    pf "I'm just eager to check up on my GEAR."
    show yuuna smi at cc
    "She nods understandingly, a small smile on her lips."
    voice "audio/voice/E2/D5/Yuuna/31.ogg"
    ym "When should I come meet the team?"
    pf "How about once the repairs are done? We can meet in front of the Hangar and I'll let you in."
    show yuuna hap at cc
    show note:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D5/Yuuna/32.ogg"
    ym "Great! I'll see you then."
    hide yuuna with dissolve
    "Yuuna slings her bag over her shoulder and heads off."
    
    stop music fadeout 5
    "I really should text my team about the repairs now rather than later... {w}It should be fine to go collect my phone."
    
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(1)
    play ambient "audio/ambience/Hangar.ogg" fadein 3
    scene bg campus hangar day with fade
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    
    "I make my way to the Hangar, but Eagle isn't in its usual dock. {w}They must have moved it so they could complete the repairs without any chance of accidentally harming the surrounding GEARs."
    
    "I circle around the Hangar until I come upon an enclosed area in a far corner, well away from the parked GEARs. As I approach, I can hear the whir of machinery muffled through the heavy doors, which are open ajar. I peek inside and see Eagle and Emerald surrounded by a group of mechanics."
    "I push on the doors, but before I can enter one of the mechanics jogs over to me."
    # do we have mechanic sprites planned? gonna use guard here i think
    show guard extra at cc with dissolve
    voice "audio/voice/E2/D5/S1/mec1m/1.ogg"
    mec1m "Sorry, only personnel may enter here."
    pf "My GEAR is here."
    voice "audio/voice/E2/D5/S1/mec1m/2.ogg"
    mec1m "Then it's undergoing repairs right now."
    pf "I know, but I need to get something from my GEAR."
    voice "audio/voice/E2/D5/S1/mec1m/3.ogg"
    mec1m "You can get it when repairs are complete."
    pf "Actually, I need it now."
    voice "audio/voice/E2/D5/S1/mec1m/4.ogg"
    mec1m "Why? What is it?"
    pf "Uh..."
    
    menu:
        "This is so embarrassing...":
            "I mumble out my response."
            pf "It's my phone. I left it in the cockpit."
            voice "audio/voice/E2/D5/S1/mec1m/5.ogg"
            mec1m "What?"
            pf "My phone..."
            voice "audio/voice/E2/D5/S1/mec1m/6.ogg"
            mec1m "What is your phone doing in your GEAR?"
            pf "... I was charging it."
            "The mechanic crosses his arms."
            voice "audio/voice/E2/D5/S1/mec1m/7.ogg"
            mec1m "Your GEAR is not a charging station."
            pf "I know."
            "He sighs."
            voice "audio/voice/E2/D5/S1/mec1m/8.ogg"
            mec1m "Alright, which GEAR is yours?"
            "I point to Eagle."
            
            voice "audio/voice/E2/D5/S1/mec1m/20.ogg"
            mec1m "Wait here."
            hide guard with dissolve
            "He closes the door. {w}After a few minutes, he returns with my phone in his hand."
            show guard extra at cc with dissolve
            
            pf "Thanks."
            voice "audio/voice/E2/D5/S1/mec1m/23.ogg"
            mec1m "Is there anything else?"
            pf "No, thanks again."
            hide guard with dissolve
            "He nods, then shuts the door."
    
        "Make up something really important.":
            pf "It's my medication."
            "His eyes go wide."
            voice "audio/voice/E2/D5/S1/mec1m/9.ogg"
            mec1m "Medication?"
            pf "Yeah, I left it in the cockpit..."
            "He nods."
            voice "audio/voice/E2/D5/S1/mec1m/10.ogg"
            mec1m "Okay, I'll make an exception for you. But please try to remember to have everything removed from your GEAR for next time."
            pf "I will."
            voice "audio/voice/E2/D5/S1/mec1m/11.ogg"
            mec1m "Which one is your GEAR? I'll get it for you."
            pf "It's okay, I can get it."
            voice "audio/voice/E2/D5/S1/mec1m/12.ogg"
            mec1m "Sorry, but I can't let you go back there. It's a liability issue. Tell me which one it is and I'll get it for you."
            "Uh oh…"
            pf "Uh, it's okay, I don't want to make trouble for you. I'll come back later."
            "He glares at me."
            voice "audio/voice/E2/D5/S1/mec1m/13.ogg"
            mec1m "I thought you said this was important."
            "Clearly, I didn't think this through."
            "I meekly point to Eagle."
            pf "Um, it's that one…"
            
            voice "audio/voice/E2/D5/S1/mec1m/20.ogg"
            mec1m "Wait here."
            hide guard with dissolve
            "He closes the door. {w}After a few minutes, he returns with my phone in his hand."
            show guard extra at cc with dissolve
            
            voice "audio/voice/E2/D5/S1/mec1m/21.ogg"
            mec1m "I couldn't find your medication, but I found this phone charging in your cockpit."
            pf "Ohhh, so that's where I left it!"
            "He gives me a strange look as he hands me my phone."
            pf "... The medication is to help with my memory."
            "He doesn't seem amused."
            voice "audio/voice/E2/D5/S1/mec1m/22.ogg"
            mec1m "Ironic that you misplaced it then."
            pf "Heh, yeah. Anyway, thanks for this. I guess I'll look in my room again for the meds."
            hide guard with dissolve
            "I leave as he shuts the door."
            "That turned out better than expected."
    
        "Just let me get it.":
            pf "Does it matter? It's important to me."
            voice "audio/voice/E2/D5/S1/mec1m/14.ogg"
            mec1m "Yes, it does matter because I will have to interrupt everyone's work so either myself or another mechanic can go into your GEAR and collect it for you."
            pf "Why can't I go myself?"
            voice "audio/voice/E2/D5/S1/mec1m/15.ogg"
            mec1m "It's against policy. Too much of a liability."
            pf "I can be careful."
            voice "audio/voice/E2/D5/S1/mec1m/16.ogg"
            mec1m "I don't need you to keep wasting my time by arguing. Either tell me what you need or leave so I can get back to work."
            pf "Fine, I left my phone in the cockpit."
            voice "audio/voice/E2/D5/S1/mec1m/17.ogg"
            mec1m "That's your very important thing?"
            pf "Yeah."
            "He sighs."
            voice "audio/voice/E2/D5/S1/mec1m/18.ogg"
            mec1m "Fine. I'll get it, but only because I know this is the only way to get you to leave."
            voice "audio/voice/E2/D5/S1/mec1m/19.ogg"
            mec1m "Which one is your GEAR?"
            "I point to Eagle."
            
            voice "audio/voice/E2/D5/S1/mec1m/20.ogg"
            mec1m "Wait here."
            show guard extra at cc  with dissolve
            "He closes the door. {w}After a few minutes, he returns with my phone in his hand."
            
            pf "Thanks."
            voice "audio/voice/E2/D5/S1/mec1m/23.ogg"
            mec1m "Is there anything else?"
            pf "No, thanks again."
            hide guard with dissolve
            "He nods, then shuts the door."
            

    "As I walk towards the exit, I unlock my phone and am greeted by--"
    stop music fadeout 3
    pf "13 messages?"
    "They're all from Nikki… Now that I think about it, I don't remember if I saw her last night..."
    "Opening them up, I read them in succession."
    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 5
    "{i}Hello my favourite big bro! How would you feel about picking me up from megumis tonight? ^__^{/i}"
    "{i}Did you get my last text? Cooking class is almost over and I'd really like to go to hang out with megumi… she can give me a ride over but can you give me a ride home? ^__^;{/i}"
    "{i}?{/i}"
    "{i}Is that a no? ￢_￢{/i}" # eyes aren't displaying
    "{i}???{/i}"
    "{i}If you don't want to get me then you should just say so! 0_0{/i}"
    "{i}Fine I'll take the bus!!{/i}"
    "{i}Um are you mad at me? o_O{/i}"
    "{i}What did i do?{/i}"
    "{i}Whatever it is i'm sorry! T.T please dont be mad anymore!!{/i}"
    "{i}Dude why are you ignoring me?{/i}"
    "{i}Just tell me!!! ><{/i}"
    "{i}Wow okay I literally make all your meals and you can't even do this one little favour for me ;-__-{/i} "
    "{i}Stop being such a jerk! (｀ヘ´){/i}" # entire face isn't displaying
    "{i}I'm on the bus now. Thanks to SOMEONE{/i}"
    stop music fadeout 3
    "{i}Guess whose team now has a sponsor and their GEARs are already undergoing repairs!{/i}"
    "Oh, that last text was sent from Yuuna this morning before class."
    "..."
    "Well, this explains a lot. {w}No wonder Nikki was so moody this morning. I'm sure once I tell her it was all a misunderstanding she'll be fine."
    
    "I shoot my team a text: {w}{i}GEARs are undergoing repairs! Meet in the hangar in 2 hours{/i}."
    
    stop ambient fadeout 3
    scene bg campus lounge day with fade
    play ambient "audio/ambience/Pilot Lounge.ogg" fadein 5
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
    
    "Now that that's taken care of, I still have a lot of time to kill. I wonder what I should do."
    
    #Afternoon choice
    $ freeTime = "afternoon"
    
    call E2FreeTime from _call_E2FreeTime_1
    
    jump E2D5S2
