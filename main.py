import time as t

password = input("Enter a password or phrase to test.")
password1 = []
score = 0
while True:
    if len(password) > 0:
        for i in range(len(password)):
            password1.append(password[i])
        input("Ready? Press anything when ready.")
        time1 = t.time()
        user_password = input("Enter phrase now!!: ")
        time2 = t.time()
        for x in range(len(password)):
            if user_password[x] == password1[x]:
                score += 1
        print("You completed the challenge in {} seconds with a {}% accuracy ({}/{})".format(time2-time1, score/len(password) * 100, score, len(password)))
    else:
        print("Password must contain data")
        t.sleep(1)
        break
