# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define door = Character("Door")
define h = Character("[hero_name]")
define l = Character("Laertes")
define c = Character("Calypso")
define n = Character("Narrator")

init:
    image bwend = im.Scale("bwend.png", 1280, 720)
    image clend = im.Scale("clend.png", 1280, 720)
    image colorful = im.Scale("colorful.png", 1280, 720)
    image home2 = im.Scale("home2.png", 1280, 720)
    image homeboyonly = im.Scale("homeboyonly.png", 1280, 720)
    image road = im.Scale("road.png", 1280, 720)
    image recovered = im.Scale("recovered.png", 1280, 720)
    image menubig = im.Scale("menubig.png", 1280, 720)


# The game starts here.

label start:

    n "..."
    n "What was it again?"
    $ hero_name = renpy.input("What did they used to call you?")
    $ hero_name = hero_name.strip()
    if not hero_name:
        $ hero_name="Icarus"
    n "Ahh, yes..."
    n "You were the legendary [hero_name]..."
    n "Now you are just the blind one on the hill."

    scene menubig

    $ renpy.pause (2.0)
    door "Knock Knock Knock"
    n "There is someone at your door."

    #menu1
    menu:
        "Wait":
            jump menu1wait
        "Open the Door":
            jump openeddoor
        "Tell them to leave":
            h "Leave."
            jump theyleave

    # This ends the game.

    return

label menu1wait:
    n "You wait"
    h "..."
    door "Knock Knock Knock"
    n "It sounds again."
    n "Someone outside wants to come in."
    n "It's a female voice."
    n "They say they have an injured child."
    n "If you wait, they might leave."
    menu:
        "Wait":
            jump theyleave
        "Open the Door":
            jump openeddoor

label theyleave:
    n "There are no more sounds outside."
    n "You have turned away a mother and her child."
    n "Your life is no better or no worse."
    n "All you know is you missed your chance of company that will never happen again."
    n "It is dark. All fades to nothingness."

    scene bwend

    $ renpy.pause (5.0)

    return

label openeddoor:
    door "Click"
    n "You opened the door."
    n "Her voice sounds desperate. She says her son is injured and needs a place to stay."
    menu:
        "Nod":
            jump stage2
        "Tell them to leave":
            jump theyleave
    return

label stage2:
    n "They come in."
    n "The mother tells you her name is Calypso and her child's name is Laertes."
    h "[hero_name]"

    c "[hero_name]?"
    c "Where have I heard that before?"
    c "It doesn't matter."
    c "Please me help run to the town and buy potions."

    menu:
        "Wait":
            jump stage2wait
        "Go buy potions in town":
            jump buypotions
        "Tell her to go herself":
            jump cbuypotions

    return

label stage2wait:
    n "You do nothing."
    c "Please."
    n "She looks at you pleadingly."

    menu:
        "Wait":
            jump cbuypotions
        "Go buy potions in town":
            jump buypotions

label cbuypotions:
    c "Alright. I will go."
    c "Please take care of my son."

    n "The mother leaves."
    n "It is only you and the child now."
    $ renpy.pause (5.0)
    n "Time passes."
    n "More time passes."
    n "It's been a long time."

    menu:
        "Go find the mother":
            jump findmother
        "Wait":
            jump deathchild

label deathchild:
    n "The mother doesn't come back."
    n "You don't know why."
    n "There is a child slowly dying on your bed."
    n "You cannot see, so you cannot help."

    n "This is yet another life because of you."

    scene bwend

    return

label findmother:
    scene road
    n "You trot outside and try to navigate your way to town."
    n "You feel a cool breeze and warm sunlight"
    scene town1

    n "The town is lively. Murmurs everywhere."
    n "You hear some about you."

    "Hey, isn't that..."
    "Who?"
    "Wow, it is. That's rare."
    "Name?"
    "You know, the one that never leaves the house."
    "..."
    "The used to be famous one?"
    "Even I know."
    "Yeah, do you really not know?"
    "..."
    "The blind one?"
    "Oh! [hero_name]!"
    "SHHHH!!!"

    n "They seemed to have quiet down after you passed by."
    n "There is a lot of noise in front of you."
    scene town2

    "Dead body."
    "She's so young."
    "Wonder who did this?"
    "Gasp, is that?"
    "Gasp, oh my."
    n "The crowd makes way."

    h "Who is this?"
    "Honor meet you! I am a royal guard."
    "This seems to be the body of the adventurer... "
    "Callus?"
    "Calculus?"
    h "Calypso."
    "Oh..."
    h "Potions"
    "What?"
    h "Potions"
    n "The guard realized what you meant. He hands a bunch of potions to you."

    scene homeboyonly
    n "You return home."
    n "You walk other to the bed."
    n "The blanket rustles."
    n "They boy is still alive."
    n "You pat around the bed and find the boy's head and mouth. "
    n "You open a potion."

    h "Laertes"
    h "Potion."

    l "..."

    n "Cautiously, you feed the boy the potion."
    $ renpy.pause (5.0)

    scene homeboyonly
    n "A year has passed."
    n "They boy is healthy."
    n "The company is quite nice."
    n "But the boy's mother is not alive."
    n "Deep down, you know it was your fault that she died."
    n "So it is your responsibility to take care of her son like your own."
    n "Eventually you would need to tell the boy what happened."
    n "Although you days are brighter, darkness still lingers, and you cannot get rid of the feeling that you were the one that killed the boy's mother."

    scene bwend
    return


    return
label buypotions:
    scene road
    n "You trot outside and try to navigate your way to town."
    n "You feel a cool breeze and warm sunlight"
    scene town1

    n "The town is lively. Murmurs everywhere."
    n "You hear some about you."

    "Hey, isn't that..."
    "Who?"
    "Wow, it is. That's rare."
    "Name?"
    "You know, the one that never leaves the house."
    "..."
    "The used to be famous one?"
    "Even I know."
    "Yeah, do you really not know?"
    "..."
    "The blind one?"
    "Oh! [hero_name]!"
    "SHHHH!!!"

    "Potions for sale here!"
    n "You approach the stand"
    h "Buy"
    n "You hand over gold pieces and you recieve potions."

    scene home2
    n "You return home."
    c "You're back. And you got the potions. Thank you!"

    n "The mother treats the son"
    n "One months pass."
    n "The child is fully recovered."
    n "It is night before they will depart and the boy is awake."

    l "[hero_name]...Can you tell me a story?"
    c "Laertes, don't bother [hero_name]. Sorry..."
    menu:
        "Tell story":
            jump story
        "Don't tell story":
            jump recoveryleave

label recoveryleave:
    scene recovered
    c "Thank you for letting us stay for so long. We are leaving now."
    c "Say goodbye to [hero_name]"
    l "Good bye [hero_name]"

    n "The mother and the boy leave."
    n "The cabin is back to what it was before."
    n "A feeling of yearning lingers within you."
    n "Perhaps you should have said more."

    scene bwend
    return


label story:
    h "It's fine. I have a story to tell."
    scene home2
    h "Long ago, there were two really famous adventureres that took on beasts, faes, and evil spirits."
    h "They were best of friends and also rivals."
    h "One of them, feeling rather competitive, proposed a challenge."
    h "The challenge was to see who can defeat the most monsters with their eyes closed."
    h "The friend refused and insisted that it was too dangerous."
    h "But the other friend didn't give up."
    h "Eventually agreeing, the two of them set off on an epic journey with blindfolds around their eyes"
    h "Millions were watching them. But they could see nothing."
    h "The competition carried on for 3 days and nights and their battle count was exactly the same."
    h "Somehow, the two wandered into the pits of Tartarus, and one sensed danger."
    h "The other however, was only focused on getting that extra battle in."
    h "'It's dangerous here. Let's leave. Forget about battles.' "
    h "The other friend was reluctant to go. It was only one more battle and it would be a win."
    h "'Look you win, I took off my blindfold. Let's leave already'"
    h "'Lies.'"
    h "The friend wasn't lying, indeed it was off."
    h "Then Death itself appeared...and the blindfolded friend happily struck it."
    h "And then a dark aura embraced both of them."
    h "Confused by what happened, the blindfolded one removed the blindfold."
    h "It was the most horrific sight ever."
    h "There was blood everywhere. There was darkness everywhere."
    h "In front, there was a dead body and Death's reaper in the body."
    h "Death said to the one living, 'You struck Death, yet your friend was the one who died.'"
    h "'I do not take unneccesary lives. But I shall take your sight.'"
    h "'You've failed to see what was important right in front of you.'"
    h "'Someone like you truely does not deserve to see.'"
    h "Then the colors started to fade from the adventurer's world."
    h "All the light, all the colors, and all the feelings, drained away..."
    h "Until all that was left was one memory and capsule to hold it."
    h "From then on, the adventurer returned home and never did anything ever again."
    h "That's it. That's the whole story."
    l "What??? That's it? Wow. This is so depressing. You're horrible at telling stories."
    c "I have to agree with my son on this. This isn't the type of story you tell children"
    h "Ok fine, I will continue it."
    h "One day, there was a knock on the adventurer's door."
    h "There was a mother and an injured child."
    c "Gasp."
    h "The mother begged for a place to stay."
    h "The adventurer let them in."
    h "The mother asks for the adventurer to step outside and grab potions."
    h "The adventurer did as told."
    h "It was the first time since that day the adventurer left the house."
    h "The feeling of the outside was refreshing."
    h "The adventurer was starting to feel alive again."
    h "It was like the adventurer was given a second chance."
    h "The adventurer ran the errand and the mother treated the child."
    h "Slowly the child started to recover."
    h "And slowly, so was the adventurer."
    l "The adventurer is you! And I'm the child!"
    h "Yes, indeed you are."
    c "Sniff. That was beautiful."
    h "Thank you for knocking at my door. You are welcome to stay as long as you like. I rather enjoy having the company."
    l "Can we? I don't want to leave!"
    c "Yes, if [hero_name] allows it."
    h "Absolutely."

    scene colorful
    n "From then on the mother and the child started staying with the adventurer."
    n "The adventurer was given a second chance, and this time, realized what was important."
    n "Slowly, the light returned. The colors returned. And the feelings returned."
    n "Finally, the adventurer could see again."

    scene clend
    n "Congratulations, you got the best ending."


    return
