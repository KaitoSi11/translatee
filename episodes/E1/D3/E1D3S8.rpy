label E1D3S8:
    
    
    if (E1D3S1_BikeDrove == 1):
        $renpy.pause(1)
        play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadein 1 fadeout 1
        "Я пошёл на парковку и взял мотоцикл. {w}После поехал домой."
        play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 1 fadeout 1
        $renpy.pause(2.5)
        jump E1D3S9
    
    elif (E1D3S1_BusRide == 1):
        play sound "audio/sfx/Vehicles/Bus Door Open.ogg" fadein 1 fadeout 1
        "Я с нетерпением ждал автобуса. Когда он подъехал, я зашёл в него и сел на ближайшее сидение."
        "Когда автобус тронулся, я уже мечтал о своем прекрасном мотоцикле всю дорогу домой."
        $renpy.pause(1.0)
        jump E1D3S9
    
    elif (E1D3S1_BikeImpounded == 1):
        play ambient "audio/ambience/Campus.ogg" fadein 1 fadeout 1
        scene bg campus main day with fade
        "Мысль о поездке на автобусе домой заставляет желудок скручиваться. Если бы у меня был мой мотоцикл--"
        "Я быстро проверил время. Еще было несколько часов до закрытия. Я мог успеть забрать свой байк обратно."
        stop ambient fadeout 3
        $renpy.pause(1)
        play ambient "audio/ambience/Parking Lot.ogg" fadein 1 fadeout 1
        scene bg campus parking day with fade
        "Я поторопился к парковке и направился прямо к зданию охраны. Тот же самый охранник зевал, смотря камеры. Он смотрел на меня, когда я подошёл, и хрюкнул в знак признания."
        play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 1 fadeout 1
        show guard extra at cc with dissolve
        voice "audio/voice/E1/D3/S8/Guard/1.ogg"
        gua "Нелегальный парковщик. Ты вернулся."
        pf "Да… Я хотел бы забрать свой байк."
        "Он кивнул."
        voice "audio/voice/E1/D3/S8/Guard/2.ogg"
        gua "100 кредитов."
    
        menu:
            "Это грабёж.":
                pf "Это вымогательство! Это не может так дорого стоить!"
                voice "audio/voice/E1/D3/S8/Guard/3.ogg"
                gua "Вот столько это и стоит."
                pf "Но мой байк был всего одну ночь на парковке!"
                voice "audio/voice/E1/D3/S8/Guard/4.ogg"
                gua "Ты хочешь его или нет?"
                pf "Хорошо."
                "Я стиснул зубы, но отдал кредиты."
    
            "Я дам тебе 50 кредитов.":
                "Я переслал 50 кредитов."
                play sound "audio/sfx/Technology/Payment Beep Failure.ogg"
                "Его коипьютер издал сигнал завершения транзакции. Охранник посмотрел на экран, затем нахмурился."
                show dots:
                    xoffset 675
                    yoffset 50
                    xzoom .75
                    yzoom .75
                "Я ухмыльнулся."
                pf "Сдачи не надо."
                voice "audio/voice/E1/D3/S8/Guard/5.ogg"
                gua "Что это за хрень? Нужно 100 кредитов."
                pf "Да, и я отправил кредиты."
                voice "audio/voice/E1/D3/S8/Guard/6.ogg"
                gua "Но ты все ещё должен 50 кредитов."
                pf "Это такая щедрая плата, и ты хочешь ещё больше?"
                show vein:
                    xoffset 675
                    yoffset 50
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S8/Guard/7.ogg"
                gua "У меня нет времени на твои игры."
                "Он начал отворачиваться от меня, когда я переслал ещё 50 кредитов."
                pf "Боже, расслабься."
    
            "Просто заплатить.":
                "Давай просто покончим с этим. Я ворчал под нос, но переслал кредиты."
    
        play sound "audio/sfx/Technology/Payment Beep Success.ogg"
        "После подтверждения транзакции его компьютер издал звуковой сигнал и распечатал квитанцию. Он передал её мне подписать, что я и сделал."
        voice "audio/voice/E1/D3/S8/Guard/8.ogg"
        gua "Теперь тебе надо идти на стоянку."
        pf "Стоянку?"
        voice "audio/voice/E1/D3/S8/Guard/9.ogg"
        gua "Это мимо парковки вне кампуса. Вокруг него металлический забор. Даже ты не сможешь пропустить его."
        "Он ухмыльнулся, и я старался не показывать свое раздражение."
        pf "Спасибо."
        "Я развернулся, но он остановил меня."
        show question:
            xoffset 675
            yoffset 50
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S8/Guard/10.ogg"
        gua "Ничего не забыл?"
        pf "Что?"
        voice "audio/voice/E1/D3/S8/Guard/11.ogg"
        gua "Пароли."
        "Он вручил мне копию квитанции. Там написано две серии чисел."
        pf "Oh, right."
        "Он указал на один пароль, а затем на другой."
        voice "audio/voice/E1/D3/S8/Guard/12.ogg"
        gua "Введи этот пароль, чтобы попасть на штрафстоянку, а этот - чтобы разблокировать замок на своём байке."
        pf "Понял, спасибо."
        stop music fadeout 3
        hide guard extra with dissolve
        scene bg campus impound day closed with fade
        "Я быстро ухожу и направляюсь на стоянку. Подойдя ближе, я легко заметил забор. На воротах был электронный замок."
        ##NEW SOUND NEEDED##play sound "audio/sfx/Technology/Passcode Entry.ogg"
        "Пока я вводил пароль для доступа на стоянку, я оглянулся, проверяя, есть ли тут охранник. Но я был один."
        ##NEW SOUND NEEDED##play sound "audio/sfx/Impacts/Impound Gate Open.ogg"
        scene bg campus impound day with Dissolve(2.5)
        "Ворота открылись с резким визгом, временно разрывая тишину, и я зашёл."
        
        "Там было мало транспорта, и я быстро заметил свой байк."
        ##NEW SOUND NEEDED##play sound "audio/sfx/Technology/Wheel Lock - Locking.ogg" fadeout 5
        "На колесе был блокиратор, и я ввёл второй пароль на боковой панели. {w}Он загорелся зелёным и разблокировался с гулким щелчком."
        play music "audio/music/A Bad Feeling (GAME VERSION).ogg" fadein 1
        "Я нетерпеливо освободил свой байк и вернулся к воротам. {w}Выйдя со стоянки я наткнулся на вчерашнего хулигана с которым было два подло выглядящих парня."
        show bully3 extra at cc with dissolve
        show bully extra at l3 with dissolve
        show bully2 extra at r3 with dissolve:
            xzoom -1
            
        menu:
            "Откуда, чёрт возьми, вы появились?!":
                "Я поставил байк в сторону, прежде чем повернулся лицом к нему."
                pf "Что вы тут делаете?"
                voice "audio/voice/E1/D3/S8/Ken/1.ogg"
                kt "Тебя ждали."
                pf "... Ты имеешь в виду, что были тут всё это время?"
                show vein:
                    xoffset 675
                    yoffset 50
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S8/Ken/2.ogg"
                kt "Завались!"
                "Он что-то показал своим друзьям, которые меня окружали. Они нависли надо мной и зловеще хрустели костяшками пальцев."
                pf "Три на одного? Шансы все еще в мою пользу…"
    
            "Иди сюда, братан.":
                "Я поставил байк в сторону, прежче чем повернулся к ним. Я повращал шеей и похрустел костяшками пальцев. затем усмехнулся."
                pf "Понятно, не хватило в первый раз. Готовы, чтобы вам снова надрали задцины?"
                show vein:
                    xoffset 675
                    yoffset 50
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S8/Ken/3.ogg"
                kt "Ты не будешь таким самодовольным, когда мы закончим с тобой."
                "Он что-то показал своим друзьям, которые меня окружали. Они нависли надо мной и зловеще хрустели костяшками пальцев."
                pf "Ну, это должно быть интересно."
    
            "Притвориться, что их нет, и пройти мимо.":
                "Я едва глянул на них, и когда два друга попытались преградить мне путь, я переезал на байке пальцы ближайшего парня. Он взвизгнул от боли и схватился за ноги, в то время как другой парень наклонился, чтобы помочь ему."
                show question:
                    xoffset 675
                    yoffset 50
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S8/Ken/4.ogg"
                kt "Какого чёрта ты делаешь?!"
                pf "Еду домой."
                show vein:
                    xoffset 675
                    yoffset 50
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S8/Ken/5.ogg"
                kt "Мы ещё не закончили тут!"
                "Он положил руки на байк,чтобы остановить меня."
                "Я замер. {w}A small twitch escapes me."
                "Я спокойно спрыгнул с байка и повернулся к нему. После, я подошёл к хулигану и ударил его в челюсть."
                play sound "audio/sfx/Human/Med_Punch.ogg"
                pf "Ещё раз тронешь мой байк…"
                "Он отступил назад, но собрался, прежде чем упасть. Он потёр челюсть, и его лицо вспыхнуло яростью."
    
        "Он качнулся на меня и я--"
        
        $ qtebase = 2
        $ qtetotal = qteath + qtebase
        $ t_var = qtetotal
        show screen timer_scr(place="E1D3S8_QTEFreeze")
    
        menu: 
            "Замер...":
                $ renpy.hide_screen ("timer_scr")
                label E1D3S8_QTEFreeze:
                    play sound "audio/sfx/Human/light_Punch.ogg"
                    "Мои ноги приковались к земле, когда его кулак упёрся мне в живот."
                    play sound "audio/sfx/Human/light_punch.ogg"
                    "Я задыхался, пытаясь не замечать пульсирующую боль в животе и ударил его по ребрам."
                    play sound "audio/sfx/Human/Med_Punch.ogg"
                    "Он могнулся пополам, но один из его друзей ударил меня в спину."
                    "Острая боль сдала меня временно неподвижным, но мне удалось уйти с пути, когда два лакея бежали на меня. {w}Они старались избегать друг друга, что в итоге заставило одного из них влететь лицом в ворота. {w}Он прикрыл лицо, кровь лилась из носа."
    
            "Трюк...":
                $ renpy.hide_screen ("timer_scr")
                "Я попытался увернуться, но потерял равновесие."
                play sound "audio/sfx/Human/Med_Punch.ogg"
                "Он ударил меня в грудь, выбив из меня воздух, в то время как один из его лакеев пнул меня в колено."
                play sound "audio/sfx/Human/light_punch.ogg"
                "Моя нога сдаёт и я упал."
                "Второй друг попытался ударить меня по ребрам, но я выкрутился в самый последний момент. Я с делал ему подсечку, и он упал на спину. Его голова приземлилась на землю с отвратительным ударом."
    
            "{color=#00ff00}{b}Dodge!{/b}{/color}" if (MCStory == 1):
                jump E1D3S8_MCStory1
            
            "Увернуться!" if (MCStory != 1):
                label E1D3S8_MCStory1:
                $ renpy.hide_screen ("timer_scr")
                play sound "audio/sfx/Human/light_punch.ogg"
                "Я легко уклонился от его удара и едва заблокировал удар его друга. Другой нападавший бежит на меня, и я в последнюю секунду отхожу с его пути. {w}Он остановился, и пока терял равновесие, я толкнул его. Он с отврптительным треском влетает в ворота. Я я легко остался на ногах, в то время как два других окружили меня."
        
        "Хулиган смотрел на меня, его лицо было искажено яростью. Его нога неуклонно приближалась к моему лицу, когда вдруг кто-то встал между нами."
        hide bully extra
        hide bully2 extra
        hide bully3 extra
        with dissolve
        "Он крикнул и упал на землю, когда новая фигура толкнула его в сустав ноги. {w}Один друг полез на новенького, но он заблокировал его с невероятной скоростью."
        ##NEW SOUND NEEDED#
        play sound [ "audio/sfx/Human/Med_Punch.ogg", "audio/sfx/Human/light_punch.ogg", "audio/sfx/Human/Med_Punch.ogg", "audio/sfx/Human/light_punch.ogg", "audio/sfx/Human/Med_Punch.ogg", "audio/sfx/Human/light_punch.ogg", "audio/sfx/Human/Med_Punch.ogg" ]
        "Он бил точно и осыпал друга градом ударов. {w}Последний удар в челюсть заставил атакующего встать на колени."
        
        pf "Берегись!"
        "Новичок повернулся как раз вовремя, чтобы предотвратить удар по затылку. {w}Вместо этого он повернул руку хулигана, чтобы удержать его в захвате. Хулиган взвизгнул от боли и сразу же замер."
        voice "audio/voice/E1/D3/S8/Ken/6.ogg"
        kt "Тьфу! Отпусти меня!"
        "Он смотрит вверх, и внезапно цвет имчез с его лица."
        voice "audio/voice/E1/D3/S8/Akira/1.ogg"
        am "Только если ты пообещаешь оставить этого парня в покое."
        show akira ang at cc with dissolve
        "Его друзья неуверенно поднялись на ноги и медленно отступили."
        voice "audio/voice/E1/D3/S8/Bully1/1.ogg"
        Bully1 "Дерьмо, это Акира?"
        show akira ann at cc
        voice "audio/voice/E1/D3/S8/Bully2/1.ogg"
        Bully2 "Похож на него."
        voice "audio/voice/E1/D3/S8/Bully1/2.ogg"
        Bully1 "Невозможно, чтобы я дрался с ним!"
    
        "Хулиган говорил сквозь стиснутые зубы."
        voice "audio/voice/E1/D3/S8/Ken/7.ogg"
        kt "Да, хорошо, я понял."
        stop music fadeout 3
        "Новичок отпустил его, и хулиган выбрался из зоны его досягаемости. {w}Он собрал друзкй и быстро ушёл."
        scene black with fade
        $renpy.pause(1)
        scene bg campus impound dusk with fade
        $renpy.pause(2.5)
        play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 1
        show akira wor at cc with dissolve
        $renpy.pause(1)
        show question:
            xoffset 720
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S8/Akira/2.ogg"
        am "Ты в порядке?"
    
        if (E1D3S5_AkiraNoticedMe == 1):
            "Я хорошенько взглянул на парня. Эти белые волосы выгляели действительно знакомыми…"
            show akira smi at cc with dissolve
            "Он улыбается, и осознание пораило меня, словно молния."
            pf "Ты же Акира!"
            show akira hap at cc
            voice "audio/voice/E1/D3/S8/Akira/3.ogg"
            am "Да, а ты новый переведённый ученик, верно?"
            "Я удивлённо моргнул."
            pf "О, ты слышал обо мне?"
            show akira thi at cc
            voice "audio/voice/E1/D3/S8/Akira/4.ogg"
            am "Отчасти. Я слышал о \"Американском GEAR\"."
            pf "Ааа…"
    
        else:
            pf "Ага, спасибо что помог мне."
            "Я заметил бирюзовые полосы на его форме. Полагаю, он тоже пилот."
            show akira hap at cc with dissolve
            voice "audio/voice/E1/D3/S8/Akira/5.ogg"
            am "Без проблем. Я знаю об этих парнях, и они никогда не делают ничего хорошего."
            show akira smi at cc
            voice "audio/voice/E1/D3/S8/Akira/5_01.ogg"
            am "Я Акира."
            pf "Я [pfirst]."
            show akira hap at cc
            voice "audio/voice/E1/D3/S8/Akira/6.ogg"
            am "Рад познакомиться. Я только хотел бы, чтобы это было при более счастливых обстоятельствах."
            pf "Хех, ага."
    
        show akira neu at cc
        pf "Надеюсь, я не звучу грубо, но что именно ты здесь делаешь?"
        "Он держит аналогичную моей квитанцию."
        show akira hap at cc with dissolve
        voice "audio/voice/E1/D3/S8/Akira/7.ogg"
        am "Забираю свой байк."
        show akira smi at cc
        pf "Ты нелегально припарковался, или что?"
        show akira hap at cc
        "Он засмеялся."
        voice "audio/voice/E1/D3/S8/Akira/8.ogg"
        am "Нет, у меня вообще-то есть парковочный пропуск."
        pf "Правда? Тогда что твой байк тут делает?"
        show akira thi at cc
        show drop:
            xoffset 720
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S8/Akira/9.ogg"
        am "Это довольно долгая история, но ты знаешь того грубого охранника? Он всегда был таким по отношению ко мне, ещё с моего первого года обучения. Я случайно припарковался в зарезервированном месте без пропуска… и это оказалось \"его\" местом."
        pf "О нет…"
        show akira smi at cc
        voice "audio/voice/E1/D3/S8/Akira/10.ogg"
        am "Да уж. Он так и не простил меня за это. Поэтому он очень часто утверждает, что в системе произошла путаница или что-то в этом роде, и мой мотоцикл оказался здесь." 
        pf "И ты позволил этому сойти с рук?"
        show akira hap at cc
        "Он снова засмеялся."
        voice "audio/voice/E1/D3/S8/Akira/11.ogg"
        am "Я уверен, что этот необычный сбой системы будет исследован в какой-то момент."
        show akira cur at cc
        voice "audio/voice/E1/D3/S8/Akira/12.ogg"
        am "В любом случае, ты в порядке?"
        pf "Да, я буду в порядке. А ты?"
        show akira smi at cc
        voice "audio/voice/E1/D3/S8/Akira/13.ogg"
        am "В порядке."
        voice "audio/voice/E1/D3/S8/Akira/14.ogg"
        am "Лучше возьму мотоцикл и отправлюсь домой."
        "Я кивнул и запрыгнул на свой байк."
        play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 3
        pf "Ещё раз спасибо за то, что вступился. Я твой должник."
        show akira mis at cc
        show note:
            xoffset 720
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S8/Akira/15.ogg"
        am "Не волнуйся. Я уверен, что ещё увижу тебя."
        pf "Ага, увидимся."
        hide akira with dissolve
        "Он помахал и вскоре исчез среди машин."
        play sound "audio/sfx/Vehicles/Bike Revving.ogg"
        stop music fadeout 3
        "Я завёл двигатель, чувствуя знакомый прилив адреналина и выехал с парковки."
        stop ambient fadeout 3
        play sound "audio/sfx/Vehicles/Bike driving off.ogg"
        $renpy.pause(1)
        scene black with fade
        $renpy.pause(2.5)
    
        jump E1D3S9
