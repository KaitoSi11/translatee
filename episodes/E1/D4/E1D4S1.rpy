label E1D4S1:
    
    
    $renpy.pause(2.5)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(2.5)
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    "Как обычно, я был разбужен рёвом своего будильника, но сегодня я не колеблясь встал с постели."
    ##NEW SOUND NEEDED##play sound "audio/sfx/Human/light_punch.ogg" fadeout 1
    scene bg homekaito myroom day with fade
    "У меня сегодня очень напряжённый день и я не могу позволить себе околачиваться."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    stop sound fadeout 3.0
    "Я оделся и спустился вниз. Проходя мимо комнаты Никки, я заметил, что её дверь открыта, а в комнате пусто.. {w}Должно быть, она на кухне."

    scene bg homekaito main day with fade
    
    "Дойдя до кухни, я обнаружил, что никого нет. {w}Дядя Кайто как всегда ушел прежде, чем я проснулся, но обычно Никки находилась дома."
    "Наверное что-то происходит в её школе сегодня и именно поэтому она ушла рано."
    
    "Я сварганил себе завтрак и проглотил его. {w}Затем я запрыгнул на свой байк и напраился в академию."
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(1)
    
    "Достигнув кампуса, я с лёгкостью дошёл до своего класса. {w}Эй! А я привык к этому месту."
    
    scene bg campus auditorium day with fade
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 1
    $renpy.pause(1)
    
    if (E1D2S2_talkwithyuunayes == 1):
        "Зайдя в класс, я заметил Юну, сидящую в передней части класса."
        "Стол рядом с ней был пуст, поэтому я подошёл к ней. Приблизившись, я заметил чью-то сумку на стуле."
        pf "Привет, хдесь не занято?"
        
        show yuuna smi at cc with dissolve
        
        if (E1D2S2_YuunaComesWithYouPass == 1): #She knows your schedule if you've gone this far with her
            "Она улыбнулась, когда заметив меня и убрала сумку."
            show yuuna hap at cc
            show note:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S1/Yuuna/1.ogg"
            ym "Нет, я придержала место для тебя."
        
        else:
            "Она улыбнулась качая головой и убрала сумку."
        
        show yuuna smi at cc
        "Я улыбнулся ей в ответ, пока садился."
        pf "Спасибо!"
        show yuuna smi b1 at cc with dissolve
        show regBlush:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S1/Yuuna/2.ogg"
        ym "Без проблем."
        pf "Что ты думаешь о нашем преподавателе?"
        show yuuna cur at cc with dissolve
        voice "audio/voice/E1/D4/S1/Yuuna/3.ogg"
        ym "Я слышала, что она очень хороша. Она строгая, но честная."
        pf "Звучит многообещающе."
        hide yuuna with dissolve
        "Прежде чем она успела ответить, профессор вошла в комнату и направилась прямо к доске."
    
    else:
        "К тому времени когда я пришёл в кабинет, я замечаю, что он в основном заполнен и все сиденья сзади заняты."
        "Я приметил пустое место рядом с окном в передней части класса."
        show yuuna neu at cc with dissolve
        "Когда я сел, девушка рядом со мной, с ярко-розовыми волосами, ненадолго заострила на мне внимание."
        hide yuuna with dissolve
        "Через несколько минут профессор вошла в комнату и направилась прямо к доске."
    
    show professorF extra at cc with dissolve
    stop music fadeout 3
    voice "audio/voice/E1/D4/S1/Professor/1.ogg"
    prof2f "Добро пожаловать в класс Истории 201. Сегодня мы будем освещать…"
    
    scene black with fade
    $renpy.pause(1)
    "Прошло не так много времени, а материал был не плох."
    $renpy.pause(2.5)
    scene bg campus auditorium day with fade
    
    $renpy.pause(1)
    
    show professorF extra at cc with dissolve
    
    voice "audio/voice/E1/D4/S1/Professor/2.ogg"
    prof2f "У нас осталось всего несколько минут до окончания занятий, ваше первое задание будет групповым проектом по тематическому исследованию на ваш выбор. Поскольку это первый день занятий, я буду назначать вам партнеров."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    "Она объединяла студентов, сидящих рядом друг с другом. {w}Наконец, она дошла и до меня."
    voice "audio/voice/E1/D4/S1/Professor/3.ogg"
    prof2f "Ты и ты отвечаете за работу вместе."
    hide professorF extra with dissolve
    show yuuna cur at cc with dissolve
    show exclamation:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    
    if (E1D2S2_talkwithyuunayes == 1):
        "Она указала на Юну и меня."
        show yuuna smi at cc with dissolve
        "Мы посмотрели друг на друга и усмехнулись. {w}Работа с ней обещает быть веселой."
    
    else:
        "Она указала на меня и розоволосую девушку рядом со мной."
        show yuuna smi at cc with dissolve
        "Мы посмотрели друг на друга, и она дружески улыбнулась. {w}Она казалась достаточно милой."
        
    show yuuna neu at cc
    voice "audio/voice/E1/D4/S1/Professor/4.ogg"
    prof2f "Ваш проект должен быть закончен к следующей неделе. Класс, вы свободны!"
    play sound "audio/sfx/Human/Class End.ogg" fadeout 1
    "Класс загудел и пришёл в движение. {w}Я повернулся к своей партнёрше."
    
    if (E1D2S2_talkwithyuunayes == 1):
        pf "Я с нетерпением жду совместной работы с тобой."
        show yuuna hap at cc with dissolve
        "Она засияла."
        voice "audio/voice/E1/D4/S1/Yuuna/4.ogg"
        ym "Я тоже. Как ты думаешь, какую нам выбрать тему?"
    
    else:
        pf "Привет, я [pfirst]."
        show yuuna smi at cc
        "Она тепло улыбнулась."
        voice "audio/voice/E1/D4/S1/Yuuna/5.ogg"
        ym "Я Юна. Рада познакомиться с тобой."
        show yuuna cur at cc
        "Ее глаза скользили по моим полосам на одежде."
        voice "audio/voice/E1/D4/S1/Yuuna/6.ogg"
        ym "Ты должно быть новенький."
        pf "Да, как ты узнала?"
        show yuuna smi at cc
        voice "audio/voice/E1/D4/S1/Yuuna/7.ogg"
        ym "Я, как правило, знаю большинство пилотов здесь."
        "Хоть ей и шла та форма что сейчас на ней, она лишена тех же полос что и у меня."
        pf "Ты не пилот, не так ли?"
        show yuuna hap at cc
        "Она слегка смеялась."
        voice "audio/voice/E1/D4/S1/Yuuna/8.ogg"
        ym "Нет, я просто работаю со многими из пилотов. Я студентка физиотерапии и здравоохранения пилотов."
        show yuuna smi at cc
        pf "That's a mouthful."
        show yuuna hap at cc
        "Она снова смеялась."
        voice "audio/voice/E1/D4/S1/Yuuna/9.ogg"
        ym "Да, ФиЗП для краткости."
        show yuuna smi at cc
        voice "audio/voice/E1/D4/S1/Yuuna/10.ogg"
        ym "Но вернёмся к делу, как ты думаешь, какую нам выбрать тему?"
        
    show yuuna neu at cc
    pf "Hm…"
    
    menu:
        "\"Пионеры-пилоты\".":
            $ E1D4S1_Pioneer = 1
            pf "Что, если мы сфокусируемся на пилотах, которые, в буквальном смысле, создали пилотирование таким, каким мы его видем сейчас?"
            "Минутку--она же не пилот..."
            pf "Конечно, если ты не хочешь выбирать эту тему, то нам не обязательно писать именно о них."
            show yuuna smi at cc
            voice "audio/voice/E1/D4/S1/Yuuna/11.ogg"
            ym "Я не против. В конце концов, то, что я изучаю, по-прежнему связано с пилотами. Это хорошая идея. Мы можем даже начать с ранних пилотов, которые помогли разработать первый военизированный GEAR."
            pf "Я думаю о том же."
    
        "Эволюция GEAR.":
            pf "Что, если мы сосредоточимся на GEAR'ах прошлых лет?"
            show yuuna smi at cc
            voice "audio/voice/E1/D4/S1/Yuuna/12.ogg"
            ym "Отличная идея! Мы можем начать с военных прототипов и постепенно показать, как одна и та же технология изменилась и превратилась в коммерческие и развлекательные механизмы, которые мы используем сегодня."
            pf "Звучит как план."
    
        "{color=#00ff00}{b}The psychology of Cenorobotics.{/b}{/color}" if (MCStory == 3):
            jump E1D4S1_MCStory1
    
        "Психология Cenorobotics." if (MCStory != 3):
            label E1D4S1_MCStory1:
            pf "Что, если мы сосредоточимся на психологическом воздействии развития и роста Cenorobotics как области?"
            show yuuna cur at cc with dissolve
            $renpy.pause(1)
            show yuuna hap at cc with dissolve
            "Ее лицо озарилось."
            show note:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S1/Yuuna/13.ogg"
            ym "Абсолютно! Это также может повлиять на социальное воздействие и на то, как общество адаптируется к росту в этой области, например, к разработке новых специальностей, таких как исследования в области здравоохранения пилотов."
            pf "Это должно быть по твоей части."
            show yuuna smi at cc
            voice "audio/voice/E1/D4/S1/Yuuna/14.ogg"
            ym "Что насчёт тебя? Тебя устраивает?"
            pf "Это звучит для меня интересно."
    
        "Не знаю. Для меня это одно и тоже.":
            #Yuuna doesn't like this answer much
            pf "Тема не имеет для меня значения. Всё будет хорошо."
            show yuuna ner at cc with dissolve
            voice "audio/voice/E1/D4/S1/Yuuna/15.ogg"
            ym "Ох."
            pf "Что насчёт тебя? Есть инетересующая тебя тема?"
            show yuuna thi at cc
            voice "audio/voice/E1/D4/S1/Yuuna/16.ogg"
            ym "Ну--"
            show dots:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            "Она остановилась, затем покачала головой."
            show yuuna neu at cc
            voice "audio/voice/E1/D4/S1/Yuuna/17.ogg"
            ym "Ничего. Нам не нужно решать прямо сейчас. Давай подумаем об этом и обсудим это позже."
            pf "Ты уверена? Похоже у тебя есть идея."
            show yuuna smi at cc
            voice "audio/voice/E1/D4/S1/Yuuna/18.ogg"
            ym "Вроде. Возможно, мы могли бы сосредоточиться на движении за повышение осведомлённости, чтобы сделать здоровье и безопасность пилота ключевой социальной проблемой, что также неизбежно высветит некоторые из общих опасностей и неправильного использования GEAR."
            "Я пожал плечами."
            pf "Звучит неплохо."
            
    stop ambient fadeout 3
    show yuuna hap at cc with dissolve
    "Юна улыбнулась."
    voice "audio/voice/E1/D4/S1/Yuuna/19.ogg"
    ym "Похоже, у нас есть тема."
    pf "Да, у меня хорошее чувство насчёт этого."
    show yuuna smi at cc
    voice "audio/voice/E1/D4/S1/Yuuna/20.ogg"
    ym "У меня тоже. У нас будет отличный проект."
    "К этому времени большая часть класса уже объединилась со своими партнёрами и покинула комнату. {w}Мы може должны идти. Возможно, там другой класс, которому нужна эта комната."
    
    if (E1D2S5_GotYuunasNumber == 1):
        pf "Круто, так что я, наверное, должен идти, но я уверен, что скоро увидимся."
        show yuuna hap at cc
        voice "audio/voice/E1/D4/S1/Yuuna/21.ogg"
        ym "Конечно, дай знать, когда сможешь работать над проектом."
        pf "Сделаю."
        show yuuna smi at cc
        "Она улыбнулась, пока мы оба собирали вещи."
    
    else:
        pf "В любом случае, мы должны идти."
        voice "audio/voice/E1/D4/S1/Yuuna/22.ogg"
        ym "Да, ты прав."
        "Я начал собирать вещи, когда Юна прервала меня."
        show yuuna cur with dissolve
        voice "audio/voice/E1/D4/S1/Yuuna/23.ogg"
        ym "Подожди, могу я узнать твой номер?"
    
        menu:
            "Девушка чтолько что спросила мой номер?":
                pf "Что?"
                show yuuna smi at cc
                voice "audio/voice/E1/D4/S1/Yuuna/24.ogg"
                ym "Хочешь обменяться номерами?"
                "Это реальность? Я скрытно ущипнул себя, стараясь не крикнуть от боли. {w}Определённо не сон."
                show yuuna sur b1 at cc with dissolve
                show shoBlush:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                "Юуна краснела под моим постоянным взглядом."
                voice "audio/voice/E1/D4/S1/Yuuna/25.ogg"
                ym "Д-Для проекта!"
                pf "А, точно, проект, над которым мы вместе работаем."
                show yuuna smi b1 at cc with dissolve
                voice "audio/voice/E1/D4/S1/Yuuna/26.ogg"
                ym "Да."
                "Я знал, что это слишком хорошо, чтобы быть правдой."
                pf "Конечно."
                show yuuna smi at cc with dissolve
                "Она улыбнулась."
    
            "*Ухмыльнуться*":
                "Ни одна леди не может устоять перед моим мужским очарованием! Я озарил её победной улыбкой."
                pf "Для тебя? Конечно."
                show yuuna cur b1 at cc with dissolve
                "Юна покраснела."
                voice "audio/voice/E1/D4/S1/Yuuna/27.ogg"
                ym "Просто так мы сможем работать над проектом."
                pf "Ммммм… над проектом."
                "Я подмигнул ей."
                pf "Я понял."
                show yuuna smi b1 at cc
                show regBlush:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                "Она моргнула и нерешительно улыбнулась."
    
            "Зачем ей знать?":
                pf "Что?"
                show yuuna smi at cc
                voice "audio/voice/E1/D4/S1/Yuuna/28.ogg"
                ym "Эм, хочешь обменяться номерами?"
                "Я нахмурился."
                pf "Зачем?"
                show yuuna cur b1 at cc with dissolve
                "Её щёки краснели."
                show shoBlush:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S1/Yuuna/25.ogg"
                ym "Для проекта!"
                pf "О… Конечно."
                show yuuna smi b1 at cc
                "Она улыбнулась."
    
            "Дать свой номер.":
                pf "867-5309."
                show yuuna ske at cc with dissolve
                "Юна моргала и морщила лоб."
                show question:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S1/Yuuna/30.ogg"
                ym "Хм, ты не пропустил некоторые цифры?"
                show yuuna thi at cc
                "Она странно посмотрела на меня."
                voice "audio/voice/E1/D4/S1/Yuuna/31.ogg"
                ym "Если ты не хочешь дать свой номер, я пойму."
                pf "Прости! Это был старый номер. Позволь дать тебе новый номер."
                show yuuna cur at cc
                voice "audio/voice/E1/D4/S1/Yuuna/32.ogg"
                ym "Да, ладно, конечно."
    
        show yuuna smi with dissolve
        "Мы быстро обменялись номерами и собрали вещи." 
    
    scene black with fade
    $renpy.pause(1)
    play sound "audio/sfx/Technology/Phone Vibration Once.ogg" fadein 1 fadeout 1
    $renpy.pause(1)
    
    "Когда мы вышли из класса мой телефон завибрировал. {w}Я глянул на неё, интересуясь, вдруг она уже прислала мне сообщение, но у неё в руках не было телефона."
    "Когда я вытащил телефон, то увидел сообщение от Сё."
    "{i}Большие новости, братишка! Мы находимся на первом этапе квалификационных матчей. Команда встречается в ангаре.{/i}"
    
    if (E1D2S11_JoinedTheTeam == 1):
        "Первая официальная встреча команты должна быть интересной. {w}Хотя я чувствую пару трепетаний в животе, я был более взволнован, чем нервничал увидеть всех."
    
    elif (E1D2S3_MetKaoriWasRudeNoHelmet == 1):
        "Мой живот скручивался в тугой узел. Интересно, как Каори отреагирует, когда увидит меня. {w}Надеюсь, Сё знает, что делает..."
        
    elif (E1D2S11_JoinedTheTeam == 0) and (E1S2D10_AskedOtherTeams == 1):
        "Интересно, как там другие. {w}Полагаю, что скоро встречу всех."
        
    play ambient "audio/ambience/Campus.ogg" fadein 1
    scene bg campus building day with fade
    
    "Ка только мы вышли на улицу, Юна повернулась ко мне."
    
    show yuuna smi at cc with dissolve
    voice "audio/voice/E1/D4/S1/Yuuna/33.ogg"
    ym "У тебя есть ещё занятия сегодня?"
    pf "Нет, но я иду в ангар. Нужно встретиться с командой перед квалификацией."
    "Она кивнула."
    show yuuna hap at cc
    voice "audio/voice/E1/D4/S1/Yuuna/34.ogg"
    ym "Удачи!"
    pf "Спасибо!"
    hide yuuna with dissolve
    "Мы помахали друг другу и разошлись."
    
    stop music fadeout 3.0
    scene black with fade
    $renpy.pause(2.5)   
    
    jump E1D4S2
