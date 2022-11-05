def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":  # check if a is in b list
            #  or if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation


print(translator(input("Enter a phrase: ")))
