label E1D1S3:
    
    #Ambience Suburbs
    pf "..."
    
    $renpy.pause(1)
    voice "audio/voice/E1/D1/S3/Kaito/2.ogg"
    hk "Добро пожаловать домой!"
    
    play ambient "audio/ambience/Night Crickets.ogg" fadein 1
    scene white with fade
    scene bg homekaito main night with Dissolve(2.5)
    $renpy.pause(1)
    
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 1
    
    "Это место отличается от уютной, но тесной квартиры, которую я ожидал. Вместо этого, я чувствую, что я только что вошел в обложку журнала домашнего декора."
    
    show kaito smi at r2 with dissolve:
        xzoom -1
    voice "audio/voice/E1/D1/S3/Kaito/3.ogg"
    hk "Вы голодны? Скоро должны привезти ужин."
    
    show nikki hap at l2 with dissolve
    voice "audio/voice/E1/D1/S3/Nikki/1.ogg"
    sf "Классно! Что у нас будет?"
    show kaito mis at r2
    voice "audio/voice/E1/D1/S3/Kaito/4.ogg"
    hk "Ну, Я подумал, что было бы неплохо показать вам {i}настоящую{/i} японскую кухню!"
    pf "Какую же?"
    show kaito hap at r2
    voice "audio/voice/E1/D1/S3/Kaito/5.ogg"
    hk "Суши, конечно! 100\% настоящие {i}нигири суши и маки суши{/i}!"
    show kaito smi at r2
    
    $ E1D1S3_mcdoesntlikesushi = 0
    
    menu:
        "Sushi!":
            pf "Отлично, я люблю суши."
            
            show kaito hap at r2
            show nikki smi at l2
            
            "Kaito grins."
            voice "audio/voice/E1/D1/S3/Kaito/6.ogg"
            hk "Ваши американские суши не могу даже начать сравниваться с нашими настоящими."
               
        "Звучит неплохо.":
            pf "Я не против сырой, холодной рыбы."
            
            show kaito smi at r2
            show nikki ske at l2
            show drop:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            $renpy.pause(1)
            voice "audio/voice/E1/D1/S3/Nikki/2.ogg"
            sf "Теперь, когда ты так сказал, это звучит не так аппетитно..."
            "Кайто выпустил сердечный смех."
    
        "Черт, я ненавижу сырую рыбу.":
            $ E1D1S3_mcdoesntlikesushi = 1
            pf "Суши? Хммм..."
            
            show kaito mis at r2
            show nikki smi at l2
            
            "Кайто подмигивает мне."
            voice "audio/voice/E1/D1/S3/Kaito/7.ogg"
            hk "Не волнуйся, паренёк, там не всё одно сашими. Поверь мне, тебе понравится!"
            "Я все еще не убежден."
            
    show kaito smi at r2
    show nikki neu at l2
    
    voice "audio/voice/E1/D1/S3/Kaito/8.ogg"
    hk "Кстати, ваши вещи прибыли несколько дней назад. Я положил их в ваши комнаты. Почему бы вам не пойти наверх и начать их распаковывать, пока я готовлю обед."
    pf "Звучит неплохо."
    
    show nikki smi at l2
    
    "Никки кивнула, и мы вместе отправились наверх."  
    
    scene black with fade
    
    pf "..."
    
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
    
    $renpy.pause(2)
         
    #BG My Room
    scene bg homekaito myroom night packed with fade
    
    $ kaiOut = "sCasual"
    
    "Коридор наверху уже, чем дома, но дом Кайто не маленький. {w}Никки направилась в первую комнату справа. {w}Моя комната находится рядом с ней, а комната Кайто дальше по коридору."                                                     
            
    "Даже с расставленными ящиками, я удивлен тем, насколько просторная моя комната. Она возможно даже больше, чем комната в общежитии в CINY."
    
    "Я направился к стене и сел на край кровати. Слава богу, Кайто поставил кровати прежде чем мы приехали. {w}Я даже не помню в какой коробке моё бельё. {w}Возможно, в этой?"
    
    "Я притянул ближайшую коробку и открыл её. Там просто одежда. Может начать из неёё выкладвать."
    
    "Я только что разобрал вещи из коробки, когда голос Кайто донёсся снизу."
            
    voice "audio/voice/E1/D1/S3/Kaito/9.ogg"
    hk "{b}ЭЙ, РЕБЯТА! ЕДА ПРИЕХАЛА!{/b}"
    
    scene black with fade
    #The Alpha build does a cool "persona-y" sliding transition of this, but for now we'll just fade
    "—После ужина—"
    
    
    #BG Uncle Kaitos Home
    scene bg homekaito main night with fade
    
    show kaito smi at r2:
        xzoom -1
    show nikki win at l2
    with dissolve
    show storm:
        xoffset 365
        yoffset 160
        xzoom .75
        yzoom .75
    $renpy.pause(1)
    voice "audio/voice/E1/D1/S3/Nikki/3.ogg"
    sf "Ух, я наелась..."
    
    show nikki neu at l2
    
    menu:
        "ОМ НОМ НОМ!":
            if (E1D1S3_mcdoesntlikesushi == 0):
                "Я жадно тянусь за добавкой, даже после того, как Никки и Кайто кладут свои палочки для еды."
                
                show kaito cur at r2
                show exclamation:
                    xoffset 1040
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D1/S3/Kaito/10.ogg"
                hk "Ты не шутил, когда говорил, что любишь суши..."
                
                show nikki hap at l2
                voice "audio/voice/E1/D1/S3/Nikki/4.ogg"
                sf "Вы бы видели его в буфете «все, что вы можете есть»! Это как смотреть на пылесос, если бы пылесосы могли есть."
                "Я съедаю последний кусочек и довольно вздыхаю."
                
                show kaito smi at r2
                voice "audio/voice/E1/D1/S3/Kaito/11.ogg"
                hk "Ну, какой вердикт вынесешь {i}настоящим{/i} суши?"
                pf "Хмм... Неплохо."
                
                show nikki mis at l2
                voice "audio/voice/E1/D1/S3/Nikki/5.ogg"
                sf "\"Неплохо\" говорит он с полным ртом суши и рисом на лице!"
                
                show kaito hap at r2
                show nikki smi at l2
                
                "Никки и Кайто кажутся удивленными, когда я убираю рис с лица."
                         
            else:
                "Я жадно тянусь за добавкой, даже после того, как Никки и Кайто кладут свои палочки для еды."
                
                show kaito ske at r2
                show question:
                    xoffset 1040
                    yoffset 5
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D1/S3/Kaito/12.ogg"
                hk "Ты уверен, что не любишь суши?"
                
                show nikki sur at l2
                show shocked:
                    xoffset 365
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D1/S3/Nikki/6.ogg"
                sf "Вау, он действительно всё съел!"
                "Я съедаю последний кусочек и подавляю отрыжку."
                
                show kaito cur at r2
                voice "audio/voice/E1/D1/S3/Kaito/13.ogg"
                hk "Ну, Что думаешь?"
                pf "Нормально."
                
                show kaito mis at r2
                
                "Кайто видит прямо через мою попытку играть в крутого, и улыбается в триумфе."
                
        "Я тоже наелся...":
            pf "То же самое."
            
            show kaito hap at r2
            
            "Kaito ест последний кусок суши и омывает его зеленым чаем."
            show note:
                xoffset 1040
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D1/S3/Kaito/14.ogg"
            hk "Аахх, прямо в точку!"
    
    show kaito smi at r2
    show nikki neu at l2
    with dissolve
    
    "Кайто откидывается на спинку стула, положив руки за голову."
    voice "audio/voice/E1/D1/S3/Kaito/15.ogg"
    hk "Ну, what was CINY like?"
    
    pf "Как обычно. Жкзамены, грязная комната общежития, подработка."
    
    show nikki hap at l2
    voice "audio/voice/E1/D1/S3/Nikki/7.ogg"
    sf "И ты все же смог накопить денег на покупку мотоцикла(велосипеда?)."
    
    pf "Точно. Я мог бы купить его раньше, если бы обслуживание GEAR не было таким затратным."
    
    show kaito cur at r2
    show nikki neu at l2
    voice "audio/voice/E1/D1/S3/Kaito/16.ogg"
    hk "Ох, Ты все ещё используешь свой старый GEAR?"
    
    pf "Да."
    
    show kaito ske at r2
    voice "audio/voice/E1/D1/S3/Kaito/17.ogg"
    hk "Это не доставляет тебе проблем? Ты должен заменить его."
    
    "Все это говорят, но когда я думаю о времени, проведенное с отцом… {w}Я не готов откинуть эти воспоминания, особенно сейчас, когда они никогда не могут быть заменены. {w}К тому же, отец был хорош в том, что делал. Я знаю, что ещё остался порох в пороховницах этого меха."
            
    pf "Полагаю, но мы с отцом работали над ним вместе. Много крови, пота и слез ушло на это, и я не совсем готов отказаться от всей этой тяжелой работы."
    
    show kaito neu at r2
    show nikki hap at l2
    voice "audio/voice/E1/D1/S3/Nikki/8.ogg"
    sf "Так и есть. Особенно тогда, когда этот растяпа уронил свечу. Помнишь? Тогда было {i}много{/i} крови--"
    
    pf "{b}Никки!{/b}"
    
    show nikki smi at l2
    
    "Она мило улыбнулась мне."
    
    show nikki mis at l2
    voice "audio/voice/E1/D1/S3/Nikki/9.ogg"
    sf "Что? Я просто поддерживаю тебя, братец."
    
    show kaito hap at r2
    
    "Дядя Кайто смеется."
    
    show kaito smi at r2
    show nikki neu at l2
    voice "audio/voice/E1/D1/S3/Kaito/18.ogg"
    hk "Понимаю. Он должен прибыть в академию в любой день. Все, что тебе нужно сделать, это указать правильный ID, чтобы забрать его."
    
    show kaito sur at r2
    show exclamation:
        xoffset 1040
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D1/S3/Kaito/19.ogg"
    hk "О, точно, это напомнило мне..."
    
    "Дядя кайто вскочил на ноги, и взял что-то с соседнего стола. {w}Он вернулся с пачкой бумаг, и передал их Никки."
    
    show kaito neu at r2
    voice "audio/voice/E1/D1/S3/Kaito/20.ogg"
    hk "Вот твои бумаги о переводе. Там находятся все необходимые бумаги. Они уже заполнены. Все, что тебе осталось сделать, это первым делом передать их директору завтра утром."
    
    show nikki hap at l2
    voice "audio/voice/E1/D1/S3/Nikki/10.ogg"
    sf "Хорошо! Спасибо, дядя."
    
    show kaito smi at r2
    voice "audio/voice/E1/D1/S3/Kaito/21.ogg"
    hk "Вот."
    
    "Он даёт каждому из нас SIM карту."
    voice "audio/voice/E1/D1/S3/Kaito/22.ogg"
    hk "Вставьте эти SIM карты в ваши телефоны. Я уже положил на них деньги, чтобы они заработали."
    
    show kaito neu at r2
    show nikki smi at l2
    
    "Кайто посмотрел на меня."
    voice "audio/voice/E1/D1/S3/Kaito/23.ogg"
    hk "А ты позаботился о бумагао о переводе?"
    
    show bg homekaito main night:
        linear .30 yoffset -50
        linear .30 yoffset 0
        linear .30 yoffset -50
        linear .30 yoffset 0
        
    show kaito neu:
        linear .30 yoffset -70
        linear .30 yoffset 0
        linear .30 yoffset -70
        linear .30 yoffset 0
    
    show nikki smi:
        linear .30 yoffset -70
        linear .30 yoffset 0
        linear .30 yoffset -70
        linear .30 yoffset 0
    
    
    "Я кивнул."
    
    show kaito smi at r2
    voice "audio/voice/E1/D1/S3/Kaito/24.ogg"
    hk "Отлично."
    
    "Я вставил новую SIM в свой телефон."

    "Немного подождав, телефон включается, показывая пустой лист контактов. Я бысто обменялся телефонами с Никки и дядей Кайто. Старые контакты я могу добавить позже."
    voice "audio/voice/E1/D1/S3/Kaito/25.ogg"
    hk "Не стесняйтесь звонить мне, если вам что-нибудь понадобится."
    
    pf "Не будем."
    
    show nikki neu at l2 with dissolve
    $renpy.pause(1)
    
    ""njn hfpujdjh e,f.rbdftn."
    
    pf "Эй, Никки, мы определённо дожны распаковать вещи пока пока не наступил джетлаг(П.п. Джетлаг -  синдром смены часового пояса, десинхрония/десинхроноз)."
    
    show nikki smi at l2
    voice "audio/voice/E1/D1/S3/Nikki/11.ogg"
    sf "Хорошая идея."
    voice "audio/voice/E1/D1/S3/Kaito/1.ogg"
    hk "Хорошо. До поздна не засиживайтесь. У вас завтра впереди длинный день."
    
    "Мы встали из-за стола и направились наверх."
    
    scene black with fade
    
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
    
    stop music fadeout 3
    
    $renpy.pause(3)
    
    jump E1D1S4
