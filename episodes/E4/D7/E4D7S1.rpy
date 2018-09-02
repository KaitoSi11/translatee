#
label E4D7S1:
    
    $ nikOut = "date"
    
    $ kenOut = "barista"
    $ kenDirt = 1
    
    if valrelatonship == 1 or yuurelatonship == 1 or kaorelatonship == 1 or mayrelatonship == 1:
        scene bg homekaito myroom dusk with fade
        "It's late by the time I reach home. As soon as I do, I head straight for my room and collapse onto the bed. I couldn't have asked for a better day yesterday, but there's something comforting about coming back to my own bed."
        stop music fadeout 5
        scene black with fade
        $renpy.pause(2.0)
        play sound [ "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg" ]
        play sound2 [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
        "As my eyelids begin to droop, my phone rings, jolting me back awake."
        scene bg homekaito myroom dusk with fade
        "It's a call from Nikki…"
    
    else:
        $renpy.pause(1.0)
        play ambient "audio/ambience/Morning.ogg" fadein 3
        $renpy.pause(2.5)
        scene bg homekaito myroom day with fade
        "The morning sun gently pulls me out of sleep. I yawn and stretch feeling fully rested. After my roller coaster of a day yesterday--actually, make that my roller coaster of a week--I'm just happy to finally have a day to relax!"
        "I take my time getting out of bed, and when I check the time, I realise it's already past noon."
        "Good thing there's nowhere I need to be. Shrugging it off, I get lost in the deep recesses of the internet."
        stop ambient fadeout 3
        $renpy.pause(2.0)
        scene bg homekaito myroom dusk with Dissolve(2.0)
        stop music fadeout 5
        "Before I know it, the day has passed. Doing nothing can sure be exhausting!"
        play sound [ "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg" ]
        play sound2 [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
        "As I'm about to go into the kitchen to grab a snack, my phone rings. {w}It's a call from Nikki… now that I think about it, I haven't seen her all day."
        
    stop sound
    stop sound2
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    "Of course I answer."
    pf "Hello?"
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_601.ogg"
    sf "Thank god you're home!"
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 3
    "She speaks quickly and seems almost out of breath."
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_602.ogg"
    sf "Can--ick me up fro--ore?"
    "Her voice is garbled and I can hardly make out what she's saying."
    pf "What?"
    "She pauses and there's a lot of movement on the phone before she speaks again."
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_603.ogg"
    sf "Please, can you get me?"
    pf "Where are you?"
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_604.ogg"
    sf "At the bookstore."
    "Her voice is clearer but she sounds scared." 
    
    $ E4D7S1_Bus = 0
    
    menu:
        "Be there in a min.":
            "Something doesn't seem right…"
            pf "Alright, I'll be there in a few minutes."
            "Nikki sighs in relief."
            voice "audio/voice/E4/Nikki/Day 6/Nikki_04_605.ogg"
            sf "Thanks."
        
        "What's wrong with the bus?":
            $ E4D7S1_Bus = 1
            pf "Are you okay? Why can't you take the bus?"
            voice "audio/voice/E4/Nikki/Day 6/Nikki_04_606.ogg"
            sf "I missed it and the next one doesn't come for another hour."
            voice "audio/voice/E4/Nikki/Day 6/Nikki_04_607.ogg"
            sf "Can you just come get me? Please?!"
            "The urgency in her voice makes me uneasy. I better make sure everything's okay."
            pf "Fine, don't move."
            "She sighs in relief."
            voice "audio/voice/E4/Nikki/Day 6/Nikki_04_608.ogg"
            sf "Okay, thanks."
            
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    scene black with fade
    "We hang up the phone and I hurry back to my bike. Nikki would tell me if she were in danger… {w}wouldn't she? I try not to dwell on the thought but pick up speed anyway."
    scene bg campus intersection night with fade
    "Luckily, traffic is on my side and I arrive a few minutes earlier than anticipated. Nikki waits for me beneath a street lamp a few feet away from the bus stop."
    "I can make out Ken's dark mop of hair beside her. It's a little strange that she's not under the bus awning… and what's Ken doing there?"
    "Nikki straightens up as I slow down. Flecks of blood stains her clothes and dark bruises mark her skin. Ken steps into the light to greet me, and I wince when I see him."
    "His left eye and cheek is puffy and starting to turn purple. Blood drips down his face from a cut at his temple. He must have tried to clean it because his forehead is smeared with streaks of red."
    "What the hell happened here?! I park my bike and rush over to them."
    show nikki sur at cc with dissolve
    "Nikki throws her arms around me and hugs me tightly."
    show nikki wor
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_609.ogg"
    sf "I'm so glad you're here!"
    pf "Oh my god, Nikki! Are you okay?"
    show nikki sad
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_610.ogg"
    sf "Yeah, I'm fine."
    pf "You're bleeding!"
    stop music fadeout 5
    show nikki wor
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_611.ogg"
    sf "No, the blood's not mine."
    pf "Is it Ken's?"
    voice "audio/voice/E4/Ken/E4/D7/01.ogg"
    ky "No."
    hide nikki with dissolve
    
    show nikki sad at l2
    show ken neu at r2:
        xzoom -1
    with dissolve
    play music "audio/music/Next Time (GAME VERSION).ogg" fadein 5
    pf "You look like hell."
    show drop:
        xoffset 1040
        yoffset 100
        xzoom .75
        yzoom .75
    show ken smi
    "He tries to smile then dabs at his swollen lip, his finger now stained with fresh blood. He holds himself stiffly and leans on the lamppost for support."
    show ken neu
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_612.ogg"
    sf "He saved me from those guys!"
    pf "What guys?"
    show nikki dis
    show ken dis
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_613.ogg"
    sf "I don't know. There was a group of them--three, I think--waiting for the bus. And when I showed up they started saying all these {i}things{/i} about me."
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_613_01.ogg"
    sf "They were being so gross and creepy but I tried to ignore them because I figured the bus would be there soon and it wouldn't matter."
    show nikki ner
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_613_02.ogg"
    sf "And then one of the guys tried to put his arm around me and I freaked out and I guess I pushed him and he got really angry! And then the other guy grabbed me--"
    "My blood runs cold."
    pf "He what? Did he hit you? Are you hurt?"
    show nikki dis
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_614.ogg"
    sf "N-No…"
    show ken neu
    "Nikki's voice trembles and her eyes glitter with tears. I'm about to pull her back into a hug when Ken slips his hand into hers and squeezes."
    show nikki thi
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_614_01.ogg"
    sf "Ken intervened before anything could have happened."
    "She glances at Ken, smiling broadly."
    show nikki neu
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_614_02.ogg"
    sf "He came barrelling out of the bookstore screaming at that guy to let me go and then he punched him right in the face!"
    show nikki sur
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_615.ogg"
    sf "The guy was super angry and he and his friends ganged up on him."
    show ken neu
    pf "How did you get your bruises then?"
    show nikki sad
    "She frowns."
    show drop:
        xoffset 365
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_616.ogg"
    sf "I tried to stop them from ganging up on Ken."
    pf "You what?! What were you thinking joining the fight? You could have been seriously injured!"
    show nikki dis
    "Nikki sets her jaw."
    voice "audio/voice/MISSING/BATCH7/Nikki_final_missed03.ogg"
    sf "There was no way I was going to let Ken fight them alone… especially not when this fight only happened because of me!"
    "I'm too stunned by her outburst to reply. Of course I'm not pleased that she put herself in danger, but a part of me is also a little proud."
    show nikki thi
    voice "audio/voice/MISSING/BATCH7/Nikki_final_missed04.ogg"
    sf "But... I didn't really need to help..."
    "I raise an eyebrow."
    show nikki dis
    voice "audio/voice/MISSING/BATCH7/Nikki_final_missed05.ogg"
    sf "Ken beat two of them up by himself. The third one had to help them up so they could escape."
    #stop music fadeout 5
    pf "...What?"
    "I look skeptically at Ken. I wouldn't say he's scrawny, but he's no muscleman either."
    show dots:
        xoffset 1040
        yoffset 100
        xzoom .75
        yzoom .75
    show ken ner
    "Ken shifts nervously. I think I still make him uncomfortable."
    #play music "audio/music/Evening Out (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E4/Ken/E4/D7/02.ogg"
    ky "I have some experience with martial arts..."
    show nikki cur
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_618.ogg"
    sf "What do you mean \"some\" experience? You're a second dan black belt!"
    "He's a what?! I certainly was not expecting that."
    pf "You threw yourself in harms way to protect Nikki?"
    show nikki cur
    show ken ann
    voice "audio/voice/E4/Ken/E4/D7/03.ogg"
    ky "Of course!"
    #show ken neu

    show nikki neu b2 with dissolve
    "Ken maintains eye contact and answers with conviction. Nikki blushes."
    show nikki thi b1 with dissolve
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_619.ogg"
    sf "A-Anyway, I told Ken he should go back inside but he refused."
    voice "audio/voice/E4/Ken/E4/D7/04.ogg"
    ky "It's not safe for her to wait alone."
    "I take another look at the Ken."
    show nikki neu
    
    menu:
        "Respect.":
            "There's a fire in his eyes I'd never noticed before. When he looks at Nikki, he isn't that timid kid trembling in his boots. He looks like someone who's willing to move mountains."
            "I meet his eyes and nod."
            pf "Thanks for being there for her."
            show exclamation:
                xoffset 1040
                yoffset 100
                xzoom .75
                yzoom .75
            show ken cur b1
            "He blinks in surprise but nods back."
            show ken ner
            voice "audio/voice/E4/Ken/E4/D7/05.ogg"
            ky "I only did what anyone would have done."
            show nikki cur
            voice "audio/voice/E4/Nikki/Day 6/Nikki_04_620.ogg"
            sf "Don't be so modest! You were amazing out there!"
            show ken smi with dissolve
            show drop:
                xoffset 1040
                yoffset 100
                xzoom .75
                yzoom .75
            show ken win
            show nikki wor
            with dissolve
            "Ken shrugs awkwardly, then winces in pain."
        
        "No way he fought off three guys alone.":
            pf "Seriously? Three against one though?"
            show nikki cur
            voice "audio/voice/E4/Nikki/Day 6/Nikki_04_621.ogg"
            sf "Yes! He was just like one of those superheros swooping in at the last minute to save the day!"
            show ken neu
            voice "audio/voice/E4/Ken/E4/D7/06.ogg"
            ky "I'm not sure how heroic it is to get a black eye."
            "If this is how he looks after \"winning\" the fight, I wonder what condition he left the other two in."
            pf "Fighting those guys by yourself was not the smartest move…"
            show ken ann
            voice "audio/voice/E4/Ken/E4/D7/07.ogg"
            ky "It was the only way to keep Nikki safe. If I had called for help, it would have only delayed things and I couldn't take that risk!"
            "His determination is admirable. Maybe I misjudged him."
            pf "Fair enough."
            show ken cur with dissolve
            show drop:
                xoffset 1040
                yoffset 100
                xzoom .75
                yzoom .75
            show ken win 
            show nikki wor
            with dissolve
            "He blinks in surprise, but nods. Then winces in pain."
        
        "I should have been here.":
            "I'm glad that someone was there for her, but I can't stop that nagging feeling that I've failed my sister. I didn't even know she was in town today."
            
            if valrelatonship == 1 or yuurelatonship == 1 or kaorelatonship == 1 or mayrelatonship == 1:
                 "Or that she hadn't returned home when I got back."
                 
            if E4D7S1_Bus == 1:
                "I almost didn't come to get her when she called!"
                
            "Ken was here for Nikki when I wasn't. I can't ignore that. Maybe he's not as bad as I thought."
            pf "I'm sorry, Nikki. I should have been there for you, but I'm glad that Ken was."
            "I look him in the eyes."
            pf "Thank you."
            show ken cur with dissolve
            $renpy.pause(1)
            show drop:
                xoffset 1040
                yoffset 100
                xzoom .75
                yzoom .75
            show ken win with dissolve
            "He blinks in surprise, but nods. Then winces in pain."
    
    show nikki dis
    pf "Are you sure you're okay, though? Maybe we should take you to the hospital."
    show ken neu
    "He shakes his head."
    voice "audio/voice/E4/Ken/E4/D7/08.ogg"
    ky "I'm fine. Nothing's broken."
    "I look him over."
    pf "Uh, I don't know about that…"
    show nikki ner
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_622.ogg"
    sf "I told him we should call an ambulance but he refused."
    show ken ner
    voice "audio/voice/E4/Ken/E4/D7/09.ogg"
    ky "I promise I'm okay. I'm sorry for causing you such trouble."
    "This is one of those rare times I wish my bike could fit more people."
    pf "Do you at least have a ride home?"
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_623.ogg"
    sf "He let me call his brother to come pick him up."
    pf "We'll wait here with you until he arrives."
    show ken neu
    voice "audio/voice/E4/Ken/E4/D7/10.ogg"
    ky "I appreciate the thought, but I would feel more at ease if you took Nikki home."
    
    menu:
        "I insist.":
            show nikki wor
            "Nikki shakes her head."
            voice "audio/voice/E4/Nikki/Day 6/Nikki_04_624.ogg"
            sf "What if they come back?"
            show ken thi
            voice "audio/voice/E4/Ken/E4/D7/11.ogg"
            ky "I know my brother will be here in a few minutes."
            pf "I can afford to wait a few minutes."
            show exclamation:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Nikki/Day 6/Nikki_04_625.ogg"
            sf "Me too!"
            "I glance at the dimly lit bookstore."
            pf "Is the bookstore still open? Maybe we can wait inside there."
            show ken neu
            voice "audio/voice/E4/Ken/E4/D7/12.ogg"
            ky "They're probably in the middle of closing."
            show nikki neu
            voice "audio/voice/E4/Nikki/Day 6/Nikki_04_626.ogg"
            sf "I'm sure your coworkers will let you back in. They're probably wondering what happened to you anyway."
        
        "Offer to walk him back into the bookstore.":
            pf "If you don't want us to wait with you, will you at least let us walk you back into the bookstore? It should be safer in there."
            show nikki neu
            voice "audio/voice/E4/Nikki/Day 6/Nikki_04_626.ogg"
            sf "I'm sure your coworkers will let you back in. They're probably wondering what happened to you anyway."
    
    pf "You work there?"
    show ken ner
    "Ken nods."
    pf "Then let's definitely get you back inside."
    show ken neu
    "Realising he's fighting a losing battle, Ken agrees."
    voice "audio/voice/E4/Ken/E4/D7/13.ogg"
    ky "Okay."
    stop music fadeout 4
    hide ken
    hide nikki
    with dissolve
    "Nikki and I go to support him but he manages to walk by himself. As we head into the bookstore, his coworkers rush out to help, each asking questions about what happened."
    
    jump E4D7S2
