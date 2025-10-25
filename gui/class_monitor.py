from gui.function import *
import flet as ft
import data_py
import logic
import config

id1=0
column=["ID","Lỗi vi phạm","Điểm trừ / cộng","Số lần"]
data_py.load_users()
# print(data_py.UserData)
t3=[]
for i in data_py.UserData.values():
    # print(i)
    if i['role'] != config.roles[0]:
        t3.append(i['id'])

t23=''
def gui(page: ft.Page):
    t1=list1("error",id1)
    t2=list1("give",id1)
    row1=[]
    for i in t1:
        row1.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(i["id"]))),
                    ft.DataCell(ft.Text(i["name"])),
                    ft.DataCell(ft.Text(str(i["point"]))),
                    ft.DataCell(ft.Text(str(i["count"]))),
                ]
            )
        )
    
    row2=[]
    for i in t2:
        row2.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(i["id"]))),
                    ft.DataCell(ft.Text(i["name"])),
                    ft.DataCell(ft.Text(str(i["point"]))),
                    ft.DataCell(ft.Text(str(i["count"]))),
                ]
            )
        )
    
    row3=[]
    for i in t3:
        t8=data_py.find_user(i)
        row3.append(
            ft.Checkbox(label=str(t8["id"])+" ."+t8["name"], value=False)
        )

    page.title = "Lớp trưởng"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 1100
    page.window.height = 770
    # page.window.full_screen=True
    page.window.resizable = False
    page.window.maximizable=False
    page.window.center()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Row(
                        controls=[
                            ft.Text(f"Xin chào lớp trưởng {data_py.find_user(id1).get('name')}", size=20)
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Text("Danh sách vi phạm:", size=16),
                                    ft.DataTable(
                                        vertical_lines=ft.border.BorderSide(3, ft.Colors.BLUE),
                                        horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREEN),
                                        border=ft.border.all(2, ft.Colors.RED),
                                        border_radius=10,
                                        columns=[
                                            ft.DataColumn(ft.Text(col)) for col in column
                                        ],
                                        rows=row1
                                    ),
                                    ft.Text("Tổng điểm: -"+str(logic.student.my_error_give.cal_errors(id1)), size=20),
                                ],
                                scroll=ft.ScrollMode.ALWAYS,
                                height=600,
                                width=500
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text("Danh sách Cộng điểm:", size=16),
                                    ft.DataTable(
                                        vertical_lines=ft.border.BorderSide(3, ft.Colors.BLUE),
                                        horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREEN),
                                        border=ft.border.all(2, ft.Colors.RED),
                                        border_radius=10,
                                        columns=[
                                            ft.DataColumn(ft.Text(col)) for col in column
                                        ],
                                        rows=row2
                                    ),
                                    ft.Text("Tổng điểm: +" + str(logic.student.my_error_give.cal_give(id1)), size=20),
                                ],
                                scroll=ft.ScrollMode.ALWAYS,
                                height=600,
                                width=500
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(
                        controls=[
                            ft.Button(text="Tổng kết", width=100, on_click=lambda e: page.go("/summary")),
                            ft.Button(text="Xoá lỗi", width=100, on_click=lambda e: page.go("/remove")),
                            ft.Button(text="Thoát", width=100, on_click=lambda e: page.window.destroy())
                        ],
                        alignment=ft.MainAxisAlignment.END
                    ),
                ]
            ))
        if page.route == "/remove":
            row4 = []
            t7 = ft.Column(
                controls=row4,
                scroll=ft.ScrollMode.ALWAYS,
                width=300,
                height=650,
                visible=False
            )

            def click1(e):
                t13=find_selected_numbers(row3)
                t14=data_py.team.read_mainfile()['idteam']
                t15=find_selected_numbers(row4)
                idt=0
                for i in t14:
                    if t13[-1] in data_py.team.read_teamfile(i['id_team'])['members']:
                        idt=data_py.team.read_teamfile(i['id_team'])['teamleider_id']
                # print(text1['textField'])
                for i in range(int(text1.value)):
                    t=logic.team.remove.remove_error(idt, t13[-1], t15[-1])
                    # print(t)
                    if t:
                        row4.clear()
                        # row3.clear()
                        for checkbox in row3:
                            checkbox.value=False
                        page.go("/")

            text1 = ft.TextField(label="Mấy lần", width=300, height=100, text_align=ft.TextAlign.LEFT)
            buton = ft.Button(text="Xác nhận", width=100, height=50, on_click=click1, disabled=False)

            t9 = ft.Column(
                controls=[text1, buton],
                scroll=ft.ScrollMode.ALWAYS,
                width=200,
                height=650,
                visible=False
            )

            def check1(e):
                is_valid = check_single_true(row3)
                if is_valid:
                    t4 = find_selected_numbers(row3)
                    t6 = list2("error", int(t4[-1]))
                    row4.clear()
                    for i in t6:
                        row4.append(
                            ft.Checkbox(label=str(i["id"]) + "." + i["name"] + ", Số lần: " + str(i["count"]), value=False)
                        )
                    if not row4:  # Nếu không có lỗi nào
                        row4.append(ft.Text(value="Không có lỗi nào"))
                    else:
                        t9.visible = True
                    t7.controls = row4
                    t7.visible = True
                else:
                    t7.visible = False
                    t9.visible = False
                page.update()

            for checkbox in row3:
                checkbox.on_change = check1



            page.views.append(
                ft.View(
                    "/remove",
                    [
                        ft.AppBar(title=ft.Text("Xoá lỗi / điểm cộng"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.Row(
                            controls=[
                                ft.Column(
                                    controls=row3,
                                    scroll=ft.ScrollMode.ALWAYS,
                                    width=200,
                                    height=650
                                ),
                                t7,
                                t9
                            ],
                            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ]
                )
            )
        if page.route == "/summary":
            t15=ft.Checkbox(label="Tuần")
            t16=ft.Checkbox(label="Học kỳ")
            t17=ft.Checkbox(label="Năm học")
            t18 = ft.Column(
                controls=[
                    t15,
                    t16,
                    t17
                ]
            )
            row5=[]
            t21=ft.Column(
                controls=row5,
                visible=True
            )
            # print(t21.controls)
            t25=ft.Column(
                controls=[],
                scroll=ft.ScrollMode.ALWAYS,
                width=700,
                height=650
            )
            def click(e):
                if t23=="Tuần":
                    t24=logic.summary.week.generate_weekly_summary().values()
                    t26=data_py.team.read_mainfile()
                    for i in t24:
                        for k in t26["idteam"]:
                            # print(str(next(iter(i))),k['id_team'],str(k["id_team"]) == str(next(iter(i))))
                            if str(k["id_team"]) == str(next(iter(i))):
                                t25.controls.append(ft.Text(f"Tên nhóm: {k["name"]}", size=18))
                    #             print("Tên nhóm:", k["name"])
                        for j in i.values():
                            t25.controls.append(ft.Text(
                                f"Tên: {j['name']}, điểm cộng: {j['give']}, điểm trừ: {j["error"]}, đánh giá: {j["ratings"]}, Tổng điểm: {str(j["total"])}",
                                size=18
                            ))
                    t22.disabled=True
                    page.update()

                elif t23=="Học kỳ":
                    t24=logic.summary.semester.generate_weekly_summary()
                    t26=data_py.team.read_mainfile()
                    for i in t24:
                        for k in t26["idteam"]:
                            # print(str(next(iter(i))),k['id_team'],str(k["id_team"]) == str(next(iter(i))))
                            if str(k["id_team"]) == str(next(iter(i))):
                                t25.controls.append(ft.Text(f"Tên nhóm: {k["name"]}", size=18))
                    #             print("Tên nhóm:", k["name"])
                        for j in i[1]:
                            t25.controls.append(ft.Text(
                                f"Tên: {j[0]}, đánh giá: {j[1]}, Tổng điểm: {j[2]}",
                                size=18
                            ))
                    t22.disabled=True
                    page.update()
                elif t23=="Năm học":
                    t24=logic.summary.year.generate_weekly_summary()
                    t26=data_py.team.read_mainfile()
                    for i in t24:
                        for k in t26["idteam"]:
                            # print(str(next(iter(i))),k['id_team'],str(k["id_team"]) == str(next(iter(i))))
                            if str(k["id_team"]) == str(next(iter(i))):
                                t25.controls.append(ft.Text(f"Tên nhóm: {k["name"]}", size=18))
                    #             print("Tên nhóm:", k["name"])
                        for j in i[1]:
                            t25.controls.append(ft.Text(
                                f"Tên: {j[0]}, đánh giá: {j[1]}, Tổng điểm: {j[2]}",
                                size=18
                            ))
                    t22.disabled=True
                    page.update()
            t22=ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=False)
            def check3(e):
                global t23
                is_valid = check_single_true([t15,t16,t17])
                if is_valid:
                    t19=find_selected_text([t15,t16,t17])
                    tt=data_py.summary.read_main("week")
                    if t19[-1]=="Tuần":
                        t23='Tuần'
                        row5.clear()
                        if data_py.summary.read_main("semester")["num"] == 0 and tt["num"] >= config.semester_1:
                            row5.append(ft.Text("Tối đa tuần học kỳ 1", size=20))
                            t21.controls=row5
                            page.update()
                        elif data_py.summary.read_main("semester")["num"] == 1 and tt["num"] == config.semester_total:
                            row5.append(ft.Text("Tối đa tuần học kỳ 2", size=20))
                            t21.controls=row5
                            page.update()
                        elif data_py.summary.read_main("semester")["num"] == 2:
                            row5.append(ft.Text("Tối đa học kỳ", size=20))
                            t21.controls=row5
                            page.update()
                        else:
                            t21.visible= True
                            row5.append(t22)
                            t21.controls=row5
                            page.update()
                    elif t19[-1]=="Học kỳ":
                        t23='Học kỳ'
                        row5.clear()
                        if data_py.summary.read_main("semester")["num"] == 0 and not tt["num"] <= config.semester_1:
                            row5.append(ft.Text("Tối đa tuần học kỳ 1", size=20))
                            t21.controls=row5
                            page.update()
                        elif data_py.summary.read_main("semester")["num"] == 1 and not tt["num"] == config.semester_total:
                            row5.append(ft.Text("Tối đa tuần học kỳ 2", size=20))
                            t21.controls=row5
                            page.update()
                        elif data_py.summary.read_main("semester")["num"] == 2:
                            row5.append(ft.Text("Tối đa học kỳ", size=20))
                            t21.controls=row5
                            page.update()
                        else:
                            t21.visible= True
                            row5.append(t22)
                            t21.controls=row5
                            page.update()
                    elif t19[-1]=="Năm học":
                        t23='Năm học'
                        row5.clear()
                        if not data_py.summary.read_main("semester")["num"] <= 2:
                            row5.append(ft.Text("Không đử học kỳ", size=20))
                            t21.controls=row5
                        else:
                            t21.visible= True
                            row5.append(t22)
                            t21.controls=row5
                            page.update()
                else:
                    row5.clear()
                    t21.controls=row5
                    page.update()


            for i in [t15,t16,t17]:
                i.on_change=check3

            page.views.append(
                ft.View(
                    "/summary",
                    [
                        ft.AppBar(title=ft.Text("Tổng kết"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.Row(
                            controls=[
                                t18,t21,t25
                            ]
                            # expand=True,
                        )
                    ]
                )
            )
        page.update()

    def view_pop(view):
        if page.views:
            page.views.pop()
        if page.views:
            top_view = page.views[-1]
            page.go(top_view.route)
        else:
            page.go("/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
def __init__(page1,id):
    global id1
    id1=id
    gui(page1)