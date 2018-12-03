label E1D2S6:
    
    
    
    "Я протянул ей руку, но она отбросила её."
    scene cg kaori intersection fall4 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    voice "audio/voice/E1/D2/S6/Kaori/1.ogg"
    ki "Не трогай меня!"
    
    "Она сделала несколько глубоких вдохов, затем неуверенно подниялась на ноги."
    scene bg campus intersection day with fade
    "Найдя точку опоры, она отряхнула форму. {w}Внезапно она повернулась ко мне." 
    show kaori ang at cc with dissolve
    voice "audio/voice/E1/D2/S6/Kaori/2.ogg"
    ki "Ты слепой?! Ты мог убить меня!"
    
    pf "Мне очень--"
    voice "audio/voice/E1/D2/S6/Kaori/3.ogg"
    ki "О чем ты думал?! Клянусь, в наши дни любой идиот пожет получить права."
    show kaori ann at cc with dissolve
    "Она указала на книги, разбросанные по дороге."
    show vein:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori ang at cc
    voice "audio/voice/E1/D2/S6/Kaori/4.ogg"
    ki "Смотри! Видишь, что ты наделал!"
    
    "Это не очень красиво."
    show kaori ann at cc with dissolve
    "Она поправила руками волосы с растущим раздражением. Всякий раз, когда я пытался извиниться, она прерывала меня словесным избиением."
    
    "Она вспыльчивая, это точно."
    
    menu:
        "Извиниться, и предложить помочь собрать вещи.":
            "Я не заслуживал этого шквала оскорблений, но мог понять ее гнев и раздражение. {w}Я признал свою ошибку, как что прикусил язык и принял оскорбления." 
    
            "Она вздохнула и наклонилась, чтобы собрать вещи. Самой собирать это всё займёт вечность. {w}Я отогнал мотоцикл к обочине, и попытался помочь ей. Но всякий раз, когда я что-то подбирал, она вырывала это из моих рук."
    
            "Мне нужно привлечь ее внимание, чтобы всё исправить. Я взял книгу, и прежде чем она её вырвала, я предложил ее ей."
            show kaori ske at cc
            voice "audio/voice/E1/D2/S6/Kaori/5.ogg"
            ki "А? Чт..."
    
            "Её взгляд перемещался то на меня, то на книгу, и всё это вреся её глаза сужались."
            show kaori ann at cc
            voice "audio/voice/E1/D2/S6/Kaori/6.ogg"
            ki "Почему ты все ещё здесь? Недостаточно проблем устроил?"
    
            "Она крадет книгу из моих рук."
    
            pf "Слушай, мне очень жаль."
            show kaori dis at cc
            "Она скрестила руки, огонь горел в её глазах."
    
            pf "Так, могу я помочь тебе?"
    
            "Она пожала плечами, и бросила книгу обратно в сумку."
            show kaori thi b1 at cc with dissolve
            voice "audio/voice/E1/D2/S6/Kaori/7.ogg"
            ki "Плевать. Делай что хочешь."
    
            "Я думаю, так она говорит \"да\"."
    
            "Я принялся собирать упавшие вещи. Прошло немного времени, и мы закончили."
            show kaori neu at cc with dissolve
            "Она проверила сумку."
            voice "audio/voice/E1/D2/S6/Kaori/8.ogg"
            ki "Похоже тут всё."
            show dots:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            $renpy.pause(1)
            show kaori thi at cc with dissolve
            $renpy.pause(1)
            "Между нами возникла неловкая тишина. {w}На мгновение она посмотрела на ноги." 
    
            "Предыдущая враждебность ушла. Я имею в виду, она все ещё раздражена, но не настолько, что \"Я собираюсь забить тебя насмерть книгами и свалить труп в канализацию\" в таком роде."
            show kaori dis at cc
            voice "audio/voice/E1/D2/S6/Kaori/9.ogg"
            ki "Спасибо... я полагаю. Хоть это и была изначально твоя вина."
    
            "Я почесал затылок с застенчивой усмешкой."
    
            pf "Без проблем. И снова, мне очень жаль за всё это."
            show kaori ann at cc
            voice "audio/voice/E1/D2/S6/Kaori/10.ogg"
            ki "Всё равно. Я опоздаю, если буду весь день говорить с идиотом как ты. Пока."
            hide kaori with dissolve
            "Она быстрым шагом прошла мимо меня. Вскоре я потерял её за поворотом."
    
            "Ну, это было… что-то."
            play sound "audio/sfx/Vehicles/Bike Ignition.ogg"
            "Я вернулся к мотоциклу уверернный, что сделал всё правильно."
            
            stop music fadeout 3
            
            $ E1D2S3_MetKaoriWasNice = 1
            
            jump E1D2S7
    
        "Быстро ей помогу и не потеряю время.":
            "{i}У кого-то{/i} проблемы с манерами, но я был бы полным придурком, если бы не помог ей."
    
            "Я вздохнул. Давай быстро разберёмся с этим, чтобы успеть в академию."
    
            "Я неохотно отогнал мотоцикл в сторону, и начал собирать её вещи. К сачастью, тут не так много, так что это не должно занять много времени..."
            show kaori ske at cc with dissolve
            "Она вырвала вещи у меня из рук."
    
            "... Или займёт."
            show kaori ang at cc
            voice "audio/voice/E1/D2/S6/Kaori/11.ogg"
            ki "Что ты делаешь?! Я не просила твоей помощи!"
            show kaori ann at cc
            "И шум в ушах вернулся. {w}Вздрогнув, I tilt my head away from her, and hope that my ears aren't bleeding."
    
            pf "Yeesh. Shouldn't you be thankful I'm taking the time to help you? We'll be done in seconds if you let me help. Come on."
            show kaori ang at cc with dissolve
            show vein:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S6/Kaori/12.ogg"
            ki "No! Just leave it!"
            
            "I'm going to be here all day if I argue with her. I step around her and grab her bag off the ground. Trying my best to ignore her verbal barrage of complaints and insults, I collect the remaining items."
            show kaori ann at cc with dissolve
            "I try to hand back her bag, but she snatches it out of my hands."
    
            "A \"thank you\" would be nice."
    
            pf "See? All there, and that took no time at all."
            show kaori dis at cc
            "She rummages inside her bag, ruining my neat packing job. Does she think I might have tried to steal something? I'm not {i}that{/i} bad."
    
            "Content, she closes the bag back up and gives me a dull look. At least she's visibly less angry than before."
            voice "audio/voice/E1/D2/S6/Kaori/13.ogg"
            ki "... Fine."
            hide kaori with dissolve
            "Without another word, she turns on her heel and heads in the direction of the academy."
    
            pf "... Still waiting on that \"thank you\"."
    
            "I trek back to my bike, feeling just a little bit more deaf than before."
            
            stop music fadeout 3
            
            $ E1D2S3_MetKaoriWasNice = 1
            
            jump E1D2S7
    
        "Whatever, I'm out.":
            $ E1D2S3_MetKaoriWasRudeNoHelmet = 1
            
            "This is going nowhere. She isn't injured, so I don't have any problem with leaving."
    
            if (E1D2S3_mcwithhelmet == 0):
                play sound "audio/sfx/Vehicles/Bike Ignition.ogg"
                "I start up my bike and sail past her, regretting ever stopping for someone as crazy as her in the first place."
                stop ambient fadeout 3
                play ambient "audio/ambience/Open Road No Helmet.ogg" fadein 1
    
            if (E1D2S3_mcwithhelmet == 1):
                play sound "audio/sfx/Vehicles/Bike Ignition.ogg"
                "I put my helmet back on and start the bike."
                play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 5 fadeout 5
                "As I make my way past her, I think I hear muffled shouting behind me. I'm too far to make out what she says, which is probably for the best."
                stop ambient fadeout 3
                play ambient "audio/ambience/Open Road Helmet.ogg" fadein 1
    
    scene black with fade
    jump E1D2S7
