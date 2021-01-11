guests = ["cheng long", "zheng zhi dan", "li lian jie"]
message = "Can you have dinner with me? " + guests[0] +" ," +guests[1]+ " ,"+ guests[2]+"."
print(message)

guests.remove("cheng long")
guests.insert(0, "jo jo")

print("cheng long can't come!")
message = "can you have dinner with me? " + guests[0] +" ," +guests[1]+ " ,"+ guests[2]+"."
print(message)

print("I found a big table!")
guests.insert(0,"xiao cheng you")
guests.insert(3,"zhang shi qi")
guests.append("zhuang qi bing")

