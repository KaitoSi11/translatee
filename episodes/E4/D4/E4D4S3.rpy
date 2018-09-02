#
label E4D4S3:
    
    $ akiOut = "sUniform"
    
    $ shoOut = "sUniform"
    
    $ kaoOut = "sUniform"
    
    $ mayOut = "sUniform"
    
    #(label match end convergence)
    play sound "audio/sfx/GEAR/GEAR Boot Up 2.ogg"
    "With the match finished, GEAR controls are restored."
    voice "audio/voice/E4/Announcer/D4/14.ogg"
    an "I think we can all agree that this was the best pre-season match bar none. Am I right?!"
    # sfx ?
    "The stadium thunders approval."
    voice "audio/voice/E4/Announcer/D4/15.ogg"
    an "We'll have the replays available later today! For now, I'll have to ask our contenders to leave the arena so the next match can begin."
    "Before shuffling out of the arena, Phoenix gives us a saluted wave."
    scene black with fade
    
    if E4D4S2_WonDuel == 1:
        stop music fadeout 5
    
    if E4D4S2_WonDuel == 0:
        "Despite losing, Akira was still depowered. Considering what he usually does to his opponents, I don't think I fared too badly."
    
    "Speaking of Phoenix, how was it also equipped with the overdrive mode? An uneasiness settles in the pit of my stomach as we return our GEARs back to the hangar and make our way to the pre-combat room."
    scene bg campus battleroom day with fade
    "I quickly change back into my uniform as questions keep swirling around in my mind. When I enter the pre-combat room, I am alone. My teammates must still be changing."
    #play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 5
    
    if E4D4S2_WonDuel == 1:
        "I try and collect my thoughts but they're just as scattered as before. I barely register my teammates' arrival."
        play music "audio/music/Let's Get It Done! (GAME VERSION).ogg" fadein 5
        show shou hap at cc with dissolve
        "Shou suddenly throws an arm around me and pulls me close, nearly choking me."
        show exclamation:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Shou/d4/22 Copy.ogg"
        ss "You were awesome out there!"
        pf "Thanks..."
        show kaori smi at l3
        show mayu smi at r3:
            xzoom -1
        with dissolve
        "I want to share in Shou's jubilation, but I can't stop thinking about how another GEAR other than Eagle was able to go into overdrive, if only for a short while."
        voice "audio/voice/E4/Mayu/D4/Mayu D4-16.ogg"
        ma "I can't believe we beat Akira and his team!"
        "Mayu's cheeks are flushed with excitement and she wears a small smile."
        voice "audio/voice/E4/Kaori/D4/Kaori_D4_27.ogg"
        ki "We got lucky we won this time. It was a really close call."
        show shou mis
        voice "audio/voice/E4/Shou/d4/23 Copy.ogg"
        ss "Aw, come on, Kaori. We {i}won{/i} against {i}Akira{/i}! No matter how close a call it was we still beat the number 1 team at ACE!"
        show kaori neu
        voice "audio/voice/E4/Kaori/D4/Kaori_D4_28.ogg"
        ki "That may be true, but they're still the number one seeded team."
        show mayu hap
        voice "audio/voice/E4/Mayu/D4/Mayu D4-17.ogg"
        ma "With this victory, we should at least solidify a position in the top three!"
        show kaori mis
        voice "audio/voice/E4/Kaori/D4/Kaori_D4_29.ogg"
        ki "I suppose that's true too…"
        "She lets a smile escape, but clearly there's still something on her mind."
        show kaori ske
        voice "audio/voice/E4/Kaori/D4/Kaori_D4_30.ogg"
        ki "But isn't anyone else concerned by Akira's overdrive ability?"
        show mayu neu
        show shou neu
        pf "Yes, I've been trying to figure that out. As far as I know, only Dad understood that kind of technology so how the hell did Akira get ahold of it?"
        show kaori neu
        voice "audio/voice/E4/Kaori/D4/Kaori_D4_31.ogg"
        ki "If he knew about this then he's got a lot of questions to answer."
        voice "audio/voice/E4/Mayu/D4/Mayu D4-18.ogg"
        ma "He never used it any previous battles so this must be a recent addition."
        pf "I need to talk to him."
        "Shou nods."
        "I'm glad my teammates understand. With all these questions floating around in my mind, I can't enjoy our win."
        show shou smi
        voice "audio/voice/E4/Shou/d4/24 Copy.ogg"
        ss "Alright, you go take care of business first. But don't forget, today you are still a winner!"
        
        menu:
            "It doesn't feel like a win.":
                "I give Shou a weak smile."
                pf "Thanks, but it's hard to focus on that when all I can think about is how Akira got ahold of this technology. Not to mention we played against their subs."
                show shou mis
                voice "audio/voice/E4/Shou/d4/25 Copy.ogg"
                ss "They're still team REBORN. Although it's pretty disconcerting about the whole Phoenix overdrive thing, I'm sure he'll be able to explain it."
                pf "That's what I'm hoping."
                "Akira's not a bad guy, after all. I'm sure he'll be helpful."
            
            "We are the champions!":
                pf "As soon as I get all of this figured out we are going to celebrate properly."
                show shou mis
                voice "audio/voice/E4/Shou/d4/26 Copy.ogg"
                ss "We'll be waiting for you!"
            
            "I could have done better.":
                pf "The only reason we won is because my overdrive mode outlasted Akira's."
                show shou mis
                "Shou shrugs."
                voice "audio/voice/E4/Shou/d4/27 Copy.ogg"
                ss "That's all part of the battle. It's still a win and you deserved it."
        
        pf "I'm going to see if I can still catch up with Akira."
        show kaori smi
        show mayu smi
        "The team nods and I head towards the Hangar."
    
    else:
        "I'm still trying to process what just happened. Somehow, Phoenix was able to match Eagle in overdrive mode. Even though his GEAR could only hold that energy expenditure for a little while, his core was definitely based on my core's design."
        "I barely notice my team's arrival. We sit in silence until Kaori voices what we've all been thinking."
        #play music "audio/music/Next Time (GAME VERSION).ogg" fadein 5

        show shou neu at cc with dissolve
        show kaori ske at l3
        show mayu neu at r3:
            xzoom -1
        with dissolve
        show question:
            xoffset 230
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Kaori/D4/Kaori_D4_32.ogg"
        ki "What the hell was that?"
        show shou thi
        voice "audio/voice/E4/Shou/d4/28 Copy.ogg"
        ss "Whatever it was, it was unexpected."
        pf "It was a lesser version of Eagle's overdrive."
        show mayu wor
        show shou neu
        voice "audio/voice/E4/Mayu/D4/Mayu D4-19.ogg"
        ma "Akira's never been able to do that before..."
        pf "No one besides Eagle has been able to do that before."
        show kaori thi
        voice "audio/voice/E4/Kaori/D4/Kaori_D4_33.ogg"
        ki "Then how was he suddenly able to get his hands on that technology?"
        pf "That's exactly what I intend to find out. As far as I know, Dad was the only person who had knowledge of how to build the overdrive mode."
        show shou thi
        show mayu ner
        "I look over at the grave faces of my team members. They wear a varying mix of disappointment and anger. I hadn't realised how much we'd depended on my core's secret weapon, and having that wild card thrown back at us hits us extra hard."
        pf "Sorry guys, but I have to find Akira."
        show mayu neu
        voice "audio/voice/E4/Mayu/D4/Mayu D4-20.ogg"
        ma "We understand."
        show shou neu
        show kaori neu
        "Kaori nods."
        voice "audio/voice/E4/Kaori/D4/Kaori_D4_34.ogg"
        ki "Go. You should hurry before he leaves."
        "I nod, and head towards the Hangar."
        
    stop music fadeout 3
    stop ambient fadeout 3
    scene black with fade
    play ambient "audio/ambience/Hangar.ogg" fadein 3
    scene bg campus hangar day with fade
    "Luckily, Akira is still there."
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
    pf "Akira!"
    show akira smi at cc with dissolve
    "He turns at the sound of his name and flashes me a smile."
    
    if E4D4S2_WonDuel == 1:
        voice "audio/voice/E4/Akira/D4/1.ogg"
        am "Hey! I believe congratulations are in order."
        pf "Thanks…"
        "His smile is genuine but something about him is different."
        show note:
            xoffset 720
            yoffset 5
            xzoom .75
            yzoom .75
        show akira hap
        voice "audio/voice/E4/Akira/D4/2.ogg"
        am "It's been a long time since I've had a match that close. What a rush! That type of feeling is intoxicating, isn't it? It's the reason I want to be a professional war gamer."
        "Even though he lost, there's no bitterness in his voice. In fact, he now speaks to me as if we're equals."
        pf "Yeah, but…"
        
    else:
        voice "audio/voice/E4/Akira/D4/3.ogg"
        am "Hey, that was a great match out there."
        show akira hap
        voice "audio/voice/E4/Akira/D4/4.ogg"
        am "I'll admit, you had me a little worried for a while. I haven't had a match that close in a long time."
        show note:
            xoffset 720
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Akira/D4/5.ogg"
        am "Thanks for giving it your all today!"
        "Akira's grin is genuine and even though I lost against him, I feel like he appreciates the challenge I provided him and respects me more for it."
        pf "Sure, but…"
    
    pf "That's not why I'm here."
    show akira neu
    "His smile falters."
    voice "audio/voice/E4/Akira/D4/6.ogg"
    am "What's up?"
    pf "You went into overdrive mode during the match. How did you do that?"
    voice "audio/voice/E4/Akira/D4/7.ogg"
    am "It kicks in automatically when I'm close to getting depowered."
    "Just like what mine used to do. My jaw sets."
    pf "How did you get that technology?"
    show akira wor
    "Akira's smile drops completely at my tone."
    voice "audio/voice/E4/Akira/D4/8.ogg"
    am "It was an upgrade from Aludian. Is something wrong?"
    pf "How did they get the technology?"
    show akira ner
    voice "audio/voice/E4/Akira/D4/9.ogg"
    am "I don't know. They didn't tell me anything specific just that this GEAR was a prototype."
    show akira ske
    voice "audio/voice/E4/Akira/D4/10.ogg"
    am "I'm not sure what's going on, but I can get you in touch with them if you want."
    pf "I'd appreciate that."
    show akira neu
    voice "audio/voice/E4/Akira/D4/11.ogg"
    am "Sure."
    "He rummages through his phone and texts me a phone number."
    voice "audio/voice/E4/Akira/D4/12.ogg"
    am "Here's the number to our account manager. Maybe he'll be able to tell you."
    pf "Thanks."
    "I feel a little bad charging over and acting kind of cold towards Akira. Of course he wouldn't know what was going on. Aludian takes care of large installations like a new core. All Akira would know is how to use it."
    
    if E4D4S2_WonDuel == 0:
        pf "And I didn't get a chance to say this before but congratulations on your win."
        show akira smi
        "Akira's smile returns."
        voice "audio/voice/E4/Akira/D4/13.ogg"
        am "Thanks, but you guys definitely didn't make it easy."
        
    else:
        pf "I didn't get a chance to say this before but that was a great match back there. Towards the end I wasn't quite sure who was going to come out victorious."
        show akira smi
        "Akira's smile returns."
        voice "audio/voice/E4/Akira/D4/14.ogg"
        am "Same here. Congrats again on your win."
        pf "Thanks."
        
    show akira cur
    "Akira glances past me."
    show akira hap
    voice "audio/voice/E4/Akira/D4/15.ogg"
    am "I should get back to my team."
    hide akira with dissolve
    
    "I nod and Akira leaves. As soon as he's out of sight, I dial the Aludian contact number he gave me."
    
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(2.5)
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    $renpy.pause(1.0)
    voice "audio/voice/E4/Aludian Manager/E4/D4/1.ogg"
    alm "Hello?"
    pf "Hi, I'm [pfull], one of the pilots for ACE-2049-11."
    voice "audio/voice/E4/Aludian Manager/E4/D4/2.ogg"
    alm "Yes, I'm familiar with you and your team. How can I help you?"
    pf "I had some questions relating to Akira's core overdrive."
    voice "audio/voice/E4/Aludian Manager/E4/D4/3.ogg"
    alm "Unfortunately, I can't help you. I'm only involved in the team side of things. You'll have to talk to someone in the Tech & Engineering department."
    pf "I see. Is there a person I can get in touch with?"
    voice "audio/voice/E4/Aludian Manager/E4/D4/4.ogg"
    alm "Your best bet would be to try calling Aludian's main number and setting up an appointment."
    pf "Alright, thanks."
    voice "audio/voice/E4/Aludian Manager/E4/D4/5.ogg"
    alm "Good luck."
    
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    stop music fadeout 5
    
    "After we hang up the call, I quickly locate Aludian's number. I try to keep my irritation in check as I wait for someone to answer. Finally, I reach the receptionist, who helpfully enquires if I have an appointment or if I'd like to make an appointment."
    scene black with fade
    stop ambient fadeout 3
    "Realising I was going to get nowhere, I make an appointment to visit the office tomorrow."
    $renpy.pause(1)
    play ambient "audio/ambience/Campus.ogg" fadein 3
    scene bg campus main dusk with fade
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
    "I'm exhausted and I've made no progress with getting answers. I text my team what happened and find them waiting on the quad. Valerie and Yuuna are there too."
    show yuuna neu at l3 with dissolve:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show mayu neu at l2 behind yuuna  with dissolve:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show valerie neu at l1 with dissolve:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show kaori neu at r1 behind shou with dissolve:
        xoffset -75
        xzoom -0.75
        yzoom 0.75
    show shou neu at r3 with dissolve:
        xoffset 100
        xzoom -0.75
        yzoom 0.75
    voice "audio/voice/E4/Yuuna/E4/D4/20.ogg"
    ym "Shou got us up to speed."
    voice "audio/voice/E4/Valerie/ValE4D4/ValE4D4L1.ogg"
    vb "With how long it took me to activate your overdrive mode, Aludian has got to be working with a prototype or have access to your core's blueprints."
    pf "Those are my thoughts exactly, but how would they have gotten those schematics?"
    show valerie cur
    voice "audio/voice/E4/Valerie/ValE4D4/ValE4D4L2.ogg"
    vb "I didn't give it to them. Promise!"
    "I give her a weak grin."
    pf "Not what I was implying, but still good to know."
    show valerie neu
    voice "audio/voice/E4/Shou/d4/29 Copy.ogg"
    ss "Still, that sucks, broseph."
    "Mayu nods."
    voice "audio/voice/E4/Mayu/D4/Mayu D4-21.ogg"
    ma "I'm a little surprised the account manager doesn't know that information."
    show yuuna ner
    "Yuuna looks thoughtful."
    voice "audio/voice/E4/Yuuna/E4/D4/21.ogg"
    ym "I think for larger companies like Aludian it makes sense. The account managers are the liaison between the sponsor and the sponsee so that's their main focus. They make sure the team gets what was supposed to go to them, so they don't need to know how that item was acquired or developed in the first place."
    show yuuna neu
    voice "audio/voice/E4/Yuuna/E4/D4/22.ogg"
    ym "The only time you see a lot of interdepartmental duties is when you're with smaller companies."
    show mayu cur
    voice "audio/voice/E4/Mayu/D4/Mayu D4-22.ogg"
    ma "Does Dasshu have a similar model as Aludian?"
    show yuuna smi
    voice "audio/voice/E4/Yuuna/E4/D4/23.ogg"
    ym "Oh yes, definitely. Especially since they sponsor more than one industry."
    show mayu neu
    pf "Well, I have an appointment scheduled for tomorrow. Hopefully that'll be more successful."
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_35.ogg"
    ki "Good, it's easier to demand answers in person."
    show yuuna neu
    show shou ske
    voice "audio/voice/E4/Shou/d4/30 Copy.ogg"
    ss "Demand? Pretty sure that's how you get kicked out of a place."
    show kaori ann
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_36.ogg"
    ki "He's got to be aggressive if he wants to get any answers! Otherwise they'll keep passing him off from one person to the next."
    pf "Something weird is going on and I intend to find out what."
    show kaori neu
    "My voice holds more confidence than I feel. I can't quiet the sinking feeling in the pit of my stomach."
    show yuuna smi
    "Yuuna nods and speaks gently."
    voice "audio/voice/E4/Yuuna/E4/D4/24.ogg"
    ym "For now, you should try not to stress about it."
    show shou neu
    voice "audio/voice/E4/Shou/d4/31 Copy.ogg"
    ss "Yeah, there's not much you can do."
    pf "You're right, I know… I think I'm going to head home then."
    show yuuna neu
    stop music fadeout 5
    
    if E4D4S2_WonDuel == 1:
        pf "I don't feel much like celebrating."
        "The team murmurs their assent. The mood is completely ruined, which is too bad because this was the win we'd been waiting for. {w}Once I get to the bottom of this, I promise we will celebrate properly!"
        
    else:
        "Everyone agrees. Mayu and Kaori look equally exhausted and even Shou doesn't have as much energy as usual. Valerie's been unusually quiet and Yuuna looks solemn. This loss weighs heavy on everyone."
        
    scene black with fade
    stop ambient fadeout 3
    "We say our goodbyes and I head to the parking lot. Then I hop on my bike and head home."
    
    jump E4D4S4
