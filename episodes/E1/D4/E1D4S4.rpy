label E1D4S4:
    
    
    #Show school arena
    scene white with fade
    scene bg campus arena day with Dissolve(2.5)
    "Сидя в своих GEAR, мы вышли на круглую арену."
    "Студенты, спонсоры, профессора и другие общие зрители заполнили стадион. Большой экран показывал каждый наш шаг для тех, кто сидел сзади.{w} Толпа затихла, когда мы встали на свои места."
    "Энергетика была немного миже, чем для обычного матча… {w}Вероятно потому, что технически это все еще экзамен."
    play music "audio/music/Fight Song 1 (GAME VERSION).ogg" fadein 1
    show bg battleground day with dissolve:
        alpha 1
        xzoom 1
        yzoom 1
        yoffset 25
        xoffset 225
        
    show mayu mech at tl with dissolve:
        xzoom -.8
        yzoom .8
    show shou mech at tr with dissolve:
        xzoom -.8
        yzoom .8
    show kaori mech at mm with dissolve:
        xzoom -1
    show mc mech at bl with dissolve:
        xzoom -1
    "Across from us, the four enemy AIs enter."
    show bg battleground day:
        parallel:
            easein 3.0 alpha 1.0
        parallel:
            easein 3.0 xoffset -225
            
    show mayu mech at tl:
        xzoom -.8
        yzoom .8
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset -1500
            
    show shou mech at tr:
        xzoom -.8
        yzoom .8
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset -1500
            
    show kaori mech at mm:
        xzoom -1
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset -1300
            
    show mc mech at bl:
        xzoom -1
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset -1300
            
    # ai mechs
    $renpy.pause(2.5)
    show aiR neu at tr with dissolve:
        xzoom .8
        yzoom .8
            
    show aiR2 neu at tl with dissolve:
        xzoom .8
        yzoom .8
            
    show aiM neu at mm with dissolve
            
    show aiM2 neu at br with dissolve
    voice "audio/voice/E1/D4/S4/Kaori/3.ogg"
    ki "Все готовы?"
    
    "Коммуникаторы снова загорелись зелёным."
    $ E1D4S4matchPlan = 0

    
    menu:
        "Лучший способ помочь - придерживаться плана. Если я не буду в поле зрения, то не поставлю их в опасную ситуацию, в которой они потеряют преимущество.":
            $ E1D4S4_FollowMatchPlan = 1
            scene bg campus arena day with fade
            "Следуя плану Каори, я держался позади от действий."
            "Мои напарники встали на позиции. Маю держалась позади Сё и Каори, которые вели атаку."
            "Каори и Сё петляли между мехами ближнего боя и отвлекали их взрывами и бробиванием обороны. Маю прыгала от укрытия до укрытия, пока не встала на позицию. После она сделала снайперский выстрел в ИИ ближнего боя." 
            "Какое-то время они держали ритм."
            scene bg battleground day with fade
            $renpy.pause(.25, hard=True)
            show mayu mech at bl:
                xzoom -1
            show aiM att at br
            with dissolve
            
            show mayu att with dissolve
            $renpy.pause(.25)
            play sound "audio/sfx/GEAR Combat/Sniper.ogg"
            $renpy.pause(.5)
            play sound "audio/sfx/GEAR Combat/Hit.ogg"
            show aiM att at br, Shake(None, 1, dist=15)
            show aiM neu at br, Shake(None, 1, dist=15) with dissolve
            "Внезапный мощный рельсовый луч от Маю разбил один ИИ ближнего боя."
            voice "audio/voice/E1/D4/S4/Shou/1.ogg"
            ss "Молодец, Маю!"
            play sound "audio/sfx/GEAR Combat/Depower.ogg"
            hide aiM with dissolve
            voice "audio/voice/E1/D4/S4/Kaori/4.ogg"
            ki "Осталось ещё три."
            show aiR att at tr behind mayu with dissolve:
                xzoom .7
                yzoom .7
            pf "Маю, осторожно!"
            "ИИ дальнего боя нацелился на Маю. Она побежала за ближайшее укрытие, но не успевала."
            show shou att at cc behind mayu with dissolve:
                xzoom -.85
                yzoom .85
            "Перед тем, как выстрел поразил бы её, Сё встал и принял урон на себя."
            play sound "audio/sfx/GEAR Combat/Rifle.ogg"
            $renpy.pause(.35)
            show shou att at cc, Shake(None, 1, dist=15) behind mayu
            show shou mech at cc, Shake(None, 1, dist=15) behind mayu with dissolve
            voice "audio/voice/E1/D4/S4/Shou/2.ogg"
            ss "Аргх!"
            show mayu mech at bl with dissolve
            voice "audio/voice/E1/D4/S4/Mayu/1.ogg"
            ma "Сё!"
            voice "audio/voice/E1/D4/S4/Shou/6.ogg"
            ss "Прости, я всё."
            play sound "audio/sfx/GEAR Combat/Depower.ogg"  
            hide shou with dissolve
            voice "audio/voice/E1/D4/S4/Kaori/5.ogg"
            ki "Хиииийяяя!"
            show mayu mech at bl:
                parallel:
                    easein 1.5 alpha 1.0
                parallel:
                    easein 1.5 xoffset -1500
            play sound "audio/sfx/GEAR Combat/Sword Single.ogg"  
            show kaori att at tl with dissolve:
                xzoom -.7
                yzoom .7
            "Каори рванула к GEAR дальнего боя и разбила его одним мощным ударом."
            play sound "audio/sfx/GEAR Combat/Hit.ogg"  
            show aiR att at tr, Shake(None, 1, dist=15) with dissolve:
                xzoom .7
                yzoom .7
                xoffset 200
            $renpy.pause(1)
            show aiR neu at tr with dissolve:
                xzoom .7
                yzoom .7
                xoffset 0
            $renpy.pause(1)
            play sound "audio/sfx/GEAR Combat/Depower.ogg" 
            hide aiR with dissolve
            show kaori mech at tl with dissolve:
                xzoom -.7
                yzoom .7
            $renpy.pause(1)
            scene black with fade
            scene bg battleground day with fade
            show kaori mech at tr with dissolve:
                xzoom -.7
                yzoom .7
            show mayu mech at bl with dissolve:
                xzoom -1
            voice "audio/voice/E1/D4/S4/Mayu/2.ogg"
            ma "GEAR ближнего боя класса А приближается к моему местоположению."
            voice "audio/voice/E1/D4/S4/Kaori/6.ogg"
            ki "Поняла!"
            show kaori mech at tr with dissolve:
                xzoom .7
                yzoom .7
            show aiM att at mm with dissolve
            "Пока каори бежала к ней, Маю уклонилась от удара вражеского меха."
            play sound "audio/sfx/GEAR Combat/Sword Double.ogg" 
            play sound2 "audio/sfx/GEAR Combat/Dodge.ogg" 
            show mayu mech at bl:
                parallel:
                    easeout .75 alpha 1.0
                parallel:
                    easeout .75 xoffset -1300
            show aiM att at mm:
                parallel:
                    easeout .75 alpha 1.0
                parallel:
                    easeout .75 xoffset -1300
            $renpy.pause(1.5)
            voice "audio/voice/E1/D4/S4/Mayu/3.ogg"
            ma "Каори, твоё расчётное время прибытия?"
            show kaori mech at tr with dissolve:
                xzoom .8
                yzoom .8
            voice "audio/voice/E1/D4/S4/Kaori/7.ogg"
            ki "Почти здесь--"
            pf "Я только что засёк на радаре. {w}GEAR стрелок у--Каори!"
            show aiR att at tl with dissolve:
                xzoom -.7
                yzoom .7
            play sound2 "audio/sfx/GEAR Combat/Rifle.ogg" 
            $renpy.pause(.4)
            play sound "audio/sfx/GEAR Combat/Hit.ogg" 
            show kaori mech at tr, Shake(None, 1, dist=15) with dissolve:
                xzoom .8
                yzoom .8
                xoffset 150
                easeout .5 xoffset 250
            voice "audio/voice/E1/D4/S4/Kaori/8.ogg"
            ki "Кйяяя!"
            "Шквал лучей пробил щит Каори и отрубил её GEAR. {w}ИИ мех должно быть обошёл так, что бы напасть с незащищённой стороны. {w}Не думаю, что когда-либо видел, как запрограммированные GEARs что-то настолько стратегическое."
            play sound "audio/sfx/GEAR Combat/Depower.ogg" 
            hide kaori with dissolve
            hide mayu
            hide aiM
            $renpy.pause(1.0)
            voice "audio/voice/E1/D4/S4/Mayu/4.ogg"
            ma "Простите, я тоже всё... У меня нет снаряжения ближнего боя..."
            scene black with fade
            "Вся моя команда была в отключке, и оставшиемя ИИ GEAR медленно шли ко мне."
            scene bg battleground day with fade
            show mc mech at bl with dissolve:
                xzoom -1
            pf "Тааааак… насчёт нашего плана…"
            show aiR att at tr with dissolve:
                xzoom .8
                yzoom .8
            show aiM att at br with dissolve
            voice "audio/voice/E1/D4/S4/Shou/3.ogg"
            ss "Может попробуешь договориться с ними?"
            voice "audio/voice/E1/D4/S4/Kaori/9.ogg"
            ki "Хорош шутить! Нам все ещё нужно получить очки. Иди и нанеи столько урона, сколько сможешь."
            pf "Легче сказать, чем сделать."
            show mc ready at bl with dissolve:
                xzoom -1
            "Я бормотал про себя и встал в боевую стойку."
    
            #"Gameplay, with only dodge/block options"
            # This just means just doing the reaction game with only dodge/block visuals/sounds
            #$ E1D4S4matchPlan = 0
            #$ survived = 0
            #$ context = "E1D4S4_MatchPlanComplete"
            #$ enemy = "aiM"
            #$ mode = "retreat"
            
            #$ mcEnergyMax = 200
            #$ mcEnergy = 200
            #$ enemyHPMax = 100
            #$ enemyHP = 100
            
            #$ qtebase = 10
            #$ qtereaction = qteath + qtetrack + qtebase
            #$ qtetotal = qtereaction
            #$ t_var = qtereaction
            #show screen battle_screen
            #$renpy.pause(1)
            #show screen timer_scrReaction(place="E1D4S4_MatchPlanComplete")
            #jump qte_game
            # and jump here after finished
            
            
            
            
            "ИИ GEAR не тратили время и уже летели на меня с оружием наготове."

            
            label E1D4S4Combat1Loopback:
           
            
            $ qtetotal = 5
            $ t_var = qtetotal
            show screen timer_scr(place="E1D4S4_L1")
            menu:
                "Отпрыгнуть!" if E1D4S4_LOOPINGMENU1 == 0:
                    $ renpy.hide_screen ("timer_scr")
                    
                    
                    show aiM att at br:
                        xoffset 0
                        parallel:
                            easeout .1 alpha 1.0
                        parallel:
                            easeout .1 xoffset -250
                    $renpy.pause(.1)

                    play sound meleeSound
                    show aiM att at br with Dissolve(.2):
                        xoffset -400
                        
                    play sound2 dodSound
                    show mc dod at bl with Dissolve(.45):
                        parallel:
                            easeout .5 alpha 1.0
                        parallel:
                            easeout .5 xoffset -150
                    
                    "Я увернулся, и лезвия прорезали воздух. Пока ИИ приходил в себя после промаха, я ударил его в бок. Щит едва вспыхнул от удара!"
                    "GEAR застиг меня врасплох и ударил рукоятью меча, нанеся больше урона, чем хотелось бы."
                    
                    show mc mech at bl:
                        xoffset 0
                    show aiM neu at br:
                        xoffset 0
                    with dissolve
                    $E1D4S4_LOOPINGMENU1=1
                    jump E1D4S4Combat1Loopback

                "Блокировать!" if E1D4S4_LOOPINGMENU2 == 0:
                    $ renpy.hide_screen ("timer_scr")
                    
                    show aiM att at br:
                        xoffset 0
                        parallel:
                            easeout .1 alpha 1.0
                        parallel:
                            easeout .1 xoffset -250
                    $renpy.pause(.1)

                    play sound meleeSound
                    show aiM att at br with Dissolve(.2):
                        xoffset -400

                    show white with Dissolve(0.15):
                    play sound2 hitSound
                    hide white with Dissolve(0.25)
                    
                    show mc blo at bl, Shake(None, .5, dist=20):
                        xoffset 150
                        parallel:
                            easeout .3 alpha 1.0
                        parallel:
                            easeout .3 xoffset 0
                
                    "Я поднял руку и укрепил щит, чтобы заблокировать атаку, но меня откинуло от силы двойного удара. Вкопав пятки в землю, я едва успел зарегистрировать следующую атаку!"
                    
                    show mc mech at bl:
                        xoffset 0
                    show aiM neu at br:
                        xoffset 0
                    with dissolve
                    $E1D4S4_LOOPINGMENU2=1
                    jump E1D4S4Combat1Loopback

                "Уворачиваться!" if E1D4S4_LOOPINGMENU3 == 0:
                    $ renpy.hide_screen ("timer_scr")
                    
                    
                    show aiM att at br:
                        xoffset 0
                        parallel:
                            easeout .1 alpha 1.0
                        parallel:
                            easeout .1 xoffset -250
                    $renpy.pause(.1)

                    play sound meleeSound
                    show aiM att at br with Dissolve(.2):
                        xoffset -400
                        
                    play sound2 dodSound
                    show mc dod at bl with Dissolve(.45):
                        parallel:
                            easeout .5 alpha 1.0
                        parallel:
                            easeout .5 xoffset -150
                            
                            
                    "Я отошёл в сторону, и меч рассёк воздух. Воспользовавшись моментом, я ударил ИИ, но моя атака едва разегистрировалась."
                    "Второй ИИ выстрелил в меня, застигнув врасплох, и мой щит вспыхнул."
                    "Это плохо!"
                    "Два ИИ быстро восстановились и снова атаковали!"
                    
                    show mc mech at bl:
                        xoffset 0
                    show aiM neu at br:
                        xoffset 0
                    with dissolve
                    $E1D4S4_LOOPINGMENU3=1
                    jump E1D4S4Combat1Loopback

                "Слишком медленно…":
                    label E1D4S4_L1:
                    $ renpy.hide_screen ("timer_scr")
                    
                    show aiM att at br:
                        xoffset 0
                        parallel:
                            easeout .1 alpha 1.0
                        parallel:
                            easeout .1 xoffset -250
                    $renpy.pause(.1)

                    play sound meleeSound
                    show aiM att at br with Dissolve(.2):
                        xoffset -400

                    show white with Dissolve(0.15):
                    play sound2 hitSound
                    hide white with Dissolve(0.25)
                    
                    show mc blo at bl, Shake(None, .5, dist=20):
                        xoffset 150
                        parallel:
                            easeout .3 alpha 1.0
                        parallel:
                            easeout .3 xoffset 0
                            
                            
                    "Я слишком медленно среагировал, и прорыл пятками землю от силы их атак. Щит мерцал, поглощая удары."

            
            
            label E1D4S4_MatchPlanComplete:
                $renpy.pause(1.0)
                $ renpy.hide_screen ("battle_screen")
                $ E1D4S4matchPlan = survived
                show aiM neu at br with dissolve:
                    xoffset 0
                show mc ready at bl with dissolve:
                    xzoom -1
            "Это как наш тренировочный матч. {w}Я только мог продержаться короткое время, так как большинство энергии ядра уходило на то, чтобы уворачиваться одновременно от двух GEAR."
    
    
        "Лееееееееееееееееероооооооооооооооооой....":
            scene black with fade
            # show team, dissolve MC to disappear
            show bg battleground day with dissolve
            show mayu mech at tl:
                xzoom -.8
                yzoom .8
            show shou mech at tr:
                xzoom -.8
                yzoom .8
            show kaori mech at mm:
                xzoom -1
            show mc mech at bl:
                xzoom -1
            show mc ready at bl with dissolve
            pf "Это Орёл. И я покажу, на что он способен!"
            play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
            show mc ready at bl, Shake(None, 1, dist=20) behind kaori:
                xzoom -1
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1750
            $renpy.pause(.75)
            voice "audio/voice/E1/D4/S4/Kaori/10.ogg"
            ki "Что?!"
            hide mc
            voice "audio/voice/E1/D4/S4/Mayu/5.ogg"
            ma "Подожди--!"
            voice "audio/voice/E1/D4/S4/Shou/4.ogg"
            ss "О-оу."
            scene black with fade
            # show centered bg with mc shielding 
            show bg battleground day with dissolve:
                xzoom 1
                yzoom 1
                xoffset 0
                yoffset 0
            show mc ready at cc behind shou with dissolve:
                xzoom -.85
                yzoom .85
            "На полной мощности двигателя, я влетел в бой, готовый разбирать на запчасти эти игрушки."
            play sound "audio/sfx/GEAR Combat/Rifle.ogg"
            show mc blo at cc behind shou with Dissolve(.25):
                xzoom -.85
                yzoom .85
                
            play sound2 [ "audio/sfx/GEAR Combat/Block.ogg", "audio/sfx/GEAR Combat/Block.ogg", "audio/sfx/GEAR Combat/Block.ogg" ]
            show mc blo at cc, Shake(None, 1.5, dist=8) behind shou:
                xoffset 75
                xzoom -.85
                yzoom .85
            $renpy.pause(.20)
            play sound3 [ "audio/sfx/GEAR Combat/Block.ogg", "audio/sfx/GEAR Combat/Block.ogg" ]
            
            "Шквал лазерного огня обрушился на меня. Орёл рекомендовал манёвры уклонения, но я игнорировал их и двигался вперёд."
            voice "audio/voice/E1/D4/S4/EagleAI/10.ogg"
            GEARpf "Энергетический щит впитал критический урон."
            # easin of shou and mayu at same time, stay by your side
            play sound "audio/sfx/GEAR Combat/SMG.ogg"
            "Внезапно шквал лучей пролетел мимо меня."
            show mayu att at tl behind mc with dissolve:
                xzoom -.7
                yzoom .7
            show shou att at bl with dissolve:
                xzoom -1
                yzoom 1
                
            "Маю и Сё летели на максимальной скорости, догоняя меня и обеспечивая подавляющий огонь. Каори плелась позади, сохраняя энергию."
            # show 2 enemy ai
            show aiR att at tr behind mc with dissolve:
                xzoom .7
                yzoom .7
            show aiM att at br with dissolve
            # slide mc offscreen further ahead
            play sound "audio/sfx/GEAR Combat/Thruster Move.ogg"
            show mc ready at cc, Shake(None, 1, dist=20) behind aiM:
                xzoom -.85
                yzoom .85
                xoffset 150
                parallel:
                    easeout .5 alpha 1.0
                parallel:
                    easeout .5 xoffset 1250
            $renpy.pause(1.0)
            "ИИ переключили внимание с меня на напарников."
            hide mc with dissolve
            # show melee ai getting rekt
            play sound2 "audio/sfx/GEAR Combat/SMG.ogg"
            $renpy.pause(.25)
            
            play sound "audio/sfx/GEAR Combat/Sniper.ogg"
            
            $renpy.pause(.35)
            play sound3 "audio/sfx/GEAR Combat/Hit.ogg"
            show aiM att at br, Shake(None, 1, dist=15) with dissolve
            play sound3 "audio/sfx/GEAR Combat/Depower.ogg"
            show aiM neu at br, Shake(None, 1, dist=15) with dissolve
            "Огонь поддержки напарников уничтожил ИИ GEAR ближнего боя. К сожалению, чрезмерное использование энергии на одни толкьо двигатели критически ослабило их щиты."
            hide aiM with dissolve
            # show mayu and shou getting rekt
            play sound3 "audio/sfx/GEAR Combat/Rifle.ogg"
            show mayu att at tl, Shake(None, 1, dist=15) behind shou:
                xzoom -.8
                yzoom .8
            show shou att at bl, Shake(None, 1, dist=15):
                xzoom -1
            with dissolve
            
            play sound "audio/sfx/GEAR Combat/Hit.ogg"
            $renpy.pause(.1)
            play sound2 "audio/sfx/GEAR Combat/Hit.ogg"
            show mayu mech at tl, Shake(None, 1, dist=15) behind shou:
                xzoom -.8
                yzoom .8
            show shou mech at bl, Shake(None, 1, dist=15):
                xzoom -1
            with dissolve
            
            "Долго под огнём они не продержались."
            play sound "audio/sfx/GEAR Combat/Depower.ogg"
            voice "audio/voice/E1/D4/S4/Mayu/6.ogg"
            ma "Простите, я всё."
            hide mayu with dissolve
            play sound "audio/sfx/GEAR Combat/Depower.ogg"
            voice "audio/voice/E1/D4/S4/Shou/5.ogg"
            ss "То же самое..."
            hide shou with dissolve
            # mc with his oppenents
            scene black with fade
            scene bg battleground day with dissolve
            show aiR neu at tr with dissolve:
                xzoom .8
                yzoom .8
            show aiM neu at br with dissolve
            "Я наконец-то достиг свои цели!"
            show mc ready at bl with dissolve:
                xzoom -1
            pf "Отлично, сделаем это--"
            "Внезапно, Орёл перестал отвечать."
    
    voice "audio/voice/E1/D4/S4/EagleAI/11.ogg"
    GEARpf "Щиты отключены. Энергия ядра 1\%."
    show mc mech at bl with dissolve:
        xzoom -1
    pf "{i}Это плохо.{/i}"
    show aiM att at br with dissolve
    "ИИ GEAR мечник замахнулся."
    "Орёл не отвечает..."
    stop music fadeout 3
    "Вот так должно всё закончиться?"
    show aiM att at br with dissolve:
        parallel:
            easeout 1.0 alpha 1.0
        parallel:
            easeout 1.0 xoffset -500
    scene black with Dissolve(.5)
    $renpy.pause(2.0, hard=True)
    voice "audio/voice/E1/D4/S4/EagleAI/12.ogg"
    GEARpf "Инициирован протокол аварийного питания ядра."
    play sound "audio/sfx/GEAR Combat/Overdrive Phase 1.ogg"
    scene white with Dissolve(.5)
    "В кабине одновременно загорелись все огни. На дисплее были разные статистики и цифры, которых я раньше никогда не видел."
    $ knockback = 0
    play sound2 "audio/sfx/GEAR Combat/Overdrive Phase 2.ogg"
    $ renpy.pause(1.0, hard=True)
    $ renpy.pause(1.4)
    "!!"
    
    play sound "audio/sfx/GEAR Combat/Overdrive Phase 3.ogg"
    $ persistent.gpix[7][0] = 1

    scene cg GEAR overdrive first with Shake((0, 0, 0, 0), 2.5, dist=20):
        xalign 0.5
        yalign 0.5
        xzoom 1.1
        yzoom 1.1
        
    "Громовой грохот привлёк моё внимание, а всплеск взрывной энергии отбросил атакующий ИИ GEAR на десять футов. Я взглянул и заметил небольшой кратер вокруг Орла."


    scene bg battleground day
    show aiR neu at tr:
        xzoom .8
        yzoom .8
    show aiM att at mm
    show mco blo at bl:
        xzoom -1
        xoffset 150
    with Dissolve(.05)
    
    #play sound "audio/sfx/GEAR Combat/Overdrive Phase 3.ogg"
    show aiR neu at tr, Shake(None, 1, dist=10):
        xzoom .8
        yzoom .8
        xoffset 200
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset 300
    show aiM att at mm, Shake(None, 1, dist=15):
        parallel:
            easein 1.5 alpha 1.0
        parallel:
            easein 1.5 xoffset 450
    with Shake((0, 0, 0, 0), 1.0, dist=10)
    #"A thunderous boom catches my attention and a surge of explosive energy shoves the attacking AI GEAR ten feet away. I look out and see a shallow crater around Eagle."
    $renpy.pause(0.5)
    voice "audio/voice/E1/D4/S4/EagleAI/13.ogg"
    GEARpf "Протокол завершён. Выходная мощность более 9000."
    play music "audio/music/Raycrash (GAME VERSION).ogg" fadein 1
    show mco mech at bl with Dissolve(1.5):
        xzoom -1
        xoffset 0
    show aiM neu with dissolve
    $ renpy.pause(.25)

    pf "Что."
    
    show aiM att at br with Dissolve(1):
        xoffset 0
    voice "audio/voice/E1/D4/S4/EagleAI/14.ogg"
    GEARpf "Внешнее оружие не обнаружено. Активирую энергетические кулаки."
    play sound "audio/sfx/GEAR Combat/Energy Fist Activation.ogg"
    show mco neuFist with Dissolve(2.5):
        xoffset -150
        xzoom -1
    "Руки Орла слабо засветились."
    
    voice "audio/voice/E1/D4/S4/EagleAI/15.ogg"
    GEARpf "Вступаю в бой с вражеским GEAR."
    hide aiR with dissolve
    $ context = "E1D4S4_FirstTarget"
    $ enemy = "aiM"
    $ mode = "overdrive"
    $ survived = 0
    
    $ mcEnergyMax = 9000
    $ mcEnergy = 9000
    $ enemyHPMax = 500
    $ enemyHP = 500
    
    $ qtebase = 10
    $ qtereaction = qteath + qtetrack + qtebase
    $ qtetotal = qtereaction
    $ t_var = qtereaction
    
    $ E1D4S4Score = 0
    #"Simulator starts, only good options, even if you time out, only good options."
    # This means only using attack/dodge visuals/sounds, no blocks. Use 'survived' to add to this sequence's score
    show screen battle_screen
    #show screen timer_scrReaction(place="E1D4S4_FirstTarget")
    jump qte_game
    label E1D4S4_FirstTarget:
        $ knockback = 0
        $renpy.pause(1)
        hide aiM with dissolve
        $ renpy.hide_screen ("battle_screen")
        show mco neuFist at bl with dissolve:
            xzoom -1
            xoffset 0
        $renpy.pause(1)
        show aiR neu at br with dissolve:
            xzoom 1
            yzoom 1
            
        voice "audio/voice/E1/D4/S4/EagleAI/16.ogg"
        GEARpf "GEAR уничтожен. Вступаю в бой со второй целью."

    $ qtebase = 10
    $ qtereaction = qteath + qtetrack + qtebase
    $ qtetotal = qtereaction
    $ t_var = qtereaction
    
    $ mcEnergyMax = 9000
    $ mcEnergy = 9000
    $ enemyHPMax = 500
    $ enemyHP = 500
    
    $ context = "E1D4S4_SecondTarget"
    $ enemy = "aiR"
    #$ survived = 0
    #"Simulator starts, only good options, even if you time out, only good options."
    # This means only using attack/dodge visuals/sounds, no blocks. Use 'survived' to add to this sequence's score
    show screen battle_screen
    #show screen timer_scrReaction(place="E1D4S4_SecondTarget")
    jump qte_game
    label E1D4S4_SecondTarget:
        $ knockback = 0
        $renpy.pause(1)
        hide aiR with dissolve
        show mco neuFist at bl with dissolve:
            xzoom -1
            xoffset 0
        $renpy.pause(1)
        $ renpy.hide_screen ("battle_screen")
        pf "Это круто!"
        voice "audio/voice/E1/D4/S4/EagleAI/17.ogg"
        GEARpf "Ядро больше не может поддерживать мощность. Орёл отключается."
        show mco mech with dissolve
        $renpy.pause(.5)
        
    $ E1D4S4Score += survived
    stop music fadeout 5
    # Let's make a total score for the episode's story
    $ E1Score = 0
    # and add all the possible scores they could've gotten so far
    #$ E1Score = E1D4S4Score + E1D4S4matchPlan + teamPractice + practiceScore
    
    if (E1D4S4_FollowMatchPlan == 1):
        pf "Фух... едва удалось справиться с этим."
    
    else:
        show bg battleground day:
            linear .5 xoffset 200
        show mco mech at bl:
            xzoom -1
            linear .5 xoffset 1000

        show aiM att at bl:
            xoffset -1000
            xzoom -1
            easeout .5 xoffset 0
        pf "Подожди! Ещё один остался!"
        
        show aiM att at bl behind mco:
            easeout .5 xoffset 400
        "Последняя цель нападает на мой GEAR."
        show kaori att at bl behind aiM:
            xoffset -1000
            xzoom -1
            easeout .25 xoffset -100
        play sound "audio/sfx/GEAR Combat/Sword Single.ogg"
        
        $renpy.pause(.25)
        show aiM att at bl, Shake(None, 1, dist=15) behind mco:
            easeout .5 xoffset 400
        play sound2 "audio/sfx/GEAR Combat/Hit.ogg"
        

        voice "audio/voice/E1/D4/S4/Kaori/5.ogg"
        ki "Хийяя!"
        
        play sound2 "audio/sfx/GEAR Combat/Depower.ogg"
        hide aiM with dissolve
        
        "Появилась Каори и разбила GEAR одним ударом."
        show kaori mech at bl with dissolve
    $renpy.pause(.25)
    
    play music "audio/music/Victory! (GAME VERSION).ogg"
    $renpy.pause(.5)
    voice "audio/voice/E1/D4/S4/ACE Academy Announcer/1.ogg"
    an "Квалификационный матч закончен. Пожалуйста покиньте арену вместе со воими GEAR."
    $renpy.pause(1)
    "Толпа на мгновение затихла, прежде чем разразилась оглушительными возгласами."
    $renpy.pause(1.0)
    #fade to black, fade in arena BG with pilot sprites
    scene black with Dissolve(2.5)
    $renpy.pause(1)
    stop music fadeout 3
    $renpy.pause(1)
    scene bg campus arena day at Zoom((1920, 1080), (0, 0, 2376, 1180), (0, 0, 2376, 1180), 0) with Dissolve(2.5)
    
    $ mcEnergyMax = 200
    $ mcEnergy = 200
    
    jump E1D4S5
