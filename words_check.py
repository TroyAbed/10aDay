


day_1=["put","sleep","leave","paint","write","listen", "look", "sit", "wake up", "get up"]
day_2=["time", "life", "love", "wold", "people", "home", "family","friend", "work", "school"]
day_3=["good", "bad", "beautiful", "ugly", "happy", "sad", "big", "small", "old", "young"]
day_4=["be", "have", "do", "say", "make", "go", "take", "get", "see", "come"]
day_5=["health", "food", "water", "heart", "mind", "nature", "art", "music", "city", "village"]
day_6=["rich","poor", "strong","weak","healthy", "sick","hot", "cold","fast","slow"]
day_7=["know", "want", "need", "like", "love", "hate", "can", "will", "shall", "should"]

day_list = [day_1, day_2, day_3, day_4, day_5, day_6]
total_list = []
for day in day_list:
    for word in day:
        if word not in total_list:
            total_list.append(word)
        else:
            print(f"!!!---WARNING: {word} is already in the list---!!!")

print("done")