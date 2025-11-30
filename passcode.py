import random
import string

def gen_passwd(length=8):
    char = string.ascii_letters + string.digits + string.punctuation
    passwd= ''.join(random.choice(char) for _ in range(length))
    return passwd  

def main():
    while True:
        print("=====================password genrater========================")
        print("1. genrate a paasword key")
        print("2. exite")
        
        choise = input("\n enter the choise ")
        
        if choise == "1":
            try:
                length = int(input("Enter password length: "))
                if length < 4:
                    print("Length should be at least 4.")
                    continue
                print("\nGenerated Password:")
                print(gen_passwd(length))
            except ValueError:
                print("Please enter a valid number.")
        elif choise == "2":
            print("goodby")
            break
        else:
            print("invalid try")

if __name__=="__main__":
    main()    