label E1D5S2:


"Я достал телефон и начал просматривать технические статьи."
"Была одна о новом симуляторе в соседней аркаде. Игра давала возможность проверить прототипы, которые еще не были протестированы или распространены. Плюс оружие звучало опасно! Стоило бы посмотреть." 
"Я взял байк и поехал к аркадам." 

label E1D5S2_ArcadeConvergence:

stop ambient fadeout 1.5
stop music fadeout 1.5
scene black with fade
$renpy.pause(1.0)


play ambient "audio/ambience/Arcade.ogg" fadein 3
play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
$renpy.pause(1.5)

scene bg activity arcade day with fade

"Тут было людно, однако большинство этих людей толпились вокрун одного симулятора, наблюдая за напряжённым матчем." 
"В правом кресле был студёнистый парень моего возраста. На его пухлом лице был решительный взляд и он кричал ряд безостановочных насмешек и оскорблений на своего противника." 

"Машина звенела - его последний соперник нокаутирован за несколько минут.." 
show gosunerd extra at cc with dissolve
voice "audio/voice/E1/D5/S2/GosuArcade/1.ogg"
fk "Хахаха! Ещё один повержен в прах! Кто следующий?" 
"Он осматривал толпу, но никто не вышел вперёд." 

menu: 
    "Я попробую!" :
        pf "Выглядит весело! Можно попробовать." 
        show gosunerd extra with dissolve:
            xzoom -1
        $renpy.pause(.25)
        "Его взгляд упал на меня и он нахмурился, когда снова осмотрел." 
        voice "audio/voice/E1/D5/S2/GosuArcade/2.ogg"
        fk "Это твои похороны." 
        pf "Разве мы не можем провести дружеский матч?" 
        voice "audio/voice/E1/D5/S2/GosuArcade/3.ogg"
        fk "Слова неудачников." 
        pf "Что вообще случилось со спортивным духом?" 
        voice "audio/voice/E1/D5/S2/GosuArcade/4.ogg"
        fk "Садись и я покажу тебе."

    "Я буду лучшим игроком.":
        pf "Я буду следующим. Эта игра зовёт меня." 
        show gosunerd extra with dissolve:
            xzoom -1
        $renpy.pause(.25)
        voice "audio/voice/E1/D5/S2/GosuArcade/5.ogg"
        fk "Зовёт тебя проиграть." 
        pf "Я слышу только зов победы. Должно быть проигрыш зовёт тебя."
        voice "audio/voice/E1/D5/S2/GosuArcade/6.ogg"
        fk "Я не проиграю!" 
        pf "Всё бывает в первый раз." 

    "Я следующий.": 
        pf "Мой черёд." 
        show gosunerd extra with dissolve:
            xzoom -1
        $renpy.pause(.25)
        voice "audio/voice/E1/D5/S2/GosuArcade/7.ogg"
        fk "Черёд проиграть." 
        pf "Посмотрим." 
        "Он открыл рот, чтобы ответить, но я сурово посмотрел на него." 
        pf "Мы здесь на разговор собрались или играть будем?" 
        voice "audio/voice/E1/D5/S2/GosuArcade/8.ogg"
        fk "Играем!" 

    "Не соревноваться с ним.":
        hide gosunerd extra with dissolve
        "Я пришёл сюда не для того, чтобы кормить троллей. Мне нужно практиковаться."
        "Найдя пустой симулятор, я начал игру."
        stop music fadeout 3.0
        stop ambient fadeout 3.0
        scene black with fade
        scene bg battleground night with fade
        show mc mech at bl with dissolve:
            xzoom -1
        show arM neu at br with dissolve
        $renpy.pause(2.5)
        #Gameplay (EASIER THAN CHALLENGING TROLL, BUT LESSER ITEMS)
        $ enemy = "arM"
        $ mode = "default"
        $ context = "E1D5S2_SoloComplete"
        
        $ mcEnergyMax = 200
        $ mcEnergy = 200
        $ enemyHPMax = 125
        $ enemyHP = 125
        
        $ survived = 0
        $ E1D5S2Score = 0
        $ E1D5S2_SoloWon = 0
        # Default means using all possilbe moves. Use 'survived' to add to this sequence's score
        play music "audio/music/Fight Song 1 (GAME VERSION).ogg"
        $ qtebase = 10
        $ qtereaction = qteath + qtetrack + qtebase
        $ qtetotal = qtereaction
        $ t_var = qtereaction
        
        show screen battle_screen
        #show screen timer_scrReaction(place="E1D5S2_SoloComplete")
        jump qte_game
        label E1D5S2_SoloComplete:
        $ E1D5S2Score = survived
        #if you score really high, you'll get a good item
        #if you score low, you'll get a mediocre item.
        if enemyHP < 0:
            $ E1D5S2_SoloWon = 1
                
        $renpy.pause(2.5)
        $ renpy.hide_screen ("battle_screen")
        scene black with fade
        play ambient "audio/ambience/Arcade.ogg" fadein 3
        play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
        $renpy.pause(1.5)
        scene bg activity arcade day with fade
        "Я выключил игру."
        $ E1D5S2Score = survived
        if (E1D5S2_SoloWon == 1):
            "Heh, still got it."

        else:
            "Хм, полагаю, хорошо, что я пришёл сюда практиковаться."

        "Выйдя из симулятора, я оглянул аркаду. Вокруг надоедливого парня все еще толпилась группа людей, который привлекал их насмешками."
        "Я достаточно практиковался сегодня, и слушать его не хотелось. Выйдя из аркады я взял байк и поехал домой."
        stop music fadeout 3.0
        stop ambient fadeout 3.0
        scene black with fade

        $renpy.pause(1.0)
        jump E1D5S7


        
hide gosunerd extra with dissolve
"Он повернулся к симулятору. Я сел и включил экран." 
stop music fadeout 3.0
stop ambient fadeout 3.0

scene black with fade
scene bg battleground night with fade
show mc mech at bl with dissolve:
    xzoom -1
show arM neu at br with dissolve
$renpy.pause(2.5)
#Game Play
play music "audio/music/Fight Song 1 (GAME VERSION).ogg" fadein 2
$ enemy = "arM"
$ mode = "default"
$ context = "E1D5S2_DuelComplete"

$ mcEnergyMax = 200
$ mcEnergy = 200
$ enemyHPMax = 150
$ enemyHP = 150

$ survived = 0
$ qtebase = 10
$ qtereaction = qteath + qtetrack + qtebase
$ qtetotal = qtereaction
$ t_var = qtereaction

$ E1D5S2Score = 0
$ E1D5S2_ArcadeMatchWon = 0
# Default means using all possilbe moves. Use 'survived' to add to this sequence's score
show screen battle_screen
#show screen timer_scrReaction(place="E1D5S2_DuelComplete")
jump qte_game
label E1D5S2_DuelComplete:
$ E1D5S2Score = survived
#If you score really high, you'll get a great item
#if you score low, you get nothing
if enemyHP < 0:
    $ E1D5S2_ArcadeMatchWon = 1
$ E1D5S2Score = survived
$renpy.pause(2.5)
$ renpy.hide_screen ("battle_screen")
scene black with fade
if (E1D5S2_ArcadeMatchWon == 1):

    play ambient "audio/ambience/Arcade.ogg" fadein 3
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 3
    $renpy.pause(1.5)
    
    scene bg activity arcade day with fade
    
    "Экран загорелся, указывая на меня, как на победителя." 
    
    show exclamation:
        xoffset 720
        yoffset 70
        xzoom .75
        yzoom .75
    show gosunerd extra at cc with dissolve
    voice "audio/voice/E1/D5/S2/GosuArcade/9.ogg"
    fk "Нет! Это не честно!" 

    menu: 
        "Мне просто повезло.": 
            "Поворачиваясь к нему я не мог сдержать усмешку." 
            pf "Полагаю, новичкам везёт." 
            hide gosunerd extra with dissolve
            "Он бормотал что-то, что я не мог разобрать, прежде чем встал и ушёл. Толпа приветствовала мою победу… {w}Или его поражение. {w}Трудно сказать что именно." 

        "Вот как выглядит чемпион.": 
            pf "Ты выглядишь как парень, которому только что надрали зад."
            "Он нахмурился и скрестил свои толстые руки на груди."
            show vein:
                xoffset 720
                yoffset 70
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D5/S2/GosuArcade/10.ogg"
            fk "Ты должно быть жульничал!" 
            pf "Когда ты так хорош, жульничество не нужно." 
            voice "audio/voice/E1/D5/S2/GosuArcade/11.ogg"
            fk "Я доложу на тебя за жульничество. Никто не может победить меня в этой игре!" 
            hide gosunerd extra with dissolve
            "Радостная толпа заглушила его нерешительную угрозу, и он с гневом ушёл. Я махал ему вслед." 
            pf "Повезёт в следующий раз!" 

        "Игра окончена.":
            "Я посмотрел на него, но ничего не сказал." 
            "Его лицо покраснело, а глаза сильно щурились. Я начал уходить, когда он остановил меня."
            voice "audio/voice/E1/D5/S2/GosuArcade/12.ogg"
            show vein:
                xoffset 720
                yoffset 70
                xzoom .75
                yzoom .75
            fk "Куда это ты идёшь? Мы ещё не закончили!"
            "Я глянул на экран \"Конца игры\"."
            pf "Нет, закончили."
            hide gosunerd extra with dissolve
            "После, я ушёл оставив его наедине с протестами."


    "Потихоньку толпа начала расходиться. Сердитого задрота нигде не было видно." 

else:

    play ambient "audio/ambience/Arcade.ogg" fadein 3
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    $renpy.pause(1.5)

    scene bg activity arcade day with fade
    
    show gosunerd extra at cc with dissolve
    "Его экран неприятно звенел, называя его победителем. {w}Он самодовольно усмехался." 
    voice "audio/voice/E1/D5/S2/GosuArcade/13.ogg"
    fk "Хммм, думаю, ты только умеешь говорить, лузер!" 

    menu: 
        "Хорошая игра.":
            pf "Хороший матч." 
            show gosunerd extra:
                xzoom -1
                easein .45 xoffset 325
            "Я предложил ему поздравительное похлопывание по плечу, но он ускользнул от меня."
            voice "audio/voice/E1/D5/S2/GosuArcade/14.ogg"
            fk "Не трогай меня, ничтожество. Твоя \"неудача\" iопределённо заразна."
            "Я всё равно похлопал его, и он резко дернулся."
            show vein:
                xoffset 1000
                yoffset 70
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D5/S2/GosuArcade/15.ogg"
            fk "Прекрати! Ты рушишь мою магию!"
            "Я пожал плечами и отошёл от симулятора."

        "Я позволил тебе победить.":
            pf "You're just lucky I went easy on you." 
            voice "audio/voice/E1/D5/S2/GosuArcade/16.ogg"
            fk "Мне не нужна удача, с моими-то умениями." 
            pf "Вот как? Давай сыграем ещё раз и посмотрим." 
            "Он противно заржал. Это напомнило мне о задыхающемся осле."
            voice "audio/voice/E1/D5/S2/GosuArcade/17.ogg"
            fk "Хаха! Ни за что! Это определённо тратой времени на нуба, вроде тебя."

        "...":
            "Я молча развернулся." 
            voice "audio/voice/E1/D5/S2/GosuArcade/18.ogg"
            fk "Полагаю, в итоге ты не так хорош." 
            "Пожав плечами я вышел из-за симулятора."
            voice "audio/voice/E1/D5/S2/GosuArcade/19.ogg"
            fk "Ну, не хочешь ничего сказать?"
            "Поняв, что я не собирался отвечать, он попробовал снова."
            voice "audio/voice/E1/D5/S2/GosuArcade/20.ogg"
            fk "Ты просто расстроен, что ты неудачник!" 
            "Этот парень слишком много говорит."

    show gosunerd extra:
        xzoom 1
        easein .45 xoffset 0
    "He glances around."
    voice "audio/voice/E1/D5/S2/GosuArcade/21.ogg"
    fk "Кто следующий?"
    "Толпа что-то тихо копошилась пока я уходил."
    hide gosunerd extra with dissolve

$renpy.pause(.5)
"Я быстро обошёл зал автоматов, но ни одна из других игр не заинтересовала меня. Выйдя, я взял байк и поехал домой."


stop music fadeout 3.0
stop ambient fadeout 3.0
scene black with fade

$renpy.pause(1.0)


jump E1D5S7
