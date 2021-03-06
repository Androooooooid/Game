﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
    image bg dalaran = "images/dalaran.jpg"
    image bg mapdalaran = "images/mapdalaran.jpg"

define j = Character("Джайна")

label start:

   scene bg dalaran with dissolve 

   "История."
   j "Даларан являлся одним из королевств, возникших после ослабления Империи Аратора. Много лет назад большинство магов жили в Строме."
   j "Когда опасность начала собираться вокруг этих земель, они покинули свои жилища и отправились на север в Альтеракские горы и обнаружили город Даларан, в котором жили Высшие Эльфы."
   j "Город стал пристанищем для всех людей, которые смогли обменяться знаниями с Высшими Эльфами. Маги Даларана стали защищать всех жителей города, которые не имели магических способностей."
   j "Над Далараном было возведено гигантское защитное поле."
   j "Это чрезмерное использование магии стало впоследствии маяком, для интересов возвращения Пылающего Легиона в Азерот."   
   j "Демоны терроризировали местное население и маги обратились за помощью к Высшим Эльфам."
   j "И высшие эльфы заключили союз с людьми: был основан Орден Тирисфаля, тайное собрание избранных магов, призванное найти и..."
   j "Наделить силой одного защитника, который должен был вести бесконечную скрытую от взора непосвященных войну с демонами."
   j "Этот защитник стал именоваться Стражем."
   
   menu class_menu:
       "Паладин":
           "Вы выбрали Паладина"
       "Воин":
           "Вы выбрали Воина"
       "Рыцарь":
           "Вы выбрали Рыцаря"
       "Маг":
           "Вы выбрали Мага"
   "Куда отправимся?"
   scene bg mapdalaran with fade
   
   label click:
   $ result = renpy.imagemap("mapdalaran.jpg", "mapdalaranwithlabel.jpg", [
       (745, 141, 994, 242, "Antonidas_pamitnic"),

       (1018, 232, 1229, 337, "sulightless"),

       (660, 314, 952, 421, "withe_palata"),

       (343, 461, 561, 527, "ametist_citadel"),

       (1316, 405, 1492, 485, "ploshad_krasa"),

       (834, 492, 1039, 591, "ploshad_rune"),

       (565, 682, 777, 757, "argentum_anklav"),
       
       (864, 667, 1026, 739, "vechnay_zari"),

       (1175, 686, 1434, 788, "ametist_fortress")
       
       ])
   
   return
