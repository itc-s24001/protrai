#s24001
#関数でおみくじをする

import random
def main():
    kuji = ["大吉","中吉","小吉","凶"]
    return random.choice(kuji)

kekka = main()
print("結果は", kekka, "です")
