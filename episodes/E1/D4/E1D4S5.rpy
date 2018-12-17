label E1D4S5:
    show mayu hap at l3 with dissolve
    show kaori neu at r3 with dissolve:
            xzoom -1
    show shou hap at cc with dissolve
    if (E1D4S4_FollowMatchPlan == 1):
        play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 1
        "За ареной Сё похлоапл меня по спине, чуть не выбив из равновесия. Даже Маю пожала мне руку. Каори стояла позади, выглядя необычайно задумчивой." 
        voice "audio/voice/E1/D4/S5/Shou/2.ogg"
        show note:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        ss "Это юыло удивительно! Ты там полностью нас спас, братан!" 
        pf "Спасибо!"
        show kaori thi at r3
        show mayu smi at l3
        voice "audio/voice/E1/D4/S5/Kaori/1.ogg"
        ki "Ты был хорош, но только потому, что мы сильно тебе помогли."
        show shou mis at cc
        voice "audio/voice/E1/D4/S5/Shou/3.ogg"
        ss "Ты шутишь? Мы трое выбили двух. Он выбил двоих в соло. Ты должна признать, что он был более чем \"хорош\"."
        show kaori neu at r3
        voice "audio/voice/E1/D4/S5/Kaori/2.ogg"
        ki "По крайней мере ты придерживался плана." 
    
        menu: 
            "Конечно придерживался." :
                pf "Мы ведь договорились об этом ранее."
                show kaori mis at r3
                voice "audio/voice/E1/D4/S5/Kaori/3.ogg"
                ki "Ну, теперь мы знаем, что ты можешь следовать указаниям. Это более чем я могу сказать для Сё."
                show shou thi at cc
                show drop:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S5/Shou/4.ogg"
                ss "Эй!"
    
            "Это потому что я чувствителен к твоим потребностям." :
                pf "Это ведь то, чего ты хотела, не так ли?"
                show kaori ske at r3
                voice "audio/voice/E1/D4/S5/Kaori/4.ogg"
                ki "Ну, да."
                "Я ухмыльнулся."
                pf "Видишь? Я знаю, чего хотят девушки."
                show kaori dis at r3
                show mayu cur at l3
                show shou hap at cc
                show dots:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                "Каори скрестила руки, показывая что её не позабавило, хотя Сё смеялся."
    
            "Это был тупой план." :
                pf "Мы бы справились лучше, если бы я не был в стороне в самого начала."
                show kaori dis at r3
                "Каори нахмурилась."
                voice "audio/voice/E1/D4/S5/Kaori/5.ogg"
                ki "ты серьёзно хочешь сказать, что--"
                show mayu wor at l3
                show shou neu at cc
                voice "audio/voice/E1/D4/S5/Shou/5.ogg"
                ss "Давайте не начинать. Мы не можем изменить то, что уже сделано."
                show kaori ann at r3
                "Каори скрестила руки."
                
        voice "audio/voice/E1/D4/S5/Kaori/6.ogg"
        ki "Мы могли выступить лучше, если бы ты был должным образом экипирован."
        show shou smi at cc
        voice "audio/voice/E1/D4/S5/Shou/6.ogg"
        ss "Я больше не беспокоюсь об этом."
        show kaori dis at r3
        show mayu neu at l3
        voice "audio/voice/E1/D4/S5/Kaori/7.ogg"
        ki "Почему нет?"
        show shou hap at cc
        show shiny:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S5/Shou/7.ogg"
        ss "Потому что у нег оесть это удивительное ядро!"
        voice "audio/voice/E1/D4/S5/Mayu/1.ogg"
        ma "Могу ли я спросить, как ты это сделал?"
        stop music fadeout 3
    else:
        show kaori ann at r3
        "Как только мы вышли с арены Каори повернулась ко мне с яростным выражением на лице."
        show kaori ang
        voice "audio/voice/E1/D4/S5/Kaori/8.ogg"
        ki "О чём, чёрт возьми, ты думал?"
        show kaori ann
        show mayu wor at l3
        show shou ner at cc
        play music "audio/music/Next Time (GAME VERSION).ogg" fadein 1
    
        menu:
            "Я делал то, что считал нужным.":
                pf "Я думал, что помогу вам заработать побольше очков."
                show kaori ang at r3
                show vein:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S5/Kaori/9.ogg"
                ki "Ты с ума сошёл? Из-за твоего безрассудства Сё и Маю были выбиты!"
                show kaori ann at r3
                show shou wor at cc
                pf "Я знал, что будет какой-то риск, но я не мог сидеть сложа руки. Я выбрал шанс, и он окупился. Мы должны набрать самый высокий балл за уничтожение всех ИИ!"
                show kaori dis at r3
                "Каори сильнее нахмурилась."
    
            "Всегда пожалуйста.":
                pf "О том, чтобы поднять нас на самыю вершину."
                show kaori ang at r3
                show exclamation:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S5/Kaori/10.ogg"
                ki "Ты подставил под угрозу всю команду!"
                show kaori ann at r3
                show shou wor at cc
                pf "Да, да, мне жаль, что я в одиночку выбил двух ИИ и дал нам огромный прирост очков."
                show kaori ang at r3
                voice "audio/voice/E1/D4/S5/Kaori/11.ogg"
                ki "Дело не в этом!"
                show kaori ann at r3
                pf "Вообще-то, как раз-таки в этом. Pun intended."
                "Kaori looks dangerously close to bursting a blood vessel."
                show kaori ang at r3
                show vein:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S5/Kaori/12.ogg"
                ki "Арррргх! Почему ты--"
    
            "Никто не загонял меня в рамки!":
                pf "Это так же был и мой бой, я не собирался пропускать его."
                show kaori ang at r3
                show vein:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S5/Kaori/13.ogg"
                ki "Ты вообще слышишь себя сейчас? Этот бой был не только твой. Он был наш!"
                show kaori ann at r3
                show shou wor at cc
                pf "И мы выбили все вражеские GEAR, не так ли? Так в чём проблема?"
                show kaori ang at r3
                show exclamation:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S5/Kaori/14.ogg"
                ki "Проблема в том, что ты подверг остальных опасности!"
                
        show kaori ann at r3 with dissolve
        show mayu ner at l3 with dissolve
        show shou neu at cc with dissolve
        "Сё подошёл к каори, пытаясб успокоить её, а Маю отошла нахад, пристально глядя на землю."
        voice "audio/voice/E1/D4/S5/Shou/8.ogg"
        ss "Каори--"
        "Каори игнорировала Сё и продолжала свою тираду."
        show kaori ang at r3
        show shou ner at cc
        voice "audio/voice/E1/D4/S5/Kaori/15.ogg"
        ki "Ты {i}не сделал{/i} то, что было лучше для команды. Ты сделал то, что было лучше для тебяЮ а Сё и Маю поплатились за твои действия. Ты возможно и заработал нам очков, но мы бы бы заработали больше, если бы половина команды не была разбита."
        voice "audio/voice/E1/D4/S5/Kaori/16.ogg"
        ki "Мы работаем в {i}команде{/i}, а это значит, что мы прикрываем друг друга!"
        show kaori ann at r3
        show shou wor at cc
        pf "И я тоже часть этой команды, что значит, что я не должен оставаться в стороне."
        show kaori ang at r3
        voice "audio/voice/E1/D4/S5/Kaori/17.ogg"
        ki "Ты вообще понимаешь, что оставила тебя в стороне, чтобы избежать того, что произошло? Что бы случилось с тобой, если бы мы не вмешались?"
        show kaori ann at r3
        show mayu sad at l3
        "Я молчал, но демонстративно скрестил руки."
        voice "audio/voice/E1/D4/S5/Kaori/18.ogg"
        ki "Тебя бы выбили. И, честно говоря, тебя должны были выбить."
        show mayu wor at l3
        show shou ang at cc
        show exclamation:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S5/Shou/9.ogg"
        ss "Каори!"
        show kaori ang at r3
        show shou ann at cc
        show vein:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S5/Kaori/19.ogg"
        ki "Что?"
        show kaori ann at r3
        "Она посмотрела на Сё, но заколебалась, когда увидела ожесточённое выражение на его лице."
        show shou ang at cc
        voice "audio/voice/E1/D4/S5/Shou/10.ogg"
        ss "Отстань от парня! Ты видела, что его GEAR сделал там? Это было {i}невероятно{/i}! Мы должны выяснить как он это сделал, а не спорить о том, что должно было случиться."
        show kaori dis at r3
        show shou ann at cc
        show dots:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        "С каждым словом Сё, Каори больше хмурилась."
        show shou dis at cc
        voice "audio/voice/E1/D4/S5/Shou/11.ogg"
        ss "Что сделано, то сделано. Мы выйграли, и как бы тебе не хотелось это признавать, ты знаешь, что по большей части победа была достигнула благодаря ему."
        show kaori ang at r3
        "Каори собралась что-то сказать, но я перебил её прежде, чем она успела. Я так устал слушать её споры."
        show kaori ann at r3
        pf "Маю, что ты думаешь?"
        show mayu sur at l3 with dissolve
        show panic:
            xoffset 230
            yoffset 135
            xzoom .75
            yzoom .75
        "Маю удивлённо подняла голову, и колебалась, прежде чем ответить. Каори и Сё пристально смотрели на неё."
        show mayu ner at l3
        voice "audio/voice/E1/D4/S5/Mayu/2.ogg"
        ma "Эм… Я не хочу доставлять неприятности."
        show shou neu at cc
        voice "audio/voice/E1/D4/S5/Shou/12.ogg"
        ss "Всё в порядке, ты не доставляешь неприятности. Просто скажи нам, что думаешь."
        show mayu neu at l3
        stop music fadeout 5
        voice "audio/voice/E1/D4/S5/Mayu/3.ogg"
        ma "Ну… Я думаю--мы не должны так злиться. Всё-таки мы хорошо выступили, и теперь знаем, что среди нас есть секретное оружие."
        "Каори скрестила руки и неохотно пожала плечами. Затем она повернулась ко мне, её глаза были наполнены любопытством."
        
    show kaori ske at r3
    show question:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S5/Kaori/20.ogg"
    ki "Ладно, что это был за режим максимальной мощности? Почему ты не сказал нам, что можешь такое, когда мы запусками симуляцию?"
    show shou neu at cc
    play music "audio/music/Evening Out (GAME VERSION).ogg" fadein 1
    
    menu:
        "Потому что я не знал.":
            pf "Я бы сказал, если знал об этом."
            show kaori dis at r3
            show storm:
                xoffset 1175
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S5/Kaori/21.ogg"
            ki "Это сарказм?"
            pf "Нет, я удивлён так же, как и вы."
    
        "Ты не спрашивала.":
            "Я ухмыльнулся."
            pf "Ты не спрашивала."
            show kaori dis at r3
            "Каори положила руки на бёдра."
            voice "audio/voice/E1/D4/S5/Kaori/22.ogg"
            ki "Потому что это абсолютно нормально спрашивать, есть ли у людей уникальное ядро, или нет."
            pf "Эй, я не умею читать мысли."
            show kaori ang at r3
            show vein:
                xoffset 1175
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S5/Kaori/23.ogg"
            ki "Хорошо, я спрашиваю сейчас! Что ты сделал со своим ядром?"
            show kaori ann at r3
            "Я снова ухмыльнулся."
            pf "Не скажу."
    
        "Есть вещи посерьёзнее, о которых нужно волноваться.":
            pf "У меня точно не было времени думать о ядре, когда всё оружие пропало!"
            show kaori dis at r3
            show storm:
                xoffset 1175
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S5/Kaori/24.ogg"
            ki "Ты все ещё мог упомянуть, что у тебя есть способность, которая может свести на нет потерю оружия."
            pf "Ну да, я мог… если бы знал о ней."
            
    show kaori ske at r3
    show question:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S5/Kaori/25.ogg"
    ki "Что?"
    show mayu cur at l3
    show shou cur at cc
    "Маю и Сё моргали."
    show shou ske at cc
    show question:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S5/Shou/13.ogg"
    ss "То есть, ты хочешь сказать, что сделал это случайно?"
    pf "В целом… да."
    
    if (E1D4S4_FollowMatchPlan == 0):
        show kaori ann at r3
        voice "audio/voice/E1/D4/S5/Kaori/26.ogg"
        ki "Ну, ты должен знать свой GEAR как свои пять пальцев. Если бы мы знали о твоём ядре, то лучше бы оценили тебя. Я бы не просила тебя стоять в стороне, и у нас бы не было прошлого разговора."
        "Мы оба молчали. Она в чём-то права…"
        show kaori dis at r3
        voice "audio/voice/E1/D4/S5/Kaori/27.ogg"
        ki "Но раз ты не сказал нам--"
        show shou neu at cc
        voice "audio/voice/E1/D4/S5/Shou/14.ogg"
        ss "Каори, не начинай снова…"
        show kaori thi at r3
        stop music fadeout 3
        voice "audio/voice/E1/D4/S5/Kaori/28.ogg"
        ki "Что начинать? Я просто говорю--"
    
    else:
        show shou cur at cc
        voice "audio/voice/E1/D4/S5/Shou/15.ogg"
        ss "Вот это случайность."
        show kaori dis at r3
        voice "audio/voice/E1/D4/S5/Kaori/29.ogg"
        ki "Ты можешь сделать это снова?"
        pf "Не знаю. Можеть быть?"
        show kaori thi at r3
        voice "audio/voice/E1/D4/S5/Kaori/30.ogg"
        ki "Хммм…"
        show dots:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        show shou neu at cc
        stop music fadeout 3
        "Мне не нравилось это задумчивое выражение лица."
        
    show mayu neu at l3
    "Звук интеркома прервал нас."
    voice "audio/voice/E1/D4/S5/ACE Academy Announcer/1.ogg"
    an "Спасибо всем, кто участвовал. Первый этам матчей завершён."
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 1
    show shou hap at cc with dissolve
    "Сё ухмыльнулся"
    show note:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S5/Shou/16.ogg"
    ss "Отлично! Первый раунд завершён. Победная вечеринка у меня дома?"
    show kaori neu at r3
    show mayu smi at l3
    voice "audio/voice/E1/D4/S5/Kaori/31.ogg"
    ki "Прости Сё. Мне другая встреча."
    show shou cur at cc
    voice "audio/voice/E1/D4/S5/Shou/17.ogg"
    ss "Правда? Где?"
    show kaori ann at r3
    voice "audio/voice/E1/D4/S5/Kaori/32.ogg"
    ki "Н-Не твоё дело!"
    show shou mis at cc
    voice "audio/voice/E1/D4/S5/Shou/18.ogg"
    ss "Не то чтобы у тебя были другие друзья--"
    show kaori ang at r3
    voice "audio/voice/E1/D4/S5/Kaori/33.ogg"
    ki "Они есть!"
    show shou cur at cc
    voice "audio/voice/E1/D4/S5/Shou/19.ogg"
    ss "Кто?"
    show kaori ann at r3
    voice "audio/voice/E1/D4/S5/Kaori/34.ogg"
    ki "Ты просто не знаешь их."
    show shou mis at cc
    voice "audio/voice/E1/D4/S5/Shou/20.ogg"
    ss "Потому что их не существует?"
    show kaori ang at r3
    "Каори подняла кулак."
    show vein:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S5/Kaori/35.ogg"
    ki "Я покажу тебе настоящих--"
    "Сё отпрыгнул."
    show kaori ann at r3
    show shou hap at cc
    show drop:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D4/S5/Shou/21.ogg"
    ss "Это была шутка! Извини!"
    show kaori dis at r3 with dissolve
    show kaori neu at r3 with dissolve
    voice "audio/voice/E1/D4/S5/Kaori/36.ogg"
    ki "Плевать. Мне нужно идти, пока я не опоздала. Увидимся, Маю."
    show mayu hap at l3
    "Маю махала, пока Каори не скрылась за углом."
    hide kaori with dissolve
    show mayu smi at l3 with dissolve
    show shou smi at cc with dissolve
    voice "audio/voice/E1/D4/S5/Shou/22.ogg"
    ss "Так, что насчёт вас двоих?"
    "Маю улыбалась, но качала головой."
    voice "audio/voice/E1/D4/S5/Mayu/4.ogg"
    ma "Я бы хотела, но сегодня приезжает отец. Ему будет интересно услышать о сегодняшнем матче."
    show shou hap at cc
    voice "audio/voice/E1/D4/S5/Shou/23.ogg"
    ss "Передай ему \"Привет\" от меня."
    show mayu hap at l3
    show note:
        xoffset 230
        yoffset 135
        xzoom .75
        yzoom .75
    "Она кивнула, попрощалась с нами и ушла."
    hide mayu with dissolve
    show shou mis at cc with dissolve
    voice "audio/voice/E1/D4/S5/Shou/24.ogg"
    ss "Вечеринка вдвоём? Что скажешь?"
    play sound "audio/sfx/Technology/Phone Vibration Once.ogg" fadein 1 fadeout 1
    "Прежде чем я успел ответить, Сё пришло смс."
    show shou cur at cc
    voice "audio/voice/E1/D4/S5/Shou/29.ogg"
    ss "Погоди."
    show shou neu at cc
    "Он быстро прочитал сообшение."
    voice "audio/voice/E1/D4/S5/Shou/25.ogg"
    ss "Вообще-то придётся отложить вечеирнку на другой раз."
    pf "Что такое?"
    show shou thi at cc
    voice "audio/voice/E1/D4/S5/Shou/26.ogg"
    ss "Это Такеши. Он устроил ещё один костёр в мусорном баке."
    pf "Что?!"
    show shou smi at cc
    voice "audio/voice/E1/D4/S5/Shou/27.ogg"
    ss "Ничего особенного. Им просто пришлось эвакуировать всех из здания. Во всяком случае, так как я временно бездомный, я собираюсь потусоваться в центре отдыха."
    pf "Хорошо... Полагаю, тебе сначала нужно разобраться с этим."
    show shou hap at cc
    "Он кивнул."
    voice "audio/voice/E1/D4/S5/Shou/28.ogg"
    ss "Похоже прощания в порядке вещей. Тогда спокойной ночи, мистер братан."
    stop music fadeout 3
    pf "Ага, тебе тоже."
    hide shou with dissolve
    "Просле прощаний я направился на парковку."
    $ kaoOut = "sUniform"
    $ mayOut = "sUniform"
    $ shoOut = "sUniform"
    scene black with fade
    $renpy.pause(2.5)
    
    jump E1D4S6
