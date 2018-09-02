label E1D2S11:
    
    if (E1D2S9_AgreeJoinShouTeam == 0):
        "With no other options, I look around the lounge for Shou. He'd mentioned that his team needed another member… Hopefully that's still the case."
        play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
        "I see him standing with two girls at the opposite end of the room. One girl, with bright red hair, stands to the side and talks quickly on her phone. The other girl with dark hair shuffles her feet while Shou chats animatedly to her." 
        pf "Hey, Shou!" 
        show shou cur at cc with dissolve
        "He turns towards me as I approach."
        show shou smi at cc
        voice "audio/voice/E1/D2/S11/Shou/1.ogg"
        ss "Hey, broseph! What's up?" 
        pf "I was just wondering if your offer was still open."
        show shou hap at cc
        voice "audio/voice/E1/D2/S11/Shou/2.ogg"
        ss "To join? Hell yeah! No luck finding another team?" 
        pf "Nope. You were right about it being tough."
        show shou smi at cc
        voice "audio/voice/E1/D2/S11/Shou/3.ogg"
        ss "Cool, well, here is the rest of the team."
        show kaori thi at r3 with dissolve
        show mayu ner at l3 with dissolve
        show shou hap at cc
        show dots:
            xoffset 230
            yoffset 135
            xzoom .75
            yzoom .75
        show storm:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        "He gestures towards the dark haired girl, who stares at her feet, while the redhead continues chatting on her phone." 
    
    elif (E1D2S9_AgreeJoinShouTeam == 1):
        "Shou talks the entire way to the lounge. He's constantly interrupting himself and going off on tangents, so I only catch about half of what he's saying. We navigate the tunnels, and eventually, reach the exit. Shou opens the door and ushers me through with a small flourish."
        play ambient "audio/ambience/Pilot Lounge.ogg"
        scene bg campus lounge day with fade
        play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
        "The lounge is filled with groups of pilots. I guess everyone is catching up with their team. Shou squeezes between the groups, and I follow him towards the back corner of the room."
        show shou smi at cc with dissolve
        "He pauses in front of two girls."
        show kaori thi at r3 with dissolve
        show mayu ner at l3 with dissolve
        show shou hap at cc
        show dots:
            xoffset 230
            yoffset 135
            xzoom .75
            yzoom .75
        show storm:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        "The one with dark hair stares at her feet as soon as she notices Shou, while the one with red hair continues chatting on her cellphone."
    
    if (E1D2S4_MayuGaveDirections == 1):
        "Hm, that girl with the dark hair looks familiar…"
        show shou smi at cc
        "Ah! Of course!"
        pf "Oh hey, thanks for giving me directions to the hangar earlier."
        show mayu cur at cc
        show shou smi at l3
        with dissolve
        show exclamation:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        show mayu smi at cc with dissolve
        "She looks up in surprise and gives me a small smile of recognition."
        voice "audio/voice/E1/D2/S11/Mayu/1.ogg"
        ma "I'm glad it helped."
        pf "I hope I didn't cause you too much trouble."
        show mayu ner at cc
        "She lowers her head again and traces circles on the floor with her foot."
        voice "audio/voice/E1/D2/S11/Mayu/2.ogg"
        ma "It was no trouble at all."
        show shou cur at l3
        show question:
            xoffset 230
            yoffset 20
            xzoom .75
            yzoom .75
        "Shou glances at me and back at the girl."
        voice "audio/voice/E1/D2/S11/Shou/4.ogg"
        ss "You know each other?"
        pf "She helped me out with some directions today."
        show mayu smi at cc
        show shou hap at l3
        "She nods, and Shou breaks into a huge grin."
        voice "audio/voice/E1/D2/S11/Shou/5.ogg"
        ss "You're already friends! That's awesome!"
        pf "Not quite… I don't even know her name."
        show mayu cur at cc
        show shou smi at l3
        voice "audio/voice/E1/D2/S11/Shou/6.ogg"
        ss "Oh, well this is Mayu."
        pf "Hello, I'm [pfirst]."
        show mayu smi at cc with dissolve
        "She bows."
        voice "audio/voice/E1/D2/S11/Mayu/3.ogg"
        ma "Pleased to meet you."
    
    else:
        "Shou motions towards the dark-haired girl."
        show shou smi at cc
        voice "audio/voice/E1/D2/S11/Shou/7.ogg"
        ss "This is Mayu. She's the coolest person on this team."
        show shou mis at cc
        voice "audio/voice/E1/D2/S11/Shou/7_1.ogg"
        ss "But..uh... don't tell Kaori I said that."
        "He glances at the redhead, who isn't paying the slightest bit of attention to us."
        show shou smi at l3
        show mayu ner b1 at cc
        with dissolve
        "Mayu blushes deeply."
        voice "audio/voice/E1/D2/S11/Mayu/4.ogg"
        ma "That's not true."
        pf "It's nice to meet you, Mayu. I'm [pfirst]."
        show mayu cur at cc
        "I smile at her and hold out my hand. She wrinkles her brow in confusion, then gingerly shakes my hand… and continues to shake it."
        pf "Um…"
        show mayu ner b1 at cc with dissolve
        show shoBlush:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Mayu/5.ogg"
        ma "Sorry!"
        "She immediately drops my hand and returns her gaze to floor."
        
    show mayu neu at l3
    show shou smi at cc
    with dissolve
    show kaori thi at r3
    show shou smi at cc
    with dissolve
    if (E1D2S3_MetKaoriWasNice == 1):
        show shou hap at cc
        "Shou turns towards the redhead."
        voice "audio/voice/E1/D2/S11/Shou/8.ogg"
        ss "Hey, quit being rude!"
        show kaori neu at cc
        show shou neu at r3:
            xzoom -1
        with dissolve
        "Her gaze shifts to him and his smile falters."
        show drop:
            xoffset 1175
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Shou/9.ogg"
        ss "I mean, will you be done soon? I'd like you to meet someone."
        show kaori dis at cc
        "She frowns."
        voice "audio/voice/E1/D2/S11/Kaori/1.ogg"
        ki "I need to call you back."
        show kaori neu at cc
        "And snaps her phone shut."
        show shou smi at r3
        stop music fadeout 3
        voice "audio/voice/E1/D2/S11/Shou/10.ogg"
        ss "So, this is Kaori."
        "Something about that scowl seems familiar… especially that hair--"
        "Oh no."
        show kaori ske at cc
        play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 1
        show question:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Kaori/2.ogg"
        ki "You…"
        menu: 
            "Apologise again.":
                pf "Look, about earlier, I really am sorry--"
                show kaori ann at cc
                voice "audio/voice/E1/D2/S11/Kaori/3.ogg"
                ki "Forget it."
                "She waves her hand dismissively."
                pf "But I don't want there to be any hard feelings--"
                show kaori dis at cc
                "She stares at me and crosses her arms, as if daring me to defy her."
                show shou cur at r3
                voice "audio/voice/E1/D2/S11/Kaori/4.ogg"
                ki "I told you to forget it."
                show question:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                "Shou glances back and forth between us."
                show shou mis at r3
                voice "audio/voice/E1/D2/S11/Shou/11.ogg"
                ss "Bro, why didn't you tell me you two were already friends?"
                pf "Well, actually--"
                show kaori ang at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/5.ogg"
                ki "Shut up!"
                show mayu sad at l3
                show kaori ann at cc
                show shou sad at r3
                with dissolve
                "I instinctively pause. Who knew a girl so petite could be so terrifying."
                show shou ner at r3
                "She glares at Shou, who is already cowering and protecting his head."
                show frightful:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Shou/12.ogg"
                ss "Don't hurt me!"
                show kaori thi at cc
                "Kaori rolls her eyes."
                voice "audio/voice/E1/D2/S11/Kaori/6.ogg"
                ki "He and I are {i}not{/i} friends."
                show shou neu at r3
                voice "audio/voice/E1/D2/S11/Shou/13.ogg"
                ss "Um, okay. So, like I said, this is Kaori, and this is…"
                pf "[pfirst]."
                show shou smi at r3
                voice "audio/voice/E1/D2/S11/Shou/14.ogg"
                ss "Right."
                
            "What are the odds that we'd run into each other again…":
                pf "What are you doing here?"
                show kaori dis at cc
                "She crosses her arms."
                voice "audio/voice/E1/D2/S11/Kaori/7.ogg"
                ki "This is {i}my{/i} team--"
                show shou mis at r3
                voice "audio/voice/E1/D2/S11/Shou/15.ogg"
                ss "Well, actually, this is our--"
                show kaori ann at cc
                show shou ner at r3
                with dissolve
                "Shou flinches from Kaori's piercing glare."
                show drop:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Shou/16.ogg"
                ss "--your team. Right, carry on."
                pf "Sorry, I didn't mean it like that. I just didn't expect to see you again."
                show kaori thi at cc
                "She pauses, then shrugs."
                voice "audio/voice/E1/D2/S11/Kaori/8.ogg"
                ki "Me neither."
                show shou sur at r3 with dissolve
                show shou hap at r3 with dissolve
                "Shou's eyes widen in surprise. Then he breaks into his usual grin and slaps me--a little too forcefully--on the back."
                show shou mis at r3
                voice "audio/voice/E1/D2/S11/Shou/17.ogg"
                ss "Kaori's actually being civil towards you? Why didn't you tell me that you two were friends?"
                show kaori dis at cc
                voice "audio/voice/E1/D2/S11/Kaori/9.ogg"
                ki "We aren't. He ran into me this morning… literally."
                show shou ske at r3
                "Shou raises an eyebrow at me."
                show question:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Shou/18.ogg"
                ss "And you're still alive?"
                pf "Huh?"
                show kaori ang at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/10.ogg"
                ki "What is that supposed to mean?!"
                show mayu sad at l3
                show shou ner at r3
                "She steps towards Shou, who immediately jumps back."
                show kaori ann at cc
                show frightful:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Shou/19.ogg"
                ss "Nothing!"
                show shou smi at r3
                voice "audio/voice/E1/D2/S11/Shou/19_1.ogg"
                ss "Anyway, since you two aren't friends… This is Kaori."
                pf "I'm [pfirst]. Nice to meet you."
    
        show kaori neu at cc
        stop music fadeout 3
        "Kaori nods."
        show shou mis at r3
        voice "audio/voice/E1/D2/S11/Shou/20.ogg"
        ss "Soooo?"
        show kaori thi at cc
        "She shrugs."
        voice "audio/voice/E1/D2/S11/Kaori/11.ogg"
        ki "It's not like we have much of a choice anyway."
        show mayu neu at l3
        show shou hap at r3
        show note:
            xoffset 1175
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Shou/21.ogg"
        ss "Sweet! You're on the team, bro!"
        show kaori neu at cc
        pf "Thanks, I think."
    
    
    elif (E1D2S3_MetKaoriWasRudeNoHelmet == 1):
        stop music fadeout 3
        show shou hap at r3:
            xzoom -1
        show kaori ann at cc
        with dissolve
        "Shou is about to get the redhead's attention, when she snaps her phone shut and stomps over to us."
        play music "audio/music/Stress (GAME VERSION).ogg" fadein 1
        show kaori ang at cc
        show exclamation:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Kaori/17.ogg"
        ki "You better not be about to introduce him, Shou!"
        show mayu sad at l3
        show kaori ann at cc
        show shou ner at r3
        show panic:
            xoffset 1175
            yoffset 20
            xzoom .75
            yzoom .75
        "He hesitates."
        show shou ske at r3
        voice "audio/voice/E1/D2/S11/Shou/31.ogg"
        ss "Uh…"
        "Seriously? Out of all of the pilots in this program, I just had to run into her. What have I done to deserve this torture?"
        show kaori ang at cc
        voice "audio/voice/E1/D2/S11/Kaori/18.ogg"
        ki "He didn't even care that he nearly {i}killed{/i} me!"
        show kaori ann at cc
        "Oh. {w}Right. {w}Karma's a bitch."
        show shou ner at r3
        "I guess I could have done a little more to remedy the situation, but she's completely overreacting. "
        
        menu:
            "Suck it up and apologise.":
                "This might be my only chance to join a team. I should try to make things right… even if she is insufferable."
                pf "You're right. I didn't handle myself well back there, and I'd like to apologise for that and for endangering you."
                show kaori dis at cc
                show shou neu at r3
                with dissolve
                "Her steady glare never waivers. I glance at Shou, who nods encouragingly. {w}After a few moments, she drops her glare and steps towards me."
                show kaori thi at cc
                voice "audio/voice/E1/D2/S11/Kaori/19.ogg"
                ki "Apology {i}not{/i} accepted."
                show shou ner at r3
                voice "audio/voice/E1/D2/S11/Shou/32.ogg"
                ss "Kaori--"
                show kaori ann at cc
                voice "audio/voice/E1/D2/S11/Kaori/20.ogg"
                ki "No. Obviously he's just apologising because he needs to join a team."
                pf "I made a mistake and I want to make things right."
                show shou ske at r3
                voice "audio/voice/E1/D2/S11/Shou/33.ogg"
                ss "C'mon, Kaori, everyone deserves a second chance."
                stop music fadeout 3
                show kaori ang at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/21.ogg"
                ki "His second chance is me not reporting him to the proper authorities."
                hide kaori with dissolve
                show mayu wor at l3
                show shou thi at r3
                "With a huff, she pushes past us and into the crowd of pilots. Shou smiles apologetically to me."
                show shou neu at r3
                voice "audio/voice/E1/D2/S11/Shou/34.ogg"
                ss "Sorry, but--"
                pf "I get it."
                hide shou with dissolve
                hide mayu with dissolve
                "He gives me one last look before leaving. Mayu follows closely at his heels."
                "Well, this sucks."
                jump E1D2S12
    
            "It's too late to apologise…":
                pf "too late…"
                show kaori ske at cc
                voice "audio/voice/E1/D2/S11/Kaori/22.ogg"
                ki "What?"
                pf "Nothing.{w} Look, you aren't hurt. Can't we just put the past in the past?"
                show kaori ang at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/23.ogg"
                ki "No! Your light was red and you ran it!"
                show kaori ann at cc
                pf "It was not red!"
                show kaori ang at cc
                voice "audio/voice/E1/D2/S11/Kaori/24.ogg"
                ki "And did you not hear the part where you nearly killed me?"
                show kaori ann at cc
                pf "{i}Nearly{/i} being the key word."
                show kaori ang at cc
                voice "audio/voice/E1/D2/S11/Kaori/25.ogg"
                ki "The last thing I need on this team is another careless idiot!"
                show kaori ann at cc
                show shou ske at r3 with dissolve
                voice "audio/voice/E1/D2/S11/Shou/35.ogg"
                ss "Hey! I resent that--"
                show kaori ang at cc
                voice "audio/voice/E1/D2/S11/Kaori/26.ogg"
                ki "Shut up, Shou!"
                show kaori ann at cc
                show shou neu at r3
                "He falls silent."
                pf "This isn't entirely my fault, either. You shouldn't have started to cross so early. You should have waited for the light to turn."
                show kaori ann b1 at cc
                "Her face turns as red as her hair and her eyes grow impossibly wide."
                show kaori ang b1 at cc
                stop music fadeout 3
                show exclamation:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/27.ogg"
                ki "It {i}had{/i} turned!"
                show mayu wor at l3
                show kaori ann at cc
                show shou thi at r3
                with dissolve
                show dots:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                show dots2:
                    xoffset 230
                    yoffset 135
                    xzoom .75
                    yzoom .75
                "We aren't getting anywhere. I glance at Shou, whose face has gone pale. Even Mayu is cowering beside them. She's staring so hard at a spot on the floor I'm worried she'll burn a hole through it."
                pf "Fine. Even if I apologise now, you wouldn't believe me, so I think it's probably best if I just go."
                show kaori dis at cc
                voice "audio/voice/E1/D2/S11/Kaori/28.ogg"
                ki "That's the first intelligent thing you've said today."
                pf "Thanks for the invite anyway, Shou."
                show shou ner at r3
                voice "audio/voice/E1/D2/S11/Shou/36.ogg"
                ss "Sure…"
                hide mayu
                hide kaori
                hide shou
                with Dissolve(2.5)
                "After one last look, I walk away."
                jump E1D2S12
    
            "I'm starting to regret {i}not{/i} running you over.":
                pf "But you're not dead, are you?"
                show kaori ske at cc
                show question:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/29.ogg"
                ki "What kind of stupid question is that?"
                pf "You keep talking about how you nearly died. Well, you know what? You're not dead. In fact, you're completely fine. So there's no need to get your panties in a twist over nothing."
                show kaori ang at cc
                voice "audio/voice/E1/D2/S11/Kaori/30.ogg"
                ki "How dare you! This is not {i}nothing{/i}. In fact--"
                show kaori ann at cc
                "I raise a hand and cut her off before she can continue."
                pf "In fact, you should put the past behind you. Because let's face it, you {i}need{/i} me."
                show kaori ann b1 at cc with dissolve
                "Her face is so red I can almost see the steam blowing out of her ears."
                show kaori ang b1 at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/31.ogg"
                ki "I don't {i}need{/i} anyone, and I certainly don't need {i}you{/i}!"
                show kaori ann at cc
                pf "How many people do you have on your team again?"
                show kaori dis at cc
                "Her frown deepens and she crosses her arms but she doesn't answer."
                pf "Exactly."
                show kaori thi at cc
                voice "audio/voice/E1/D2/S11/Kaori/32.ogg"
                ki "So? We'll find someone."
                show shou neu at r3
                voice "audio/voice/E1/D2/S11/Shou/37.ogg"
                ss "But Kaori, there's no one else."
                "Shou had gotten so uncharacteristically quiet that I'd nearly forgotten about him. Even now, his voice was barely above a whisper."
                show kaori dis at cc
                voice "audio/voice/E1/D2/S11/Kaori/33.ogg"
                ki "We'll find someone."
                show shou ner at r3
                voice "audio/voice/E1/D2/S11/Shou/38.ogg"
                ss "Can't you give him another chance?"
                pf "I'm willing to put our disagreements aside and start with a clean slate. {w}Are you?"
                show kaori ann at cc
                "She pauses, then looks me straight in the eyes."
                stop music fadeout 3
                voice "audio/voice/E1/D2/S11/Kaori/34.ogg"
                ki "No."
                show shou neu at r3
                voice "audio/voice/E1/D2/S11/Shou/39.ogg"
                ss "Kaori--"
                show kaori ang at cc
                show exclamation:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/35.ogg"
                ki "Shut up, Shou!"
                show mayu wor at l3
                show kaori ann at cc
                show shou neu at r3
                with dissolve
                pf "Whatever. Thanks anyway, Shou."
                show shou ner at r3
                voice "audio/voice/E1/D2/S11/Shou/40.ogg"
                ss "Sure…"
                hide mayu
                hide kaori
                hide shou
                with Dissolve(2.5)
                "I turn and walk away, but after a short distance, I glance back and see Shou and Kaori arguing. I'll figure something out tomorrow."
                jump E1D2S12
    
    
    elif (E1D2S3_EncounteredKaori == 0):
        stop music fadeout 3
        show shou hap at cc
        "Shou turns towards the redhead."
        play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1 fadeout 1
        voice "audio/voice/E1/D2/S11/Shou/41.ogg"
        ss "Hey, quit being rude!"
        show kaori neu at cc
        show shou neu at r3:
            xzoom -1
        with dissolve
        "Her gaze shifts to him and his smile falters."
        show drop:
            xoffset 1175
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Shou/42.ogg"
        ss "I mean, will you be done soon? I'd like you to meet someone."
        show kaori dis at cc
        "She frowns."
        voice "audio/voice/E1/D2/S11/Kaori/1.ogg"
        ki "I need to call you back."
        show kaori neu at cc
        "And snaps her phone shut."
        show shou smi at r3
        voice "audio/voice/E1/D2/S11/Shou/43.ogg"
        ss "So, this is Kaori."
        show kaori ske at cc
        "She gives me a quick once over, then crosses her arms over her chest." 
        show question:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Kaori/36.ogg"
        ki "A pilot?"
        show shou mis at r3
        voice "audio/voice/E1/D2/S11/Shou/44.ogg"
        ss "Not just any pilot, but a pilot who's willing to join my team!"
        show kaori dis at cc
        voice "audio/voice/E1/D2/S11/Kaori/37.ogg"
        ki "{i}Your{/i} team?"
        show shou hap at r3
        "Her eyes narrow at Shou and he shrinks back, then wears a sheepish grin."
        voice "audio/voice/E1/D2/S11/Shou/45.ogg"
        ss "I mean {i}our{/i} team."
        show kaori neu at cc
        voice "audio/voice/E1/D2/S11/Kaori/38.ogg"
        ki "That's better."
        "She turns back towards me."
        show kaori thi at cc
        show shou smi at r3
        with dissolve
        voice "audio/voice/E1/D2/S11/Kaori/39.ogg"
        ki "Hm… I suppose you'll do. Not like we really have a choice or anything."
        menu: 
            "Well, that was easy!": 
                pf "Heh, and they said joining this team would be hard."
                show kaori dis at cc
                show shou hap at r3
                "Shou stifles a laugh, but Kaori narrows her eyes."
                voice "audio/voice/E1/D2/S11/Kaori/40.ogg"
                ki "Who's \"they\"?"
                pf "Uh, no one... just the people in my class."
                show kaori ske at cc
                voice "audio/voice/E1/D2/S11/Kaori/41.ogg"
                ki "Which class?"
                pf "Piloting 101?"
                show kaori ann at cc
                "She suddenly whirls on Shou."
                show kaori ang at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/42.ogg"
                ki "You brought me a first year?!"
                show shou mis at r3
                voice "audio/voice/E1/D2/S11/Shou/46.ogg"
                ss "No, he's just new!"
                pf "I'm a second year, but a transfer student so they're making me take Piloting 101 again."
                show kaori dis at cc
                show shou smi at r3
                with dissolve
                "She relaxes."
                voice "audio/voice/E1/D2/S11/Kaori/43.ogg"
                ki "Well, I hope you at least know how to fight. I don't want to spend forever catching you up to our level."
                pf "I can hold my own."
                show kaori thi at cc
                voice "audio/voice/E1/D2/S11/Kaori/44.ogg"
                ki "We'll see."
                show shou mis at r3
                "Shou leans in close to me and lowers his voice."
                voice "audio/voice/E1/D2/S11/Shou/47.ogg"
                ss "I think she likes you!"
                show shou smi at r3
                "If that's how she acts towards somebody she likes, then I hope I never get on her bad side."
    
            "Nice to meet you.": 
                "I extend my hand."
                pf "I'm [pfirst]. Pleased to meet you."
                show kaori neu at cc
                "She stares blankly at my hand and makes no move to take it. After a minute, I lower it. {w}Well that was awkward."
                pf "Anyway, thanks for letting me join your team. I was kind of worried I wouldn't be able to find one."
                "Shou claps me on the back."
                show shou mis at r3
                voice "audio/voice/E1/D2/S11/Shou/48.ogg"
                ss "Aren't you glad you had me to look out for you?"
                pf "Yeah, you're like my fairy godmother."
                show shou ske at r3
                show confused:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Shou/49.ogg"
                ss "Yeah!--Wait, what?"
                show kaori mis at cc
                show shou cur at r3
                with dissolve
                "Kaori snorts, surprising both of us--Shou especially. He continues to stare at her, and her frown returns."
                show kaori thi at cc
                voice "audio/voice/E1/D2/S11/Kaori/45.ogg"
                ki "What?"
                show shou smi at r3
                voice "audio/voice/E1/D2/S11/Shou/50.ogg"
                ss "I just didn't know you were able to laugh."
                "Her hands clench into fists."
                show kaori ang at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/46.ogg"
                ki "What's that supposed to mean?!"
                show shou hap at r3
                voice "audio/voice/E1/D2/S11/Shou/51.ogg"
                ss "Nothing!"
                show kaori dis at cc
                "She relaxes and refolds her arms over her chest."
                voice "audio/voice/E1/D2/S11/Kaori/47.ogg"
                ki "Just because I don't laugh at your stupid jokes doesn't mean I don't have a sense of humour."
                show shou mis at r3
                "He leans into me and lowers his voice."
                voice "audio/voice/E1/D2/S11/Shou/52.ogg"
                ss "Don't listen to her. I'm hilarious."
                    
            "You'll do too.":
                pf "When's practice?" 
                "Kaori and Shou exchange a look."
                voice "audio/voice/E1/D2/S11/Shou/53.ogg"
                ss "You're dedicated!"
                pf "Well, qualifiers are only two days away, so we need to practice as soon as possible."
                show kaori smi at cc
                "Kaori crosses her arms but her lips twitch at the side as if she's happy with my demand to practice." 
                ki "Hmm…"
        voice "audio/voice/E1/D2/S11/Shou/54.ogg"
        show note:
            xoffset 1175
            yoffset 20
            xzoom .75
            yzoom .75
        ss "Anyway, welcome to the team, bro!"
        pf "Thanks."
    
    
    elif (E1D2S3_MetKaoriWasRudeYesHelmet == 1):
        show shou hap at cc
        "Shou turns towards the redhead."
        voice "audio/voice/E1/D2/S11/Shou/65.ogg"
        ss "Hey, quit being rude!"
        show kaori ann at r3
        "She holds up her hand and stops Shou from talking." 
        voice "audio/voice/E1/D2/S11/Kaori/48.ogg"
        ki "Not now, Shou. Can't you see I'm on the phone? I'm trying to see if I can find the bastard who tried to run me over today. His bike must be in the parking lot somewhere. I'll find him!" 
        "Oh crap. She's talking about me! I should have recognised her as the girl who got in my way."
        show shou mis at cc
        stop music fadeout 3
        voice "audio/voice/E1/D2/S11/Shou/66.ogg"
        ss "But Kaori, I've got someone who can fill the final position on our team." 
        show kaori ske at cc
        show shou smi at r3:
            xzoom -1
        with dissolve
        "Kaori looks at me when Shou points my way. She gives me a quick up and down."
        play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 1
        show mayu neu at l3
        voice "audio/voice/E1/D2/S11/Kaori/49.ogg"
        ki "Who are you?" 
        menu: 
            "I'm the guy who almost ran you over. Sorry.":
                $ E1D2S11_ComingCleanAboutRunningOverKaori = 1
                pf "I'm the guy who needs to apologise to you. I think I almost ran you over this morning."
                show kaori ann at cc
                "Her eyes narrow." 
                show question:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/50.ogg"
                ki "You what?" 
                pf "Uh, yeah. I almost hit a girl at a green light."
                stop music fadeout 3
                show kaori ang at cc
                show shou cur at r3
                play music "audio/music/Stress (GAME VERSION).ogg" fadein 1
                show exclamation:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/51.ogg"
                ki "You idiot! The light was RED!"
                show kaori ann at cc
                "I clearly remember the light being green, but since I need this girl's approval to join the team I bite my tongue." 
                pf "Well, either way, I'm really sorry about that. I hope you can forgive me." 
    
            "The man of your dreams!":
                "I put on my most charming smile." 
                pf "Just some guy who's going to make all your dreams come true."
                show kaori neu at cc
                "She just stares at me." 
                show kaori ske b1 at cc
                show question:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/55.ogg"
                ki "W-What?"
                pf "You heard me."
                "I wink at her."
                voice "audio/voice/E1/D2/S11/Kaori/56.ogg"
                ki "Huh?"
                show tsuBlush:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori thi b1 at cc
                "Clearly flustered, she frowns, but doesn't seem to know what to do with herself."
                show shou hap at r3
                voice "audio/voice/E1/D2/S11/Shou/71.ogg"
                ss "He's our ticket to winning, Kaori!"
                show kaori neu at cc
                "Shou's goofy grin seems to bring Kaori back to her senses."
                show kaori mis at cc
                voice "audio/voice/E1/D2/S11/Kaori/57.ogg"
                ki "No wonder you get along so well with Shou, you're as big an idiot as he is."
                #pf and Shou speak at the same time
                show shou mis at r3
                "Both of us" "Hey!"
                show shou cur at r3
                show exclamation:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                "We speak simultaneously and glance at each other in surprise."
                show kaori dis at cc
                "Kaori looks between me and Shou and lets out a long, exasperated sigh." 
    
            "I'm new.":
                pf "I'm a transfer student." 
                show kaori dis at cc
                "Kaori plants her hands on her hips and gives me a once over."
                show kaori ske at cc
                voice "audio/voice/E1/D2/S11/Kaori/59.ogg"
                ki "Hm… Where did you transfer from?" 
                pf "CINY in the States."
                show kaori neu at cc
                "She continues to stare at me."
                show kaori ske at cc
                show question:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/60.ogg"
                ki "Have we met before?"
                "My heart pounds in my chest. She can't know it's me, right? I'm pretty sure I wore my helmet. {w}Or did I?"
                pf "Um, no."
                show kaori neu at cc
                "She narrows her eyes, but eventually nods." 
    
        if (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
            show shou ske at r3
            show question:
                xoffset 1175
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S11/Shou/67.ogg"
            ss "Do you guys know each other?" 
            show kaori ang at cc
            show vein:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S11/Kaori/52.ogg"
            ki "This jerk tried to kill me today! How could you bring him to join our team?"
            show mayu sad at l3
            show kaori ann at cc
            pf "I didn't try to kill you!" 
            show kaori dis at cc
            voice "audio/voice/E1/D2/S11/Kaori/53.ogg"
            ki "Then why did you run that red light? There's no way I'd ever let you join my team."
            show shou neu at r3
            voice "audio/voice/E1/D2/S11/Shou/68.ogg"
            ss "But Kaori, we need another member."
            show kaori ann at cc
            stop music fadeout 3
            voice "audio/voice/E1/D2/S11/Kaori/54.ogg"
            ki "We'll find someone. Anyone but him."
            show shou thi at r3
            "Shou gives me an apologetic smile." 
            voice "audio/voice/E1/D2/S11/Shou/69.ogg"
            ss "Sorry…"
            show mayu sad at l3
            pf "Don't worry about it."
            show shou ner at r3
            voice "audio/voice/E1/D2/S11/Shou/70.ogg"
            ss "Guess I'll see you around."
            hide mayu
            hide kaori
            hide shou
            with Dissolve(2.5)
            "I nod, then leave. I don't know why I thought telling her who I was would be a good idea." 
            jump E1D2S12
    
        else:
            show kaori dis at cc
            "Kaori folds her arms over her chest."
            voice "audio/voice/E1/D2/S11/Kaori/58.ogg"
            ki "You're lucky we need another team member."
            show shou hap at r3
            show mayu hap at l3
            "Shou grins, and claps me on the back."
            show note:
                xoffset 1175
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S11/Shou/73.ogg"
            ss "Welcome aboard!" 
            show shou smi at r3
            pf "Looking forward to it." 
    
    show kaori neu at r3
    show shou hap at cc
    with dissolve
    stop music fadeout 3
    voice "audio/voice/E1/D2/S11/Shou/22.ogg"
    ss "So, you're probably wondering why we need another member."
    #Day Out or Open Road here
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
    show mayu neu at l3
    "Actually, I hadn't, but now that he mentioned it…"
    pf "Yeah, kind of."
    show shou mis at cc
    voice "audio/voice/E1/D2/S11/Shou/23.ogg"
    ss "Basically, Kaori and I were part of this super awesome team, but then they stopped being awesome so we left."
    show kaori ske at r3
    voice "audio/voice/E1/D2/S11/Kaori/12.ogg"
    ki "Wow, Shou, for once, you didn't ramble."
    show shou cur at cc
    "He feigns offense."
    show shou ner at cc
    show crying:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S11/Shou/24.ogg"
    ss "You wound me! All of my stories are brief."
    show shou hap at cc
    voice "audio/voice/E1/D2/S11/Shou/24_1.ogg"
    ss "Remember when I told you about my one birthday where everyone showed up wearing the same clothes as me?"
    "He turns to me."
    show shou mis at cc
    voice "audio/voice/E1/D2/S11/Shou/25.ogg"
    ss "Actually, it's a pretty good story. So, basically, I grew up in this kind of--Mayu knows where I'm talking about--"
    show kaori dis at r3
    voice "audio/voice/E1/D2/S11/Kaori/13.ogg"
    ki "Don't encourage him!"
    show mayu smi at l3
    "Mayu smiles faintly."
    show kaori neu at r3
    voice "audio/voice/E1/D2/S11/Kaori/14.ogg"
    ki "Anyway, the point is, we used to be on a team but left because the team was turning into something we didn't agree with."
    show shou smi at cc
    voice "audio/voice/E1/D2/S11/Shou/26.ogg"
    ss "Except Mayu. She's a first year."
    pf "Oh! I didn't know that."
    show shou hap at cc
    voice "audio/voice/E1/D2/S11/Shou/27.ogg"
    ss "Yeah! She got a whole bunch of invites to other teams but decided to join us. We're pretty lucky to have her."
    pf "How come you chose this team?"
    show mayu thi b1 at l3 with dissolve
    show dots:
        xoffset 230
        yoffset 135
        xzoom .75
        yzoom .75
    "Mayu shifts uncomfortably under my gaze."
    voice "audio/voice/E1/D2/S11/Mayu/7.ogg"
    ma "I trust Shou."
    "I wait for her to say more, but she doesn't."
    show shou smi at cc
    show kaori dis at r3
    "Kaori taps her foot impatiently."
    voice "audio/voice/E1/D2/S11/Kaori/15.ogg"
    ki "So, now that you know all that. Are you in?"
    "They're all a little strange in their own way, but I think I can learn to get along with them… even Kaori."
    $ E1D2S11_JoinedTheTeam = 1
    pf "Yeah, I'm in."
    show shou hap at cc
    voice "audio/voice/E1/D2/S11/Shou/28.ogg"
    ss "Great!"
    show kaori thi at r3
    "Kaori checks her phone."
    show kaori neu at r3
    show exclamation:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S11/Kaori/16.ogg"
    ki "I've spent too much time talking to you and I need to get home."
    hide kaori with dissolve
    "With a short wave, she heads out."
    show shou smi at cc
    voice "audio/voice/E1/D2/S11/Shou/29.ogg"
    ss "We should get going too."
    show mayu smi at l3
    "Mayu nods."
    pf "Yeah, me too."
    show shou mis at cc
    voice "audio/voice/E1/D2/S11/Shou/30.ogg"
    ss "We'll see you tomorrow?"
    pf "Yeah, see you."
    hide mayu
    hide shou
    with dissolve
    "We wave good bye and go our separate ways."
    
    
        
    jump E1D2S12
