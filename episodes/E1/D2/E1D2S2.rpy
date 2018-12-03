label E1D2S2:
    
    play ambient "audio/ambience/Bus Stop.ogg" fadein 1
    scene bg isokaze neighborhood day with fade
    
    "Cars whip by когда я приближался к автобусной остановке. {w}Там было несколько человек, ожидавших автобус. Я убрал руки в карманы и присллонился к навесу на остановке в ожидании."
    
    play sound "audio/sfx/Vehicles/Bus Door Open.ogg"
    "Резкий визг тормозов сообщил о прибытии автобуса. Несколько человек вышли из автобуса, и я искал в сумке свою ID карту."
    scene bg travel bus day with fade
    play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
    "Я вошёл в автобус и прислонил ID карту к сканнеру. На нём появился подтверждающий сигнал."
    play sound "audio/sfx/Vehicles/Bus Door Open.ogg"
    "Не дожидаясь, когда я найду свободное место, автобус тронулся, и моё тело чуть не обняло пол. Было не так много свободных мест, поэтому я неуверенно поплёлся в конец автобуса."
    stop ambient fadeout 5
    play ambient "audio/ambience/Bus.ogg" fadein 1
    "Оглядываясь, я заметил, что большинство пассажиров носило форму академии ACE. Это утешает, я полагаю."
    "Здесь свободное место рядом с девушкой примерно моего возраста."

    $ persistent.gpix[61][0] = 1
    $ persistent.gpix[62][0] = 1
    $ persistent.gpix[63][0] = 1
    scene cg yuuna bus meeting1 with dissolve:
        xzoom .5
        yzoom .5
    "Она пристально смотрела в окно и её осанка была неудобно прямой."
    "На её форме не было тиановой маркировки. {w}Полагаю, она не пилот."
    
    "Она была очень милой, так что мне было интересно, почему рядом с ней было свободное место. {w}Может, она не так дружелюбна?"
    
    menu:
        "Ладно, я попробую. было бы неплохо знать хоть одного человека из Академии.":
            $ E1D2S2_talkwithyuunayes = 1
    
        "Лучше найду другое место.":
            $ E1D2S2_talkwithyuunayes = 0
        
    if (E1D2S2_talkwithyuunayes == 1):
    
        "Я неизящно сел рядом с ней."
        "Мы сидели в тишине, пока я собирал мужество, чтобы поговорить с ней. В конце концов, она неудобно повернулась под моим взглядом, и я прочистил горло."
    
        pf "Хм, ты тоже едешь в Академию?"
        play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 1
        "Я мысленно вдарил себя за бывор такого тупого вопроса. Очевидно же, что едет в Академию. Я же сразу это заметил. К моему удивлению, она тепло улыбнулась."
        scene cg yuuna bus meeting3 with dissolve:
            xzoom .5
            yzoom .5
        voice "audio/voice/E1/D2/S2/Yuuna/1.ogg"
        ym "Да."
    
        "Она указала на мою форму."
        scene cg yuuna bus meeting2 with dissolve:
            xzoom .5
            yzoom .5
        voice "audio/voice/E1/D2/S2/Yuuna/2.ogg"
        ym "Ты в программе пилотов? Я слышала, что там большая конкуренция и туда сложно попасть."
    
        menu: 
            "Да.":
                pf "Да."
                voice "audio/voice/E1/D2/S2/Yuuna/3.ogg"
                ym "… Да, ты в программе пилотов? Иди да, в эту программу сложно попасть?"
                pf "Хм… Да."
                voice "audio/voice/E1/D2/S2/Yuuna/4.ogg"
                ym "О… эм, хорошо."
                scene cg yuuna bus meeting1 with dissolve:
                    xzoom .5
                    yzoom .5
                "Она вежливо ждала, что я скажу больше. Но я этого не сделал, и она снова повернулась к окну. {w}Время от времени я ловил её взгляд на мне."
    
            "Не, это было легко!":
                "Я пренебрежительно махнул рукой."
                pf "Я без проблем попал туда."
                scene cg yuuna bus meeting3 with dissolve:
                    xzoom .5
                    yzoom .5
                voice "audio/voice/E1/D2/S2/Yuuna/5.ogg"
                ym "Ох, понятно."
                "Её улыбка казалась натянутой."
    
            "Просто нужно усердно трудиться.":
                pf "Я думаю, любой сможет поступить, пока пытается."
                scene cg yuuna bus meeting3 with dissolve:
                    xzoom .5
                    yzoom .5
                "Она вежливо улыбнулась мне."
    
        pf "Точно, я не услышал, в какой ты программе. Или как тебя зовут, раз уж на то пошло. Меня зовут [pfull]."
        scene cg yuuna bus meeting3 with dissolve:
            xzoom .5
            yzoom .5
        voice "audio/voice/E1/D2/S2/Yuuna/6.ogg"
        ym "Я Юна, Юна Мисаки. я изучаю ЗПФТ."
        pf "\"PHPT\"?"
        voice "audio/voice/E1/D2/S2/Yuuna/7.ogg"
        ym "Здоровье пилотов и физиотерапия."
        stop music fadeout 3
        stop ambient fadeout 5
        "Прежде чем я успел спросить что-то ещё, автобус остановился."
    
        play sound "audio/sfx/Vehicles/Bus Chime.ogg"
        $renpy.pause(1)
        voice "audio/voice/E1/D2/S2/Bus Announcer/1.ogg"
        "Диктор автобуса" "Академия ACE."
        
        scene black with fade
        scene white with fade
        play sound "audio/sfx/Vehicles/Bus Door Open.ogg"
        play ambient "audio/ambience/Campus.ogg" fadein 3
        scene bg campus main day with Dissolve(2)
    
        "Я выпрыгнул из автобуса и Юна сделала то же самое. Шум уезжающего автобуса не заглушал болтовню студентов. Юна вытащила телефон и проверила расписание."
        
        play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
        show yuuna neu at cc with dissolve
        
        label E1D2S2_yuunaloop:
            menu:
                "Спросить где у неё урок.":
                    pf "Так, какой твой первый урок?"
                    show yuuna smi at cc with dissolve
                    voice "audio/voice/E1/D2/S2/Yuuna/8.ogg"
                    ym "Введение в психологию."
                    pf "Психологию?"
                    
                    voice "audio/voice/E1/D2/S2/Yuuna/9.ogg"
                    ym "Психическое здоровье столь же важно, как и физическое. Урок проходит--"
                    "Она указала через плечо на возвышающееся здание вдалеке."
                    voice "audio/voice/E1/D2/S2/Yuuna/10.ogg"
                    ym "--там. Какой у тебя урок?"
                    "Я проверил телефон."
                    pf "101 пилотный."
                    show yuuna sur at cc
                    show question:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D2/S2/Yuuna/11.ogg"
                    ym "Ох, так ты на первом году обучения?"
                    pf "Нет, на втором. Однако меня не приняли на второй год, когда я перевёлся."
                    show yuuna smi at cc
                    voice "audio/voice/E1/D2/S2/Yuuna/12.ogg"
                    ym "Ох, понятно. Ну, добро пожаловать в Академию!"
                    
                    pf "Хех, спасибо!"
                    show yuuna hap at cc
                    voice "audio/voice/E1/D2/S2/Yuuna/13.ogg"
                    ym "Ну, если тебе нужна помощь, или есть вопросы - обращайся. Я довольно хорошо знаю кампус."
    
                    menu:
                        "Посмотрим, знает ли она как получить разрешение на парковку.":
                            $ E1D2S2_YuunaComesWithYouPass = 1
                            "Меня посетила мысль."
                            pf "Вообще-то, ты знаешь как получить разрешение на парковку?"
                            show yuuna smi at cc
                            voice "audio/voice/E1/D2/S2/Yuuna/14.ogg"
                            ym "Да, знаю. Я могу отвести тебя туда, так как у меня еще есть время до урока."
    
                            pf "Отлично, это мне очень поможет! Спасибо."
                            show yuuna hap at cc
                            voice "audio/voice/E1/D2/S2/Yuuna/15.ogg"
                            ym "Конечно! Следуй за мной."
                            hide yuuna with dissolve
    
                            "Юна вливается в толпу студентов, и большая чать сил уходит на то, чтобы не потерять её."
                            "Я заметил студентов, бездельничающих у передней лужайки. Полагаю, они старшекурсники--уже привыкшие к учебным будням. Студенты с взволнованными глазами, с походкой где-то между ходьбой и бегом, должно быть первокурсники."
                            scene bg campus building day with fade
                            "В итоге, мы остановились перед огромным зданием… {w}который выглядит так же, как и остальные. Я пристально смотрел на него, пытаясь найти способ отличить его от других."
                            show yuuna neu at cc with dissolve
                            "Юна смотрела на меня."
    
                            voice "audio/voice/E1/D2/S2/Yuuna/16.ogg"
                            ym "Всё в порядке?"
    
                            pf "Что? А, да."
                            show yuuna smi at cc
                            voice "audio/voice/E1/D2/S2/Yuuna/17.ogg"
                            ym "Тогда пойдём внутрь."
    
                            pf "Конечно."
                            hide yuuna with dissolve
                            "Я ещё раз посмотрел на здание, а потом зашёл внуть вслед за Юной."
                            stop ambient fadeout 3
                            scene black with fade
                            "Она провела меня через ряд коридоров, и остановилась перед дверью с табличной \"Администрация кампуса\"."
                            "Мы одновременно дошли до двери, но я был быстрее."
                            "Она улыбнулась, когда я держал для неё дверь."
                            voice "audio/voice/E1/D2/S2/Yuuna/18.ogg"
                            ym "Ох! Спасибо."
                            stop music fadeout 3
                            scene bg campus office day with fade
                            play ambient "audio/ambience/Campus Office.ogg" fadein 1
                            "То, что должно быть просторным офисом в итоге заполнено раздражёнными учениками. Только один человек стоял за стойкой, и он не выглядел сговорчивым."
                            show yuuna smi at cc
                            "Юуна указала на ряд стульев у дальней стены."
                            voice "audio/voice/E1/D2/S2/Yuuna/19.ogg"
                            ym "Я подожду тебя там."
                            pf "Спасибо, надеюсь, это не займет слишком много времени. Если займёт, то можешь уйти. Я не хочу, чтобы ты опоздала."
                            voice "audio/voice/E1/D2/S2/Yuuna/20.ogg"
                            ym "Не волнуйся, у меня есть немного времени."
                            show yuuna hap at cc
                            "Она обнадёживающе улыбнулась, прежде чем отправиться к стульям."
                            hide yuuna with dissolve
                            "Я встал в очередь. {w}Когда я поднял шею, чтобы увидеть, что впереди, то заметил хмурый взгляд на лице администратора. Он качал головой, но студент продолжал спорить с ним."
                            "Это займёт время…"
                            jump E1D2S5
    
                        "Самому изучить место.":
                            pf "Спасибо, буду знать. Я, думаю, будет лучше, если я сам погуляю и узнаю места."
                            show yuuna smi at cc
                            "Она понимающе кивнула."
                            voice "audio/voice/E1/D2/S2/Yuuna/21.ogg"
                            ym "Конечно. Тогда, полагаю, ещё увидимся?"
                            pf "Надеюсь."
                            hide yuuna with dissolve
                            "Она помахала на прощанье, и я потерял её в толпе студентов."
                            "Я проверил телефон и заметил, что у меня ещё есть око часа до начала занятий. {w}Пойти в класс пораньше, или погулять?"
                            jump E1D2S4
    
                "Мне надо поторопиться.":
                    
                    pf "Я должен идти в класс. Не хочу потеряться в первый день." 
                    show yuuna smi at cc
                    "Она понимающе кивнула."
                    voice "audio/voice/E1/D2/S2/Yuuna/21.ogg"
                    ym "Конечно. Тогда, полагаю, ещё увидимся?"
                    pf "Надеюсь."
                    hide yuuna with dissolve
                    "Она помахала на прощанье, и я потерял её в толпе студентов."
                    "Я проверил телефон и заметил, что у меня ещё есть око часа до начала занятий. {w}Пойти в класс пораньше, или погулять?"
                    jump E1D2S4
    
                "Таааак…" if (E1D2S2_yuunaloopback == 0):
                    $ E1D2S2_yuunaloopback = 1
                    pf "Таааак…"
                    show dots:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    show yuuna thi at cc with dissolve
                    "Я смотрел куда угодно, но не на Юну. {w}Она неловко переминалась на месте, возившись с ниткой на рукаве. {w}Секунды шли, молчание становилось все более и более тяжёлым."
                    jump E1D2S2_yuunaloop
                    
    elif (E1D2S2_talkwithyuunayes == 0):
    
        "Не похоже, что она хочет, чтобы ее беспокоили."
        scene bg travel bus day with fade
        "Я пробшёл в конец автобуса, и нашёл место у окна. Я сел, и смотрел как мимо проносились деревья."
    
        $renpy.pause(3)
        play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
    
        "Мой карман завибрировал."
        "Это напоминание, чтобы проверить почту, отправленную самому себе вчера вечером. {w}Я собрал всю необходимую мне информацию, которая мне пригодится в первый день и сжал её в одно письмо для быстрого доступа."
        "Я листал и напоминал себе информацию и расписание. {w}Когда я нажал на кнопку локации, он открыл мне подробную карту кампуса. Это пригодится."
        "Следующие несколько минут я изучал разные места кампуса. {w}Красный пульсирующий свет указывает на самые большие здания, в то время как более мелкие вспыхивают желтыми. {w}Мои классы, кажется, не слишком далеки друг от друга, что очень удобно. Теперь я ни за что не потеряюсьь."
    
        "..."
    
        "Лавка хот-догов? {w}Клянусь, они есть в каждом кампусе. Однако, удивительно найти его в японской школе… и он отмечен на карте."
    
        play sound "audio/sfx/Vehicles/Bus Chime.ogg"
        $renpy.pause(1)
        voice "audio/voice/E1/D2/S2/Bus Announcer/1.ogg"
        "диктор автобуса" "Академия ACE."

        "Я юыстро собрал вези и вышел из автобуса с остальными студентами."
        
        scene black with fade
        play sound "audio/sfx/Vehicles/Bus Door Open.ogg"
        scene white with fade
        play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
        play ambient "audio/ambience/Campus.ogg" fadein 3
        scene bg campus main day with Dissolve(2)
    
        "Первое, что я заметил - это то, насколько чист и ухожен кампус. {w}Как в брошюре. Деревья и изгороди аккуратно отделаны; нет ни лишнего листочка. Трава скошена. Даже архитектура демонстрирует прямые линии и дизайн. {w}Я любил CINY, но он мог бы использовать несколько советов по поддержке чистоты."
        "Я проверил время. {w}У меня был где-то час до занятий. {w}Пойти в класс пораньше? Последнее, что я хочу, это опаздывать на первый урок. {w}С другой стороны, сидеть в пустом классе в течение часа кажется контрпродуктивным. Я мог бы провести время, проверяя разные места кампуса."
    
        jump E1D2S4
