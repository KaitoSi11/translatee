label E1D2S3:
    
    $renpy.pause(1)
    
    "Попрощавшись с Никки, я пошёл в гараж. Я не мог поверить, рассматривал возможность поездки на автобусе, когда моя малышка ждала меня здесь!"
    
    play sound "audio/sfx/Technology/Garage Door Open.ogg" fadein 1.0
    scene white with fade
    
    "Сердце билось в ожидании,пока дверь гаража открывалась и окутывала мою гордость и радость в ореол мягкого света. Слёза наворачиваются от того, как свет отражается от полированного металла."
    
    "Я нежно ласкал плавные изгибы мотоцикла. Нас надолго разлучили, но теперь мы, наконец, воссоединились. {w}Я больше никогда тебя не оставлю, обещаю."
    
    pf "{i}Хоп!{/i}"
    
    
    "Vaulting from the back of the bike, я сёл на мотоцикл и раздался мягкий глухой звук. {w}Как и всегда, удобно."
    
    "Мои руки опирались на руль. Пока я подготавливался к отъезду, у меня возникло ощущение, что я забыл что-то важное... {w}Что-то что предотвратит превращение моих мозгов в пиццу на тротуаре."
    $ E1D2S3_mcwithhelmet = 0
    menu:
        "безопасность превыше всего!":
            $ E1D2S3_mcwithhelmet = 1
            "Только дурак не наденет шлем."
            scene black with fade
            play sound "audio/sfx/Technology/Helmet HUD Power On.ogg"
            "Как только я надел шлем, зрение моментально пропало. Потом включился интерфейс, освещая мой взор кучей текста и цифр, делясь болшей информацией и приложениями, чем мне нужно."  
            
            "Я читал об оригинальных шлемах, которые только могли защитить голову. Даже представить не могу такую примитивную технологию. Теперь, даже самый стандартный шлем имеет GPS, а так же спидометр и плеер." 
    
        "Шлем - это хороший аксессуар.":
            $ E1D2S3_mcwithhelmet = 1
            Девушки и так знают, что я крут, основываясь только на мотоцикле. Но шлем, закрывающий лицо, добавляет капельку загадочности, на что девушки клюют. Они все хотят знать: \"Кто этот сексуальный парень на не менее сексуальном байке?\" И когда я сниму шлем, и ослеплю их своей улыбкой, только и останется что ловить их, когда они будут падать в обморок."
            scene black with fade
            play sound "audio/sfx/Technology/Helmet HUD Power On.ogg"
            "Как только я надел шлем, зрение моментально пропало. Потом включился интерфейс, освещая мой взор кучей текста и цифр, делясь болшей информацией и приложениями, чем мне нужно."  
    
            "Я читал об оригинальных шлемах, которые только могли защитить голову. Даже представить не могу такую примитивную технологию. Теперь, даже самый стандартный шлем имеет GPS, а так же спидометр и плеер."
    
        "Пфф, шлемы для слабаков.":
            "Да. Точняк. Как будто меня поймают за ношением этого отстоя."
    
    scene bg isokaze neighborhood day with fade
    #SFX: Bike starting up
    play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 3
    "Я повернул ключ зажигания. Рёв мотора шлёт дрожь по спине. {w}Идеально."
    play sound "audio/sfx/Vehicles/Bike Revving.ogg"
    "Я поддал газу несколько раз, наслаждаясь звуком, прежде чем выехать на улицу."
    play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 3
    $renpy.pause(1)
    play music "audio/music/Open Road (GAME VERSION).ogg" fadein 1
    #Road BG
    scene bg travel openroad day with fade
    stop ambient fadeout 5
    $renpy.pause(1)
    "Вот это жизнь. {w}Ничто не сравнится с ощущением свободы на дороге."
    
    if (E1D2S3_mcwithhelmet == 0):
        play ambient "audio/ambience/Open Road No Helmet.ogg"
        $renpy.pause(1)
        $ persistent.gpix[1][0] = 1
        scene cg mc firstride nohelmet at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        "... Количество насекомых, собранных по пути, немного рушило эффект. Но я выбрал такую жизнь. {w}Я ни о чём не жалею!"
        $renpy.pause(1)
    
    elif (E1D2S3_mcwithhelmet == 1):
        play ambient "audio/ambience/Open Road Helmet.ogg" fadein 1
        $renpy.pause(1)
        $ persistent.gpix[2][0] = 1
        scene cg mc firstride helmet at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        "Я на полную использовал возможности шлема. {w}Взглянув, я мог видеть как быстро я ехал, и как быстро ехали машины мимо меня. {w}Тут даже есть функция, которая предупредит меня об опастисти столкновения."
    
        "Динамики, встроенные в шлем, обеспечивали оптимальную акустику. {w}Некоторые могут утверждать, что это вопрос безопасности. Но у меня есть привычка держать звук на минимуме."
        $renpy.pause(1)
    
    "Трафик был на моей стороне, и я успешно ехал."
    
    scene bg campus intersection day with fade
    
    "Светофор впереди был зелёный. Идеально. Надеюсь, что продержится достаточно, чтобы я мог проехать."
    
    play sound "audio/sfx/Vehicles/Bike Accelerate.ogg"
    
    "Оставайся зелёный. Оставайся зелёный. Оставайся зелёныйОставайся зелёныйОставайся зелёныйОставайся зелёный--"
    
    "Нет! Жёлтый."
    
    "Вообще-то я был не {i}так уж{/i} и далеко. Это было бы на волоске, но я уверен что смог бы это сделать. Я сжал руль, а затем--"
    
    $ qtebase = 3
    $ qtetotal = qteath + qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E1D2S3_dontgunit")
    
    menu:
        "Тормози. Это была плохая идея.":
            label E1D2S3_dontgunit:
                $ renpy.hide_screen ("timer_scr")
                "На самом деле, было не так близко, как я думал. Не стоит рисковать."
                play sound "audio/sfx/Vehicles/Bike Screech.ogg"
                "Я сжал тормоз и потихоньку остановился на красный сигнал."
                "Несколько учеников Академии ACE пересекали улицу, и оживлённо разговаривали, проходя мимо меня. Я слегка нетерпеливо барабанил пальцами. Вскоре все студенты перешли дорогу и светофор снова загорелся зелёным."
                jump E1D2S7
    
        "ЖМИ, ЁКАРНЫЙ БАБАЙ!":
            $ renpy.hide_screen ("timer_scr")
            "Я смогу!"
    
    play sound "audio/sfx/Vehicles/Bike Accelerate.ogg"
    "Я выжал ручку газа, байк заревел с удвоенной силой."
    
    "Я прочти проехал! Ещё чуть-чуть и--"
    
    $ E1D2S3_EncounteredKaori = 1
    voice "audio/voice/E1/D2/S3/Kaori/1.ogg"
    ki "{b}Кьяяяяя~!{/b}"
    
    scene white with fade
    stop ambient fadeout 3
    stop music fadeout 3
    
    pf "{b}Воах!{/b}"
    
    play sound "audio/sfx/Vehicles/Bike Screech.ogg"
    
    "Краем глаза я заметил красные волосы. Свернув в сторону, я едва увернулся от студента. Это было близко!"
    voice "audio/voice/E1/D2/S3/Kaori/2.ogg"
    ki "{i}Oof!{/i}"
    play sound "audio/sfx/Impacts/Kaori Falling Over.ogg"

    $ persistent.gpix[21][0] = 1 
    $ persistent.gpix[22][0] = 1
    $ persistent.gpix[23][0] = 1
    $ persistent.gpix[24][0] = 1
    scene cg kaori intersection fall1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    play ambient "audio/ambience/Campus Road.ogg" fadein 1
    "Она упала на землю, а её вещи разбросало по пешеходному переходу."
    scene cg kaori intersection fall2 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    "Она щурится на меня в оцепенении."
    scene cg kaori intersection fall3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    "Но это быстро сменилось на самый страшный взгляд, который я когда-либо видел. {w}Ой-ой."
    
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
    
    menu:
        "Это моя вина. Я должен помочь ей.":
    
            if (E1D2S3_mcwithhelmet == 0):
                pf "Ты в порядке? Вот, возьми меня за руку."
    
            elif (E1D2S3_mcwithhelmet == 1):
                $ E1D2S3_mctakeshelmetoff = 1
                pf "Ты в порядке--"
    
                "Жар от её взгляда мог расплавить шлем. {w}Точно, шлем. С эттой штукой я звуку как приглушённый пришелец."
    
                "Попробуем снова."
    
                "Я снял шлем."
    
                pf "Ты в порядке? Позволь мне помочь."
    
            jump E1D2S6
    
        "Смотри по сторонам!":
            "Этот безумный {i}пешеход{/i} просто выпрыгнула из ниоткуда перед мотоциклом! Она что, смерти хочет?" 
    
            if (E1D2S3_mcwithhelmet == 1):
                $ E1D2S3_mctakeshelmetoff = 1
                "Я снял шлем." 
    
            pf "Разве тебе никто не говорил смотреть по сторонам, когда переходишь улицу?"
            
            scene cg kaori intersection fall4 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    
            "Она в шоке смотрела на меня. Погоди-ка--{w}Это злоба. Ага. Определённо злоба."
            voice "audio/voice/E1/D2/S3/Kaori/3.ogg"
            ki "Ты шутишь?! Идиот, светофор был красный!"
    
            menu:
                "Моя вина. Ты как, в порядке?":
                        "Хорошо, возможно светофор переключился на красный, когда я выехал на перекрёсток. Возможно, я был немного груб сейчас."
    
                        pf "Извини, виноват. Вот, ты в порядке?"
                        jump E1D2S6
                                
                "Я думаю, что тут кто-то дальтоник.":
                    "Я закатил глаза. Некоторые люди думают, что мир вращается вокруг них и они не могут ошибаться."
    
                    pf "Ты дальтоник? Светофор был зелёный."
                    
                    scene cg kaori intersection fall3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    
                    "Она скептически смотрела на меня."
    
                    "Я не собираюсь извиняться за то, что явно не было моей ошибкой!"
                    
                    scene cg kaori intersection fall4 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
                    voice "audio/voice/E1/D2/S3/Kaori/4.ogg"
                    ki "Ты..."
                    
                    scene bg campus intersection day with fade
    
                    "Она поднялась, отряхнула юбку, подошла ко мне и свирепо смотрела на меня."
                    
                    show kaori ang b1 at cc with dissolve
                    show vein:
                        xoffset 720
                        yoffset 110
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D2/S3/Kaori/5.ogg"
                    ki "Ты правда так туп?! Светофор был красный. КРАСНЫЙ. К-Р-А-С-Н-Ы-Й. Ты знаешь, что это значит? Это значит, что ты должен ОСТАНОВИТЬСЯ! Как у тебя вообще есть водительские права!"
    
                    "Кажется, она уверена, что свет был красным. Возможно ли, что она права? {w}… {w}Ха-ха! Я? Не прав? Иногда я превозхожу сам себя."
    
                    #honk honk
                    play sound "audio/sfx/Vehicles/A couple of honks.ogg"
                    "Я собрался раздавить ее с остроумной репликой, когда гудок автомобиля прервал меня."
                    "Ох, точно. Я все ещё на проезжей части … и позади меня большое количество машин.  {w}И светофор преключился на зелёный--видишь, я знаю как выглядит зеленый!" 
                    pf "Слушай, я бы {i}с радостью{/i} остался и поговорил, но--"
    
                    #honk honk honk
                    play sound "audio/sfx/Vehicles/More harsher honks.ogg"
    
                    "Оркестр сердитых гудков снова прервал меня."
    
                    pf "Хорошо, хорошо! Я уезжаю!"
    
                    if (E1D2S3_mcwithhelmet == 0):
                        "Я сочувствующе посмотрел на девушку и быстро уехал."
    
                    if (E1D2S3_mcwithhelmet == 1):
                        "Я сочувствующе посмотрел на девушку, прежде чем надел шлем и уехал."
                
                    show kaori ann at cc
                    "Несмотря на то, что это была ее вина, я не могу ничего поделать, кроме как посочувствовать ей. С количеством машин на дороге, собирать все её вещи - просто ад."
                    
                    $ E1D2S3_MetKaoriWasRudeNoHelmet = 1
    
                    "Ну хорошо. В любом случае, каковы шансы, что мы снова встретимся?"
                    stop music fadeout 3
                    scene black with fade
                    jump E1D2S7
                        
                        
                "Покеда.":
                    $ E1D2S3_MetKaoriWasRudeNoHelmet = 1
                    jump E1D2S3_seeya
    
        "Неее. Я сваливаю.":
            label E1D2S3_seeya:
                $ E1D2S3_MetKaoriWasRudeNoHelmet = 1
                "Да, нет. Наверное, лучше я уберусь отсюда, прежде чем всё станет таким же кислым, как её лицо."
                scene cg kaori intersection fall4 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0)
                play sound "audio/sfx/Vehicles/Bike driving off.ogg"
                "Как только светофор загорелся зелёным, я ускорился, убедившись, что дал ей досточно свободного места." 
                "Сомневаюсь, что снова на неё натолкнусь."
                if (E1D2S3_mcwithhelmet == 1) and (E1D2S3_mctakeshelmetoff == 0):
                    $ E1D2S3_MetKaoriWasRudeNoHelmet = 0
                    $ E1D2S3_MetKaoriWasRudeYesHelmet = 1
                    "Не то чтобы это было важно, потому что она не могла видеть мое лицо. Хвала богу за то, что придумали шлемы."
                stop music fadeout 3
                scene black with fade
                jump E1D2S7
    
    
    scene black with fade
    jump E1D2S4
