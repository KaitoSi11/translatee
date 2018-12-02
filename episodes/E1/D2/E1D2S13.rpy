label E1D2S13:
    
    $renpy.pause(1)
    scene bg homekaito main dusk with Dissolve(2.5)
    "Как только я открыл входную дверь, то услышал звон на кухне. {w}Должно быть Никки дома. {w}Как я и предполагал, она что-то помешивала в кастрюле, окружённая кучей приборов."
    play ambient "audio/ambience/Kitchen Cooking.ogg" fadein 1
    show nikki neu at cc with dissolve
    pf "Привет, Никки."
    show nikki cur at cc with dissolve
    show exclamation:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    "Она удивлённо посмотрела на меня."
    show nikki hap at cc
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 1
    voice "audio/voice/E1/D2/S13/Nikki/1.ogg"
    sf "Привет! Ты рано вернулся домой."
    pf "Разве? Как раз к ужину. {w}Что готовишь?"
    show nikki smi at cc
    voice "audio/voice/E1/D2/S13/Nikki/2.ogg"
    sf "Угадай!"
    "Я попытался заглянуть в горшок, но она закрыла его от меня."
    show nikki mis at cc
    voice "audio/voice/E1/D2/S13/Nikki/3.ogg"
    sf "Не жульничать!"
    
    menu:
        "Мой нос знает.":
            "Я глубоко вздохнул, чтобы разобрать ароматы, витавшие в воздухе. Доминирующий аромат - помидоры, а за ним следует мясо - говядина, а также намек на сельдерей ... базилик…"
            pf "Ты готовишь Болоньезе!"
            show nikki smi at cc with dissolve
            "Она посмеялась и показала мне кипящий соус в кастрюле."
            voice "audio/voice/E1/D2/S13/Nikki/4.ogg"
            sf "Хорошая догадка!"
            pf "Это не было догадкой. Супер Нюхач знает всё."
            "Я торжественно стукнул по носу."
            show nikki ske at cc
            show drop:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S13/Nikki/5.ogg"
            sf "Ты такой странный. Кто вообще жаёт имя своему носу?"
            pf "Смейся сколько хочешь, но ты запоёшь по-другому, когда Супер Нюхач спасёт тебя от опасности."
            show nikki cur at cc
            show question:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S13/Nikki/6.ogg"
            sf "И почему я буду в опасности?"
            pf "Я не знаю. Возможно, твои враги планируют напасть на тебя."
            show nikki smi at cc
            "Она снова засмеялась."
            show nikki mis at cc
            voice "audio/voice/E1/D2/S13/Nikki/7.ogg"
            sf "У меня нет врагов!"
            pf "Просто подожди."
            voice "audio/voice/E1/D2/S13/Nikki/8.ogg"
            sf "Грубо! Я очень милая."
            "Она шлёпнула меня по руке, и теперь моя очередь смеяться."
            show nikki neu at cc
    
        "{color=#00ff00}{b}Так или иначе, я уже знаю ответ.{/b}{/color}" if (MCStory == 3):
            jump E1D2S13_MCStory1
            
        "Так или иначе, я уже знаю ответ." if (MCStory != 3):
            label E1D2S13_MCStory1:
                pf "Это Болоньезе."
                show nikki cur at cc with dissolve
                "Никки удивленно моргнула."
                show question:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S13/Nikki/9.ogg"
                sf "Как ты так быстро выяснил это?"
                pf "Всё просто.  Во-первых, ты используешь кастрюлю для медленной варки, а это означает то, что это, скорее всего, суп или соус."
                pf "Во-вторых, на тебе фартук, а это значит, что ты готовишь что-то грязное или пачкающееся - или и то, и другое."
                pf "На разделочной доске остатки разных овощей и все еще мокрая от свежесрезанного томатного сока и семян. Нож все ещё запачкан томатом, что значит, что это густой томатный соус."
                show nikki sur at cc
                pf "В мусорной корзине говядина, и, учитывая ограниченные ингредиенты, которые ты сможешь найти в Японии, я подумал, что наиболее вероятное блюдо, которое ты делаешь - болоньезе."
                show drop:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                "Никки застыла на время моей речи и смотрела на меня с широко открытыми глазами. Как только я закончил, она оттаяла, а затем надулась."
                show nikki dis at cc with dissolve
                voice "audio/voice/E1/D2/S13/Nikki/10.ogg"
                sf "Это не честно! Ты все ещё проиграл."
                pf "Что? Разве ты не делаешь болоньезе?"
                show nikki thi at cc
                voice "audio/voice/E1/D2/S13/Nikki/11.ogg"
                sf "нет, я делаю его, но ты не последовал правилам и {i}угадал{/i}. Ты провёл какой-то странный роботизированный анализ!"
                "Я ослепил её уверенной улыбкой."
                pf "Да не, Я просто дурачился. Я не могу в самом деле проанализировать кухню."
                show nikki cur at cc
                voice "audio/voice/E1/D2/S13/Nikki/12.ogg"
                sf "Ох. Тогда как ты узнал?"
                pf "Я просто почуял его. В этом доме так хорошо пахнет!"
                show nikki smi at cc
                "Никки хихикнула, и продолжила готовку."
                voice "audio/voice/E1/D2/S13/Nikki/13.ogg"
                sf "Спасибо."
                show nikki neu at cc
    
        "Я и не понял, что нам снова по пять лет.":
            stop music fadeout 3
            pf "Просто скажи мне."
            show nikki smi at cc
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 1
            voice "audio/voice/E1/D2/S13/Nikki/14.ogg"
            sf "Нет, угадай! Это просто."
            pf "Если это так просто, тогда почему просто не скажешь мне?"
            show nikki hap at cc
            voice "audio/voice/E1/D2/S13/Nikki/15.ogg"
            sf "Потому что так будет веселее! Ну давай, всего разочек. Ты можешь почувствовать запах и понять."
            pf "Я ненавижу игры с угадыванием."
            show nikki mis at cc
            voice "audio/voice/E1/D2/S13/Nikki/16.ogg"
            sf "Всего один раз!"
            "Я снова вытянул шею в сторону кастрюли, но она заблокировала меня."
            pf "Никки--"
            "Я быстро никлонил голову в другую сторону, обманув её и сумел заглянуть в кастрюлю."
            show nikki sur at cc
            voice "audio/voice/E1/D2/S13/Nikki/17.ogg"
            sf "Эй!"
            pf "Это болоньезе."
            show nikki dis at cc
            show storm:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            "Она надулась и вернулась к готовке."
            voice "audio/voice/E1/D2/S13/Nikki/18.ogg"
            sf "Ты не весёлый."
            show nikki neu at cc
    
        "Я хочу своб детку назад, детку назад, детку назад, детку назад…":
            stop music fadeout 3
            pf "Соус барбекю!"
            show nikki ske at cc
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 1
            show drop:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S13/Nikki/19.ogg"
            sf "Ты сейчас шутишь?"
            pf "Пицца!"
            show nikki dis at cc
            voice "audio/voice/E1/D2/S13/Nikki/20.ogg"
            sf "Нет, ты не можешь приготовить пиццу в кастрюле."
            pf "Окономияки!"
            show nikki ann at cc
            show vein:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S13/Nikki/21.ogg"
            sf "Снова, это не то, что ты можешь приготовить в кастрюле."
            pf "Молочный поросёнок!"
            show nikki sur at cc
            voice "audio/voice/E1/D2/S13/Nikki/22.ogg"
            sf "Что--"
            pf "Одэн!"
            show nikki dis at cc
            show storm:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S13/Nikki/23.ogg"
            sf "Нет--"
            pf "Шад Ро!"
            show nikki ske at cc
            voice "audio/voice/E1/D2/S13/Nikki/24.ogg"
            sf "Ты вообще знаешь, что такое Шад Ро?"
            pf "Фугу!"
            show nikki cur at cc
            show dots:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            $renpy.pause(2.5)
            "Она просто смотрела на меня."
            show nikki dis at cc
            voice "audio/voice/E1/D2/S13/Nikki/25.ogg"
            sf "Seriously?"
            pf "... Тааааааааак, это значит нет?"
            show nikki ske at cc
            voice "audio/voice/E1/D2/S13/Nikki/26.ogg"
            sf "Как именно ты попал в самую престижную программу пилотов в стране??"
            show nikki neu at cc
            "Я посмеялся над ней, и она посмеялась в ответ."
    
    stop music fadeout 3
    pf "Я просто рад, что готовишь миенно ты, а не я. Всё, что ты делаешь - вкусно! Ты знаешь, у тебя действительно есть талант повара!"
    show nikki mis at cc
    voice "audio/voice/E1/D2/S13/Nikki/27.ogg"
    sf "О, заткнись."
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 1
    "Она пыталась сдержать улыбку, но провалилась."
    show nikki neu at cc
    pf "Ты ходила в магазин после школы? Я не знал, что дядя Кайто хранит все эти ингридиенты дома."
    voice "audio/voice/E1/D2/S13/Nikki/28.ogg"
    sf "Да, я ходила. Вчерашние суши были очень хороши, но знаешь, сегодня я хотела что-то более здорового."
    "Hmm, to Nikki, \"hearty\" foods are \"comfort\" foods."
    pf "Это значит, что у тебя был сегодня плохой день в школе?"
    show nikki cur at cc with dissolve
    "Она удивлённо моргнула, затем засмеялась."
    show nikki smi at cc
    show note:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S13/Nikki/29.ogg"
    sf "Конечно нет! Он был отличным. Я встретила много людей на ярмарке клубов, которую они провели после школы. Там так много крутых клубов! Ты знал, что у них есть клуб кэндо? Ты определённо не найдёшь такого дома!"
    show nikki hap at cc
    voice "audio/voice/E1/D2/S13/Nikki/29_1.ogg"
    sf "Я думаю попробовать клуб танцев, хотя, возможно пойду в студсовет."
    pf "Вау, похоже у тебя был довольно насыщенный день."
    show nikki neu at cc
    "Она быстро проверила пасту и кивнула."
    show nikki smi at cc
    voice "audio/voice/E1/D2/S13/Nikki/30.ogg"
    sf "Определённо! Я немного разочарована тем, что у них нет кулинарного клуба, но это нормально. Они предлагают класс кулинарии, который я возьму. Вскоре я буду экспертом в японской кухне!"
    pf "Может, организуешь кулинарный клуб."
    show nikki hap at cc
    voice "audio/voice/E1/D2/S13/Nikki/31.ogg"
    sf "Ооооо, возможно!"
    "Я начал накрывать стол на троих, когда Никки покачала головой."
    show nikki thi at cc
    voice "audio/voice/E1/D2/S13/Nikki/32.ogg"
    sf "Ты не видел сообщение дяди Кайто? Он будет сегодня поздно."
    pf "Я не проверял телефон."
    "Вскоре стол был накрыт, и у нас с Никки была большая порция пасты перед нами."
    show nikki neu at cc
    voice "audio/voice/E1/D2/S13/Nikki/33.ogg"
    sf "Как прошёл твой первый день?"
    
    if (E1D2S11_JoinedTheTeam == 1) and (E1D2S3_MetKaoriWasNice == 1):
        pf "Мой день был немного стрынным. Он начался ужасно. {w}Я чуть не сбил девушку по дороге в школу, но был джентельменом, каким и являюсь--"
        show nikki smi at cc
        "Никки фыркнула, и я проигнорировал её."
        pf "--Я остановился помочь ей. Мне повезло, что я сделал это. Потому что когда я искал команду, единственным, кто искал членов, была она."
        show nikki ske at cc
        show question:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/34.ogg"
        sf "Так, она позволил тебе вступить?"
        pf "Ага."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/35.ogg"
        sf "Везунчик."
        pf "Как я и сказал."
    
    elif (E1D2S11_JoinedTheTeam == 1) and (E1D2S3_MetKaoriWasRudeYesHelmet == 1):
        pf "Мой день был довольно стрынным. Он начался ужасно. Эта безумная девушка выскочила перед моим мотоциклом по дороге в школу. А затем, когда я искал команду, единственная команда, принимавшая участников, была {i}её{/i}!"
        show nikki cur at cc
        voice "audio/voice/E1/D2/S13/Nikki/36.ogg"
        sf "О чувак! Она позволила тебе присоединиться?"
        pf "Да, но только потому, что она не знала, что я был тем, кто чуть не сбил её."
        show nikki sur at cc
        show shocked:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/37.ogg"
        sf "То есть, ты даже не остановился, чтобы помочь ей?"
        pf "Нет… Зачем мне тратить время на споры с кем-то, кто явно ошибается? Я просто надеюсь, что она не выяснит, что это был я. Это будет неудобно."
        show nikki ske at cc
        show drop:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/38.ogg"
        sf "Ваааааау. Ты заслуживаешь того, что бы они ни сделала."
    
    elif (E1D2S11_JoinedTheTeam == 1) and (E1D2S3_EncounteredKaori == 0):
        pf "Он был нормальным. Мне удалось вступить в команду, что было довольно удачно, учитывая, что только одна команда искала членов."
        show nikki hap at cc
        show note:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/39.ogg"
        sf "Это хорошо! Как твои товарищи по команде?"
        pf "Они все довольно ... разные. Одна девушка слегка ужасающая. Другая девушка настолько тихая, что я забыл, что она там. И парень, который предложил меня… ну, он особый фрукт."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/40.ogg"
        sf "Не уверена, что могу поверить в то, что {i}ты{/i} там самый нормальный человек."
    
    elif (E1D2S11_JoinedTheTeam == 0) and (E1D2S3_MetKaoriWasRudeNoHelmet == 1):
        pf "It could have been better. On my way into school, this dumb girl tried to cross the street and basically jumped in front of my bike. And the best part? She was a complete jerk to me when I stopped to check on her."
        show nikki ske at cc
        show drop:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/41.ogg"
        sf "To be fair, you probably gave her a heart attack." 
        pf "That's her fault! My light was still green. {i}Her{/i} light was red."
        show nikki thi at cc
        voice "audio/voice/E1/D2/S13/Nikki/42.ogg"
        sf "Oh… well, even so…" 
        
        if (E1D2S10_EnoughRejection == 1):
            pf "And to make matters worse, when I tried to join a team, the {i}only{/i} team looking for another member was hers."
            show nikki cur at cc
            voice "audio/voice/E1/D2/S13/Nikki/43.ogg"
            sf "Ohhhh, man. How did that go?" 
            pf "As soon as she saw me she said no."
            
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/44.ogg"
        sf "Maybe you should stop running people over?" 
        pf "It's not like I do this for fun!"
        show nikki smi at cc
        "She just laughs." 
    
    elif (E1D2S11_JoinedTheTeam == 0) and (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
        pf "It was interesting... to say the least."
        show nikki cur at cc
        voice "audio/voice/E1/D2/S13/Nikki/51.ogg"
        sf "Sounds like a good story." 
        pf "Well... It started out with me nearly running over this girl."
        show nikki sur at cc
        show shocked:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/52.ogg"
        sf "You nearly ran someone over? I knew you drove too crazy on that bike." 
        pf "It wasn't my fault! She walked out in front of me."
        show nikki ske at cc
        voice "audio/voice/E1/D2/S13/Nikki/53.ogg"
        sf "Uh huh, is she okay?" 
        pf "She was fine... At least, I thought she was fine."
        show nikki dis at cc
        show drop:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/54.ogg"
        sf "You didn't stay to find out? Wow, jerk." 
        pf "Hey, she didn't seem hurt so I didn't think it was a big deal. But then I ended up running into her later that day. She's another pilot, and her team was the only one looking for a new member."
        show nikki ske at cc
        voice "audio/voice/E1/D2/S13/Nikki/55.ogg"
        sf "Ouch. Did she let you join? After all, it sounds like she didn't see you." 
        pf "Well, she was obsessing over finding out who nearly ran her over, so I felt bad for leaving the scene like I did. Maybe she'd actually gotten hurt or something. {w}So like an idiot I confessed and apologised to her. As expected, she was furious and refused to let me on the team."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/56.ogg"
        sf "I hate to say it, but it serves you right. That's karma."
        pf "That smug smile of yours makes me think you don't hate saying that."
        show nikki smi at cc
        voice "audio/voice/E1/D2/S13/Nikki/57.ogg"
        sf "No, you're right, I loved it!"  
    
    elif (E1D2S11_JoinedTheTeam == 0) and (E1D2S3_EncounteredKaori == 0):
        pf "It was okay. No luck finding a team, though."
        show nikki wor at cc
        show panic:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/45.ogg"
        sf "No?" 
        pf "One guy offered me a space, but to be honest, he was a bit... strange. I wasn't crazy about the idea of joining him."
        show nikki neu at cc
        voice "audio/voice/E1/D2/S13/Nikki/46.ogg"
        sf "Beggars can't be choosers." 
        pf "Yeah, I guess. I was hoping that another team was looking but nobody in the Pilot's Lounge was very helpful."
        show nikki smi at cc
        voice "audio/voice/E1/D2/S13/Nikki/47.ogg"
        sf "I'm sure you can try again tomorrow."
        pf "Yeah, but it would have been better if I'd found one today."
    
    show nikki cur at cc
    voice "audio/voice/E1/D2/S13/Nikki/48.ogg"
    sf "So, it sounds like finding a team today was super important."
    pf "Oh, yeah, the qualifier is on Friday."
    show nikki sur at cc
    show frightful:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S13/Nikki/49.ogg"
    sf "But that's in two days!"
    pf "I know. Everyone else knew this in advance and formed teams over the summer."
    show nikki wor at cc
    voice "audio/voice/E1/D2/S13/Nikki/50.ogg"
    sf "Well, that's not really fair."
    pf "Yeah, but it's fine."
    show nikki neu at cc
    
    if (E1D2S2_talkwithyuunayes == 1):
        pf "In other news, I met Yuuna, this really nice girl, on the bus today."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/58.ogg"
        sf "Ooooh, do you liiiiike her? Is she gonna be your giiirrrlllfriiiiend?"
        pf "Oh shut up. She was just really helpful."
        show nikki smi at cc
        voice "audio/voice/E1/D2/S13/Nikki/59.ogg"
        sf "Oh yeeaaaah?" 
    
    if (E1D2S2_YuunaComesWithYouPass == 1):
        pf "She showed me the way to the administrative office."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/60.ogg"
        sf "Because you can't get there on your own?" 
            
        if (E1D2S5_bribedforpass == 1) or (E1D2S5_flirtforpass == 1):
            pf "I could have, or I could have spent more time with a friendly girl."
            show nikki mis at cc
            voice "audio/voice/E1/D2/S13/Nikki/62.ogg"
            sf "Of course you would choose the girl."
            pf "You know me, always the charmer."
            show nikki smi at cc
            voice "audio/voice/E1/D2/S13/Nikki/63.ogg"
            sf "Yea... Sure..." 
            pf "Don't believe me? Well, guess who managed to snag a parking pass on charms alone."
            show nikki hap at cc
            voice "audio/voice/E1/D2/S13/Nikki/64.ogg"
            sf "Yuuna?"
            pf "Very funny."
            show nikki smi at cc
            "Nikki laughs."
    
        elif (E1D2S5_bribedforpass == 0) and (E1D2S5_flirtforpass == 0):
            pf "Well, it's a good thing she did because when the receptionist gave me a hard time, Yuuna stepped in and got me the parking pass."
            show nikki smi at cc
            voice "audio/voice/E1/D2/S13/Nikki/61.ogg"
            sf "You're right, she does sound helpful." 
    
            
    if (E1D2S2_talkwithyuunayes == 1) and (E1D2S2_YuunaComesWithYouPass == 0):
        pf "Yeah, she offered to help me if I needed anything. It's nice to have someone on campus willing to help."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/65.ogg"
        sf "She doesn't know what she got herself into!" 
        
        if (E1D2S4_GoingToGetPassNoYuuna == 1):
            #This is a different variable than E1D2S2_YuunaComesWithYouPass. This one is if you did talk to yuuna, then left her, but went to get a pass on your own
            pf "I probably should have asked her the way to the permit office. Although, I did find it eventually."
            show nikki cur at cc
            voice "audio/voice/E1/D2/S13/Nikki/66.ogg"
            sf "Did you get your pass?" 
    
            if (E1D2S5_gotbikepass == 1):
                pf "Of course, I'm smooth like that. Who would say no to this face?"
                show nikki mis at cc
                voice "audio/voice/E1/D2/S13/Nikki/67.ogg"
                sf "I do, all the time."
    
            if (E1D2S5_gotbikepass == 0):
                pf "No... The administrator was a serious ass. I have to fill out a bunch of forms online before I can get it."
                show nikki ske at cc
                voice "audio/voice/E1/D2/S13/Nikki/68.ogg"
                sf "That's annoying."
                
    show nikki smi at cc
    voice "audio/voice/E1/D2/S13/Nikki/69.ogg"
    sf "Sounds like you’ve had quite the day."
    stop ambient fadeout 3
    scene black with fade
    "The conversation continues and eventually lulls to a natural close. Soon both of our plates are polished clean."
    play ambient "audio/ambience/Night Crickets.ogg" fadein 1
    scene bg homekaito main night with Dissolve(2.5)
    $renpy.pause(1)
    pf "I am so full."
    show nikki mis at cc with dissolve
    voice "audio/voice/E1/D2/S13/Nikki/70.ogg"
    sf "Who told you to be such a pig?"
    show nikki neu at cc
    "I help her with clean-up."
    pf "I think I'm going to relax for a bit, then go to bed early tonight."
    show nikki smi at cc
    voice "audio/voice/E1/D2/S13/Nikki/71.ogg"
    sf "Yeah, me too. Goodnight!"
    pf "Night."
    hide nikki with dissolve
    stop music fadeout 3
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1 fadeout 1
    scene black with fade
    $renpy.pause(1)
    "We part ways and I head into my room."
    $renpy.pause(1)
    scene bg homekaito myroom night with fade
    
    if (E1D2S5_gotbikepass == 0):
        "It's too early to go to bed, so I'll start the process for getting a parking pass. {w}Who knows how long it'll take before they mail me one, and I'd like to get it sooner rather than later."
        "I log into my weblink and find the documents to request a permit. {w}It takes me longer than I expected to fill out all of the paperwork, and it leaves me exhausted. {w}Crawling into bed, I close my eyes and soon fall asleep."
    
    else:
        "It's too early to go to bed, but I'm mentally exhausted and don't feel up to doing much. {w}I browse the internet for a while, looking up nothing in particular, until my eyes feel heavy and I drift off to sleep."
    
    scene black with Dissolve(2.5)
    
    jump E1D3S1
