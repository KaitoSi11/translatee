label E1D3S1:
    
    
    $renpy.pause(1)
    #morning sounds
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1)
    #black background fade in/out 
    scene bg homekaito myroom blurry with Dissolve(2.5)
    "Солнце светило в лицо через шторы."
    scene black with fade
    "Я перевернулся, пытаясь заставить себя снова уснуть. Но чем больше я пытался вернуться ко сну, тем более бодрым становился."
    $renpy.pause(1)
    "Который час?"
    scene bg homekaito myroom blurry with fade
    "На часах \"6:30\". У меня все ещё было полчаса до будильника. {w}Я должен поспать."
    scene black with fade
    "Я зарылся глубже в одеяло, но вскоре мне стало скучно. Всегда когда я естественным образом просыпаюсь так рано, это когда у меня джетлаг. Не уверен, благословение это, или проклятие. {w}Полагаю, можно начать собираться."
    scene bg homekaito myroom day with fade
    "Я быстро одел форму и спустился вниз…"
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
    scene black with fade
    $renpy.pause(3)
    #bg change
    scene bg homekaito main day with fade
    "... На пустую кухню."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    "Странно быть первым. Обычно, в это время Никки занималась своими делами на кухне."
    "Почитаю что-нибудь, пока жду ее.  Все равно она должна скоро спуститься."
    play sound "audio/sfx/Technology/Payment Beep Success.ogg"
    "Я открыл новостное приложение на телефоне. На главной странице не было ничего интересного... {w}пока я не нашёл статью об Aludian Enterprises."
    
    "{i}Aludian Enterprises официально объявила о своих намерениях спонсировать перспективную команду на предстоящих \"Военных играх\". {w}Быстро развивающаяся компания, занимающаяся исследованиями и разработками, привлекла большое внимание в области cenorobotics, и они оказывают давление на устоявшихся новаторов, таких как Vector Industries и Paragon Weaponry.{/i}"
    "{i}Большая часть их успеха может быть приписана генеральному директору Донни Русу, который был главным выпускником Пилотной программы в Академии ACE, и дальновидным, когда дело доходит до современных и функциональных проектов для GEAR.{/i}"
    
    "Хм, не думаю, что слышал об этих парнях раньше. Должно быть, это местная компания, которая еще не расширилась до штатов. Похоже, они делают себе имя."
    "Время на телефоне \"6:57\". Я пытался услышать любые признаки жизни наверху, но было всё так же тихо."
    play sound "audio/sfx/Human/Stomach Grumble.ogg"
    #stomach grumble
    "Лучше взять что-нибудь перекусить прежде чем придётся идти. Не похоже, что Никки скоро спустится."
    play sound "audio/sfx/Technology/Payment Beep Success.ogg"
    "На телефоне вспыхнула новая статься--заголовок Dasshu. {w}Это должно быть хорошо!"
    play sound "audio/sfx/Technology/Phone Projection.ogg"
    "Я нажал кнопку в форме кинопроектора внизу страницы, и текст спроецировался на ближайшую поверхность. Затем я поставил свой телефон в док-станцию на стол, чтобы текст на кухонном столе сиял."
    "Я взял пару ломтиков хлеба и положил их в тостер. Пока они готовились, я сидел за столом и читал статью."
    
    "{i}Ханаку Диштару, генеральный директор Dasshu, сделал вчера незапланированное появление на поминках Юудай Мисаки. Год назад сообщество было шокировано неожиданной смертью самого многообещающего пилота Академии ACE. {w}Семья почла за честь, что могучий магнат нашел время, чтобы выразить свое почтение их сыну, и одновременно отложил открытие новой линии энергетических напитков Dasshu. {w}Открытие было пересено на следующую неделю--{/i}"
    stop music fadeout 3
    voice "audio/voice/E1/D3/S1/Nikki/1.ogg"
    sf "Что читаешь?"
    show nikki neu at cc with dissolve
    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 1
    menu:
        "АААААААААААХХХХ!":
            pf "Ахх!"
            show nikki cur at cc with dissolve
            "Я пподпрыгнул от удивления и чуть не упал со стула, пытаясь повернуться к ней. Она странно на меня посмотрела."
            show nikki ske at cc
            show question:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/2.ogg"
            sf "Боже, в чем твоя проблема?"
            pf "Ты напугала меня!"
            show nikki mis at cc
            show shiny:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/3.ogg"
            sf "Почему? Ты что, хентай смотрел, или что-то ещё?"
            pf "Что? Нет! Конечно нет!"
            show nikki smi at cc
            "Она посмеялась над моим испуганным выражением лица и прошла мимо меня."
            show nikki mis at cc
            voice "audio/voice/E1/D3/S1/Nikki/4.ogg"
            sf "Я знаю! Знаю! Ты читал новости; Я видела их на столе. Скууууууууучно! Ты ведь знаешь, что это официально делает тебя старым? Только старики ради веселья читают новости."
    
        "Как твои ноги не издают звука?":
            pf "Боже, Никки! Ты напугала меня. Издавай хоть немного шума, когда ходишь!"
            show nikki smi at cc
            "Она засмеялась."
            voice "audio/voice/E1/D3/S1/Nikki/5.ogg"
            sf "Но это полностью разрушило бы мои шансы удивить тебя."
            pf "Давай больше без этого, пожалуйста. Нужно будет повесить колокольчики тебе на шею, чтобы слышать, как ты идешь… как люди делают это с кошками."
            show nikki cur at cc
            voice "audio/voice/E1/D3/S1/Nikki/6.ogg"
            sf "Ты сравниваешь меня с кошкой?"
            pf "В этом всё и дело, не так ли?"
            show nikki ske at cc
            voice "audio/voice/E1/D3/S1/Nikki/7.ogg"
            sf "Эмм?"
            pf "Ты знаешь, как кошкодевочки--"
            show nikki dis at cc
            show drop:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/8.ogg"
            sf "О Боже! Прекрати, извращенец!"
            pf "Что?"
            show nikki ann at cc
            voice "audio/voice/E1/D3/S1/Nikki/9.ogg"
            sf "Ага... Мне не нужно знать о твоих странный маленьких фантазиях!"
            pf "Это не--"
            show nikki dis at cc
            voice "audio/voice/E1/D3/S1/Nikki/10.ogg"
            sf "Так ты не думаешь, что девушка будет выглядеть супер мило с кошачьими ушками?"
            pf "... Нет…"
            "Но теперь, когда я представил это… Я определённо не должен был говорить нет"
            show nikki mis at cc
            voice "audio/voice/E1/D3/S1/Nikki/11.ogg"
            sf "Сотри слюни с лица."
            "Я инстинктивно вытер подбородок, но там ничего не было."
            show nikki smi at cc
            "Никки просто рассмеялась и прошла мимо меня."
    
        "Ничего!":
            show nikki cur at cc
            "Я инстинктивно выключил проекцию. Она попыталась заглянуть через моё плечо, но я ыключил экран. Последнее, что мне нужно так рано утром, это Никки, высмеивающая меня за чтение новостей."
            show nikki ske at cc with dissolve
            show question:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/12.ogg"
            sf "Почему ты такой странный?"
            pf "Я не странный!"
            show nikki sad at cc
            voice "audio/voice/E1/D3/S1/Nikki/13.ogg"
            sf "Тогда почему бы не показать мне?"
            pf "Там ничего интересно. Поверь, тебе не понравится."
            show nikki win b1 at cc with dissolve
            show shoBlush:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/14.ogg"
            sf "Еу!"
            pf "Что?"
            show nikki dis b1 at cc
            voice "audio/voice/E1/D3/S1/Nikki/15.ogg"
            sf "Я только что поймала тебя за просмотром хентая?"
            pf "Нет!"
            show nikki dis b1 at cc
            voice "audio/voice/E1/D3/S1/Nikki/16.ogg"
            sf "Это же кухня. Мы {i}едим{/i} тут--"
            pf "Это не хентай! Смотри!"
            "Я включил телефон и попыталсяь показать ей статью, но она закрыла глаза."
            show nikki win b1 at cc
            show drop:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/17.ogg"
            sf "Прекрати! Я не хочу видеть это!"
            pf "Слушай! Это не хентай! Просто посмотри!"
            "Я тыкал телефоном ей в лицо, но она отворачивалась от меня."
            voice "audio/voice/E1/D3/S1/Nikki/18.ogg"
            sf "Нееееет!"
            pf "Смотри, черт подери, смотри!"
            show nikki sad b1 at cc with dissolve
            "Она недостаточно быстро закрывала глаза и видела статью."
            show nikki smi at cc with dissolve
            "Затем она перестала сопротивляться и засмеялась."
            pf "Что?"
            show nikki mis at cc
            voice "audio/voice/E1/D3/S1/Nikki/19.ogg"
            sf "Дурачок, я знала, что это был не хентай."
            pf "Тогда почему--."
            show nikki hap at cc
            show note:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S1/Nikki/20.ogg"
            sf "Потому что эта реакция бесценна!"
            show nikki smi at cc
            "Она продолжала смеяться и прошла мимо меня."
            "Младшие сёстры…"
            
    stop music fadeout 3
    $renpy.pause(1)
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    show nikki cur at cc with dissolve
    "Никки глянула на мой тост, который выскочил, пока мы разговаривали."
    voice "audio/voice/E1/D3/S1/Nikki/21.ogg"
    sf "Твой тост сожжён."
    pf "Что!"
    "Я вскочил со стула и встал рядом с ней."
    pf "Он не сожжён."
    show nikki ner at cc
    "Она перевернула их, чтобы показать мне другую сторону угольного цвета."
    pf "Ох…"
    show nikki smi at cc
    voice "audio/voice/E1/D3/S1/Nikki/22.ogg"
    sf "ты безнадёжен! Как ты выживаешь в колледже без меня?"
    pf "Я ем в столовой."
    show nikki mis at cc
    voice "audio/voice/E1/D3/S1/Nikki/23.ogg"
    sf "Это всё объясняет."
    "Она выбросила тост и достала из холодильника два йогурта."
    show nikki neu at cc
    voice "audio/voice/E1/D3/S1/Nikki/24.ogg"
    sf "Ну, раз ты испортил завтрак, нам придётся быстро перекусить, если мы не хотим опоздать."
    "Я взял йогурт, который она мне вручила, и мы оба съели их в рекордно короткие сроки. {w}Затем мы взяли наши вещи и направились к двери."
    show nikki hap at cc with dissolve
    show exclamation:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S1/Nikki/25.ogg"
    sf "Можешь подвезти меня сегодня? Вчера автобус был так переполнен!"  
    
    if (E1D2S7_BullyFightWin == 1):
        $ E1D3S1_BikeImpounded = 1
        "Я выглядел немного застенчиво."
        pf "Прости, Никки, мой байк все ещё в школе." 
        show nikki cur at cc
        voice "audio/voice/E1/D3/S1/Nikki/26.ogg"
        sf "Почему?" 
        pf  "Ну… потому что его конфисковали." 
        show nikki ske at cc
        "Никки подняла бровь."
        show question:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S1/Nikki/27.ogg"
        sf "... Что ты сделал?" 
        "Я не собирался рассказывать ей о драке, поэтому я придумал быстрое оправдание." 
        pf "Эм… Я просто припарковался не в том месте; ничего серьёзного. Сегодня уже получу байк обратно. Офис был закрыт к тому времени, когда я пытался его забрать." 
        show nikki mis at cc
        "Никки фыркнула."
        voice "audio/voice/E1/D3/S1/Nikki/28.ogg"
        sf "Почему я не удивлена, что ты нажил себе проблем в первый день?"
        "Если бы она знала…"
        pf "Хех, ты же знаешь меня…"
        show nikki neu at cc
        voice "audio/voice/E1/D3/S1/Nikki/29.ogg"
        sf "Окей, полагаю, увидимся вечером."
        hide nikki with dissolve
        "Она помахала и пошла к автобусной остановке. Я сделал так же."
        jump E1D3S2
        
    elif (E1D2S5_gotbikepass == 1):
        menu: 
            "Ты просто хочешь похвастаться старшим братом {i}пилотом{/i}. Конечно я подвезу тебя!":
                $ E1D3S1_BikeDrove = 1
                "Я уверенно усмехнулся ей." 
                pf "Надеешься подружиться, имея крутого старшего брата?"
                show nikki thi at cc with dissolve
                "Никки закатила глаза."
                show drop:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S1/Nikki/30.ogg"
                sf "Скорее не хочу снова быть раздавленной между вонючей старухой и толстым парнем." 
                pf "Ага… Уверен, так оно и есть."
                show nikki ske at cc
                voice "audio/voice/E1/D3/S1/Nikki/31.ogg"
                sf "Если ты собираешься быть таким, то я просто пойду на автобус…"
                stop music fadeout 3
                "Она развернулась и я засмеялся."
                play music "audio/music/Open Road (GAME VERSION).ogg" fadein 1 fadeout 1
                show nikki cur at cc
                pf "Я шучу, Никки. Давай, я отвезу тебя в школу." 
                play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 1 fadeout 1
                scene black with fade
                $renpy.pause(2.5)
                play sound "audio/sfx/Vehicles/Bike Screech.ogg" fadein 1 fadeout 1
                jump E1D3S3
    
            "Чёрта с два, женщина! Мой байк для дам.": 
                $ E1D3S1_BikeDrove = 1
                pf "Ну уж нет! Я не хочу, чтобы люди видели, как я езжу с младшей сестрой."
                show nikki ske at cc
                show question:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S1/Nikki/32.ogg"
                sf "Младшей? Ты серьёзно?" 
                pf "Очень серьёзно."
                show nikki dis at cc
                "Я погладил её по голове как ребёнка." 
                pf "Тебе всё ещё нужно научиться ориентироваться в городе. Катать тебя не принесет мне никакой пользы."
                show nikki ann at cc
                voice "audio/voice/E1/D3/S1/Nikki/33.ogg"
                sf "Ой, пожалуйста, как будто это причина. Ты просто козёл." 
    
                menu: 
                    "Может я должен её подвезти…":
                        stop music fadeout 3
                        pf "Хорошо. Хорошо. Я подвезу тебя."
                        play music "audio/music/Open Road (GAME VERSION).ogg" fadein 1 fadeout 1
                        show nikki hap at cc
                        "Никки улыбнулась."
                        show note:
                            xoffset 720
                            yoffset 160
                            xzoom .75
                            yzoom .75
                        voice "audio/voice/E1/D3/S1/Nikki/34.ogg"
                        sf "Спасибо!" 
                        pf "Я все ещё козёл?" 
                        show nikki thi at cc with dissolve
                        show nikki neu at cc with dissolve
                        voice "audio/voice/E1/D3/S1/Nikki/35.ogg"
                        sf "Хмм… Полагаю, нет. Но особо не надейся. Ты ещё что-нибудь учудишь до конца дня."
                        pf "Отлично…" 
                        play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 1 fadeout 1
                        scene black with fade
                        $renpy.pause(2.5)
                        play sound "audio/sfx/Vehicles/Bike Screech.ogg" fadein 1 fadeout 1
                        jump E1D3S3
    
                    "Пошло оно! Я козёл!":
                        "Я подмигнул ей и пошёл к мотоциклу."
                        pf "Удачи в школе!" 
                        hide nikki with dissolve
                        "Никки ворчала ответ, пока тащилась к автобусной остановке."
                        "Теперь я мог впечатлить дам своим байком." 
                        jump E1D3S4
        
                
            "Вообще-то я поеду на автобусе.": 
                $ E1D3S1_BusRide = 1
                pf "Я собрался сегодня снова поехать на автобусе."
                show nikki ske at cc
                "Никки нахмурилась, положив руки на бёдра."
                show question:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S1/Nikki/36.ogg"
                sf "Почему? Разве у тебя нет мотоцикла?"
                pf "Да, но не знаю, хочу ли ехать на нём сегодня."
                show nikki wor at cc with dissolve
                "Внезапно она приложила свою руку к моему лбу."
                pf "Эм… Что ты делаешь?"
                show nikki sad at cc
                voice "audio/voice/E1/D3/S1/Nikki/37.ogg"
                sf "Проверяю, заболел ли ты. Ты {i}всегда{/i} предпочитал брать мотоцикл."
                show nikki cur at cc with dissolve
                "Я убрал её руку со своего лица."
                pf "Я а порядке. Я просто думаю, что было бы хорошо узнать город."
                show nikki ske at cc
                "Никки посмотрела на меня самым скептическим взглядом, который я когда-либо видел."
    
                if (E1D2S2_talkwithyuunayes == 1):
                    show nikki hap at cc with dissolve
                    "Затем ее лицо засияло игривой улыбкой."
                    voice "audio/voice/E1/D3/S1/Nikki/38.ogg"
                    sf "Ты надеешься снова увидеть эту девушку?" 
                    pf "Нет нет. Я действительно думаю, что автобус - хорошая идея." 
                    show nikki smi at cc
                    show shiny:
                        xoffset 720
                        yoffset 160
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D3/S1/Nikki/39.ogg"
                    sf "Кооооооооооонечно. Без разницы. В любом случае, увидимся сегодня вечером."
                    hide nikki with dissolve
                    "Я попытался протестовать, но она уже ушла к автобусной остановке."
                    jump E1D3S2
    
                else:
                    show nikki thi at cc
                    "Затем она пожала плечами."
                    voice "audio/voice/E1/D3/S1/Nikki/40.ogg"
                    sf "Хорошо, если ты не хочешь говорить мне, тогда я не хочу знать. Но, я полагаю, это значит, что твой байк можно взять?"
                    pf "Что?"
                    show nikki mis at cc
                    voice "audio/voice/E1/D3/S1/Nikki/41.ogg"
                    sf "Ну, ты же не собираешься брать его… Так, значит, я могу его взять?"
                    $renpy.pause(1)
                    "Моё сердце замерло."
                    pf "Что?!"
                    show nikki smi at cc
                    "Никки залилась смехом."
                    show note:
                        xoffset 720
                        yoffset 160
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D3/S1/Nikki/42.ogg"
                    sf "Ты бы видел своё лицо! Во всяком случае, хорошего дня. Увидимся вечером?"
                    hide nikki with dissolve
                    "Она повернулась и пошла к своей автобусной остановке. Как только шок прошёл, я я пошёлд на свою." 
                    jump E1D3S2
    
    
    else:
        $ E1D3S1_BusRide = 1
        pf "Извини Никки, я не беру мотоцикл сегодня. У меня еще нет пропуска на парковку."
        show nikki wor at cc
        voice "audio/voice/E1/D3/S1/Nikki/43.ogg"
        sf "Ох, сколько времени займёт получение?"
        pf "Я не уверен, но надеюсь скоро получу."
        show nikki mis at cc
        voice "audio/voice/E1/D3/S1/Nikki/44.ogg"
        sf "Ну, ради твоего здравомыслия, я надеюсь, что это не слишком долго!"
        pf "Спасибо… я думаю?"
        show nikki smi at cc
        "никки засмеялась."
        voice "audio/voice/E1/D3/S1/Nikki/45.ogg"
        sf "Увидимся позже, хорошо?"
        pf "Да, увидимся."
        hide nikki with dissolve
        "Она помахала и пошла на автобусную остановку, пока я шёл к своей."
        jump E1D3S2

