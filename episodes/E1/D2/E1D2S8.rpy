label E1D2S8:
    
    stop music fadeout 5
    if (E1D2S2_YuunaComesWithYouPass == 0):
        #Yuuna's scene already puts you next to building. This is the filler to introduce building BG from Kaori / parking / Mayu...etc
        scene bg campus main day with fade
        "Я открыл в телефоне карту кампуса. К счастью, по ней легко ориентироваться, и вскоре я уже стоял перед классом. {w}Хвала Богу за технологии."
    stop ambient fadeout 3
    scene black with fade
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 1
    scene bg campus auditorium day with fade
    "Я глубоко вздохнул, успокоил нервы, и крепко толкнул дверь. {w}Быстро осмотрев класс, я выбрал место почти в самом конце. I can tell this is a first year introductory class based on how spread out the students are and how quiet the room is."
    "Ненавижу, что снова придётся проходить вводные уроки. Некоторые факультативы в CINY \"не охватывали весь объем материала курса\". Чтобы это ни значило."
    
    "Тишина охватила класс, когда человек шёл к передней части класса."
    show professorM extra at cc with dissolve
    voice "audio/voice/E1/D2/S8/Prof/1.ogg"
    profm "Доброе утро. Это 101 пилотный. Это все, кто должен быть?"
    play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 3
    "Профессор терпеливо ждал, когда горстка студентов шла к ближайшему выходу. Я зевал и смотрел, как они, потеряв интерес, вышли."
    play sound "audio/sfx/Technology/Phone Projection.ogg" fadein 1
    "Он переместил ссылку со своего планшета на экран позади него."
    voice "audio/voice/E1/D2/S8/Prof/2.ogg"
    profm "Это ссылка класса. Считайте это вашим жизненно важным ресурсом на протяжении курса. Там вы найдёте задания и материалы для чтения. А также ваши текущие оценки. Вы можете найти мою контактную информацию на вкладке \"Связь\". Там перечислены мои рабочие часы, поэтому, пожалуйста, не стесняйтесь заходить. Мне иногда бывает одиноко, и я ценю посетителей."
    
    "Этот фраза получиля пару слабых смешков."
    
    menu:
        "Он подробно объясняет.":
            "Большинство студентов не обращают внимания на это введение, но профессоры больше всего не любят, когда студенты задают вопросы, на который он уже ответил."
    
        "Это так скучно.":
            "Я уже миллион раз слушал эту речь. Хоть профессора и меняются, но слова - никогда."
            
        "{color=#00ff00}{b}Memorize the information.{/b}{/color}" if (MCStory == 2):
            "Я автоматически сохранил информацию в памяти."
    voice "audio/voice/E1/D2/S8/Prof/3.ogg"
    profm "Теперь, когда мы закончили со скучной частью, я уверен, что вы все хотите узнать больше о квалификационных экзаменах в пятницу."
    
    "Класс заметно оживился."
    voice "audio/voice/E1/D2/S8/Prof/4.ogg"
    profm "Квалификационный экзамен не только зарегистрирует вас как действующего пилота, а также предоставит рейтинг вашей команды. Я уверен, что вы уже выбрали команду, но я все равно хотел бы напомнить вам, что каждая команда должна состоять, как минимум, из четырёх человек, чтобы пройти квалификацию." 
    
    "В середине класса поднялась рука."
    
    show studentM extra at r3 with dissolve:
        xzoom -1
    voice "audio/voice/E1/D2/S8/Prof/5.ogg"
    profm "Да?"
    voice "audio/voice/E1/D2/S8/FirstYearStudent/1.ogg"
    stu7m "Вы уверены, что экзамен в эту пятницу? Ведь это даёт нам только два дня на поиск команды..."
    
    "Тихий смех наполнил класс. Студент заметно сжался от всех взглядов, навравленных на него."
    voice "audio/voice/E1/D2/S8/Prof/6.ogg"
    profm "Большинство студентов, которые начинают свой первый год здесь в Академии Ace, знают о сроках проведения квалификационных экзаменов, и за лето формируют команду и готовятся. Раньше мы продлевали время подготовки, но выяснили, что большинству студентов не нужны дополнительные дни. Так что в соответствии с этим мы скорректировали расписание."
    voice "audio/voice/E1/D2/S8/FirstYearStudent/2.ogg"
    stu7m "Но что делать тем, кто раньше не знал о квалификации? Что нам делать?"
    voice "audio/voice/E1/D2/S8/Prof/7.ogg"
    profm "Предлагаю постараться найти команду. Ещё вопросы?"
    
    "Студент хмурился, но покачал головой."
    
    hide studentM extra with dissolve
    voice "audio/voice/E1/D2/S8/Prof/8.ogg"
    profm "Хорошо. на экзамене ваша команда выступит против четырёх ИИ GEARS. Затем вам будет присвоен рейтинг, основанный на вашей общей эффективности по сравнению с другими командами. Не волнуйтесь, если не сможете победить всех ИИ GEARS. Она запрограммированы так, чтобы их было чрезвычайно сложно победить."
    voice "audio/voice/E1/D2/S8/Prof/9.ogg"
    profm "Убедитесь, что ваш GEAR находится в идеальном состоянии. Все экзамены проходятся вживую, а не на симуляторе, чтобы наиболее точно измерить ваши способности."
    voice "audio/voice/E1/D2/S8/Prof/10.ogg"
    profm "Вопросы?"
    
    "Молчание стало ответом."
    show note:
        xoffset 675
        yoffset 50
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S8/Prof/11.ogg"
    profm "Тогда начнём."
    
    #Screen fade black
    scene black with fade
    $renpy.pause(1)
    #Screen back to classroom
    scene bg campus auditorium day with fade
    show professorM extra at cc with dissolve
    voice "audio/voice/E1/D2/S8/Prof/12.ogg"
    profm "Пожалуйста проверьте ваши задания на сайте, и сделайте их до следующего урока. Добро пожаловать в академию Ace. Надеюсь, вы отлично отдохнёте остаток дня."
    hide professorM extra with dissolve
    play sound "audio/sfx/Human/Class End.ogg"
    stop ambient fadeout 3
    stop music fadeout 3
    "Стулья гремели, пока студенты выходили из класса. Те, кто остались, оживлённо болтали маленькими группами."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    play ambient "audio/ambience/Campus.ogg" fadein 1
    "Зевая, я ждал, пока толпа у двери рассосётся, прежде чем выйти из комнаты. Уже за дверью я услышал разговор, который привлёк моё внимание."
    show studentM extra at l2 with dissolve
    voice "audio/voice/E1/D2/S8/stu7m/1.ogg"
    stu7m "Эй, ты видел, что они притащили сегодня в ангар?"
    show studentM2 extra at r2 with dissolve:
        xzoom -1
    voice "audio/voice/E1/D2/S8/stu8m/1.ogg"
    stu8m "Эту древнюю штуку? Хах. Я буду удивлен, если он все еще работает. Где, черт возьми, можно найти что-то подобное? Уверен, что они его из океана выловили!"
    
    "Студенты громно смеялись." 
    hide studentM extra
    hide studentM2 extra
    with dissolve
    "... У меня такое сувство, что я знал, о чём они говорили..."
    scene bg campus main day with fade
    "Пока я торопился выйти из класса, решил проверить телефон и обрадовался уведомлению. Я с нетерпением прочитал сообщение. Там было написано, что мой GEAR был зарегистрирован, и теперь у меня есть доступ в ангар."
    
    "Ну, это, безусловно, облегчило мне жизнь. В CINY, Я проводил {i}дни{/i} пытаясь его зарегистрировать. Нам надо было самим предоставлять документы, коенчно же, никто в офисе администрации не был полезен."
    
    "Удовлетворенный, я убрал телефон и направился к ангару."
    
    if (E1D2S4_MayuGaveDirections == 1):
        scene black with fade
        stop music fadeout 3
        stop ambient fadeout 3
        scene bg campus lounge day with fade
        play ambient "audio/ambience/Pilot Lounge.ogg" fadein 1
        "Вскоре я вернулся в зал пилотов, и направился прямо к охраннику. Не отрываясь от своей голографической книги, он указал на кард-ридер."
        play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
        Я приложил ID карту и задержал дыхание. Ридер издал утвердительный звук, и дверь открылась. Я быстро прошёл внутрь."
        stop ambient fadeout 3
    
    else:
        "Я открыл карту на телефоне и коснулся метки ангара. Вскоре пульсирующий всет проложил путь от моего текущего местоположения до ангара."
        scene black with fade
        stop music fadeout 3
        stop ambient fadeout 3
        play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
        "Это довольно далеко от сердца кампуса, но я неплохо шёл. Я приложил ID карту и вошёл."
        stop ambient fadeout 3
    
    jump E1D2S9
