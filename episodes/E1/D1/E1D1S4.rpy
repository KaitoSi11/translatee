label E1D1S4:
        
    scene bg homekaito myroom night packed with fade
    "Хорошо, Время распаковки."
    
    play sound "audio/sfx/Impacts/Box Shuffling.ogg" fadein 1 fadeout 1
    
    scene bg homekaito myroom night with Dissolve(3.0)
    $ nikOut = "sSleepwear"
    
    $renpy.pause(1.0)
    "I manage to put most of my things away before I'm interrupted."
    
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 1
    voice "audio/voice/E1/D1/S4/Nikki/1.ogg"
    sf "Ты уже распаковал вещи?"
    
    show nikki neu at r3 with dissolve:
        xzoom -1
    
    "Никки выглядит напряжённой. Не смотря на небольшую улыбку, её брови дрожат от волнения."
    
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
    "Она переминается с ноги на нону uncomfortably."
    
    menu:
        "Я думаю, это отличная идея.":
            pf "Это будет неплохой переменой. И нам не придется беспокоиться о несовпадающих носках или что-то в этом роде." 
            show nikki smi at cc
            "Она хихикает."
            show nikki mis at cc
            voice "audio/voice/E1/D1/S4/Nikki/3.ogg"
            sf "Может с тобой такое и происходит, но мои носки всегда совпадают."
    
        "Без разницы.":
            pf "А это важно? Мы привыкнем."
            show nikki thi at cc
            "Никки смотри в пол."
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
            "For such a small girl, she sure packs a punch."
            "Nikki sighs."
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
    sf "Oh, I almost forgot! What kind of uniform do you have to wear anyway? I mean, mine’s... normal, but you’re going to ACE Academy."
    
    "I shrug."
    
    pf "The dress code says something about distinguishing the students in the pilot program from the rest of the student body. The pilots wear teal markings to indicate their program." 
    
    show nikki cur at cc
    voice "audio/voice/E1/D1/S4/Nikki/7.ogg"
    sf "Ooh, that sounds good. You transferred directly into their pilot program, right?"
    
    pf "Yup." 
    
    show nikki hap at cc
    voice "audio/voice/E1/D1/S4/Nikki/8.ogg"
    sf "I heard that program is hard to get into, but I never doubted you! I hope they're ready for you because you're going to kick butt!"
    
    pf "Thanks, sis."
    
    "The clock on my nightstand flashes 11:00 PM."
    
    pf "I think it's time to go to bed."
    
    show nikki wor at cc
    voice "audio/voice/E1/D1/S4/Nikki/9.ogg"
    sf "What? Already?"
    
    "I gently herd her out of my room."
    show crying:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D1/S4/Nikki/10.ogg"
    sf "But it's not {i}that{/i} late!"
    
    pf "Come on. You don't want to be falling asleep in class now, do you?"
    
    show nikki sad at cc
    show storm:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    "She pouts, and I'm worried she'll continue to argue, but she just mumbles something incoherent and turns towards her room."
    
    pf "Good night."
    
    show nikki smi at cc
    voice "audio/voice/E1/D1/S4/Nikki/11.ogg"
    sf "Night."
    
    hide nikki with dissolve
    play sound "audio/sfx/Impacts/Box Shuffling.ogg" fadein 5 fadeout 5
    
    "I return to my mess of boxes and try to organise them into something resembling a neat pile. {w}As I reach for the last box, a picture frame falls to the ground with a loud clatter. My heart tightens in my chest as I snatch it up and inspect it for any fractures. {w}Luckily, it's unharmed."
    
    
    $ persistent.gpix[0][0] = 1
    
    scene cg mc family photo at Zoom((1920, 1080), (1740, 180, 1920, 1080), (1740, 180, 1920, 1080), 0) with dissolve
    
    "Я провёл пальцем по улыбающимся лицам: я, Никки, мама, папа. {w}Мы были на ярмарке, и Никки хотела покататься на американских горках. {w}Помню, что спорил с мамой о чем-то глупом до того, как была сделана фотография, но по ней вы никогда не сможете сказать этого. Мама всегда выглядела уравновешенной."
    
    scene cg mc family photo at Zoom((1920, 1080), (1740, 180, 1920, 1080), (0, 0, 3840, 2160), 5.0)
    
    "Я положил рамку рядом с компьютером, пытаясь подавить ком в горле."
    
    "Я лёг на кровать и закрыл глаза, но мылсли отказывались уходить. {w}В конце концов усталость берет верх, и я засыпаю среди путаницы вопросов и «что, если», носящихся в голове."
    
    stop music fadeout 3
    stop ambient fadeout 3
        
    scene black with fade
    
    $renpy.pause(1)
    
    jump E1D2S1
