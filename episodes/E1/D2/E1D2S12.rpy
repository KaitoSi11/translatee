label E1D2S12:
    
    stop music fadeout 3
    stop ambient fadeout 3
    scene black with fade
    "..."
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
    
    if (E1D2S7_ParkedFar == 1):
        play ambient "audio/ambience/Parking Lot.ogg" fadein 1
        scene bg campus parking dusk empty with fade
        "Время совершить поход до самого конца участка. Интересно, почему они сделали гостевую парковку так далеко. Разве это не будет препятствовать, а не поощрять людей к посещению?"
        "Хотя я ворчал весь путь до мотоцикла, в конце концов я нашел его в том же месте, где припарковал." 
    
        if (E1D2S7_BullyFightWin == 0) and (E1D2S7_CleanMove == 1):
            pf "Время ехать."
    
        if (E1D2S3_mcwithhelmet == 1):
            "Я запрыгнул на мотоцикл и надел шлем."
            
        if (E1D2S3_mcwithhelmet == 0):
            "Я запрыгнул на мотоцикл. Я не мог дождаться, когда почувствую ветер на моем лице."
            
        play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 3
        stop ambient fadeout 3
        stop music fadeout 3
        scene black with fade
        "Заведя мотоцикл, я направился домой."
        play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 1 fadeout 1
        
        #Don't need to go through images
        #scene bg campus intersection dusk with fade
        #scene bg travel openroad dusk with fade
        #scene isokaze highschool dusk with fade

        $renpy.pause(2)
        
        jump E1D2S13
        
    
    elif (E1D2S7_BullyFightWin == 1):
        play ambient "audio/ambience/Parking Lot.ogg" fadein 1
        scene bg campus parking dusk with fade
        "Я быстро шёл к парковке, и вскоре появились первые места. Когда я приблизился, то заметил как далеко она простирается. Должно быть хреново тем неудачникам, которым приходится парковаться на противоположной стороне школы."
        "Я стоял там, где я помню, как стоял мой мотоцикл, но он был заменен другим. Я просканировал первые несколько рядов мотоциклов, но нигде не могу найти свой."
        "Этого не может быть… Я уверен, что припарковался здесь."
        "Между кампусом и и парковкой находилось небольшое здание. Это должно быть здание охраны. Когда я подошёл, крепкий охранник нахмурился."
        show guard extra at cc with dissolve
        pf "Извините."
        voice "audio/voice/E1/D2/S12/Guard/1.ogg"
        gua "Да?"
        pf "Я припарковал свой мотоцикл утром, но его больше нет здесь."
        "Он повернулся к компьютеру."
        voice "audio/voice/E1/D2/S12/Guard/2.ogg"
        gua "Какой номер пропуска?"
        pf "У меня нет его."
        "Он оглянулся на меня и поднял бровь."
        show question:
            xoffset 675
            yoffset 50
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S12/Guard/3.ogg"
        gua "Ты припарковался в зарезервированном месте без пропуска. Чего ты вообще ожидал?"
        pf "Я думал, что мой мотоцикл будет всё ещё там, где я его оставил."
        voice "audio/voice/E1/D2/S12/Guard/4.ogg"
        gua "Ну, теперь ты будешь знать лучше. Твой мотоцикл был конфискован."
        "Я чувствовал как рука в груди сжимала сердце. Моя малышка! Что, если они поцарапали её?"
    
        "Этот придурок должно быть вызвал его, чтобы мой мотоцикл убрали, когда он пришёл. Что за неудачник, не умеющий проигрывать!"
        voice "audio/voice/E1/D2/S12/Guard/5.ogg"
        gua "Ты можешь забрать его утром."
        pf "Но почему не сейчас?"
        "Охранник посмотрел на меня, как будто у меня было две головы."
        voice "audio/voice/E1/D2/S12/Guard/6.ogg"
        gua "Ты не знаешь который сейчас час?"
        pf "Эм…"
        "Я посмотрел на телефон."
        pf "Минута шестого."
        voice "audio/voice/E1/D2/S12/Guard/7.ogg"
        gua "Именно. Моя работа закончена."
        pf "Что? Но мы все ещё разговариваем--"
        show storm:
            xoffset 675
            yoffset 50
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S12/Guard/8.ogg"
        gua "Уже нет. Мы закрыты. Если у тебя есть жалоба, то можешь подать её утром."
        hide guard extra with dissolve
        "Он вытолкнул меня из здания и запер его. Похоже, у меня нет выбора, кроме как поехать сегодня домой на автобусе."
        jump E1D2S12_BusConverge
        
    elif (E1D2S1_firstdaybus == 1):
        "Я пошёл в сторону парковки прежде чем вспомнил, что оставил мотоцикл дома. Ох чёрт, я забыл посмотреть расписание автобусов! К счастью, скоро прибудет один. Я просматиривал расписание, пока торопился  к передней части кампуса."
        scene bg campus main dusk with fade
        "Посадка и высадка производится в одном и том же месте, так?"
    
        label E1D2S12_BusConverge:
            scene black with fade
            play ambient "audio/ambience/Parking Lot.ogg" fadein 1
            "Когда я добрался до автобусной остановки, там была небольшая группа ожидавших учеников."
            if (E1D2S2_talkwithyuunayes == 1):
                "Я поднял шею, чтобы найти Юну, но её там не было. Полагаю, мне просто хотелось думать, что она там."
            else:
                "Я посмотрел на их лица, вдруг узнаю кого-нибудь. Но я не узнал никого." 
    
            play sound "audio/sfx/Vehicles/Bus Door Open.ogg" fadein 1 fadeout 1
            "После ожидания, которое казалось длинною в жизнь, автобус прибыл."
            stop ambient fadeout 3
            scene bg travel bus dusk with fade
            stop music fadeout 3
            play sound "audio/sfx/Vehicles/Bus Chime.ogg" fadein 1 fadeout 1
            play ambient "audio/ambience/Bus.ogg" fadein 1
            "Я смог сразу найти место, и добрался домой без приключений."
            scene black with fade
            $renpy.pause(1)
            play sound "audio/sfx/Vehicles/Bus Chime.ogg" fadein 1 fadeout 1
            stop ambient fadeout 3
            play sound "audio/sfx/Vehicles/Bus Door Open.ogg" fadein 1 fadeout 1
            $renpy.pause(1)
        
    jump E1D2S13
