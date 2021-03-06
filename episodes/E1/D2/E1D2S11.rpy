label E1D2S11:
    
    if (E1D2S9_AgreeJoinShouTeam == 0):
        "Оставшись без вариантов, я осмотрел зал в поисках Сё. Он упоминал, что его команде не хватает человека… Надеюсь, что все ещё так."
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
        ss "Эй, перестань вести себя грубо!"
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
        ss "Я хочу сказать, ты скоро закончишь? Я бы хотел, чтобы ты познакомилась кое с кем."
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
        "Сё повернулся к рыжей."
        play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1 fadeout 1
        voice "audio/voice/E1/D2/S11/Shou/41.ogg"
        ss "Эй, перестань вести себя грубо!"
        show kaori neu at cc
        show shou neu at r3:
            xzoom -1
        with dissolve
        "Её взгляд переключился на него, и его улыбка спала."
        show drop:
            xoffset 1175
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Shou/42.ogg"
        ss "Я хочу сказать, ты скоро закончишь? Я бы хотел, чтобы ты познакомилась кое с кем."
        show kaori dis at cc
        "She frowns."
        voice "audio/voice/E1/D2/S11/Kaori/1.ogg"
        ki "Я перезвоню."
        show kaori neu at cc
        "И закрыла телефон."
        show shou smi at r3
        voice "audio/voice/E1/D2/S11/Shou/43.ogg"
        ss "Так, это Каори."
        show kaori ske at cc
        "Она быстро осмотрела меня, потом скрестила руки." 
        show question:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S11/Kaori/36.ogg"
        ki "Пилот?"
        show shou mis at r3
        voice "audio/voice/E1/D2/S11/Shou/44.ogg"
        ss "не просто какой-нибудь пилот, а пилот, желающий вступить в мою команду!"
        show kaori dis at cc
        voice "audio/voice/E1/D2/S11/Kaori/37.ogg"
        ki "{i}Твою{/i} команду?"
        show shou hap at r3
        "Её глаза впились в Сё и он отпрянул назад, затем робко улыбнулся."
        voice "audio/voice/E1/D2/S11/Shou/45.ogg"
        ss "Я имел в виду {i}нашу{/i} команду."
        show kaori neu at cc
        voice "audio/voice/E1/D2/S11/Kaori/38.ogg"
        ki "Так-то лучше."
        "Она повернулась обратно ко мне."
        show kaori thi at cc
        show shou smi at r3
        with dissolve
        voice "audio/voice/E1/D2/S11/Kaori/39.ogg"
        ki "Хм… Полагаю ты подойдёшь. Не то чтобы у нас был выбор."
        menu: 
            "Ну, это было просто!": 
                pf "Хех, и они сказали, что присоединиться к этой команде будет сложно."
                show kaori dis at cc
                show shou hap at r3
                "Сё сдерживал смех, но Каори вцепилась в него взглядом."
                voice "audio/voice/E1/D2/S11/Kaori/40.ogg"
                ki "Кто \"они\"?"
                pf "Эм, никто... просто люди в моём классе."
                show kaori ske at cc
                voice "audio/voice/E1/D2/S11/Kaori/41.ogg"
                ki "Каком классе?"
                pf "101 пилотный?"
                show kaori ann at cc
                "Она внезапно налетела на Сё."
                show kaori ang at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/42.ogg"
                ki "Ты привёл мне первогодку?!"
                show shou mis at r3
                voice "audio/voice/E1/D2/S11/Shou/46.ogg"
                ss "Нет, он просто новенький!"
                pf "Я второгодка, но переведённый ученик так что они заставили меня снова взять 101 пилотный."
                show kaori dis at cc
                show shou smi at r3
                with dissolve
                "Она расслабилась."
                voice "audio/voice/E1/D2/S11/Kaori/43.ogg"
                ki "Ну, я надеюсь, ты хоть как-то умеешь сражаться. Я не хочу потратить вечность на то, чтобы достиг нашего уровня."
                pf "Я справлюсь."
                show kaori thi at cc
                voice "audio/voice/E1/D2/S11/Kaori/44.ogg"
                ki "Посмотрим."
                show shou mis at r3
                "Сё наклонился ко мне и понизил голос."
                voice "audio/voice/E1/D2/S11/Shou/47.ogg"
                ss "Я думаю ты ей нравишься!"
                show shou smi at r3
                "Если она так себя ведёт с теми, кто ей нравится, то надеюсь никогда не попать на плохую её сторону."
    
            "Приятно познакомиться.": 
                "Я протянул руку."
                pf "Я [pfirst]. Рад познакомиться."
                show kaori neu at cc
                "Она безучастно посмотрела на мою руку и ничего не сделала. Через минуту я опустил её. {w}Ну, это было неловко."
                pf "В любом случае, спасибо, что позволили мне присоединиться к вашей команде. Я беспокоился, что не смогу найти."
                "Сё хлопнул меня по спине."
                show shou mis at r3
                voice "audio/voice/E1/D2/S11/Shou/48.ogg"
                ss "Разве ты не рад, что у тебя есть я, который присмотрит за тобой?"
                pf "Да, ты как моя крестная фея."
                show shou ske at r3
                show confused:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Shou/49.ogg"
                ss "Да!--Подожди, что?"
                show kaori mis at cc
                show shou cur at r3
                with dissolve
                "Каори фыркнула, удивив нас обоих--особенно Сё. Он продолжал смотреть на неё, и она снова нахмурилась."
                show kaori thi at cc
                voice "audio/voice/E1/D2/S11/Kaori/45.ogg"
                ki "Что?"
                show shou smi at r3
                voice "audio/voice/E1/D2/S11/Shou/50.ogg"
                ss "Я просто не знал, что ты можешь смеяться."
                "Она сжала кулаки."
                show kaori ang at cc
                show vein:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/46.ogg"
                ki "Что это должно значить?!"
                show shou hap at r3
                voice "audio/voice/E1/D2/S11/Shou/51.ogg"
                ss "Ничего!"
                show kaori dis at cc
                "Она расслабилась и вернула руки на грудь."
                voice "audio/voice/E1/D2/S11/Kaori/47.ogg"
                ki "Если я не смеюсь над твоими тупыми шутками, то это не значит, что у меня нет чувства юмора."
                show shou mis at r3
                "Он наклонился ко мне и понизил голос."
                voice "audio/voice/E1/D2/S11/Shou/52.ogg"
                ss "Не слушай ее. Я веселый."
                    
            "Ты тоже.":
                pf "Когда тренировка?" 
                "Каори и Сё обменялись взглядом."
                voice "audio/voice/E1/D2/S11/Shou/53.ogg"
                ss "А ты предан делу!"
                pf "Ну, квалификация через два дня, так что нам нужно практиковаться как можно скорее."
                show kaori smi at cc
                "Каори скрестила руки, но ее уголок её губ дёрнулся, будто она довольна моей нужде в практике." 
                ki "Хммм…"
        voice "audio/voice/E1/D2/S11/Shou/54.ogg"
        show note:
            xoffset 1175
            yoffset 20
            xzoom .75
            yzoom .75
        ss "В любом случае, добро пожаловать в команду, бро!"
        pf "Спасибо."
    
    
    elif (E1D2S3_MetKaoriWasRudeYesHelmet == 1):
        show shou hap at cc
        "Сё повернулся к рыжей."
        voice "audio/voice/E1/D2/S11/Shou/65.ogg"
        ss "Эй, перестань вести себя грубо!"
        show kaori ann at r3
        "Она подняла руку и прервала Сё." 
        voice "audio/voice/E1/D2/S11/Kaori/48.ogg"
        ki "Не сейчас, Сё. ты не видишь, что я разговариваю по телефону? Я пытаюсь узнать, смогу ли я найти ублюдка, который пытался сбить меня сегодня. Его мотоцикл должен быть где-то на парковке. Я найду его!" 
        "О, дерьмо. Она говорит обо мне! Я должен был узнать её."
        show shou mis at cc
        stop music fadeout 3
        voice "audio/voice/E1/D2/S11/Shou/66.ogg"
        ss "Но Каори, у меня есть кто-то, кто может заполнить последнее место в нашей команде." 
        show kaori ske at cc
        show shou smi at r3:
            xzoom -1
        with dissolve
        "Каори взглянула на меня, когда Сё указал в мою сторону. Она быстро осмотрела сверху донизу."
        play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 1
        show mayu neu at l3
        voice "audio/voice/E1/D2/S11/Kaori/49.ogg"
        ki "Ты кто?" 
        menu: 
            "Я парень, который чуть не сбил тебя. Извини.":
                $ E1D2S11_ComingCleanAboutRunningOverKaori = 1
                pf "Я парень, которому нужно извиниться перед тобой. Кажется, я чуть не сбил тебя этим утром."
                show kaori ann at cc
                "Она нахмурилась." 
                show question:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/50.ogg"
                ki "Ты что?" 
                pf "Эх, да. Я почти сбил девушку на зелёном светофоре."
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
                ki "ты идиот! Светофор был КРАСНЫЙ!"
                show kaori ann at cc
                "Я отчетливо помнил, как светофор был зеленым, но раз мне нужно одобрение этой девушки, чтобы присоединиться к команде, то прикусил язык." 
                pf "Ну, в любом случае, мне очень жаль. Надеюсь, ты простишь меня." 
    
            "Человек твоей мечты!":
                "Я надел свою самую очаровательную улыбку." 
                pf "Просто парень, который собирается воплотить в жизнь все твои мечты."
                show kaori neu at cc
                "Она просто смотрит на меня." 
                show kaori ske b1 at cc
                show question:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/55.ogg"
                ki "Ч-Что?"
                pf "Ты слышала меня."
                "Я подмигнул ей."
                voice "audio/voice/E1/D2/S11/Kaori/56.ogg"
                ki "Хм?"
                show tsuBlush:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori thi b1 at cc
                "Явно взволнованная, она хмурилась, но, похоже, не знала, что делать с собой."
                show shou hap at r3
                voice "audio/voice/E1/D2/S11/Shou/71.ogg"
                ss "Он наш билет к победе, Каори!"
                show kaori neu at cc
                "Тупая улыбка Сё похоже вернула Каори в чувства."
                show kaori mis at cc
                voice "audio/voice/E1/D2/S11/Kaori/57.ogg"
                ki "Не удивительно, что ты так хорошо поладил с Сё. Ты такой же идиот, как и он."
                #pf and Shou speak at the same time
                show shou mis at r3
                "Мы оба" "Эй!"
                show shou cur at r3
                show exclamation:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                "Сказали мы одновременно и удивленно посмотрели друг на друга."
                show kaori dis at cc
                "Каори смотрит между нами и издала долгий, раздраженный вздох." 
    
            "Я новенький.":
                pf "Я переведённый ученик." 
                show kaori dis at cc
                "Каори положила руки на бёдра и быстро оглянула меня."
                show kaori ske at cc
                voice "audio/voice/E1/D2/S11/Kaori/59.ogg"
                ki "Хм… Откуда ты перевёлся?" 
                pf "CINY в Штатах."
                show kaori neu at cc
                "Она продолжада смотреть на меня."
                show kaori ske at cc
                show question:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S11/Kaori/60.ogg"
                ki "Мы раньше не встречались?"
                "Сердце колотилось в груди. Она не может же знать, что это был я? Я был уверен, что одел шлем. {w}Или нет?"
                pf "Эм, нет."
                show kaori neu at cc
                "Она прищюрилась, но в в итоге кивнула." 
    
        if (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
            show shou ske at r3
            show question:
                xoffset 1175
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S11/Shou/67.ogg"
            ss "Вы знаете друг друга?" 
            show kaori ang at cc
            show vein:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S11/Kaori/52.ogg"
            ki "Этот придурок пытался сегодня убить меня! Как ты мог пригласить его в нашу команду?"
            show mayu sad at l3
            show kaori ann at cc
            pf "Я не пытался тебя убить!" 
            show kaori dis at cc
            voice "audio/voice/E1/D2/S11/Kaori/53.ogg"
            ki "Тогда почему ты проехал на красный сигнал? Я никогда не позволю тебе присоединиться к моей команде."
            show shou neu at r3
            voice "audio/voice/E1/D2/S11/Shou/68.ogg"
            ss "Но Каори, нам нужен ещё один человек."
            show kaori ann at cc
            stop music fadeout 3
            voice "audio/voice/E1/D2/S11/Kaori/54.ogg"
            ki "Мы найдём кого-нибудь. Кого угодно, но не его."
            show shou thi at r3
            "Сё извиняющеся улыбнулся мне." 
            voice "audio/voice/E1/D2/S11/Shou/69.ogg"
            ss "Прости…"
            show mayu sad at l3
            pf "Не волнуйся об этом."
            show shou ner at r3
            voice "audio/voice/E1/D2/S11/Shou/70.ogg"
            ss "Полагаю, ещё увидимся."
            hide mayu
            hide kaori
            hide shou
            with Dissolve(2.5)
            "Я кивнул, а потом ушёл. Я не знаю почему думал, что говорить ей, кем я был, было бы хорошей идеей." 
            jump E1D2S12
    
        else:
            show kaori dis at cc
            "Каори сложила руки на груди."
            voice "audio/voice/E1/D2/S11/Kaori/58.ogg"
            ki "Тебе повезло, нам нужен ещё один член в команду."
            show shou hap at r3
            show mayu hap at l3
            "Сё усмехнулся, и похлопал по спине"
            show note:
                xoffset 1175
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S11/Shou/73.ogg"
            ss "Добро пожаловать на борт!" 
            show shou smi at r3
            pf "С нетерпением жду этого." 
    
    show kaori neu at r3
    show shou hap at cc
    with dissolve
    stop music fadeout 3
    voice "audio/voice/E1/D2/S11/Shou/22.ogg"
    ss "Итак, тебе, наверное, интересно, зачем нам нужен ещё один член команды."
    #Day Out or Open Road here
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
    show mayu neu at l3
    "Вообще-то нет, но раз он упомянул это…"
    pf "Да, немного."
    show shou mis at cc
    voice "audio/voice/E1/D2/S11/Shou/23.ogg"
    ss "По сути, мы с Каори были частью этой супер классной команды, но потом они перестали быть классными, поэтому мы ушли."
    show kaori ske at r3
    voice "audio/voice/E1/D2/S11/Kaori/12.ogg"
    ki "Вау, Сё, в этот раз ты не заговорился."
    show shou cur at cc
    "Он притворился обиженным."
    show shou ner at cc
    show crying:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S11/Shou/24.ogg"
    ss "Ты ранила меня! Все мои рассказы короткие."
    show shou hap at cc
    voice "audio/voice/E1/D2/S11/Shou/24_1.ogg"
    ss "Помните, когда я рассказал вам о моем дне рождения, где все появились в той же одежде, что и я?"
    "Он повернулся ко мне."
    show shou mis at cc
    voice "audio/voice/E1/D2/S11/Shou/25.ogg"
    ss "На самом деле, это довольно хорошая история. Итак, в основном, я вырос в этом виде -- Маю знает где--"
    show kaori dis at r3
    voice "audio/voice/E1/D2/S11/Kaori/13.ogg"
    ki "Не поддерживай его!"
    show mayu smi at l3
    "Маю слабо улыбнулась."
    show kaori neu at r3
    voice "audio/voice/E1/D2/S11/Kaori/14.ogg"
    ki "Во всяком случае, дело в том, что мы были в команде, но ушли, потому что команда превращалась во что-то, с чем мы не соглашались."
    show shou smi at cc
    voice "audio/voice/E1/D2/S11/Shou/26.ogg"
    ss "Кроме Маю. Она первогодка."
    pf "О! Я не знал этого."
    show shou hap at cc
    voice "audio/voice/E1/D2/S11/Shou/27.ogg"
    ss "Да уж! Она получила целую кучу приглашений в другие команды, но решила присоединиться к нам. Нам очень повезло, что она с нами."
    pf "Как ты выбрала эту команду?"
    show mayu thi b1 at l3 with dissolve
    show dots:
        xoffset 230
        yoffset 135
        xzoom .75
        yzoom .75
    "Маю некомфортно мнётся под моим взглядом."
    voice "audio/voice/E1/D2/S11/Mayu/7.ogg"
    ma "Я доверяю Сё."
    "Я ждал, что она скажет больше, но нет."
    show shou smi at cc
    show kaori dis at r3
    "Каори нетерпеливо стучала ногой."
    voice "audio/voice/E1/D2/S11/Kaori/15.ogg"
    ki "Ну, теперь, когда ты всё это знаешь. Вступаешь к нам?"
    "Они все немного странны по-своему, но я думаю, что могу поладить с ними ... даже с Каори."
    $ E1D2S11_JoinedTheTeam = 1
    pf "Да, я вступаю."
    show shou hap at cc
    voice "audio/voice/E1/D2/S11/Shou/28.ogg"
    ss "Отлично!"
    show kaori thi at r3
    "Каори проверила свой телефон."
    show kaori neu at r3
    show exclamation:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S11/Kaori/16.ogg"
    ki "Я кучу времени потратила, разговария с вами, и мне нужно идти домой."
    hide kaori with dissolve
    "Быстро махнув, она вышла."
    show shou smi at cc
    voice "audio/voice/E1/D2/S11/Shou/29.ogg"
    ss "Мы тоже должны идти."
    show mayu smi at l3
    "Маю кивнула."
    pf "Да, я тоже."
    show shou mis at cc
    voice "audio/voice/E1/D2/S11/Shou/30.ogg"
    ss "Увидимся завтра?"
    pf "Да, увидимся."
    hide mayu
    hide shou
    with dissolve
    "Мы попрощались и разошлись."
    
    
        
    jump E1D2S12
