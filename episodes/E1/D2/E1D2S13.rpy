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
        pf "Могло быть лучше. По дороге в школу эта глупая девушка пыталась перейти дорогу и практически выпрыгнула перед моим мотоциклом. А знаешь какая лучшая часть? Она вела себя очень противно, когда я остановился помочь ей."
        show nikki ske at cc
        show drop:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/41.ogg"
        sf "Справедливости ради, из-за тебя её мог хватить сердечный приступ." 
        pf "Это её вина! Мой сигнал был все ещё зелёный. {i}Её{/i} сигнал был красный."
        show nikki thi at cc
        voice "audio/voice/E1/D2/S13/Nikki/42.ogg"
        sf "Ох… хорошо, даже так…" 
        
        if (E1D2S10_EnoughRejection == 1):
            pf "И что ещё хуже, когда я пытался вступить в команду, {i}единственная{/i} команда, искавшая членов, была её."
            show nikki cur at cc
            voice "audio/voice/E1/D2/S13/Nikki/43.ogg"
            sf "Оххх, мужик. И как это прошло?" 
            pf "Как только она меня увидела, то сказала нет."
            
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/44.ogg"
        sf "Может тебе стоит перестать сбивать людей?" 
        pf "Как будто я это делаю веселья ради!"
        show nikki smi at cc
        "Она просто смеялась." 
    
    elif (E1D2S11_JoinedTheTeam == 0) and (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
        pf "Это было интересно... по меньшей мере."
        show nikki cur at cc
        voice "audio/voice/E1/D2/S13/Nikki/51.ogg"
        sf "Звучит как хорошая история." 
        pf "Ну... Она произошла со мной, когда я чуть не сбил эту девушку."
        show nikki sur at cc
        show shocked:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/52.ogg"
        sf "Ты чуть не сбил кого-то? Я знала, что ты слишком безумно водишь мотоцикл." 
        pf "Это была не моя вина! Она вышла передо мной."
        show nikki ske at cc
        voice "audio/voice/E1/D2/S13/Nikki/53.ogg"
        sf "Ага, она в порядке?" 
        pf "Она была в порядке... По крайней мере, я думал, что она в порядке."
        show nikki dis at cc
        show drop:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/54.ogg"
        sf "Ты не остановился, чтобы проверить? Вау, придурок." 
        pf "Эй, она не выглядела раненой, так что я подумал, что ничего страшного. Но потом я столкнулся с ней позже в тот же день. Она была другим пилотом. И ей команда была единственной, которая искала новочо члена."
        show nikki ske at cc
        voice "audio/voice/E1/D2/S13/Nikki/55.ogg"
        sf "Ауч. Она позволила тебе вступить? В конце концов, похоже, что она тебя не видела." 
        pf "Ну, она была одержима тем, что пыталась узнать кто её чуть не сбил. Так что я чувствовал себя плохо за то, что сбежал с места дтп. Может она действительно поранилась или что-то ещё. {w}Так что я как идиот признался ей и извинился. Как и ожидалось, она разъярилась и отказала мне."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/56.ogg"
        sf "Мне не нравится говорить это, но с тобой поступили правильно. Это карма."
        pf "Эта самодовольная улыбка заставляет меня думать, что на самом деле тебе нравится это говорить."
        show nikki smi at cc
        voice "audio/voice/E1/D2/S13/Nikki/57.ogg"
        sf "Нет, ты прав, я обожаю это!"  
    
    elif (E1D2S11_JoinedTheTeam == 0) and (E1D2S3_EncounteredKaori == 0):
        pf "он был норм. Хоть и не повезло найти команду."
        show nikki wor at cc
        show panic:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S13/Nikki/45.ogg"
        sf "Нет?" 
        pf "Один парень предложил мне место, но честно говоря, он был немного... странный. Я не сходил с ума по поводу идеи присоединиться к нему."
        show nikki neu at cc
        voice "audio/voice/E1/D2/S13/Nikki/46.ogg"
        sf "Неимущие не могут быть теми, кто выбирает." 
        pf "Да, я полагаю. Я надеялся, что какая-нибудь другая команда ищет, но никто в зале пилотов не был очень полезным."
        show nikki smi at cc
        voice "audio/voice/E1/D2/S13/Nikki/47.ogg"
        sf "Уверена, что ты можешь попробовать завтра."
        pf "Да, но было бы лучше, если бы я нашел сегодня."
    
    show nikki cur at cc
    voice "audio/voice/E1/D2/S13/Nikki/48.ogg"
    sf "Так, похоже найти команду сегодня было очень важно."
    pf "Да, Квалификация в пятницу."
    show nikki sur at cc
    show frightful:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S13/Nikki/49.ogg"
    sf "Но это через два дня!"
    pf "Я знаю. Все остальные знали это заранее и сформировали команды в течение лета."
    show nikki wor at cc
    voice "audio/voice/E1/D2/S13/Nikki/50.ogg"
    sf "Ну, это не очень справедливо."
    pf "Да, но всё в порядке."
    show nikki neu at cc
    
    if (E1D2S2_talkwithyuunayes == 1):
        pf "К другим новостям. Сегодня я встретил в автобусе очень симпатичную девушку, Юну."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/58.ogg"
        sf "Оооооооо, она нраааааааавится тебе? Она будет твоей деееееевууууушкооооой?"
        pf "Ох, помолчи. Она просто очень мне помогла."
        show nikki smi at cc
        voice "audio/voice/E1/D2/S13/Nikki/59.ogg"
        sf "Воооооот каааааак?" 
    
    if (E1D2S2_YuunaComesWithYouPass == 1):
        pf "Она показала мне путь в офис администрации."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/60.ogg"
        sf "Потому что ты не мог туда сам дойти?" 
            
        if (E1D2S5_bribedforpass == 1) or (E1D2S5_flirtforpass == 1):
            pf "Я мог бы. Или, я мог бы провести больше времени с дружелюбной девушкой."
            show nikki mis at cc
            voice "audio/voice/E1/D2/S13/Nikki/62.ogg"
            sf "Конечно ты выберешь девушку."
            pf "Ты меня знаешь, я всегда обаятелен."
            show nikki smi at cc
            voice "audio/voice/E1/D2/S13/Nikki/63.ogg"
            sf "Ага... Конечно..." 
            pf "Ты не веришь мне? Хорошо, угадай кто смог получить пропуск на парковку на одном обаянии."
            show nikki hap at cc
            voice "audio/voice/E1/D2/S13/Nikki/64.ogg"
            sf "Юна?"
            pf "Очень смешно."
            show nikki smi at cc
            "Никки смеялась."
    
        elif (E1D2S5_bribedforpass == 0) and (E1D2S5_flirtforpass == 0):
            pf "Ну, она сделала хорошую вещь, потому что когда меня мурыжил регистратор, Юна пошла и получила мне пропуск."
            show nikki smi at cc
            voice "audio/voice/E1/D2/S13/Nikki/61.ogg"
            sf "Ты прав, она звучит полезной." 
    
            
    if (E1D2S2_talkwithyuunayes == 1) and (E1D2S2_YuunaComesWithYouPass == 0):
        pf "Да, Она предложила помочь, если мне что-то нужно. Приятно, что кто-то из кампуса готов помочь."
        show nikki mis at cc
        voice "audio/voice/E1/D2/S13/Nikki/65.ogg"
        sf "Она не знает во что себя втянула!" 
        
        if (E1D2S4_GoingToGetPassNoYuuna == 1):
            #This is a different variable than E1D2S2_YuunaComesWithYouPass. This one is if you did talk to yuuna, then left her, but went to get a pass on your own
            pf "Вероятно, мне следовало спросить у нее дорогу до офиса. Хотя, в конце концов, я сам нашёл."
            show nikki cur at cc
            voice "audio/voice/E1/D2/S13/Nikki/66.ogg"
            sf "Ты получил пропуск?" 
    
            if (E1D2S5_gotbikepass == 1):
                pf "Конечно, я же очень приятный. Кто откажет такому лицу"
                show nikki mis at cc
                voice "audio/voice/E1/D2/S13/Nikki/67.ogg"
                sf "Я это делаю всё время."
    
            if (E1D2S5_gotbikepass == 0):
                pf "Нет... Администратор был серьёзной заназой в заднице. Я должен заполнить кучу форм онлайн, прежде чем я смогу получить."
                show nikki ske at cc
                voice "audio/voice/E1/D2/S13/Nikki/68.ogg"
                sf "Это раздражает."
                
    show nikki smi at cc
    voice "audio/voice/E1/D2/S13/Nikki/69.ogg"
    sf "Похоже, у тебя был тот ещё день."
    stop ambient fadeout 3
    scene black with fade
    "Беседа продолжалась, и в итоге подошла к естественному концу. Вскоре наши тарелки блестели от чистоты."
    play ambient "audio/ambience/Night Crickets.ogg" fadein 1
    scene bg homekaito main night with Dissolve(2.5)
    $renpy.pause(1)
    pf "Я так наелся."
    show nikki mis at cc with dissolve
    voice "audio/voice/E1/D2/S13/Nikki/70.ogg"
    sf "Кто сказал тебе быть такой свиньёй"
    show nikki neu at cc
    "Я помог ей с помывкой посуды."
    pf "Я думаю немного расслабиться, а затем пойти спать пораньше."
    show nikki smi at cc
    voice "audio/voice/E1/D2/S13/Nikki/71.ogg"
    sf "Да, я тоже. Спокойной ночи!"
    pf "Спокойной."
    hide nikki with dissolve
    stop music fadeout 3
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1 fadeout 1
    scene black with fade
    $renpy.pause(1)
    "Мы разошлись, и я зашёл в свою комнату."
    $renpy.pause(1)
    scene bg homekaito myroom night with fade
    
    if (E1D2S5_gotbikepass == 0):
        "Слишком рано ложиться спать, поэтому я начал процесс получения парковки. {w}Кто знает, сколько времени потребуется, прежде чем они отправят мне письмо, и я хотел бы получить его раньше, чем позже."
        "Я залогинился на сайте и нашёл документы для запроса пропуска. {w}Заполнение документов заняло больше времени, чем я ожидал, и я устал. {w}Забравшись в постель, я закрыл глаза и вскоре уснул."
    
    else:
        "Слишком рано ложиться спать, но я мысленно истощён, и не чувствую, что смогу много сделать. {w}Я какое-то время сидел в интернете, ничего особо не выискивая, пока не почувствовал тяжесть глаз и пошёл спать."
    
    scene black with Dissolve(2.5)
    
    jump E1D3S1
