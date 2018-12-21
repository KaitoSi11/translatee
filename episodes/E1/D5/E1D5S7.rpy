label E1D5S7:

$ nikOut = "sCasual"

play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 3
$renpy.pause(1.5)

scene bg homekaito main night with fade

"Войдя в комнату меня окружил смех. Никки и две девушки сидели в гостинной. Они заметили меня."

show nikki hap at cc
show highschoolgirl extra at l3
show highschoolgirl2 extra at r3
with dissolve

"Никки встретила меня широкой улыбкой и махала мне, пока две другие перешёптывались." 
show nikki smi
voice "audio/voice/E1/D5/S7/Nikki/1.ogg"
sf "Эё, ты вернулся! Где ты был?"

if (E1D5S1_EventAlone == 1):
    pf "Я ходил практиковаться в аркадных симуляторах."
    "Nikki's friends both perk up."
    voice "audio/voice/E1/D5/S7/HSS1/1.ogg"
    hstu1f "Симуляции GEAR?"
    pf "Ага."
    voice "audio/voice/E1/D5/S7/HSS2/1.ogg"
    hstu3f "Там было много других пилотов?"
    pf "Хм, не тех, кого бы я знал."
    show nikki ske
    voice "audio/voice/E1/D5/S7/HSS1/2.ogg"
    hstu1f "Ох, единственный пилот…"
    "Никки странно посмотрела на них, затем пожала плечами."

elif (E1D5S1_EventKaori == 1):
    pf "Я ходил в магазин, смотрел планшеты."
    voice "audio/voice/E1/D5/S7/Nikki/2.ogg"
    sf "О, правда? Нашёл что-нибудь хорошее?"
    pf "Да."
    show nikki cur
    "Она посмотрела на мои пустые руки."
    voice "audio/voice/E1/D5/S7/Nikki/3.ogg"
    sf "Но недостаточно хорошее для покупки?"
    pf "О, Каори хотела новый планшет. Я просто показывал ей варианты."
    show nikki dis
    voice "audio/voice/E1/D5/S7/Nikki/4.ogg"
    sf "Это довольно отстойное свидание. Я разочарована в тебе."
    "Друзья Никки, похоже, были начеку."
    pf "Это было не свидание!"
    show nikki mis
    voice "audio/voice/E1/D5/S7/Nikki/5.ogg"
    sf "Кооооонечно, как скажешь."
    "Подруга Никки наклонилась и шептала."
    voice "audio/voice/E1/D5/S7/HSS2/2.ogg"
    hstu3f "У него есть девушка?"
    show nikki smi
    voice "audio/voice/E1/D5/S7/Nikki/6.ogg"
    sf "Ха--в его мечтах."
    "Девушки посмотрели друг на друга и захихикали."

elif (E1D5S1_EventShou == 1) or (E1D5S1_EventMayu == 1):
    pf "Я болтался с друзьями."
    show nikki mis
    show question:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D5/S7/Nikki/7.ogg"
    sf "О, да? У тебя есть друзья?"
    pf "Очень смешно."
    "Никки ухмыльнулась."
    show nikki neu
    voice "audio/voice/E1/D5/S7/Nikki/8.ogg"
    sf "Кто?"
    pf "Просто Сё и Маю из команды."
    "Подружки Никки наклонились к ней и шептали."
    voice "audio/voice/E1/D5/S7/HSS1/3.ogg"
    hstu1f "О какой команде он говорит?"
    voice "audio/voice/E1/D5/S7/Nikki/9.ogg"
    sf "Его команда пилотов."
    voice "audio/voice/E1/D5/S7/HSS2/3.ogg"
    hstu3f "Оооооо."
    "Они обе глянули на меня, оценивая."

elif (E1D5S1_EventYuuna == 1):
    pf "Я встретился с Юной, для работы над нашим проектом."
    show nikki ske
    voice "audio/voice/E1/D5/S7/Nikki/10.ogg"
    sf "Серьёзно? Ты делал домашку в субботу?"
    pf "Ага…"
    voice "audio/voice/E1/D5/S7/Nikki/11.ogg"
    sf "Тооооооочно, это никак не связано со встречей с милой девушкой."
    "Подружки Никки внезапно напряглись."
    pf "Мы действительно делали домашнюю работу. По факту, мы закончили проект."
    show nikki cur
    voice "audio/voice/E1/D5/S7/Nikki/12.ogg"
    sf "Ты говоришь, что часами был наедине с милой девушкой, и все, что делал, это учился?"
    pf "Эм, да."
    "She sighs."
    show drop:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    show nikki dis
    voice "audio/voice/E1/D5/S7/Nikki/13.ogg"
    sf "Ты так безнадёжен!"
    "Девушки посмотрели друг на друга и захихикали."

pf "Чем вы занмаетесь?" 
show nikki neu
voice "audio/voice/E1/D5/S7/Nikki/14.ogg"
sf "Играем в Нарисуй это."
pf "Что это?" 
"Первая девушка заговрила вперёд Никки." 
voice "audio/voice/E1/D5/S7/HSS1/4.ogg"
hstu1f "Это весёлая игра! Выбираешь слово из кучи, рисуешь, и люди догадываются, что это." 
pf "Звучит довольно легко."
show note:
    xoffset 1175
    yoffset 160
    xzoom .75
    yzoom .75
voice "audio/voice/E1/D5/S7/HSS2/4.ogg"
hstu3f "Присоединяйся! Так мы сможем играть командами по двое."
voice "audio/voice/E1/D5/S7/HSS1/5.ogg"
hstu1f "Да! Присоединяйся!"
pf "Хм…"
"Я глянул на Никки, она пожала плечами."
voice "audio/voice/E1/D5/S7/Nikki/15.ogg"
sf "Конечно, почему бы и нет?"
pf "Хорошо."
"Обе девушки радостно подпрыгнули."
show nikki cur
"Первая встала с дивана и схватила меня за руку, затем потащила назад, чтобы я сел с ней."
voice "audio/voice/E1/D5/S7/HSS1/6.ogg"
hstu1f "Ура! Ты будешь в моей команде." 
voice "audio/voice/E1/D5/S7/HSS2/5.ogg"
hstu3f "Нет! Он должен быть в моей команде."
"Другая девушка схватиа меня за вторую руку."
pf "Эм."
voice "audio/voice/E1/D5/S7/HSS1/7.ogg"
hstu1f "Почему? Ты с Никки лучшие подруги. Вы должны быть в команде!"
show nikki sur
"Она крепче обхватила мою руку."
voice "audio/voice/E1/D5/S7/HSS2/6.ogg"
hstu3f "Но он пилот в ACE, значит он умён, и должен быть в моей команде!"
"Похоже меня собрались разорвать надвое."
show crying:
    xoffset 720
    yoffset 160
    xzoom .75
    yzoom .75
show nikki dis with dissolve
voice "audio/voice/E1/D5/S7/Nikki/16.ogg"
sf "Ой! Я думала, что вы мои друзья, а не его?"

#hstu1f and hstu3f speaking simultaneously
voice "audio/voice/E1/D5/S7/HSS1/8.ogg"
hstu1f "Так и есть!"
voice "audio/voice/E1/D5/S7/HSS2/7.ogg"
hstu3f "Так и есть!"
show nikki ske
voice "audio/voice/E1/D5/S7/Nikki/17.ogg"
sf "Тогда почему вы не хотите быть в моей команде?"
"Они глянули друг на друга, но ни одна из них не отпустила меня. Никки скрестила руки."
show nikki smi
voice "audio/voice/E1/D5/S7/Nikki/18.ogg"
sf "Хорошо. Что ж, он мой брат, поэтому будет в моей команде."
"Обе девушки разочарованно надулись и отпустили меня." 
voice "audio/voice/E1/D5/S7/HSS2/8.ogg"
hstu3f "Ты зануда, Никки."
show nikki neu
voice "audio/voice/E1/D5/S7/Nikki/19.ogg"
sf "Плевать. Вы можете ходить первыми!" 
voice "audio/voice/E1/D5/S7/HSS1/9.ogg"
hstu1f "Хорошо." 

hide nikki
hide highschoolgirl extra
hide highschoolgirl2 extra2
with dissolve

show highschoolgirl extra at r1:
    xzoom -1
show highschoolgirl2 extra at r3:
    xoffset 75
    xzoom -1
show nikki neu at l3
with dissolve
$renpy.pause(.5)

"Подруга Никки взяла карточку, и улыбнулась, увидя слово."
"Она быстро глянула на меня, затем начала рисовать. На рисунке был лондин… одеты в что-то жутко знакомое."
"Дторая двушка сразу ответила." 
voice "audio/voice/E1/D5/S7/HSS2/9.ogg"
hstu3f "Горячий! Это слово - горячий!" 
show nikki cur
voice "audio/voice/E1/D5/S7/HSS1/10.ogg"
hstu1f "Да!" 
"Они обе захихикали. Никки схватила листок и взглянула на него."
show question:
    xoffset 230
    yoffset 160
    xzoom .75
    yzoom .75
show nikki ske
voice "audio/voice/E1/D5/S7/Nikki/20.ogg"
sf "Что? Как ты догадалась из этого, что это \"горячий\"?"
"Она ткнула рисунок мне в лицо."
show nikki cur
voice "audio/voice/E1/D5/S7/Nikki/21.ogg"
sf "Ты бы знал, что это \"горячий\"?"

menu:
    "Нет, но это определённо женские штучки.":
        pf "Нет, но я уверен, что вы, девушки, лучше меня знаете, горяч парень или нет."
        show nikki dis
        "Никки просто смотрела на меня."
        voice "audio/voice/E1/D5/S7/Nikki/22.ogg"
        sf "Хорошо, забей."

    "Как ещё бы ты описала меня?":
        pf "Это довольно очевидно для меня."
        "Я усмехнулся девушким, они покраснели."
        show nikki dis
        voice "audio/voice/E1/D5/S7/Nikki/23.ogg"
        sf "Что? Заткнись. От тебя никакого толку."

    "Определённо нет.":
        pf "Я не думаю, что \"горячий\", это именно то слово."
        show nikki neu
        voice "audio/voice/E1/D5/S7/Nikki/24.ogg"
        sf "Спасибо!"

show confused:
    xoffset 230
    yoffset 160
    xzoom .75
    yzoom .75
show nikki cur
voice "audio/voice/E1/D5/S7/Nikki/25.ogg"
sf "Почему ты не нарисовала огонь, или например, кружку кофе, или что-нибудь такое? Кто это вообще должен быть?" 

show heart:
    xoffset 875
    yoffset 160
    xzoom .75
    yzoom .75
    
show heart2:
    xoffset 330
    yoffset 160
    xzoom -.75
    yzoom .75

"Обе девушки посмотрели на меня и снова захихикали."
$renpy.pause(.75)
show shocked:
    xoffset 230
    yoffset 160
    xzoom .75
    yzoom .75
show nikki sur b1 with dissolve
$renpy.pause(1.0)

"Никки посмотреал на нах троих, затем нахмурилась." 

show nikki ann b1
voice "audio/voice/E1/D5/S7/Nikki/26.ogg"
sf "Девочки, он мой брат!"
voice "audio/voice/E1/D5/S7/HSS2/10.ogg"
hstu3f "И?"
voice "audio/voice/E1/D5/S7/HSS1/11.ogg"
hstu1f "Он милый…"

show nikki ang b1
voice "audio/voice/E1/D5/S7/Nikki/27.ogg"
sf "Но он {i}мой брат{/i}!" 
show nikki ann b1
"Девушки посмотрели друг на друга, потом вздохнули."
voice "audio/voice/E1/D5/S7/HSS1/12.ogg"
hstu1f "Аааа, мы понятия не имели."
voice "audio/voice/E1/D5/S7/HSS2/11.ogg"
hstu3f "Да, нам жаль! Но ты должна была нам сказать."
show nikki cur with dissolve
"Никки смотрела в замешательстве."
voice "audio/voice/E1/D5/S7/Nikki/28.ogg"
sf "Хм? Что сказать?"
voice "audio/voice/E1/D5/S7/HSS1/13.ogg"
hstu1f "Что ты с ним--ты знаешь."
"Она показала головой на меня."
voice "audio/voice/E1/D5/S7/HSS1/14.ogg"
hstu1f "У тебя с ним отношения…"
"Никки продолжала смотреть несколько секунд..."
show frightful:
    xoffset 230
    yoffset 160
    xzoom .75
    yzoom .75
show nikki sur with dissolve
$renpy.pause(.5)
"...затем выражение ее лица превращается в ужас."
voice "audio/voice/E1/D5/S7/Nikki/29.ogg"
sf "О мой Бог, нет!"
voice "audio/voice/E1/D5/S7/HSS2/12.ogg"
hstu3f "Понятно, почему ты так защищала его." 
voice "audio/voice/E1/D5/S7/HSS1/15.ogg"
hstu1f "И хотела его в свою команду." 
voice "audio/voice/E1/D5/S7/HSS2/13.ogg"
hstu3f "Никки, тебе не нужно смущаться. Это нормально!"
show nikki win
voice "audio/voice/E1/D5/S7/Nikki/30.ogg"
sf "Отвратительно, отвратительно, отвратительно!" 
"Дела стали отчень странными."
pf "Я пойду наверх." 
voice "audio/voice/E1/D5/S7/HSS1/16.ogg"
hstu1f "О нет! Останься и поиграй с нами." 
voice "audio/voice/E1/D5/S7/HSS2/14.ogg"
hstu3f "Да, останься!" 
show nikki ann
"Никки встала и толкала меня к лестнице." 
voice "audio/voice/E1/D5/S7/Nikki/31.ogg"
sf "Не слушай их. Просто иди!" 
pf "Иду я, иду!" 


stop ambient fadeout 3.0
scene black with fade
$renpy.pause(.5)


"Я поднялся по лестнице, все ещё слыша, как они ругались." 
voice "audio/voice/E1/D5/S7/HSS2/15.ogg"
hstu3f "Почему ты прогнала его, Никки? Мы хорошо проводили время."
voice "audio/voice/E1/D5/S7/HSS1/17.ogg"
hstu1f "Да, к тому же он горяч."
voice "audio/voice/E1/D5/S7/Nikki/32.ogg"
sf "Фу, девочки, прекратите." 
voice "audio/voice/E1/D5/S7/HSS2/16.ogg"
hstu3f "Смотерть - не преступление." 
voice "audio/voice/E1/D5/S7/Nikki/33.ogg"
sf "Ну, а должно быть! Извините, но я собираюсь это прекратить." 
"Когда я зашёл в комнату и повалился на кровать из голоса исчезли."


$renpy.pause(.5)
stop music fadeout 20
scene bg homekaito myroom night with fade

"Я никогда не пойму девушек. Но забавно, что они подумали, что я горяч. На самом деле, они не были так плохи на вид…"
"Я усмехался, вспоминая, как они сжимали мои руки рядом со своими грудями. С такими формами забываешь то... {w}что они ещё в старшей школе."
"Улыбка пропала. Может быть и хорошо, что Никки не часто приводит своих друзей домой."

play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
"В этот момент на телефон пришло смс. Вздохнув с облегчением, я с нетерпением протянул руку и открывл его."
"Все рейтинги команд будут опубликованы в понедельник." 
"Полагаю, посмотрю рейтинг, когда пойду в школу."

scene black with fade

"Остаток вечера я провёл просматривая видео про котов, пока не пришло время ложиться спать."
"Как толкьо голова коснулась подушки, я уснул. Кто знал, что ждало меня завтра."

#jump E1END

jump E2D1S1
