import random
import time
import sys

print("============= CANDLELIGHT =============")
print()

time.sleep(1)

def narrate(text, pause=1.8):
    print(text)
    time.sleep(pause)

narrate("...The fight was long... longer than anyone expected.")
narrate("The rain cuts your face, like razors against open wounds.")
narrate("You're on one knee, your weight braced on your sword as it pins a goblin's body to the ground.")
narrate("You need to find shelter. The thick darkness amplifies the horrific sounds echoing inside your head.")
narrate("The other goblins fled, all moving toward the same place. Shelter, perhaps…")
narrate("...or something worse.")

print()
narrate("You follow their footsteps, the massive sword dragging a rough trail in its wake.")
narrate("A dim light flickers ahead, but with every step, it drifts farther from your grasp.")
narrate("Faint echoes reach your ears, but you can't make out a single word.")
narrate("A cave! Dark as it is, at least it will keep the rain off your wounds.")
print()

while True:
    choice1 = input("Enter cave? y/n ").lower()
    print()

    if choice1 == "n":
        narrate("You suddenly feel a sharp pain. It's like your brain is being stabbed repeatedly by daggers.")
        narrate("You drop your sword and you grab hold of the back of your head. It's an arrow...")
        narrate("The veil of darkness overpowers your vision...")
        narrate("It's all over.")
        sys.exit()
    elif choice1 == "y":
        narrate("You step into the cave, seeking refuge from the storm.")
        break
    else:
        narrate("You're hesitating... Please enter 'y' or 'n'.")

narrate("It all got quiet. Only drops of water hit the ground, and the faint light glimmered in the cave.")
narrate("You take a few slow, quiet steps, with your sword resting on your shoulder...")
narrate("You suddenly trip. It's very hard to see, so you kneel, trying to feel what's on the ground.")
narrate("It feels like...a body...")

while True:
    choice2 = input("Search? y/n ").lower()
    print()

    if choice2 == "n":
        narrate("You back up, not wanting to mess with something unknown.")
        break
    elif choice2 == "y":
        narrate("It feels like it's been there a while. The putrid smell... the weight of hollow bones... oh? A satchel.")
        satchel = input("Open the satchel? y/n ").lower()
        if satchel == "y":
            narrate("You found a potion")
            narrate("You pop open the cork and smell it... it's something familiar... herbs...")
            narrate("Your mouth feels dry, despite the damp air clinging to you.")
            narrate("You take a sip... oh, it feels good... you just chug it!")
            narrate("Congratulations! your HP is now full (40)!")
            break
        else:
            narrate("You back up, not wanting to mess with something unknown.")
            break
    else:
        narrate("You're awkwardly kneeling in front of a dead body... Please enter 'y' or 'n'.")

print()

narrate("'HELP!' You hear a sharp scream. 'HELP ME!'")
narrate("You instinctively start running towards the voice...'Where are you?'")
narrate("You hear nothing... just silence. It's hard to see now.")
narrate("'Huh, two tunnels. I wonder which way to go...'")

while True:
    choice3 = input("Go left or right? l/r ").lower()
    print()

    # ===== LEFT PATH – SPIDER =====
    if choice3 == "l":
        narrate("You take the left path, hoping it will lead you closer to the voice calling for help.")
        narrate("'Hello?' you shout into the darkness. 'Are you there?'")
        narrate("The silence doesn't answer, but it doesn't stay silent for long. A faint skittering echoes through the passage, growing louder with every breath.")
        narrate("'What the hell is that?...'")
        narrate("You take a few cautious steps forward when suddenly a burning sting erupts across your feet.")
        narrate("'Argh - what?!'")
        narrate("Something drops on your shoulders and flares the already hurting wounds.")
        narrate("Small, glowing sparks stare back at you from above")
        narrate("A piercing scream tears through the cavern, and a massive spider crashes down on top of you")

        while True:
            player_hp = 40
            spider_hp = 35

            print("\n========== Combat ==========")

            while player_hp > 0 and spider_hp > 0:
                print(f"\nYour HP: {player_hp}")
                print("Spider HP: ?")
                print("1. Attack")
                print("2. Roll")

                try:
                    fight1 = int(input("Choose your action (1/2): "))
                except ValueError:
                    continue

                spider_action = random.randint(1, 2)

                if fight1 == 1:
                    damage = random.randint(5, 9)
                    spider_hp -= damage
                    print(f"You slash the spider for {damage} damage!")
                elif fight1 == 2:
                    print("You roll to evade the attack!")

                if spider_hp <= 0:
                    print("\nThe spider collapses, defeated, letting out a final shriek!")
                    break

                if spider_action == 1:
                    spider_damage = random.randint(5, 10)
                    if fight1 == 2 and random.randint(1, 100) <= 60:
                        print("The spider strikes, but you dodge just in time!")
                    else:
                        player_hp -= spider_damage
                        print(f"The spider bites you for {spider_damage} damage!")
                else:
                    print("The spider skitters wildly and misses!")

            if player_hp <= 0:
                retry = input("Try again? y/n: ").lower()
                if retry == "y":
                    continue
                else:
                    sys.exit()
            break
        break

    # ===== RIGHT PATH – CANDLE / KOBOLD =====
    elif choice3 == "r":
        narrate("You take the right path, hoping it will lead you closer to the voice calling for help.")
        narrate("'Hello?' you shout into the darkness. 'Are you there?'")
        narrate("The light appears again - this time brighter, stronger. It isn't moving toward you, but an uneasy feeling that you're not alone started creeping in.")
        narrate("As you take a few slow, quiet steps, you hear a ragged voice. A harsh, almost angry sound.")
        narrate("You don't recognize any words, but you keep moving forward.")
        narrate("The light grows brighter still, flooding the darkness until the surroundings finally come into view.")
        narrate("A massive candle burns in the middle of the path.")
        narrate("Its flame is intense, blindingly bright, radiating heat. Yet it doesn't hurt.")
        narrate("You step closer, drawn by the heat, desperate for rest.")
        narrate("'YOU NO TAKE CANDLE! CANDLE MINE!'")
        narrate("A bulky, giant Kobold charges towards you, eyes glowing red, claws raised, out for blood.")

        while True:
            player_hp = 40
            kobold_hp = 35

            print("\n========== Combat ==========")

            while player_hp > 0 and kobold_hp > 0:
                print(f"\nYour HP: {player_hp}")
                print("Kobold HP: ?")
                print("1. Attack")
                print("2. Roll")

                try:
                    fight2 = int(input("Choose your action (1/2): "))
                except ValueError:
                    continue

                kobold_action = random.randint(1, 2)

                if fight2 == 1:
                    damage = random.randint(5, 10)
                    kobold_hp -= damage
                    print(f"You slash the Kobold for {damage} damage!")
                elif fight2 == 2:
                    print("You roll to evade the kobold's attack!")

                if kobold_hp <= 0:
                    print("\nThe kobold falls and quakes the ground, reaching for the candle, while taking its last breath.")
                    break

                if kobold_action == 1:
                    kobold_damage = random.randint(5, 10)
                    if fight2 == 2 and random.randint(1, 100) <= 60:
                        print("The kobold strikes, but you dodge just in time!")
                    else:
                        player_hp -= kobold_damage
                        print(f"The kobold claws you for {kobold_damage} damage!")
                else:
                    print("The kobold charges mindlessly and misses!")

            if player_hp <= 0:
                retry = input("Try again? y/n: ").lower()
                if retry == "y":
                    continue
                else:
                    sys.exit()
            break
        break

    else:
        narrate("You're resting your head against the wall... Please enter 'l' or 'r'.")

# ===== FINAL CHAMBER & BOSS =====

print()
narrate("Exhausted, you pick up your sword and lean your back against the wall.")
narrate("If only you could steal a few minutes of shut-eye...")
print()
narrate("'HELP!' the voice is back again.")
narrate("You jolt upright and follow the sound, quickening your pace, blade ready for whatever waits ahead.")
narrate("With every step, more voices rise to meet you - an eerie, ritualistic chant echoing and multiplying against the cave walls.")
narrate("The passage opens into a vast chamber, barely lit by a sickly glow.")
narrate("Goblins crowd the center of the room, all facing something you can't yet see.")
narrate("'HELP! Please!'")
narrate("The chant stops. Every head turns toward you and stares.")
narrate("From behind the horde, a harsh command rings out 'GEVER VAZA!'")
narrate("The goblins scatter to the edges of the chamber.")
narrate("A massive hobgoblin steps into view, armored head to toe, gripping heavy chains that bind a woman to a raised altar.")
narrate("'You're here!' the woman cries.")
narrate("With the last of her strength, she casts a spell. Warm energy surges through you - you feel alive, invigorated, stronger than ever.")
narrate("'Please...free me!'")
narrate("The hobgoblin snarls and strikes her with the back of his shillelagh.")
narrate("He descends from the altar and roars, 'VAWS-HAK!'")
narrate("With a thunderous bellow, the hobgoblin charges, powering his attack.")

print("\n========== Combat ==========")

while True:
    player_hp = 50
    hobgoblin_hp = 50

    while player_hp > 0 and hobgoblin_hp > 0:
        print(f"\nYour HP: {player_hp}")
        print("Hobgoblin HP: ?")
        print("1. Attack")
        print("2. Roll")

        try:
            fight3 = int(input("Choose your action (1/2): "))
        except ValueError:
            continue

        hobgoblin_action = random.randint(1, 2)

        if fight3 == 1:
            damage = random.randint(5, 10)
            hobgoblin_hp -= damage
            print(f"You slash the hobgoblin for {damage} damage!")
        elif fight3 == 2:
            print("You roll to evade the hobgoblin's smash!")

        if hobgoblin_hp <= 0:
            print("\nThe hobgoblin falls and it all goes quiet")
            break

        if hobgoblin_action == 1:
            damage = random.randint(5, 10)
            if fight3 == 2 and random.randint(1, 100) <= 60:
                print("The hobgoblin swings, but you dodge just in time!")
            else:
                player_hp -= damage
                print(f"The hobgoblin smashes you for {damage} damage!")
        else:
            print("The hobgoblin strikes wide and misses!")

    if player_hp <= 0:
        retry = input("Try again? y/n: ").lower()
        if retry == "y":
            continue
        else:
            sys.exit()
    break

narrate("With the hobgoblin's fall, a few of the goblins kneel and the other scatter outside the cave.")
narrate("They recognize you as the leader and bow to your might.")
narrate("With one last slash of the sword, you free the fair lady from the chains imprisoning her.")
narrate("'Wake up, you're free' you whisper to her ear.")
narrate("'Now, let's get out of here and go home!'")

print("\nTHE END")
input("\nPress Enter to exit...")
