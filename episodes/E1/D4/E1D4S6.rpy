label E1D4S6:
    
    scene bg homekaito main dusk with fade
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 1
    "Дядя Кайто и Никки бездельничали на диване, когда я вернулся домой. Я плюхнулся на соседнее кресло."
    show kaito smi at l2
    show nikki hap at r2:
        xzoom -1
    with dissolve
    show exclamation:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S6/Nikki/1.ogg"
    sf "Ты наконец-то дома! Я уже волновалась."
    pf "Прости, квалификация была позже, чем ожиладось."
    show nikki neu at r2
    voice "audio/voice/E1/D4/S6/Kaito/2.ogg"
    hk "Точно! Сегодня был важный день. Как всё прошло?"
    
    menu:
        "Мы набрали много очков!":
            pf "Было трудно, но я уверен, что мы набрали высокий балл!"
            show kaito hap at l2
            show nikki hap at r2
            with dissolve
            "Никки спрыгнула со своего места, чтобы обнять меня, в то время как клыбка дяди Кайто была от уха до уха."
            show heart:
                xoffset 1050
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Nikki/2.ogg"
            sf "Ура! Я ни на секунду не сомневалась в тебе."
            show note:
                xoffset 365
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Kaito/3.ogg"
            hk "Горжусь тобой, парень! Я знал, что ты сможешь сделать это."
            show nikki neu at r2
            pf "Спасибо вам."
            show kaito smi at l2
    
        "Пожалуйста, это же я.":
            pf "Мы просто были против ИИ GEAR... это даже не испытание."
            show kaito mis at l2
            "Дядя Кайто легко бьёт меня кулаком."
            show note:
                xoffset 365
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Kaito/4.ogg"
            hk "Вот как мы это делаем!"
            "Никки закатила глаза, но все равно смеялась."
            show nikki smi at r2
            show heart:
                xoffset 1050
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Nikki/3.ogg"
            sf "Вы парни такие отстойные, но всё равно поздравляю! Это большое достижение."
            pf "Спасибо вам."
            show kaito smi at l2
    
        "Могло быть лучше.":
            pf "Мы нормально справились…"
            show nikki hap at r2
            show heart:
                xoffset 1050
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Nikki/4.ogg"
            sf "Это отлично! Поздравляю!"
            show kaito cur at l2
            voice "audio/voice/E1/D4/S6/Kaito/5.ogg"
            hk "Это хорошо, не так ли?"
            show nikki neu at r2
            pf "Ага."
            show kaito ske at l2
            show question:
                xoffset 365
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Kaito/6.ogg"
            hk "Тогда почему ты не рад этому?"
            pf "Я чувствую, что это была больше удача, чем наши умения."
            show nikki sad at r2
            "Никки нахмурилась."
            show kaito neu at l2
            show drop:
                xoffset 1050
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S6/Nikki/5.ogg"
            sf "Почему ты так думаешь? Ты сражался изо всех сил?"
            pf "Ага."
            voice "audio/voice/E1/D4/S6/Kaito/7.ogg"
            hk "Твоя команда сражалась изо всех сил?"
            pf "Ну, да."
            show nikki neu at r2
            voice "audio/voice/E1/D4/S6/Nikki/6.ogg"
            sf "Тогда ты просто накручиваешь себя."
            show kaito smi at l2
            voice "audio/voice/E1/D4/S6/Kaito/8.ogg"
            hk "Твоя сестра права. По мне так звучит как честная победа."
            pf "Полагаю, вы правы."

    voice "audio/voice/E1/D4/S6/Kaito/9.ogg"
    hk "Итак, я полагаю, твоя команда была счастлива, что взяла тебя, не так ли?"
    
    if (E1D4S4_FollowMatchPlan == 0):
        pf "Типа того."
        show nikki cur at r2
        voice "audio/voice/E1/D4/S6/Nikki/7.ogg"
        sf "Что это значит?"
        pf "Мое оружие отсутствовало, потому что оно еще не прошло таможню, поэтому команда хотела, чтобы я просто торчал сзади и держался подальше."
        show kaito cur at l2
        show nikki ske at r2
        show storm:
            xoffset 1050
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S6/Nikki/8.ogg"
        sf "Не очень-то похоже на команду."
        pf "Именно! Я участник, а не наблюдатель! Вот я и участвовал. Когда матч начался, я вышел и самостоятельно выбил двух ИИ."
        show kaito hap at l2
        show nikki smi at r2
        "Никки азартно ухмыльнулась, а Кайто смеялся."
        voice "audio/voice/E1/D4/S6/Kaito/10.ogg"
        hk "Похоже на правду."
        show nikki neu at r2
        pf "Поначалу Каори сильно бесилась, что я не последовал её приказу, но потом они просто заинтересовались моим ядром."
    
    else:
        pf "Абсолютно! Из-за того, что мое оружие не прошло таможню, они попросили меня держаться подальше."
        show kaito cur at l2
        show nikki wor at r2
        "Никки надулась."
        voice "audio/voice/E1/D4/S6/Nikki/9.ogg"
        sf "Это не честно."
        pf "Все нормально. Я понял, поэтому сдержался. Они очень хорошо справились и разбили двух ИИ до того, как их выбили. Тогда, к большому удивлению всех, мне удалось вывезти двух других."
        show kaito hap at l2
        "Дядя Кайто засмеялся."
        voice "audio/voice/E1/D4/S6/Kaito/11.ogg"
        hk "Это мой мальчик!"
        show nikki neu at r2
        pf "Но потом было немного странно. Все заинтересовались моим ядром."
        
    show kaito cur at l2
    show question:
        xoffset 365
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S6/Kaito/12.ogg"
    hk "Что не так с твоим ядром?"
    pf "Я не знаю."
    show nikki cur at r2
    show question:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S6/Nikki/10.ogg"
    sf "Ты заметил что-то странное, когда был в CINY?"
    pf "Нет…"
    show kaito ner at l2
    show nikki smi at r2
    voice "audio/voice/E1/D4/S6/Nikki/11.ogg"
    sf "Тогда я бы не волновалась об этом."
    stop music fadeout 3
    pf "Полагаю, ты права."
    $renpy.pause(1)
    scene black with fade
    $renpy.pause(2.5)
    scene bg homekaito main night with fade
    $renpy.pause(1)
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 1
    show kaito neu at l2
    show nikki neu at r2
    with dissolve
    "Дядя Кайто встал и потянулся."
    voice "audio/voice/E1/D4/S6/Kaito/13.ogg"
    hk "Пойду возьму попить. Хочешь поесть? Мы оставили тебе тарелку."
    pf "Да, было бы отлично!"
    "Я начал вставать, когда Кайто остановил меня."
    show kaito smi at l2
    voice "audio/voice/E1/D4/S6/Kaito/14.ogg"
    hk "Я принесу её."
    pf "Спасибо."
    hide kaito with dissolve
    "Я повернулся к Никки."
    pf "Ну, как прошёл твой день?"
    show nikki hap at r2 with dissolve
    voice "audio/voice/E1/D4/S6/Nikki/12.ogg"
    sf "Довольно хорошо. Я говорила тебе, что я проходила прослушивание в танцевальную команду? Я прошла!"
    pf "Это отлично, Никки!"
    show nikki smi at r2
    voice "audio/voice/E1/D4/S6/Nikki/13.ogg"
    sf "Я очень восхищена этим! Но я немного волнуюсь, потому что... я не танцевала с тех пор--"
    stop music fadeout 3
    show nikki ner at r2 with dissolve
    $renpy.pause(1)
    show nikki thi at r2 with dissolve
    play music "audio/music/Slow Day (GAME VERSION).ogg" fadein 1
    show dots:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    "Её голос затих и она отвернулась."
    pf "Я знаю. И они бы гордились тем, что ты снова начала заниматься этим."
    show nikki smi at r2 with dissolve
    "Она печально улыбнулась."
    voice "audio/voice/E1/D4/S6/Nikki/14.ogg"
    sf "Это странное чувство, зная, что их не будет рядом, чтобы посмотреть мои соревнования. Мама никогда не пропускала шоу. И помнишь, как папа делал плакат с моим именем, и размахивал им как идиот?"
    "Не мог ничего поделать, кроме как посмеяться над воспоминаниями."
    show nikki ner b1 at r2 with dissolve
    voice "audio/voice/E1/D4/S6/Nikki/15.ogg"
    sf "Ах, помню, что была {i}так{/i} смущена."
    pf "Ага, ты говорила ему неправильные даты соревнований, надеясь, что он не появится."
    show nikki smi b1 at r2
    voice "audio/voice/E1/D4/S6/Nikki/16.ogg"
    sf "Я знаю, но он всегда появлялся! Он махал этим плакатом и кричал громче всех, и всё, о чем я могла думать, как я хотела заползти в яму и умереть."
    show nikki sad at r2
    voice "audio/voice/E1/D4/S6/Nikki/17.ogg"
    sf "Но я думаю об этом сейчас… Я бы всё отдала, лишь бы снова увидеть один из его постеров--"
    show nikki win at r2
    "Её голос дрогнул, и она протёрла глаза. Я подошёл ближе и обнял её."
    voice "audio/voice/E1/D4/S6/Nikki/18.ogg"
    sf "Мне жаль."
    show nikki sad at r2
    pf "Я тоже скучаю по ним. Но слушай, у тебя все ещё есть я."
    voice "audio/voice/E1/D4/S6/Kaito/15.ogg"
    hk "И к счастью для тебя, Я эксперт в делании постеров."
    show kaito smi at l2 with dissolve
    show nikki cur at r2
    "Мы смотрели на дядю Кайто, пока он ставил передо мной тарелку. Никки слабо посмеялась."
    show nikki smi at r2
    voice "audio/voice/E1/D4/S6/Nikki/19.ogg"
    sf "Тебе трудно будет влезть в эту шкуру."
    show kaito mis at l2
    voice "audio/voice/E1/D4/S6/Kaito/16.ogg"
    hk "Я готов принять вызов."
    show nikki neu at r2
    "Она улыбнулась и снова вытерла глаза."
    stop music fadeout 3
    show heart:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S6/Nikki/20.ogg"
    sf "Спасибо, ребята."
    show kaito hap at l2
    "Дядя Кайто улыбнулся в ответ."
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 1
    voice "audio/voice/E1/D4/S6/Kaito/17.ogg"
    hk "Так, ночной просмотр кино?"
    pf "Я в игре."
    show nikki hap at r2
    show note:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S6/Nikki/21.ogg"
    sf "Я тоже!"
    show kaito smi at l2
    show note:
        xoffset 365
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S6/Kaito/18.ogg"
    hk "Отлично, что хотите посмотреть?"
    show nikki neu at r2
    
    label E1D4S6_MovieChoiceLoop:
    
        menu:
            "{i}The GEARfather{/i}":
                pf "Стареющий патриарх черного рынка Синдикат GEAR передает контроль над империей своему сопротивляющемуся сыну."
                show kaito hap at l2
                show exclamation:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/19.ogg"
                hk "Хорошо! Слишком много Дона Гирлеоне не бывает."
                pf "Об этом я и говорю!"
                show nikki cur at r2
                voice "audio/voice/E1/D4/S6/Nikki/22.ogg"
                sf "Я раньше не видела этот фильм."
                show kaito sur at l2 with dissolve
                "Я с дядей Кайто крикнули, не веря."
                show shocked:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                #player and Hitoshi Kaito line should be together 
                "Мы оба" "Что?!"
                show kaito mis at l2
                voice "audio/voice/E1/D4/S6/Kaito/21.ogg"
                hk "\"Я предложу ему шестерню, от которой он не сможет отказаться\"."
                show nikki thi at r2
                "Никки качала головой."
                show kaito ske at l2
                voice "audio/voice/E1/D4/S6/Nikki/23.ogg"
                sf "Э-э-э... Нет."
                pf "Хорошо, мы посмотрим его сейчас."
        
            "{i}The Sixth GEAR{/i}":
                pf "Маленького мальчика преследует тёмная тайна: его посещает разрушенный GEAR."
                show nikki win at r2
                show crying:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/24.ogg"
                sf "Нуууууу, мы же не собираемся СНОВА смотреть этот фильм."
                pf "Да ладно, это же классика!"
                show kaito mis at l2
                voice "audio/voice/E1/D4/S6/Kaito/22.ogg"
                hk "\"Я вижу мёртвые GEARs\"."
                pf "Ха! Видишь? Дядя Кайто втянулся в это."
                show nikki dis at r2
                show storm:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/25.ogg"
                sf "Ладно ладно. Я могу понять, когда перевес голосов против, но в следующий раз я выберу фильм."
                show kaito smi at l2
                voice "audio/voice/E1/D4/S6/Kaito/23.ogg"
                hk "Это честно."
                show nikki mis at r2
                "Никки озорно улыбнулась. О-оу, на что мы только что согласились?"
        
            "{i}The Lord of the GEARs{/i}":
                pf "Низкорослый пилот и его спутники отправились в путешествие, чтобы уничтожить GEAR всевластия."
                show nikki hap at r2
                show exclamation:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/26.ogg"
                sf "Ооооо, да! Арагир такой восхитительный!"
                pf "Он крут."
                show kaito mis at l2
                voice "audio/voice/E1/D4/S6/Kaito/24.ogg"
                hk "Да ладно, этот фильм глубже, чем просто про Арагира. \"GEAR всевластия, чтобы управлять всеми. GEAR всевластия, чтобы найти их; GEAR всевластия, чтобы привести их всех и свяжать в темноте\"."
                show nikki smi at r2
                "Никки залилась смехом."
                voice "audio/voice/E1/D4/S6/Nikki/27.ogg"
                sf "О Боже, дядя, ты задрот!?"
                show kaito hap at l2
                "Он ухмыльнулся."
                show note:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/25.ogg"
                hk "Виновен по всем статьям."
        
            "{i}Raiders of the Lost GEAR{/i}":
                pf "Известный археолог нанят, чтобы найте GEAR завета."
                show kaito ske at l2
                "Дядя Кайто похоже не понял."
                voice "audio/voice/E1/D4/S6/Kaito/26.ogg"
                hk "Не уверен, что видел это, приятель."
                show nikki cur at r2
                show shocked:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/28.ogg"
                sf "Правда, дядя Кайто? Он довольно популярен в Америке."
                pf "Ага! \"Библия говорит, что GEAR выравнивает горы и опустошает целые регионы. Армия несущая такой GEAR... непобедима\"."
                show kaito neu at l2
                show drop:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/27.ogg"
                hk "Нет, ни о чём не говорит."
                show nikki smi at r2
                voice "audio/voice/E1/D4/S6/Nikki/29.ogg"
                sf "О, тогда мы должны его посмотреть."
        
            "{i}The Hunger GEARs{/i}":
                pf "Катнис Невердин добровольно занимает место своей младшей сестры в Голодных GEARs, телевизионном бою на смерть, в котором подростки выбираются случайным образом."
                show nikki hap at r2
                show exclamation:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/30.ogg"
                sf "Я люблю этот фильм! Я никогда не относила тебя к тем, кому это нравится."
                pf "Ты шутишь? \"Пусть шестерни всегда крутятся в твою сторону\"."
                show nikki smi at r2
                voice "audio/voice/E1/D4/S6/Nikki/31.ogg"
                sf "Да!"
                pf "Что думаешьЮ дядя?"
                show kaito hap at l2
                "Дядя Кайто улыбался нам."
                voice "audio/voice/E1/D4/S6/Kaito/28.ogg"
                hk "Конечно, почему бы и нет?"
        
            "{i}GEAR юрского периода{/i}":
                pf "Во время осмотра, тематический парк подвергся отключению питания, что позволило его клонированным экспонатам dino-GEAR разгуляться."
                show kaito mis at l2
                voice "audio/voice/E1/D4/S6/Kaito/29.ogg"
                hk "Я всегда готов посмотреть, как динозавры терроризируют людей."
                show nikki hap at r2
                voice "audio/voice/E1/D4/S6/Nikki/32.ogg"
                sf "\"Держите ваши задницы\"!"
                show kaito cur at l2 with dissolve
                show dots:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                "Мы посмотрели на неё."
                show nikki mis at r2
                voice "audio/voice/E1/D4/S6/Nikki/33.ogg"
                sf "Что? Это фраза из фильма."
                pf "Все ещё немного неожиданно."
                show kaito neu at l2
                voice "audio/voice/E1/D4/S6/Kaito/30.ogg"
                hk "Совсем чуть-чуть."
        
            "{i}Snakes on a GEAR{/i}":
                pf "Военный пилот получает GEAR полный смертоносных и ядовитых змей, которые были преднамеренно выпущены, чтобы убить его и помешать ему давать показания против босса мафии."
                show nikki ske at r2
                voice "audio/voice/E1/D4/S6/Nikki/34.ogg"
                sf "Этот фильм был довольно тупым."
                pf "Шутишь? Джамуэль Л. Сэксон был крут! \"Я уже имел дело с этими сукиными--\""
                show kaito mis at l2
                voice "audio/voice/E1/D4/S6/Kaito/31.ogg"
                hk "Мы поняли."
                pf "Вам не нравится этот фильм?"
                show kaito neu at l2
                voice "audio/voice/E1/D4/S6/Kaito/32.ogg"
                hk "Он нормальный. Ты уверен, что он подходит для Никки?"
                show nikki ann at r2
                show vein:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/35.ogg"
                sf "Я не маленький ребёнок!"
                show kaito hap at l2
                "Дядя Кайто поднял руки."
                show drop:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/33.ogg"
                hk "Мне жаль!"
                show nikki smi at r2
                "Никки ухмыльнулась."
                voice "audio/voice/E1/D4/S6/Nikki/36.ogg"
                sf "Во всяком случае, я уже его видела. Я посмотрю, если придётся."
                show kaito smi at l2
                voice "audio/voice/E1/D4/S6/Kaito/34.ogg"
                hk "Хорошо, тебе решать, приятель."
                pf "Мы смотрим его."
        
            "{i}I, Cenorobot{/i}":
                pf "Пилот технофоб исследует GEAR, который мог быть разбит дружественным GEAR, что приводит к большей угрозе для человечества."
                show kaito mis at l2
                show exclamation:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/35.ogg"
                hk "Отличный выбор! Сильный фильм. \"У людей есть мечты. Даже собаки имеют мечты, но ты, ты просто машина. Имитация жизни. Может ли GEAR написать симфонию? Может GEAR превратить... холст в красивый шедевр\"?"
                show nikki mis at r2
                voice "audio/voice/E1/D4/S6/Nikki/37.ogg"
                sf "\"Можешь\"?"
                show kaito smi at l2
                pf "Хаха, Никки, тебе тоже нравится этто фильм?"
                show nikki hap at r2
                show exclamation:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/38.ogg"
                sf "Конечно! Почему его не любить?"
        
            "{i}Пятьдесят оттенков GEAR{/i}" if (E1D4S6_FiftyShadesLoopback == 0):
                $ E1D4S6_FiftyShadesLoopback = 1
                pf "Жизнь студентки литератулы Анастасии Айрон навсегда меняется, когда она встречает могущественного, богатого магната GEAR. Слышал, там есть пара горячих сцен--"
                "Я пожалел сразу, как только сказал об этом. Что вообще попудило меня попросить этто фильм?"
                show kaito ske at l2
                show nikki ske at r2
                "Дядя Кайто странно посмотрел на меня."
                show drop:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/37.ogg"
                hk "Мне придётся отклонить это."
                show nikki ner at r2
                show drop:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/39.ogg"
                sf "Без обид, но это, наверное, последний фильм, который я бы хотела посмотреть с семьей."
                pf "Да, вы правы, не знаю, о чём я думал."
                jump E1D4S6_MovieChoiceLoop
        
            "Что-нибудь с Сеонардо ДиЛаприо!":
                ### NOTE - new as of Ep4 release
                $ E1D4S6_Ceonardo = 1
                pf "Давайте посмотрим фильм с Сеонардо ДиЛаприо."
                show nikki mis at r2
                voice "audio/voice/E1/D4/S6/Nikki/40.ogg"
                sf "Ты странно одержим им, ты знаешь об этом?"
                pf "Нет, просто он очень талантливый актёр."
                show nikki smi at r2
                voice "audio/voice/E1/D4/S6/Nikki/41.ogg"
                sf "Ага, конечно, \"талантливый\" актёр, у которого все ещё нет Москара."
                pf "Как ты смеешь! Все знают, что Москары сфальсифицированы!"
                "Дядя Кайто кивнул."
                show kaito mis at l2
                voice "audio/voice/E1/D4/S6/Kaito/38.ogg"
                hk "Если честно, он {i}должен был{/i} выйграть по крайней мере уже два."
                show nikki mis at r2
                sf "О нет, ты тоже, дядя Кайто?"
                show kaito hap at l2
                "Он засмеялся."
                show bulb:
                    xoffset 365
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Kaito/39.ogg"
                hk "Так, Сеонардо ДиЛаприо… Как насчёт {i}GEAR с Уолл стрит{/i}?"
                show nikki hap at r2
                show bulb:
                    xoffset 1050
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S6/Nikki/42.ogg"
                sf "Мы должны посмотреть {i}Жомео и Рульетту{/i}! Там он был хорош!"
                
                label E1D4S6_MovieChoiceLoopCeonardo:
                    menu:
                        "{i}GEAR с Уолл стрит{/i} с Никки?!" if (E1D4S6_CeonardoLoopback == 0):
                            $ E1D4S6_CeonardoLoopback = 1
                            pf "На самом деле, я не уверен, что это лучший выбор, дядя."
                            show kaito neu at l2 with dissolve
                            show dots:
                                xoffset 365
                                yoffset 5
                                xzoom .75
                                yzoom .75
                            $renpy.pause(1)
                            show nikki cur at r2 with dissolve
                            show confused:
                                xoffset 1050
                                yoffset 160
                                xzoom .75
                                yzoom .75
                            "Он задумчиво смотрел на Никки, затем кивнул. Никки казалась растерянной, но смирилась с этим."
                            jump E1D4S6_MovieChoiceLoopCeonardo
            
                        "Давайте посмотрим {i}Жомео и Рульетту{/i}.":
                            pf "Мы можем посмотреть {i}Жомео и Рульетту{/i}."
                            show nikki smi at r2
                            show note:
                                xoffset 1050
                                yoffset 160
                                xzoom .75
                                yzoom .75
                            voice "audio/voice/E1/D4/S6/Nikki/44.ogg"
                            sf "Ура!"
                            show kaito smi at l2
                            voice "audio/voice/E1/D4/S6/Kaito/40.ogg"
                            hk "Это один из его лучших фильмов."
            
                        "Мне не нравится ни то, ни другое.":
                            pf "Я не очень хочу смотреть эти два. Давайте лучше посмотрим {i}GEARception{/i}."
                            show kaito cur at l2
                            show exclamation:
                                xoffset 365
                                yoffset 5
                                xzoom .75
                                yzoom .75
                            voice "audio/voice/E1/D4/S6/Kaito/41.ogg"
                            hk "О! Этот хорош!"
                            show nikki thi at r2
                            voice "audio/voice/E1/D4/S6/Nikki/45.ogg"
                            sf "Я ненавижу конец. Он перестал вращаться или нет?"
                            show kaito smi at l2
                            voice "audio/voice/E1/D4/S6/Kaito/1.ogg"
                            hk "Ни за что, это бы всё испортило."
                
    pf "В любом случае, я пойду найду фильм."
    #fade to black
    scene black with fade
    stop music fadeout 3
    "Мы наслаждались кинематографическим опытом до поздней ночиt--отличный конец хорошего дня."
    
    jump E1D5S1
