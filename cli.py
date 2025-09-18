import data
import logic
import getpass

def teacher(id):
    print(f"Welcome, {data.find_user(id).get('name')}, Role: {data.find_user(id).get('role')}")
    print("Type 'exit' to quit.")
    print("Type 'help' for help.")
    while True:
        try:
            cmd = input("> ")
            if cmd == "exit": break
            elif cmd == "help":
                print('''
                    exit: Exit the program
                    help: Show this help message
                    list: List all students
                    register: Register a new user
                    add: add a user to a team
                    remove: remove a user from a team
                ''')
            elif cmd == "list":
                import logic.student
                logic.student.list_students()
            elif cmd == "register":
                user = input("Name: ")
                password = getpass.getpass("Password: ")
                id = len(data.UserData)
                role = input("Role (admin, teacher, class monitor, teamleider, student): ")
                if role == "teamleider":
                    team = input("Name team: ")
                    import logic.team
                    logic.team.team(team,id)
                if logic.reg.register(user, password, id+1, role):
                    print("User registered successfully.")
                else:
                    print("Failed to register user.")
            elif cmd == "add":
                team_name = str(input("Team Name: "))
                user_name = str(input("User name: "))
                user_id = data.find_user_name(user_name).get("id")
                team_id = data.team.find_team(team_name)
                print(team_id, user_id)
                if logic.team.add_member(team_id, user_id):
                    print("User added to team successfully.")
                else:
                    print("Failed to add user to team.")
            elif cmd == "remove":
                team_name = str(input("Team Name: "))
                user_name = str(input("User name: "))
                user_id = data.find_user_name(user_name).get("id")
                team_id = data.team.find_team(team_name)
                if logic.team.remove_member(team_id, user_id):
                    print("User removed from team successfully.")
                else:
                    print("Failed to remove user from team.")
        except (AttributeError, KeyError, TypeError, ValueError, IndexError, IOError, OSError, ZeroDivisionError, ImportError, NameError, RuntimeError) as e:
            print(f"Lỗi: {e}")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")

def class_monitor(id):
    print(f"Welcome, {data.find_user(id).get('name')}, Role: {data.find_user(id).get('role')}")
    print("Type 'exit' to quit.")
    print("Type 'help' for help.")
    while True:
        try:
            cmd = input("> ")
            if cmd == "exit": break
            elif cmd == "help":
                print('''
                    exit: Exit the program
                    help: Show this help message
                    list: List all students
                    remove: remove a error or give from a student in my class
                    summary: Summary of anything
                ''')
            elif cmd == "list":
                import logic.student
                logic.student.list_students()
            elif cmd == "remove":
                input_type = str(input("Type (error/give): "))
                student_name = str(input("Student name: "))
                student_id = data.find_user_name(student_name).get("id")
                if input_type == "error":
                    error_id = int(input("Error ID: "))
                    import logic.team.add
                    if logic.team.add.remove_error(id, student_id, error_id):
                        print("Error removed successfully.")
                    else:
                        print("Failed to remove error.")
                elif input_type == "give":
                    give_id = int(input("Give ID: "))
                    import logic.team.add
                    if logic.team.add.remove_give(id, student_id, give_id):
                        print("Give removed successfully.")
                    else:
                        print("Failed to remove give.")
            elif cmd == "summary":
                import logic.summary
                print('''
                    Summary options:
                    1. Weekly summary
                    2. Semester summary
                    3. Yearly summary
                ''')
                choice = input("Choose an option (1/2/3): ")
                if choice == "1":
                    tt=data.summary.read_main("week")
                    if data.summary.read_main("semester")["num"] == 1:
                        if tt["num"] == 18:
                            print("Max week")
                            continue
                    elif data.summary.read_main("semester")["num"] == 2:
                        if tt["num"] == 17:
                            print("Max week")
                            continue
                    t=logic.summary.week.generate_weekly_summary().values()
                    print(t)
                    for i in t:
                        print(i)
                        for j in i.values():
                            print(j)
                            print("Name:", j["name"])
                            print("Ratings:", j["ratings"])
                            print("Total:", str(j["total"]))
                elif choice == "2":
                    tt=data.summary.read_main("week")
                    if data.summary.read_main("semester")["num"] == 1:
                        if tt["num"] != 18:
                            print("Not enough week")
                            continue

                    elif data.summary.read_main("semester")["num"] == 2:
                        if tt["num"] != 17:
                            print("Not enough week")
                            continue
                elif choice == "3":
                    print(logic.summary.year.generate_yearly_summary())
                else:
                    print("Invalid choice.")
        except (AttributeError, KeyError, TypeError, ValueError, IndexError, IOError, OSError, ZeroDivisionError, ImportError, NameError, RuntimeError) as e:
            print(f"Lỗi: {e}")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")

def teamleider(id):
    print(f"Welcome, {data.find_user(id).get('name')}, Role: {data.find_user(id).get('role')}")
    print("Type 'exit' to quit.")
    print("Type 'help' for help.")
    while True:
        try:
            cmd = input("> ")
            if cmd == "exit": break
            elif cmd == "help":
                print('''
                    exit: Exit the program
                    help: Show this help message
                    list: List all students in my team
                    add: add error or give to a student in my team
                ''')
            elif cmd == "list":
                for i in data.team.list_teams(id):
                    print(f" - Name: {i[0]}, ID: {i[1]}")
            elif cmd == "add":
                input_type = str(input("Type (error/give): "))
                student_name = str(input("Student name: "))
                how = int(input("How many: "))
                while how <= 0:
                    print("Please enter a positive number.")
                    how = int(input("How many: "))
                student_id = data.find_user_name(student_name).get("id")
                if input_type == "error":
                    error_id = int(input("Error ID: "))
                    import logic.team.add
                    for i in range(how):
                        if logic.team.add.add_error(id, student_id, error_id):
                            print(f"{i} Error added successfully.")
                        else:
                            print(f"{i} Failed to add error.")
                elif input_type == "give":
                    give_id = int(input("Give ID: "))
                    import logic.team.add
                    for i in range(how):
                        if logic.team.add.add_give(id, student_id, give_id):
                            print(f"{i} Give added successfully.")
                        else:
                            print(f"{i} Failed to add give.")
        except (AttributeError, KeyError, TypeError, ValueError, IndexError, IOError, OSError, ZeroDivisionError, ImportError, NameError, RuntimeError) as e:
            print(f"Lỗi: {e}")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")

def student(id):
    print(f"Welcome, {data.find_user(id).get('name')}, Role: {data.find_user(id).get('role')}")
    print("Type 'exit' to quit.")
    print("Type 'help' for help.")
    while True:
        try:
            cmd = input("> ")
            if cmd == "exit": break
            elif cmd == "help":
                print('''
                    exit: Exit the program
                    help: Show this help message
                    list: list my errors and give
                ''')
            elif cmd == "list":
                import logic.student.my_error_give
                print("My errors:")
                for i in logic.student.my_error_give.my_errors(id):
                    print(f" - Name: {i['name']}, ID: {i['id']}")
                print(logic.student.my_error_give.cal_errors(id))
                print("My give:")
                for i in logic.student.my_error_give.my_give(id):
                    print(f" - Name: {i['name']}, ID: {i['id']}")
                print(logic.student.my_error_give.cal_give(id))
                print("Total:", logic.student.my_error_give.cal_total(id))
        except (AttributeError, KeyError, TypeError, ValueError, IndexError, IOError, OSError, ZeroDivisionError, ImportError, NameError, RuntimeError) as e:
            print(f"Lỗi: {e}")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")