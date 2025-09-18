import data
import logic
import getpass
import cli

logined = False
id = 0
data.load_users()

while not logined:
    if data.UserData == {}:
        print("No users found. Please register.")
        name = input("Name > ")
        password = getpass.getpass("Pass > ")
        role = "admin"
        id = len(data.UserData) + 1
        logic.reg.register(name, password, id, role)
        print("Registration successful. Please log in.")
    user = input("User > ")
    if logic.login.login(user, getpass.getpass("Pass > ")):
        id = data.find_user_name(user).get("id")
        logined = True
        print("Login successful!")
    else:
        print("Login failed.")

choose=""
while choose not in ["c", "u"]:
    choose=input("Choose cli or gui (c/u): ")

if choose=="c": 
    if data.find_user(id).get("role") == "teacher":
        cli.teacher(id)

    elif data.find_user(id).get("role") == "class monitor":
        cli.class_monitor(id)

    elif data.find_user(id).get("role") == "teamleider":
        cli.teamleider(id)

    elif data.find_user(id).get("role") == "student":
        cli.student(id)

# if choose=="u":
#     input_type = "give"
#     student_name = "thanh"
#     how = 1
#     student_id = data.find_user_name(student_name).get("id")
#     print(student_id)
#     if input_type == "error":
#         error_id = int(input("Error ID: "))
#         import logic.team.add
#         for i in range(how):
#             if logic.team.add.add_error(id, student_id, error_id):
#                 print("Error added successfully.")
#             else:
#                 print("Failed to add error.")
#     elif input_type == "give":
#         give_id = 1
#         import logic.team.add
#         for i in range(how):
#             if logic.team.add.add_give(id, student_id, give_id):
#                 print("Give added successfully.")
#             else:
#                 print("Failed to add give.")