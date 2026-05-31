import os
def search_engine():
    search = input("Enter your search: ")
    path = r"C:\Users\user\Desktop"
    total = 0
    found = False
    First_time = True
    for root,dirs,files in os.walk(path):
        for file in files:
            if search in file:
                found = True
                if First_time==True:
                    print("founded")
                    First_time = False
                print(file)
                print(os.path.join(root,file))
                total += 1
        
    else:
        if found == False:
            print("not found")
        print("total matches",total)

while True:
    print("1.search")
    print("2.exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        search_engine()
    elif(choice==2):
        exit()
    else:
        print("Invalid choice")
        continue