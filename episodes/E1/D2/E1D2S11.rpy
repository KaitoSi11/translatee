label E1D2S11:
    
    if (E1D2S9_AgreeJoinShouTeam == 0):
        "Оставшись без вариантов, я осмотрел зал в поисках Сё. He'd mentioned that his team needed another member… Hopefully that's still the case."
        play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
        "Я заметил его стоящим с двумя девушками на противоположном конце комнаты. Первая девушка, с ярко-рыжими волосами, стояла в стороне и быстро разговаривала по телефону. Другая девушка с темными волосами шаркала ногой, пока Сё что-то оживлённо ей рассказывал." 
        pf "Привет, Сё!" 
        show shou cur at cc with dissolve
        "Он повернулся ко мне как только я подошёл."
        show shou smi at cc
        voice "audio/voice/E1/D2/S11/Shou/1.ogg"
        ss "Эй, братан! Как дела?" 
        pf "Мне просто интересно, твоё предложение ещё в силе?"
        show shou hap at cc
        voice "audio/voice/E1/D2/S11/Shou/2.ogg"
        ss "Вступить к нам? Да, чёрт возьми! Не повезло найти другую команду?" 
        pf "Нет. Ты был прав, что это будет трудно."
        show shou smi at cc
        voice "audio/voice/E1/D2/S11/Shou/3.ogg"
        ss "Круто. Хорошо, вот остальная часть команды."
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
        "Он жестом указал на тёмноволосую девушку, смотрящую себе под ноги, пока рыжая разговаривала по телефону." 
    
    elif (E1D2S9_AgreeJoinShouTeam == 1):
        "Сё болтал весь путь до зала. Он постоянно прерывал себя и уходио по касательным, поэтому я понял только половину того, что он говорил. Мы шли по туннелям, и в итоге, достигаем выхода. Сё открыл дверь и провёл меня внутрь немного махнув."
        play ambient "audio/ambience/Pilot Lounge.ogg"
        scene bg campus lounge day with fade
        play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
        "Зал был заполнен группами пилотов. Полагаю, все пересекаются со своими командами тут. Сё протиснулся между командами, и я пошёл за ним в задний угол комнаты."
        show shou smi at cc with dissolve
        "Он остановился перед двумя девушками."
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
        "Та, что с тёмными волосами, смотрела себе под ноги, как только заметила Сё, пока та, что с рыжими волосами разговаривала по мобильнику ."
    
    if (E1D2S4_MayuGaveDirections == 1):
        "Хм, Хм, тёмноволосая девушка кажется мне знакомой……"
        show shou smi at cc
        "Ах! Ну конечно же!"
        pf "Привет, спасибо что показала мне где ангар."
        show mayu cur at cc
        show shou smi at l3
        with dissolve
        show exclamation:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        show mayu smi at cc with dissolve
        "Она удивлённо смотрела на меня и немного улыбнулась узнав."
        voice "audio/voice/E1/D2/S11/Mayu/1.ogg"
        ma "Рада помочь."
        pf "Надеюсь, я не причинил тебе много проблем."
        show mayu ner at cc
        "Она снова опустила голову и снова водила ногой по кругу."
        voice "audio/voice/E1/D2/S11/Mayu/2.ogg"
        ma "Это вовсе не было проблемой."
        show shou cur at l3
        show question:
            xoffset 230
            yoffset 20
            xzoom .75
            yzoom .75
        "Сё посмотрел на меня и на девушку."
        voice "audio/voice/E1/D2/S11/Shou/4.ogg"
        ss "Вы знаете друг друга?"
        pf "Она мне немного помогла сегодня."
        show mayu smi at cc
        show shou hap at l3
        "Она кивнула, и Сё широко заулыбался."
        voice "audio/voice/E1/D2/S11/Shou/5.ogg"
        ss "Вы уже друзья! Это потрясающе!"
        pf "Не особо… Я даже не знаю её имени."
        show mayu cur at cc
        show shou smi at l3
        voice "audio/voice/E1/D2/S11/Shou/6.ogg"
        ss "Ох, хорошо, это Маю."
        pf "Привет, Я [pfirst]."
        show mayu smi at cc with dissolve
        "Она поклонилась."
        voice "audio/voice/E1/D2/S11/Mayu/3.ogg"
        ma "Приятно познакомиться."
    
    else:
        "Сё указал на тёмноволосую девушку."
        show shou smi at cc
        voice "audio/voice/E1/D2/S11/Shou/7.ogg"
        ss "Это Маю. Она самая крутая в этой команде."
        show shou mis at cc
        voice "audio/voice/E1/D2/S11/Shou/7_1.ogg"
        ss "Но..эм... не говори Каори, что я это сказал."
        "Он посмотрел на рыжую, которая не обращала на нас никакого внимания."
        show shou smi at l3
        show mayu ner b1 at cc
        with dissolve
        "Маю сильно покраснела."
        voice "audio/voice/E1/D2/S11/Mayu/4.ogg"
        ma "Это не правда."
        pf "Приятно познакомиться Маю. Я [pfirst]."
        show mayu cur at cc
        "Я улыбнулся ей и протянул руку. Она подняла брови в замешательстве, затем осторожно пожала мою руку… и продолжала жать её."
        pf "Эм…"
        show mayu ner b1 at cc with dissolve
        show shoBlush:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Mayu/5.ogg"
        ma "Извини!"
        "Она тотчас же отпустила мою руку и продолжила смотреть в пол."
        
    show mayu neu at l3
    show shou smi at cc
    with dissolve
    show kaori thi at r3
    show shou smi at cc
    with dissolve
    if (E1D2S3_MetKaoriWasNice == 1):
        show shou hap at cc
        "Сё повернулся к рыжей."
        voice "audio/voice/E1/D2/S11/Shou/8.ogg"
        ss "Эй, перестань быть грубой!"
        show kaori neu at cc
        show shou neu at r3:
            xzoom -1
        with dissolve
        "Ее взгляд переключился на него, и его улыбка спала."
        show drop:
            xoffset 1175
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Shou/9.ogg"
        ss "Я хочу сказать, ты скоро закончишь? Я юы хотел, чтобы ты познакомилась кое с кем."
        show kaori dis at cc
        "Она нахмурилась."
        voice "audio/voice/E1/D2/S11/Kaori/1.ogg"
        ki "Я перезвоню."
        show kaori neu at cc
        "И закрыла телефон."
        show shou smi at r3
        stop music fadeout 3
        voice "audio/voice/E1/D2/S11/Shou/10.ogg"
        ss "Так, Это Каори."
        "Что-то в этом хмуром выражении кажется знакомым… особенно эти волосы--"
        "О нет."
        show kaori ske at cc
        play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 1
        show question:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Kaori/2.ogg"
        ki "Ты…"
        menu: 
            "Снова извиниться.":
                pf "Слушай, насчёт того,что было ранее, мне очень жаль--"
                show kaori ann at cc
                voice "audio/voice/E1/D2/S11/Kaori/3.ogg"
                ki "Забудь."
                "Она небрежно махнула рукой."
                pf "Но я не хочу, чтобы были какие-то обиды--"
                show kaori dis at cc
                "Она смотрела на меня и скрестила руки, словно я осмелился ослушаться её."
                show shou cur at r3
                voice "audio/voice/E1/D2/S11/Kaori/4.ogg"
                ki "Я же сказала - забудь."
                show question:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                "Сё водил взляд туда и обратно между нами."
                show shou mis at r3
                voice "audio/voice/E1/D2/S11/Shou/11.ogg"
                ss "Бро, почему ты не сказал мне, что вы уже друзья?"
                pf "Ну, на самом деле--"
                show kaori ang at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/5.ogg"
                ki "Заткнись!"
                show mayu sad at l3
                show kaori ann at cc
                show shou sad at r3
                with dissolve
                "Я инстинктивно остановился. Кто знал, что такая маленькая девушка может быть настолько ужасающей."
                show shou ner at r3
                "Она смотрела на Сё, который уже сжался и защищал голову."
                show frightful:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Shou/12.ogg"
                ss "Не бей меня!"
                show kaori thi at cc
                "Каори закатила глаза."
                voice "audio/voice/E1/D2/S11/Kaori/6.ogg"
                ki "Я и он {i}не{/i} друзья."
                show shou neu at r3
                voice "audio/voice/E1/D2/S11/Shou/13.ogg"
                ss "Хм, хорошо. Итак, как я уже сказал, это Каори, а это…"
                pf "[pfirst]."
                show shou smi at r3
                voice "audio/voice/E1/D2/S11/Shou/14.ogg"
                ss "Точно."
                
            "Каковы шансы, что мы снова столкнемся друг с другом…":
                pf "Что ты тут делаешь?"
                show kaori dis at cc
                "She crosses her arms."
                voice "audio/voice/E1/D2/S11/Kaori/7.ogg"
                ki "Это {i}моя{/i} команда--"
                show shou mis at r3
                voice "audio/voice/E1/D2/S11/Shou/15.ogg"
                ss "Ну, на самом деле, она наша--"
                show kaori ann at cc
                show shou ner at r3
                with dissolve
                "Шоу вздрогнул от пронзительного взгляда Каори."
                show drop:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Shou/16.ogg"
                ss "--твоя команда. Точно, продолжай."
                pf "Прости, я не это имел в виду. Просто не ожидал увидеть тебя снова."
                show kaori thi at cc
                "Она сделала паузу, затем пожала плечами."
                voice "audio/voice/E1/D2/S11/Kaori/8.ogg"
                ki "Я тоже."
                show shou sur at r3 with dissolve
                show shou hap at r3 with dissolve
                "Глаза Сё расширились от удивления. Затем он улыбается как обычно и хлопает меня - слишком сильно - по спине."
                show shou mis at r3
                voice "audio/voice/E1/D2/S11/Shou/17.ogg"
                ss "Каори вежлива к тебе? Почему ты не сказал мне, что вы друзья?"
                show kaori dis at cc
                voice "audio/voice/E1/D2/S11/Kaori/9.ogg"
                ki "Мы не друзья. Он врезался в меня утром… буквально."
                show shou ske at r3
                "Сё поднял бровь на меня."
                show question:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Shou/18.ogg"
                ss "И ты ещё жив?"
                pf "Что?"
                show kaori ang at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/10.ogg"
                ki "Что это должно значить?!"
                show mayu sad at l3
                show shou ner at r3
                "Она шагнула к Сё, который уже отпрыгнул назад."
                show kaori ann at cc
                show frightful:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Shou/19.ogg"
                ss "Ничего!"
                show shou smi at r3
                voice "audio/voice/E1/D2/S11/Shou/19_1.ogg"
                ss "Во всяком случае, поскольку вы двое не друзья… Это Каори."
                pf "Я [pfirst]. Приятно познакомиться."
    
        show kaori neu at cc
        stop music fadeout 3
        "Каори кивнула."
        show shou mis at r3
        voice "audio/voice/E1/D2/S11/Shou/20.ogg"
        ss "Тааааак?"
        show kaori thi at cc
        "Она пожала плечами."
        voice "audio/voice/E1/D2/S11/Kaori/11.ogg"
        ki "Так или иначе, не похоже что у нас есть большой выбор."
        show mayu neu at l3
        show shou hap at r3
        show note:
            xoffset 1175
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Shou/21.ogg"
        ss "Славно! Ты в команде, бро!"
        show kaori neu at cc
        pf "Спасибо, я полагаю."
    
    
    elif (E1D2S3_MetKaoriWasRudeNoHelmet == 1):
        stop music fadeout 3
        show shou hap at r3:
            xzoom -1
        show kaori ann at cc
        with dissolve
        "Сё собирался привлечь внимание рыжей,когда она захлопнула телефон и подошла к нам."
        play music "audio/music/Stress (GAME VERSION).ogg" fadein 1
        show kaori ang at cc
        show exclamation:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Kaori/17.ogg"
        ki "Тебе лучше не пытаться представить его, Сё!"
        show mayu sad at l3
        show kaori ann at cc
        show shou ner at r3
        show panic:
            xoffset 1175
            yoffset 20
            xzoom .75
            yzoom .75
        "Он колеблется."
        show shou ske at r3
        voice "audio/voice/E1/D2/S11/Shou/31.ogg"
        ss "Эм…"
        "Серьёзно? из всех пилотов этой программы, мне пришлось столкнуться именно с ней. За что я заслужил эту пытку?"
        show kaori ang at cc
        voice "audio/voice/E1/D2/S11/Kaori/18.ogg"
        ki "Его даже не волнует, что он {i}чуть не убил{/i} меня!"
        show kaori ann at cc
        "О. {w}Точно. {w}Карма та ещё сука."
        show shou ner at r3
        "Наверное, я мог бы сделать чуть больше, чтобы исправить ситуацию, но она слишком остро реагирует. "
        
        menu:
            "Смириться и извиниться.":
                "Возможно это единственный шанс попасть в команду. Я должен попытаться сделать все правильно ... даже если она невыносима."
                pf "Ты права. Я не очень хорошо повёл себя тогда, и хотел бы извиниться за то, что подверг тебя опасности"
                show kaori dis at cc
                show shou neu at r3
                with dissolve
                "Её твёрдый взгляд не спадал. Я глянул на Сё, который одобрительно кивал. {w}Через несколько мгновений она опустила взгляд и шагнула ко мне."
                show kaori thi at cc
                voice "audio/voice/E1/D2/S11/Kaori/19.ogg"
                ki "Извинения {i}не{/i} приняты."
                show shou ner at r3
                voice "audio/voice/E1/D2/S11/Shou/32.ogg"
                ss "Каори--"
                show kaori ann at cc
                voice "audio/voice/E1/D2/S11/Kaori/20.ogg"
                ki "нет. Очевидно, он просто извиняется, потому что ему нужно присоединиться к команде."
                pf "Я сделал ошибку, и я хочу сделать все правильно."
                show shou ske at r3
                voice "audio/voice/E1/D2/S11/Shou/33.ogg"
                ss "Да ладно, Каори, каждый заслуживает второй шанс."
                stop music fadeout 3
                show kaori ang at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/21.ogg"
                ki "Его второй шанс это то, что я не сообщила о нём соответствующим властям."
                hide kaori with dissolve
                show mayu wor at l3
                show shou thi at r3
                "Она раздражённо прошла мимо нас в толпу пилотов. Сё извиняющимся тоном улыбнулся мне."
                show shou neu at r3
                voice "audio/voice/E1/D2/S11/Shou/34.ogg"
                ss "Прости, но--"
                pf "Я понял."
                hide shou with dissolve
                hide mayu with dissolve
                "Он последний раз взглянул на меня перед уходом. Маю последовала за ним по пятам."
                "Ну, это отстой."
                jump E1D2S12
    
            "Слишком поздно извиняться…":
                pf "Слишком поздно…"
                show kaori ske at cc
                voice "audio/voice/E1/D2/S11/Kaori/22.ogg"
                ki "Что?"
                pf "Ничего.{w} Слушай, ты же не ранена. Не можем мы просто оставить прошлое в прошлом?"
                show kaori ang at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/23.ogg"
                ki "Нет! Твой цвет был красным, и ты проехал на него!"
                show kaori ann at cc
                pf "Он не был красным!"
                show kaori ang at cc
                voice "audio/voice/E1/D2/S11/Kaori/24.ogg"
                ki "И ты не слышал ту часть, где ты чуть не убил меня?"
                show kaori ann at cc
                pf "{i}Чуть{/i} было ключевым словом."
                show kaori ang at cc
                voice "audio/voice/E1/D2/S11/Kaori/25.ogg"
                ki "Последнее, что мне нужно в этой команде - еще один неосторожный идиот!"
                show kaori ann at cc
                show shou ske at r3 with dissolve
                voice "audio/voice/E1/D2/S11/Shou/35.ogg"
                ss "эй! Я возмущён этим--"
                show kaori ang at cc
                voice "audio/voice/E1/D2/S11/Kaori/26.ogg"
                ki "Завались, Сё!"
                show kaori ann at cc
                show shou neu at r3
                "Он замолк."
                pf "Это не только моя вина. Ты не должна была так рано переходить дорогу. надо было подождать пока загорится твой цвет."
                show kaori ann b1 at cc
                "Её лицо покраснело в тон с волосами, и глаза невероятно расширились."
                show kaori ang b1 at cc
                stop music fadeout 3
                show exclamation:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/27.ogg"
                ki "{i}Он{/i} загорелся!"
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
                "Так мы никуда не придём. Я посмотрел на Сё, лицо его было бледным. Даже Маю сжалась рядом с ним. Она так пристально смотрит в пол, что может дыру в нём прожечь."
                pf "Хорошо. Даже если я сейчас извинюсь, ты не поверишь мне. Так что будет лучше всего, если я просто пойду."
                show kaori dis at cc
                voice "audio/voice/E1/D2/S11/Kaori/28.ogg"
                ki "Это первая умная вещь, которую ты сказал сегодня."
                pf "В любом случае, спасибо за приглашение Сё."
                show shou ner at r3
                voice "audio/voice/E1/D2/S11/Shou/36.ogg"
                ss "Конечно…"
                hide mayu
                hide kaori
                hide shou
                with Dissolve(2.5)
                "Ещё раз взлгянув на них, я ушел."
                jump E1D2S12
    
            "Я начинаю жалеть, что {i}не{/i} переехал тебя.":
                pf "Но ты же не мертва, не так ли?"
                show kaori ske at cc
                show question:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/29.ogg"
                ki "Что это за тупой вопрос?"
                pf "Ты продолжаешь говорить о том, что чуть не умерла. Ну, знаешь что? Ты не мертва. По факту, ты полностью в порядке. Так что нечего тут из штанов выпрыгивать из-за ничего."
                show kaori ang at cc
                voice "audio/voice/E1/D2/S11/Kaori/30.ogg"
                ki "Как смеешь ты! Это было не {i}ничего{/i}. По факту--"
                show kaori ann at cc
                "Я поднял руку и прервал её, прежде чем она продолжила."
                pf "По факту, ты должна оставить прошлое позади. Потому что давай взглянем правде в лицо, тебе {i}нужен{/i} я."
                show kaori ann b1 at cc with dissolve
                "Ее лицо было настолько красным, что я почти видел, как пар выходил из её ушей."
                show kaori ang b1 at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/31.ogg"
                ki "Мне {i}никто{/i} не нужен, несомненно мне не нужен {i}ты{/i}!"
                show kaori ann at cc
                pf "Ещё раз, сколько людей в вашей команде?"
                show kaori dis at cc
                "Она нахмурилась и скрестила руки, но не ответила."
                pf "Именно."
                show kaori thi at cc
                voice "audio/voice/E1/D2/S11/Kaori/32.ogg"
                ki "И? Мы найдём кого-нибудь."
                show shou neu at r3
                voice "audio/voice/E1/D2/S11/Shou/37.ogg"
                ss "Но Каори, больше никого нет."
                "Сё так нехарактерно тихо говорил, что я почти забыл о нем. Даже сейчас его голос был чуть выше шепота."
                show kaori dis at cc
                voice "audio/voice/E1/D2/S11/Kaori/33.ogg"
                ki "Мы найдём кого-нибудь."
                show shou ner at r3
                voice "audio/voice/E1/D2/S11/Shou/38.ogg"
                ss "Разве ты не можешь дать ему еще один шанс?"
                pf "Я готов отложить наши разногласия и начать с чистого листа. {w}А ты?"
                show kaori ann at cc
                "Она сделала паузу, а потом посмотрела мне прямо в глаза."
                stop music fadeout 3
                voice "audio/voice/E1/D2/S11/Kaori/34.ogg"
                ki "нет."
                show shou neu at r3
                voice "audio/voice/E1/D2/S11/Shou/39.ogg"
                ss "Каори--"
                show kaori ang at cc
                show exclamation:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/35.ogg"
                ki "Заткнись, Сё!"
                show mayu wor at l3
                show kaori ann at cc
                show shou neu at r3
                with dissolve
                pf "Без разницы. В любом случае, спасибо Сё."
                show shou ner at r3
                voice "audio/voice/E1/D2/S11/Shou/40.ogg"
                ss "Конечно…"
                hide mayu
                hide kaori
                hide shou
                with Dissolve(2.5)
                "Я развернулся и ушёл, но потом обернулся назад и увидел как Сё спорил с Каори. Завтра что-нибудь придумаю."
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
