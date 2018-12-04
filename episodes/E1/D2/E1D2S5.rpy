label E1D2S5:

    stop music fadeout 3
    voice "audio/voice/E1/D2/S5/Receptionist/1.ogg"
    "Секретать" "Следующий!"
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
    "Очередь спокойно ползёт, и вот наконец, когда вроде бы прошла вечность, я подошёл к стойке." 
    show receptionist extra at cc with dissolve
    pf "Hi, I need a parking pass for a motorcycle--"
    voice "audio/voice/E1/D2/S5/Receptionist/2.ogg"
    "Секретать" "Вам нужно заполнить запрос онлайн на сайте. Подтверждение занимает от одной до двух недель, и если его одобрят, то пропуск отправят вам по почте."
    "Прежде чем я успел ответить, он посмотрел за меня."
    voice "audio/voice/E1/D2/S5/Receptionist/3.ogg"
    "Секретать" "Следующий!" 
    pf "Подожди-ка!"
    "Я положил руки на стол."
    
    "Он сердито посмотрел на меня."
    voice "audio/voice/E1/D2/S5/Receptionist/4.ogg"
    "Секретать" "Что?"
    
    menu:
        "Подкупить его.":
            pf "Я надеялся, что этот процесс мог бы пройти быстрее."
            "Я наклонился и ослепил его самой очаровательной улыбкой."
            pf "Вы кажетесь разумным человеком. Вы уверены, что мы не можем… {i}договориться{/i}?"
            show storm:
                xoffset 675
                yoffset 25
                xzoom .75
                yzoom .75
            $renpy.pause(1)
            "He narrows his eyes."
            voice "audio/voice/E1/D2/S5/Receptionist/5.ogg"
            "Секретарь" "Что именно ты предлагаешь?"
            menu:
                "Предложить подкупить его деньгами (1).":
                    "Я что-то написал в ближайшем листе и предложил его перевёрнутым секретарю. Он подозрительно посмотрел на меня. Я дважды кивнул с уверенной ухмылкой."
                    pf "Я уверен, сумма более чем щедра, сэр."
                    "Он осторожно перевернул бумагу…  и его выражение померкло."
                    voice "audio/voice/E1/D2/S5/Receptionist/6.ogg"
                    "Секретарь" "Тут написано {i}один{/i} credit."
                    "Я дважды коснулся своего носа и подмигнул."
                    "Он смял лист и бросил его в мусорную корзину."
                    voice "audio/voice/E1/D2/S5/Receptionist/13.ogg"
                    "Секретарь" "Следующий!"
    
                    menu:
                        "Время предложить {i}два{/i} credits!":
                            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 2
                            pf "Стоп! Подождите-ка. Слушай, ты ведешь жесткую сделку… но я сыграю в эту игру."
                            "Я что-то написал на другом листочке, прежде чем перевернул его. Он перевернул его, быстро взглянул, затем шлёпнул им по стойке. Внезапно он встал на ноги, его глаза были раскаленны."
                            show vein:
                                xoffset 675
                                yoffset 25
                                xzoom .75
                                yzoom .75
                            voice "audio/voice/E1/D2/S5/Receptionist/7.ogg"
                            "Секретарь" "Проваливай!"
                            "Я поднял руки."
                            pf "Воу, успокойся."
                            voice "audio/voice/E1/D2/S5/Receptionist/8.ogg"
                            "Секретарь" "Не говори мне успокоиться!"
                            pf "Знаете что? Я прекращаю переговоры до тех пор, пока вы не будете более уравновешенным."
                            hide receptionist extra with dissolve
                            stop music fadeout 1
                            "Я спокойно отошёл от стойки, прежде чем он успел ответить. Я слышал его ярость, по коллеги успокаивали его. Боже, почему он так вспылил? Думаю, я просто заполню документы онлайн, дома вечером."
                            play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
                            if (E1D2S2_YuunaComesWithYouPass == 0):
                                jump E1D2S5_NoYuunaJump
    
                            elif (E1D2S2_YuunaComesWithYouPass == 1):
                                jump E1D2S5_YesYuunaJump
    
                        "Просто предлоить ему 50 credits.":
                            jump E1D2S5OfferFifty
    
                        "Это безнадёжно.":
                            pf "Alright, whatever."
                            "Бесполезно продолжать, если он даже не ценит {i}целый{/i} й credit. Просто заполню документы онлайн."
                            hide receptionist extra with dissolve
                            "Я ушёл."
                            if (E1D2S2_YuunaComesWithYouPass == 0):
                                jump E1D2S5_NoYuunaJump
    
                            elif (E1D2S2_YuunaComesWithYouPass == 1):
                                jump E1D2S5_YesYuunaJump
    
                "Предложить взятку суммой 50 credits.":
                    label E1D2S5OfferFifty:
                        $ E1D2S5_offer50directly = 1
                        "Я набросал сумму на листе и предложил его ему перевёрнутым."
                        "Он взглянул на письмо, потом нахмурился на меня, но выдержал его взгляд."
                        pf "Либо бери, либо отказывайся."
    
            if (E1D2S5_offer50directly == 1):
                "Он кивнул."
                voice "audio/voice/E1/D2/S5/Receptionist/11.ogg"
                "Секретарь" "Хорошо."
    
            if (E1D2S5_offer50directly == 0):
                "Он продолжал смотреть на меня, его подозрение росло, но я отказывался сдаваться. Через несколько секунд он кивнул."
                voice "audio/voice/E1/D2/S5/Receptionist/9.ogg"
                "Секретарь" "Это более приемлемо."
    
            "Он что-то напечатал на компьютере, потом открыл ящик и положил пластиковую карточку на стойку."
    
            $ E1D2S5_bribedforpass = 1
            $ E1D2S5_gotbikepass = 1
            voice "audio/voice/E1/D2/S5/Receptionist/10.ogg"
            "Секретарь" "Вот твой пропуск. Если потеряешь, то придётся платить за замену. Чем-то ещё могу помочь?"
            pf "Нет, спасибо."
            voice "audio/voice/E1/D2/S5/Receptionist/13.ogg"
            "Секретарь" "Следующий!"
            hide receptionist extra with dissolve
            "Я положил пропуск в кошелёк и направился к выходу. Это один способ добиваться цели."
            if (E1D2S2_YuunaComesWithYouPass == 0):
                jump E1D2S5_NoYuunaJump
    
            elif (E1D2S2_YuunaComesWithYouPass == 1):
                jump E1D2S5_YesYuunaJump
    
    
        "Кем он себя возомнил?":
            "Я выпрямился и посмотрел на него."
            pf "Мне кажется, вы меня не услышали. Я хочу пропуск на парковку."
            voice "audio/voice/E1/D2/S5/Receptionist/12.ogg"
            "Секретарь" "А я хочу встретить пилота, который не будет самовлюблённым мудаком. Похоже, мы не получим то, чего хотим."
            "Он посмотрел за меня прежде, чем я успел ответить."
            voice "audio/voice/E1/D2/S5/Receptionist/13.ogg"
            "Секретарь" "Следующий!"
    
            menu:
                "Он реально меня бесит.":
                    "Я сжал руки в кулаки и ударил по стойке."
                    pf "Слушай, ты самодовольный--"
                    voice "audio/voice/E1/D2/S5/Security/1.ogg"
                    "Охрана" "Проблемы?"
                    show guard extra at l3 with dissolve
                    "Надо мной навис крепкий охранник. На его лице был шрам, проходящий через глаз до подбородка."
                    pf "Проблемы? Нет, конечно же нет."
    
                    "Секретать довольно узмыльнулся и смотрел на меня, пока разговаривал с охранником."
                    voice "audio/voice/E1/D2/S5/Receptionist/14.ogg"
                    "Секретарь" "Он как раз собирался уходить."
                    "Я продолжал смотреть на него, пока он не перестал улыбаться и не отвёл глаза. Я легко улыбнулся."
                    pf "Да, как раз собирался."
                    "Под ледяным взглядом охранника, обжигающим спину, я беззаботно ушёл от стойки."
                    hide guard extra
                    hide receptionist extra
                    with dissolve
                    if (E1D2S2_YuunaComesWithYouPass == 0):
                        jump E1D2S5_NoYuunaJump
    
                    elif (E1D2S2_YuunaComesWithYouPass == 1):
                        jump E1D2S5_YesYuunaJump
    
                "Забудь, это бесполезно.":
                    pf "Плевать."
                    "Этот парень придурок. Я просто заполню документы онлайн, или приду потом, когда там будет сидеть более разумный человек."
                    hide receptionist extra with dissolve
                    if (E1D2S2_YuunaComesWithYouPass == 0):
                        jump E1D2S5_NoYuunaJump
    
                    elif (E1D2S2_YuunaComesWithYouPass == 1):
                        jump E1D2S5_YesYuunaJump
    
    
        "Давай поговорим об этом.":
            pf "Таааааак…"
    
            "This is another one of those moments where I wish I had thought before speaking."
            "He waits for me to finish, but I can see the impatience building in his eyes. {w}It's now or never!"
    
            menu:
                "Flirt with him.":
                    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 2
                    "I offer him my best \"come hither\" look. He instinctively leans away from me. Not exactly the reaction I was going for, but I can work with it."
                    show question:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    "I lock eyes with him and grin flirtatiously. He leans further back, confused."
    
                    pf "Has anyone ever told you you have very pretty eyes?"
                    "His cheeks turn a faint pink, but his frown deepens as he looks behind me."
                    voice "audio/voice/E1/D2/S5/Receptionist/15.ogg"
                    "Секретарь" "Слушай, у меня нет времени на это--"
    
                    "I step back in his line of sight. My grin widens and I wiggle my eyebrows."
    
                    pf "Aw come on, cutie. Now you're just teasing me. Your voice… it's like angels singing."
                    show shoBlush:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D2/S5/Receptionist/16.ogg"
                    "Секретарь" "Ч-Что?!"
    
                    "His face flushes deep red and he opens and closes his mouth as if trying to find the right words to say."
    
                    pf "You sure are adorable when you're all flustered."
    
                    "I wink at him."
                    show tsuBlush:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D2/S5/Receptionist/17.ogg"
                    "Секретарь" "I--You!--What?--Why??--This--Here, just take it!"
    
                    $ E1D2S5_gotbikepass = 1
                    $ E1D2S5_flirtforpass = 1
                    "He violently pulls open a drawer and flings a plastic card at me before slamming it shut. I take it with a playful smile."
    
                    pf "Thank you."
                    stop music fadeout 4
                    "I wink and blow him a kiss, and he quickly looks down. I turn around and walk away as he grumbles to himself. {w}After a few seconds, he realizes there's still a line of students waiting."
                    hide receptionist extra with dissolve
                    "Yup, still got it."
                    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
                    if (E1D2S2_YuunaComesWithYouPass == 0):
                        jump E1D2S5_NoYuunaJump
    
                    elif (E1D2S2_YuunaComesWithYouPass == 1):
                        jump E1D2S5_YesYuunaJump
    
                "Try and be reasonable.":
                    pf "That's such a complicated process for something so simple. There must be an easier way."
                    show storm:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    "The man taps the desk with his finger."
                    voice "audio/voice/E1/D2/S5/Receptionist/18.ogg"
                    "Секретарь" "There isn't. If you have an issue with this process, you can send a complaint online."
    
                    pf "It's just a bike pass."
                    voice "audio/voice/E1/D2/S5/Receptionist/19.ogg"
                    "Секретарь" "I don't have time for this."
    
                    "He tries to look around me, but I block him."
    
                    pf "Come on!"
    
                    "I hold his gaze. Just when I think he's about to give in, his expression hardens."
                    show vein:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D2/S5/Receptionist/20.ogg"
                    "Секретарь" "Nope. Next!"
                    hide receptionist extra with dissolve
                    "I sigh in resignation. There's no getting through to him, so I turn around and start to head out."
                    if (E1D2S2_YuunaComesWithYouPass == 0):
                        jump E1D2S5_NoYuunaJump
    
                    elif (E1D2S2_YuunaComesWithYouPass == 1):
                        jump E1D2S5_YesYuunaJump
    
                "Make up an elaborate sob story.":
                    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 2
                    "I sniffle."
    
                    pf "I… I lost my pass in the most horrible way…"
                    show question:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    "I bury my face in my hands. {w}After a few seconds, I peek through my fingers. He looks at me with both irritation and confusion. I add another muffled sob for good measure, and he sighs."
                    voice "audio/voice/E1/D2/S5/Receptionist/21.ogg"
                    "Секретарь" "And how could that have possibly happened?"
    
                    "I drop my hands, all signs of distress wiped clean from my face. He blinks in surprise, and narrows his eyes at my complete change in demeanor."
    
                    pf "Well… I was on my way to school, minding my own business, when all of a sudden everything became dark. While everyone's paused in their tracks, I keep walking. By the time I notice something's wrong, there's a spaceship right above me. A bright light shines down from the ship and everything turns blindingly white. Next thing I know, I'm inside the spaceship and surrounded by aliens."
                    show drop:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    pf "Somehow, we manage to communicate and understand each other. They take me around on their spaceship, showing me every single part of it. I actually got to meet every alien on board. They told me they came to Earth to strike a deal with our ruler so we could become allies. Apparently there's going to be an intergalactic war happening in the near future. I told them we don't have a ruler for our planet, and that each country has a different person in charge."
    
                    pf "Somehow that devolved into a debate about which happened first, the chicken or the egg, until they finally admitted they actually didn't know what a chicken or egg was. I actually had to draw a picture for them, and I'm not the greatest artist, so they still don't know what they are--well they figured out what an egg is because that's kind of hard to mess up, even for me."
    
                    pf "Then I realized what time it was and told them I had to go to school or I would be late."
                    show storm:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    pf "They wanted to exchange something as a memento and really wanted my brain, but I told them I needed it to survive. So they said they had the perfect solution. They brought out a probe, and even though I tried to fight it--well, I'd rather not get into it…" 
    
                    "I hang my head at my traumatising \"memory\", but peek at the administrator out of the corner of my eye. He stares, dumbfounded."
    
                    pf "Anyway, after that extremely uncomfortable and overly personal experience, I'm looking for a way to jump out of this ship without killing myself, when my bike pass falls out of my pocket, out of the ship, and into oblivion! Then everything went black and I found myself right in front of the school… {w}And now, here I am."
                    show dots:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    "He closes his mouth and frowns."
                    voice "audio/voice/E1/D2/S5/Receptionist/22.ogg"
                    "Receptionist" "... Are you done?"
    
                    "I nod."
                    voice "audio/voice/E1/D2/S5/Receptionist/23.ogg"
                    "Receptionist" "Great. Next!"
                    stop music fadeout 2.0
                    "I stand there flabbergasted. How could my totally plausible story not impress him?"
                    "Oh well. {w}This guy wouldn't know a good story even if he were a part of it."
                    hide receptionist extra with dissolve
                    "I turn around and head out."
                    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
                    if (E1D2S2_YuunaComesWithYouPass == 0):
                        jump E1D2S5_NoYuunaJump
    
                    elif (E1D2S2_YuunaComesWithYouPass == 1):
                        jump E1D2S5_YesYuunaJump
    
                "My dog ate it.":
                    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 2
                    "Suddenly, my mind goes blank. I rub the back of my head with my hand, stalling for time."
    
                    pf "I… Uh…"
    
                    "He narrows his eyes. As his gaze moves to the student behind me, I blurt out the first thing that comes to my mind." 
    
                    pf "My dog ate it!"
                    show dots:
                        xoffset 675
                        yoffset 25
                        xzoom .75
                        yzoom .75
                    $renpy.pause(2.5)
                    voice "audio/voice/E1/D2/S5/Receptionist/24.ogg"
                    "Receptionist" "…Your dog ate your pass."
    
                    pf "Um, yeah."
                    voice "audio/voice/E1/D2/S5/Receptionist/25.ogg"
                    "Receptionist" "Is it okay?"
    
                    pf "Well, I assume not. It's in my dog."
                    voice "audio/voice/E1/D2/S5/Receptionist/26.ogg"
                    "Receptionist" "Not the pass; your {i}dog{/i}. Is your dog okay?"
    
                    pf "Oh, uh, yeah. Of course. My dog's fine."
                    voice "audio/voice/E1/D2/S5/Receptionist/27.ogg"
                    "Receptionist" "Good. Next!"
    
                    pf "Hey, wait a minute! What about my pass?"
                    voice "audio/voice/E1/D2/S5/Receptionist/28.ogg"
                    "Receptionist" "Maybe your dog can give it back to you."
    
                    "The smile he flashes me doesn't reach his eyes." 
                    voice "audio/voice/E1/D2/S5/Receptionist/13.ogg"
                    "Receptionist" "Next!" 
                    hide receptionist extra with dissolve
                    "I sigh. Well, that didn't work. Defeated, I turn around and start to head out."
                    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
                    if (E1D2S2_YuunaComesWithYouPass == 0):
                        jump E1D2S5_NoYuunaJump
    
                    elif (E1D2S2_YuunaComesWithYouPass == 1):
                        jump E1D2S5_YesYuunaJump
    
    
    if (E1D2S2_YuunaComesWithYouPass == 1):
        label E1D2S5_YesYuunaJump:
            if (E1D2S5_gotbikepass == 0):
                show yuuna smi at cc with dissolve
                "Suddenly Yuuna is beside me. Her smile falters when she sees my face."
                show yuuna neu at cc
                voice "audio/voice/E1/D2/S5/Yuuna/1.ogg"
                ym "Is everything okay?"
    
                "I shrug."
    
                pf "I wasn't able to get a pass."
                show yuuna thi at cc
                "She frowns. Her eyebrows knit delicately together."
                show yuuna neu at cc
                voice "audio/voice/E1/D2/S5/Yuuna/2.ogg"
                ym "Hmm… hold on."
                hide yuuna with dissolve
                "She walks straight to the desk, much to the dismay of the student in line. The man seems nervous by her approach."
    
                "I can't hear what she says, but he looks ashamed and withdraws the pass from a drawer. As she plucks the pass from his fingers, she thanks him with a slight bow of her head, which he returns."
                show yuuna smi at cc with dissolve
                "Yuuna returns with a soft smile on her face and holds out the pass."
                voice "audio/voice/E1/D2/S5/Yuuna/3.ogg"
                ym "Here you go."
    
                "How on earth did she do that? Maybe she used magic. Or those hypnotic eyes of hers--"
                
                show yuuna ner at cc
                voice "audio/voice/E1/D2/S5/Yuuna/4.ogg"
                ym "Um…"
    
                "Right. The pass."
    
                pf "Oh, yeah. Thanks."
                
                show yuuna smi at cc
    
                $ E1D2S5_gotbikepass = 1
                "She smiles."
                voice "audio/voice/E1/D2/S5/Yuuna/5.ogg"
                ym "No problem at all."
    
                "I take it from her and put it in my wallet. We head out as another flood of students enter the office."
                
    
            elif (E1D2S5_gotbikepass == 1):
                show yuuna smi at cc with dissolve
                "Suddenly, I see Yuuna's smiling face."
                voice "audio/voice/E1/D2/S5/Yuuna/6.ogg"
                ym "How did it go?"
    
                pf "I got the pass without any problems."
                show exclamation:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                show yuuna sur at cc
                "Her eyes grow wide."
    
                pf "What is it?"
                show yuuna hap at cc
                voice "audio/voice/E1/D2/S5/Yuuna/7.ogg"
                ym "Oh, nothing. I'm just a little surprised you got the pass so easily. They usually push you to fill out the online form."
    
                if (E1D2S5_bribedforpass == 1):
                    pf "What can I say? I'm resourceful."
                    show yuuna cur at cc
                    voice "audio/voice/E1/D2/S5/Yuuna/8.ogg"
                    ym "Ah... Interesting."
    
                elif (E1D2S5_flirtforpass == 1):
                    "I wink at her."
                    pf "I have a way with words."
                    show yuuna cur at cc
                    voice "audio/voice/E1/D2/S5/Yuuna/9.ogg"
                    ym "I see..."
                    
                show dots:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                "She seems like she's unsure how to react."
                pf "Shall we get going?"
                show yuuna smi at cc
                "She nods. We head out as another flood of students enter the office."
    
            stop music fadeout 3
            hide yuuna with dissolve
            scene bg campus building day with fade
            play ambient "audio/ambience/Campus.ogg" fadein 3
            
            "There seem to be fewer students milling around outside and more hurrying towards classes. I check the time.Twenty-five minutes until class starts."
            play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
            show yuuna smi at cc
            voice "audio/voice/E1/D2/S5/Yuuna/10.ogg"
            ym "Do you know where your first class is?"
    
            pf "Yeah, it's here."
    
            "I show her the campus map on my phone. A small flashing light indicates where I need to be."
            
            show yuuna hap at cc
            voice "audio/voice/E1/D2/S5/Yuuna/11.ogg"
            ym "Oh, that's close by! I can walk there with you."
    
            pf "That would be great."
            
            scene bg campus main day with fade
            
            "We head down one of the narrower paths. It leads straight to a regal-looking building with tall, arching windows. Only a few students are meandering about."
            show yuuna smi at cc with dissolve
            voice "audio/voice/E1/D2/S5/Yuuna/12.ogg"
            ym "This is it."
    
            pf "Thanks, you've been a big help."
            show yuuna smi at cc
            voice "audio/voice/E1/D2/S5/Yuuna/13.ogg"
            ym "It's no problem at all."
    
            pf "And you're off to Psychology?"
            voice "audio/voice/E1/D2/S5/Yuuna/14.ogg"
            ym "Mhm."
    
            pf "What other classes do you have this semester?"
            
            show yuuna thi at cc
            voice "audio/voice/E1/D2/S5/Yuuna/15.ogg"
            ym "Um..."
    
            "She pulls out her phone. I do the same, and we study each other's schedule."
    
            show yuuna smi at cc
            voice "audio/voice/E1/D2/S5/Yuuna/16.ogg"
            ym "Well, it looks like we have History of Robotics together on Friday."
    
            pf "I guess that means we'll be seeing a lot more of each other."
            
            show yuuna hap at cc with dissolve
    
            "We both exchange smiles."
    
            "I notice the time on my phone. Fifteen minutes until class."
            
            show yuuna smi at cc
    
            pf "My class is starting soon."
    
            "Yuuna peers at her phone before tucking it back into her pocket."
            
            show yuuna cur at cc
            voice "audio/voice/E1/D2/S5/Yuuna/17.ogg"
            ym "Oh, right! I have to go or I'll be late. See you Friday?"
    
            "I nod, and we go our separate ways."
            hide yuuna with dissolve
            "After a few steps, I realise I don't have any way to contact her apart from our Friday class. I turn around, but she's already a good distance away."
    
            $ qtebase = 5
            $ qtetotal = qteintel + qtebase
            $ t_var = qtetotal
            show screen timer_scr(place="E1D2S5_YuunaNoNumber")
            menu:
                "Ask for her phone number.":
                    $ renpy.hide_screen ("timer_scr")
                    $ E1D2S5_GotYuunasNumber = 1
                    pf "Wait, Yuuna!"
                    # maybe show her at a distance?
                    show yuuna cur at cc with dissolve:
                        xzoom -0.75
                        yzoom 0.75
                    "She freezes."
                    show question:
                        xoffset 720
                        yoffset 100
                        xzoom .5
                        yzoom .5
                    voice "audio/voice/E1/D2/S5/Yuuna/18.ogg"
                    ym "Yes?"
                    pf "Do you think I can get your number?"
                    show shoBlush:
                        xoffset 720
                        yoffset 100
                        xzoom .5
                        yzoom .5
                    show yuuna sur b1 at cc with dissolve
                    "She seems surprised. Wait, that definitely didn't come out right."
                    pf "Sorry, I mean, I might have a question or two while trying to navigate around ACE Academy and could use your help--that is, if you don't mind me bugging you."
                    show yuuna hap at cc with dissolve
                    "She giggles and nods."
                    voice "audio/voice/E1/D2/S5/Yuuna/19.ogg"
                    ym "Sure."
                    "I jog over to her and we exchange numbers."
                    show yuuna smi at cc
                    pf "Thanks. See you on Friday!"
                    voice "audio/voice/E1/D2/S5/Yuuna/20.ogg"
                    ym "Okay, see you then."
                    hide yuuna with dissolve
    
                "Let it go.":
                    label E1D2S5_YuunaNoNumber:
                        $ renpy.hide_screen ("timer_scr")
                        "Let it go. {w}Let it go. {w}Can't ask for her number anymore."
                        "She's already too far away. I'll talk to her on Friday."
                        
        "I watch as she disappears around the corner."
    
    
    if (E1D2S2_YuunaComesWithYouPass == 0):
        label E1D2S5_NoYuunaJump:
            scene bg campus building day with fade
            "As I exit the administrative building, I check the time on my phone. Fifteen minutes left before my first class. I should start making my way there."
    
    
    jump E1D2S8
