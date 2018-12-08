label E1D2S7:
    
    stop ambient fadeout  3
    scene bg campus parking day with Dissolve(2)
    play ambient "audio/ambience/Parking Lot.ogg" fadein 1
    
    "После довольно короткой поездки я приехал в академию и стал искать место для парковки."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    "Каждое место на этой огромной парковке было занято каким-нибудь транспортом. Видимо, все остальные сегодня тоже приехали.  Серьёзно. Похоже, у каждого студента есть свой транспорт."
    
    "Я был почти готов сдаться, когда увидел... {w}Свободное место."
    
    "Волна головокружительных эмоций чуть не вырвалась из меня. Я практически мог видеть священный луч света, сияющий на нем, сопровождающийся пнгельским хором."
    
    "Я подъехал ближе, и потом замер. В передней части этого места на земле был знак: \"Парковка только для владельцев пропусков\"."
    
    "Ну конечно. Как же мне везёт."
    
    "Тяжело вздохнув, я начал отгонять мотоцикл назад. Полагаю, лучше..."
    
    "Подожди-ка."
    
    "Я снова оглядел парковку. Она полностью лишена жизни, что означает…"
    
    menu:
        "Нет свидетелей.":
            "Если никто не видел, что я занял это место, значит, я не сделал ничего плохого?"
    
            "Отбрасывая все сомнения, я поставил байк на свободное место. Видишь? Ничего плохого не случилось."
    
            "Теперь, пора идти в класс--"
            
            stop music fadeout 3
            play sound "audio/sfx/Vehicles/Bike Revving.ogg" fadein 3 fadeout 3
            "Я обернулся как раз вовремя. Ко мне подъехал другой мотоцикл. Судя по растрепанной форме, парень тоже студент, но яростный хмурый взгляд убеждал меня, что он не собирался заводить друзей." 
            
            play music "audio/music/Stress (GAME VERSION).ogg" fadein 3
            show bully3 extra at cc with dissolve
            show exclamation:
                xoffset 675
                yoffset 50
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S7/Ken/1.ogg"
            kt "Эй! Какого хрена ты делаешь?!"
            voice "audio/voice/E1/D2/S7/Ken/2.ogg"
            kt "Убери эту херню с моего места. Сейчас же!"
    
            "Оскалив зубы, он указал пальцем за собой. Отлично. Отлично. Из всех людей, которые могли бы владеть этим местом, это должен был быть кто-то вроде {i}него{/i}."
            voice "audio/voice/E1/D2/S7/Ken/3.ogg"
            kt "Ты не слышал меня? Вали!"
    
            "Он спрыгнул с байка и пошёл ко мне."
    
            menu:
                "Лучше не встрявать в драку в первый день.":
                    pf "Хорошо, хорошо, дай секудку."
    
                    "Я неохотно убрал байк с места."
    
                    "Как бы мне не было больно отказываться от этого места, я чувствовал, что он не из тех, кто избежит драки. Драка в первый день вряд ли что-то сделает с моей репутацией."
                    "К тому же, это {i}его{/i} место."
                    voice "audio/voice/E1/D2/S7/Ken/4.ogg"
                    kt "... Да, так я и думал."
                    hide bully3 extra with dissolve
                    "Он издевательские усмехнулся прежде чем сел на свой байк"
                    "Полагаю, лучше найти другое место."
                    jump E1D2S7_FarParking
    
                "\"Херню\"? Кто бы говорил!":
                    pf "ПожалуйстаЮ будь так добр расскажи, что ты там назвал кучей болтов?"
    
                    "Его байк едва подходил для дорог. Это древняя, ржавая, смертельная ловушка, которая выглядела так, как будто она передавалась из поколения в поколение, пока наконец, не стала его."
                    voice "audio/voice/E1/D2/S7/Ken/5.ogg"
                    kt "Что ты только что…?"
                    show vein:
                        xoffset 675
                        yoffset 50
                        xzoom .75
                        yzoom .75
                    "Его лицо покраснело. Похоже, я задел за живое."
    
                    pf "Ты слышал. Похоже, что этот металлолом едва удерживается скотчем."
    
                    "Практически дрожа от гнева, он встал так, чтобы его байк не было видно, возможно, он боялся, что я {i}действителньо{/i} замечу на нём скотч."
    
                    "Он похрустел ппытке запугать меня."
                    voice "audio/voice/E1/D2/S7/Ken/6.ogg"
                    kt "You think you're hot shit? Well, you won't look so hot once I'm done with you."
    
                    "He beckons for me to come forward, then raises his fists. I tighten my own fists in response."
                    voice "audio/voice/E1/D2/S7/Ken/7.ogg"
                    kt "Or are you too scared?"
    
                    "I laugh. Scared? Of a worm like him? In one smooth motion, I hop off my bike and saunter towards him."
                    $ E1D2S7_BullyFight = 1
    
                "Tough luck, pal.":
                    "I shrug before dismounting from my bike, but he cuts me off when I try to move past him."
                    show question:
                        xoffset 675
                        yoffset 50
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D2/S7/Ken/8.ogg"
                    kt "You think you can just ignore me?"
    
                    pf "I'm trying to, but you're not making it easy."
                    show vein:
                        xoffset 675
                        yoffset 50
                        xzoom .75
                        yzoom .75
                    "Judging by his deepening scowl and narrowed eyes, I can tell he won't be satisfied until one of us is bleeding on the ground. Great, first that crazy girl and now this douchebag. Today is just not my lucky day."
                    $ E1D2S7_BullyFight = 1
    
            "The tension between us is palpable. I tighten my fists, fueling the fire in his eyes."
    
        "This spot still isn't mine.":
            $ E1D2S7_CleanMove = 1
            "It's still not my spot to take. I'll find parking off-site. {w}Following the signs, I drive my bike past the rows of reserved spaces."
            jump E1D2S7_FarParking
            
    if (E1D2S7_BullyFight == 1):
    
        "He shifts into a fighting stance; his hands are up to protect his face.  He's definitely no stranger to violence. I better not underestimate him. I match his stance, and then--"
    
        $ qtebase = 3
        $ qtetotal = qteath + qtebase
        $ t_var = qtetotal
        show screen timer_scr(place="E1D2S7_FightTImeout")
        
        menu:
        
            "{color=#00ff00}{b}First Blood!{/b}{/color}" if (MCStory == 1):
                jump E1D2S7_FirstBlood
        
            "First Blood!" if (MCStory != 1):
                label E1D2S7_FirstBlood:
                $ renpy.hide_screen ("timer_scr")
                "I slide forward and swing my leg low."
                
                "When his arm moves to block, I catch him off-guard with a roundhouse kick to the head."
                play sound "audio/sfx/Human/Med_Punch.ogg"
                "He flies backwards several feet before tumbling to a stop on the asphalt."
                hide bully3 extra with dissolve
                "Taking my time, I bring my foot back in and take a deep breath."
                "I stroll towards his crumpled body and poke him with a toe."
                play sound "audio/sfx/Human/Poke Noise.ogg"
                "He doesn't stir."
                "Maybe I overestimated him. This guy was hardly worth the effort. Too bad."
    
                "I didn't hit him {i}that{/i} hard, so I'm sure he'll be up in time for class… I think."
                "Exhaling, I stride past his unconscious body, my parking spot safe."
                $ E1D2S7_BullyFightWin = 1
                jump E1D2S8
    
            "Try getting fancy...":
                $ renpy.hide_screen ("timer_scr")
                "Heh, it's a good thing I took those five karate classes when I was ten. This loser doesn't stand a chance when he sees what I can do!"
    
                "When I see an opening, I prepare for an axe kick. Swinging my leg up high, I aim for the soft flesh between his neck and his collarbone, but when my leg gets up to about midriff level, it gets stuck."
                play sound "audio/sfx/Human/light_punch.ogg"
                "My crotch shoots a painful warning, and I lose my balance, landing on my back."
    
                "I've made a terrible mistake. I forgot I'm not as flexible as ten-year-old me."
                "The guy doubles over in laughter, and I grit my teeth, willing myself to push past the pain."
                "Suddenly, a shadow falls on me. I recognise the guard uniform."
                show guard extra at r3 with dissolve:
                    xzoom -1
                voice "audio/voice/E1/D2/S7/Guard/1.ogg"
                gua "What are you doing on the ground?"
                pf "Nothing. I just fell, that's all."
                "The guard looks skeptical and glances at the other guy who nods in confirmation."
                voice "audio/voice/E1/D2/S7/Guard/2.ogg"
                gua "Well, get the hell up then. What are you two doing hanging around in a parking lot anyway?"
                "Wincing, I manage to get back on my feet."
                pf "I just wanted to park my bike."
                voice "audio/voice/E1/D2/S7/Ken/9.ogg"
                kt "Yeah, but in {i}my{/i} spot!"
                voice "audio/voice/E1/D2/S7/Guard/3.ogg"
                gua "We can easily resolve this. Show me your parking passes."
                "The jerk immediately hands his over. I can only sheepishly shake my head."
                pf "I don't have one."
                voice "audio/voice/E1/D2/S7/Guard/4.ogg"
                gua "Then you have no right parking here. Go move your bike to the visitor's lot."
                hide bully3 extra
                hide guard extra
                with dissolve
                "Reluctantly, I wheel my bike away."
                jump E1D2S7_FarParking
    
            "Wait...":
                $ renpy.hide_screen ("timer_scr")
                "I stay crouched with my fists up, waiting for him to make his move. But he doesn’t."
    
                "Instead he dances from foot to foot, tempting me to take a step towards him. I won't take the bait, though; I want him to hit first."
                "He feigns a couple of attacks while I circle him warily."
                voice "audio/voice/E1/D2/S7/Ken/10.ogg"
                kt "What are you waiting for? C'mon!"
    
                "I fake a kick, and grin when he flinches. He still doesn't attack, though. He just matches my circle." 
                voice "audio/voice/E1/D2/S7/Guard/5.ogg"
                gua "Will one of you make the first move? You're wasting my time."
                show guard extra at r3 with dissolve:
                    xzoom -1
                "We both freeze and stare at the burly guard beside us. His arms are crossed over his chest, and his uniform strains around his muscles."
                voice "audio/voice/E1/D2/S7/Guard/6.ogg"
                gua "Well?"
                "The other guy tries to sidestep around the guard but the guard's arm flies out and stops him." 
                voice "audio/voice/E1/D2/S7/Guard/7.ogg"
                gua "Show me your parking passes. Or we can deal with this in my office. Your choice."
                "The guard gives us a hard look. I shake my head as the jerk next to me pulls out a bike pass."
                voice "audio/voice/E1/D2/S7/Ken/11.ogg"
                kt "I’ve got mine right here."
                "The guard examines it, then hands it back to the guy. He looks at me and points over his shoulder."
                voice "audio/voice/E1/D2/S7/Guard/8.ogg"
                gua "Get out of here and stop actually making me do my job. I'm supposed to be on a break right now."
                hide guard extra with dissolve
                "He turns and walks away, grumbling about bratty students. I move to grab my bike, and as I do, I catch the smug look on that jerks face."
                hide bully3 extra with dissolve
                "I say nothing as I wheel my bike from the parking spot and look for somewhere else to park." 
                jump E1D2S7_FarParking
    
            "Play it safe!":
                $ renpy.hide_screen ("timer_scr")
                "The best offence is a good defence. I {i}want{/i} him to strike first. That way I can assess his skill and he'll tire himself out more quickly."
    
                "I shift into a defensive stance and wait. Just as expected, he moves in."
    
                "He lunges and swings his leg towards my face."
                play sound "audio/sfx/Human/light_punch.ogg"
                "I deflect his attack. {w}Although his moves hold power, he lacks speed and agility, which fortunately for me, are my strengths." 
                ##NEW SOUND NEEDED## - (put back in on 05/01/16, but should check if this is alright)
                play sound [ "audio/sfx/Human/light_punch.ogg", "audio/sfx/Human/Med_Punch.ogg", "audio/sfx/Human/light_punch.ogg", "audio/sfx/Human/Med_Punch.ogg"  ]
                "With a frustrated grunt, he strikes again, and again, each punch and kick growing more desperate than the last as he continually fails to hit his target."
    
                "Before long, his face burns red and he's gasping for breath. His attacks become more erratic, and half of them end up nowhere near me. Meanwhile, I've barely broken a sweat."
                show vein:
                    xoffset 675
                    yoffset 50
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S7/Ken/12.ogg"
                kt "Fight me already!"
    
                "I merely smirk at him. He roars with rage, and unsteadily throws another punch, which I easily evade. I wonder how long I can keep this up before he collapses from exhaustion."
    
                "Regardless, this has gone on long enough, and I've got better places to be. I think it's time to wrap things up."
                ##NEW SOUND NEEDED## - (put back in on 05/01/16, but should check if this is alright)
                play sound "audio/sfx/Human/Med_Punch.ogg"
                "When he strikes again, I block his fist with one arm."
                play sound "audio/sfx/Human/Med_Punch.ogg"
                "Then I lean in close and land my own punch straight to his solar plexus. {w}He chokes as the air is knocked out of him, but I don't stop."
                play sound "audio/sfx/Human/light_punch.ogg"
                "Bringing my knee into my chest, I catch him with a side kick, and he crumples to the ground."
                hide bully3 extra with dissolve
                "I wait for him to get up, and when he doesn't, I check my bike to make sure it's okay. Then I walk away."
    
                "He'll be fine… And if not, someone will find him… eventually."
                $ E1D2S7_BullyFightWin = 1
                jump E1D2S8
    
            "Trip...": 
                $ renpy.hide_screen ("timer_scr")
                "I swing my fist towards his face. He steps out of my way at the last minute, but I can't stop the forward momentum."
                play sound "audio/sfx/Human/light_punch.ogg"
                "I try to balance myself but my feet don't seem to work, and I tumble to the ground." 
    
                "I look back up at the guy, who is folded over with laughter. Scrambling to my feet, I ready myself to hit him again, when a strong hand grips my shoulder." 
                show guard extra at r3 with dissolve:
                    xzoom -1
                voice "audio/voice/E1/D2/S7/Guard/9.ogg"
                gua "Alright, time to stop. This is just too painful to watch." 
                "The other guy tries to keep a straight face, but every so often a laugh escapes him."
                voice "audio/voice/E1/D2/S7/Guard/10.ogg"
                gua "What are you laughing about?"
                "He shuts up."
                voice "audio/voice/E1/D2/S7/Guard/11.ogg"
                gua "Both of you show me your parking passes."
                "The jerk pulls out his pass and hands it to the guard. When the guard looks to me I can only shrug." 
                pf "I don't have a pass."
                voice "audio/voice/E1/D2/S7/Guard/12.ogg"
                gua "So you were trying to fight over something that wasn't even yours? Get out of here." 
                "He points a finger over his shoulder towards what I assume to be off campus parking." 
                hide bully3 extra
                hide guard extra
                with dissolve
                "I grab my bike and wheel it out of the spot, wishing I had a pass if only so I could make that guy look like the ass. I can faintly hear the guard scolding him as I head out, which makes me feel a little better… but only a little." 
                jump E1D2S7_FarParking
    
    label E1D2S7_FightTImeout:
        $ renpy.hide_screen ("timer_scr")
        "I freeze, and in that moment of hesitation, a fist collides with my stomach. I cringe, waiting for the inevitable second blow, but nothing happens."
        show guard extra at r3 with dissolve:
            xzoom -1
        "A burly guard restrains the other guy."
        voice "audio/voice/E1/D2/S7/Guard/13.ogg"
        gua "This is a parking lot, not a boxing ring."
        show storm:
            xoffset 675
            yoffset 50
            xzoom .75
            yzoom .75
        "The other guy continues to struggle in vain. Once he realises he can't escape, he calms down and the guard lets him go."
        voice "audio/voice/E1/D2/S7/Guard/14.ogg"
        gua "Do either one of you even belong here? Where are your passes?"
        voice "audio/voice/E1/D2/S7/Ken/13.ogg"
        kt "Here."
        "The guard inspects his pass and nods, then looks expectantly at me."
        voice "audio/voice/E1/D2/S7/Guard/15.ogg"
        gua "Well?"
        pf "I don't have a pass…"
        voice "audio/voice/E1/D2/S7/Guard/16.ogg"
        gua "Then get out of here."
        hide bully3 extra
        hide guard extra
        with dissolve
        "With my stomach twinging in pain, I begin to wheel out my bike. Behind me I can hear the guard yelling."
        voice "audio/voice/E1/D2/S7/Guard/17.ogg"
        gua "What are you smirking about? Park your vehicle and get out of here!"
        "Suddenly, I don't feel so bad."
        jump E1D2S7_FarParking
        
    label E1D2S7_FarParking:
        
        $ E1D2S7_ParkedFar = 1
        stop music fadeout 3
        scene black with fade
        "After what seems like an eternity, I finally find an empty, unmarked spot. I pull in, hop off the bike and glance back the way I came."
        stop ambient fadeout 3
        scene bg campus main day with fade
        play ambient "audio/ambience/Campus.ogg" fadein 1 fadeout 1
        "My heart sinks at how small the grand buildings on campus look. This is not going to be a fun walk back."
        "With no other option, I begin my long trek back to campus and make it back just in time to find my class."
        
        
        jump E1D2S8
