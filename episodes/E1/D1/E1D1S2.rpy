label E1D1S2:

    $ kaiOut = "sWork"
    
    #BG Train Station
    scene bg travel trainstation dusk with dissolve
    #Ambience Train Station
    play ambient "audio/ambience/Train Station.ogg" fadein 3
    
    $ achievement.grant("welcome_to_isokaze")
    
    "Как только мы вышли из поезда, на меня обрушилась какофония звуков. {w}Бизнесмен быстро проходит мимо, говоря по телефону строгим тоном, пока стоящая рядом мать тщетно старалась успокоить плачущего ребёнка. {w}Группа пожилых женщин украдкой бросает взгляды на нас и перешёптывается между собой. Они часто громко смеялись."
    
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
    
    show nikki neu at cc with Dissolve(.75)
    
    "Никки с нетерпением выходит из поезда, вдыхая прохладный воздух."
       
    if (E1D1S1_nikkimad == 1) :
            "К счастью для меня, она быстро вернулась в своё обычное состояние."
    
    show nikki hap at cc
    show note:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D1/S2/Nikki/1.ogg"
    sf "Ах, так-то лучше!"
    "Она оглядывается на меня и кладет руки на бедра."
    show nikki neu at cc
    voice "audio/voice/E1/D1/S2/Nikki/2.ogg"
    sf "Поторопись, слоупок!"
    
    
    if (MCStory == 1):
        "Я легко беру наш багаж и выхожу на платформу."
    
    elif (MCStory != 1):
        "Борясь с весом нашего башажа, я падаю, выходя из поезда."
        #SFX Luggage Slamming
        play sound "audio/sfx/Impacts/Luggage Drop.ogg"
        
        "Чемоданы бесцеремонно падают рядом со мной на платформу. Хорошо, что здесь нет ничего хрупкого. Предложение нести обе наши сумки уже не кажется такой хорошей идеей."
        
        show nikki smi at cc
        
        pf "Отлично. {w}Превосходно. {w}Просто замечательно."
        "Я минутку передохнул, разминая горящие конечности."
        
    pf "Ты уже видела дядю Кайто?"
    
    show nikki cur at cc
    voice "audio/voice/E1/D1/S2/Nikki/3.ogg"
    sf "Эмм, ещё нет. Когда мы должны с ним встретиться?"
    pf "В 6:30... {w}Похоже, он немного опаздывает. {w}Вероятно пробки."
    $renpy.pause(1)
    "После нескольких минут сканирования, из толпы появляется знакомое лицо."
    
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    
    show kaito smi at r3:
        xzoom -1
    with dissolve
    show exclamation:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    show nikki sur at cc with dissolve
    voice "audio/voice/E1/D1/S2/Nikki/4.ogg"
    sf "Дядя Кайто!"
    
    show kaito hap at r3
    
    "Его лицо расплылось в широкой ухмылке."
    voice "audio/voice/E1/D1/S2/Kaito/7.ogg"
    hk "{b}До~бро по~жа~ло~ва~ть в Я~по~ни~ю~~!{/b}"
    
    show nikki hap at cc
    
    "Никки хихикает над {i}англисйким{/i} Кайто."
    voice "audio/voice/E1/D1/S2/Nikki/5.ogg"
    sf "{b}При~вет!~ Меня зовут Ни~кки~~{/b}"
    
    show kaito smi at r3
    show nikki neu at cc
    with dissolve
    
    menu:
        "Привет.":
                pf "Привет, дядя Кайто."
                
                show kaito hap at r3
                voice "audio/voice/E1/D1/S2/Kaito/1.ogg"
                hk "Как поживает моя любимый племянник?"
                pf "Я твой единственный племянник."
                
                show kaito mis at r3
                voice "audio/voice/E1/D1/S2/Kaito/2.ogg"
                hk "Все ещё любимый!"
                
                show nikki smi at cc
                
                "Никки смеётся."
    
        "Herro!":
            stop music fadeout .75
            pf "Why herro dere!"
            
            show kaito sur at r3
            show nikki sur at cc
            with dissolve
            
            show dots:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            show dots2:
                xoffset 1175
                yoffset 5
                xzoom .75
                yzoom .75
            $renpy.pause(1)
            "Они оба смотрят на меня."
            pf "...Что?"
            
            show kaito ske at r3
            show nikki dis at cc
            voice "audio/voice/E1/D1/S2/Nikki/6.ogg"
            sf "Ты не можешь говорить это! Это оскорбительно!"
            pf "Вы двое только что делали тоже самое!"
            
            show kaito dis at r3
            voice "audio/voice/E1/D1/S2/Kaito/3.ogg"
            hk "Тебе ещё нужно немного подучиться, пацан."
            
            show nikki thi at cc
            
            "Никки скрестила руки и кивнула в знак согласия. {w}Что я сделал не так?!"
            play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
                
        "Дядя Кайто свободно говорит по-английски...":
            pf "Я разговаривал с тобой два часа назад... {w}Ты так не говорил."
            
            show kaito mis at r3
            
            "Кайто смотрит на меня с проказливой усмешкой."
            voice "audio/voice/E1/D1/S2/Kaito/4.ogg"
            hk "Чёрт, снова раскусили меня!"
    
        "Какого хрена?":
            pf "Эм, почему вы так говорите?"
            
            show kaito mis at r3
            show note:
                xoffset 1175
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D1/S2/Kaito/5.ogg"
            hk "{b}Ч~то ты име~ешь в ви~ду?{/b}"
            pf "Прекратите."
            
            show nikki mis at cc
            show note:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D1/S2/Nikki/7.ogg"
            sf "{b}Пре~кра~тить что, браа~аааааааа~тик?{/b}"
            pf "Серьёзно!"
            
            show kaito hap at r3
            show nikki smi at cc
            
            "Никки и Кайто рассмеялись. {w}Не может быть, чтобы я был связмн с этими двумя."
    
    #SFX Stomach Grumble
    play sound "audio/sfx/Human/Stomach Grumble.ogg"
    
    show kaito cur at r3
    show nikki cur b1 at cc
    with dissolve
    show shoBlush:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    $renpy.pause(1)
    "Громкое урчание прервало нас."
    
    show nikki sur b1 at cc with dissolve
    voice "audio/voice/E1/D1/S2/Nikki/8.ogg"
    sf "Хехе... Извините."
    
    show kaito hap at r3
    
    "Дядя Кайто рычит, смеясь."
    
    show kaito smi at r3
    show nikki smi b1 at cc
    voice "audio/voice/E1/D1/S2/Kaito/6.ogg"
    hk "Пойдёмте накормим вас."
    
    stop ambient fadeout 3
    stop music fadeout 3
    
    #BG Fade black
    scene black with fade
    #SFX Car Start/Drive Away
    play sound "audio/sfx/Vehicles/Car Start and Drive Away.ogg"
    
    $renpy.pause(5.0)
    
    jump E1D1S3
