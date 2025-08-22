grade = "B"
best_font = "Comic Sans"

while True:
    answer = input("Vilken är den bästa fonten?: ")
    if answer.lower() == best_font.lower():
        print("WOW! Vad rätt du har! Du får A!")
        grade = "A"
    else:
        print("WOW! Vad fel du har! Du får F!")
        grade = "F"
    print(f"Du fick {grade} som slut betyg.")