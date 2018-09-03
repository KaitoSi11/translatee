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
            hk "Ваши американские суши не могу даже начать сравниваться с подлинными вещами."
               
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
            "Kaito выпустил сердечный смех."
    
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
    "—After Dinner—"
    
    
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
                "Я жадно тянусь ещё за едой, даже после того, как Никки и Кайто кладут свои палочки для еды."
                
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
                "Я жадно тянусь ещё за едой, даже после того, как Никки и Кайто кладут свои палочки для еды."
                
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
                
                "Kaito видит прямо через мою попытку играть в крутого, и улыбается в триумфе."
                
        "Я тоже наелся...":
            pf "Ditto."
            
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
    hk "So, what was CINY like?"
    
    pf "The usual. Exams, a messy dorm room, a part-time job."
    
    show nikki hap at l2
    voice "audio/voice/E1/D1/S3/Nikki/7.ogg"
    sf "And you still managed to save enough money to buy yourself a bike."
    
    pf "True. I could have bought it sooner if maintaining a GEAR wasn't such a money sink."
    
    show kaito cur at r2
    show nikki neu at l2
    voice "audio/voice/E1/D1/S3/Kaito/16.ogg"
    hk "Oh, you're still using your original GEAR?"
    
    pf "Yup."
    
    show kaito ske at r2
    voice "audio/voice/E1/D1/S3/Kaito/17.ogg"
    hk "Is it giving you trouble? You should probably replace it if it needs that many fixes."
    
    "Everyone says that, but when I think about all the time I spent with Dad… {w}I'm not ready to put those memories aside, especially now that they can never be replaced. {w}Besides, Dad was great at what he did. I know there's still plenty of fight left in that mech."
            
    pf "I guess, but Dad and I worked on it together. A lot of blood, sweat, and tears went into it and I'm not quite ready to give up on all of that hard work."
    
    show kaito neu at r2
    show nikki hap at l2
    voice "audio/voice/E1/D1/S3/Nikki/8.ogg"
    sf "It's true. Especially that one time when butterfingers here dropped the torch. Remember that? There was {i}a lot{/i} of blood--"
    
    pf "{b}Nikki!{/b}"
    
    show nikki smi at l2
    
    "She smiles sweetly at me."
    
    show nikki mis at l2
    voice "audio/voice/E1/D1/S3/Nikki/9.ogg"
    sf "What? I'm just backing you up, big bro."
    
    show kaito hap at r2
    
    "Uncle Kaito laughs."
    
    show kaito smi at r2
    show nikki neu at l2
    voice "audio/voice/E1/D1/S3/Kaito/18.ogg"
    hk "I understand. It should be arriving at the academy any day now. All you'll have to do is present the proper ID to claim it."
    
    show kaito sur at r2
    show exclamation:
        xoffset 1040
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D1/S3/Kaito/19.ogg"
    hk "Oh yeah, that reminds me..."
    
    "Uncle Kaito jumps to his feet and grabs something off a nearby table. {w}He returns with a packet of papers, which he hands to Nikki."
    
    show kaito neu at r2
    voice "audio/voice/E1/D1/S3/Kaito/20.ogg"
    hk "Here are your transfer papers. They're already filled out and all the docs you need are in there. All you have to do is hand this to the headmaster first thing tomorrow morning."
    
    show nikki hap at l2
    voice "audio/voice/E1/D1/S3/Nikki/10.ogg"
    sf "Okay! Thanks, Uncle."
    
    show kaito smi at r2
    voice "audio/voice/E1/D1/S3/Kaito/21.ogg"
    hk "Here."
    
    "He hands each of us a SIM card."
    voice "audio/voice/E1/D1/S3/Kaito/22.ogg"
    hk "Put these SIM cards into your phones. I've already added credit to them to start you off."
    
    show kaito neu at r2
    show nikki smi at l2
    
    "Kaito looks over at me."
    voice "audio/voice/E1/D1/S3/Kaito/23.ogg"
    hk "And you took care of your transfer stuff?"
    
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
    
    
    "I nod."
    
    show kaito smi at r2
    voice "audio/voice/E1/D1/S3/Kaito/24.ogg"
    hk "Great."
    
    "I pop the new SIM card into my phone."

    "After a moment of waiting, the phone boots up to an empty contacts list. I quickly exchange numbers with Nikki and Uncle Kaito. I can add the rest of my old contacts later."
    voice "audio/voice/E1/D1/S3/Kaito/25.ogg"
    hk "Don't hesitate to call me if you need anything."
    
    pf "We won't."
    
    show nikki neu at l2 with dissolve
    $renpy.pause(1)
    
    "The conversation lulls into a silence."
    
    pf "Hey, Nikki, we should probably unpack a bit before the jet lag takes over."
    
    show nikki smi at l2
    voice "audio/voice/E1/D1/S3/Nikki/11.ogg"
    sf "Good idea."
    voice "audio/voice/E1/D1/S3/Kaito/1.ogg"
    hk "Alright. Don't stay up too late, though. You both have a long day ahead of you tomorrow."
    
    "We excuse ourselves from the table and head upstairs."
    
    scene black with fade
    
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
    
    stop music fadeout 3
    
    $renpy.pause(3)
    
    jump E1D1S4
