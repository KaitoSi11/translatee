label E1D2S1:
    
    $renpy.pause(2.0)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1.5)
    #BG Black background transition into daytime room background but hazy / unfocused.
    scene bg homekaito myroom blurry with Dissolve(2.5)
    scene black with fade
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(2.5)
    pf "Что…?"
    scene bg homekaito myroom blurry with fade
    "Мягкие солнечные лучи проходят через окно, грея мою щёку. Мелодичное пение птиц вдалеке почти утоплено в раздражающем звуке будильника."
    "Я отвернулся от окна и увидел \"7:00 AM\" на часах."
    pf Неужели уже утро?"
    
    menu:
        "Так и есть. Пора вставать":
            $ E1D2S1_timetogetup = 1
            $ E1D2S1_okaytimetogo = 0
            $ E1D2S1_almostup = 0
            stop sound
            play sound "audio/sfx/Technology/Button Click.ogg"
            "Я выключил будильник. Я никогда не был жаворонком, но вообще-то и не чувствовал себя таким же уставшим как обычно… Я даже чувствовал себя переполненным энергией. {w}Полагаю, джетлаги как-то странно работают. По крайней мере, я не опоздаю в свой первый день." 
            scene white with fade
            scene bg homekaito myroom day with Dissolve(2)
            play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
            
            "Встав с кровати, я на автомате начал свой утренний ритуал. Не раздумывая, я взял джинсы и почти надев их заметил форму, валяющуюся на стуле."
            pf "Чёрт…"
            "К этому придётся привыкнуть…"
            "Я снял джинсы и взял форму. Должен признать, что касается формы, эта довольно-таки неплоха. Она немного яркая для моего вкуса и, совсем не то, чего я ожидал, но разрез льстит, а тиановые полосы выглядят довольно круто."
            "Я взглянул в зеркало, чтобы поправить галстук. {w}Узел мог бы быть лучше, но у меня не было много случаев, в которых мне нужно было одевать гастук {w}Я всё ещё выгляжу чертовски хорошо, и это всё, что имеет значение."
            "После быстрой проверки, чтобы убедиться, что собрал все вещи, я спустился вниз." 
            scene black with fade
            play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
            $renpy.pause(3)
    
        "Ещё 5 минут...":
            stop sound
            play sound "audio/sfx/Technology/Button Click.ogg"
            "Я нажал кнопку \"повтора\" и вознаградился блаженной тишиной. {w}Ещё пять минут и я буду готов встретить мир."
            scene black with fade
            "…"
            play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
            $renpy.pause(3)
            "Ещё {b}не могло{/b} пройти пять минут.{w} За что вы меня ненавидите, часы?"
    
            menu:
                "Хорошо, пора вставать.":
                    $ E1D2S1_timetogetup = 0
                    $ E1D2S1_okaytimetogo = 1
                    $ E1D2S1_almostup = 0
                    stop sound
                    play sound "audio/sfx/Technology/Button Click.ogg"
                    "Хорошо, я сейчас встану. {w}Если я пролежу ещё больше, то вообще не уйду из дома."
                    scene bg homekaito myroom blurry with fade
                    scene white with fade
                    scene bg homekaito myroom day with Dissolve(2)
                    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
                
                    "Собрав аолю и решительность, я покинул тёплую кровать {w}Утро и я никогда не виделись лицом к лицу, и я шатался по комнате как зомби. Я автоматически бросил вещи в свою сумку и надеялся, что получил всё, что мне нужно. {w}Я думал, что получил. {w}Если нет, то узнаю об этом в школе."
                    "Я заканчил одеваться в джинсы и футболку, и собирался спуститься вниз, когда заметил тёмную форму, лежащую на стуле."
                
                    "Чьей идеей было заставлять всех носить форму?"
                
                    "Я вздохнул и переоделся в форму. {w}Я не могу вспомнить последний раз, когда мне нужен галстук или пиджак ... или даже брюки."
                    "Ну да пофиг. {w}Чувствуя себя немного более живым, я схватил свою сумку и спустился вниз."
                    scene black with fade
                    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
                    $renpy.pause(3)
            
                "Я пости проснулся… zzz...":
                    $ E1D2S1_timetogetup = 0
                    $ E1D2S1_okaytimetogo = 0
                    $ E1D2S1_almostup = 1
                    stop sound
                    play sound "audio/sfx/Technology/Button Click.ogg"
                    "Я снова нажал кнопку \"повтора\". {w}Утро не должно быть замечено. {w}Я же могу позволить себе поспать немного подольше? {w}Мне не нужно долго собираться. {w}Я просто посплю ещё пять минут… {w}Может быть десять…"
                    $renpy.pause(3)
                    "…"
                    play sound "audio/sfx/Human/Poke Noise.ogg"
                    $renpy.pause(1)
                    "Что-то бьёт меня в бок."
                    
                    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
                    voice "audio/voice/E1/D2/S1/Nikki/1.ogg"
                    sf "Эй! Просыпайся! Ты опоздпешь!"
                
                    "Ух, какая гарпия кричит мне в ухо? {w}Кыш, кыш…"
                    voice "audio/voice/E1/D2/S1/Nikki/2.ogg"
                    sf "Ты действительно хочешь опоздать в первый день?"
                    
                    play sound "audio/sfx/Human/Poke Noise.ogg"
                    $renpy.pause(1)
                
                    "Ох, точно... {w}школа. {w}Всё будет в порядке. {w}Ещё есть время."
                    
                    play sound "audio/sfx/Human/Poke Noise.ogg"
                
                    "Но удары по мне были настойчивы. Снова, и снова, и {i}снова{/i}."
                    
                    play sound "audio/sfx/Human/Poke Noise.ogg"
                    $renpy.pause(1)
                
                    pf "Хватит… {w}Прекрати--Никки!" 
                    stop music fadeout 3
                    scene bg homekaito myroom blurry
                    scene white with fade
                    scene bg homekaito myroom day with Dissolve(2)
                    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
                    show nikki smi at cc with dissolve
                
                    "Я скинул одеяло и встретился лицом к лицу с сестрой. Между нашими лицами была пара дюймов."
                    show note:
                        xoffset 720
                        yoffset 160
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D2/S1/Nikki/3.ogg"
                    sf "Доброе утро, принцесса."
                    "Я метал в неё ножи взглядом, но она отражала их улыбкой."
                
                    show nikki mis at cc
                    voice "audio/voice/E1/D2/S1/Nikki/4.ogg"
                    sf "Как мило с твоей стороны наконец присоединиться к миру живых. Я уже думала, что ты умер, судя по тому, сколько времени мне понадобилось, чтобы разбудить тебя."
                
                    pf "Тьфу."
                    
                    show nikki hap at cc
                    voice "audio/voice/E1/D2/S1/Nikki/5.ogg"
                    sf "Разве ты не рад, что я пришла и разбудила тебя?"
                
                    pf "Полагаю..."
                    
                    show nikki smi at cc
                    voice "audio/voice/E1/D2/S1/Nikki/6.ogg"
                    sf "Хмммм. И что бы ты делал без меня?"
                
                    pf "Спал."
                    
                    show nikki ann at cc
                    $renpy.pause(.5)
                    show storm:
                        xoffset 720
                        yoffset 160
                        xzoom .75
                        yzoom .75
                    $renpy.pause(1)
                    "Она скрестила руки и сурово посмотрела на меня."
                    voice "audio/voice/E1/D2/S1/Nikki/7.ogg"
                    sf "Никакого сна! Тебе нужно поесть, прежде чем идти. Я знаю, каково тебе, когда ты голоден, и я не стала бы подвергать кого-либо такой пытке."
                
                    "Она сбрасывает моё одеяло и идёт к двери."
                    show nikki dis at cc
                    voice "audio/voice/E1/D2/S1/Nikki/8.ogg"
                    sf "Я сделаю нам завтрак. Даже не думай снова засыпать!"
                    
                    hide nikki with dissolve
                
                    "Кто, я? {w}Да с кем она вообще думает, она говорит… со..."
                
                    #FX: Maybe have a small black fade in and out here to simulate him nearly dozing off again?
                    scene black with Dissolve(2.5)
                    scene bg homekaito myroom day with fade
                
                    "Воу--Это было близко."
                    "… {w}Мне действительно пора вставать."
                
                    "Зевая, я издал небольшой стон, когда потягивался, и практически выпал из постели. {w}Как только ноги вспомнили всоё предназначение, я начал собирать вещи. {w}Спотыкаясь по комнате, я врезался в стул и форма упала на пыльный пол."
                    pf "Отлично, давай будем выглядеть как бездомный студент."
                    "Я отряхнул форму, и мне удалось избавиться от большей части пыли. Достаточно хорошо."
                    "Ничто в этой форме не кажется естественным. Никто в моём возрасте не носит ежедневно костюм с галстуком. {w}К тому же, материал довольно жесткий, но полагаю, что это цена, которую ты платишь за крутой вид."
                    "После успешного переодевания, я провёл рукой по волосам, пытаясь уложить большую их часть, прежде чем взял сумку и спустился."
                    scene black with fade
                    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
                    $renpy.pause(3)
    
    stop ambient fadeout 2.0
    #BG kaito house day
    $renpy.pause(1)
    scene bg homekaito main day with fade
    $ nikOut = "sUniform"
        
    if (E1D2S1_timetogetup == 1) or (E1D2S1_okaytimetogo == 1):
        if (E1D2S1_timetogetup == 1):
            "Скоро я вошёл на кухню, нетерпя начать день. Пробуждение в такой час чувствуется большим достижением."
            show nikki smi at cc with dissolve
            "Никки подавила зевок, когда положила тарелку с яичницей и тостами. {w}Внезапно, я не чувствую такого успеха."
            pf "А мне ты тоже приготовила завтрак?"
            show nikki cur at cc with dissolve
            $renpy.pause(1)
            show dots:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            $renpy.pause(2.5)
            "Она удивлённо моргнула, и через пару секунд ответила."
            show nikki hap at cc with dissolve
            voice "audio/voice/E1/D2/S1/Nikki/9.ogg"
            sf "Вообще-то да."
            "Она усмехнулась, и положила ещё одну тарелку на стол."
            show nikki cur at cc
            voice "audio/voice/E1/D2/S1/Nikki/10.ogg"
            sf "Вгляни на себя, братец, встаёшь рано и сияешь. Ты переносишь \"новую жизнь\" на новый уровень."
            pf "Эй, я пытаюсь."
            pf "Где дядя Кайто?"
            show nikki neu at cc
            voice "audio/voice/E1/D2/S1/Nikki/11.ogg"
            sf "Он уже ушёл на работу, так что нам придётся самим закрывать дверь, когда пойдём."
            "Я кивнул, и она подошла ко мне с игривой улыбкой." 
    
        elif (E1D2S1_okaytimetogo == 1):
            show nikki neu at cc with dissolve
            "Подавляя зевоту, я медленно вваливаюсь на кухню и вижу Никки за столом. кушающую тосты. Она заметила, что я вошёл и её лицо озарилось улыбкой."
            show nikki hap at cc
            voice "audio/voice/E1/D2/S1/Nikki/12.ogg"
            sf "Отлично, ты встал! Я уже собиралась идти за тобой."
            pf "Ну, я уже здесь."
            voice "audio/voice/E1/D2/S1/Nikki/13.ogg"
            sf "Я сделала тосты. Хочешь?"
            pf "Хмхм."
            "Я сел за стол, но она просто засмеялась."
            show nikki smi at cc
            voice "audio/voice/E1/D2/S1/Nikki/14.ogg"
            sf "Они в тостере. Иди возьми сам."
            "Ворча, я взял тост и укусил."
            pf "Дяди Кайто нет?"
            show nikki neu at cc
            voice "audio/voice/E1/D2/S1/Nikki/15.ogg"
            sf "Он уже ушёл на работу."
            pf "Хм."
            "Я наслаждался тишикой, когда Никки подошла ко мне с игривой улыбкой." 
    
        show nikki smi at cc
        "В белой рубашке и клетчатой юбке она немного крутится на месте и выжидательно смотрит на меня."
        voice "audio/voice/E1/D2/S1/Nikki/16.ogg"
        sf "Ну как?"
    
        menu:
            "Она выглядит мило... Это сделает мою жизнь сложнее.":
                "Я скрестил руки и нахмурился."
                show nikki ner at cc
                voice "audio/voice/E1/D2/S1/Nikki/17.ogg"
                sf "Что?"
                pf "Нет."
                show panic:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S1/Nikki/18.ogg"
                sf "Нет?"
                pf "Нет, так не пойдёт."
                show nikki wor at cc
                voice "audio/voice/E1/D2/S1/Nikki/19.ogg"
                sf "Что не так?"
                "Беспокойство отражается на её лице, когда Никки начала нервно поправлять форму."
                show nikki sad at cc
                pf "Ох, ничего. я просто пытался выяснить как лучше доставить GEAR в твою школу."
                show nikki ske at cc
                "Она вопросительно подняла бровь."
                pf "Ну а как мне ещё удерживать всех парней от тебя?"
                show nikki smi b1 at cc with dissolve
                show regBlush:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                "Никки зизикнула, и её щёки немного порозовели."
                voice "audio/voice/E1/D2/S1/Nikki/20.ogg"
                sf "Ты смешон."
                pf "Я даже думаю написать строгое письмо в твою школу."
                voice "audio/voice/E1/D2/S1/Nikki/21.ogg"
                sf "О нет, не надо этого!"
                "Я улыбнулся, но Никки увидела заботу в моих глазах."
                show nikki neu at cc
                voice "audio/voice/E1/D2/S1/Nikki/22.ogg"
                sf "Я буду в порядке. я уже большая девочка, могу сама справиться."
                pf "Да, ты права."
                "Но как старший брат, я настаиваю на её защите, даже если она больше не нуждается в этой защите."
        
            "Что ты имеешь в виду этим \"ну как\"?":
                "..."
                "Я безучастно смотрел на нее."
                pf "\"Ну как\" что?"
                show nikki mis at cc
                "Она закатила глаза, но её голос всё ещё болезненно-сладкий."
                voice "audio/voice/E1/D2/S1/Nikki/23.ogg"
                sf "Ты не заметил никаких {i}изменений{/i} во мне сегодня?"
                pf "Хммм…"
                "Она подстриглась? {w}Нет. Покрасила волосы? {w}Нет. Изменила стиль? {w}Эм, возможно. Я не уверен. Должен ли я пойти в этом направлении?"
                show nikki dis at cc
                "{i}Тук, тук, тук.{/i}"
                "Никки стучит ногой, ее улыбка прерывается."
                "Я должен что-нибудь сказать, и поскорее."
                pf "Мне нравится то, что ты сделала со своими волосами?"
                show storm:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S1/Nikki/24.ogg"
                sf "Нет."
                "Мимо, хорошо. {w}Что насчёт её глаз? Контактные линзы другого цвета? {w}Нет, все ещё янтарные. Эмм…"
                
                #SFX Lightbulb
                play sound "audio/sfx/UI or Plot Element/Lightbulb.ogg"
                
                pf "Ага…!"
                pf "Это твоя дурацкая одежда!"
                show nikki sur b1 at cc with dissolve
                "Nikki's eyes widen. She kind of looks like she got the wind knocked out of her."
                pf "Я прав, не так ли?"
                show nikki wor at cc
                show panic:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S1/Nikki/25.ogg"
                sf "Дурацкая? О боже, я выгляжу так плохо?"
                pf "Эм, нет, конечно нет. Я имею в виду, что это плохой выбор, но если ты собиралась выглядеть как \"непослушная школьница\", то у тебя получилось."
                show nikki ann at cc
                show vein:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S1/Nikki/26.ogg"
                sf "Плохой выбор? Это моя форма, придурок! Я не \"выбирала\" одевать это!"
                "А, ну это многое объясняет. Форма. Как та, что сейчас на мне. Внезапно, моя форма выглядит не так уж и плохо."
                pf "Хаха, разве я сказал \"дурацкая\"? Я имел в виду \"отличная\". Ты хорошо выглядишь!"
                show nikki dis at cc
                voice "audio/voice/E1/D2/S1/Nikki/27.ogg"
                sf "Ах, хабудь. Заканчивай есть холодный тост. Мы опоздаем."
        
            "Моя сестра не можеть быть такой милой!":
                ##SFX: Poke Noise
                play sound "audio/sfx/Human/Poke Noise.ogg"
                show nikki win b1 at cc with dissolve
                "Слишком прелестно! Я щипал её за щёки, игнорируя протесты, пока она извивалась."
                show crying:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S1/Nikki/28.ogg"
                sf "Ааааааааай! П-Прекрати!"
                pf "KYAAAAA~! Kawaii desu!"
                show nikki ann b1 at cc
                "Никки нахмурилась, когда вырвалась из моих рук. Она осторожно похлопала себя по щеке, словно уверяя себя, она все ещё тут."
                "Я усмехаюсь и глажу её по голове."
                pf "Ооооооо, не злись."
                show nikki neu b1 at cc
                show tsuBlush:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S1/Nikki/29.ogg"
                sf "Хммм!"
                "Несмотря на её сердитый вид, я заметил следы появляющейся улыбки."
    
    elif (E1D2S1_almostup == 1):
        "Никки хмурилась, когда я наконец вошёл на кухню. Я не знаю, почему {i}она{/i} раздражена. Я один тут, кому не помешал бы ещё час сна."
        show nikki ann at cc with dissolve
        voice "audio/voice/E1/D2/S1/Nikki/30.ogg"
        sf "наконец-то! Я думала ты снова уснул."
        "Я поворчал в ответ, и сев за стол широко зевнул."
        #stomach growl
        play sound "audio/sfx/Human/Stomach Grumble.ogg"
        "Передо мной яичница с тостами, и мой желудок урчит в предвкушении еды. {w}Я с удовольствием налетаю на еду, но на первом укусе я осознаю кое-что"
        pf "Она холодная."
        show nikki dis at cc
        voice "audio/voice/E1/D2/S1/Nikki/31.ogg"
        sf "Вот что происходит, когда всё утро валяешься в постели. Теперь быстро ешь. Мы опоздаем."
        "Господи, кое-кто слишком раздражителен с утра."
    
    stop music fadeout 3
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 2
    "Мы закочили завтракать в тишине, пока Никки бросала на меня быстрые взгялы. {w}Я поглотил еду, собрал вещи и встретил Никки у двери."
    show nikki thi at cc with dissolve
    voice "audio/voice/E1/D2/S1/Nikki/32.ogg"
    sf "Как ты собираешься добираться до академии?"
    pf "На мотоцикле, естественно."
    show nikki ske at cc
    show question:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S1/Nikki/33.ogg"
    sf "А разве тебе не нужно разрешение? Я помню, ты волновался об этом."
    "Разрешение? {w}Я напрочь забыл оь этом! {w}Мне нужно разрешение на парковку мотоцикла, но у них должна же быть гостевая парковка, которую я могу использовать... Если найду место."
    "Итак, что мне сделать? {w}Взять мотоцикл, и надеяться на лучшее, или поехать на автобусе, а потом на мотоцикле, когда получу разрешение?" 
    
    menu:
        "Поехать на автобусе":
            $ E1D2S1_firstdaybus = 1
            pf "Ты права, сегодня я поеду на автобусе. Надо разобраться с ситуацией с парковкой, прежде чем брать мотоцикл."
            show nikki neu at cc
            "Никки согласно кивнула."
            voice "audio/voice/E1/D2/S1/Nikki/34.ogg"
            sf "На каком автобусе поедешь?"
            pf "На том, который движется на юг города."
            show nikki sad at cc
            "Она вздохнула."
            voice "audio/voice/E1/D2/S1/Nikki/35.ogg"
            sf "Эх, а я на том, что поедет на запад..."
            pf "Это не на этом же перекрёстке, не так ли?"
            show nikki thi at cc
            voice "audio/voice/E1/D2/S1/Nikki/36.ogg"
            sf "Нет, я так не думаю."
            pf "Ну... По крайней мере ты сможешь изучить город."
            show nikki neu at cc
            voice "audio/voice/E1/D2/S1/Nikki/37.ogg"
            sf "Да, ты прав."
            pf "Увидимся позже?"
            show nikki smi at cc
            voice "audio/voice/E1/D2/S1/Nikki/38.ogg"
            sf "Хорошо провести время в школе, окей?"
            "Она лучезарно улыбнулась мне."

            stop music fadeout 3
            scene black with fade
            jump E1D2S2
    
        "Взять мотоцикл":
            $ E1D2S1_firstdaybike = 1
            "Эх. Я уверен, все будет хорошо, если я возьму мотоцикл. {w}Там должна быть хоть {i}какая-то{/i} парковка, которая не требует разрешения."
            pf "Дааа… Я возьму мотоцикл."
            show nikki mis at cc
            voice "audio/voice/E1/D2/S1/Nikki/39.ogg"
            sf "Ох, точно. Конечно. Я и забыла как ты плакал, когда его забрали для транспортировки."
            pf "Очень забавно… Теперь я не предложу тебе прокатиться."
            show nikki neu at cc
            voice "audio/voice/E1/D2/S1/Nikki/40.ogg"
            sf "Даже если и предложил бы, то мне всё равно пришлось бы отказаться. I need to figure out how to navigate around Isokaze sometime, right?"
            pf "Правда? Если тебя увидят на моём мотоцикле, то это автоматически сделает тебя самой популярной девочкой в школе. Уверена, что хочешь пропустить такую отличную возможность?"
            show nikki mis at cc
            voice "audio/voice/E1/D2/S1/Nikki/41.ogg"
            sf "Пожалуйста, ты видел меня? С моей обаятельной улыбкой и шармом мне не нужен твой мотоцикл, чтобы быть популярной."
            pf "Как скажешь."
            show nikki smi at cc
            "Никки пошла на автобус, но остановилась и помахала на прощанье."
            voice "audio/voice/E1/D2/S1/Nikki/42.ogg"
            sf "Удачи в твой первый день!"
            pf "И тебе!"
    
    stop music fadeout 3
    scene black with fade
    jump E1D2S3

