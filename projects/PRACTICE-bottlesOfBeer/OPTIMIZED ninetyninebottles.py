bottles = 99
# song verses
# first verse
first_verse ="bottles of beer on the wall"
also_first_verse = "bottles of beer!"
# the first verse of the song, but singular!
first_verse_singular = "bottle of beer on the wall"
also_first_verse_singular = "bottle of beer!"
# second verse
second_verse = "You take one down, pass it around"
# final verse, for when bottles hits 0
final_verse = """No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall"""
# a while loop. I accidentally used a for loop at first lol
while bottles!=0:
    # In my initial try, I forgot to break the code. As a result, this ran infinitely when bottles hit 0. To fix this, I added the break line, when the else statement is satisfied.
    if bottles>2:
        print(str(bottles),first_verse)
        print(str(bottles),also_first_verse)
        print(second_verse)
        bottles = bottles - 1
        print(str(bottles),first_verse)
        print("-")
    elif bottles>1:
        print(str(bottles),first_verse)
        print(str(bottles),also_first_verse)
        print(second_verse)
        bottles = bottles - 1
        print(str(bottles),first_verse_singular)
        print("-")
        # I used elif to avoid too many nested IFs
    elif bottles == 1:
        print(str(bottles),first_verse_singular)
        print(str(bottles),also_first_verse_singular)
        print(second_verse)
        bottles = bottles - 1
        print(str(bottles),first_verse)
        print("-")
    else:
        print(final_verse)
        break
# what are staged commits??