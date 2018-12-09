label E1D3S4:
    
    "Я открыл на телефоне расписание и проверил первый урок: Арсенал GEAR 201. {w}Здание тоже не слишком далеко."
    scene bg campus building day with fade
    stop ambient fadeout 3
    "Вскоре я достиг здания."
    scene bg campus auditorium day with fade
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 1
    "Класс был в два раза меньше, чем класс Пилотирования 101. {w}По какой-то причине, это утешало меня, возможно, потому что они напоминали классы в CINY."
    play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 1
    "Я сел в конце класса как только зашёл профессор."
    show professorM2 extra at cc with dissolve
    voice "audio/voice/E1/D3/S4/Prof/1.ogg"
    prof1m "Доброе утро, класс. Добро пожаловать на Арсенал GEAR 201. Я уверен, что вы все устали слышать один и те же приветственные речи, так что не буду докучать этим. Вместо этого мы погрузимся сразу в материал."
    voice "audio/voice/E1/D3/S4/Prof/2.ogg"
    prof1m "Вопрос: Кто может назвать одну из ведущих компаний по производству оружия GEAR??"
    
    menu:
        "Potato Shooter Incorporated.":
            pf "Potato Shooter Incorporated!"
            "Класс залился смехом."
            show drop:
                xoffset 675
                yoffset 50
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Prof/3.ogg"
            prof1m "Очень смешно. Настоящей компанией будет Paragon Weaponry."
    
        "{color=#00ff00}{b}Paragon Weaponry.{/b}{/color}" if (MCStory == 2):
            jump E1D3S4_MCStory1
        
        "Paragon Weaponry." if (MCStory != 2):
            label E1D3S4_MCStory1:
            "Прежде чем я успел ответить, другой студент поднял руку."
            voice "audio/voice/E1/D3/S4/stu8m/2.ogg"
            stu8m "Vector Industries!"
            voice "audio/voice/E1/D3/S4/Prof/4.ogg"
            prof1m "Прости, неправильно."
            pf "Paragon Weaponry."
            show note:
                xoffset 675
                yoffset 50
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Prof/5.ogg"
            prof1m "Очень хорошо!"
            voice "audio/voice/E1/D3/S4/stu8m/3.ogg"
            stu8m "Почему не Vector?"
            voice "audio/voice/E1/D3/S4/Prof/6.ogg"
            prof1m "Vector работает с двигателями и устройствами маневрирования, а Paragon - с оружием… Отсюда и название \"Paragon Weaponry\"."
    
        "Dasshu.":
            pf "Dasshu."
            voice "audio/voice/E1/D3/S4/Prof/7.ogg"
            prof1m "Это неправильно. Dasshu только недавно начали инвестировать в сферу Cenorobotics. Однако, их основной бизнес по-прежнему энергетические напитки. Правильным ответом будет Paragon Weaponry."
    
        "Aludian Enterprises.":
            pf "Aludian Enterprises."
            voice "audio/voice/E1/D3/S4/Prof/8.ogg"
            prof1m "Не совсем. Хотя Aludian Enterprises, безусловно, создает шум в СМИ, они ни в коем случае не являются лидирующей компанией. Примером ветерана индустрии может быть Paragon Weaponry."
    voice "audio/voice/E1/D3/S4/Prof/9.ogg"
    prof1m "Их недавняя область исследования показала, что..."
    
    "Он углубился в детали исследований и разработок Paragon Weaponry и будущее лучевого оружия на оставшееся время урока."
    stop music fadeout 3
    $renpy.pause(1)
    scene black with fade
    #time passes, class ends
    $renpy.pause(1)
    scene bg campus auditorium day with fade
    $renpy.pause(1)
    show professorM2 extra at cc with dissolve
    voice "audio/voice/E1/D3/S4/Prof/10.ogg"
    prof1m "Вот и всё на сегодня. Чтения и задания этой недели вы найдете на своей веб-ссылке. Хорошего дня!"
    hide professorM2 extra with dissolve
    play sound "audio/sfx/Human/Class End.ogg"
    "Студенты поспешили собрать свои вещи, прежде чем уйти из класса. {w}Думаю, вернусь в ангар. Этот урок вдохновил меня пойти и хорогенько осмотреть свой GEAR."
    stop ambient fadeout 3
    scene black with fade
    play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
    $renpy.pause(2.5)
    play ambient "audio/ambience/Hangar.ogg" fadein 1 fadeout 1
    #scene bg campus hangar day with dissolve
    "Я прошёл через зал пилотов и последовал по туннелям, пока не дошёл до GEAR."
    scene cg GEAR hangar first with fade
    play sound "audio/sfx/GEAR/GEAR Elevator.ogg"
    $renpy.pause(2.5)
    "Опустив лестницу рядом с док-станцией, я поднялся наверх, примерно на уровень груди робота."
    scene black with fade
    play sound [ "audio/sfx/GEAR/GEAR Cockpit Open.ogg"]
    "Я открыл грудную клетку. С механическим рёвом, он открыл разделительные панели, показывая опускающееся сидение. {w}Я легко запрыгнул на него и вдохнул успокаивающий запах металла и пластика. Это слабо напоминало мне о запахе новой машины."
    $renpy.pause(1)

    $ persistent.gpix[4][0] = 1
    $ persistent.gpix[5][0] = 1
    $ persistent.gpix[6][0] = 1
    scene cg GEAR cockpit first1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with Dissolve(2.5)
    $renpy.pause(1)
    play sound "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
    stop ambient fadeout 3
    "Как только я уселся, то запустил механизм закрытия. Когда грудные панели вернулись на место, сидение углубилось в GEAR пока я не приютился в темноте кабины."
    $renpy.pause(1)
    play sound "audio/sfx/GEAR/GEAR Boot Up 1.ogg"
    $renpy.pause(1.5)
    scene cg GEAR cockpit first2 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with Dissolve(1.5)
    $renpy.pause(1.5)
    "Я инициировал запуск. Кабина загорелась красным, затем замерцала, и я не мог сдержать улыбку от знакомых ощущений. {w}Яркое свечение панелей освещала интерьер до тех пор, пока не осталось ни следа тени. Статистика мерцала вокруг меня в виде серии быстрых чисел и диаграмм."
    $renpy.pause(1.5)
    play sound "audio/sfx/GEAR/GEAR Boot Up 2.ogg"
    $renpy.pause(1.5)
    scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with Dissolve(2.5)
    play ambient "audio/ambience/GEAR Cockpit.ogg" fadein 1 fadeout 1
    $renpy.pause(1)
    voice "audio/voice/E1/D3/S4/EagleAI/1.ogg"
    GEARpf "Последовательность инициализации Gear завершена."
    
    "Знакомый голос GEAR чувствовался как приветствие старого друга."
    
    pf "Орел, пожалуйста, запусти комплексную проверку."
    
    voice "audio/voice/E1/D3/S4/EagleAI/2.ogg"
    GEARpf "Проверка запущена..."
    
    "Сейчас нечего делать, кроме как ждать. {w}Индикаторы вдоль дисплея пульсировали, меняя цвета по мере прохождения проверки. Оа протекала разными теплыми цветами: красным, оранжевым, желтым, прежде чем осветил кабину ярко-зеленым."
    $renpy.pause(1)
    voice "audio/voice/E1/D3/S4/EagleAI/3.ogg"
    GEARpf "Все системные функции: В норме."
    
    voice "audio/voice/E1/D3/S4/EagleAI/4.ogg"
    GEARpf "Обнаружена неизвестная док-станция."
    
    pf "Зарегистрировать текущий док в качестве домашней станции."
    $renpy.pause(1)
    voice "audio/voice/E1/D3/S4/EagleAI/5.ogg"
    GEARpf "Завершено."
    
    voice "audio/voice/E1/D3/S4/EagleAI/6.ogg"
    GEARpf "Рекомендация: обновите конфигурацию системы калибровки."
    
    "Это рекомендовалось всё время. Всякий раз, когда мы меняли местоположение, Орёл запрашивал повторную калибровку системы. Даже малейшая разница в давлении воздуха могла вызвать неточность."
    
    "По крайней мере, процесс был прост. Все, что мне нужно было сделать, это убедиться, что я правильно следовал порядку последовательных номеров, чтобы Орёл мог выполнить необходимые внутренние вычисления." 
    
    pf "Хорошо, начинай процесс."
    voice "audio/voice/E1/D3/S4/EagleAI/7.ogg"
    GEARpf "Инициирую последовательность калибровки..."
    play sound "audio/sfx/GEAR/GEAR Virtual Training Simulator.ogg"
    # Let's set our variables so the game knows where we are at
    #$ firstCalibration = 0
    #$ context = "E1D3S4_SystemCalibrationLoopback"
    # 6 and 6
    #$ numBase = 6
    #$ numLimit = 6
    # We will now display the numbers minigame. Hopefully, the if statements for the variables will take us back to where we need to be.
    #jump numbers_game
    # If all goes well, it should jump back here vvv
    #label E1D3S4_SystemCalibrationLoopback:
        
    #    if firstCalibration == 0:
    #        voice "audio/voice/E1/D3/S4/EagleAI/8.ogg"
    #        GEARpf "Calibration sequence failed. Please try again."
    #        jump numbers_game
            
    #    else:
    #        voice "audio/voice/E1/D3/S4/EagleAI/9.ogg"
    #        GEARpf "Calibration successful."
    #        pf "Perfect."
  
    "Я дал ему несколько минут, так как Eagle автоматически настраивался."
    "..."
    "....."
    voice "audio/voice/E1/D3/S4/EagleAI/9.ogg"
    GEARpf "Калибровка успешно завершена."
    pf "Идеально."  
    
    "Вроде всё в порядке."
    $renpy.pause(1)
    stop ambient fadeout 3
    scene cg GEAR cockpit first1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    $renpy.pause(1)
    play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
    $renpy.pause(1)
    "Взглянув напоследок, я выключил GEAR и открыл грудную клетку."
    scene black with fade
    play ambient "audio/ambience/Hangar.ogg" fadein 1
    play sound "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
    "Как только я выпрыгнул, панели начали закрываться пока я не услышал слабый щелчок."
    scene cg GEAR hangar first with fade
    if (E1D2S11_JoinedTheTeam == 0):
        play sound "audio/sfx/GEAR/GEAR Elevator.ogg"
        "Я использлвал лифт и добрался до земли. {w}Когда я стоял один в тишине пустого ангара, то почувствовал приступ тоски по дому."
        play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 1
        "Я ожидал, что ACE будет отличаться от CINY, но я был не совсем готов к реакции на мой GEAR. {w}Неудивительно, что достижения Японии в области Cenorobotics перевешивали достижения США, но наша техника создавалась для долгосрочной работы."
    
        "Мой GEAR возможно, не самая новой модели, или не оснащён новейшим оружием или аксессуарами, но я уверен в его способности сражаться."
    
        "Сомнение закралось в ход мыслей. {w}Может быть, приехать сюда было ошибкой. Я мог бы остаться в CINY. У меня были высокие оценки, и группа друзей, на которых я мог положиться. Я проводил бы дни, практикуясь вместо того, чтобы сидеть в ангаре... {w}just me and that weirdo from yesterday--"
        stop music fadeout 3
        "Я обернулся, пока Сё шёл ко мне."
    
    if (E1D2S11_JoinedTheTeam == 1):
        play sound "audio/sfx/GEAR/GEAR Elevator.ogg"
        "Когда я повернулся к лифту, то увидел, как Сё махал мне рукой. Я проворно спустился вниз и встал рядом с ним."
        $renpy.pause(2.5)
        
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
    scene bg campus hangar day with fade
    show shou smi at cc with dissolve
    voice "audio/voice/E1/D3/S4/Shou/1.ogg"
    ss "Мистер братишка."
    pf "Эй, как дела?"
    show shou hap at cc
    voice "audio/voice/E1/D3/S4/Shou/2.ogg"
    ss "Хорошо. Это твоё место \"отдыха\"? Второй раз наталкиваюсь на тебя здесь."
    pf "Хех, я думаю, это начинает им быть. Что ты здесь делаешь?"
    stop music fadeout 3
    show shou mis at cc
    voice "audio/voice/E1/D3/S4/Shou/3.ogg"
    ss "Я думал нанести визит своей GEAR. Это помогает, когда я немного поддерживаю ей компанию. Поднимает ей настроение."
    
    menu:
        "Вот почему я предпочитаю мужские GEAR.":
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 1
            pf "Это еще одно доказательство того, что девушки всех типов требуют повышенного ухода."
            show shou cur at cc
            "Сё поморгал, затем рассмеялся."
            show shou hap at cc with dissolve
            voice "audio/voice/E1/D3/S4/Shou/4.ogg"
            ss "Расскажи-ка мне. Тогда, я так понимаю, твой GEAR \"он\"?"
            pf "Я никогда не считал его \"им\" или \"ею\"."
            show shou mis at cc
            show bulb:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Shou/5.ogg"
            ss "Ааа, так значит \"Зе\"!"
            pf "Что?"
            show shou smi at cc
            voice "audio/voice/E1/D3/S4/Shou/6.ogg"
            ss "Ты знаешь, нейтральный пол."
            pf "Ну, вроде. Я просто называю \"оно\"."
            stop music fadeout 3
            show shou cur at cc
            voice "audio/voice/E1/D3/S4/Shou/7.ogg"
            ss "А, ну так тоже."
    
        "Ей? Ты имеешь в виду девушку?":
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 1
            pf "Есть девушка, которую ты держишь в плену в своём GEAR?"
            show shou hap at cc with dissolve
            "Сё засмеялся."
            voice "audio/voice/E1/D3/S4/Shou/8.ogg"
            ss "Если бы… К сожалению, ни одна девушка не подходит к моему GEAR."
            show shou smi at cc
            "Он мечтательно вздохнул, а я изо всех сил старался сохранять невозмутимый вид."
            pf "Мне жаль."
            stop music fadeout 3
            show shou sad at cc with dissolve
            show crying:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Shou/9.ogg"
            ss "Мне тоже."
    
        "Неодушевлённые объекты не имеют пола.":
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 1
            pf "Ей?"
            show shou smi at cc
            voice "audio/voice/E1/D3/S4/Shou/10.ogg"
            ss "Да."
            pf "... Твоей девушке?"
            show shou hap at cc with dissolve
            "Сё засмеялся."
            voice "audio/voice/E1/D3/S4/Shou/11.ogg"
            ss "Нет, моему GEAR."
            pf "Твой GEAR \"она\"?"
            show shou mis at cc
            voice "audio/voice/E1/D3/S4/Shou/12.ogg"
            ss "Да! А твой?"
            pf "Мой GEAR."
            show shou smi at cc
            voice "audio/voice/E1/D3/S4/Shou/13.ogg"
            ss "Да, \"она\" \"он\"?"
            pf "\"Оно\"."
            show shou cur at cc
            voice "audio/voice/E1/D3/S4/Shou/14.ogg"
            ss "Оууу."
            show dots:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            "Он задумался."
            show shou smi at cc
            voice "audio/voice/E1/D3/S4/Shou/15.ogg"
            ss "Ну, в любом случае, спасибо."
            pf "За что?"
            show shou mis at cc
            voice "audio/voice/E1/D3/S4/Shou/16.ogg"
            ss "За мысль, что для меня возможно найти девушку."
            stop music fadeout 3
            pf "Хорошо, тогда."
            
    show shou smi at cc with dissolve
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
    voice "audio/voice/E1/D3/S4/Shou/17.ogg"
    ss "Так что ты тут делал?"
    pf "Просто проверял, что все работает нормально."
    show shou hap at cc
    voice "audio/voice/E1/D3/S4/Shou/18.ogg"
    ss "И как, нормально?"
    pf "Да."
    show shou cur at cc with dissolve
    "Он заинтересованно посмотрел на мой GEAR."
    show shou mis at cc
    voice "audio/voice/E1/D3/S4/Shou/19.ogg"
    ss "Как насчёт симуляци боя?"
    "Я пожал плечами. Было бы неплохо почувствовать, как обстоят дела в ACE."
    pf "Конечно."
    show shou smi at cc
    voice "audio/voice/E1/D3/S4/Shou/20.ogg"
    ss "Мы оба можем использовать базовую программу роботов. Таким образом, все аксессуары и оружие будут одинаковыми и оно будет основываться только на навыках.."
    pf "Пусть победит сильнейший."
    #show shou hap at cc with dissolve
    #hide shou with dissolve
    scene black with fade
    play sound "audio/sfx/GEAR/GEAR Elevator.ogg"
    $renpy.pause(2.5)
    #scene cg GEAR hangar first at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    #$renpy.pause(2.5)
    "Он узмыльнулся и побежал в обратную сторону. Я видел, как он остановился у зелёного GEAR прежде чем я залез в свой."
    play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
    $renpy.pause(1.5)
    scene cg GEAR cockpit first1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    #play sound "audio/sfx/Impacts/Luggage Drop.ogg"
    $renpy.pause(1.5)
    stop ambient fadeout 3
    play sound "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
    $renpy.pause(1.5)
    play sound "audio/sfx/GEAR/GEAR Boot Up 1.ogg"
    $renpy.pause(1.5)
    scene cg GEAR cockpit first2 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    play ambient "audio/ambience/GEAR Cockpit.ogg" fadein 1
    $renpy.pause(1.5)
    play sound "audio/sfx/GEAR/GEAR Boot Up 2.ogg"
    #$renpy.pause(2.5)
    scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    "Как только я сел в кабину, то включил конфигурацию открытой сети."
    stop music fadeout 3
    play sound "audio/sfx/GEAR/GEAR Virtual Training Simulator.ogg"
    "Сразу же пришёл запрос от Сё, и я принял его. После подключения, мы загрузили программу виртуальной тренировки."
    stop ambient fadeout 3
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 1
    #Open up rapid mini-game part so the mechs and such appear but no QTE yet
    
    
   
    
    scene bg battleground day with Dissolve(2.5)
    show mc mech at bl with dissolve:
        xzoom -1
    show shou mech at br with dissolve
    show shiny:
        xoffset 1200
        yoffset 50
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S4/Shou/30.ogg"
    ss "Ох! очень забавно(модно). Я раньше не видел так близко американский GEAR."
    
    pf "Ага."
    
    "Я экспериментировал со своими элементами управления GEAR и наблюдал за тем, как он делал те же движения в симуляторе."
    "Симуляторы необычайно точны в подражании реальным действиям, но они все еще не могли полностью воспроизвести ощущение живых матчей. {w}Ты не мог чувствовать каждый удар или даже малейший сдвиг в движении в  симуляторе матчей."
    voice "audio/voice/E1/D3/S4/Shou/31.ogg"
    ss "Как видишь, у нас обоих одинаковое стандартное оборудование. У тебя есть энергетический щит для блокирования, двигатели для передвижения, оружие дальнего и ближнего боя.."
    
    "Я осмотрел свой GEAR и нашёл всё, что он упомянул."
    
    pf "Какая-то конкретная причина, почему мы не играем нашим личным оружием?"
    voice "audio/voice/E1/D3/S4/Shou/32.ogg"
    ss "Это сровняет игровое поле. Придётся победить только своими умениями."
    
    pf "Пытаешься узнать из чего я сделан?"
    
    "Сё просто усмехнулся."
    voice "audio/voice/E1/D3/S4/Shou/33.ogg"
    ss "Помни, что ты должны использовать правильнное оружие в нужное время. Обычно ты можете сделать несколько шагов, но ты должен думать быстро!"
    
    menu:
        "Хорошо, спасибо!":
            pf "Так трюк в том, чтобы просто реагировать в соответствии с ситуацией."
            voice "audio/voice/E1/D3/S4/Shou/34.ogg"
            ss "Ты понялt!"
    
        "Это не первоё моё родео.":
            pf "Мне не привыкать рубить GEAR своим клинком."
            "Сё фыркнул от смеха."
            voice "audio/voice/E1/D3/S4/Shou/35.ogg"
            ss "Я надеюсь, ты разбавишь обстановку несколькими выстрелами."
            "Я не мог перестать улыбаться."
    
        "Погнали уже.":
            pf "Почему мы все ещё разговариваем? Я могу уже подстрелить тебя?"
            show note:
                xoffset 1175
                yoffset 50
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Shou/36.ogg"
            ss "Мне нравится энтузиазм."
    
    #"Как только матч начнется, мне придется быстро реагировать на его действия, пока битва не закончится. {w}Каким бы ни был правильный ход, мне придется тщательно обдумать это. Аккуратность - ключ к победе."
    voice "audio/voice/E1/D3/S4/Shou/37.ogg"
    ss "Ты готов?"
    pf "Ага."
    voice "audio/voice/E1/D3/S4/Shou/38.ogg"
    ss "Тогда погнали!"
    
    
    
    $ survived = 0
    $ practiceScore = 0
    
    $ mcEnergyMax = 200
    $ mcEnergy = 200
    $ enemyHPMax = 200
    $ enemyHP = 200
    
    $ qtebase = 10
    $ qtereaction = qteath + qtetrack + qtebase
    $ qtetotal = qtereaction
    $ t_var = qtereaction
    
    
    #$ inv.add("defaultCore")
    #$ inv.add("defaultFrame")
    #$ inv.add("defaultThruster")
    #$ inv.add("defaultBuster")
    #$ inv.add("defaultRifle")
    
    #$ inv.equip("defaultCore")
    #$ inv.equip("defaultFrame")
    #$ inv.equip("defaultThruster")
    #$ inv.equip("defaultBuster")
    #$ inv.equip("defaultRifle")
    
    
    
    #show screen battle_screen
    # Start rapid combat sequence, there is no failure state
    #$ context = "E1D3S4_ShouPracticeComplete"
    #$ enemy = "shou"
    #$ mode = "default"
    #$renpy.pause(1)
    #jump qte_game
    # And jump back here after timer ends
    
    
 


    "Мои руки легко встали на своим места и держали управление. Я не мог перестать улыбаться, так как моё сердце билось быстрее в ожидании боя."
    "Я скучал по этому."
    "Орёл перешёл в боевую стойку и держал пушку, пока Сё активировал свои двигатели и направил на меня двойные пистолеты."



    $ E1C1E1_C = 0

    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E1C1E1_L1")
    menu:
        "Отпрыгнуть!":
            jump E1C1E1_W1

        "Слишком медленно…":
            $ E1C1E1_C += 1
            jump E1C1E1_L1

        "Увернуться!":
            jump E1C1E1_W1

    label E1C1E1_L1:
        $ renpy.hide_screen ("timer_scr")
        
        
        show shou att with Dissolve(.45):
            xoffset 0
        play sound "audio/sfx/GEAR Combat/SMG.ogg"
        $renpy.pause(.35)
        
        play sound2 hitSound
        
        show mc blo at bl, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -75
                
                
        "Я слишком медленно среагировал и не смог увернуться, но поднял щит в самый последний момент и поглотил вытрел."
        "Все же, приборная панель предупредительно замигала. Я принял слишком много урона! Нужно минимизировать попадания по себе… Я не переживу полный урон."
        jump E1COMBATCONVERGENCE1

    label E1C1E1_W1:
        $ renpy.hide_screen ("timer_scr")
        
        
        show shou att with Dissolve(.45):
            xoffset 0
        play sound "audio/sfx/GEAR Combat/SMG.ogg"
        $renpy.pause(.05)
        
        play sound2 dodSound
        show mc dod at bl with Dissolve(.45):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -150

        
        
        "Я увернулся и его атака прошла мимо. Я достал пушку и выстрелил в ответ. Он увернулся, но выстрел всё равно задел его, так что получил немного урона."
        jump E1COMBATCONVERGENCE1

    label E1COMBATCONVERGENCE1:
    "Как только я ускорился вперёд, Сё отступил, чтобы сохранить дистанцию между нами. Он снова выстрелил, но его точность не хороша, так что я уклонился. Держа пушку я прицелился…"

    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E1C1E1_L2")
    menu:
        "Стрелять!":
            jump E1C1E1_W2

        "Палить!":
            jump E1C1E1_W2

        "Промахнуться…":
            $ E1C1E1_C += 1
            jump E1C1E1_L2


    label E1C1E1_L2:
        $ renpy.hide_screen ("timer_scr")
        
        
        show shou att with Dissolve(.45):
            xoffset 0
        play sound "audio/sfx/GEAR Combat/SMG.ogg"
        $renpy.pause(.35)
        
        play sound2 hitSound
        
        show mc blo at bl, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -75
                
                
        "Рука дрогнула, Сё легко увернулся, а затем выстрелил в ответ. Я отпрыгнул, но я был недостаточно быстр, и я вздрогнул, когда получил ещё один удар."
        if E1C1E1_C == 1:
            "Щит потреблял энергию, когда поглощал удары, и теперь я на опасно низком уровне. Не думаю, что смогу поглотить ещё один удар"
            jump E1COMBATCONVERGENCE2
        if E1C1E1_C == 2:
        
            play sound Depowered
            show mc mech with dissolve:
                xoffset -200
            
            "Щит исчез когда GEAR потемнел."
            jump E1D3S4_ShouPracticeComplete

    label E1C1E1_W2:
        $ renpy.hide_screen ("timer_scr")
        

        show mc attR with Dissolve(.45)
        play sound rangeSound
        play sound2 hitSound
        
        show shou blo at br, Shake(None, 1, dist=20):
        
        
        "Моя точность хороша, и щит Сё замерцал, поглощая выстрел. Судя по глубине мерцания, похоже, он получил значительное количество урона!"
        jump E1COMBATCONVERGENCE2


    label E1COMBATCONVERGENCE2:
    "Поскольку Сё любит использовать оружие дальнего боя, мне лучше сократить дистанцию и заставить его вступить в ближний бой! Я ускорился вперед..."


    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E1C1E1_L3")
    menu:
        "Промах…":
            $ E1C1E1_C += 1
            jump E1C1E1_L3

        "Руби!":
            jump E1C1E1_W3

        "Кромсай!":
            jump E1C1E1_W3

        "Уловка…":
            $ E1C1E1_C += 1
            jump E1C1E1_L3

        "Атака!":
            jump E1C1E1_W3

    label E1C1E1_W3:
        $ renpy.hide_screen ("timer_scr")
        
        
        show mc ready at bl, Shake(None, 1, dist=20):
            xoffset 0
            xzoom -1
            parallel:
                easeout .1 alpha 1.0
            parallel:
                easeout .1 xoffset 250
        $renpy.pause(.1)

        play sound meleeSound
        show mc attM at bl with Dissolve(.2):
            xoffset 400

        show white with Dissolve(0.15):
        play sound2 hitSound
        hide white with Dissolve(0.25)
        
        show shou mech at br, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset 150
                
 
        "Я переключил меч на среднее ускорение и замахнулся им по высокой дуге. Сё попытался блокировать пистолетами, и меч ударился о них с громким треском."
        "Мы боролись в битве воли, и капли пота падали на лицо. Громкий рёв вырвался с губ, когда я направил всю силу в атаку… И бробил защиту Сё!"
        
        play sound Depowered
        
        "Как только мой меч пробился, GEAR Сё потемнел."
        $ E1C1_WON = 1
        jump E1D3S4_ShouPracticeComplete

    label E1C1E1_L3:
        $ renpy.hide_screen ("timer_scr")
        
        
        
        show shou att with Dissolve(.45):
            xoffset 0
        play sound "audio/sfx/GEAR Combat/SMG.ogg"
        $renpy.pause(.35)
        
        play sound2 hitSound
        
        show mc ready at bl, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -75
        
        
        "Я переключил меч на среднее ускорение и замахнулся им по высокой дуге, Но Сё выстрелил прежде, чем я успел двинуться. Я не был готов блокировать выстрелы и получил ещё удар по щиту!"
        "Приборная панель предупредительно замигала, но я пытался игнорировать её и ясно мыслить. Когда я был в пределах досягаемости Сё, то сделал замах и ударил по щиту."
        
        play sound Depowered
        
        "Он парировал выстрелом в упор, который невозможно заблокировать, и теперь я полностью побеждён."
        jump E1D3S4_ShouPracticeComplete







 
    
    
    label E1D3S4_ShouPracticeComplete:
        play sound "audio/sfx/GEAR/GEAR Virtual Training Simulator.ogg"
        $renpy.pause(2.0)
        $ renpy.hide_screen ("battle_screen")
        $ practiceScore = survived
        scene black with fade
        stop music fadeout 3
        play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
        $renpy.pause(1)
        play ambient "audio/ambience/Hangar.ogg" fadein 1
        "Как только матч закончился, я выключил GEAR и спустился на землю."
        play sound "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
        $renpy.pause(2.5)
        scene bg campus hangar day with fade
        play sound "audio/sfx/GEAR/GEAR Elevator.ogg"
        $renpy.pause(2.5)
        "Через пару минут показался Сё."
        show shou neu at cc with dissolve
        
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
    if (E1D2S11_JoinedTheTeam == 1):
        if E1C1_WON == 0:
            pf "Так, насчёт матча--"
            show shou mis at cc with dissolve
            voice "audio/voice/E1/D3/S4/Shou/39.ogg"
            ss "Всё хорошо, чувак. Я уверен, ты был занят переездом и всё такое."
            pf "Да, я буду более сосредоточен в следующих матчах."
            show shou smi at cc
            "Сё кивнул."
    
        else:
            show shou hap at cc with dissolve
            show note:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Shou/46.ogg"
            ss "Неплохо! Я знал, что сделал всё правильно, выбрав тебя. У меня шестое чувство на такие вещи."
            pf "Хех, спасибо. Ты и сам был неплох."
    
    if (E1D2S11_JoinedTheTeam == 0):
        if E1C1_WON == 0:
            pf "Ну что ж."
            show shou mis at cc with dissolve
            voice "audio/voice/E1/D3/S4/Shou/40.ogg"
            ss "Я думаю, тебе просто нужно вникнуть в суть вещкё."
            pf "Да, определённо. По крайней мере, я теперь знаю чего ожидать, так что буду держаться лучше"
            show shou smi at cc
            "Сё кивнул."
    
        else:
            show shou hap at cc with dissolve
            show note:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S4/Shou/21.ogg"
            ss "Неплохо! Ты определённо сможешь продержаться на квалификации."
            pf "Спасибо."
    
        show shou mis at cc
        voice "audio/voice/E1/D3/S4/Shou/22.ogg"
        ss "Как проходит поиск команды?"
    
        if (E1S2D10_AskedOtherTeams == 1):
            pf "Не так, как я ожидал."
            show shou sad at cc
            voice "audio/voice/E1/D3/S4/Shou/23.ogg"
            ss "Облом. Большинство команд собираются вместе летом, поэтому они хорошо подготовлены к отборочным."
            pf "Да, мне кажется ты упоминал это в прошлый раз. Тем не менее, я думал, что будет больше новых людей, которые не нашли команду, или больше команд, которым не достаёт участника."
            show shou mis at cc
            voice "audio/voice/E1/D3/S4/Shou/24.ogg"
            ss "Ну, моё предложение все ещё открыто…"
    
        if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
            pf "Вообще-то у меня ещё не было шанса поговорить с другими пилотами."
            show shou thi at cc with dissolve
            voice "audio/voice/E1/D3/S4/Shou/25.ogg"
            ss "А, ну, смотри, я знаю, что с Каори не всё прошло гладко, но предложение присоединиться к нашей команде все еще открыто."
            pf "Я почти уверен, что у Каори случится сердечный приступ, если она узнает, что я присоединился."
            show shou smi at cc
            voice "audio/voice/E1/D3/S4/Shou/48.ogg"
            ss "Каори поймет, что если хочет участвовать в отборочных турнирах, то тебе придется присоединиться. Твоё вступление выгодно нам так же, как и тебе."
    
        "У меня нет другого выбора, и квалификация завтра."
        pf "Конечно, я вступлю."
        show shou hap at cc with dissolve
        "Сё вернулся к своей обычной ухмылке."
        show note:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S4/Shou/26.ogg"
        ss "Потрясающие! Поверь мне, это будет хорошо!"
    
        if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
            pf "Так ты уверен, что Каори примет это?"
            show shou smi at cc with dissolve
            "He smiles reassuringly."
            voice "audio/voice/E1/D3/S4/Shou/27.ogg"
            ss "Не волнуйся, я поговорю с ней."
            
    show shou cur at cc
    voice "audio/voice/E1/D3/S4/Shou/28.ogg"
    ss "В любом случае, мы хотим встретиться завтра перед квалификацией, так что скажи свой номер?"
    show shou smi at cc
    "Мы быстро обменялись номенами."
    pf "Так… Полагаю, надо пойти и сделать кое-то."
    show shou hap at cc
    voice "audio/voice/E1/D3/S4/Shou/47.ogg"
    ss "Да, мне тоже. Хорошо, тогда увидимся позже!"
    
    menu:
        "Погоди, давай сыграем ещё матч!":
            pf "Сё, подожди!"
            show shou cur at cc with dissolve
            show question:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            "Он остановился и удивлённо посмотрел на меня."
            pf "Как насчёт реванша?"
            show shou mis at cc with dissolve
            "Он ухмыльнулся."
            voice "audio/voice/E1/D3/S4/Shou/29.ogg"
            ss "Да, чёрт побери! Те же правила?"
            pf "Погнали."
            hide shou with dissolve
            "Он побежал к своему GEAR и я вернулся в свой."
            scene black with fade
            #fade to black
            $renpy.pause(2.5)
            "После, потренировавшись, пришло время разойтись."
            stop music fadeout 3
            # fill in whatever needs to be here for S8
            $ E1D3S4_PlayedAnotherWithShou = 1
            jump E1D3S8
    
        "Мне нужно учиться.":
            stop music fadeout 3
            pf "Пока."
            hide shou with dissolve
            "Как только я проводил его взглядом, то направился в библиотеку."
            scene black with fade
            stop ambient fadeout 3
            $renpy.pause(1)
            scene bg campus library day with fade
            play ambient "audio/ambience/Ace Academy Library.ogg" fadein 1
            "Я только получил задания для одного урока, но я не хочу отставать. {w}К тому же, если сделаю уроки сейчас, то в выходные смогу делать что захочу."
            jump E1D3S6
    
        "В зале пилотов всегда что-то происходит.":
            pf "Пока."
            hide shou with dissolve
            stop ambient fadeout 3
            scene bg campus lounge day with fade
            play ambient "audio/ambience/Pilot Lounge.ogg" fadein 1
            play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
            "Я вернулся в зал пилотов. До сих пор каждый раз, когда я проходил через зал, он был полон студентов. {w}Я уверен, что я либо встречу кого-нибудь классного, либо найду что-нибудь интересное."
            $ E1D3S4_WentToThePilotsLounge = 1
            jump E1D3S5
