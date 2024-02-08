#Convert name into title
def title_name(fname , lname):
    f_name = fname.title()
    l_name = lname.title()

    return f"{f_name} {l_name}"

first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")

full_name = title_name(first_name, last_name)
print(full_name)

