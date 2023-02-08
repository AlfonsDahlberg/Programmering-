i = 2
while i <= 10:
    print(i)
    i += 2

print("done")

secret_word = "banan"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter guess")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("dålig")
else:
    print("banan är korrekt")
