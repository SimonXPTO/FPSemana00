room_descriptions = [
    ["A","B","C","D","E"],
    ["F","G","H","I","J"],
    ["K","L","M","N","O"],
    ["P","Q","R","S","T"],
    ["U","V","W","X","Y"]
]
position=(2,2)

while (True):
    x,y=position
    description= room_descriptions[y][x]
    print(position,":",description)

    print("What now?")
    command = input()

    if command == "north":
        print("You move north...")
        y=y-1
    elif command =="south":
        print("YOu move south")
        y=y+1
    elif command=="east":
        print("heading east...")
        x=x+1
    elif command=="west":
        print("heading west...")
        x-=1
    elif command=="goodbye":
        break
    else:
        print("i don't understand " + command)

    position = (x,y)