label E1D2S10:
    
    
    #  The previous programming is so silly. They separated going alone or with shou even though it is the same scene and location. 
    #  I think I figured out a clean way to merge S10 and S11 but still keep them separate for voice files.
    
    if (E1D2S9_AgreeJoinShouTeam == 1):
        jump E1D2S11
        
    elif (E1D2S9_AgreeJoinShouTeam == 0):
        jump E1D2S10_WentSolo
    
    
    label E1D2S10_WentSolo:
        scene black with fade:
        "Я взялся за ручку двери и вошёл внутрь."
        play ambient "audio/ambience/Pilot Lounge.ogg" fadein 1
        scene bg campus lounge day with fade
        "В зале была группа студентов, и все были одеты в похожую тианову форму. Я сделал несколько шагов, затем останавился, пытаясь решить, как справиться с ситуацией."
        $ E1S2D10_AskedOtherTeams = 1
        menu: 
            "Я просто буду честен в своей ситуации.":
                play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
                "Должна быть хотя бы одна или две команды, ищущие нового участника."
                "Я взглядуд на небольшую группу людей, сидевших ближе всего ко мне, оживленно говорящих между собой. Они выглядели достаточно дружелюбными." 
                pf "Привет! Как дела?"
                show studentM extra at l2
                show studentM2 extra at r2
                with dissolve
                "Они развернулись и посмотрели на меня. Близсидящая девушка быстро оглядела меня." 
                voice "audio/voice/E1/D2/S10/stu7m/2.ogg"
                stu7m "Эм… Привет. Мы чем-то можем помочь?"
                "Парень, рядом с ней, начал говорить прежде чем я ответил."
                voice "audio/voice/E1/D2/S10/stu2m/1.ogg"
                stu2m "Эй, ты же новенький, да? Я видел тебя сегодня в кампусе. Ты пределённо выделяешься."
                "Он смотрел на мои светлые волосы."
                pf "Полагаю, я выгляжу немного иначе."
                voice "audio/voice/E1/D2/S10/stu7m/3.ogg"
                stu7m "Ты только что перевёлся к нам?"
                pf "Да, из CINY, что в Штатах."
                voice "audio/voice/E1/D2/S10/stu7m/4.ogg"
                stu7m "Немного поздний период года для перевода, не так ли?" 
                "Разве? Учебный год только начался. Но они все согласно кивнули." 
                voice "audio/voice/E1/D2/S10/stu2m/2.ogg"
                stu2m "Да, команды обычно формируются летом, прежде чем начнутся занятия. Ты уже нашёл команду?"
                pf "Да... В этом как раз моя проблема. Я надеялся,что кто-то в холле поможет мне. Вам ведь не нужен ещё один пилот?" 
                "Второй студент помотал головой." 
                voice "audio/voice/E1/D2/S10/stu2m/3.ogg"
                stu2m "Нет, у нас всё заполнено. По крайней мере мест пилотов нет." 
                pf "Как всегда не везёт. Может вы знаете кого-то, кто ищёт человека в команду?" 
                "Группа обменялась взглядами, прежде чем первый студент снова заговорил."
                voice "audio/voice/E1/D2/S10/stu7m/5.ogg"
                stu7m "Синдзиро и Итами искали ещё одного пилота, не так ли?" 
                voice "audio/voice/E1/D2/S10/stu2m/4.ogg"
                stu2m "Точно. На твоём месте я бы поговорил с ними. Последнее, что я слышал, что их команда не была полной. Вероятно, ты также научишься многому у них. Они были лучшими пилотами в свой первый год." 
                "Синдзиро? Это тот парень, который поддходил ко мне ранее? У меня не сложилось впечатление, что он был лучшим пилотом. Может быть в этом парне есть что-то больше, чем я думал." 
                pf "Ну, что ж, спасибо за помощь."
                hide studentM extra
                hide studentM2 extra
                with dissolve
                "Я улыбнулся и отошёл от группы. Похоже мы возвращаемся в начало." 
        
            "I'm a smooth operator.":
                "Я надел свою самую очаровательную улыбку и осмотрел на комнату, ища подходящую цель."
                "Я выцепил взгядом симпатичную девушку, и направился к ней."
                show studentF2 extra at r2 with dissolve
                pf "Привет, Я [pfirst]."
                show bully2 extra at l2 with dissolve
                play music "audio/music/Stress (GAME VERSION).ogg" fadein 1
                "Прежде, чем она ответила, высокий парень подошёл к нам, и холодно посмотрел на меня." 
                voice "audio/voice/E1/D2/S10/stu2m/5.ogg"
                stu2m "Тебе чего надо?" 
                pf "Раз ты спросил, я как раз надеялся узнать имя этой милой дамы."
                "Она удивлённо моргнула, и попыталась скрыть появляющийся румянец на щеках. Он стал еще более взволнованным, наблюдая её реакцию."
                voice "audio/voice/E1/D2/S10/stu2m/6.ogg"
                stu2m "Она не хочет тебя знать!"
                pf "Ты уверен в этом?"
                voice "audio/voice/E1/D2/S10/stu2m/7.ogg"
                stu2m "Хм?"
                pf "Ты спросил её?"
                voice "audio/voice/E1/D2/S10/stu2m/8.ogg"
                stu2m "Ну, нет."
                pf "Тогда откуда тебе знать, что она не заинтересована во мне так же, как я в ней?"
                "Не дожидаясь его ответа, я повернулся к девушке."
                pf "Как я говорил ранее, прежде чем нас грубо прервали, я [pfirst], а тебя как зовут?"
                "Она стеснительно улыбалась."
                stu9f "Мицуки."
                "Лицо парня было ярко-красным, когда он встал между нами, и повернулся к ней."
                voice "audio/voice/E1/D2/S10/stu2m/9.ogg"
                stu2m "Какого хрена ты говоришь этому придурку своё имя?"
                stu9f "Я могу сказать свое имя всем, кому хочу."
                voice "audio/voice/E1/D2/S10/stu2m/10.ogg"
                stu2m "Но этому парню? Ни за что!"
                hide studentF2 extra
                hide bully2 extra
                with dissolve
                stop music fadeout 3
                "Я отошёл, пока пара ругалась. Даже если у них открыт набор в команду, то это, вероятно, не сработает."
                "Я заметил, как она смотрела на меня краем глаза, пока ёё продолжал отчитывать парень. Хех, всё ещё работает!"
                "Пока я искал другую группу, я увидел группу хихикающих девушек, наблюдающих за мной... {w}Бинго. Я подошёл к ним."
                play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 1
                show studentF2 extra at l3
                show studentF extra at r3
                show highschoolgirl2 extra at cc
                with dissolve
                pf "Привет, дамы." 
                "Одна из них улыбнулась." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_01.ogg"
                stu1f "У тебя небольшие проблемы?" 
                pf "У меня? Да никогда в жизни! Но я думаю, не каждый ценит мое обаяние." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_02.ogg"
                stu1f "Может ты просто не очень хорошо выбираешь с кем говорить. Я бы точно не отказала тебе."
                "Я усмезнулся."
                pf "О, да? И почему это"
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_03.ogg"
                stu1f "Ты выглядишь как молодой Сеонардо ДиЛаприо!"
                voice "audio/voice/E1/D2/S10/stu4f/stu4f_01.ogg"
                stu4f "Ооо, Сеонардо ДиЛаприо!"
                voice "audio/voice/E1/D2/S10/stu3f/Alexandria Bearden_stu3f_1.ogg"
                stu3f "Подожди, какой Сеонардо ДиЛаприо?"
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_04.ogg"
                stu1f "Ну, ты знаешь--Сеонардо ДиЛаприо."
                voice "audio/voice/E1/D2/S10/stu4f/stu4f_02.ogg"
                stu4f "Сеонардо ДиЛаприо, он играл в {i}Джомео(JoJo Refference) and Рульетте{/i}."
                voice "audio/voice/E1/D2/S10/stu3f/Alexandria Bearden_stu3f_2.ogg"
                stu3f "Ооох, Сеонардо ДиЛаприо! Полагаю, он похож на него."
                pf "Отлично, я рад, что мы установили это."
                voice "audio/voice/E1/D2/S10/stu4f/stu4f_03.ogg"
                stu4f "Так кто ты такой?" 
                pf "Я студент, переведённый из CINY." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_05.ogg"
                stu1f "Ты из Штатов?" 
                pf "Да. Только что перевелся на второй год обучения программы пилотов." 
                "Одна из девушек легко толкнула свою подругу. Она наклонилась ближе и шептала что-то, потом попыталась скрыть улыбку." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_06.ogg"
                stu1f "Что такое?" 
                voice "audio/voice/E1/D2/S10/stu3f/Alexandria Bearden_stu3f_3.ogg"
                stu3f "… Он из Штатов." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_07.ogg"
                stu1f "Ииии?" 
                voice "audio/voice/E1/D2/S10/stu4f/stu4f_04.ogg"
                stu4f "Ну, помнишь тот старый GEAR в ангаре? Он прибыл из Штатов." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_08.ogg"
                stu1f "Это твой GEAR?" 
                pf "… Возможно." 
                voice "audio/voice/E1/D2/S10/stu3f/Alexandria Bearden_stu3f_4.ogg"
                stu3f "Хм… Я и не знала, что Америка так отстала от Японии, когда дело доходит до GEAR." 
                "Моя улыбка пропала."
                pf "Как по мне, он все ещё отлично работает." 
                "Мой GEAR важен для меня. Вс считают его мусором?" 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_09.ogg"
                stu1f "Какая команда пожелала, чтобы ты присоединился к ним?" 
                pf "Никакая, пока что. Я как раз и ищу команду." 
                "Она обменялась взглядами со своими друзьями, затем повернулась ко мне и покачала головой." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_10.ogg"
                stu1f "Ну, удачи. Не думаю, что какая-то команда возьмёт тебя с таким GEAR." 
                hide studentF2 extra
                hide studentF extra
                hide highschoolgirl2 extra
                with dissolve
                "Она и остальные ее друзья отвернулись от меня, и я неловко смотрел на их спины."
                "Полагаю, мой GEAR - это первое впечатление ко мне."
        
            "Я должен искать группы по 3 человека":
                play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
                "Раз команда работает как группа по меньшей мере из 4 пилотов, лучше всего предположить, что любая группа из трех человек по-прежнему ищет четвертого участника. {w}Мои глаза пали на группу из трех учеников, сидящих в дальнем конце комнаты. Рядом с ними есть дополнительный стул, поэтому я подошёл и сел."
                show studentM extra at l3
                show studentM2 extra at l1
                show studentF2 extra at r1
                with dissolve
                pf "Привет, вы выглядите так, как-будто ищете пилота." 
                voice "audio/voice/E1/D2/S10/stu7m/6.ogg"
                stu7m "А ты кто такой?"
                pf "Студент, переведённый из CINY. Лучший в своём классе, и ищущий команду, нуждающуюся в квалифицорованном человеке." 
                "Они обменялись взглядами друг с другом." 
                voice "audio/voice/E1/D2/S10/stu2m/11.ogg"
                stu2m "Переведённый? Я слышал, что экзамен был довольно тяжёлым." 
                pf "Я справился." 
                voice "audio/voice/E1/D2/S10/stu7m/7.ogg"
                stu7m "Хорошо, но вообще-то мы не ищем никого." 
                "Девушка вежливо улыбается и машет другому пилоту."
                show studentF extra at r3 with dissolve
                voice "audio/voice/E1/D2/S10/stu7m/8.ogg"
                stu7m "Прости, но это наш четвёртый пилот." 
                "Она посмотрела на меня, будто бы он ожидал, что я освобожу его место. Ну уж нет."
                pf "Есть идеи, кто ещё ищёт?" 
                voice "audio/voice/E1/D2/S10/stu2m/12.ogg"
                stu2m "Мы не следим за другими командами и их нуждами. Насколько я знаю, команды формируются летом, но ты все ещё можешь поспрашивать, вдруг кому не хватает людей."
                pf "Ну, в люьом случае, спасибо."
                hide studentF2 extra
                hide studentF extra
                hide studentM extra
                hide studentM2 extra
                with dissolve
                "Я встал и отошёл от них. Снова оглядев комнату, я вижу, что больше нет групп по три человека. Кажется, у всех есть группа пилотов, с которыми они  уже работают."  
                "Так много усилий для того, чтобы найти команду таким образом." 
    
    "Пойти ли к Сё и посмотреть, примет ли он все ещё меня, или просто пойти домой, и попробовать завтра?"
    stop music fadeout 3
    menu:
            "Возможно, Сё даст мне ещё один шанс.":
                jump E1D2S11
    
            "Достаточно с меня отказов за один день.":
                $ E1D2S10_EnoughRejection = 1
                jump E1D2S12
    

