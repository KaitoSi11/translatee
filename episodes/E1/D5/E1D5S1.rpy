label E1D5S1:


play ambient "audio/ambience/Morning.ogg" fadein 3
play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
$renpy.pause(1.5)

scene bg homekaito myroom day with fade

"Нежное щебетание птиц постепенно пробудило меня от моего сна. Мои мышцы завопили, когда я попытался поднятся. Похоже, что из-за матчей какое-то время тело будет болеть. Тем не менее, боль - это напоминание о хорошей  битве, что расслабляло."

pf "9:00 AM."

"Зевая, я вылез из постели и приготовился ко дню."

stop ambient fadeout 2.0
scene black with fade
$renpy.pause(.5)
scene bg homekaito main day with fade

"Я спустился вниз, ожидая увидеть Никки."

pf "Привет--"

"Никого не было. Странно. Я вытащил телефон и увидел сообщение от неё."

"{i}Хэй!Я собираюсь позавтракать вместе со своими друзьями,а затем пройтись по магазинам. Я хотела сказать тебе лично, но ты спал когда я собиралась уходить, Соня. =3={/i}"
"{i}Кайто также сказал, что направляется на экстренное совещание. Я знаю, как ты бесполезен, когда дело доходит до готовки, поэтому открой холодильник и проверь второй ряд. Поговорим позже! ^w^{/i}"

pf "Бесполезен?! Грррр..."

"Открыв холодильник, меня встретил самый вкусновыглядящий сэндвич с яичным салатом, который я когда-либо видел."

pf "Чёрт, Никки. Всегда делает так, что невозможно на неё злиться."

"Я взял сендвич и сок, и сел за стол. Интересно, что бы сделать сегодня…"


label E1D5S1_WeekendChoiceSelection:

menu:
    # "Заниматься самостоятельно.":
    #    $ E1D5S1_EventAlone = 1
    #    jump E1D5S2
        
    "Работать над проектом по истории вместе с Юной.":
        $ E1D5S1_EventYuuna = 1
        jump E1D5S3
        
    "Спросить Каори о командной стратегии.":
        $ E1D5S1_EventKaori = 1
        jump E1D5S4
        
    "Прогулятся с Сё." if (E1D5S6_MayuNoThanksLoop == 0):
        $ E1D5S1_EventShou = 1
        jump E1D5S5
        
    "Посмотреть,как поживает Маю." if (E1D5S6_MayuNoThanksLoop == 0):
        $ E1D5S1_EventMayu = 1
        jump E1D5S6
        
        
        
