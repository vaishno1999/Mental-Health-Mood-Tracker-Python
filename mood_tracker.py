mood_quotes = {
    "happy": "Keep smiling! Happiness is contagious",
    "sad": "It's okay to feel sad. Better days are coming",
    "angry": "Take a deep breath. You are stronger than you think",
    "anxious": "You're doing the best you can. One step at a time",
    "tired": "Rest is productive too. Recharge and rise again",
    "neutral": "Every day won’t be exciting, and that’s okay"
}

mood_log = []
day = 1

print("Welcome to the Mental Health Mood Tracker")
print("Type 'done' when you're finished.\n")

while True:
    mood = input(
        f"Enter your mood for Day {day} "
        "(happy/sad/angry/anxious/tired/neutral): "
    ).lower().strip()

    if mood == "done":
        break

    if mood in mood_quotes:
        print("Quote:", mood_quotes[mood])
        mood_log.append(mood)
        day += 1
    else:
        print("Please enter a valid mood or type 'done'.")

print("\nWeekly Mood Summary:")

for i in range(len(mood_log)):
    print(f"Day {i + 1}: Mood - {mood_log[i].capitalize()}")

print("\nThanks for using the mood tracker.")
