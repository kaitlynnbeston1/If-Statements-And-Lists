# lists of users
currentUsers=["admin", "Napstablook22", "undyne_the_undying", "asgore_dreemor", "w.d.gaster", "sans"]
newUsers = ["SANS", "W.D.Gaster", "tobyfox", "Papyrus", "SoMeOnE", "ANonIMouS"]

# Checking the usernames
for user in newUsers:
    user = user.lower()
    if user in currentUsers:
        print(f" Sorry, {user} is already taken. Please try again.")
    else:
        print(f"{user} is a valid username. Creating your account.")
        currentUsers.append(user)


# Showing the new list of users.
print("List of users:")
for user in currentUsers:
    print(user)
