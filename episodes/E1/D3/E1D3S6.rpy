label E1D3S6:
    # Already in library, ambient is playing with no music
    "Я вошёл через раздвижные двери в большую светлую библиотеку. Ряд за рядом высокие стеллажи с книгами тянулись дальше, чем мог видеть."
    
    "Несколько студентов разбросаны по комнате. Некоторые искали что-то на книжных полках, в то время как другие занимались за одноместными стоилками по всей библиотеке.." 
    
    if (E1D2S2_talkwithyuunayes == 0):
        $ E1D3S6_WentLibraryStudied = 1
        jump E1D3S7
    
    "Я шёл к одному из пустых столов, когда в глаза бросились ярко-розовые волосы."
    show yuuna neu at cc with dissolve
    "Юна концентрировалась на большой книге перед ней." 
    
    menu:
        "Оставить её в покое.":
            $ E1D3S6_WentLibraryStudied = 1
            "Она вглядела занятой. Лучше не беспокоить её."
            hide yuuna with dissolve
            jump E1D3S7
    
        "Пойти поздороваться.":
            $ E1D3S6_WentLibraryYuuna = 1
            play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 1
            "Я подошёл." 
            pf "Привет, Юна."
            show exclamation:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna cur at cc with dissolve
            show yuuna smi at cc with dissolve
            "Она взглянула на меня и улыбнулась."
            voice "audio/voice/E1/D3/S6/Yuuna/1.ogg"
            ym "Привет." 
            "Я указал на пустой стул рядом с ней."
            pf "Могу присесть?"
            show yuuna hap at cc
            voice "audio/voice/E1/D3/S6/Yuuna/2.ogg"
            ym "Конечно." 
            pf "Что читаешь?"
            show yuuna smi at cc
            voice "audio/voice/E1/D3/S6/Yuuna/3.ogg"
            ym "Просто один из учебников."
            stop music fadeout 3
            "Я глянул на открытую страницу и заметил слова \"здоровье\" и \"приоритет\". Должно быть книга по физиотерапии."
    
            if (E1D2S2_YuunaComesWithYouPass == 1):
                pf "Спасибо ещё раз за то, что помогла мне вчера."
                show yuuna hap b1 at cc with dissolve
                voice "audio/voice/E1/D3/S6/Yuuna/4.ogg"
                ym "Ничего особенного." 
                pf "Нет, я действительно ценю это. Редко можно найти кого-то, кто изо всех сил помог бы незнакомцу."
                show yuuna smi b1 at cc
                show regBlush:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                "Юна улыбнулась."
                stop music fadeout 3
                voice "audio/voice/E1/D3/S6/Yuuna/5.ogg"
                ym "Ну, я была рада помочь."
                
            show yuuna smi at cc with dissolve
            voice "audio/voice/E1/D3/S6/Yuuna/6.ogg"
            ym "Так, тебе нравится ACE??"
            play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 1
    
            menu: 
                "Он ооооооооотлиииичен!":
                    pf "Он крут!"
                    show yuuna cur at cc with dissolve
                    "Она моргнула от этого всплеска эмоций."
                    show dots:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    show yuuna thi b1 at cc with dissolve
                    "Пара соседних учеников шикнули, и она смутилась."
                    pf "Извини за это."
                    "Когда она говорла дальше, ее голос был значительно мягче."
                    show yuuna hap b1 at cc with dissolve
                    voice "audio/voice/E1/D3/S6/Yuuna/7.ogg"
                    ym "Не волнуйся. Приятно видеть кого-то таким восторженным. Но теперь мне любопытно, что сделало это таким замечательным днем."
                    pf "Ну, мой первый урок казался многообещающим, хоть это и первый год. {w}Кажется, что материал более специфичен для академии ACE, поэтому он не будет полностью повторяться. Мне также удалось найти команду для квалификации."
                    pf "Ох, и я встретил вчера в автобусе действительно милую девушку."
                    show yuuna ner b1 at cc with dissolve
                    show regBlush:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    "Она покраснела и слабо улыбнулась."
                    show yuuna smi b1 at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/8.ogg"
                    ym "Ты слишком добр. В какую команду ты вступил?" 
                    pf "В ней Сё и две другие девушки, кажется, Каори и Маю."
                    show yuuna hap at cc with dissolve
                    "Юна понимающе кивнула." 
                    voice "audio/voice/E1/D3/S6/Yuuna/9.ogg"
                    ym "Они должно быть хорошая команда."
                    pf "О, ты знаешь их?"
                    show yuuna smi at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/10.ogg"
                    ym "Нет, но я о них слышала."
                    pf "Что ты слышала?"
                    show yuuna thi at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/11.ogg"
                    ym "Обычные вещи--что они были частью другой хорошей команды, но ушли из-за разногласий с лидером."
                    pf "А, да, я тоже это слышал."
                    show yuuna smi at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/12.ogg"
                    ym "Я не пилот, поэтому не слышу никаких подробных сплетен."
                    pf "Это нормально. Я новичок, поэтому я не слышу никаких подробных сплетен."
                    show yuuna hap at cc
                    "Она тихо посмеялась."
             
                "С тобой здесь, я думаю, я мог бы привыкнуть к этому месту.":
                    pf "Он не плох. Совсем не плох."
                    show yuuna cur at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/13.ogg"
                    ym "Наслаждаешься пребыванием здесь?"
                    pf "Абсолютно."
                    show yuuna hap at cc
                    "Она казалась довольной моим ответом."
                    voice "audio/voice/E1/D3/S6/Yuuna/14.ogg"
                    ym "Что тебе больше всего нравится в ACE?"
                    "Я долго смотрел на неё."
                    pf "Ну, должен сказать, что тут самые красивые достопримечательности, которые я когда-либо видел."
                    show question:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    show yuuna cur b1 at cc with dissolve
                    voice "audio/voice/E1/D3/S6/Yuuna/15.ogg"
                    ym "Правда? Даже лучше, чем в CINY?"
                    pf "О да, CINY Не может сравниться."
                    "Я усмехнулся ей."
                    show yuuna sur b1 at cc with dissolve
                    show shoBlush:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    "Она удивленно моргала и кажется почти засмущалась, её щёки легко покраснели."
                    show yuuna ner b1 at cc
                    "Она быстро сменила тему."
                    show yuuna thi b1 at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/16.ogg"
                    ym "Так, скоро квалификация пилотов, да?"
                    pf "Да, и я уже нашёл себе команду."
                    show yuuna hap b1 at cc with dissolve
                    voice "audio/voice/E1/D3/S6/Yuuna/17.ogg"
                    ym "О, это здорово!"
                    "Её лицо снова покраснело, когда ученики рядом с нами шикнули ей."
                    show yuuna ner b1 at cc with dissolve
                    voice "audio/voice/E1/D3/S6/Yuuna/18.ogg"
                    ym "Я имела в виду, это замечательно."
                    show yuuna smi b1 at cc with dissolve
                    pf "Я так же взволнован. Я чувствую себя хорошо в этой команде."
                    
                "Нормально, я полагаю.":
                    pf "It's alright." 
                    show yuuna ner at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/19.ogg"
                    ym "О… Есть что-то о чём ты скучешь в CINY, чего нет здесь?"
                    pf "Не особо."
                    show yuuna neu at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/20.ogg"
                    ym "Понятно."
                    show dots:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    "Она замолкла и ждала, пока я что-нибудь не скажу."
                    pf "Я имею в виду, что среди всех школ, эта не ужасная."
                    show yuuna cur at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/21.ogg"
                    ym "О, эм, полагаю, этого хорошо."
                    pf "В любом случае, я забочусь о схватках GEAR, так что найти команду - залог успеха."
                    show yuuna smi at cc
                    "Она вежливо улыбнулась."
    
            show yuuna hap at cc
            voice "audio/voice/E1/D3/S6/Yuuna/22.ogg"
            ym "Ну, рада слышать, что тебе нравится здесь."
            show yuuna cur at cc with dissolve
            "Она глянула на часы на стене, и её глаза округлились."
            voice "audio/voice/E1/D3/S6/Yuuna/23.ogg"
            ym "Ох, Я не заметила который уже час. У меня назначена встреча в регистратуре."
            show yuuna neu at cc
            "Она начала собираться."
            show yuuna smi at cc
            voice "audio/voice/E1/D3/S6/Yuuna/24.ogg"
            ym "Было приятно снова тебя увидеть."
            pf "Да, тебя тоже. Завтра увидимся, верно?"
            show yuuna cur at cc
            "Она моргала."
            pf "Я имею в виду в классе…"
            show yuuna hap at cc
            voice "audio/voice/E1/D3/S6/Yuuna/25.ogg"
            ym "О да! Тогда увидимся."
            hide yuuna with dissolve
            "Она ушла улыбнувшись и быстро помахав."
            stop music fadeout 3
            "Я сел за её только что освободившийся стол и достал планшет из сумки. Пора за работу."
            #fade to black
            scene black with fade
            $renpy.pause(2.5)
            "Когда я закончил, было уже поздно. Я быстро собрал вещи и ушёл."
            stop ambient fadeout 3
    
            jump E1D3S8
