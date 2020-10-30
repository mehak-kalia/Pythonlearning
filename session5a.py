state1 = {
    "active": 881,
    "confirmed": 3497,
    "deaths": 78,
    "recovered": 2538,
    "state": "Punjab",
}

state2 = {
    "active": 51922,
    "confirmed": "116752",
    "deaths": 5651,
    "recovered": 59166,
    "state": "Maharashtra",
}

state3 = {
    "active": 21993,
    "confirmed": 50193,
    "deaths": 576,
    "recovered": 27624,
    "state": "Tamil Nadu",
}

state4 = {
    "active": 27741,
    "confirmed": 47102,
    "deaths": 1904,
    "recovered": 17457,
    "state": "Delhi",
}


state5 = {
    "active": 6149,
    "confirmed": 25148,
    "deaths": 1561,
    "recovered": 17438,
    "state": "Gujarat",
}

state6 = {
    "active": 5659,
    "confirmed": 15785,
    "deaths": 488,
    "recovered": 9638,
    "state": "Uttar Pradesh",
}

state7 = {
    "active": 2721,
    "confirmed": 13626,
    "deaths": 323,
    "recovered": 10582,
    "state": "Rajasthan",
}

state8 = {
    "active": 2308,
    "confirmed": 11426,
    "deaths": 486,
    "recovered": 8632,
    "state": "Madhya Pradesh",
}

state9 = {
    "active": 4528,
    "confirmed": 7944,
    "deaths": 134,
    "recovered": 4983,
    "state": "Haryana",
}

state10 = {
    "active": 2842,
    "confirmed": 3615,
    "deaths": 115,
    "recovered": 2570,
    "state": "Karnataka",
}
        #0        1      2       3       4      5       6        7       8        9
india =[state1, state2, state3, state4, state5, state6, state7, state8, state9, state10]
print("length of india is:", len(india))

#example of filtration
#for i in range(0, len(india)):
    #print("active: {}\nconfirmed{}".format(india[i] ["active"], india[i] ["confirmed"]))
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #print()

#filtering data as expected by user
#filter1=input("please enter urr first filter:")
#ilter2=input("please enter urr second filter:")
#for i in range(0, len(india)):
 #   print("{}: {}\n{}: {}".format(filter1, india[i][filter1], filter2, india[i][filter2]))
  #  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #print()

#searching from the data linear search
state = input("enter the state to search")
for i in range(0, len(india)):

    print("matching {} with {}".format(state, india[i]["state"]))
    #if state == india[i]["state"]:
    if state.lower() == india[i]["state"].lower():
        print("state {} found".format(state))
        print(india[i])
        break

#linear search goes on from 0 to n-1 elements

#sorting the data to sort active cases
for i in range(0, len(india)):
        active_cases = india[i]["active"]
        print("active cases are:",  active_cases)
        for j in range(0, len(india)-i-1):
            if india [i]["active"][j] > india [i]["active"][j+1]:
                india [i]["active"][j], india [i]["active"][j+1] = india [i]["active"][j+1], india [i]["active"][j]

print("active cases now are:", active_cases)

