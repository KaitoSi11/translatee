label E1D5S4:
stop music fadeout 3.0

if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S3_MetKaoriWasNice == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
    $renpy.pause(1.5)
    play sound "audio/sfx/Technology/Phone Vibration Once.ogg" 
    $renpy.pause(1.5)
    "Дойдя до телефона, громкий звонок поразил меня. Звонила Каори."
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    "... Это странно."
    pf "Привет Каори. Я как раз собирался звонить--"
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E1/D5/S4/Kaori/1.ogg"
    ki "Ты сломал мой планшет!" 
    pf "Э-эм, что?"
    voice "audio/voice/E1/D5/S4/Kaori/2.ogg"
    ki "Ты сломал мой планшет, так что должен мне новый." 

    menu: 
        "Когда я это сделал?":
            pf "Когда я вообще был у твоего планшета?"
            voice "audio/voice/E1/D5/S4/Kaori/3.ogg"
            ki "Когда ты чуть не сбил меня нв своём байке."
            "Я превался."
            pf "Оууу…"
            voice "audio/voice/E1/D5/S4/Kaori/4.ogg"
            ki "Именно. В любом случае, он сломан из-за тебя."

        "Я не дарю подарки до второго или третьего свидания.":
            pf "По крайней мере, подожди, пока мы не сходим на свидание, прежде чем начать просить подарки."
            voice "audio/voice/E1/D5/S4/Kaori/5.ogg"
            ki "Это не подарок, если ты причина, по которой мне нужна замена!"
            pf "Ты хочешь, чтобы я купил его, не так ли?"
            voice "audio/voice/E1/D5/S4/Kaori/6.ogg"
            ki "Конечно! Ты сломал его!"
            pf "По мне, звучит как подарок."
            voice "audio/voice/E1/D5/S4/Kaori/7.ogg"
            ki "Это не так!"
            pf "Эй, я понял--"
            voice "audio/voice/E1/D5/S4/Kaori/8.ogg"
            ki "У меня нет времени на это. Ты должен мне замену."

        "Я никогда не был рядом с твоим планшетом.":
            pf "Нет, я не делал этого."
            voice "audio/voice/E1/D5/S4/Kaori/9.ogg"
            ki "Да, ты делал!"
            pf "Как я вообще мог его сломать, если даже никогда им не пользовался?"
            voice "audio/voice/E1/D5/S4/Kaori/10.ogg"
            ki "Когда ты чуть не убил меня, ты ,вообще-то, вместо этого убил мой планшет."
            pf "Что?"
            voice "audio/voice/E1/D5/S4/Kaori/11.ogg"
            ki "Ты разбил экран, когда моя сумка упала на тротуар, теперь он даже не включается."
            pf "Это всё ещё звучит как {i}твоя{/i} проблема."
            "На секунду ярость Каори поутихла."
            voice "audio/voice/E1/D5/S4/Kaori/12.ogg"
            ki "{i}Моя{/i} проблема? Идиот! {i}Ты{/i} проехал на красный. {i}Ты{/i} чуть не сбил меня. И {i}из-за тебя{/i} моя сумка--должна добавить,сумка с важными вещами--полетела по тротуару, разбив эти самые ценные вещи. И если бы не ты, я--"
            pf "Боже, {i}снова{/i} это? Что заставит тебя заткнуться насчёт этого?"
            voice "audio/voice/E1/D5/S4/Kaori/13.ogg"
            ki "Планшет."

    pf "Хорошо."
    pf "Какой планшет у тебя был? Я заменю его тем же. Разницы не заметишь." 
    voice "audio/voice/E1/D5/S4/Kaori/14.ogg"
    ki "У меня был EN85…"
    pf "Нет, правда, какой у тебя был?"
    voice "audio/voice/E1/D5/S4/Kaori/15.ogg"
    ki "Именно такой и был!"
    pf "Я думал, у тебя будет модель новее."
    voice "audio/voice/E1/D5/S4/Kaori/16.ogg"
    ki "Почему? Он хорошо работал, пока ты не сломал его."
    pf "Ну, хорошо. Как долго он у тебя был?"
    voice "audio/voice/E1/D5/S4/Kaori/17.ogg"
    ki "Два года."
    pf "Это довольно долго… Сколько стоит замена?"
    voice "audio/voice/E1/D5/S4/Kaori/18.ogg"
    ki "399.99 кредитов, плюч налог."
    pf "399.99 кредитов?{w} {i}Плюс{/i} налог?!"
    voice "audio/voice/E1/D5/S4/Kaori/19.ogg"
    ki "Он столько стоит."
    pf "Он б/у. Ты знаешь, что такое амортизация? Я жам тебе 150 кредитов, и это щедро."
    voice "audio/voice/E1/D5/S4/Kaori/20.ogg"
    ki "Что?! Это даже не близко к тому, сколько я за него заплатила!"
    pf "Конечно нет, Эт остарая модель, но сейчас бы она стоила именно столько."
    voice "audio/voice/E1/D5/S4/Kaori/21.ogg"
    ki "Я заплатила вдвое больше этого, когда покупала, так что вот сколько он стоит."
    pf "Это не так работает."
    voice "audio/voice/E1/D5/S4/Kaori/22.ogg"
    ki "Это так работает для меня!"
    pf "Может я достану тебе б/у модель."
    voice "audio/voice/E1/D5/S4/Kaori/23.ogg"
    ki "Нет! Люди не забоятся о своих вещах. Зная тебя, ты купишь мне немиправный планшет, и его придётся сразу же заменить."
    pf "Я умею выбирать электронику. Я не настолько туп, чтобы купить тебе сломанный."
    voice "audio/voice/E1/D5/S4/Kaori/24.ogg"
    ki "Сомнительно."
    "Она очень усложняет это." 
    pf "Слушай, я не собираюсь платить изначальную цену, {i}и налог{/i}, или что-то, если он уже не стоит этого." 
    voice "audio/voice/E1/D5/S4/Kaori/25.ogg"
    ki "Хорошо, но ты должен по крайней мере принести мне что-то сопоставимое с моим старым--например YX140." 

else:
    "Хмм, Каори никогда не отправляла информацию о стратегиях, которые она хотела, чтобы я изучил до нашей встречи в понедельник. {w}В какое время эта встреча? Лучше спрошу её."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    "Я взял телефон и набрал её."
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    "Прошло несколько гудков, прежде чем Каори подняла трубку." 
    voice "audio/voice/E1/D5/S4/Kaori/26.ogg"
    ki "Алло?" 
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    pf "Привет, Каори, это [pfirst]." 
    voice "audio/voice/E1/D5/S4/Kaori/27.ogg"
    ki "О, привет." 
    pf "Слушай, ты не отправляла мне стратегии для изучения." 
    voice "audio/voice/E1/D5/S4/Kaori/28.ogg"
    ki "Конечно я посылала их. Ещё раз проверь свою почту."
    "Я пролистал почту, и как ожидалось, не видел ничего от Каори."
    pf "Ну, там ничего нет, так что я не знаю кому ты отправляла."
    voice "audio/voice/E1/D5/S4/Kaori/29.ogg"
    ki "Разве это не твоя почта?"
    "Она написала неправильный адрес."
    pf "Нет, в моём нет \"7\"."
    voice "audio/voice/E1/D5/S4/Kaori/30.ogg"
    ki "Ух, идиот! Почему ты дал мне неправильный email?"
    pf "Я не давал тебе неправильный--"
    voice "audio/voice/E1/D5/S4/Kaori/31.ogg"
    ki "Подожди, я пошлю снова."
    "Я слышал шум на другом конце телефона и что-то похожее на разочарованный стон." 
    voice "audio/voice/E1/D5/S4/Kaori/32.ogg"
    ki "Тьфу, планшет все ещё не работает, так что придётся взять ноутбук. Подожди."
     
    if (E1D2S3_EncounteredKaori == 0):
        menu: 
            "Что ты с ним сделала?":
                pf "Что с твоим планшетом?" 
                voice "audio/voice/E1/D5/S4/Kaori/33.ogg"
                ki "Не знаю. Ч ним была какая-то хрень, а со вчерашнего дня он вообще не включается." 
                pf "Отстой." 
                voice "audio/voice/E1/D5/S4/Kaori/34.ogg"
                ki "Мне это так надоело. Я потом пойду в торговый центр, чтобы купить YX140."

            "Похоже, тебе нужен мужчина, чтобы починить его.":
                pf "Я могу прийти и починить его для тебя." 
                voice "audio/voice/E1/D5/S4/Kaori/35.ogg"
                ki "Ты не сможешь починить. Он полностью мёртв." 
                pf "Я могу, у меня очень умелые руки…" 
                voice "audio/voice/E1/D5/S4/Kaori/36.ogg"
                ki "Достаточно умелые, чтобы вернуть его к жизни?" 
                pf "Достаточно умелые, чтобы заставить тебя забыть о поломке." 
                voice "audio/voice/E1/D5/S4/Kaori/37.ogg"
                ki "Что? Плевать--Я просто пойду в торговый центр, и куплю YX140." 

            "Я все ещё не получил сообшение…":  
                pf "Ты уже переслала сообшение?" 
                voice "audio/voice/E1/D5/S4/Kaori/38.ogg"
                ki "Нет, мой компьютер медленно работает. Вот почему я всегда использовала планшет." 
                pf "Так купи новый." 
                voice "audio/voice/E1/D5/S4/Kaori/39.ogg"
                ki "Как будто я не думала об этом! Я сегодня пойду в торговый центр, чтобы купить YX140."

    if (E1D2S3_MetKaoriWasRudeYesHelmet == 1):
        pf "Что случилось? Ты сломала его?" 
        voice "audio/voice/E1/D5/S4/Kaori/40.ogg"
        ki "Нет, {i}Я{/i} я не ломала его." 
        pf "Кто-то другой сделал это?" 
        voice "audio/voice/E1/D5/S4/Kaori/41.ogg"
        ki "Какой-то идиот сбил меня в первый день занятий, и с тех пор он не работает!"
        "Упс…" 
        pf "Ого, что за придурок!" 
        voice "audio/voice/E1/D5/S4/Kaori/42.ogg"
        ki "Я знаю! Я пойду в торговый центр, чтобы купить YX140, но я желала бы знать, кто это был, чтобы заставить его купить новый."
            
pf "Что насчёт Z90? У него лучше характеристики, и он дешевле." 
voice "audio/voice/E1/D5/S4/Kaori/43.ogg"
ki "Нет, это не так! YX140 заменил EN85. У него больше GB, чем у Z90, и лучше связь."
pf "О чём ты говоришь? Все совместимо, и ты можешь получить его с большим GB. Кроме того, Z90 сделан Macrohard, который лучше, чем Pineapple." 
voice "audio/voice/E1/D5/S4/Kaori/44.ogg"
ki "Ты шутишь? Pineapple лучше. Он работает быстрее и не получает вирусов, поэтому имеет лучший срок годности."
pf "Это шутка? Встретимся в магазине. Я покажу, что Z90 так же хорош--если не лучше--чем YX140. Если после этого ты все еще не поверишь мне, я уступлю." 
voice "audio/voice/E1/D5/S4/Kaori/45.ogg"
ki "Хорошо, ео только потому, что я знаю, что ты не прав! Встретимся там через полчаса." 
"Разговор прекратился без лишних слов. {w}Ага, и тебе пока! {w}Я взял куртку и пошёл." 


stop ambient fadeout 3.0
stop music fadeout 3.0
scene black with fade
$renpy.pause(1.5)
play ambient "audio/ambience/Mall.ogg" fadein 3
scene bg mall main day with fade

$renpy.pause(1.0)


"Я пришёл в торговый зал до Каори и ждал у южного входа."
"Через несколько минут я увидел её, идущей в худи и джинсах. Странно видеть её без формы." 

$ kaoOut = "sCasual"
$ kaoHairF = "long"
$ kaoHairB = "long"

show kaori neu at cc with dissolve

menu: 
    "Хорошо выглядишь.":
        play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 2
        pf "Мне нравится твой наряд."
        show kaori dis
        voice "audio/voice/E1/D5/S4/Kaori/46.ogg"
        ki "Почему? Ничего особенного."
        pf "Просто приятно видеть, что ты любишь носить."
        show kaori thi
        voice "audio/voice/E1/D5/S4/Kaori/47.ogg"
        ki "Я-Я полагаю…"

    "Ты на все свидания ходишь в худи?": 
        play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 2
        pf "Немного посредственно для свидания, но я не против."
        show vein:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori dis 
        voice "audio/voice/E1/D5/S4/Kaori/48.ogg"
        ki "Это не свидание!"
        pf "Не пойми меня неправильно, я не возражаю! Ты все ещё хорошо выглядишь."
        show kaori ann with dissolve
        voice "audio/voice/E1/D5/S4/Kaori/49.ogg"
        ki "Заткнись! Я не одеваюсь так на свидания."
        pf "А как ты одеваешься на свидания?"
        show tsuBlush:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori dis b1 with dissolve
        voice "audio/voice/E1/D5/S4/Kaori/50.ogg"
        ki "Э-Это не важно!"

    "Во что ты одета?!": 
        play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 2
        pf "Из всего своего гардероба ты выбрала это?" 
        show kaori dis
        voice "audio/voice/E1/D5/S4/Kaori/51.ogg"
        ki "Что это значит?" 
        pf "Что ты могла бы выглядеть лучше."
        show kaori ann
        voice "audio/voice/E1/D5/S4/Kaori/52.ogg"
        ki "Что не так с тем, как я сейчас выгляжу?" 
        pf "Как быдто ты даже не старалась." 
        "Каори стиснула челюсть." 
        show vein:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D5/S4/Kaori/53.ogg"
        ki "Я не для тебя одеваюсь. А для себя."

    "Ничего не говорить.":
        play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 2
        "Кого волнует, как она одета? На мне так же нет формы. Воскресенье же."

show kaori neu with dissolve
voice "audio/voice/E1/D5/S4/Kaori/54.ogg"
ki "Пойдём внутрь." 
pf "Ты босс!" 

stop ambient fadeout 3.0
scene black with fade
$renpy.pause(1.5)
play ambient "audio/ambience/Electronics Store.ogg" fadein 3
scene bg store electronics day with fade

$renpy.pause(1.0)

"Я следовал за Каори в магазин электроники."


"Она направилась сразу к планшетам и показала на XY140."

show kaori neu at cc with dissolve
voice "audio/voice/E1/D5/S4/Kaori/55.ogg"
ki "Вот он." 
pf "А здесь мой." 
"Я показал на Z90 и прочитал описание." 
pf "Оптический дисплей с Hexa-HD разрешением 750 ppi, чипом V9Z и 256-битной архитектурой. У него даже есть антиотражающее покрытие на экране. Вы должны признать, что это удивительный планшет. А также…" 
"Я показал на XY140."
pf "... Он дешевле." 
"Каори скрестила руки." 
show kaori ske with dissolve
voice "audio/voice/E1/D5/S4/Kaori/56.ogg"
ki "И? XY140 стоит немного дороже, потому что ты получаешь больше. Смотри, он содержит в три раза больше файлов, и, хотя дисплеи совпадают, XY140 обладает потрясающей стабилизацией видео и встроенными опциями подключения к данным." 

if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S3_MetKaoriWasNice == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
    pf "Всё, что ты сказала, не заставило меня поверить, что это стоит больших денег." 
    show kaori ann
    voice "audio/voice/E1/D5/S4/Kaori/57.ogg"
    ki "Не могу поверить, что ты хочешь купить мне модель хуже, чтобы {i}компенсировать{/i} мои разбитые вещи." 
    pf "Он не хуже! Это отличный планшет." 
    voice "audio/voice/E1/D5/S4/Kaori/58.ogg"
    ki "Но не сравним с моим E85." 
    pf "Почему ты такая упрямая?" 
    show kaori dis
    voice "audio/voice/E1/D5/S4/Kaori/59.ogg"
    ki "Почему тееб нужно было ломать мой планшет?"
    pf "Ты убиваешь меня."
    voice "audio/voice/E1/D5/S4/Kaori/60.ogg"
    ki "Так тебе и надо, за попытку убить меня."

else:
    pf "Z90 все ещё лучше." 
    show kaori ann
    voice "audio/voice/E1/D5/S4/Kaori/61.ogg"
    ki "Нет, и так как это мой планшет, я возьму XY140."
    pf "Ты невозможна." 
    show kaori dis
    voice "audio/voice/E1/D5/S4/Kaori/62.ogg"
    ki "А ты все ещё не прав."

stop music fadeout 1.0
voice "audio/voice/E1/D5/S4/GosuElectronics/1.ogg"
rn "Просто, чтобы вы знали, вы {i}оба{/i} не правы." 
show exclamation:
    xoffset 720
    yoffset 110
    xzoom .75
    yzoom .75
show kaori cur with dissolve
$renpy.pause(.5)
"Каори и я развернулись."

hide kaori with dissolve


show gosunerd extra at l2 with dissolve:
    xzoom -1

show kaori cur at r3 with dissolve
    
"Позади нас стоял коротышка в круглых очках. Он встал мжду нами и взял другую модель с полки." 
play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
voice "audio/voice/E1/D5/S4/GosuElectronics/2.ogg"
rn "Это IB760 от Bensang. У него самый быстрый на рынке процессор с векторным ядром на частоте 6,00 ГГц, технологиями redtooth, и датчик отпечатков пальцев на экране. Не говоря уже о превосходном разрешении с передовой технологией Multi-Touch." 
"Он потянулся и взял что-то ещё."
voice "audio/voice/E1/D5/S4/GosuElectronics/3.ogg"
rn "К тому же, он идёт со встроенным чехлом, так что не придётся тратиться на дополнительные аксессуары." 

show gosunerd extra:
    xzoom 1

"Он взглянул на Каори." 
voice "audio/voice/E1/D5/S4/GosuElectronics/4.ogg"
rn "Что, из того, что я слышал, вы могли бы действительно использовать." 
"Я обменялся с Каори взглядом." 

show kaori dis

voice "audio/voice/E1/D5/S4/Kaori/63.ogg"
ki "Никто не спрашивал твоего мнения." 
voice "audio/voice/E1/D5/S4/GosuElectronics/5.ogg"
rn "Очевидно тебе нужно это, раз ты рассматриваешь XY140 как какой-то сорт технологическх плебеев."
show kaori ang
show vein:
    xoffset 1175
    yoffset 110
    xzoom .75
    yzoom .75
voice "audio/voice/E1/D5/S4/Kaori/64.ogg"
ki "Чего тебе--!"
show kaori ann
pf "Об этом я тебе и говорил! Говорил же, что XY140 не так хорош."

show gosunerd extra:
    xzoom -1

voice "audio/voice/E1/D5/S4/GosuElectronics/6.ogg"
rn "Воу, успокойтесь \"Мистер Всемогущий\", Z90 более {i}худший{/i} выбор!"
pf "Что?"
voice "audio/voice/E1/D5/S4/GosuElectronics/7.ogg"
rn "Кто захочет использовать машину, построенную на операционной системе Frame? Последний раз, когда этот кусок барахла работал, был Frame XP!"
pf "Frame 7 был хорош!"
"Он громко хихмкал."
voice "audio/voice/E1/D5/S4/GosuElectronics/8.ogg"
rn "Как мило. Не удивительно, что вы вместе, у вас обоих вкус к плохим планшетам."

show kaori sur b1 with dissolve
voice "audio/voice/E1/D5/S4/Kaori/65.ogg"
ki "Вместе?!"

show kaori ang b1:
    xzoom -1
    easein .5 xoffset -150
    
$renpy.pause(.15)
    
show gosunerd extra:
    xzoom 1
    easein .33 xoffset -70

$renpy.pause(.5)
"Каори топнула ногой вперед, ее руки сжались в кулаки. Ботаник был явно потрясен, но старался сохранять спокойствие."
voice "audio/voice/E1/D5/S4/Kaori/66.ogg"
ki "Ты понятия не имеешь, о чём говоришь!"
show kaori ann b1
pf "Без шуток! Macrohard имеет весь бизнес-рынок."
voice "audio/voice/E1/D5/S4/Kaori/67.ogg"
ki "И Pineapple делает премиальные, передовые устройства!"
pf "Так же, сейчас все модели поставляются со встроенным Redtooth 3.0!"
voice "audio/voice/E1/D5/S4/Kaori/68.ogg"
ki "И с датчиками отпечатков пальцев, и улучшенной технологией Multi-Touch!"
"Он открыл рот, чтобы что-то сказать, но Каори перебила его." 
show kaori ang b1 with dissolve
voice "audio/voice/E1/D5/S4/Kaori/69.ogg"
ki "И мы не всместе!"
show kaori dis b1 with dissolve
pf "Ага, иди занимайся своими делами!"
voice "audio/voice/E1/D5/S4/GosuElectronics/9.ogg"
rn "Вы нубы! Ваш взор слишком затуманен, чтобы видеть свет! Иначе, вы бы поняли, что у Andzoid лучшее оборудование, программное обеспечение, {i}и{/i} он стоит ваших денег!"

hide gosunerd extra with dissolve
$renpy.pause(.5)

"Прежде чем кто-либо из нас успел что-то сказать, он развернулся и уверенно ушёл. Кажется, в его руке материализовались сырные хлопья."
hide kaori with dissolve
show vein:
    xoffset 720
    yoffset 110
    xzoom .75
    yzoom .75
show kaori ann at cc with dissolve
$renpy.pause(.5)
voice "audio/voice/E1/D5/S4/Kaori/70.ogg"
ki "Идиот! Суёт свой нос куда не следует." 
pf "Я знаю, да?"
$renpy.pause(.5)
show kaori thi with dissolve
stop music fadeout 3.0
"Мы замолкли, когда я посмотрел на демонстрационную модель IB760."

$renpy.pause(1.0)
"..."
pf "Вообще-то, Каори…"
show kaori neu
voice "audio/voice/E1/D5/S4/Kaori/71.ogg"
ki "Что?" 
pf "Я полагаю, он в чём-то прав." 
voice "audio/voice/E1/D5/S4/Kaori/72.ogg"
ki "Дай я посмотрю." 
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
"Мы оба посмотрели \"характеристики\" планшета."
show kaori cur
voice "audio/voice/E1/D5/S4/Kaori/73.ogg"
ki "Хм, функции тут определенно перевешивают XY140…" 
pf "И аппаратно он выкидывает Z90 из гонки."
"Я наблюдал, как Каори проводила пальцем по экрану планшета и подправляла настройки и конфигурацию. Мгновение спустя она взяла коробку IB760 с полки и осмотрела её."
pf "Так... Значит, ты хочешь этот?" 
show kaori neu
voice "audio/voice/E1/D5/S4/Kaori/74.ogg"
ki "Как бы мне не хотелось это признавать, это имеет смысл."
pf "Только не позволь {i}ему{/i} услышать это."

if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S3_MetKaoriWasNice == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
    hide kaori with dissolve
    "Я взял у неё планшет и пошёл к кассе." 
    pf "Рад, что мы разобрались с этим." 
    show kaori neu at l3 with dissolve
    "Когда я собирался заплатить, Каори отпихнула меня от кассы и достала свой кошелек."
    pf "Что?" 
    voice "audio/voice/E1/D5/S4/Kaori/75.ogg"
    ki "Как бы то ни было, мне не нужно, чтобы ты заплатил за это."

    menu:
        "Мне все ещё нужно взять ответственность.":
            "Я покачал головой."
            pf "Нет, но это все ещё моя вина, что тебе нужен новый планшет."
            show kaori sur with dissolve
            "Прежде чем она успела ответить, Я приложил свою карту. \"Подтверждено\"! появилось на дисплее."
            show kaori ske
            show exclamation:
                xoffset 230
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D5/S4/Kaori/76.ogg"
            ki "Т-Ты идиот! Я просто позволила тебе сорваться с крючка, и ты все равно заплатил…"
            "Я улыбнулся ей."
            pf "Ох, ну уже слишком поздно."
            show kaori cur b1 with dissolve
            "Каори казалась взволнованной. Я протянул ей сумку."
            pf "Вот."
            show kaori neu b1
            "Несколько секунд она смотрела на сумку, прежде чем неохотно взяла её. Я рад, что после всего этого испытания выбора планшена, она не будет сопротивляться. Поалгаю, она понимала, что мы оба одинаково упрямы."
            voice "audio/voice/E1/D5/S4/Kaori/77.ogg"
            ki "... Спасибо."

        "Не буду спорить с этим!":
            pf "Сильная, независимая женщина, которой не нужен мужчина! Мне нравится."
            show kaori dis
            voice "audio/voice/E1/D5/S4/Kaori/78.ogg"
            ki "Ух ты, я пытаюсь сделать что-то хорошее, а ты все еще продолжаешь быть полным придурком."
            pf "Что? Эт оне был сарказм!"
            show kaori ann
            "Она посмотрела на меня, потом заплатила за планшет и взяла сумку."

        "Я частично заплачу.":
            pf "Позволь оплатить половину. Ты хоть и получаешь новый планшет, но я виноват, что тебе приходится делать это раньше, чем позже."
            show kaori thi
            "Она обдумывала это."
            pf "По крайней мере мы сможем нахвать это разрешённой ситуацией."
            show kaori neu
            voice "audio/voice/E1/D5/S4/Kaori/79.ogg"
            ki "Хорошо."
            "Кассир выставил счет, и мы оба оплатили картами. После этого Каори взяла сумку."
            voice "audio/voice/E1/D5/S4/Kaori/80.ogg"
            ki "Спасибо, полагаю."
            pf "Без проблем."

else:
    hide kaori with dissolve
    "Она взяла планшет и пошла к кассе." 
    show kaori neu at l3 with dissolve
    
    pf "Рад, что мы разобрались с этим."
    voice "audio/voice/E1/D5/S4/Kaori/81.ogg"
    ki "Я тоже."
    "Каори достала кошелёк и заплатила."

"Мы вышли из магазина."
    
stop ambient fadeout 3.0
scene black with fade
$renpy.pause(1.5)
play ambient "audio/ambience/Mall.ogg" fadein 3
scene bg mall main day with fade

$renpy.pause(1.0)

show kaori neu at cc with dissolve
$renpy.pause(.25)

"На улице Каори повернулась ко мне."
show kaori thi at cc with dissolve
$renpy.pause(.5)
voice "audio/voice/E1/D5/S4/Kaori/82.ogg"
ki "Спасибо, что пришёл, полагаю… Я имею в виду, кое-что, что ты говорил было полезно, но в основном ты доставлял головную боль."
"Я ухмыльнулся ей."
pf "Ты действительно плоха в комплиментах."
show tsuBlush:
    xoffset 720
    yoffset 110
    xzoom .75
    yzoom .75
show kaori ann b1 with dissolve
voice "audio/voice/E1/D5/S4/Kaori/83.ogg"
ki "Это не был комплимент!"
"Но я заметил румянец, подкрадывающийся к ее щекам."
pf "Во всяком случае, не беспокойся об этом. Мы команда, а значит, что мы заботимся друг о друге, верно?"
show kaori neu b1
voice "audio/voice/E1/D5/S4/Kaori/84.ogg"
ki "Да, вот как мы смогли победить того неудачника, когда он пришел."
pf "Ха! Ты видела, как он раздражённо ушёл?"
show kaori mis b1
voice "audio/voice/E1/D5/S4/Kaori/85.ogg"
ki "Может быть, это научит его перестать бодаться там, где не нужно."
"Я засмеялся, и показалось, что Каори улыбнулась."

if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S3_MetKaoriWasNice == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
    pf "Так, всё хорошо?"
    show kaori neu at cc with dissolve
    voice "audio/voice/E1/D5/S4/Kaori/86.ogg"
    ki "Что?"
    pf "Ты знаешь--насчёт всего этой ситуации, когда я чуть не сбил тебя."
    show kaori cur
    voice "audio/voice/E1/D5/S4/Kaori/87.ogg"
    ki "Ох."
    "Она посмотрела на свою сумку и кивнула."
    show kaori neu
    voice "audio/voice/E1/D5/S4/Kaori/88.ogg"
    ki "Ага, всё хорошо."
    pf "Круто, потому что я не хотел начинать дружбу на плохой ноте."
    "Она моргнула при упоминании \"дружбы\" и отмахнулась от этого."

else:
    pf "По крайней мере ты сможешь послать стратегии."
    show kaori neu with dissolve
    voice "audio/voice/E1/D5/S4/Kaori/89.ogg"
    ki "Хех, да. Я отправлю их, когда настрою его."
    pf "Тебе нужен совет, как это сделать?"
    "Она положила руку на бок."
    show kaori dis
    voice "audio/voice/E1/D5/S4/Kaori/90.ogg"
    ki "Нет."
    "Я убылнулся на её суровое выражение."
    pf "Я пошутил, Каори. Это то, что делают друзья. Они шутят друг с другос."
    show kaori neu with dissolve
    "Она моргнула при упоминании \"друзей\" и хмурый взгляд исчез."

show kaori neu
voice "audio/voice/E1/D5/S4/Kaori/91.ogg"
ki "Как бы то ни было, я лучше пойду. Увидимся в понедельник."
pf "Ага, увидимся."
hide kaori with dissolve
"Кивнув, она развернулась и исчезла в толпе людей."



stop music fadeout 3.0
stop ambient fadeout 3.0
scene black with fade
"Я пошёл в противоположном направлении к магазину оборудования GEAR, который хотел проверить."
"Как только стало поздно, я пошёл домой."

        
        
$renpy.pause(2.0)   



jump E1D5S7
