import json
with open("tsis4/json/sample-data.json", "r") as new_file:
    data = json.load(new_file)
    print("Interface Status")
    print("================================================================================")
    print("DN                                                       Description           Speed        MTU  ")
    print("--------------------------------------------------   --------------------      ------      -------")
    for i in range(18):
        for x1, x2 in data["imdata"][i]['l1PhysIf']["attributes"].items():
            if x1 == 'dn':
                print(x2, end="                                      ")
            if x1 == "speed":
                print(x2, end="")
            if x1 == "mtu":
                print(x2, end="       ")
        print("\n")