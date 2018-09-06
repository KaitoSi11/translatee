label E1D1S4:
        
    scene bg homekaito myroom night packed with fade
    "Хорошо, Время распаковки."
    
    play sound "audio/sfx/Impacts/Box Shuffling.ogg" fadein 1 fadeout 1
    
    scene bg homekaito myroom night with Dissolve(3.0)
    $ nikOut = "sSleepwear"
    
    $renpy.pause(1.0)
    "Мне удалось разобрать большинство своих вещей, прежде чем меня прервали."
    
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 1
    voice "audio/voice/E1/D1/S4/Nikki/1.ogg"
    sf "Ты уже распаковал вещи?"
    
    show nikki neu at r3 with dissolve:
        xzoom -1
    
    "Никки выглядела напряжённой. Не смотря на небольшую улыбку, её брови дрожали от волнения."
    
    pf "Только что. А ты?"
    
    show nikki ner at cc with dissolve:
        xzoom 1
    voice "audio/voice/E1/D1/S4/Nikki/2.ogg"
    sf "Почти… но слушай, что ты думаешь об этой форме? Она довольно странная, не так ли?"
    show dots:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    "Она некомфортно переминается с ноги на ногу."
    
    menu:
        "Я думаю, это отличная идея.":
            pf "Это будет неплохой переменой. И нам не придется беспокоиться о несовпадающих носках или что-то в этом роде." 
            show nikki smi at cc
            "Она хихикнула."
            show nikki mis at cc
            voice "audio/voice/E1/D1/S4/Nikki/3.ogg"
            sf "Может с тобой такое и происходит, но мои носки всегда совпадают."
    
        "Без разницы.":
            pf "А это важно? Мы привыкнем."
            show nikki thi at cc
            "Никки посмотрела в пол."
            voice "audio/voice/E1/D1/S4/Nikki/4.ogg"
            sf "Полагаю, ты прав."
    
        "Это же будет как в моих любимых аниме!":
            pf "Ты шутишь? Это же отлично! Просто подумай о всех этих девушках в коротких юбках. Хехехехе."
            show nikki ske at cc
            "И этот ветер, идеально выбирающий время, показывая разноцветные трусики--"
            
            show nikki ann
            play sound "audio/sfx/Human/light_punch.ogg"
            with Shake((0, 0, 0, 0), .5, dist=10)
            
            $renpy.pause(.25)
            pf "Ау!"
            "Для такой маленькой девочки у неё уверенные удары."
            "Никки вздохнула."
            #show tsuBlush:
             #   xoffset 720
              #  yoffset 160
               # xzoom .75
                #yzoom .75
            voice "audio/voice/E1/D1/S4/Nikki/5.ogg"
            sf "Ты безнадёжен."
            
    show nikki sur at cc with dissolve
    show exclamation:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D1/S4/Nikki/6.ogg"
    sf "Ох, я почти забыла! Какую форму ты должен носить? Я имею в виду, что моя... обычная, но ты же идёшь в академию ACE."
    
    "Я пожал плечами."
    
    pf "Форма говорит о том, что ты обычный студент или состоишь в программе пилотов. У пилотов на одежде тиановая маркировка." 
    
    show nikki cur at cc
    voice "audio/voice/E1/D1/S4/Nikki/7.ogg"
    sf "Ооо, звучит неплохо. Ты перевёлся прямо в программу пилотов, да?"
    
    pf "Да." 
    
    show nikki hap at cc
    voice "audio/voice/E1/D1/S4/Nikki/8.ogg"
    sf "Я слышала к ним сложно попать, но я в тебе не сомневалась! Я надеюсь они готовы, ведь ты надёрешь им зад!"
    
    pf "Спасибо, сестрёнка."
    
    "Часы на тумбочке показали 11:00 PM."
    
    pf "Думаю, пора спать."
    
    show nikki wor at cc
    voice "audio/voice/E1/D1/S4/Nikki/9.ogg"
    sf "Что? Уже?"
    
    "Я нежно вытолкнул её из комнаты."
    show crying:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D1/S4/Nikki/10.ogg"
    sf "Но ещё не {i}настолько{/i} поздно!"
    
    pf "Да ладно. Ты же не хочешь потом уснуть в классе?"
    
    show nikki sad at cc
    show storm:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    "Она вздохнула, и я волновался, что она продолжит спорить, но она просто пробормотала что-то бессвязное и направилась в свою комнату."
    
    pf "Спокойной ночи."
    
    show nikki smi at cc
    voice "audio/voice/E1/D1/S4/Nikki/11.ogg"
    sf "Спокойной."
    
    hide nikki with dissolve
    play sound "audio/sfx/Impacts/Box Shuffling.ogg" fadein 5 fadeout 5
    
    "Я вернулся к разбросанным коробкам и попытался собрать их в аккуратную кучю. {w}Когда я добрался до последней коробки, рамка с фотографией упала на землю с громким грохотом. Сержде сжалось в груди, когда я схватил её и проверил, не разбилась ли она. {w}К счастью, она невредима."
    
    
    $ persistent.gpix[0][0] = 1
    
    scene cg mc family photo at Zoom((1920, 1080), (1740, 180, 1920, 1080), (1740, 180, 1920, 1080), 0) with dissolve
    
    "Я провёл пальцем по улыбающимся лицам: я, Никки, мама, папа. {w}Мы были на ярмарке, и Никки хотела покататься на американских горках. {w}Помню, что спорил с мамой о чем-то глупом до того, как была сделана фотография, но по ней вы никогда не сможете сказать этого. Мама всегда выглядела уравновешенной."
    
    scene cg mc family photo at Zoom((1920, 1080), (1740, 180, 1920, 1080), (0, 0, 3840, 2160), 5.0)
    
    "Я положил рамку рядом с компьютером, пытаясь подавить ком в горле."
    
    "Я лёг на кровать и закрыл глаза, но мылсли отказывались уходить. {w}В конце концов усталость взяла верх, и я заснул среди путаницы вопросов и «что, если», носящихся в голове."
    
    stop music fadeout 3
    stop ambient fadeout 3
        
    scene black with fade
    
    $renpy.pause(1)
    
    jump E1D2S1
