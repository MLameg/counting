#Problem 2

#Part i: Reads sentence from standard input
x = input("Please enter a sentence: ").lower()

#Part ii: Counts number of words and characters, not including space
w = 1
c = 0
for word in x:
    c += 1
    if word == " ":
            w += 1
            c -= 1
print("You entered a", w, "word sentence that contains" ,c, "characters.")

#Part iii: Count number of vowels
v = 0
for letter in x:
        if ( (letter=="a") | (letter=="e") | (letter=="i") | (letter=="o") | (letter=="u") ):
                v += 1

print("There are" , v, "vowels in your sentence.")
