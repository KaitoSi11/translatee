label E1D5S3:


"Я знаю, что у нас есть целая неделя для работы над нашим проектом, но мне нравится быстро расправляться с заданиями. Надеюсь, Юна такая же."
play sound "audio/sfx/Technology/Phone Dial.ogg"
"Я набрал её номер и ждал."

play sound "audio/sfx/Technology/Phone Answer.ogg"
"Через несколько секунд она подняла трубку."


voice "audio/voice/E1/D5/S3/yuuna/1.ogg"
ym "Алло?"
pf "Привет Юна. Это [pfirst]."
voice "audio/voice/E1/D5/S3/yuuna/2.ogg"
ym "Привет! Как ты?"
pf "Хорошо. Я тут думал, хочешь всттетиться сегодня и работать над проектом?"
voice "audio/voice/E1/D5/S3/yuuna/3.ogg"
ym "Конечно! Вообще-то я рада, что ты позвонил. Я не була уверена насчёт тебя, но мне нравится побыстрее делать поручения."
"Я улыбнулся."
pf "Я тоже."
"Она посмеялась."
voice "audio/voice/E1/D5/S3/yuuna/4.ogg"
ym "Хорошо, что мы партнёры! Когда ты свободен?"
pf "Я всегда свободен. Что насчёт тебя?"
voice "audio/voice/E1/D5/S3/yuuna/5.ogg"
ym "То же самое."
pf "Хорошо, как насчёт встретиться около полудня?"
voice "audio/voice/E1/D5/S3/yuuna/6.ogg"
ym "Конечно, в библиотеке кампуса?"
pf "Да, пойдёт."
voice "audio/voice/E1/D5/S3/yuuna/7.ogg"
ym "Отлично, тогда, увидимся!"
pf "Пока."
"Мы положили трубки."

stop music fadeout 3.0
stop ambient fadeout 3.0
scene black with fade
play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 4
$renpy.pause(3.0)
play sound2 "audio/sfx/Vehicles/Bike driving off.ogg" fadein 3 fadeout 5
$renpy.pause(5.5)

"Приехав в кампус, я припарковал ьайк и ждал перед библиотекой."

play ambient "audio/ambience/Campus.ogg" fadein 3
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
$renpy.pause(1.5)

scene bg campus building day with fade



"Осталось пара минут до полудня. Надеюсь, Юна скоро придёт."
"Каждые несколько минут я проверял время на телефоне… {w}12:07… {w}12:13… {w}12:20… {w}Она так и не пришла, так что я написал ей."
"{i}Я тут, а где ты?{/i}"

$renpy.pause(1.5)
play sound "audio/sfx/Technology/Phone Vibration Once.ogg" 
$renpy.pause(1.5)

"Ответа долго ждать не пришлось."
"{i}Прости! Я всё ещё жду автобус. Я думаю, он должен скоро прибыть.{/i}"
"{i}Я пока найду нам место в библиотеке.{/i}"
"{i}Хорошо, спасибо{/i}"

stop ambient fadeout 3.0
scene black with fade
$renpy.pause(1.5)
play ambient "audio/ambience/Ace Academy Library.ogg" fadein 3
scene bg campus library day with fade

$renpy.pause(1.0)


"Библиотека была в основном пуста, что имело смысл. Не слишком много людей учится по выходным. К счастью, это также означает, что большая часть пространства для совместной работы открыта."
stop music fadeout 6
"Блуждая по полкам, я собрал несколько справочников, которые могли быть полезны, но не мог найти конкретный книгу. Пожав плечами, я направился в пустую комнату ждать Юну. Открыв книгу на случайной странице, я без энтузиазма просматривал её."
"Я снова проаерил время: 12:45. Не похоже, что она идёт…"
play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5.0
"Внезапно, я заметил розовые волосы {w}Юна была в дальнем конце библиотеки, разыскивая меня. Я помахал ей, и она улыбнувшись поторопилась ко мне."

$ yuuOut = "sCasual"

show yuuna ner at cc with dissolve
$renpy.pause(.5)

voice "audio/voice/E1/D5/S3/yuuna/8.ogg"
ym "Прости, что я так поздно. Автобус отстал от графика, что очень необычно. Я надеюсь, ты не слишком зол на меня."
"Я улыбнулся ей в ответ."
pf "Всё хорошо. Я просто рад, что ты добралась."
show yuuna smi with dissolve
"Юна села напротив меня. Я заметил, что она была одета не в свою форму."

menu:
    "Никогда не думал, что она такая милая.":
        pf "Ты сегодня выглядишь очень хорошо. Мне нравится твой стиль."
        show regBlush:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna smi b1 with dissolve
        "Она покраснела."
        show yuuna hap b1 with dissolve
        voice "audio/voice/E1/D5/S3/yuuna/9.ogg"
        ym "Ох! Спасибо. Ты тоже хорошо выглядишь."
        pf "Спасибо."

    "Она горяча!":
        pf "Я бы хотел чаще ыидеть тебя без формы."
        show yuuna neu
        voice "audio/voice/E1/D5/S3/yuuna/10.ogg"
        ym "Что?"
        "Она нахмурила лоб."
        pf "Потому что эта одежда тебе очень идёт."
        show yuuna cur
        voice "audio/voice/E1/D5/S3/yuuna/11.ogg"
        ym "Ох…"
        show yuuna smi
        voice "audio/voice/E1/D5/S3/yuuna/12.ogg"
        ym "Спасибо."
        
    "Странно видеть её не в форме.":
        pf "Ты выглядишь… по-другому."
        show yuuna ner
        "Она выглядела обеспокоенной."
        voice "audio/voice/E1/D5/S3/yuuna/13.ogg"
        ym "Что-то не так?"
        pf "Нет, просто странно видеть тебя в свитере."
        show yuuna cur
        voice "audio/voice/E1/D5/S3/yuuna/14.ogg"
        ym "О-Ох… Тебе не нравится?"
        pf "Всё нормально."

    "Ничего не говорить.":
        "Это нормально, что она не в форме, так как сегодня суббота, я ведь тоже не в ней. Нет смысла обсуджать это, когда мы можем приступить к работе."
        show yuuna cur
        "Я заметил, что Юна тоже на меня смотрела."

show yuuna smi with dissolve
"Она улыбнулась."
voice "audio/voice/E1/D5/S3/yuuna/15.ogg"
ym "Немного забавно витель тебя не в форме, но в хорошем смысле. Это кажется более личным."
pf Да, я понял."
"Она показала на книгу рядом со мной."
show yuuna cur
voice "audio/voice/E1/D5/S3/yuuna/16.ogg"
ym "Ты уже выбрал справочники?"
"Я кивнул."
pf "Я не мог найти нужный пример, пока ждал тебя."
voice "audio/voice/E1/D5/S3/yuuna/17.ogg"
ym "Ты проверил базу данных?"
pf "Ещё нет."
show yuuna smi
voice "audio/voice/E1/D5/S3/yuuna/18.ogg"
ym "Давай сделаем это."
hide yuuna with dissolve
show yuuna smi at l3 with dissolve
$renpy.pause(.5)
"Она встала и направилась к ближайшему компьютеру. Мы добрались до него, и она быстро печатала в поисковике."
show yuuna thi with dissolve
voice "audio/voice/E1/D5/S3/yuuna/19.ogg"
ym "Тут говорится, что книга доступна… Пойдём снова поищем на стеллажах."
hide yuuna with dissolve
"Она повела меня обратно к полкам, время от времени оглядываясь на меня. Как только мы пришли, она осматривала полку и хмурилась, когда увидела книгу."
show yuuna dis at cc with dissolve
show storm:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
$renpy.pause(.5)
voice "audio/voice/E1/D5/S3/yuuna/20.ogg"
ym "Я не понимаю. Она должна быть тут."
pf "Может, комрьютер ошибся."
voice "audio/voice/E1/D5/S3/yuuna/21.ogg"
ym "Возможно… но без неё мы не можем работать над проектом."
pf "Почему бы нам не спросить у библиотекаря? Может он знает, где она."
show yuuna smi
"Она оживилась."
voice "audio/voice/E1/D5/S3/yuuna/22.ogg"
ym "Хорошая идея."
"Я начал возвращаться туда, откуда мы пришли, когда заметил телегу рядом с нами. Она была заполнена книгами, но в глаза бросился определенный заголовок."
pf "Подожди-ка--"
show yuuna cur with dissolve
"Она остановилась."
pf "Не эта ли книга нам нужна?"
"Она наклонилась посмотреть."
show yuuna hap
voice "audio/voice/E1/D5/S3/yuuna/23.ogg"
ym "Это она!"
pf "Отлично!"
"Я потянулся, чтобы взять её..."
show shocked:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
show yuuna sur with dissolve
"...но остановился, когда заметил испуганную Юну."
pf "Что?"
voice "audio/voice/E1/D5/S3/yuuna/24.ogg"
ym "Мы не можем просто взять её."
pf "Почему нет?"
show yuuna cur
voice "audio/voice/E1/D5/S3/yuuna/25.ogg"
ym "Это тележка возврата."
pf "И?"
voice "audio/voice/E1/D5/S3/yuuna/26.ogg"
ym "Книга ещё не возвращена."
pf "Что ты имеешь в виду? В системе написано, что она возвращена, и она в тележке."
show yuuna neu
voice "audio/voice/E1/D5/S3/yuuna/27.ogg"
ym "Да, но её ещё не вернули на свою полку."
pf "Все будет хорошо. Мы можем сделать копию нужного нам раздела, а затем положить ее обратно в тележку."
show yuuna ner
voice "audio/voice/E1/D5/S3/yuuna/28.ogg"
ym "Но что если кто-то заметит пропажу?"
"Я оглянулся. Библиотекаря нигде не было видно."
pf "Здесь никого нет. К тому же, мы всё сделаем быстро. Не волнуйся."
show yuuna thi
"Она нервно закусила губу, прежде чем неохотно кивнула."
hide yuuna with dissolve
"Я взял книгу, и мы направились к копировальному аппарату. Юна быстро и проворно шагала, мне нужно было её догонять. Она часто оглядывалась на меня, ей было явно некомфортно."
"Она отступила назад, когда мы достигли копировального аппарата, занялся копированием. Машина прогрелась за пару минут, а Юуна все время ёрзала."
show yuuna neu at cc with dissolve
voice "audio/voice/E1/D5/S3/yuuna/29.ogg"
ym "Она рабоатет?"
pf "Да, ей просто нужно пара минут."
show panic:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
show yuuna thi
voice "audio/voice/E1/D5/S3/yuuna/30.ogg"
ym "Мы должны поторопиться."
pf "Не волнуйся, всё будет хорошо."
"Она не выглядела убеждённой, но молчала. Казалось, что секунды растягивались и замедлялись, пока мы ждали, когда машина обработает копии. Юуна продолжала кусать губу."
"Наконец, копировальный аппарат выплюнул наши документы. Юна быстро собрала их и пошла. Она ускорилась, когда мы приблизиилсь к телеге, и не расслаблялась, пока я не вернул книгу её собратьям."
pf "было не так уж и плохо, не так ли?"
show yuuna smi
"Она слабо улыбнулась, но её лицо было немного бледным."
voice "audio/voice/E1/D5/S3/yuuna/31.ogg"
ym "По крайней мере мы получили то, что нам нужно."
pf "Кстати об этом, Нам нужн овернуться к работе."
"Она кивнула и мы вернулись в нашу комнату."




stop ambient fadeout 3.0
stop music fadeout 2.0
scene black with fade
$renpy.pause(1.5)
play ambient "audio/ambience/Ace Academy Library.ogg" fadein 2
play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 3
scene bg campus library dusk with fade

$renpy.pause(1.0)



"Я набрал последние пару слов в нашем отчете, и откинулся на стуле, усмехаясь Юне."
pf "Ииии...мы закончили!"

show yuuna hap at cc with dissolve
"Она вздохнула с облегчением."
show note:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
voice "audio/voice/E1/D5/S3/yuuna/32.ogg"
ym "Я рада, что мы закончили. Теперь не придётся беспокоиться об этом до конца недели."
pf "Ага."
show yuuna smi
"Мы долго занимались, и было довольно поздно."
"Юуна уже складывала свой ноутбук, так что я тоже сложил свой. Затем она взяла справочники."
voice "audio/voice/E1/D5/S3/yuuna/33.ogg"
ym "Я пойду верну их."
pf "Может мне помочь с этим?"
voice "audio/voice/E1/D5/S3/yuuna/34.ogg"
ym "Нет, спасибо. Это займёт минуту."
hide yuuna with dissolve
"Она обнадёживающе улыбнулась перед уходом."
"Я убирал комнату, пока она занималась книгами, и встретился с ней уже на улице."



stop ambient fadeout 3.0
scene black with fade
$renpy.pause(1.5)
scene bg campus building dusk with fade

show yuuna smi at cc with dissolve
voice "audio/voice/E1/D5/S3/yuuna/35.ogg"
ym "Ну, мне лучше пойти на автобусную остановку."
pf "Я провожу тебя."

show yuuna cur
voice "audio/voice/E1/D5/S3/yuuna/36.ogg"
ym "Ох, тебе не стоит."
pf "Я приехал сюда, поэтому не проитв. К тому же, уже довольно поздно, и кто знает, сколько придётся ждать автобус."

show yuuna smi
"Она улыбнулась и кивнула."


scene black with fade
$renpy.pause(1.5)
scene bg campus intersection dusk with fade


show yuuna smi at cc with dissolve
"Когда мы пришли автобусная остановка была пуста, и, как и ожидалось, автобуса нигде не было."
voice "audio/voice/E1/D5/S3/yuuna/37.ogg"
ym "Мы сегодня много сделали. С тобой очень легко работать."
pf "Спасибо. На мгновение я подумал, что ты готова кинуть меня."
show yuuna cur
"Она с любопытством посмотрела на меня."
voice "audio/voice/E1/D5/S3/yuuna/38.ogg"
ym "Когад это?"
pf "Когда мы нашли нужную книгу."
voice "audio/voice/E1/D5/S3/yuuna/11.ogg"
ym "Ох..."
show yuuna thi
"She shifts slightly."
voice "audio/voice/E1/D5/S3/yuuna/39.ogg"
ym "Я думала ою этом. Я никогда не делал ничего подобного раньше."
"Теперь была моя очередь выглядеть растерянным."
pf "Ты никогда не брала книгу?"
show yuuna neu
voice "audio/voice/E1/D5/S3/yuuna/40.ogg"
ym "Нет, я никогда {i}без разрешения{/i} не брала книгу."
pf "Это не то что бы было без разрешения..."
show yuuna dis
voice "audio/voice/E1/D5/S3/yuuna/41.ogg"
ym "Мы полностью нарушили правила!"
pf "Незнаю, зашли ли мы так далеко."
voice "audio/voice/E1/D5/S3/yuuna/42.ogg"
ym "Мы зашли! Ты не должен использовать книгу, которая находится в корзине возврата. Она ещё не обработана."
pf "Да, но это незначительная вещь. Это как когда забываешь убирать поднос в кафетерии."
show yuuna neu
"Она смотрела прямо на меня."
pf "... Ты забываешь убирать свой поднос?"
voice "audio/voice/E1/D5/S3/yuuna/43.ogg"
ym "Конечно нет. Ты должен убирать за собой."
pf "Хорошо, тогда это как..."

label E1D5S3_YuunaLoopbackStart:
menu:
    "Взять дополнительные палочки для еды и салфетки." if (E1D5S3_YuunaLoopbackOption1 == 0):
        $ E1D5S3_YuunaLoopbackOption1 = 1
        $ E1D5S3_YuunaLoopbackCounter = E1D5S3_YuunaLoopbackCounter + 1
        pf "Когда ты берёшь еду и ещё дополнительные палочки для еды и салфетки в баре самообслуживания."
        show yuuna dis
        "Юна нахмурилась."
        voice "audio/voice/E1/D5/S3/yuuna/44.ogg"
        ym "Мне нужна только одна пара палочек для еды."
        pf "Они на потом."
        voice "audio/voice/E1/D5/S3/yuuna/45.ogg"
        ym "Если все будут брать допольнительно чебе что-то, тогда ничего не останется для других."

    "Взять ручку из банка." if (E1D5S3_YuunaLoopbackOption2 == 0):
        $ E1D5S3_YuunaLoopbackOption2 = 1
        $ E1D5S3_YuunaLoopbackCounter = E1D5S3_YuunaLoopbackCounter + 1
        pf "Когда ты идёшь в банк--или куда-нибудь, где свободно лежат ручки--берёшь одну из ручек после использования."
        show yuuna sur
        voice "audio/voice/E1/D5/S3/yuuna/46.ogg"
        ym "Но это {i}воровство{/i}!"
        pf "Обычно это случайность--ты не понимаешь этого, пока не стало слишком поздно."
        show yuuna dis
        show storm:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        $renpy.pause(1.5)
        voice "audio/voice/E1/D5/S3/yuuna/47.ogg"
        ym "Случайность или нет--это все ещё сбор того, что не принадлежит тебе."

    "взять большей одной послеобеденной мятной конфеты в ресторане." if (E1D5S3_YuunaLoopbackOption3 == 0):
        $ E1D5S3_YuunaLoopbackOption3 = 1
        $ E1D5S3_YuunaLoopbackCounter = E1D5S3_YuunaLoopbackCounter + 1
        pf "Когда в ресторане есть миска мяты или конфеты для клиентов, чтобы взять после еды, и вы берёшь больше одной."
        show yuuna thi
        "Она наморщиалсь."
        voice "audio/voice/E1/D5/S3/yuuna/48.ogg"
        ym "Я не верю, что это обычай в Японии."
        pf "Ох, должно быть это американский обычай."

    "Взять дополнительные бесплатные образцы." if (E1D5S3_YuunaLoopbackOption4 == 0):
        $ E1D5S3_YuunaLoopbackOption4 = 1
        $ E1D5S3_YuunaLoopbackCounter = E1D5S3_YuunaLoopbackCounter + 1
        pf "Когда магазин предлагает бесплатные образцы, и ты ждёшь некоторое время, прежде чем вернуться снова, чтобы человек, раздающий образцы, не узнал тебя."
        show yuuna neu
        voice "audio/voice/E1/D5/S3/yuuna/49.ogg"
        ym "Но как насчет людей, которые еще не получили образец?"
        pf "Что насчёт них?"
        show yuuna dis
        voice "audio/voice/E1/D5/S3/yuuna/50.ogg"
        ym "Если я возьму их, у них не будет."
        pf "У них обычно есть много того, что они отдают…"

    "Использование нескольких электронных писем для голосования за участие в конкурсе, когда это один голос на человека." if (E1D5S3_YuunaLoopbackOption5 == 0):
        $ E1D5S3_YuunaLoopbackOption5 = 1
        $ E1D5S3_YuunaLoopbackCounter = E1D5S3_YuunaLoopbackCounter + 1
        pf "Когда в конкурсе говорится, что это только один голос на человека, вы используете свои другие учетные записи электронной почты, чтобы проголосовать за понравившуюся вам запись."
        show yuuna neu
        voice "audio/voice/E1/D5/S3/yuuna/51.ogg"
        ym "Но это все равно будет голосование более одного раза за человека, потому что эти письма принадлежат мне."
        pf "Технически, полагаю так и есть."
        voice "audio/voice/E1/D5/S3/yuuna/52.ogg"
        ym "Это несправедливое преимущество."
        pf "Нет, если все это делают."
        show yuuna dis
        "Она неодобрительно посмотрела на меня."

        
if (E1D5S3_YuunaLoopbackCounter == 3):
    jump E1D5S3_YuunaLoopbackEnd

else:
    pf "Хорошо, как насчёт..."
    jump E1D5S3_YuunaLoopbackStart


label E1D5S3_YuunaLoopbackEnd:

$renpy.pause(.5)
show yuuna cur with dissolve
$renpy.pause(.5)
voice "audio/voice/E1/D5/S3/yuuna/53.ogg"
ym "Ты делаешь все эти вещи?"
pf "Жм... нет..."
"Она смотрела на меня с широко раскрытыми глазами."
voice "audio/voice/E1/D5/S3/yuuna/54.ogg"
ym "Но это наршение правил."
pf "Они больше похожи на рекомендации."
show yuuna thi
voice "audio/voice/E1/D5/S3/yuuna/55.ogg"
ym "Я-Я никогда не нарушала правила."
pf "Ни разу?"
show yuuna dis
voice "audio/voice/E1/D5/S3/yuuna/56.ogg"
ym "Это привело бы к полному хаосу, если бы все игнорировали правила и делали то, что хотели."
pf "Как этот автобус, да?"
show yuuna cur
voice "audio/voice/E1/D5/S3/yuuna/57.ogg"
ym "Что?"
pf "Ну, в расписании сказано, что он должен был быть здесь около получаса назад, но уже поздно."
show yuuna thi with dissolve
voice "audio/voice/E1/D5/S3/yuuna/11.ogg"
ym "Ох..."
show storm:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
show yuuna dis
"Она выглядела разочарованной."
voice "audio/voice/E1/D5/S3/yuuna/58.ogg"
ym "Я надеялась, что проблема с автобусом решится сама собой, прежде чем мне нужно будет ехать домой."
pf "Не похоже, что он приедет. Кто-нибудь может тебя подобрать?"
"Она покачала головой."
show yuuna neu
voice "audio/voice/E1/D5/S3/yuuna/59.ogg"
ym "Моя семья не в городе в эти выходные. Это нормально, я постоянно езжу на автобусе."

label E1D5S3_StayLongerLoop:
menu:
    "Go home.":
        pf "Are you sure you'll be okay here?"
        show yuuna smi
        "She nods."
        voice "audio/voice/E1/D5/S3/yuuna/60.ogg"
        ym "Yes."
        pf "Alright, then I better get back before it gets too late."
        show yuuna smi
        voice "audio/voice/E1/D5/S3/yuuna/61.ogg"
        ym "Sure."
        pf "Text me when you get home."
        voice "audio/voice/E1/D5/S3/yuuna/62.ogg"
        ym "Okay."
        "She waves goodbye and I wave back, before heading to my bike and driving home."
        jump E1D5S7

    "Stay with her longer." if (E1D5S3_StayWithYuunaLoop == 0):
        $ E1D5S3_StayWithYuunaLoop = 1
        pf "Well, I'll wait with you a while longer. Hopefully it'll show up."
        show yuuna smi
        "She brightens up."
        voice "audio/voice/E1/D5/S3/yuuna/63.ogg"
        ym "You don't have to do that, but thanks. It's always nice to have company."
        
        scene black with fade
        $renpy.pause(1.5)
        scene bg campus intersection dusk with fade
        
        show yuuna thi at cc with dissolve
        
        "After another half an hour, the bus still doesn't show up."
        jump E1D5S3_StayLongerLoop

    "Offer her a ride.":
        pf "I can take you home."
        show yuuna smi
        "She smiles but shakes her head."
        voice "audio/voice/E1/D5/S3/yuuna/64.ogg"
        ym "I don't want to cause any trouble for you. I don't mind waiting."

        if (E1D2S2_talkwithyuunayes == 1):
            pf "It's no trouble at all. We ride the same bus line so you're on my route home."

        else:
            pf "You're waiting for bus 85 which goes to my area of Isokaze as well. It's no trouble at all."

voice "audio/voice/E1/D5/S3/yuuna/65.ogg"
ym "That's very kind of you, but you don't have to worry about me. I'm used to waiting for the bus."
pf "I know, but it's getting late and if I left you here alone I'd be worried you never got home safely."
show yuuna cur b1 with dissolve
"Her cheeks tinge pink and she looks away, a small smile playing at her lips."
voice "audio/voice/E1/D5/S3/yuuna/66.ogg"
ym "You'd be worried about me?"
pf "Yeah."
show yuuna smi b1
"She looks back at me, a full smile on her face."
voice "audio/voice/E1/D5/S3/yuuna/67.ogg"
ym "Well, it will get dark soon... and I wouldn't want you to worry..."
"I grin at her."
pf "Come on, let's go pick up my bike."
show yuuna hap b1
"She returns my smile with an even brighter smile."
voice "audio/voice/E1/D5/S3/yuuna/68.ogg"
ym "Okay, thanks."



stop ambient fadeout 3.0
scene black with fade
$renpy.pause(1.5)
scene bg campus parking dusk empty with fade


"When we reach my bike, Yuuna's eyes widen in appreciation."
show yuuna cur at cc with dissolve
voice "audio/voice/E1/D5/S3/yuuna/69.ogg"
ym "You have a beautiful ride."
"I can't help myself from feeling a warmth of pride."
pf "Thanks! I brought her back from the States. She goes everywhere with me."
"I hop on my bike and pat the seat behind me. She carefully climbs on."
pf "Are you ready?"
show yuuna thi
voice "audio/voice/E1/D5/S3/yuuna/70.ogg"
ym "Um..."
pf "What is it?"
voice "audio/voice/E1/D5/S3/yuuna/71.ogg"
ym "What am I supposed to hold on to?"
pf "Oh... well, you're kind of supposed to hold onto me..."
show shoBlush:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
show yuuna sur b2 with dissolve
voice "audio/voice/E1/D5/S3/yuuna/72.ogg"
ym "What?!"
pf "What's wrong?"
show yuuna ner b2
show panic:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
voice "audio/voice/E1/D5/S3/yuuna/73.ogg"
ym "Um, this was a bad idea. I--I should go wait for the bus."
"I feel her squirm behind me."

$ qtebase = 3
$ qtetotal = qtebase
$ t_var = qtetotal
show screen timer_scr(place="E1D5S3_timeout")

menu:
    "Help her.":
        $ renpy.hide_screen ("timer_scr")
        $ E1D5S3_HelpedYuuna = 1
        "Before she can hop off the bike, I reach back, grab her hands, and wrap her arms around my waist. Yuuna lets out a small gasp."
        pf "See? This isn't so bad, right?"
        show yuuna cur b2
        voice "audio/voice/E1/D5/S3/yuuna/74.ogg"
        ym "Umm, r--right..."

    "Let her go.":
        label E1D5S3_timeout:
        $ renpy.hide_screen ("timer_scr")
        "In one smooth motion she slides off the bike. Her cheeks are as pink as her hair."
        show yuuna smi b2
        voice "audio/voice/E1/D5/S3/yuuna/75_2.ogg"
        ym "Thank you for the offer."
        pf "Are you sure you don't want a ride?"
        voice "audio/voice/E1/D5/S3/yuuna/76_2.ogg"
        ym "Yeah, I'll see you another time."
        pf "Okay..."
        "She gives me one last smile before turning away. Once she's out of sight, I start my engine and go home."
        jump E1D5S7


stop ambient fadeout 3.0
scene black with fade
play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 4
$renpy.pause(3.0)

play sound2 "audio/sfx/Vehicles/Bike driving off.ogg" fadein 3 fadeout 5
$renpy.pause(3.0)

"I can feel the warmth of Yuuna against me and the softness of her chest pressing against my back...{w} I try not to think about it."
stop music fadeout 12

"Her grip tightens around my waist as we continue down the freeway."
"Yuuna diligently directs me towards her house. The scenery blends into a blur of colour as we drive by."
"After a few minutes, Yuuna's directions sound more confident and there's a tinge of excitement in her voice. Her grip relaxes slightly and I'm acutely aware of every time she presses close to me to speak."
"I feel her hand slip away for a moment--I assume to push the hair out of her eyes--and her chest pushes up against me again as she sighs."
pf "Are you okay?"
voice "audio/voice/E1/D5/S3/yuuna/75.ogg"
ym "Yes--sorry--I just love sunsets and the view right now is breath-taking."

play music "audio/music/Tender Moments (GAME VERSION).ogg" fadein 3.0

$renpy.pause(1.0)
$ persistent.gpix[64][0] = 1
show cg yuuna bike evening:
    alpha 0
    xzoom .60
    yzoom .60
    yoffset -50
    xoffset 150
    
show cg yuuna bike evening:
    parallel:
        easein 3.0 alpha 1.0
    parallel:
        easein 3.0 xoffset 50


$renpy.pause(2.0)

"I quickly glance towards the sun as it hovers over the horizon, reflecting a trail of golden fire on the glittering waves of the ocean."
pf "You definitely don't see sunsets like these in New York. I could get used to this."
voice "audio/voice/E1/D5/S3/yuuna/76.ogg"
ym "Are you liking it in Isokaze so far?"
pf "Yeah, but I haven't seen much outside of ACE."
voice "audio/voice/E1/D5/S3/yuuna/77.ogg"
ym "You should go to the park. It's so beautiful--especially in spring when the cherry blossoms bloom. I used to go there all the time and play on the statues."
voice "audio/voice/E1/D5/S3/yuuna/78.ogg"
ym "You'll learn a lot about the town's culture and history there too. Although I haven't been there since--a while so I'm not sure if it's changed at all."
pf "Maybe you can come with me and show me."
"She pauses." 

voice "audio/voice/E1/D5/S3/yuuna/79.ogg"
ym "Sure… After all, Isokaze is a pretty special place."
pf "Yeah, I'm beginning to see that."
"She leans closer into me, but doesn't say anything more." 

show cg yuuna bike evening:
    parallel:
        linear 3.0 xoffset 0
    parallel:
        linear 3.0 yoffset -50
    parallel:
        linear 3.0 xzoom .5
    parallel:
        linear 3.0 yzoom .5
    parallel:
        linear 2.5 alpha 0

$renpy.pause(2.0)
stop music fadeout 3.0
scene black with fade     
$renpy.pause(1.0)

"Before long, we arrive at her house."

play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 4.0
scene bg isokaze neighborhood night with fade

"She slips off the bike and waits for me to do the same. As I walk her to her front door, she turns to me. I don't anticipate her stopping and almost trip into her, but catch myself just in time. Still, I hear a slight gasp when she notices how close we are to each other. She suddenly becomes shy and takes a small step back."

show yuuna smi b1 at cc with dissolve

voice "audio/voice/E1/D5/S3/yuuna/80.ogg"
ym "Thanks for taking me home. I had a nice time today."
pf "Me too. Maybe we can hang out again?"
voice "audio/voice/E1/D5/S3/yuuna/61.ogg"
ym "Sure."
pf "And do something besides study."

show yuuna hap b1
"She laughs."
show regBlush:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
voice "audio/voice/E1/D5/S3/yuuna/81.ogg"
ym "I'd like that."

show yuuna smi b1 with dissolve
voice "audio/voice/E1/D5/S3/yuuna/82.ogg"
ym "Have a good night. Get home safely, okay?"
pf "I will. Talk to you later."
hide yuuna with dissolve
$renpy.pause(.5)
"She turns towards her door while I go back to my bike. As I switch on the engine, I see her turn around. She gives me a brief wave before heading inside, and I wave back before heading home."

stop music fadeout 3.0
scene black with fade
$renpy.pause(2.0)   


jump E1D5S7
