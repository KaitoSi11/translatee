label E1D4S2:
    
    play ambient "audio/ambience/Hangar.ogg" fadein 1
    
    scene bg campus hangar day with fade
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
    if (E1D2S11_JoinedTheTeam == 1):
        "К тому времени, как я пришёл в ангар, команда уже ждала у GEAR'а Сё."
        show mayu smi at l3 with dissolve
        show kaori ann at r3 with dissolve:
            xzoom -1
        show shou neu at cc with dissolve
        "Маю первая заметила меня и легонько помахала. {w}Каори и Сё похоже о чём-то спорили, но Сё заткнул её, когда я пришёл." 
        show shou smi at cc
        pf "Привет парни."
        show kaori neu at r3
        "Каори глянула на меня и кивнула."
        voice "audio/voice/E1/D4/S2/Kaori/1.ogg"
        ki "По крайней мере ты не опоздал." 
        show shou hap at cc
        show exclamation:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Shou/1.ogg"
        ss "Братишка, ты сделал это!"
    
        menu:
            "Я пришёл так быстро, как смог!":
                pf "Я ушел, как только получил твоё сообщение. Большие новости, верно?"
                show shou mis at cc
                voice "audio/voice/E1/D4/S2/Shou/2.ogg"
                ss "Ага! Мы получили назначенное время."
                pf "И когда это?" 
                show kaori thi at r3
                voice "audio/voice/E1/D4/S2/Kaori/2.ogg"
                ki "Позже. Прямо сейчас нам нужно практиковаться."
                pf "Понятно." 
    
            "Йоооу!":
                pf "Конечно, всё что угодно для моего любимого товарища."
                show shou cur with dissolve
                "Сё указал на себя."
                voice "audio/voice/E1/D4/S2/Shou/3.ogg"
                ss "Это же я, да?"
                "Я ухмыльнулся."
                pf "Я позволю вам самим решить."
                show kaori thi at r3 with dissolve
                show dots:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show mayu cur at l3 with dissolve
                show confused:
                    xoffset 230
                    yoffset 135
                    xzoom .75
                    yzoom .75
                "Каори закатила глаза. Маю выглядела смущённой."
                show shou smi at cc
                pf "Раз я здесь, давайте начнём матч."
                show kaori dis at r3
                voice "audio/voice/E1/D4/S2/Kaori/3.ogg"
                ki "Матч будет позже, сейчас нужно практиковаться."
                show mayu smi at l3
                "Я кивнул."
    
            "Выбора особо не было.":
                pf "Да, я получил сообщение. Когда матч?" 
                show kaori thi at r3
                voice "audio/voice/E1/D4/S2/Kaori/4.ogg"
                ki "Позже сегодня. Я хотела сначала попрактиковаться." 
                "Я кивнул."
    
        show kaori mis at r3
        voice "audio/voice/E1/D4/S2/Kaori/5.ogg"
        ki "Хорошо, идите в свои GEARs включи симуляторы. Посмотрим, с чем мы работаем."
                
    elif (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
        show shou smi at cc with dissolve
        "Я встретился с Сё прежде, чем мы встретимся с остальной командой."
        show mayu neu at l3 with dissolve
        show kaori neu at r3 with dissolve:
            xzoom -1
        show shou hap at cc with dissolve
        "Shou smiles sheepishly as we turn to meet the girls."
        voice "audio/voice/E1/D4/S2/Shou/18.ogg"
        ss "Эм, привет Каори… Помнишь, я говорил, что нашёл четвёртого члена команды?"
        show mayu cur at l3
        show kaori sur at r3 with dissolve
        "Каори указала на меня." 
        show kaori ang at r3 with dissolve
        show vein:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Kaori/16.ogg"
        ki "Ни за что. Не этот парень. Я думал, что ты действительно нашёл кого-то полезного."
        show mayu wor at l3
        show kaori ann at r3
        show shou sur at cc
        show panic:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Shou/19.ogg"
        ss "Он полезен!" 
        voice "audio/voice/E1/D4/S2/Kaori/17.ogg"
        ki "Нет."
        show shou ner at cc
        voice "audio/voice/E1/D4/S2/Shou/20.ogg"
        ss "Он полезен тем, что он будет причиной, по которой они позволят нам участвовать в отборочных."
        show mayu neu at l3
        show kaori dis at r3 with dissolve
        "Каори посмотрела на него и ничего не сказала."
        voice "audio/voice/E1/D4/S2/Kaori/18.ogg"
        ki "Мы найдём другого." 
        show mayu wor at l3 with dissolve
        voice "audio/voice/E1/D4/S2/Mayu/3.ogg"
        ma "Больше никого нет." 
        show kaori neu at r3
        show shou cur at cc
        "Сё и Каори повернулись к Маю. Она быстро опустила глаза."
        show mayu ner at l3
        voice "audio/voice/E1/D4/S2/Mayu/4.ogg"
        ma "Если бы были, мы бы уже нашли…"
        show shou smi at cc
        voice "audio/voice/E1/D4/S2/Shou/21.ogg"
        ss "Никогда не слышал более справедливых слов, подруга."
        show mayu smi at l3 with dissolve
        show kaori ann at r3 with dissolve
        "Она застенчиво усмехнулась, но Каори демонстративно скрестила руки"
    
        menu: 
            "Извиниться.": 
                pf "Мне очень жаль за то, как мы встретились, но я знаю, что буду хорошим дополнением к команде." 
                show shou hap at cc
                voice "audio/voice/E1/D4/S2/Shou/22.ogg"
                ss "Видишь, он хороший парень!"
                show kaori dis at r3
                show storm:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S2/Kaori/19.ogg"
                ki "Если бы он был таким хорошим парнем, он бы следовал правилам дорожного движения." 
                show shou smi at cc
                voice "audio/voice/E1/D4/S2/Shou/23.ogg"
                ss "Я уверен, что он обычно так и делает."
                pf "Это был несчастный случай, и я сожалею об этом."
                show shou neu at cc
                voice "audio/voice/E1/D4/S2/Shou/24.ogg"
                ss "Послушай, он уже извинился, и нам нужен еще один член команды. Хочешь участвовать в отборочных или нет?"
                "Каори задумалась."
                show kaori neu with dissolve
                voice "audio/voice/E1/D4/S2/Kaori/21.ogg"
                ki "Хорошо, но тебе лучше делать то, что тебе говорят."
                show shou smi at cc
                pf "По рукам."
    
            "Поверь мне, я единственный парень, который тебе нужен.": 
                pf "Слушай Сё, я именно то, что тебе нужно." 
                show kaori ske at r3
                show question:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S2/Kaori/20.ogg"
                ki "И как ты узнаешь, что мне нужно?" 
                "Я ослепительно улыбнулся ей." 
                show mayu ner b1 at l3 with dissolve
                show shou ner with dissolve
                pf "Я знаю, что нужно каждой женщине."
                show kaori dis at r3
                "Сё легко толкнул меня."
                show shou wor at cc
                show frightful:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S2/Shou/25.ogg"
                ss "Ты играешь с огнём, бро." 
                pf "Я не против сгореть, особенно рыжеволосой." 
                show kaori ann at r3 with dissolve
                "Каори холодно смотрела на меня."
                voice "audio/voice/E1/D4/S2/Kaori/22.ogg"
                ki "Нет, абсолютно нет."
                show mayu wor at l3
                show shou neu at cc
                voice "audio/voice/E1/D4/S2/Shou/26.ogg"
                ss "Да ладно, Каори, он единственный оставшийся человек. Ты хочешь участвовать в отборочных, или нет?"
                "Каори задумалась."
                show kaori dis at r3
                voice "audio/voice/E1/D4/S2/Kaori/23.ogg"
                ki "Ладно! Просто не напортачь."
                show mayu neu at l3
                show shou smi at cc
                pf "Никогда."
    
            "Вам нужен я.": 
                pf "Мы оба хотим одно и то же. Я могу помочь вам получить это." 
                show kaori dis at r3
                voice "audio/voice/E1/D4/S2/Kaori/24.ogg"
                ki "Ты мне не нужен."
                show mayu wor at l3
                pf "Ага, как скажешь."
                show shou neu at cc
                voice "audio/voice/E1/D4/S2/Shou/27.ogg"
                ss "Он прав, Каори." 
                show kaori ann at r3
                show storm:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                "Каори смотрит на Сё смертельным взглядом." 
                show shou ske with dissolve
                show question:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S2/Shou/28.ogg"
                ss "Ты хочешь участвовать в отборочных, или нет? Если ты не примешь его, мы все можем спокойно пойти домой."
                "Она не теряла хмурый вид, но неохотно кивнула."
                show kaori dis at r3 with dissolve
                voice "audio/voice/E1/D4/S2/Kaori/25.ogg"
                ki "Хорошо, ты можешь вступить. Но это ничего не меняет."
                show mayu neu at l3
                show shou smi at cc
                pf "Хорошо." 
    
        show shou hap with dissolve
        voice "audio/voice/E1/D4/S2/Shou/29.ogg"
        ss "Ладно! Вот это уже другое дело." 
        show mayu cur at l3 with dissolve
        show dots:
            xoffset 230
            yoffset 135
            xzoom .75
            yzoom .75
        show kaori neu at r3 with dissolve
        show dots2:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        "Мы трое молча смотрели на него." 
        show shou cur with dissolve
        voice "audio/voice/E1/D4/S2/Shou/30.ogg"
        ss "Или нет."
        show mayu smi at l3
        show kaori thi at r3
        voice "audio/voice/E1/D4/S2/Kaori/26.ogg"
        ki "Хватит тратить время, Сё! Нам нужно практиковаться."
        pf "Что насчёт отборочных?"
        show shou smi at cc
        voice "audio/voice/E1/D4/S2/Shou/31.ogg"
        ss "Об этом позже."
        show kaori mis at r3
        voice "audio/voice/E1/D4/S2/Kaori/27.ogg"
        ki "Нам нужно посмотреть на что ты годишься. Поторопись и залеазй в свой GEAR, чтобы мы начали симуляцию."
        
        
    elif (E1D2S11_JoinedTheTeam == 0) and (E1S2D10_AskedOtherTeams == 1):
        "Сё был внутри ангара, Смотрел на свой GEAR широко улыбаясь. {w}Он посмотрел через плечо и помахал мне." 
        show shou hap at cc with dissolve
        show exclamation:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Shou/4.ogg"
        ss "Привет бро!"
        pf "Привет! Где все?" 
        show shou smi at cc
        voice "audio/voice/E1/D4/S2/Shou/5.ogg"
        ss "Скоро будут. Они не такие быстрые, как ты." 
    
        menu: 
            "Я был недалеко.":
                pf "У меня просто были уроки недалеко отсюда."
                show shou mis at cc
                voice "audio/voice/E1/D4/S2/Shou/6.ogg"
                ss "Круто, девоски скоро прибудут." 
    
            "Это дар." :
                pf "Что могу сказать? Я много в чём хорош."
                show shou mis at cc
                voice "audio/voice/E1/D4/S2/Shou/7.ogg"
                ss "Да, и в чём же?" 
                pf "Возможно, если тебе повезёт, то выяснишь." 
                show shou hap at cc
                "Сё засмеялся."
                show shou mis at cc
                show note:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S2/Shou/8.ogg"
                ss "К счастью девушки этого не слышали."
    
            "Я готов к отборочным.":
                pf "Когда матч?"
                show shou mis at cc
                voice "audio/voice/E1/D4/S2/Shou/9.ogg"
                ss "Вау, кто-то нетерпелив. Давайте подождем остальную часть команды, чтобы мы могли поговорить об этом вместе." 
                pf "Окей." 
    
        pf "ты уже говорил с остальной частью команды?" 
        show shou thi at cc with dissolve
        show drop:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Shou/10.ogg"
        ss "Ну, насчёт этого--"
        "Внезапно, мы услышали голос позади нас."
        show mayu neu at l3 with dissolve
        show kaori neu at r3 with dissolve:
            xzoom -1
        show shou neu at cc
        voice "audio/voice/E1/D4/S2/Kaori/6.ogg"
        ki "Сё, это новый член команды, о котором ты говорил?" 
        show kaori ske at r3 with dissolve
        "Она взглянула на меня, затем вздохнула."
        voice "audio/voice/E1/D4/S2/Kaori/7.ogg"
        ki "Полагаю, ты подойдёшь."
        show shou mis at cc
        pf "Спасибо?"
        show mayu smi at l3
        voice "audio/voice/E1/D4/S2/Shou/11.ogg"
        ss "Видишь? Я говорил, что он тебе понравится!"
        show kaori thi at r3
        show drop:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Kaori/8.ogg"
        ki "Не то чтобы мы купались в предложениях."
        show shou hap at cc
        "Сё игнорировал её ихлопнул меня по спине."
        show kaori neu at r3
        show note:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Shou/12.ogg"
        ss "Добро пожаловать на борт, братишка!"
        "Он указывает на темноволосую девушку, которая слегка улыбалась мне."
        show shou smi at cc
        voice "audio/voice/E1/D4/S2/Shou/13.ogg"
        ss "Это Маю. Последний член нашей команды."
    
        if (E1D2S4_MayuGaveDirections == 1):
            "Она выглядит знакомо…"
            pf "Точно! ты же пилот, которая показала мне направление."
            show mayu hap b1 at l3 with dissolve
            show regBlush:
                xoffset 230
                yoffset 135
                xzoom .75
                yzoom .75
            "Она кивнула, и её улыбка расширилась."
            voice "audio/voice/E1/D4/S2/Mayu/1.ogg"
            ma "Похоже это очень помогло." 
            show mayu smi at l3 with dissolve
            pf "Да, ещё раз спасибо."
    
        else:
            "Она кивнула."
            voice "audio/voice/E1/D4/S2/Mayu/2.ogg"
            ma "Рада что ты в нашей команде."
    
        pf "Спасибо! Так, что теперь?"
        show kaori mis at r3
        voice "audio/voice/E1/D4/S2/Kaori/9.ogg"
        ki "Теперь мы практикуемся."
        show mayu neu at l3
    
        menu: 
            "Что насчёт матча?":
                pf "Разве уже не время отборочных?"
                show kaori neu at r3
                voice "audio/voice/E1/D4/S2/Kaori/10.ogg"
                ki "Нет, сегодня позже, и мы должны сначала проверить твои умения." 
                pf "Понятно."
    
            "Взять инициативу!": 
                pf "Отлично! Я покажу вам парочку своих движений." 
                show kaori dis at r3
                voice "audio/voice/E1/D4/S2/Kaori/11.ogg"
                ki "Нет, ты будешь позади." 
                pf "Раз так хочешь… Я могу работать позади." 
                show shou hap at cc with dissolve
                voice "audio/voice/E1/D4/S2/Shou/14.ogg"
                "Сё фыркнул."
                show mayu cur b1 at l3
                show kaori ann at r3
                show question:
                    xoffset 230
                    yoffset 135
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S2/Kaori/12.ogg"
                show vein:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                ki "Что?!"
                show shou smi at cc
                voice "audio/voice/E1/D4/S2/Shou/15.ogg"
                ss "Ничего."
                show mayu neu at l3
                show kaori neu at r3
    
            "Не хочк тратить время.":
                pf "Когда наши отборочные?"
                voice "audio/voice/E1/D4/S2/Shou/16.ogg"
                ss "Сегодня позже." 
                pf "Насколько позже?"
                show kaori neu at r3
                voice "audio/voice/E1/D4/S2/Kaori/13.ogg"
                ki "Достаточно поздно, чтобы у нас было время попрактиковаться. Мне нужно оценить твои умения, чтобы я знала, с чем мы работаем."
                pf "Хорошо."
    
        show shou hap at cc with dissolve
        "Сё посмотрел на нас всех, затем широко улыбнулся." 
        voice "audio/voice/E1/D4/S2/Shou/17.ogg"
        ss "Отлично, мы в деле! Сделаем это."
        show mayu smi at l3
        show kaori thi at r3
        "Маю прятала улыбку, а Каори закатила глаза."
        voice "audio/voice/E1/D4/S2/Kaori/14.ogg"
        ki "Хватит тратить время. Залезайте в свои GEAR и начинайте симуляцию."
        
    
    jump E1D4S3
