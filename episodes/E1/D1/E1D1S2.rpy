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
    hk "{b}W~el~com~e   to   Ja~pan~!{/b}"
    
    show nikki hap at cc
    
    "Nikki giggles at Kaito's {i}English{/i}."
    voice "audio/voice/E1/D1/S2/Nikki/5.ogg"
    sf "{b}He~llo!~ My name is Ni~kki~~{/b}"
    
    show kaito smi at r3
    show nikki neu at cc
    with dissolve
    
    menu:
        "Hey.":
                pf "Hey, Uncle Kaito."
                
                show kaito hap at r3
                voice "audio/voice/E1/D1/S2/Kaito/1.ogg"
                hk "How's my favourite nephew doing?"
                pf "I'm your only nephew."
                
                show kaito mis at r3
                voice "audio/voice/E1/D1/S2/Kaito/2.ogg"
                hk "Still my favourite!"
                
                show nikki smi at cc
                
                "Nikki laughs."
    
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
            "They both stare at me."
            pf "...What?"
            
            show kaito ske at r3
            show nikki dis at cc
            voice "audio/voice/E1/D1/S2/Nikki/6.ogg"
            sf "You can't say that! That's offensive!"
            pf "You two were just doing the same thing!"
            
            show kaito dis at r3
            voice "audio/voice/E1/D1/S2/Kaito/3.ogg"
            hk "You have quite a bit to learn, kiddo."
            
            show nikki thi at cc
            
            "Nikki crosses her arms and nods in agreement. {w}What did I do wrong?!"
            play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
                
        "Uncle Kaito speaks fluent English...":
            pf "I spoke to you two hours ago... {w}You don't talk like that."
            
            show kaito mis at r3
            
            "Kaito shoots me an impish grin."
            voice "audio/voice/E1/D1/S2/Kaito/4.ogg"
            hk "Darn, foiled again!"
    
        "WTF?":
            pf "Um, why are you two talking like that?"
            
            show kaito mis at r3
            show note:
                xoffset 1175
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D1/S2/Kaito/5.ogg"
            hk "{b}Wh~at do y~ou me~an?{/b}"
            pf "Stop."
            
            show nikki mis at cc
            show note:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D1/S2/Nikki/7.ogg"
            sf "{b}Sto~p what Oniiiiiiii-cha~nnnnn?{/b}"
            pf "Seriously!"
            
            show kaito hap at r3
            show nikki smi at cc
            
            "Nikki and Kaito burst out laughing. {w}There's no way I'm actually related to these two."
    
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
    "A loud grumble interrupts us."
    
    show nikki sur b1 at cc with dissolve
    voice "audio/voice/E1/D1/S2/Nikki/8.ogg"
    sf "Hehe... Sorry."
    
    show kaito hap at r3
    
    "Uncle Kaito roars with laughter."
    
    show kaito smi at r3
    show nikki smi b1 at cc
    voice "audio/voice/E1/D1/S2/Kaito/6.ogg"
    hk "Let's get some food in you."
    
    stop ambient fadeout 3
    stop music fadeout 3
    
    #BG Fade black
    scene black with fade
    #SFX Car Start/Drive Away
    play sound "audio/sfx/Vehicles/Car Start and Drive Away.ogg"
    
    $renpy.pause(5.0)
    
    jump E1D1S3
