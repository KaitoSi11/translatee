label E1D4S5:
    show mayu hap at l3 with dissolve
    show kaori neu at r3 with dissolve:
            xzoom -1
    show shou hap at cc with dissolve
    if (E1D4S4_FollowMatchPlan == 1):
        play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 1
        "За ареной Сё похлоапл меня по спине, чуть не выбив из равновесия. Даже Маю пожала мне руку. Каори стояла позади, выглядя необычайно задумчивой." 
        voice "audio/voice/E1/D4/S5/Shou/2.ogg"
        show note:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        ss "Это юыло удивительно! Ты там полностью нас спас, братан!" 
        pf "Спасибо!"
        show kaori thi at r3
        show mayu smi at l3
        voice "audio/voice/E1/D4/S5/Kaori/1.ogg"
        ki "Ты был хорош, но только потому, что мы сильно тебе помогли."
        show shou mis at cc
        voice "audio/voice/E1/D4/S5/Shou/3.ogg"
        ss "Ты шутишь? Мы трое выбили двух. Он выбил двоих в соло. Ты должна признать, что он был более чем \"хорош\"."
        show kaori neu at r3
        voice "audio/voice/E1/D4/S5/Kaori/2.ogg"
        ki "По крайней мере ты придерживался плана." 
    
        menu: 
            "Конечно придерживался." :
                pf "Мы ведь договорились об этом ранее."
                show kaori mis at r3
                voice "audio/voice/E1/D4/S5/Kaori/3.ogg"
                ki "Ну, теперь мы знаем, что ты можешь следовать указаниям. Это более чем я могу сказать для Сё."
                show shou thi at cc
                show drop:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S5/Shou/4.ogg"
                ss "Эй!"
    
            "Это потому что я чувствителен к твоим потребностям." :
                pf "Это ведь то, чего ты хотела, не так ли?"
                show kaori ske at r3
                voice "audio/voice/E1/D4/S5/Kaori/4.ogg"
                ki "Ну, да."
                "Я ухмыльнулся."
                pf "Видишь? Я знаю, чего хотят девушки."
                show kaori dis at r3
                show mayu cur at l3
                show shou hap at cc
                show dots:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                "Каори скрестила руки, показывая что её не позабавило, хотя Сё смеялся."
    
            "Это был тупой план." :
                pf "Мы бы справились лучше, если бы я не был в стороне в самого начала."
                show kaori dis at r3
                "Каори нахмурилась."
                voice "audio/voice/E1/D4/S5/Kaori/5.ogg"
                ki "ты серьёзно хочешь сказать, что--"
                show mayu wor at l3
                show shou neu at cc
                voice "audio/voice/E1/D4/S5/Shou/5.ogg"
                ss "Давайте не начинать. Мы не можем изменить то, что уже сделано."
                show kaori ann at r3
                "Каори скрестила руки."
                
        voice "audio/voice/E1/D4/S5/Kaori/6.ogg"
        ki "Мы могли выступить лучше, если бы ты был должным образом экипирован."
        show shou smi at cc
        voice "audio/voice/E1/D4/S5/Shou/6.ogg"
        ss "Я больше не беспокоюсь об этом."
        show kaori dis at r3
        show mayu neu at l3
        voice "audio/voice/E1/D4/S5/Kaori/7.ogg"
        ki "Почему нет?"
        show shou hap at cc
        show shiny:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S5/Shou/7.ogg"
        ss "Потому что у нег оесть это удивительное ядро!"
        voice "audio/voice/E1/D4/S5/Mayu/1.ogg"
        ma "Могу ли я спросить, как ты это сделал?"
        stop music fadeout 3
    else:
        show kaori ann at r3
        "Как только мы вышли с арены Каори повернулась ко мне с яростным выражением на лице."
        show kaori ang
        voice "audio/voice/E1/D4/S5/Kaori/8.ogg"
        ki "О чём, чёрт возьми, ты думал?"
        show kaori ann
        show mayu wor at l3
        show shou ner at cc
        play music "audio/music/Next Time (GAME VERSION).ogg" fadein 1
    
        menu:
            "Я делал то, что слитал нужным.":
                pf "Я думал, что помогу вам заработать побольше очков."
                show kaori ang at r3
                show vein:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S5/Kaori/9.ogg"
                ki "Ты с ума сошёл? Из-за твоего безрассудства Сё и Маю были выбиты!"
                show kaori ann at r3
                show shou wor at cc
                pf "Я знал, что будет какой-то риск, но я не мог сидеть сложа руки. Я выбрал шанс, и он окупился. Мы должны набрать самый высокий балл за уничтожение всех ИИ!"
                show kaori dis at r3
                "Каори сильнее нахмурилась."
    
            "Всегда пожалуйста.":
                pf "О том, чтобы поднять нас на самыю вершину."
                show kaori ang at r3
                show exclamation:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S5/Kaori/10.ogg"
                ki "Ты подставил под угрозу всю команду!"
                show kaori ann at r3
                show shou wor at cc
                pf "Да, да, мне жаль, что я в одиночку выбил двух ИИ и дал нам огромный прирост очков."
                show kaori ang at r3
                voice "audio/voice/E1/D4/S5/Kaori/11.ogg"
                ki "Делл не в этом!"
                show kaori ann at r3
                pf "Actually, that is the point. Pun intended."
                "Kaori looks dangerously close to bursting a blood vessel."
                show kaori ang at r3
                show vein:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S5/Kaori/12.ogg"
                ki "Арррргх! Почему ты--"
    
            "Nobody puts me in a corner!":
                pf "This was my fight too and I wasn't going to miss it."
                show kaori ang at r3
                show vein:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S5/Kaori/13.ogg"
                ki "Do you even hear yourself right now? This fight wasn't about just you. It was about all of us!"
                show kaori ann at r3
                show shou wor at cc
                pf "And we took out all the enemy GEARs, didn't we? So what's the problem?"
                show kaori ang at r3
                show exclamation:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S5/Kaori/14.ogg"
                ki "The problem is that you put the rest of us in danger!"
                
        show kaori ann at r3 with dissolve
        show mayu ner at l3 with dissolve
        show shou neu at cc with dissolve
        "Shou steps forward in an attempt to calm Kaori down, while Mayu hangs back, staring intently at a spot on the ground."
        voice "audio/voice/E1/D4/S5/Shou/8.ogg"
        ss "Kaori--"
        "Kaori ignores Shou and continues her tirade."
        show kaori ang at r3
        show shou ner at cc
        voice "audio/voice/E1/D4/S5/Kaori/15.ogg"
        ki "You did {i}not{/i} do what was best for the team. You did what was best for yourself, and Shou and Mayu paid the price for your actions. You might have scored some points for us, but we could have scored even more if half the team hadn't been shut down."
        voice "audio/voice/E1/D4/S5/Kaori/16.ogg"
        ki "We work as a {i}team{/i}, which means we look out for each other!"
        show kaori ann at r3
        show shou wor at cc
        pf "And I'm a part of this team too, which means I shouldn't have been sidelined."
        show kaori ang at r3
        voice "audio/voice/E1/D4/S5/Kaori/17.ogg"
        ki "Did you ever think that I sidelined you in order to avoid something like this from happening? What would have happened to you if we hadn't stepped in?"
        show kaori ann at r3
        show mayu sad at l3
        "I stay silent, but cross my arms defiantly."
        voice "audio/voice/E1/D4/S5/Kaori/18.ogg"
        ki "You would have been taken out. And frankly, you should have been."
        show mayu wor at l3
        show shou ang at cc
        show exclamation:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S5/Shou/9.ogg"
        ss "Kaori!"
        show kaori ang at r3
        show shou ann at cc
        show vein:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S5/Kaori/19.ogg"
        ki "What?"
        show kaori ann at r3
        "She glares at Shou, but hesitates when she sees the hardened expression on his face."
        show shou ang at cc
        voice "audio/voice/E1/D4/S5/Shou/10.ogg"
        ss "Give the guy a break! Didn't you see what his GEAR did out there? That was {i}incredible{/i}! We should be figuring out how he did that instead of arguing over what should have happened."
        show kaori dis at r3
        show shou ann at cc
        show dots:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        "Kaori's frown deepens with Shou's every word."
        show shou dis at cc
        voice "audio/voice/E1/D4/S5/Shou/11.ogg"
        ss "What's done is done. We still won, and as much as you hate to admit it, you know that our victory was in large part due to him."
        show kaori ang at r3
        "Kaori opens her mouth to speak, but I interrupt her before she can. I'm so tired of listening to her argue."
        show kaori ann at r3
        pf "Mayu, what do you think?"
        show mayu sur at l3 with dissolve
        show panic:
            xoffset 230
            yoffset 135
            xzoom .75
            yzoom .75
        "Mayu looks up in surprise and hesitates before answering. Both Shou and Kaori stare intently at her, waiting."
        show mayu ner at l3
        voice "audio/voice/E1/D4/S5/Mayu/2.ogg"
        ma "Um… I don't want to cause trouble."
        show shou neu at cc
        voice "audio/voice/E1/D4/S5/Shou/12.ogg"
        ss "It's okay, you won't cause any trouble. Just tell us what you think."
        show mayu neu at l3
        stop music fadeout 5
        voice "audio/voice/E1/D4/S5/Mayu/3.ogg"
        ma "Well… I think--maybe we shouldn't be so angry. After all, we scored pretty well and now we know that we have a secret weapon among us."
        "Kaori crosses her arms and grudgingly shrugs. Then she turns towards me, her eyes brimming with curiosity."
        
    show kaori ske at r3
    show question:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S5/Kaori/20.ogg"
    ki "Yeah, what exactly was that max power mode thing anyway? Why didn't you tell us you could do that when we ran the simulation?"
    show shou neu at cc
    play music "audio/music/Evening Out (GAME VERSION).ogg" fadein 1
    
    menu:
        "Because I didn't know.":
            pf "I would have if I'd known about it."
            show kaori dis at r3
            show storm:
                xoffset 1175
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S5/Kaori/21.ogg"
            ki "Is that sarcasm?"
            pf "No, I'm just as surprised as you guys."
    
        "You didn't ask.":
            "I shrug."
            pf "You didn't ask."
            show kaori dis at r3
            "Kaori puts her hands on her hips."
            voice "audio/voice/E1/D4/S5/Kaori/22.ogg"
            ki "Because it's totally normal to ask everyone if they have a unique core or not."
            pf "Hey, I'm not a mind reader."
            show kaori ang at r3
            show vein:
                xoffset 1175
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S5/Kaori/23.ogg"
            ki "Well, I'm asking now! What did you do with your core?"
            show kaori ann at r3
            "I shrug again."
            pf "Couldn't tell you."
    
        "We had bigger things to worry about.":
            pf "I didn't exactly have time to think about my core since all of my weapons were missing!"
            show kaori dis at r3
            show storm:
                xoffset 1175
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S5/Kaori/24.ogg"
            ki "You still could have mentioned you had this ability that could have negated your loss of weaponry."
            pf "Well, yeah, I could have… if I had known about it."
            
    show kaori ske at r3
    show question:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S5/Kaori/25.ogg"
    ki "Huh?"
    show mayu cur at l3
    show shou cur at cc
    "Mayu and Shou blink."
    show shou ske at cc
    show question:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S5/Shou/13.ogg"
    ss "You mean you did that by accident?"
    pf "Yeah… basically."
    
    if (E1D4S4_FollowMatchPlan == 0):
        show kaori ann at r3
        voice "audio/voice/E1/D4/S5/Kaori/26.ogg"
        ki "Well, you should know your GEAR like the back of your hand. If we'd known about your core we could have assessed you better. I wouldn't have asked you to stay back and we wouldn't have had that previous conversation."
        "We both fall silent. She kind of has a point…"
        show kaori dis at r3
        voice "audio/voice/E1/D4/S5/Kaori/27.ogg"
        ki "But since you didn't tell us--"
        show shou neu at cc
        voice "audio/voice/E1/D4/S5/Shou/14.ogg"
        ss "Kaori, don't start this again…"
        show kaori thi at r3
        stop music fadeout 3
        voice "audio/voice/E1/D4/S5/Kaori/28.ogg"
        ki "Start what? I'm just saying--"
    
    else:
        show shou cur at cc
        voice "audio/voice/E1/D4/S5/Shou/15.ogg"
        ss "That's some accident."
        show kaori dis at r3
        voice "audio/voice/E1/D4/S5/Kaori/29.ogg"
        ki "Could you do it again?"
        pf "I really don't know. Maybe?"
        show kaori thi at r3
        voice "audio/voice/E1/D4/S5/Kaori/30.ogg"
        ki "Hm…"
        show dots:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        show shou neu at cc
        stop music fadeout 3
        "I don't like that thoughtful look on her face."
        
    show mayu neu at l3
    "The crackle of the intercom interrupts us."
    voice "audio/voice/E1/D4/S5/ACE Academy Announcer/1.ogg"
    an "Thank you to everyone who participated. The first phase of matches have been completed."
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 1
    show shou hap at cc with dissolve
    "Shou grins."
    show note:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S5/Shou/16.ogg"
    ss "Alright! Round one complete. Victory party at my place?"
    show kaori neu at r3
    show mayu smi at l3
    voice "audio/voice/E1/D4/S5/Kaori/31.ogg"
    ki "Sorry, Shou. I've got someplace to be."
    show shou cur at cc
    voice "audio/voice/E1/D4/S5/Shou/17.ogg"
    ss "Really? Where?"
    show kaori ann at r3
    voice "audio/voice/E1/D4/S5/Kaori/32.ogg"
    ki "N-None of your business!"
    show shou mis at cc
    voice "audio/voice/E1/D4/S5/Shou/18.ogg"
    ss "It's not like you have any other friends--"
    show kaori ang at r3
    voice "audio/voice/E1/D4/S5/Kaori/33.ogg"
    ki "Yes, I do!"
    show shou cur at cc
    voice "audio/voice/E1/D4/S5/Shou/19.ogg"
    ss "Who?"
    show kaori ann at r3
    voice "audio/voice/E1/D4/S5/Kaori/34.ogg"
    ki "You just don't know them."
    show shou mis at cc
    voice "audio/voice/E1/D4/S5/Shou/20.ogg"
    ss "Is it because they aren't real?"
    show kaori ang at r3
    "Kaori raises her fist."
    show vein:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S5/Kaori/35.ogg"
    ki "I'll show you real--"
    "Shou jumps away."
    show kaori ann at r3
    show shou hap at cc
    show drop:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S5/Shou/21.ogg"
    ss "It was a joke! I'm sorry!"
    show kaori dis at r3 with dissolve
    show kaori neu at r3 with dissolve
    voice "audio/voice/E1/D4/S5/Kaori/36.ogg"
    ki "Whatever. I need to go before I'm late anyway. See you, Mayu."
    show mayu hap at l3
    "Mayu waves, as Kaori disappears around the corner."
    hide kaori with dissolve
    show mayu smi at l3 with dissolve
    show shou smi at cc with dissolve
    voice "audio/voice/E1/D4/S5/Shou/22.ogg"
    ss "So, what about you two?"
    "Mayu smiles, but shakes her head."
    voice "audio/voice/E1/D4/S5/Mayu/4.ogg"
    ma "I wish I could, but Father is visiting tonight. He will be very eager to hear about today's match."
    show shou hap at cc
    voice "audio/voice/E1/D4/S5/Shou/23.ogg"
    ss "Tell him \"Hi\" for me."
    show mayu hap at l3
    show note:
        xoffset 230
        yoffset 135
        xzoom .75
        yzoom .75
    "She nods, says goodbye to the both of us and leaves."
    hide mayu with dissolve
    show shou mis at cc with dissolve
    voice "audio/voice/E1/D4/S5/Shou/24.ogg"
    ss "Party of two? What do you say?"
    play sound "audio/sfx/Technology/Phone Vibration Once.ogg" fadein 1 fadeout 1
    "Before I can answer, Shou gets a text."
    show shou cur at cc
    voice "audio/voice/E1/D4/S5/Shou/29.ogg"
    ss "Hold on."
    show shou neu at cc
    "He quickly reads over the message."
    voice "audio/voice/E1/D4/S5/Shou/25.ogg"
    ss "Actually, we might need a rain check on that party."
    pf "What's up?"
    show shou thi at cc
    voice "audio/voice/E1/D4/S5/Shou/26.ogg"
    ss "It's just Takeshi. He set yet another trashcan bonfire."
    pf "What?!"
    show shou smi at cc
    voice "audio/voice/E1/D4/S5/Shou/27.ogg"
    ss "It's no big deal. They just had to evacuate everyone in the building. Anyway, since I'm temporarily homeless, I'm going to go hang out in the rec center."
    pf "Alright... I guess I'll let you handle that then."
    show shou hap at cc
    "He nods."
    voice "audio/voice/E1/D4/S5/Shou/28.ogg"
    ss "Looks like farewells are in order. Goodnight to you then, Mr. Broseph."
    stop music fadeout 3
    pf "Yeah, you too."
    hide shou with dissolve
    "After saying goodbye, I head towards the parking lot."
    $ kaoOut = "sUniform"
    $ mayOut = "sUniform"
    $ shoOut = "sUniform"
    scene black with fade
    $renpy.pause(2.5)
    
    jump E1D4S6
