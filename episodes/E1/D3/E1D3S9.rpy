label E1D3S9:
    
    $renpy.pause(1)
    scene bg homekaito main dusk with fade
    "Я вошёл в дом и услышал смех, доносящийся из кухни."
    play ambient "audio/ambience/Kitchen Cooking.ogg" fadein 1
    "Я опустил сумку на пол и последовал за звуками моей семьи и восхитительным запахом ужина."
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 1
    pf "Привет." 
    "Я сел за столом и наблюдал, как Никки и дядя Кайто ходили по кухне. На них были одинаковые фартуки." 
    pf "Хорошо выглядишь, дядя! Этот фартук тебе действительно подходит. Подчёркивает глаза."
    hk "..."
    voice "audio/voice/E1/D3/S9/Kaito/6.ogg"
    hk "That's it! I'm done!" 
    "Он сорвал фартук и бросил его в сторону."
    show kaito dis at l2 with dissolve
    show storm:
        xoffset 365
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S9/Kaito/7.ogg"
    hk "Ты сказала, что я выгляжу круто."
    "Никки хихикнула и возвращается к готовке."
    show nikki hap at r2 with dissolve:
        xzoom -1
    show note:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S9/Nikki/1.ogg"
    sf "Ты выглядел круто! Каждая дама любит мужчин, умеющих готовить." 
    pf "А я люблю леди, которые готовят для меня!"
    show kaito hap at l2
    voice "audio/voice/E1/D3/S9/Kaito/8.ogg"
    hk "Аминь!"
    show nikki dis at r2
    "Кайто сел рядом со мной. Мы смеялись, пока Никки показывала нам язык."
    voice "audio/voice/E1/D3/S9/Nikki/2.ogg"
    sf "Мужчины!" 
    show kaito smi at l2
    pf "Так что у нас на ужин?"
    show nikki smi at r2 with dissolve
    voice "audio/voice/E1/D3/S9/Nikki/3.ogg"
    sf "Угадай!" 
    pf "О Боже, только не снова."
    show kaito hap at l2
    "Кайто засмеялся."
    show nikki neu at r2
    voice "audio/voice/E1/D3/S9/Kaito/9.ogg"
    hk "Как прошел день, приятель?" 
    pf "Он был нормальным."
    show kaito mis at l2
    voice "audio/voice/E1/D3/S9/Kaito/10.ogg"
    hk "Да? До каких проделок добрался?" 
    pf "Ничего особенного. С утра были уроки, потом проверил свой GEAR."
    show kaito smi at l2
    
    if (E1D2S11_JoinedTheTeam == 0): #this means he joined the team today because if you joined yesterday, it be a 1 here
        pf "Хотя мне удалось вступить в команду."
        show nikki cur at r2
        "Никки оглянулась."
        voice "audio/voice/E1/D3/S9/Nikki/4.ogg"
        sf "ты нашёл ту, которая примет тебя? Поздравляю, старший братец!" 
        pf "Да, это была вчерашняя команда. Мне не повезло найти другую, но к счастью, Сё сегодня сноа предложил мне." 
    
        if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
            show nikki ner at r2
            voice "audio/voice/E1/D3/S9/Nikki/5.ogg"
            sf "Надеюсь, эта девушка смирится с этим." 
            pf "Сё не казался взволнованным."
            show kaito cur at l2
            show nikki neu at r2
            show question:
                xoffset 365
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S9/Kaito/11.ogg"
            hk "Девушка? Хочу услышать об этой девушке." 
            pf "Она просто член команды."
            show kaito mis at l2
            show drooling:
                xoffset 365
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S9/Kaito/12.ogg"
            hk "Пока что... работая вместе в команда... дела могут... {i}накалиться{/i}." 
            "С такой пламенной личностью, как Каори, я не удивлюсь, если все накалится, хотя это не будет так, как предлагает дядя."
            show kaito smi at l2
    
        elif (E1D2S9_AgreeJoinShouTeam == 0):
            show nikki ske at r2
            show question:
                xoffset 1050
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S9/Nikki/6.ogg"
            sf "Разве это не команда, которую ты отверг?" 
            pf "Да, но у меня не было других вариантов. Кроме того, у них достойная репутация. Сойдёт, по крайней мере для квалификации."
            show nikki thi at r2
            voice "audio/voice/E1/D3/S9/Nikki/7.ogg"
            sf "Хмм." 
            "Никки повернулась к плите, а Кайто злопнул меня по спине."
            show kaito hap at l2
            show nikki neu at r2
            voice "audio/voice/E1/D3/S9/Kaito/13.ogg"
            hk "Хорошая работа, парень! Кто в команде?" 
            pf "Сё, я, и пара девушек."
            show kaito cur at l2
            show question:
                xoffset 365
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S9/Kaito/14.ogg"
            hk "Хорошо выглядящих девушек?"
            show nikki ang at r2
            voice "audio/voice/E1/D3/S9/Nikki/8.ogg"
            sf "Дядя Кайто! Не поддерживайте его!"
            show nikki ann at r2
            "Я пожал плечами."
            show kaito mis at l2
            "Кайто подмигнул мне."
            voice "audio/voice/E1/D3/S9/Kaito/15.ogg"
            hk "Я знал, что ты сможешь сделать пребывание здесь полезным для себя."
            show nikki dis at r2
            pf "Спасибо, я думаю."
            show kaito smi at l2
            show nikki neu at r2
    
    elif (E1D2S11_JoinedTheTeam == 1):
        pf "Появился один из товарищей по команде, и у нас был тренировочный бой."
        show kaito hap at l2
        voice "audio/voice/E1/D3/S9/Kaito/16.ogg"
        hk "Звучит весело." 
        pf "Так и было. Думаю, мы сделаем хорошую команду."
        show kaito smi at l2
        voice "audio/voice/E1/D3/S9/Kaito/17.ogg"
        hk "Кто ещё в коменде?" 
        pf "Сё, я, и пара девушек."
        show kaito cur at l2
        show question:
            xoffset 365
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S9/Kaito/18.ogg"
        hk "Хорошо выглядящих девушек?" 
        "I shrug." 
        pf "Да, полагаю."
        show kaito mis at l2
        "Кайто подмигнул мне и я просто кивнул."
    
    if (E1D3S1_BikeImpounded == 1):
        show nikki cur at r2
        voice "audio/voice/E1/D3/S9/Nikki/9.ogg"
        sf "И ты вернул свой байк?" 
        pf "Да, слава Богу. По крайней мере, мне больше не придется ездить на автобусе."
        show nikki hap at r2
        show bulb:
            xoffset 1050
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S9/Nikki/10.ogg"
        sf "Мне  тоже!" 
        pf "Мечтай дальше."
        show kaito ske at l2
        show nikki neu at r2
        show exclamation:
            xoffset 365
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S9/Kaito/19.ogg"
        hk "Воу, воу. Что случилось с твоим байком?"
        show nikki mis at r2
        voice "audio/voice/E1/D3/S9/Nikki/11.ogg"
        sf "Он каким-то образом припарковался не в том месте, и его конфисковали."
        show kaito cur at l2
        voice "audio/voice/E1/D3/S9/Kaito/20.ogg"
        hk "Правда? Как ты так умудрился"
        pf "Эх... Долгая история."
        show nikki smi at r2
        voice "audio/voice/E1/D3/S9/Nikki/12.ogg"
        sf "Давайте будем честными, очевидно, что ты собирался сделать что-то глупое в первый день."
        pf "Э-Эй!"
        show kaito hap at l2
        show nikki mis at r2
        "Дядя Кайто смеялся. Никки игриво ухмыльнулась мне."
        
    show nikki neu at r2
    "Никки поставила перед нами полные тарелки, затем сняла фартук и села к нам за столом."
    show kaito neu at l2
    voice "audio/voice/E1/D3/S9/Kaito/21.ogg"
    hk "Что ещё делал сегодня?" 
    
    if (E1D3S4_PlayedAnotherWithShou == 1):
        pf "В основном только тренировался с Сё, новым товарищем по команде."
        show kaito cur at l2
        voice "audio/voice/E1/D3/S9/Kaito/22.ogg"
        hk "Он хорош?" 
        pf "Да, я думаю, что мы подходим, но полагаю, что узнаем это завтра на отборочных, правда ли это."
    
    elif (E1D3S6_WentLibraryYuuna == 1):
        pf "Я пошёл позаниматься в библиотеку и столкнулся с одним другом."
        show nikki mis at r2
        voice "audio/voice/E1/D3/S9/Nikki/13.ogg"
        sf "Оооооо, это была та деееевуууушкааа?" 
        pf "Замолчи Никки! {w}Как ты вообще узнала это?!"
        show nikki smi at r2
        voice "audio/voice/E1/D3/S9/Nikki/14.ogg"
        sf "Я и не знала, но спасибо что поделился!"
        show kaito hap at l2
        voice "audio/voice/E1/D3/S9/Kaito/23.ogg"
        hk "Ещё одна девушка? Похоже ты получаешь всех дам." 
        pf "Не то что бы. Она просто помогла мне вчера."
        show kaito mis at l2
        show drooling:
            xoffset 365
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S9/Kaito/24.ogg"
        hk "Точно, \"помогла\"."
        show nikki mis at r2
        "Дядя Кайто и Никки обменялись улыбками. {w}По крайней мере, я точно знаю, что они родственники." 
    
    elif (E1D3S6_WentLibraryStudied == 1):
        pf "У меня был шанс наверстать упущенное, так что всё хорошо."
        show kaito smi at l2
        voice "audio/voice/E1/D3/S9/Kaito/25.ogg"
        hk "Горжусь тобой, парень. Рад, что ты продолжаешь усердно заниматься."
        show nikki hap at r2
        voice "audio/voice/E1/D3/S9/Nikki/15.ogg"
        sf "Ты собираешься быть любимчиком учителя со всей этой учёбой?" 
        pf "Извини, но кто в лучшей школе Cenorobotics Японии?"
        show nikki ske at r2
        voice "audio/voice/E1/D3/S9/Nikki/16.ogg"
        sf "О, теперь ты просто злорадствуешь."
        show kaito hap at l2
        show nikki dis at r2
        "Кайто рассмеялся."
        voice "audio/voice/E1/D3/S9/Kaito/26.ogg"
        hk "Тут он тебя подловил, детка."
        show nikki wor at r2
        voice "audio/voice/E1/D3/S9/Nikki/17.ogg"
        sf "Нечестно! Вы, парни, набрасываетесь на меня."
    
    elif (E1D3S4_WentToThePilotsLounge == 1):
        pf "Я немного поболтался в зале пилотов."
        show kaito smi at l2
        voice "audio/voice/E1/D3/S9/Kaito/27.ogg"
        hk "Звучит круто." 
        pf "Да, так и было. Я многое узнал о парне по имени Акира. Он пилот высшего уровня в программе."
        show nikki sur at r2 with dissolve
        voice "audio/voice/E1/D3/S9/Nikki/18.ogg"
        sf "Так он твой соперник?"
        pf "Соперник?"
        show nikki hap at r2
        voice "audio/voice/E1/D3/S9/Nikki/19.ogg"
        sf "Да, такие истории всегда нуждаются в сопернике злодее.!"
        pf "Хм, ну, на самом деле он хороший парень. Всем нравится."
        show nikki mis at r2
        voice "audio/voice/E1/D3/S9/Nikki/20.ogg"
        sf Правда? Он милый?" 
        pf "Откуда мне знать?"
        show nikki cur at r2
        voice "audio/voice/E1/D3/S9/Nikki/21.ogg"
        sf "Девушки думают, что он милый?" 
        pf "... Поладаю, да?"
        show nikki hap at r2
        "Никки засияла."
        show nikki mis at r2
        voice "audio/voice/E1/D3/S9/Nikki/22.ogg"
        sf "Опытный, вежливый и милый. Ты мог бы чему-то научиться у него."
        pf "Что это значит?!"
        show nikki smi at r2
        voice "audio/voice/E1/D3/S9/Nikki/23.ogg"
        sf "Хехе! Ничего."
        
    $renpy.pause(1)
    stop ambient fadeout 3
    stop music fadeout 3
    scene black with fade
    $renpy.pause(2.5)
    play sound "audio/sfx/Human/Burp.ogg"
    scene bg homekaito main night with fade
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 1
    show kaito smi at l2 with dissolve
    show nikki cur at r2 with dissolve:
        xzoom -1
    "Kaito вычистил свою тарелку, затем положил руку на живот и громко рыгнул. Я с Никки посмотрели на него."
    show kaito mis at l2
    voice "audio/voice/E1/D3/S9/Kaito/28.ogg"
    hk "Я просто похвалил шеф-повара!" 
    pf "Я сделаю тоже самое."
    show nikki win at r2
    "Я открыл рот, чтобы рыгнуть, но Никки вскрикнула в знак протеста." 
    show crying:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S9/Nikki/24.ogg"
    sf "Пожалуйста, не надо! Я бы предпочел не иметь их."
    show kaito hap at l2
    show nikki neu at r2
    "Кайто и я смеялись, когда Никки убирала тарелки со стола. Затем Кайто положил руку мне на плечо."
    show kaito smi at l2
    voice "audio/voice/E1/D3/S9/Kaito/1.ogg"
    hk "Похоже, у тебя был тот ещё день, приятель."
    pf "будет легче, когда я вольюсь в ритм."
    voice "audio/voice/E1/D3/S9/Kaito/2.ogg"
    hk "Конечно."
    show kaito hap at l2
    voice "audio/voice/E1/D3/S9/Kaito/2_1.ogg"
    hk "Хотите посмотреть фильм или что-то, прежде чем оба отправитесь спать?"
    show nikki hap at r2
    "Я почти согласился, но из меня вырвался долгий зевок." 
    pf "Я довольно устал. Думаю, пойду посмотрю некоторые заметки и лягу спать пораньше. У меня завтра квалификация."
    show kaito smi at l2
    voice "audio/voice/E1/D3/S9/Kaito/3.ogg"
    hk "Это честно. Никки?"
    show nikki neu at r2
    voice "audio/voice/E1/D3/S9/Nikki/25.ogg"
    sf "Я присоединюсь к тебе, когда закончу с уборкой."
    show kaito hap at l2
    voice "audio/voice/E1/D3/S9/Kaito/4.ogg"
    hk "Я помогу тебе."
    show nikki smi at r2
    voice "audio/voice/E1/D3/S9/Nikki/26.ogg"
    sf "Спасибо!" 
    show kaito smi at l2
    "Я встаю, и Кайто и Никки помахали мне."
    show kaito hap at l2
    show nikki hap at r2
    with dissolve
    show note:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S9/Nikki/27.ogg"
    sf "Спокойной ночи!"
    show note:
        xoffset 365
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S9/Kaito/5.ogg"
    hk "Спокойной ночи!"
    hide kaito
    hide nikki
    with dissolve
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1 fadeout 1
    $renpy.pause(1)
    scene black with fade
    "Я помахал в ответ и пошёл в комнату."
    $renpy.pause(1)
    scene bg homekaito myroom night with Dissolve(2.5)
    "В комнате я забрался в кровать и взял планшет, чтобы просмотреть заметки с сегодняшнего урока. {w}Я только успел прочитать часть их, когда глаза стали тяжёлыми, и я не мог продолжать. {w}Я выключил свет и закрыл глаза."
    stop music fadeout 3
    scene black with fade
    "Пока я засыпал, то думал о завтрашней квалификамии." 
    
    
    jump E1D4S1
