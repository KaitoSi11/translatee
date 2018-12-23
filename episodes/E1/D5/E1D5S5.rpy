label E1D5S5:


"Интересно, что делает Сё."
play sound "audio/sfx/Technology/Phone Dial.ogg"
"Я взял телефон и набрал его."
play sound "audio/sfx/Technology/Phone Answer.ogg"
"Через пару секунд он ответил."
voice "audio/voice/E1/D5/S5/Shou/1.ogg"
ss "Братан, что я могу для тебя сделать?"
pf "Здрарова, хочешь отдохнуть, или что-то такое?"
voice "audio/voice/E1/D5/S5/Shou/2.ogg"
ss "Ага! Я в кафе кампуса. Почему бы тебе не завалиться сюда?"
pf "Звучит как план. Выхожу."
voice "audio/voice/E1/D5/S5/Shou/3.ogg"
ss "Круто, увидимся!"
"Быстро попрощавшись, я пошёл к байку."

stop music fadeout 3.0
stop ambient fadeout 3.0
scene black with fade
$renpy.pause(.5)   

label E1D5S5_ConvergenceFromMayuCall:

play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 4
$renpy.pause(4.0)

$ shoOut = "sCasual"
$ mayOut = "sCasual"

play ambient "audio/ambience/Desert Maid Cafe.ogg" fadein 2
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5.0
scene bg campus cafe day with fade

$renpy.pause(.25)

if (E1D5S1_EventShou == 1):

    show shou smi at l2
    show mayu neu at r2
    with dissolve
    "Зайдя в кафе, я заметил как Сё махал мне из дальнего угла."
    "Подойдя ближе я удивился, каогда заметил Маю, смотревшую молча на меня."
    show mayu smi with dissolve
    "Она вежливо улыбнулась, заметив мой взгляд."
    show shou hap
    voice "audio/voice/E1/D5/S5/Shou/4.ogg"
    ss "Приятно видеть тебя, дружище."
    pf "Привет Сё, Маю. Я не знал, что вы оба тут."
    show shou cur
    "Сё удивлённо взглянул."
    voice "audio/voice/E1/D5/S5/Shou/5.ogg"
    ss "Это ведь не проблема? Маю сама хотела сюда прийти."
    "Погоди-ка--Маю пригласила его..?"
    pf "Конечно нет, но если у вас уже есть планы, то я всегда могу зависнуть с вами позже."
    show shou hap
    voice "audio/voice/E1/D5/S5/Shou/6.ogg"
    ss "Не глупи! Я пригласил тебя, так что ты должен остаться. Маю не возражает."
    "Я взглянул на неё, и она покачала головой."
    voice "audio/voice/E1/D5/S5/Mayu/1.ogg"
    ma "Нет, пожалуйста, присоединяйся."
    voice "audio/voice/E1/D5/S5/Shou/7.ogg"
    ss "Присаживайся."

    menu:
        "Я не хочу мешать им.":
            $ E1D5S1_EventShou = 0
            $ E1D5S1_EventAlone = 1
            pf "На самом деле, вы выглядите, как будто в середине чего-то, так что посидим как-нибудь потом."
            show mayu cur
            show shou neu
            voice "audio/voice/E1/D5/S5/Shou/8.ogg"
            ss "Не уходи."
            show mayu sad
            voice "audio/voice/E1/D5/S5/Mayu/2.ogg"
            ma "Пожалуйста, не уходи из-за меня."
            pf "Нет, нет, это не из-за теюя. Мне всё равно нужно было кое-что сделать. Веселитесь, хорошо? Позже как-нибудь увидимся!"
            show mayu cur
            "Сё собирался протестовать, но я вышел прежде, чем он успел."
            hide mayu
            hide shou
            with dissolve
            "Я слышал о номом симуляторе GEAR вышедшем недавно в аркаде неподалёку. Можно как раз его проверить."
            "Я вернулся к байку и поехал."
            jump E1D5S2_ArcadeConvergence

        "Сесть.":
            pf "Спасибо."
            "Я сел рядом с Сё."

elif (E1D5S1_EventMayu == 1):

    show shou smi at l2
    show mayu neu at r2
    with dissolve
    "Сё махал мне с задней части кафе, где он сидел с Маю."
    show mayu smi with dissolve
    "Заметив меня, Маю улыбнулась."
    voice "audio/voice/E1/D5/S5/Mayu/3.ogg"
    ma "Привет."
    pf "Привет Маю, Сё."
    show shou hap
    voice "audio/voice/E1/D5/S5/Shou/4.ogg"
    ss "Приятно видеть тебя, дружище!"
    voice "audio/voice/E1/D5/S5/Shou/7.ogg"
    ss "Присаживайся."
    pf "Спасибо."
    "Я сел рядом с Маю."

show shou smi
show mayu smi
"Сё протянул мне меню. Я быстро посмотрел его, и когда подошла официантка, заказал латте с зеленым чаем. Как толкьо я заказал, офицантка ушла."
pf "Что насчёт вас?"
voice "audio/voice/E1/D5/S5/Shou/9.ogg"
ss "Всё в порядке, мы уже заказали."
pf "Оо..."
voice "audio/voice/E1/D5/S5/Shou/10.ogg"
ss "Ну, как думаешь, какой ранг ты получил?"
pf "Что?"
show shou mis
voice "audio/voice/E1/D5/S5/Shou/12.ogg"
ss "С квалификации."

menu:
    "Вероятно, где-то в середине.":
        pf "Хм, Я думаю, мы попали куда-нибудь в середину."
        voice "audio/voice/E1/D5/S5/Shou/13.ogg"
        ss "Да? Почему это?"
        pf "Ну, я знаю, что, безусловно, мог бы добиться большего, если бы у меня было оружие, но мы все равно хорошо справились. Я думаю, что это усреднило всё."
        show shou hap
        voice "audio/voice/E1/D5/S5/Shou/14.ogg"
        ss "Я согласен!"

    "В десятку лучших, конечно же!":
        pf "Мы определённо будем на вершине!"
        show shou cur
        voice "audio/voice/E1/D5/S5/Shou/15.ogg"
        ss "Думаешь?"
        pf "Да! Ты видел эти ИИ? Когда мы закончили они были металлоломом."
        show shou hap
        "Сё засмеялся."

    "Где-то в низу, может в конце.":
        pf "Я не уверен... Мы могли справиться лучше."
        show shou thi
        show mayu cur
        voice "audio/voice/E1/D5/S5/Shou/16.ogg"
        ss "Я думал, мы хорошо справились."
        pf "Да, но против нас было много факторов, и я не думаю, что мы были на пике."
        show shou neu
        show mayu neu
        voice "audio/voice/E1/D5/S5/Shou/17.ogg"
        ss "Хммм."
voice "audio/voice/E1/D5/S5/Shou/18.ogg"
ss "Ну, я думаю, мы получим хороший рейтинг! Что ты думаешь, Маю?"
show mayu cur
voice "audio/voice/E1/D5/S5/Mayu/4.ogg"
ma "Мы, вероятно, будем где-то в двадцатке."
show shou hap
voice "audio/voice/E1/D5/S5/Shou/19.ogg"
ss "Это довольно хорошо!"
show mayu smi
"офицантка поставила латте. Я вдохнул аромат чая и сделал глоток. На вкус он был даже лучше, чем пахнул - идеальная смесь чая и молока."
show shou smi
voice "audio/voice/E1/D5/S5/Shou/20.ogg"
ss "Как оно?"
pf "Замечательный."
show shou mis
"Сё ухмыльнулся."
voice "audio/voice/E1/D5/S5/Shou/21.ogg"
ss "Теперь ты знаешь наш худший секрет. Это лучшее кафе в кампусе."
pf "Хужший секрет?"
show note:
    xoffset 1040
    yoffset 135
    xzoom .75
    yzoom .75
show mayu hap
voice "audio/voice/E1/D5/S5/Mayu/5.ogg"
ma "Потому что все остальные тоже знают, что это хорошее место."
show mayu smi
show shou smi
voice "audio/voice/E1/D5/S5/Shou/22.ogg"
ss "Ага!"
pf "Ох."
"Они терпеливо ждали, пока я пил."
pf "Разве вы не заказывали тоже?"
"Маю кивнула."
pf "Так где ваши напитки?"
voice "audio/voice/E1/D5/S5/Shou/23.ogg"
ss "Мы уже выпили их."
pf "То есть вы заказали и выпили свои напитки еще до того, как я приехал?"
voice "audio/voice/E1/D5/S5/Shou/24.ogg"
ss "Да."
pf "Оу."
"И снова наступило молчание. Внезапно мой чай показался очень интересным."
"Через несколкьо минут Маю встала."
voice "audio/voice/E1/D5/S5/Mayu/6.ogg"
ma "Извините, но я только что вспомнила, что мне нужно идти. Я обещала позже встретиться с отцом."
show exclamation:
    xoffset 365
    yoffset 20
    xzoom .75
    yzoom .75
show shou cur
"Сё выглядел удивлённым."
voice "audio/voice/E1/D5/S5/Shou/25.ogg"
ss "Правда? Я мне казалось ранее ты сказала, что весь день свободна."
show mayu ner with dissolve
stop music fadeout 5
voice "audio/voice/E1/D5/S5/Mayu/7.ogg"
ma "Мне жаль, я забыла об этом. Поговорим позже."
show mayu smi with dissolve
$renpy.pause(.5)
hide mayu
with dissolve
$renpy.pause(.5)
hide shou with dissolve
"Мы попрощались и она ушла."
show shou neu at cc with dissolve
play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 10
"Я продолжал потягивать напиток, пока Сё смотрел, как она уходила. Его лицо - зеркало любопытства и скептицизма. Как только она вышла за пределы слышимости, я повернулся к Сё."
pf "Маю довольно быстро выбежала…"
voice "audio/voice/E1/D5/S5/Shou/26.ogg"
ss "Ага…"
pf "Это нормально?"
show shou thi
voice "audio/voice/E1/D5/S5/Shou/27.ogg"
ss "Нет."
"Интересно, она была разочарована тем, что я пришёл и прервал их?"
pf "Ты думаешь, она ушла из-за меня?"
show shou cur
"Он удивлённо посмотрел на меня."
voice "audio/voice/E1/D5/S5/Shou/28.ogg"
ss "Почему ты об этом подумал?"
pf "Ну, не знаю. Она ушла довольно скоро после моего прихода… Что-то между вами есть?"
show shou neu
voice "audio/voice/E1/D5/S5/Shou/29.ogg"
ss "Ничего. Мы просто друзья."
pf "А она знает об этом?"
show question:
    xoffset 720
    yoffset 20
    xzoom .75
    yzoom .75
voice "audio/voice/E1/D5/S5/Shou/30.ogg"
ss "Что?"
pf "У меня такое ощущение, что у неё есть к тебе чувства…"
show shou cur
$renpy.pause(.75)
show shou hap with dissolve
$renpy.pause(.5)
"Сё подумал, а потом рассмеялся."
show shou smi
voice "audio/voice/E1/D5/S5/Shou/31.ogg"
ss "Это глупо! Я с Маю знаком много лет. Я уверен, что она видит во мне старшего брата."

if (E1D5S1_EventMayu == 1):
    pf "Значит… ты не против, если я приглашу её куда-нибудь?"
    show shou mis
    "Сё широко ухмыльнулся."
    voice "audio/voice/E1/D5/S5/Shou/32.ogg"
    ss "Правда что ли? Вам двоим было был обы здорово вместе! Маю отличная девушка."
    pf "Да, я вижу."

    menu:
        "Поговорить с Сё о чём-нибудь другом.":
            $ E1D5S5_MechConversation = 1
            jump E1D5S7_MechConvergence

        "Раз Маю уже ушла, у меня нет причин оставаться.":
            "Я допил чай."
            pf "Приятно было повидаться Сё, но мне тоже нужно идти. Нужно позаниматься с Никки."
            show shou smi
            "Он выглядел немного удивлённым, но кивнул."
            voice "audio/voice/E1/D5/S5/Shou/38.ogg"
            ss "Без проблем. Можем позависать в другое время."
            pf "Да."
            
            stop music fadeout 3.0
            stop ambient fadeout 3.0
            scene black with fade
            $renpy.pause(2.0)   
            
            "Мы оба встали и оплатили заказы, затем покинули кафе и разошлись."
            "Я провёл некоторое время в торговом центре, проверяя оборудование GEAR. Как только стало поздно, я направился домой."
            jump E1D5S7
            
elif (E1D5S1_EventShou == 1):
    menu:
        "Продолжать этот разговор.":
            pf "Как долго вы знакомы?"
            show shou smi
            voice "audio/voice/E1/D5/S5/Shou/39.ogg"
            ss "Вечность--мы выросли вместе."
            pf "Вот как."
            ss "Ага."
            pf "Вы двое очень разные. Я бы и предположить не мог, что вы такие давние друзья."
            "Сё снова засмеялся."
            show shou hap
            voice "audio/voice/E1/D5/S5/Shou/40.ogg"
            ss "Да, я это понимаю. Думаю, что мы дополняем друг друга."
            show shou smi
            voice "audio/voice/E1/D5/S5/Shou/40_1.ogg"
            ss "Мы понимаем друг друга, так как мы выдели как мы становились теми, кто мы сейчас."
            pf "И ты не думаешь, что такая связь создаёт чувства?"
            voice "audio/voice/E1/D5/S5/Shou/41.ogg"
            ss "Нет, не такие чувства."
            pf "Хм… Тогда что насчёт этого свидания в кафе?"
            show shou cur
            voice "audio/voice/E1/D5/S5/Shou/42.ogg"
            ss "Это не был свиданимем. Мы делаем это постоянно."
            pf "Делаете что?"
            show shou thi
            voice "audio/voice/E1/D5/S5/Shou/43.ogg"
            ss "Приходим за кофе, может ланчем… Иногда потом мыходим смотреть кино, или в торговый центр, или просто гуляем. Это не отличается от того, как если бы ты и я делали это."

            menu:
                "Это описание свидания.":
                    pf "Всё, что ты только расказал, выглядит как типичное свидание."
                    show shou ske
                    voice "audio/voice/E1/D5/S5/Shou/44.ogg"
                    ss "Что? Нет."
                    pf "Если бы ты хотел пойти на свидание, куда бы ты пригласил человека?"
                    show shou thi
                    voice "audio/voice/E1/D5/S5/Shou/45.ogg"
                    ss "Я бы спросил, хочет ли она посмотреть фильм, или, может быть, поужинать или выпить кофе… Всё, что я только что описал, не так ли?"
                    show shou thi
                    pf "Ага."

                "Никакого гомосексуальства.":
                    pf "Если бы я не знал ничего лучше, то думал, что ты хотел это всё тоже сделать со мной."
                    show shou hap
                    voice "audio/voice/E1/D5/S5/Shou/46.ogg"
                    ss "Почему это так плохо?"
                    pf "Прости друг, ты просто не в моём вкусе."
                    show shocked:
                        xoffset 720
                        yoffset 20
                        xzoom .75
                        yzoom .75
                    show shou sur
                    voice "audio/voice/E1/D5/S5/Shou/47.ogg"
                    ss "Что? Нет! Это не то, что я имел в виду! Я имел в виду, что было бы круто так гулять как друзья."
                    pf "Прямо как ты с Маю гуляешь как друзья?"
                    show shou cur
                    ss "Ага."
                    pf "Но делаешь все эти штучки свиданий?"
                    show shou sur
                    voice "audio/voice/E1/D5/S5/Shou/48.ogg"
                    ss "Ага--Подожди, нет!"
                    show shou thi
                    "Сё откинулся на спинку стула с задумчивым видом."

                "Это было бы совсем иначе.":
                    pf "Если бы мы сделали это вместе, это было бы свиданием."
                    show shou cur
                    voice "audio/voice/E1/D5/S5/Shou/49.ogg"
                    ss "Что? Парни не делают такое как друзья?"
                    pf "Нет, мы можем--просто не всё сразу"
                    show shou thi
                    voice "audio/voice/E1/D5/S5/Shou/50.ogg"
                    ss "... Полагаю, это было бы немного странно."
                    pf "Именно."

            show shou neu
            voice "audio/voice/E1/D5/S5/Shou/51.ogg"
            ss "Дело в том--с Маю всё по-другому."
            pf "Конечно."
            voice "audio/voice/E1/D5/S5/Shou/52.ogg"
            ss "И она знает, что мы просто друзья."
            pf "Ага-ага, и то, что она так рано ушла не имеет никакого отношения к тому, что я пришёл и разрушил ваше свидание."
            show shou cur
            voice "audio/voice/E1/D5/S5/Shou/53.ogg"
            ss "Нет, конечно нет. У неё просто дела с отцом."
            pf "Точно."
            show shou smi
            "Он безнадёжен."

        "Поговорить очём-нибудь другом.":
            $ E1D5S5_MechConversation = 1
            "Я не уверен, но не хочу влезать в это."
            jump E1D5S7_MechConvergence

            
            
label E1D5S7_MechConvergence:
if (E1D5S5_MechConversation == 1):
    pf "Как твой GEAR после квалификации? Очевидно мой видал лучшие дни."
    show shou mis
    voice "audio/voice/E1/D5/S5/Shou/33.ogg"
    ss "Она держится."
    pf "Хорошо, должен спросить--почему ты относишься к своему GEAR как к \"ней\"?"
    show shou smi
    voice "audio/voice/E1/D5/S5/Shou/34.ogg"
    ss "Ну, ты знаешь как люди обращаются к своей машине, или лодке как к \"ней\"? Так вот, Изумруд, моя лодка."
    pf "Хорошо, тогда почему у неё не женский каркас?"
    voice "audio/voice/E1/D5/S5/Shou/35.ogg"
    ss "Потому что это я."
    pf "Что?"
    show shou cur
    voice "audio/voice/E1/D5/S5/Shou/36.ogg"
    ss "Ты знаешь--GEAR является воплощением пилота."
    pf "Да, я знаю это. Но если у твоего GEAR женская сущность… И GEAR - воплощение пилота… тогда ты--"
    show shou mis
    voice "audio/voice/E1/D5/S5/Shou/37.ogg"
    ss "Я вижу, куда ты клонишь, и я собираюсь остановить тебы прямо тут, потому что это не так. Как сосуд, я называю ее женщиной, но эстетика, рама и все такое - это мое отражение."
    pf "Ох… Точно."
    show shou hap
    "Я кивнул, но не был все ещё уверен, что понял до конца."

show shou smi
"Когда разговор подходил к концу, я сделал еще один глоток из того, что с удивлением оказалось пустой чашкой."
voice "audio/voice/E1/D5/S5/Shou/54.ogg"
ss "Ты закончил с этим?"
pf "Видимо да."
voice "audio/voice/E1/D5/S5/Shou/55.ogg"
ss "Хочешь ещё одну?"
pf "Нет, мне хватит, спасибо."

menu:
    "Пойти домой.":
        pf "Что ж, было приятно повидаться, но мне пора уходить."
        "Он кивнул."
        show shou hap
        voice "audio/voice/E1/D5/S5/Shou/56.ogg"
        ss "Ага, можем в другой раз собраться."
        show shou smi
        pf "Да."
        
        stop music fadeout 3.0
        stop ambient fadeout 3.0
        scene black with fade
        $renpy.pause(2.0)           

        "Мы оба встали и оплатили заказы, затем покинули кафе и разошлись."
        "Я провёл некоторое время в торговом центре, проверяя оборудование GEAR. Как только стало поздно, я направился домой."
        jump E1D5S7

    "Погнали в аркаду.":
        pf "У тебя ещё есть дела?"
        show shou cur
        voice "audio/voice/E1/D5/S5/Shou/57.ogg"
        ss "Ничего, что бы я знал."
        pf "Я думаю пойти в аркаду потренироваться. Мы могли бы сыграть пару раундов."
        show shou hap
        voice "audio/voice/E1/D5/S5/Shou/58.ogg"
        ss "Звучит неплохо!"
        pf "Я знаю только тот, что рядом с моим домом. Тут поблизости есть какой-нибудь?"
        show shou smi
        voice "audio/voice/E1/D5/S5/Shou/59.ogg"
        ss "Да, есть одна рядом. Я отведу тебя туда."
        pf "Круто."
        
        stop music fadeout 3.0
        stop ambient fadeout 3.0
        scene black with fade
        $renpy.pause(2.0)   
        
        "Мы оплатили наши заказы, и Сё показал мне путь к аркаде. Мы играли симуляционные матчи GEAR допоздна. Потом мы попрощались и разошлись по домам."
        jump E1D5S7

