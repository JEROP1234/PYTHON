# List of  school supplies
writing_supplies = ["pens", "pencils", "erasers"]
books = ["notebooks", "textbooks"]
accessories = ["ruler", "calculator"]
important_supplies = writing_supplies + books + accessories
user_supplies = [ "notebooks", "ruler"]
print("Your supplies:")
for item in user_supplies:
    if item in writing_supplies:
        print(f"{item} - Writing Supply")
    elif item in books:
        print(f"{item} - Book")
    elif item in accessories:
        print(f"{item} - Accessory")
if 'pens' not in user_supplies:
    print("you forgot a pen")
else:
    print("You added a pen")
