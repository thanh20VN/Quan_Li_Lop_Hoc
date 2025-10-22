import data_py
import logic
import getpass
import config

def teacher(id):
    print(f"Chào mừng, {data_py.find_user(id).get('name')}, Vai trò: {data_py.find_user(id).get('role')}")
    print("Nhập 'exit' để thoát phần miền.")
    print("Nhập 'help' để biết thêm thông tin.")
    while True:
        try:
            cmd = input("> ")
            if cmd == "exit": break
            elif cmd == "help":
                print('''
                    exit: Thoát phần miền
                    help: Hiển thị thông tin trợ giúp
                    list: Liệt kê tất cả học sinh
                    register: Đăng ký người dùng mới
                    add: Thêm người dùng vào nhóm
                    remove: Xóa người dùng khỏi nhóm
                    export: Xuất file excel của lớp học
                ''')
            elif cmd == "list":
                import logic.student
                for i in logic.student.list_students():
                    print(f" - Tên: {i[0]}, ID: {i[1]}")
            elif cmd == "register":
                import logic
                user = input("Tên: ")
                password = getpass.getpass("Mật khẩu: ")
                id = len(data_py.UserData)
                print('''
                    Vai trò có thể là: 
                ''')
                for i, role1 in enumerate(config.roles, 1):
                    print(f"                       {i}. {role1}")
                roid = input("Vai trò : ")
                for i, role1 in enumerate(config.roles, 1):
                    # print(f"                       {i}. {role1}")
                    if str(roid) == str(i):
                        role = role1
                # print(role)
                if role == "teamleider":
                    team = input("Tên nhóm: ")
                    import logic.team
                    logic.team.create_team(team,id)
                t=logic.reg.register(user, password, id+1, role)
                if isinstance(t, str):print(t)
                # ...
            elif cmd == "add":
                import logic
                team_name = str(input("Tên nhóm: "))
                user_name = str(input("Tên người dùng: "))
                user_id = data_py.find_user_name(user_name).get("id")
                team_id = data_py.team.find_team(team_name)
                # print(team_id, user_id)
                t=logic.team.add_member(team_id,user_id)
                if isinstance(t, str):print(t)
                # ...
            elif cmd == "remove":
                team_name = str(input("Tên nhóm: "))
                user_name = str(input("Tên người dùng: "))
                user_id = data_py.find_user_name(user_name).get("id")
                import logic.team
                team_id = data_py.team.find_team(team_name)
                t=logic.team.remove_member(team_id, user_id)
                if isinstance(t, str):print(t)
                # ...
            elif cmd == "export":
                import logic.export
                print('''
                    Loại xuất:
                        1. Xuất Tuần
                        2. Xuất Học Kỳ
                        3. Xuất Năm
                ''')
                choice = input("Chọn một tùy chọn (1/2/3): ")
                if choice == "1":
                    t1=data_py.summary.read_main("week")
                    for i in range(1, t1["num"]+1):print("Tuần",i)
                    t2=input("Nhập tuần bạn muốn xuất (1 -"+str(t1["num"])+"): ")
                    while not t2.isdigit() or not (1 <= int(t2) <= t1["num"]):
                        print("Vui lòng nhập một số hợp lệ.")
                        t2=input("Nhập tuần bạn muốn xuất (1 -"+str(t1["num"])+"): ")
                    t3=data_py.team.read_mainfile()
                    t4=[]
                    for i in t3["idteam"]:t4.append(i["id_team"])
                    t5={}
                    for i in t4:
                        t6=data_py.summary.read(i, "week", t2)
                        t5[str(i)]=t6
                    t=logic.export.week.__init__(t5)
                    if isinstance(t, str):print(t)
                elif choice == "2":
                    t1=data_py.summary.read_main("semester")
                    for i in range(1, t1["num"]+1):print("Học kỳ",i)
                    t2=input("Nhập học kỳ bạn muốn xuất (1 -"+str(t1["num"])+"): ")
                    while not t2.isdigit() or not (1 <= int(t2) <= t1["num"]):
                        print("Vui lòng nhập một số hợp lệ.")
                        t2=input("Nhập học kỳ bạn muốn xuất (1 -"+str(t1["num"])+"): ")
                    t3=data_py.team.read_mainfile()
                    t4=[]
                    for i in t3["idteam"]:t4.append(i["id_team"])
                    t5={}
                    for i in t4:
                        t6=data_py.summary.read(i, "semester", t2)
                        t5[str(i)]=t6['students']
                    t=logic.export.semester.__init__(t5)
                    if isinstance(t, str):print(t)
                elif choice == "3":
                    t1=data_py.summary.read_main("semester")
                    if  t1["num"] == 2:
                        t3=data_py.team.read_mainfile()
                        t5=data_py.summary.read(1, "year", 1)
                        t=logic.export.year.__init__(t5)
                        if isinstance(t, str):print(t)
                    else:
                        print("Chưa đủ học kỳ để xuất báo cáo năm.")
                else:
                    print("Lựa chọn không hợp lệ.")
            elif cmd == "summary":
                import logic.summary
                print('''
                    Những loại tổng kết:
                    1. Tổng kết hàng tuần
                    2. Tổng kết học kỳ
                    3. Tổng kết hàng năm
                ''')
                choice = input("Chọn một tùy chọn (1/2/3): ")
                if choice == "1":
                    tt=data_py.summary.read_main("week")
                    if data_py.summary.read_main("semester")["num"] == 0 and tt["num"] >= config.semester_1:
                        print("Tối đa tuần học kỳ 1")
                        continue
                    elif data_py.summary.read_main("semester")["num"] == 1 and tt["num"] == config.semester_total:
                        print("Tối đa tuần học kỳ 2")
                        continue
                    elif data_py.summary.read_main("semester")["num"] == 2:
                            print("Tối đa học kỳ")
                            continue
                    t=logic.summary.week.generate_weekly_summary().values()
                    t1=data_py.team.read_mainfile()
                    if isinstance(t, str):
                        print(t)
                        continue
                    for i in t:
                        for k in t1["idteam"]:
                            if k["id_team"] == str(next(iter(i))):
                                print("Tên nhóm:", k["name"])
                        for j in i.values():
                            print("Tên:", j["name"])
                            print("Điểm cổng:", j["give"])
                            print("Điểm trừ:", j["error"])
                            print("Đánh giá:", j["ratings"])
                            print("Tổng điểm:", str(j["total"]))
                elif choice == "2":
                    tt=data_py.summary.read_main("week")
                    # print(tt["num"],type(tt["num"]))
                    if data_py.summary.read_main("semester")["num"] == 0 and not tt["num"] <= config.semester_1:
                        print("Không đủ tuần học kỳ 1")
                        continue
                    elif data_py.summary.read_main("semester")["num"] == 1 and not tt["num"] == config.semester_total:
                        print("Không đủ tuần học kỳ 2")
                        continue
                    elif data_py.summary.read_main("semester")["num"] == 2:
                        print("Tối đa học kỳ")
                        continue
                    t=logic.summary.semester.generate_weekly_summary()
                    t1=data_py.team.read_mainfile()
                    if isinstance(t, str):print(t);continue
                    for i in t:
                        for k in t1["idteam"]:
                            if k["id_team"] == str(next(iter(i))):
                                print("Tên nhóm:", k["name"])
                        for j in i[1]:
                            print("Tên:", j[0])
                            print("Tổng điểm:", str(j[1]))
                            print("Đánh giá:", j[2])
                elif choice == "3":
                    # print(data_py.summary.read_main("semester")["num"],data_py.summary.read_main("semester")["num"]<=2)
                    if not data_py.summary.read_main("semester")["num"] <= 2:
                        print("Không đủ học kỳ")
                        continue
                    else:
                        t=logic.summary.year.generate_weekly_summary()
                        t1=data_py.team.read_mainfile()
                        if isinstance(t, str):print(t);continue
                        for i in t:
                            for k in t1["idteam"]:
                                if k["id_team"] == str(next(iter(i))):
                                    print("Tên nhóm:", k["name"])
                            for j in i[1]:
                                print("Tên:", j[0])
                                print("Tổng điểm:", str(j[1]))    # Đúng thứ tự - Tổng điểm
                                print("Đánh giá:", j[2])       # Đúng thứ tự - Đánh giá
                # ...
        except (AttributeError, KeyError, TypeError, IndexError, ValueError, IOError, OSError, ZeroDivisionError, ImportError, NameError, RuntimeError) as e:
            import traceback
            traceback.print_exc()

def class_monitor(id):
    print(f"Chào mừng, {data_py.find_user(id).get('name')}, Vai trò: {data_py.find_user(id).get('role')}")
    print("Nhập 'exit' để thoát phần miền.")
    print("Nhập 'help' để biết thêm thông tin.")
    while True:
        try:
            cmd = input("> ")
            if cmd == "exit": break
            elif cmd == "help":
                print('''
                    exit: Thoát phần miền
                    help: Hiển thị thông tin trợ giúp
                    list: Liệt kê tất cả học sinh
                    remove: Xóa một lỗi hoặc phần thưởng của học sinh trong lớp
                    summary: Tổng kết mọi thứ
                ''')
            elif cmd == "list":
                import logic.student.my_error_give
                print("Điểm trừ của tôi:")
                for i in logic.student.my_error_give.my_errors(id):
                    print(f" - Loại: {i['name']}, ID: {i['id']}")
                print("Điểm trừ của tôi:", logic.student.my_error_give.cal_errors(id))
                print("Điểm cộng của tôi:")
                for i in logic.student.my_error_give.my_give(id):
                    print(f" - Loại: {i['name']}, ID: {i['id']}")
                print("Điểm cộng của tôi:", logic.student.my_error_give.cal_give(id))
                print("Tổng:", logic.student.my_error_give.cal_total(id))
            elif cmd == "remove":
                input_type = str(input("Type (error/give): "))
                student_name = str(input("Student name: "))
                student_id = data_py.find_user_name(student_name).get("id")
                if input_type == "error":
                    error_id = int(input("Error ID: "))
                    import logic.team.add
                    t=logic.team.add.remove_error(id, student_id, error_id)
                    if isinstance(t, str):print(t)
                    # ...
                elif input_type == "give":
                    give_id = int(input("Give ID: "))
                    import logic.team.add
                    t=logic.team.add.remove_give(id, student_id, give_id)
                    if isinstance(t, str):print(t)
                    # ...
            elif cmd == "summary":
                import logic.summary
                print('''
                    Những loại tổng kết:
                    1. Tổng kết hàng tuần
                    2. Tổng kết học kỳ
                    3. Tổng kết hàng năm
                ''')
                choice = input("Chọn một tùy chọn (1/2/3): ")
                if choice == "1":
                    tt=data_py.summary.read_main("week")
                    if data_py.summary.read_main("semester")["num"] == 0 and tt["num"] >= config.semester_1:
                        print("Tối đa tuần học kỳ 1")
                        continue
                    elif data_py.summary.read_main("semester")["num"] == 1 and tt["num"] == config.semester_total:
                        print("Tối đa tuần học kỳ 2")
                        continue
                    elif data_py.summary.read_main("semester")["num"] == 2:
                            print("Tối đa học kỳ")
                            continue
                    t=logic.summary.week.generate_weekly_summary().values()
                    t1=data_py.team.read_mainfile()
                    if isinstance(t, str):
                        print(t)
                        continue
                    for i in t:
                        for k in t1["idteam"]:
                            if k["id_team"] == str(next(iter(i))):
                                print("Tên nhóm:", k["name"])
                        for j in i.values():
                            print("Tên:", j["name"])
                            print("Điểm cổng:", j["give"])
                            print("Điểm trừ:", j["error"])
                            print("Đánh giá:", j["ratings"])
                            print("Tổng điểm:", str(j["total"]))
                elif choice == "2":
                    tt=data_py.summary.read_main("week")
                    # print(tt["num"],type(tt["num"]))
                    if data_py.summary.read_main("semester")["num"] == 0 and not tt["num"] <= config.semester_1:
                        print("Không đủ tuần học kỳ 1")
                        continue
                    elif data_py.summary.read_main("semester")["num"] == 1 and not tt["num"] == config.semester_total:
                        print("Không đủ tuần học kỳ 2")
                        continue
                    elif data_py.summary.read_main("semester")["num"] == 2:
                        print("Tối đa học kỳ")
                        continue
                    t=logic.summary.semester.generate_weekly_summary()
                    t1=data_py.team.read_mainfile()
                    if isinstance(t, str):print(t);continue
                    for i in t:
                        for k in t1["idteam"]:
                            if k["id_team"] == str(next(iter(i))):
                                print("Tên nhóm:", k["name"])
                        for j in i[1]:
                            print("Tên:", j[0])
                            print("Tổng điểm:", str(j[1]))
                            print("Đánh giá:", j[2])
                elif choice == "3":
                    # print(data_py.summary.read_main("semester")["num"],data_py.summary.read_main("semester")["num"]<=2)
                    if not data_py.summary.read_main("semester")["num"] <= 2:
                        print("Không đủ học kỳ")
                        continue
                    else:
                        t=logic.summary.year.generate_weekly_summary()
                        t1=data_py.team.read_mainfile()
                        if isinstance(t, str):print(t);continue
                        for i in t:
                            for k in t1["idteam"]:
                                if k["id_team"] == str(next(iter(i))):
                                    print("Tên nhóm:", k["name"])
                            for j in i[1]:
                                print("Tên:", j[0])
                                print("Tổng điểm:", str(j[1]))    # Đúng thứ tự - Tổng điểm
                                print("Đánh giá:", j[2])       # Đúng thứ tự - Đánh giá
                else:
                    print("Invalid choice.")
        except (AttributeError, KeyError, TypeError, IndexError, ValueError, IOError, OSError, ZeroDivisionError, ImportError, NameError, RuntimeError) as e:
            import traceback
            traceback.print_exc()

def teamleider(id):
    print(f"Chào mừng, {data_py.find_user(id).get('name')}, Vai trò: {data_py.find_user(id).get('role')}")
    print("Nhập 'exit' để thoát phần miền.")
    print("Nhập 'help' để trợ giúp.")
    while True:
        try:
            cmd = input("> ")
            if cmd == "exit": break
            elif cmd == "help":
                print('''
                    exit: Thoát phần mềm
                    help: Hiển thị thông điệp trợ giúp này
                    list: Liệt kê tất cả học sinh trong nhóm của tôi
                    add: Thêm lỗi hoặc cho một học sinh trong nhóm của tôi
                ''')
            elif cmd == "list":
                t=data_py.team.list_teams(id)
                if isinstance(t, str):print(t);continue
                for i in t:
                    print(f" - Tên: {i[0]}, ID: {i[1]}")
            elif cmd == "add":
                input_type = str(input("Loại (error/give): "))
                student_name = str(input("Tên học sinh: "))
                how = int(input("Số lượng: "))
                while how <= 0:
                    print("Vui lòng nhập một số dương.")
                    how = int(input("Số lượng: "))
                student_id = data_py.find_user_name(student_name).get("id")
                if input_type == "error":
                    error_id = int(input("Điểm trừ ID: "))
                    import logic.team.add
                    for i in range(how):
                        t=logic.team.add.add_error(id, student_id, error_id)
                        if isinstance(t, str):print(t);continue
                elif input_type == "give":
                    give_id = int(input("Điểm cộng ID: "))
                    import logic.team.add
                    for i in range(how):
                        t=logic.team.add.add_give(id, student_id, give_id)
                        if isinstance(t, str):print(t);continue
                        # ...
        except (AttributeError, KeyError, TypeError, IndexError, ValueError, IOError, OSError, ZeroDivisionError, ImportError, NameError, RuntimeError) as e:
            import traceback
            traceback.print_exc()

def student(id):
    print(f"Chào mừng, {data_py.find_user(id).get('name')}, Vai trò: {data_py.find_user(id).get('role')}")
    print("Nhập 'exit' để thoát phần mềm.")
    print("Nhập 'help' để trợ giúp.")
    while True:
        try:
            cmd = input("> ")
            if cmd == "exit": break
            elif cmd == "help":
                print('''
                    exit: Thoát phần mềm
                    help: Hiển thị thông điệp trợ giúp này
                    list: Liệt kê điểm trừ và điểm cộng của tôi
                ''')
            elif cmd == "list":
                import logic.student.my_error_give
                print("Điểm trừ của tôi:")
                for i in logic.student.my_error_give.my_errors(id):
                    print(f" - Loại: {i['name']}, ID: {i['id']}")
                print("Điểm trừ của tôi:", logic.student.my_error_give.cal_errors(id))
                print("Điểm cộng của tôi:")
                for i in logic.student.my_error_give.my_give(id):
                    print(f" - Loại: {i['name']}, ID: {i['id']}")
                print("Điểm cộng của tôi:", logic.student.my_error_give.cal_give(id))
                print("Tổng:", logic.student.my_error_give.cal_total(id))
        except (AttributeError, KeyError, TypeError, IndexError, ValueError, IOError, OSError, ZeroDivisionError, ImportError, NameError, RuntimeError) as e:
            import traceback
            traceback.print_exc()