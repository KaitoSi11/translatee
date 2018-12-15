label E1D5S6:

"Интересно, что делает Маю."
play sound "audio/sfx/Technology/Phone Dial.ogg"
"Я набрал её номер..."
play sound "audio/sfx/Technology/Phone Answer.ogg"
"...и она почти сразу ответила."
voice "audio/voice/E1/D5/S6/Mayu/1.ogg"
ma "Алло?"
pf "О, привет, это [pfirst]."
voice "audio/voice/E1/D5/S6/Mayu/2.ogg"
ma "Ох, привет."
pf "Привет."
voice "audio/voice/E1/D5/S6/Mayu/3.ogg"
ma "...Привет."
"Мы замолкли."

stop music fadeout 3.0
menu:
    "... Об этом я не думал.":
        pf "... Так, эм… Как ты?"
        voice "audio/voice/E1/D5/S6/Mayu/4.ogg"
        ma "Хорошо, спасибо, а ты?"
        pf "Хорошо, хорошо."
        voice "audio/voice/E1/D5/S6/Mayu/5.ogg"
        ma "..."
        "Я практически слышал её замешательство."
        voice "audio/voice/E1/D5/S6/Mayu/6.ogg"
        ma "Эм... ты ищешь Сё?"
        pf "А, ну--"
        play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 3.0
        "Меня прервал шум на заднем плане, и я мог разобрать приглушённый голос Сё."
        voice "audio/voice/E1/D5/S6/Shou/4.ogg"
        ss "Меня? Это меня?"
        "Его голос стал разборчивым."
        voice "audio/voice/E1/D5/S6/Shou/5.ogg"
        ss "Как оно, братан!"
        pf "О, привет Сё. Гуляешь с Маю?"
        voice "audio/voice/E1/D5/S6/Shou/6.ogg"
        ss "Да, мы прост оперекусываем в кафешке. Присоединяйся к нам!"

        menu:
            "Не, спасибо.":
                $ E1D5S1_EventMayu = 0
                $ E1D5S6_MayuNoThanksLoop = 1
                pf "Похоже, вы оба хорошо проводите время, не хочу навязываться."
                voice "audio/voice/E1/D5/S6/Shou/7.ogg"
                ss "Ты не навязываешься!"
                pf "Сппсибо, но я откажусь. Может, в другой раз."
                voice "audio/voice/E1/D5/S6/Shou/8.ogg"
                ss "Хорошо, поговорим позже!"
                stop music fadeout 5.0
                pf "Пока."
                "Ну, это не сработало. Интересно, свободен ли кто-нибудь еще."
                jump E1D5S1_WeekendChoiceSelection

            "Конечно!":
                pf "Ты не возражаешь?"
                voice "audio/voice/E1/D5/S6/Shou/9.ogg"
                ss "Конечно нет! Чем больше, тем лучше!"
                pf "Круто, я скоро буду."
                voice "audio/voice/E1/D5/S6/Shou/10.ogg"
                ss "Увилимся!"
                "Я положил трубку и пошёл к мотоциклу."
                stop music fadeout 3.0
                stop ambient fadeout 3.0
                scene black with fade
                jump E1D5S5_ConvergenceFromMayuCall

jump E1D5S7
