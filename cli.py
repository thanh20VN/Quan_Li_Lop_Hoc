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
                import logic
                user = input("Name: ")
                password = getpass.getpass("Password: ")
                id = len(data.UserData)
                role = input("Role (admin, teacher, class monitor, teamleider, student): ")
                if role == "teamleider":
                    team = input("Name team: ")
                    import logic.team
                    logic.team.team(team,id)
                logic.reg.register(user, password, id+1, role)
                # ...
            elif cmd == "add":
                import logic
                team_name = str(input("Team Name: "))
                user_name = str(input("User name: "))
                user_id = data.find_user_name(user_name).get("id")
                team_id = data.team.find_team(team_name)
                # print(team_id, user_id)
                logic.team.add_member(team_id,user_id)
                # ...
            elif cmd == "remove":
                team_name = str(input("Team Name: "))
                user_name = str(input("User name: "))
                user_id = data.find_user_name(user_name).get("id")
                team_id = data.team.find_team(team_name)
                logic.team.remove_member(team_id, user_id)
                # ...
        except (AttributeError, KeyError, TypeError, IndexError, IOError, OSError, ZeroDivisionError, ImportError, NameError, RuntimeError) as e:
            import traceback
            traceback.print_exc()
        except (ValueError) as e:
            print(e)
        except Exception as e:
            print(f"{type(e).__name__}: {e}")

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
                    logic.team.add.remove_error(id, student_id, error_id)
                    # ...
                elif input_type == "give":
                    give_id = int(input("Give ID: "))
                    import logic.team.add
                    logic.team.add.remove_give(id, student_id, give_id)
                    # ...
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
                    if data.summary.read_main("semester")["num"] == 0:
                        if tt["num"] >= 18:
                            print("Max week")
                            continue
                    elif data.summary.read_main("semester")["num"] == 1:
                        if tt["num"] >= 17:
                            print("Max week")
                            continue
                    elif data.summary.read_main("semester")["num"] == 2:
                            print("Max semester")
                            continue
                    t=logic.summary.week.generate_weekly_summary().values()
                    for i in t:
                        for j in i.values():
                            print("Name:", j["name"])
                            print("Ratings:", j["ratings"])
                            print("Total:", str(j["total"]))
                elif choice == "2":
                    tt=data.summary.read_main("week")
                    # print(tt["num"],type(tt["num"]))
                    if data.summary.read_main("semester")["num"] == 0:
                        if not tt["num"] <= 18:
                            print("Not enough week semester 1")
                            continue
                    elif data.summary.read_main("semester")["num"] == 1:
                        if not tt["num"] <= 17:
                            print("Not enough week semester 2")
                            continue
                    elif data.summary.read_main("semester")["num"] == 2:
                            print("Max semester")
                            continue
                    t=logic.summary.semester.generate_weekly_summary()
                    for i in t:
                        print("Team ID:", i[0])
                        for j in i[1]:
                            print("Name:", j[0])
                            print("Total:", str(j[1]))
                            print("Ratings:", j[2])
                elif choice == "3":
                    print(logic.summary.year.generate_yearly_summary())
                else:
                    print("Invalid choice.")
        except (AttributeError, KeyError, TypeError, IndexError, IOError, OSError, ZeroDivisionError, ImportError, NameError, RuntimeError) as e:
            import traceback
            traceback.print_exc()
        except (ValueError) as e:
            print(e)
        except Exception as e:
            print(f"{type(e).__name__}: {e}")

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
                        logic.team.add.add_error(id, student_id, error_id)
                        # ...
                elif input_type == "give":
                    give_id = int(input("Give ID: "))
                    import logic.team.add
                    for i in range(how):
                        logic.team.add.add_give(id, student_id, give_id)
                        # ...
        except (AttributeError, KeyError, TypeError, IndexError, IOError, OSError, ZeroDivisionError, ImportError, NameError, RuntimeError) as e:
            print(f"{type(e).__name__}: {e}")
        except (ValueError) as e:
            print(e)
        except Exception as e:
            print(f"{type(e).__name__}: {e}")

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
        except (AttributeError, KeyError, TypeError, IndexError, IOError, OSError, ZeroDivisionError, ImportError, NameError, RuntimeError) as e:
            print(f"{type(e).__name__}: {e}")
        except (ValueError) as e:
            print(e)
        except Exception as e:
            print(f"{type(e).__name__}: {e}")