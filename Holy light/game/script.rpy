# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Джайна")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    j "Даларан являлся одним из королевств, возникших после ослабления Империи Аратора. Много лет назад большинство магов жили в Строме."
    j "Когда опасность начала собираться вокруг этих земель, они покинули свои жилища и отправились на север в Альтеракские горы и обнаружили город Даларан, в котором жили Высшие Эльфы."
    j "Город стал пристанищем для всех людей, которые смогли обменяться знаниями с Высшими Эльфами. Маги Даларана стали защищать всех жителей города, которые не имели магических способностей."
    j "Над Далараном было возведено гигантское защитное поле."
    j "Это чрезмерное использование магии стало впоследствии маяком, для интересов возвращения Пылающего Легиона в Азерот."
    j "Демоны терроризировали местное население и маги обратились за помощью к Высшим Эльфам."
    j "И высшие эльфы заключили союз с людьми: был основан Орден Тирисфаля, тайное собрание избранных магов, призванное найти и..."
    j "наделить силой одного защитника, который должен был вести бесконечную скрытую от взора непосвященных войну с демонами."
    j "Этот защитник стал именоваться Стражем."
    
    # This ends the game.

    return
