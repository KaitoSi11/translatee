label E1D1S1:
    
    stop music fadeout 1
    
    scene black
    
    play ambient "audio/ambience/Bullet Train.ogg" fadein 4 fadeout 2

    $renpy.pause(2.0)
    
    play sound "audio/sfx/Vehicles/Bus Chime.ogg"
    $renpy.pause(1.5, hard=True)
    
    
    voice "audio/voice/E1/D1/S1/Train Announcer/1.ogg"
    "Диктор поезда" "Внимание пассажиры:"

    voice "audio/voice/E1/D1/S1/Train Announcer/2.ogg"
    "Диктор поезда" "Мы скоро прибудем в пункт назначения."

    voice "audio/voice/E1/D1/S1/Train Announcer/3.ogg"
    "Диктор поезда" "Пожалуйста, убедитесь, что не забыли никаких вещей."
    pf "...{w}...{w}..."
    
    $renpy.pause(.5)
    play sound "audio/sfx/Human/Poke_1.ogg"
    $renpy.pause(.75)
    
    pf "?!"
    
    "Что-то ударило меня по щеке! {w}Я отворачиваюсь от окна и вижу маленькую руку рядом со мной."
    
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
    #scene  bg travel train dusk with Dissolve(.1)
    scene white with dissolve
    scene bg travel train dusk at shaketrain with Dissolve(1.75)
    
    $renpy.pause(.25)

    
    show nikki smi b1 at cc with dissolve
    
    "Никки." 
    
    "Я глянул на её спящую позу. У неё всегда был немного беспокойный сон. Я отодвинул руку в её сторону, не так осторожно, как мог бы это сделать. Мы почти прибыли; она могла также проснуться."

    play sound "audio/sfx/Human/Poke_1.ogg"
    $renpy.pause(.75)
    
    "Она зашевелилась и потянулась с широким зевком, снова ударяя меня по лицу. {i}В этот{/i} раз она сделала это специально!"
    
    show nikki neu at cc with Dissolve(.75)
    $renpy.pause(.25)
    
    $renpy.pause(.25)
    voice "audio/voice/E1/D1/S1/Nikki/1.ogg"
    sf "Ох, привет, братец. Похоже, я задремала... Ты хорошо спал?"
    
    menu:
        "Отомстить!":
            
            "Я смотрю на неё краем глаза и так же широко потягиваюсь, задевая её щёку."
            
            play sound "audio/sfx/Human/Poke_1.ogg"
            show nikki win at cc, Shake(None, .3, dist=6)
            #Need shake effect
            $renpy.pause(.75)
            show nikki ann with dissolve
            voice "audio/voice/E1/D1/S1/Nikki/2.ogg"
            sf "Эй!"
            
            
            show nikki ann
            "Она шлёпает меня в ответ, но я просто смеюсь."
            pf Ой, извини. Не заметил тебя."
            voice "audio/voice/E1/D1/S1/Nikki/3.ogg"
            sf "Это было грубо!"
        "О каком это ещё \"сне\" ты говоришь?":
            pf "Я не смог поспать."
            show nikki cur
            voice "audio/voice/E1/D1/S1/Nikki/4.ogg"
            sf "Почему?"
            pf "Такое чувство, что рядом со мной был медведь... по крайней мере, по звукам так и было."
            show nikki sur with dissolve
            "Её глаза округлились."
            voice "audio/voice/E1/D1/S1/Nikki/5.ogg"
            sf "Ты хочешь сказать, что я храплю?"
            pf "Честно говоря, я удивлен, что это не разбудило тебя."
            show nikki dis with dissolve
            voice "audio/voice/E1/D1/S1/Nikki/6.ogg"
            sf "Ты же шутишь, да? Я действительно храплю?"
            pf "How can such a small person make such a {i}loud{/i} noise?"
            show nikki wor
            voice "audio/voice/E1/D1/S1/Nikki/7.ogg"
            sf "О Боже, Я больше никогда не смогу показать лицо на публике! Долгие поездки будут казаться ещё дольше, если я не смогу поспать! А что насчёт ночёвок? Как я вообще найду парня?"
            "Я больше не мог сохранять серьёзное лицо и рассмеялся."
            pf "Не, ты будешь в порядке, сестрёнка. Это был парень позади нас."
            show nikki ann with dissolve
            play sound "audio/sfx/Human/light_punch.ogg"
            with Shake((0, 0, 0, 0), .5, dist=5)
            "Она ударила меня в руку."
            voice "audio/voice/E1/D1/S1/Nikki/8.ogg"
            sf "Это не смешно!"
            show nikki neu with dissolve
            "Но я вижу как она сдерживает улыбку."
        "*Ворчать*":
            "Скрестив руки на груди, Я опускаюсь на свое место и бормочу себе под нос. Если бы я спал, это было бы грубым пробуждением, поэтому я считаю, что имею право быть немного сердитым."
            show nikki smi with dissolve
            voice "audio/voice/E1/D1/S1/Nikki/9.ogg"
            sf "Оооо, Кто-то у нас злюка!"
            "Как только она погладила меня по голове, я углубился в своё место,  мои протесты постепенно превращаются в низкое рычание."
            pf "Гррр…"
            "Никки лучится улыбкрй в моём направлении. По крайней мере, один из нас наслаждается этим."
    

    "Солнце светит в глаза, привлекая внимание. {w}Небо пылает красно-оранжевым цветом, пока солнце ползет к его отражению на сверкающем океане. {w}Лёгкий бриз колышет деревья за пределами побережья. Кажется, что листья прощаются с нами по мере того, как мы проезжаем мимо." 
    
    hide nikki with dissolve
    show nikki cur at r2 with dissolve
    voice "audio/voice/E1/D1/S1/Nikki/10.ogg"
    sf "Разве это не похоже на сказку?"
    
    stop music fadeout 5
    show nikki hap with dissolve
    "На ее губах улыбка, но ее теплые глаза ищут мои. Через мгновение она опустила глаза и опустилась обратно в кресло." 
    
    show nikki thi
    voice "audio/voice/E1/D1/S1/Nikki/11.ogg"
    sf "Знаешь, тебе не нужно было тоже ехать... Ты уже был на первом году обучения в CINY, и... тебе не стоило тоже ехать."
    
    $ E1D1S1_nikkimad = 0
    menu:
        "Отлично! Тогда я возвращаюсь.":
            play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
            pf "Какое облегчение! Я просто подожду, пока этот поезд развернется, а затем полечу первым же рейсом в Штаты."
            show nikki wor
            voice "audio/voice/E1/D1/S1/Nikki/12.ogg"
            sf "Ах!? Эмм..."
            "Её глаза округлились, и она закусила губу, пфтаясь скрыть беспокойство." 
            "Не могу ничего поделать, кроме как рассмеяться."
            pf "Мы начинаем здесь новую жизнь. Я бы ни за что тебя не бросил."
            show nikki neu with dissolve
            "Она расслабилась и улыбнулась."
            pf "Но более важно то, что я слышал, что японские девушки те ещё красавицы."
            show nikki smi
            "Никки все ещё улыбалась, но при этом закатила глаза."
            voice "audio/voice/E1/D1/S1/Nikki/13.ogg"
            sf "Ты смешон."
        "Для этого и нужны старшие братья.":
            play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
            pf "После всего, что произошло… мы - это всё, что осталось. Я не был бы хорошим братом,если бы позволил тебе переехать одной."
            show nikki neu with dissolve
            "Она вздызает, но всё ещё улыбается."
            voice "audio/voice/E1/D1/S1/Nikki/14.ogg"
            sf "Откуда мне знать, что ты собирался сказать что-то подобное?"
        "Кто-то должен позаботиться о тебе.":
            $ E1D1S1_nikkimad = 1
            pf "Если я не приеду, то кто же позаботится о тебе?"
            show nikki ann
            "Никки хмурится, и её вгляд уже не такой тёплый."
            voice "audio/voice/E1/D1/S1/Nikki/15.ogg"
            sf "Ни кому {i}не нужно{/i} заботиться обо мне. Я больше не ребёнок. У меня начнётся последний год в старшей школе!"
            pf "Это не то, что я имел в виду."
            "Легко забыть, что она уже не та маленькая девочка, которая притворяется больной, потому что слишком нервничает, чтобы начать свой первый день в школе. {w}Мы только что были выкорчеваны из единственной жизни, которую знали, но Никки - воплощение спокойствия, пока ждёт остановки поезда."
            pf "Никки…"
            hide nikki with dissolve
            $renpy.pause(.25)
            "Но она уже повернулась ко мне спиной и суетилась в кошельке."  
    
    stop music fadeout 3
    play sound "audio/sfx/Vehicles/Bus Chime.ogg"
    $renpy.pause(1.5, hard=True)
    
    voice "audio/voice/E1/D1/S1/Train Announcer/4.ogg"
    "Диктор поезда" "Мы прибыли на станцию Изоказе. Пожалуйста, не прислоняйтесь к дверям."
    
    if (E1D1S1_nikkimad == 1) :
        "Ничего не могу поделать, чувствую себя плохо."
    else:
        show nikki smi
        voice "audio/voice/E1/D1/S1/Nikki/16.ogg"
        sf "О, это наша остановка! Пойдём!"
    
    scene black with fade
    jump E1D1S2
    
