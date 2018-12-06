label E1D2S5:

    stop music fadeout 3
    voice "audio/voice/E1/D2/S5/Receptionist/1.ogg"
    "Секретать" "Следующий!"
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
    "Очередь спокойно ползёт, и вот наконец, когда вроде бы прошла вечность, я подошёл к стойке." 
    show receptionist extra at cc with dissolve
    pf "Hi, I need a parking pass for a motorcycle--"
    voice "audio/voice/E1/D2/S5/Receptionist/2.ogg"
    "Секретать" "Вам нужно заполнить запрос онлайн на сайте. Подтверждение занимает от одной до двух недель, и если его одобрят, то пропуск отправят вам по почте."
    "Прежде чем я успел ответить, он посмотрел за меня."
    voice "audio/voice/E1/D2/S5/Receptionist/3.ogg"
    "Секретать" "Следующий!" 
    pf "Подожди-ка!"
    "Я положил руки на стол."
    
    "Он сердито посмотрел на меня."
    voice "audio/voice/E1/D2/S5/Receptionist/4.ogg"
    "Секретать" "Что?"
    
    menu:
        "Подкупить его.":
            pf "Я надеялся, что этот процесс мог бы пройти быстрее."
            "Я наклонился и ослепил его самой очаровательной улыбкой."
            pf "Вы кажетесь разумным человеком. Вы уверены, что мы не можем… {i}договориться{/i}?"
            show storm:
                xoffset 675
                yoffset 25
                xzoom .75
                yzoom .75
            $renpy.pause(1)
            "He narrows his eyes."
            voice "audio/voice/E1/D2/S5/Receptionist/5.ogg"
            "Секретарь" "Что именно ты предлагаешь?"
            menu:
                "Предложить подкупить его деньгами (1).":
                    "Я что-то написал в ближайшем листе и предложил его перевёрнутым секретарю. Он подозрительно посмотрел на меня. Я дважды кивнул с уверенной ухмылкой."
                    pf "Я уверен, сумма более чем щедра, сэр."
                    "Он осторожно перевернул бумагу…  и его выражение померкло."
                    voice "audio/voice/E1/D2/S5/Receptionist/6.ogg"
                    "Секретарь" "Тут написано {i}один{/i} credit."
                    "Я дважды коснулся своего носа и подмигнул."
                    "Он смял лист и бросил его в мусорную корзину."
                    voice "audio/voice/E1/D2/S5/Receptionist/13.ogg"
                    "Секретарь" "Следующий!"
    
                    menu:
                        "Время предложить {i}два{/i} credits!":
                            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 2
                            pf "Стоп! Подождите-ка. Слушай, ты ведешь жесткую сделку… но я сыграю в эту игру."
                            "Я что-то написал на другом листочке, прежде чем перевернул его. Он перевернул его, быстро взглянул, затем шлёпнул им по стойке. Внезапно он встал на ноги, его глаза были раскаленны."
                            show vein:
                                xoffset 675
                                yoffset 25
                                xzoom .75
                                yzoom .75
                            voice "audio/voice/E1/D2/S5/Receptionist/7.ogg"
                            "Секретарь" "Проваливай!"
                            "Я поднял руки."
                            pf "Воу, успокойся."
                            voice "audio/voice/E1/D2/S5/Receptionist/8.ogg"
                            "Секретарь" "Не говори мне успокоиться!"
                            pf "Знаете что? Я прекращаю переговоры до тех пор, пока вы не будете более уравновешенным."
                            hide receptionist extra with dissolve
                            stop music fadeout 1
                            "Я спокойно отошёл от стойки, прежде чем он успел ответить. Я слышал его ярость, по коллеги успокаивали его. Боже, почему он так вспылил? Думаю, я просто заполню документы онлайн, дома вечером."
                            play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
                            if (E1D2S2_YuunaComesWithYouPass == 0):
                                jump E1D2S5_NoYuunaJump
    
                            elif (E1D2S2_YuunaComesWithYouPass == 1):
                                jump E1D2S5_YesYuunaJump
    
                        "Просто предлоить ему 50 credits.":
                            jump E1D2S5OfferFifty
    
                        "Это безнадёжно.":
                            pf "Alright, whatever."
                            "Бесполезно продолжать, если он даже не ценит {i}целый{/i} й credit. Просто заполню документы онлайн."
                            hide receptionist extra with dissolve
                            "Я ушёл."
                            if (E1D2S2_YuunaComesWithYouPass == 0):
                                jump E1D2S5_NoYuunaJump
    
                            elif (E1D2S2_YuunaComesWithYouPass == 1):
                                jump E1D2S5_YesYuunaJump
    
                "Предложить взятку суммой 50 credits.":
                    label E1D2S5OfferFifty:
                        $ E1D2S5_offer50directly = 1
                        "Я набросал сумму на листе и предложил его ему перевёрнутым."
                        "Он взглянул на письмо, потом нахмурился на меня, но выдержал его взгляд."
                        pf "Либо бери, либо отказывайся."
    
            if (E1D2S5_offer50directly == 1):
                "Он кивнул."
                voice "audio/voice/E1/D2/S5/Receptionist/11.ogg"
                "Секретарь" "Хорошо."
    
            if (E1D2S5_offer50directly == 0):
                "Он продолжал смотреть на меня, его подозрение росло, но я отказывался сдаваться. Через несколько секунд он кивнул."
                voice "audio/voice/E1/D2/S5/Receptionist/9.ogg"
                "Секретарь" "Это более приемлемо."
    
            "Он что-то напечатал на компьютере, потом открыл ящик и положил пластиковую карточку на стойку."
    
            $ E1D2S5_bribedforpass = 1
            $ E1D2S5_gotbikepass = 1
            voice "audio/voice/E1/D2/S5/Receptionist/10.ogg"
            "Секретарь" "Вот твой пропуск. Если потеряешь, то придётся платить за замену. Чем-то ещё могу помочь?"
            pf "Нет, спасибо."
            voice "audio/voice/E1/D2/S5/Receptionist/13.ogg"
            "Секретарь" "Следующий!"
            hide receptionist extra with dissolve
            "Я положил пропуск в кошелёк и направился к выходу. Это один способ добиваться цели."
            if (E1D2S2_YuunaComesWithYouPass == 0):
                jump E1D2S5_NoYuunaJump
    
            elif (E1D2S2_YuunaComesWithYouPass == 1):
                jump E1D2S5_YesYuunaJump
    
    
        "Кем он себя возомнил?":
            "Я выпрямился и посмотрел на него."
            pf "Мне кажется, вы меня не услышали. Я хочу пропуск на парковку."
            voice "audio/voice/E1/D2/S5/Receptionist/12.ogg"
            "Секретарь" "А я хочу встретить пилота, который не будет самовлюблённым мудаком. Похоже, мы не получим то, чего хотим."
            "Он посмотрел за меня прежде, чем я успел ответить."
            voice "audio/voice/E1/D2/S5/Receptionist/13.ogg"
            "Секретарь" "Следующий!"
    
            menu:
                "Он реально меня бесит.":
                    "Я сжал руки в кулаки и ударил по стойке."
                    pf "Слушай, ты самодовольный--"
                    voice "audio/voice/E1/D2/S5/Security/1.ogg"
                    "Охрана" "Проблемы?"
                    show guard extra at l3 with dissolve
                    "Надо мной навис крепкий охранник. На его лице был шрам, проходящий через глаз до подбородка."
                    pf "Проблемы? Нет, конечно же нет."
    
                    "Секретать довольно узмыльнулся и смотрел на меня, пока разговаривал с охранником."
                    voice "audio/voice/E1/D2/S5/Receptionist/14.ogg"
                    "Секретарь" "Он как раз собирался уходить."
                    "Я продолжал смотреть на него, пока он не перестал улыбаться и не отвёл глаза. Я легко улыбнулся."
                    pf "Да, как раз собирался."
                    "Под ледяным взглядом охранника, обжигающим спину, я беззаботно ушёл от стойки."
                    hide guard extra
                    hide receptionist extra
                    with dissolve
                    if (E1D2S2_YuunaComesWithYouPass == 0):
                        jump E1D2S5_NoYuunaJump
    
                    elif (E1D2S2_YuunaComesWithYouPass == 1):
                        jump E1D2S5_YesYuunaJump
    
                "Забудь, это бесполезно.":
                    pf "Плевать."
                    "Этот парень придурок. Я просто заполню документы онлайн, или приду потом, когда там будет сидеть более разумный человек."
                    hide receptionist extra with dissolve
                    if (E1D2S2_YuunaComesWithYouPass == 0):
                        jump E1D2S5_NoYuunaJump
    
                    elif (E1D2S2_YuunaComesWithYouPass == 1):
                        jump E1D2S5_YesYuunaJump
    
    
        "Давай поговорим об этом.":
            pf "Таааааак…"
    
            "Это ещё один из таких моментов, когда я хотел бы сначала думать, а потом говорить."
            "Он ждал, пока я закончу, но я видел нетерпение в его глазах. {w}Сейчас или никтогда!"
    
            menu:
                "Флиртовать.":
                    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 2
                    "Я посмотрел на него своим \"лучшим\" взглядом. Он инстинктивно отстранился от меня. Не совсем то, к чему я стремился, но работаем с чем есть."
                    show question:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    "Я посмотрел ему в глаза, и кокетливо усмехнулся. Он смущенно наклонился в другую сторону."
    
                    pf "Кто-нибудь говорил тебе, что у тебя очень красивые глаза?"
                    "Его щёки покраснели, но он нахмурился, когда посмотрел на очередь позади меня."
                    voice "audio/voice/E1/D2/S5/Receptionist/15.ogg"
                    "Администратор" "Слушай, у меня нет времени на это--"
    
                    "Я чуть отошёл. Моя улыбка стала ещё шире, и я поиграл бровями."
    
                    pf "Ой да ладно, милашка. Теперь ты просто дразнишь меня. У тебя просто… ангельский голос."
                    show shoBlush:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D2/S5/Receptionist/16.ogg"
                    "Администратор" "Ч-Что?!"
    
                    "Его лицо покраснело, и рот двигался в немом ответе, словно пытался найти правильные слова."
    
                    pf "Ты такой очаровательный, когда смущаешься."
    
                    "Я подмигнул ему."
                    show tsuBlush:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D2/S5/Receptionist/17.ogg"
                    "Администратор" "Я--Ты!--Что?--Почему??--Вот--Просто возьми это!"
    
                    $ E1D2S5_gotbikepass = 1
                    $ E1D2S5_flirtforpass = 1
                    "Он яростно открыл ящик и бросил мне пластиковую карточку, прежде чем захлопнуть его. Игриво улыбаясь, я взял её."
    
                    pf "Спасибо."
                    stop music fadeout 4
                    "Я подмигнул и послал воздушный поцелуй, и он быстро опустил взгляд. Я развернулся и ушёл пока он ворчал сам себе. {w}Через несколько секунд он понял, что очередь всё ещё ждала."
                    hide receptionist extra with dissolve
                    "Ага, всё-таки получил его."
                    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
                    if (E1D2S2_YuunaComesWithYouPass == 0):
                        jump E1D2S5_NoYuunaJump
    
                    elif (E1D2S2_YuunaComesWithYouPass == 1):
                        jump E1D2S5_YesYuunaJump
    
                "Попытаться вразумить.":
                    pf "Это такой сложный процесс для чего-то такого простого. Должен же быть путь попроще."
                    show storm:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    "Мужчина постукивал по столу пальцем."
                    voice "audio/voice/E1/D2/S5/Receptionist/18.ogg"
                    "Администратор" "Нет. Если у вас возникла проблема с этим процессом, вы можете отправить жалобу онлайн."
    
                    pf "Это всего лишь пропуск на парковку."
                    voice "audio/voice/E1/D2/S5/Receptionist/19.ogg"
                    "Администратор" "У меня нет времени на это."
    
                    "Он попытался посмотреть на толпу позади меня, но я заблокировал обзор."
    
                    pf "Да ладно тебе!"
    
                    "Я выдержал его взгляд. Только я подумал, что он собрался сдаться, его выражение ужесточилось."
                    show vein:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D2/S5/Receptionist/20.ogg"
                    "Администратор" "Нет. Следующий!"
                    hide receptionist extra with dissolve
                    "Я вздохнул, сдавшись. До него не добраться, поэтому я развернулся и пошёл."
                    if (E1D2S2_YuunaComesWithYouPass == 0):
                        jump E1D2S5_NoYuunaJump
    
                    elif (E1D2S2_YuunaComesWithYouPass == 1):
                        jump E1D2S5_YesYuunaJump
    
                "Придумать грустную историю.":
                    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 2
                    "I sniffle."
    
                    pf "Я… Я потерял свой пропуск самым ужасным способом…"
                    show question:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    "Я закрыл руками лицо. {w}Через несколько секунд я посмотрел сквозь пальцы. Он смотрел на меня как с раздражением, так и с замешательством. Я ещё раз приглушённо всхлипнул, и он вздохнул."
                    voice "audio/voice/E1/D2/S5/Receptionist/21.ogg"
                    "Администратор" "Ну и как это могло произойти?"
    
                    "Я опустил руки, все признаки горя исчезли с лица. Он удивлённо моргнул и прищурился на полное изменение моего поведения."
    
                    pf "Нуу… Я шёл в академию, думая о своём, когда всё вокруг потемнело. Пока все останавливились, я продолжал идти. К тому времени, когда я заметил, что что-то не так, надо мной был космический корабль. Из корабля светил яркий свет, и все стало ослепительно белым. Следующее, что я помнил - я внутри космического корабля и окружён инопланетянами."
                    show drop:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    pf "Как-то мы могли общаться и понимать друг друга. Они водили меня по кораблю, показывая каждую его часть. Вообще-то, мне удалось встретиться с каждым пришельцем на борту. Они сказали, что прилетели на Землю, чтобы заключить сделку с нашим правителем и стать союзниками. По всей видимости, в ближайшем будущем произойдет межгалактическая война. Я сказал им, что у Земли нет единого правителя, и разными странами управляют разные люди."
    
                    pf "Каким-то образом это перешло в дебаты о том, что появилось сначала, курица или яйцо, пока они, наконец, не признались, что на самом деле они не знали, что такое курица или яйцо. На самом деле, мне пришлось нарисовать для них картину, и я не самый большой художник, поэтому они до сих пор не знают, что это такое - они выяснили, что такое яйцо, потому что это легко нарисовать, даже для меня."
    
                    pf "Тогда я понял который уже час и сказал им, что должен идти в академию, иначе бы опоздал."
                    show storm:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    pf "Они хотели обменять что-то в память о встрече, и хотели мой мозг. Но я сказал им, что он нужен мне для выживания. Поэтому они сказали, что у них идеальное решение. Они вывели зонд, и хотя я пытался бороться с ним--ну, я бы не хотел вдаваться в подробности…" 
    
                    "I hang my head at my traumatising \"памяти\", но взглянул на администратора краем глаза. Он смотрел, ошеломлённо."
    
                    pf "В любом случае, после этого крайне неудобного и чрезмерно личного опыта,я искал способ выбраться из корабля, не убив себя, когда мой пропуск на парковку выпал из кармана прямиком в небытие! Тогда всё ствло чёрным, и я оказался перед академией… {w}И вот теперь я тут."
                    show dots:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    "Он закрыл рот и нахмурился."
                    voice "audio/voice/E1/D2/S5/Receptionist/22.ogg"
                    "Администратор" "... Ты закончил?"
    
                    "Я кивнул."
                    voice "audio/voice/E1/D2/S5/Receptionist/23.ogg"
                    "Администратор" "Отлично. Следующий!"
                    stop music fadeout 2.0
                    "Я стоял ошеломленный. Как моя вполне правдоподобная история не впечатлила его?"
                    "Ну хорошо. {w}Этот парень не знал бы хорошей истории, даже если бы был её частью."
                    hide receptionist extra with dissolve
                    "Я развернулся и ушёл."
                    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
                    if (E1D2S2_YuunaComesWithYouPass == 0):
                        jump E1D2S5_NoYuunaJump
    
                    elif (E1D2S2_YuunaComesWithYouPass == 1):
                        jump E1D2S5_YesYuunaJump
    
                "Моя собака сьела его.":
                    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 2
                    "Внезапно все мысли исчезли. Я почесал затылок, стараясь тянуть время."
    
                    pf "Я… Эм…"
    
                    "Он прищурился. Когда его взгляд начал двигаться к ученику позади меня, я выдал первое, что пришло в голову." 
    
                    pf "Моя собака сьела его!"
                    show dots:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    $renpy.pause(2.5)
                    voice "audio/voice/E1/D2/S5/Receptionist/24.ogg"
                    "Администратор" "…Твоя собака сьела пропуск."
    
                    pf "Эм, да."
                    voice "audio/voice/E1/D2/S5/Receptionist/25.ogg"
                    "Администратор" "Всё в порядке?"
    
                    pf "Ну, я полагаю, нет. Он всё-таки в собаке."
                    voice "audio/voice/E1/D2/S5/Receptionist/26.ogg"
                    "Администратор" "Я не про пропуск; а про твою {i}собаку{/i}. С ней всё в порядке?"
    
                    pf "А, эм, да. Конечно. Моя собака в порядке."
                    voice "audio/voice/E1/D2/S5/Receptionist/27.ogg"
                    "Администратор" "Хорошо. Следующий!"
    
                    pf "Эй, подождите-ка! Что насчёт пропуска?"
                    voice "audio/voice/E1/D2/S5/Receptionist/28.ogg"
                    "Администратор" "Может быть твоя собака вернёт его."
    
                    "The smile he flashes me doesn't reach his eyes." 
                    voice "audio/voice/E1/D2/S5/Receptionist/13.ogg"
                    "Администратор" "Следующий!" 
                    hide receptionist extra with dissolve
                    "Я вздохнул. Ну, это не сработало. Побеждённый, я развернулся и начал уходить."
                    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
                    if (E1D2S2_YuunaComesWithYouPass == 0):
                        jump E1D2S5_NoYuunaJump
    
                    elif (E1D2S2_YuunaComesWithYouPass == 1):
                        jump E1D2S5_YesYuunaJump
    
    
    if (E1D2S2_YuunaComesWithYouPass == 1):
        label E1D2S5_YesYuunaJump:
            if (E1D2S5_gotbikepass == 0):
                show yuuna smi at cc with dissolve
                "Внезапно рядом со мной оказалась Юна. Её улыбка дрогнула, когда увидела моё лицо."
                show yuuna neu at cc
                voice "audio/voice/E1/D2/S5/Yuuna/1.ogg"
                ym "Всё хорошо?"
    
                "Я пожал плечами."
    
                pf "Я не смог получить пропуск."
                show yuuna thi at cc
                "Она нахмурилась. Her eyebrows knit delicately together."
                show yuuna neu at cc
                voice "audio/voice/E1/D2/S5/Yuuna/2.ogg"
                ym "Хмм… Подожди."
                hide yuuna with dissolve
                "Она подошла к столу, к разочарованию студента в очереди. Секретать похоже нервничал из-за этого."
    
                "Я не слышал, что она говорила, но похоже было стыдно, и он вытащил пропуск из ящика. Как только она вырвала из его рук пропус, то поблагодарила лёгким кивком, который он вернул в ответ."
                show yuuna smi at cc with dissolve
                "Юна вернулась с лёгкой улыбкой и протянула пропуск."
                voice "audio/voice/E1/D2/S5/Yuuna/3.ogg"
                ym "Ну вот."
    
                "Как она это сделала? Может, использовала магию. Или она может гипнотизировать взглядом--"
                
                show yuuna ner at cc
                voice "audio/voice/E1/D2/S5/Yuuna/4.ogg"
                ym "Эм…"
    
                "Точно. Пропуск."
    
                pf "Ох, да. Спасибо."
                
                show yuuna smi at cc
    
                $ E1D2S5_gotbikepass = 1
                "Она убылнулась."
                voice "audio/voice/E1/D2/S5/Yuuna/5.ogg"
                ym "Без проблем."
    
                "Я взял пропуск из её рук и положил в кошелек. Мы вышли из офиса пока в него вливалась ещё одна толпа студентов."
                
    
            elif (E1D2S5_gotbikepass == 1):
                show yuuna smi at cc with dissolve
                "Внезапно, я увидел улыбающееся лицо Юны."
                voice "audio/voice/E1/D2/S5/Yuuna/6.ogg"
                ym "Как прошло?"
    
                pf "Я без проблем получил пропуск."
                show exclamation:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                show yuuna sur at cc
                "Её глаза широко раскрылись."
    
                pf "Что такое?"
                show yuuna hap at cc
                voice "audio/voice/E1/D2/S5/Yuuna/7.ogg"
                ym "Ох, ничего. Я просто немного удивлена, что ты так легко получил пропуск. Обычно они заставляют заполнять документы онлайн."
    
                if (E1D2S5_bribedforpass == 1):
                    pf Ну что я могу сказать? Я находчив."
                    show yuuna cur at cc
                    voice "audio/voice/E1/D2/S5/Yuuna/8.ogg"
                    ym "Ах... Интересно."
    
                elif (E1D2S5_flirtforpass == 1):
                    "Я подмигнул ей."
                    pf "У меня есть словесный способ."
                    show yuuna cur at cc
                    voice "audio/voice/E1/D2/S5/Yuuna/9.ogg"
                    ym "Понятно..."
                    
                show dots:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                "Кажется, она не уверена как отреогировать на это."
                pf "Shall we get going?"
                show yuuna smi at cc
                "Она кивнула. Мы вышли из офиса пока в него вливалась ещё одна толпа студентов."
    
            stop music fadeout 3
            hide yuuna with dissolve
            scene bg campus building day with fade
            play ambient "audio/ambience/Campus.ogg" fadein 3
            
            "Кажется уже меньше студентов толпилось вокруг, и больше спешило на занятия. Я проверил время.Двадцать пять минут до начала урока."
            play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
            show yuuna smi at cc
            voice "audio/voice/E1/D2/S5/Yuuna/10.ogg"
            ym "Ты знаешь, где твой урок?"
    
            pf Да, он тут."
    
            "Я показал ей карту кампуса на телефоне. Нельщая подсвеченная точка показывает, где я должен находиться."
            
            show yuuna hap at cc
            voice "audio/voice/E1/D2/S5/Yuuna/11.ogg"
            ym "О, это близко! Я могу пройтись с тобой."
    
            pf "Это было бы замечательно."
            
            scene bg campus main day with fade
            
            "Мы направились по одному из коротких путей. Он вёл прямо к царственному зданию с высокими, выгнутыми окнами. Лишь несколько студентов блуждали."
            show yuuna smi at cc with dissolve
            voice "audio/voice/E1/D2/S5/Yuuna/12.ogg"
            ym "Вот и всё."
    
            pf "Спасибо, ты очень помогла."
            show yuuna smi at cc
            voice "audio/voice/E1/D2/S5/Yuuna/13.ogg"
            ym "Без проблем."
    
            pf "А ты идёшь на психологию?"
            voice "audio/voice/E1/D2/S5/Yuuna/14.ogg"
            ym "Уху."
    
            pf "Какие ещё предметы у тебя в этом семестре?"
            
            show yuuna thi at cc
            voice "audio/voice/E1/D2/S5/Yuuna/15.ogg"
            ym "Эм..."
    
            "Она достала телефон. я сделал то же самое, и мы изучили расписание."
    
            show yuuna smi at cc
            voice "audio/voice/E1/D2/S5/Yuuna/16.ogg"
            ym "Ну, похоже в пятницу у нас совместная история робототехники."
    
            pf "Полагаю, это означает, что мы будем видеться чаще."
            
            show yuuna hap at cc with dissolve
    
            "Мы оба улыбнулись."
    
            "Я заметил время на телефонк. Пятнадцать минут до занятий."
            
            show yuuna smi at cc
    
            pf "Урок скоро начнётся."
    
            "Юна глянула на свой телефон, прежде чем положить его обратно в карман."
            
            show yuuna cur at cc
            voice "audio/voice/E1/D2/S5/Yuuna/17.ogg"
            ym "Ох, точно! Я должна идти, или я опоздаю. Увидимся в пятницу?"
    
            "Я кивнул, и мы разошлись."
            hide yuuna with dissolve
            "Через несколько шагов, я понял, что у меня нет способа связаться с ней, кроме как на уроке в пятницу. Я развернулся, но она уже была довольно далеко."
    
            $ qtebase = 5
            $ qtetotal = qteintel + qtebase
            $ t_var = qtetotal
            show screen timer_scr(place="E1D2S5_YuunaNoNumber")
            menu:
                "Спросить у неё номер телефона.":
                    $ renpy.hide_screen ("timer_scr")
                    $ E1D2S5_GotYuunasNumber = 1
                    pf "Подожди, Юна!"
                    # maybe show her at a distance?
                    show yuuna cur at cc with dissolve:
                        xzoom -0.75
                        yzoom 0.75
                    "Она замерла."
                    show question:
                        xoffset 720
                        yoffset 100
                        xzoom .5
                        yzoom .5
                    voice "audio/voice/E1/D2/S5/Yuuna/18.ogg"
                    ym "Да?"
                    pf "Как думаешь, могу я получить твой номер?"
                    show shoBlush:
                        xoffset 720
                        yoffset 100
                        xzoom .5
                        yzoom .5
                    show yuuna sur b1 at cc with dissolve
                    "Она выглядит удивлённой. Подожди, так определённо не получится."
                    pf "Прости, я имел в виду, что у меня может пявиться несколько вопросов по академии, и ты могла бы помочь--конечно, если ты не возражаешь."
                    show yuuna hap at cc with dissolve
                    "Она хихикнула и кивнула."
                    voice "audio/voice/E1/D2/S5/Yuuna/19.ogg"
                    ym "Конечно."
                    "Я подбежал к ней, и мы обменялись номерами."
                    show yuuna smi at cc
                    pf "Спасибо. Увидимся в пятницу!"
                    voice "audio/voice/E1/D2/S5/Yuuna/20.ogg"
                    ym "Хорошо. Тогда, увидимся."
                    hide yuuna with dissolve
    
                "Забудь об этом.":
                    label E1D2S5_YuunaNoNumber:
                        $ renpy.hide_screen ("timer_scr")
                        "Забудь об этом. {w}Забудь об этом. {w}Ты уже не сможешь спросить её номер."
                        "Она уже слишком далеко. Поговорю с ней в пятницу."
                        
        "Я смотрел как она исчезла за углом."
    
    
    if (E1D2S2_YuunaComesWithYouPass == 0):
        label E1D2S5_NoYuunaJump:
            scene bg campus building day with fade
            "Выйдя из административного здания, я проверил время. Пятнадцать минут до занятий. Надо бы уже пойти туда."
    
    
    jump E1D2S8
