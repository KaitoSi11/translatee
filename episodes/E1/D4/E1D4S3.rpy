label E1D4S3:
     
    pf "Подожди, прежде чем мы пойдём, как эти матчи работают?"
    show kaori neu at r3
    voice "audio/voice/E1/D4/S3/Kaori/1.ogg"
    ki "Это зависит от того, сколько очков ты получил. Мы будем соревноваться с запрограммированными ИИ GEAR--"
    show shou mis at cc
    voice "audio/voice/E1/D4/S3/Shou/1.ogg"
    ss "Как босс, которого сложно победить."
    voice "audio/voice/E1/D4/S3/Kaori/3.ogg"
    ki "--и наш счет рассчитывается так - сколько мы победили, и как хорошо мы сражались в целом. Такие вещи, как точность, сколько ударов мы берем, тактика, командная работа - все это складывается."
    pf "Так сколько очков всё это стоит?"
    show shou hap at cc
    voice "audio/voice/E1/D4/S3/Shou/3.ogg"
    ss "Они не делятся точными числами, но все знают, что победа над ИИ даёт дофига очков!"
    show kaori ann at r3
    show exclamation:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S3/Kaori/5.ogg"
    ki "Теперь поторопись и садись в свой GEAR! Нам действительно нужно практиковаться перед нашим выходом."
    hide kaori with dissolve
    "Она развернулась и мы разошлись."
    
    stop music fadeout 3
    scene black with fade
    $renpy.pause(1)
    play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
    $renpy.pause(2.5)
    scene cg GEAR cockpit first1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    play sound "audio/sfx/Impacts/Luggage Drop.ogg"
    $renpy.pause(2.5)
    stop ambient fadeout 3
    play sound "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
    $renpy.pause(2.5)
    play sound "audio/sfx/GEAR/GEAR Boot Up 1.ogg"
    $renpy.pause(2.5)
    scene cg GEAR cockpit first2 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    play ambient "audio/ambience/GEAR Cockpit.ogg" fadein 1 fadeout 1
    $renpy.pause(2.5)
    play sound "audio/sfx/GEAR/GEAR Boot Up 2.ogg"
    $renpy.pause(2.5)
    scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    "Забравшись в свой GEAR, я запустил симуляцию."
    play sound "audio/sfx/GEAR/GEAR Virtual Training Simulator.ogg"
    #NOT COMPLETE YET, will need to figure out of this text is happening in the simulator or during the battle screen
    # "Я проголосовал в кабине" - Austin
    
    "Обычные статистические данные всплывали на экране, но что-то в них казалось странным."
    "Голос Каори донёсся через коммуникатор."
    voice "audio/voice/E1/D4/S3/Kaori/2.ogg"
    ki "Где твоё оружие?"
    pf "Я не знаю. Глянем, есть ли что-то в настройках."
    voice "audio/voice/E1/D4/S3/Kaori/4.ogg"
    ki "Почему ты не провёл полную проверку своего GEAR?"
    pf "Я провёл. Он не сканирует оружие, так как оно не является основной частью функций меха."
    voice "audio/voice/E1/D4/S3/Kaori/6.ogg"
    ki "У твоего \"боевого\" GEAR нет оружия, установленного в качестве основной функции во время проверок?"
    "Я никогда не сталкивался с этой проблемой раньше, хотя она тут и права. {w}Я пробовал каждую комбинацию настроек, о которой только мог подумать, но мое оружие все еще не регистрировалось." 
    voice "audio/voice/E1/D4/S3/Shou/4.ogg"
    ss "Попробуй подождать минуту. Иногда GEAR лагает, когда прогревается."
    pf "Тут не должно быть лагов."
    "Мы всё равно подождали. {w}Через несколько минут было ясно, что мое оружие не собиралось показываться."
    pf "Я не знаю, что происходит."
    voice "audio/voice/E1/D4/S3/Kaori/10.ogg"
    ki "У тебя вообще есть оружие?"
    pf "Конечно есть!"
    voice "audio/voice/E1/D4/S3/Kaori/11.ogg"
    ki "Тогда где оно?"
    "Внезапно слышится тихий голос Маю."
    voice "audio/voice/E1/D4/S3/Mayu/1.ogg"
    ma "Возможно, они все ещё обрабатываются на таможне. Я слышала, что GEAR и их аксессуары обрабатываются отдельно." 
    voice "audio/voice/E1/D4/S3/Shou/5.ogg"
    ss "В этом есть смысл."
    pf "Как долго проходит это?"
    voice "audio/voice/E1/D4/S3/Mayu/2.ogg"
    ma "Я-Я не знаю."
    voice "audio/voice/E1/D4/S3/Kaori/12.ogg"
    ki "Слишком долго! Нам нужно это оружие прямо сейчас."
    voice "audio/voice/E1/D4/S3/Shou/6.ogg"
    ss "Не волнуйся, всё будет в порядке." 
    voice "audio/voice/E1/D4/S3/Kaori/13.ogg"
    ki "Нет, не будет! Как он будет сражаться без оружия?" 
    pf "Я что-нибудь придумаю. Давай просто наснём матч. У нас не так много времени."
    voice "audio/voice/E1/D4/S3/Kaori/14.ogg"
    ki "Хорошо." 
    
    #Transition to "game world"
    stop ambient fadeout 3
    
    #show all mechs for the first time
    voice "audio/voice/E1/D4/S4/Kaori/1.ogg"
    ki "Все готовы?"
    
    "Все коммуникаторы мигнули зелёным цветом в подтверждение."
    voice "audio/voice/E1/D4/S4/Kaori/2.ogg"
    ki "Хорошо, начнём!"
    
    
    
    scene black with fade
    
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 1
    show bg battleground day with dissolve:
        alpha 1
        xzoom 1
        yzoom 1
        yoffset 25
        xoffset 0
        
    show mayu mech at tl with dissolve:
        xzoom -.8
        yzoom .8
    show shou mech at tr with dissolve:
        xzoom -.8
        yzoom .8
    show kaori mech at mm with dissolve:
        xzoom -1
    show mc mech at bl with dissolve:
        xzoom -1

    show bg battleground day:
        parallel:
            easein 3.0 alpha 1.0
        parallel:
            easein 3.0 xoffset -200
            
    show mayu mech at tl:
        xzoom -.8
        yzoom .8
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset -1500
            
    show shou mech at tr:
        xzoom -.8
        yzoom .8
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset -1500
            
    show kaori mech at mm:
        xzoom -1
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset -1300
            
    show mc mech at bl:
        xzoom -1
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset -1300
            
    # ai mechs
    $renpy.pause(2.5)
    show aiR neu at tr with dissolve:
        xzoom .8
        yzoom .8
            
    show aiR2 neu at tl with dissolve:
        xzoom .8
        yzoom .8
            
    show aiM neu at mm with dissolve
            
    show aiM2 neu at br with dissolve
    
    $renpy.pause(1)
    
    scene bg battleground day with fade
    show mc mech at bl with dissolve:
        xzoom -1
    show aiM att at br with dissolve
    show mc ready at bl with dissolve:
        xzoom -1
        
        
        
        
        
        
        
    "Мы все встали на свои позиции и встали в боевую стойку напротив ИИ. Мой ближайший враг бежал на меня с парными мечами!"
    
    
    #$renpy.pause(1)
    ##Start simulated combat. You match up against an AI mech. You don't have any "attack" choices, just dodging and blocking.
    #$ enemy = "aiM"
    #$ D4Jetpack = 0
    #$ survived = 0
    #$ teamPractice = 0
    #$ mode = "retreat"
    #$ context = "E1D4S3_TeamPracticeComplete"
    
    #$ mcEnergyMax = 200
    #$ mcEnergy = 200
    #$ enemyHPMax = 100
    #$ enemyHP = 100
    
    #$ qtebase = 10
    #$ qtereaction = qteath + qtetrack + qtebase
    #$ qtetotal = qtereaction
    #$ t_var = qtereaction
    
    
    
    #show screen battle_screen
    #$renpy.pause(1)
    ##show screen timer_scrReaction(place="E1D4S3_TeamPracticeComplete")
    #jump qte_game
    # and jump here after finished
    
 
 
 
 
     
    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E1D4S3_L1")
    menu:
        "Танцуй!":
            jump E1D4S3_W1

        "Медленно…":
            jump E1D4S3_L1

        "Уворачивайся!":
            jump E1D4S3_W1

    label E1D4S3_W1:
        $ renpy.hide_screen ("timer_scr")
        
        show aiM att at br:
            xoffset 0
            parallel:
                easeout .1 alpha 1.0
            parallel:
                easeout .1 xoffset -250
        $renpy.pause(.1)

        play sound meleeSound
        show aiM att at br with Dissolve(.2):
            xoffset -400        
        
        play sound2 dodSound
        show mc dod at bl with Dissolve(.45):
            parallel:
                easeout .5 alpha 1.0
            parallel:
                easeout .5 xoffset -150
        
        "Я едва успел уйти в сторону!"
        "Это не сулило ничего хорошего…"
        jump E1D4S3_COMBATCONVER1

    label E1D4S3_L1:
        $ renpy.hide_screen ("timer_scr")
        
        show aiM att at br:
            xoffset 0
            parallel:
                easeout .1 alpha 1.0
            parallel:
                easeout .1 xoffset -250
        $renpy.pause(.1)

        play sound meleeSound
        show aiM att at br with Dissolve(.2):
            xoffset -400

        show white with Dissolve(0.15):
        play sound2 hitSound
        hide white with Dissolve(0.25)
        
        show mc blo at bl, Shake(None, .5, dist=20):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -150
                
                
        "Я не был готов к нападению и пытался поднять щит. ИИ взмахнул мечом и ударил меня в плечо."
        "Приборная панель Орла сходила с ума от звуковых сигналов и предупреждений, когда мой уровень энергии падал."
        "Нельзя пропустить ещё один удар, или мне придёт конец!"
        jump E1D4S3_COMBATCONVER1


    label E1D4S3_COMBATCONVER1:
    "Я ответил апперкотом и ударом в солнечное сплетение, которые нанесли некоторый урон, но рядом не стояло с сокрушительным ударом, который я получил. ИИ прервал мою атаку и снова напал."


    $ qtetotal = 5
    $ t_var = qtetotal
    show screen timer_scr(place="E1D4S3_L2")
    menu:
        "Замер…":
            jump E1D4S3_L2

        "Защищаться!":
            jump E1D4S3_W2

        "Блокировать!":
            jump E1D4S3_W2

    label E1D4S3_W2:
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
        show mc ready at bl with Dissolve(.2):
            xoffset 250

        play sound2 hitSound
        
        show aiM neu at br, Shake(None, .5, dist=10):
            parallel:
                easeout .3 alpha 1.0
            parallel:
                easeout .3 xoffset -100
                
        "Я поднял руку чтобы защититься, так как его меч снова бил по моему щиту. Свободной рукой я ударил ИИ в бок."
        "Как и прежде, Орёл получил тревожное количество урона, в то время как ИИ едва ли почувствовал мою атаку."
        $ E1D4S3_FakeFightWin = 1
        jump E1D4S3_TeamPracticeComplete

    label E1D4S3_L2:
        $ renpy.hide_screen ("timer_scr")
        "ИИ нанёс удар мечом, и Орёл запротестовал серией звуковых сигналов и вспышек, предупреждающих меня об опасно низких уровнях энергии."
        "У меня едва хватало времени, чтобы зарегистрировать предупреждения, прежде чем ИИ снова замахнулся!"
        jump E1D4S3_TeamPracticeComplete
         
     
 
 
 
 
    
    
    label E1D4S3_TeamPracticeComplete:
        #play sound "audio/sfx/GEAR/GEAR Virtual Training Simulator.ogg"
        #$renpy.pause(2.5)
        $ renpy.hide_screen ("battle_screen")
        $ teamPractice = survived
        if E1D4S3_FakeFightWin == 0:
            #IF you do poorly
            show aiM att behind mc:
                easeout .35 xoffset -850
            $renpy.pause(.15)
            play sound "audio/sfx/GEAR Combat/Sword Double.ogg"
            $renpy.pause(.15)
            play sound "audio/sfx/GEAR Combat/Hit.ogg"
            show mc mech at bl, Shake(None, .5, dist=25) with dissolve
            $renpy.pause(.5)
            play sound "audio/sfx/GEAR Combat/Depower.ogg"
            hide mc with dissolve
            $renpy.pause(1.0)
            "Ну, это был провал. Меня уничтожили. В свою защиту могу сказать, что это был безнадёжный матч, так как у меня не было оружия."
    
        if E1D4S3_FakeFightWin == 1:
            #IF you do well
            "Я уклонялся и блокировал большинство атак. Однако я не мог контратаковать - только защищаться."
            show aiM att behind mc:
                easeout .35 xoffset -600
            $renpy.pause(.15)
            play sound "audio/sfx/GEAR Combat/Sword Double.ogg"
            $renpy.pause(.15)
            play sound "audio/sfx/GEAR Combat/Hit.ogg"
            show mc mech at bl, Shake(None, .5, dist=25) with dissolve:
                linear .4 xoffset -75
            $renpy.pause(.5)
            play sound "audio/sfx/GEAR Combat/Depower.ogg"
            hide mc with dissolve
            $renpy.pause(1.0)
            "Когда моё ядро постепенно истощилось, Ии GEAR не потребовалось много усилий, чтобы уничтожить меня."
            
        
        #fade to finished simulation
        scene black with fade
        #scene cg GEAR cockpit first3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        "Без четвёртого участника моей команде едва удалось победить."
    
    stop music fadeout 3
    scene black with fade
    
    play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg" fadein 1
    "Мы выключили симулятор и вылезли из своих GEAR."
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 3
    play ambient "audio/ambience/Hangar.ogg" fadein 1
    $renpy.pause(1)
    
    scene bg campus hangar day with fade
    $renpy.pause(1)
    
    show mayu neu at l3
    show kaori dis at cc
    show shou neu at r3:
        xzoom -1
        xoffset 75
    with dissolve
    $renpy.pause(.5)
    "Я начал идти к команде, но они добрались до меня первыми."
    show kaori ang with dissolve
    show vein:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S3/Kaori/15.ogg"
    ki "Мы не можем так играть матч!Мы едва набрали хоть какие-то очки." 
    show kaori ann with dissolve
    voice "audio/voice/E1/D4/S3/Shou/7.ogg"
    ss "Не волнуйся, Каори. Я уверен, он скоро получит своё оборудование." 
    voice "audio/voice/E1/D4/S3/Kaori/16.ogg"
    ki "Недостаточно скоро! Матч сегодня."
    show kaori dis
    voice "audio/voice/E1/D4/S3/Kaori/16_1.ogg"
    ki "Может он не должен участвовать. Мы можем сказать им, что у нас четыре члена команды, но один из наших GEARs не в состоянии сражаться."
    show mayu dis with dissolve
    "Маю решительно посмотрела на неё."
    voice "audio/voice/E1/D4/S3/Mayu/3.ogg"
    ma "Нет. он должен. Это единственный способ." 
    show mayu neu with dissolve
    "Сё извиняющеся смотрел на меня."
    show shou thi with dissolve
    show drop:
        xoffset 1250
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S3/Shou/8.ogg"
    ss "Слушай, может тебе просто держаться сзади. Без оружия ИИ просто погубит тебя." 
    pf "Я все ещё могу помочь нам набрать очки." 
    show kaori neu
    voice "audio/voice/E1/D4/S3/Kaori/17.ogg"
    ki "Нет, Сё прав. Тебе нужно держаться позади. Это увеличит наши очки, что сейчас важно." 
    show shou cur with dissolve
    "Сё смотрел в шоке."
    show shocked:
        xoffset 1250
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S3/Shou/9.ogg"
    ss "Ты только что согласилась со мной?" 
    show kaori ann
    show exclamation:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S3/Kaori/18.ogg"
    ki "Не сейчас, Сё!" 
    show shou smi
    voice "audio/voice/E1/D4/S3/Shou/10.ogg"
    ss "Ты никогда не соглашалась со мной!" 
    voice "audio/voice/E1/D4/S3/Kaori/19.ogg"
    ki "Идиот! Почему ты продолжаешь говорить это?" 
    
    "В этот момент группа инженеров подошла к нам."
    hide shou
    hide mayu
    hide kaori
    with dissolve
    
    show studentM extra at l3:
        xoffset -100
    show kaori dis at cc:
        xoffset 75
        xzoom -1
    show shou neu at r3:
        xzoom -1
        xoffset 125
    with dissolve
    voice "audio/voice/E1/D4/S3/Engineer/1.ogg"
    eng1 "Что ваши GEARs все ещё стоят тут?"
    show shou cur
    show question:
        xoffset 1250
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S3/Shou/11.ogg"
    ss "Что?"
    voice "audio/voice/E1/D4/S3/Engineer/2.ogg"
    eng1 "Они должны быть готовы к следующему матчу."
    show kaori neu
    voice "audio/voice/E1/D4/S3/Kaori/20.ogg"
    ki "Это значит, что мы следующие. Пойдём."
    pf "Что насчёт наших GEARs?"
    voice "audio/voice/E1/D4/S3/Kaori/21.ogg"
    ki "Инженеры позаботятся об этом."
    
    stop music fadeout 3.0
    stop ambient fadeout 3.0
    scene black with fade
    
    "Инженеры пошли к нашим GEAR. Моя команда разделилась и направилась к раздевалкам."
    "Мы быстро переоделись в боевую форму. К счастью, я сохранил старую из Штатов"
    "Я следовал за Сё в предбоевую комнату, которая была маленькой комнатой, соединяющей раздевалку и арену."
    
    
    
    $renpy.pause(1.0)
    
    $ shoOut = "Pilot"
    $ mayOut = "Pilot"
    $ kaoOut = "Pilot"
    play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 1
    scene bg campus battleroom day
    show shou smi at l3:
        xoffset -150
    with fade
    
    
    
    "Пространство казалось тесным. Диваны у стен, а в центре круглый стол."
    
    
    show kaori neu at cc:
        xoffset 200
    show mayu neu at r3:
        xoffset 200
        xzoom -1
    with dissolve
    
    "Едва я успел войти в комнату, когда Каори и Маю вошли в обтягивающих костюмах, подчёркивающих их формы."
    
    
    menu:
        "Так изящно!":
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
            pf "Ваши костюмы круты!"
            show kaori ske 
            show mayu cur
            with dissolve
            show dots:
                xoffset 920
                yoffset 110
                xzoom .75
                yzoom .75
            show question:
                xoffset 1375
                yoffset 135
                xzoom .75
                yzoom .75
            "Каори странно на меня смотрела. Маю выглядела немного удивленной."
            show mayu smi with dissolve
            voice "audio/voice/E1/D4/S3/Mayu/5.ogg"
            ma "Эм, спасибо?"
            pf "Без проблем. Вы обе отлично выглядите!"
            show kaori dis with dissolve
            "Каори нахмурилась."
            voice "audio/voice/E1/D4/S3/Kaori/23.ogg"
            ki "Хорошо…"
            "Хотя большинство костюмов пилотов мало чем отличались друг от друга, японские модели всегда имели более \"аэродинамичный\" вид. Впервые мне удалось увидеть эти костюмы вблизи--"
            show kaori ang
            show shou cur
            with dissolve
            $renpy.pause(.5)
            show vein:
                xoffset 920
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Kaori/24.ogg"
            ki "Хватит пялиться!!"
            show kaori dis
            pf "Чт…?"
            show mayu sur b1 with dissolve
            "Глаза Маю округлились и она скрестила руки на груди."
            show mayu ner b1
            show shoBlush:
                xoffset 1375
                yoffset 135
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Mayu/6.ogg"
            ma "Я не думала, что ты такой."
            pf "Нет, я просто хотел сказать, что эти костюмы хорошо смотрятся на вас."
            show kaori ann
            voice "audio/voice/E1/D4/S3/Kaori/25.ogg"
            ki "Мы поняли, что ты имел в виду! И мы не ценим то, что ты пялишься!"
            show storm:
                xoffset 920
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Kaori/25_01.ogg"
            ki "Давай, Маю. Пойдем, прежде чем он скажет что-то еще, о чём пожалеет."
            hide kaori
            hide mayu
            with dissolve
            "Она притянула Маю к себе, и они направились к столу.."
            hide shou with dissolve
            show shou mis at cc with dissolve
            $renpy.pause(.5)
            stop music fadeout 5
            show shou mis
            voice "audio/voice/E1/D4/S3/Shou/12.ogg"
            ss "Ты дилетант, братишка."
            pf "Нет, серьезно, я не смотрел на них так."
            pf "Погоди, это действительно не так получилось."
            "Shou just shakes his head."
            show shou cur
            voice "audio/voice/E1/D4/S3/Shou/13.ogg"
            ss "Каждый должен носить эти костюмы. Ты делаешь это странным."
            hide shou with dissolve
            "Он пошёл к ним за стол."
    
        "Мне нравится.":
            $ E1D4S3_Stare = 1
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
            "Их форма ничего не оставляла для воображения. Я с нетерпением наблюдал за девушками, когда они подходили. Я только что умер и попал на небеса?"
            show mayu cur
            show question:
                xoffset 1375
                yoffset 135
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Mayu/7.ogg"
            ma "Привет?"
            "..."
            show shou cur
            show mayu cur
            show kaori ang
            with dissolve
            $renpy.pause(.5)
            show exclamation:
                xoffset 920
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Kaori/26.ogg"
            ki "ЭЙ!"
            show kaori ann
            "Сердитые взгляд Каори вывел меня из задумчивости. Её руки были на бёдрах."
            show vein:
                xoffset 920
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Kaori/27.ogg"
            ki "Что ты делаешь?"
            pf "Я просто восхищался вашей невероятно эффективной и умной тактикой отвлечения."
            "Сё и девушки просто смотрели на меня."
            show kaori ske
            voice "audio/voice/E1/D4/S3/Kaori/28.ogg"
            ki "Что?"
            pf "С такой формой, другая команда будет настолько отвлечена, что забудет о битве и даст нам преимущество."
            show mayu sur b1
            show kaori ann
            show shou smi
            with dissolve
            show shoBlush:
                xoffset 1375
                yoffset 135
                xzoom .75
                yzoom .75
            "Маю подняла руки, чтобы спрятать грудь. Каори смотрела на меня и скрестила руки."
            show mayu ner b1 with dissolve
            voice "audio/voice/E1/D4/S3/Kaori/29.ogg"
            ki "Как другая команда увидит нас, когда мы будем {i}внутри{/i} гигантского робота?"
            pf "Ох…"
            show kaori dis
            voice "audio/voice/E1/D4/S3/Kaori/30.ogg"
            ki "Именно. Эти костюмы для функциональных целей, не более того. Не будь извращенцем!"
            hide kaori
            hide mayu
            with dissolve
            "Отругав меня, Каори и Маю пошли к столу."
            hide shou with dissolve
            show shou mis at cc with dissolve
            $renpy.pause(.5)
            stop music fadeout 5
            show shou mis
            "Shou shakes his head."
            voice "audio/voice/E1/D4/S3/Shou/14.ogg"
            ss "Это была любительская ошибка, братан."
            show shou hap
            show drooling:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Shou/15.ogg"
            ss "Ты должен \"засматриваться\" чувак. Но не так очевидно."
            hide shou with dissolve
            "После этих слов мудрости он хлопнул меня по плечу, затем присоединяется к девушкам за столом." 
    
        "Без комментариев.":
            "Мы все в одинаковых костюмах. Я не фанат того, как материал облегает, но, по крайней мере, он обеспечивает достаточное движение и поглощение ударов, что, я полагаю, их цель."
            hide kaori
            hide shou
            hide mayu
            with dissolve
            "Девушки пошли прямо за стол, и Сё присоединился к ним."
    
        "Точка сброса посылок Сё выглядит без признаков жизни.":
            hide kaori
            hide mayu
            with dissolve
            "Девушки проигнорировали нас и пошли сразу к столу."
            show shou neu at cc with dissolve
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
            "Они не единственные с тесной формой. Сё тоже довольно тесно. По факту..."
            pf "Эм, Сё."
            show question:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Shou/16.ogg"
            ss "Что такое, братан?"
            pf "Ничего. Мне просто интересно, ты в порядке."
            show shou hap
            show note:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Shou/17.ogg"
            ss "Лучше не бывает! А что?"
            pf "Ты уверен, что нет чувства, что чего-то не хватает?"
            show shou cur
            "Его улыбка сменилась растерянностью."
            voice "audio/voice/E1/D4/S3/Shou/18.ogg"
            ss "Нет… Почему должлен?"
            pf "Ну, твоя ширинка расстёгнута."
            show shou sur with dissolve
            show exclamation:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            "Вздрогнув, Сё посмотрел вниз."
            stop music fadeout 5
            show shou cur
            voice "audio/voice/E1/D4/S3/Shou/19.ogg"
            ss "Там внизу нет молнии."
            pf "Похоже, там почти {i}ничего{/i} нет."
            "Сё снова взглянул на меня."
            show shou sur b1 with dissolve
            show drop:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S3/Shou/20.ogg"
            ss "Глаза вверх, чувак! Ты не должен осквернять другого братана вот так..."
            hide shou with dissolve
            "Прежде чем я успел ответить, Сё ушёл и присоединился к девушкам за столом."
    
    
    "Подойдя к столу, Каори нажала на кнопку сбоку, которая вызвала голограмму поля битвы на арене."
    play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 1
    "Четыре GEAR побольше, появились на правой стороне поля, а четыре GEAR поменьше - на другой стороне."
    show kaori neu at r3:
        xzoom -1
        xoffset 200
    show shou neu at l3:
        xoffset -250
    show mayu neu at cc:
        xoffset -300
    with dissolve
    $renpy.pause(.5)
    "Каори показала на правую сторону."
    voice "audio/voice/E1/D4/S3/Kaori/31.ogg"
    ki "Это вражеские ИИ GEAR, с которыми мы будем сражаться."
    "Она показала на другую сторону."
    voice "audio/voice/E1/D4/S3/Kaori/32.ogg"
    ki "Это мы."
    voice "audio/voice/E1/D4/S3/Kaori/33.ogg"
    ki "ИИ запрограммированы, чтобы быть сложными, поэтому важно, чтобы мы придерживались плана и работали вместе, чтобы побить их."
    show mayu dis
    "Маю торжественно говорит." 
    voice "audio/voice/E1/D4/S3/Mayu/8.ogg"
    ma "GEARs, с которыми мы стокнёмся, специально разработаны для квалификационных матчей академии ACE. Они меняются ежегодно, чтобы быть уверенным, что их нельзя победить, используя системный подход."
    
    "Легким движением пальцев Маю увеличила голограммы ИИ GEAR. Статистика боевого вооружения и частей ИИ всплыла рядом с GEARs."
    voice "audio/voice/E1/D4/S3/Mayu/9.ogg"
    ma "Похоже мы имеем два GEAR ближнего боя класса А, and two Class A long range support GEAR."
    "Каори кивнула. Протянув руку в голографическое поле, она перенесла наши GEAR на позицию на карте."
    show kaori thi
    voice "audio/voice/E1/D4/S3/Kaori/34.ogg"
    ki "Зная всё это, мы с Сё пазобьём GEAR ближнего боя, чтобы дать Маю пространство. Она сфокусируется на подавлении огня задней линии. Это должно дать нам достаточно времени, чтобы прикончить два GEAR и заняться оставшимеся."
    "Маю и Сё кивнули. Каори перенесла последний GEAR к заднему краю карты, затем многозначительно посмотрела на меня."
    show kaori neu
    show mayu neu
    voice "audio/voice/E1/D4/S3/Kaori/35.ogg"
    ki "Вот где ты будешь. Не дай убить себя."
    "Я уныло посмотрел на неё, но спорить не стал."
    "Карта замигала красным, и дверь на арену открылась."
    show shou smi
    "Лицо Сё озарилось азартом, и он практически прыгнул к двери."
    voice "audio/voice/E1/D4/S3/Shou/21.ogg"
    ss "Это наш сигнал к выходу."
    voice "audio/voice/E1/D4/S3/Kaori/36.ogg"
    ki "Все поняли план?"
    "Все кивнули."
    voice "audio/voice/E1/D4/S3/Kaori/37.ogg"
    ki "Хорошо, тогда пошли."
    
    stop music fadeout 3.0
    stop ambient fadeout 3.0
    scene black with fade
    
    "Глубоко вздохнув, я последовал за Сё и остальными к нашим GEAR."
    
    
    jump E1D4S4
