from gui.function import *
import flet as ft
import data_py
import logic
import config
import logic.student.my_error_give

id1=0
column=["STT","Tên học sinh", "Tổ", "Điểm cộng", "Điểm trừ", "Tổng điểm cộng"]
data_py.load_users()
 
t1=[]
for i in data_py.UserData.values():
    # print(i)
    if i['role'] != config.roles[0]:
        t1.append(i['id'])


def gui(page: ft.Page):
    t2=[]
    row1=[]
    def load():
        row1.clear()
        data_py.UserData= {}
        data_py.load_users()
        t2.clear()

        for i in data_py.UserData.values():
            if i['role'] != config.roles[0] and i['role'] == config.roles[2]:
                team_name=''
                for j in data_py.team.read_mainfile()['idteam']:
                    if j['id_team'] == i['id']:
                        team_name=j['name']
                t2.append([
                    i['id'],
                    i['name'],
                    team_name,
                    logic.student.my_error_give.cal_give(i['id']),
                    logic.student.my_error_give.cal_errors(i['id']),
                    logic.student.my_error_give.cal_total(i['id'])
                ])
            elif i['role'] != config.roles[0]:
                team_name=''
                for j in data_py.team.read_mainfile()['idteam']:
                    t4=data_py.team.read_teamfile(j['id_team'])
                    for h in t4['members']:
                        if h == i['id']:
                            team_name=j['name']
                            break
                t2.append([
                    i['id'],
                    i['name'],
                    team_name,
                    logic.student.my_error_give.cal_give(i['id']),
                    logic.student.my_error_give.cal_errors(i['id']),
                    logic.student.my_error_give.cal_total(i['id'])])
        for i in t2:
            row1.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(i[0])),
                        ft.DataCell(ft.Text(i[1])),
                        ft.DataCell(ft.Text(i[2])),
                        ft.DataCell(ft.Text(i[3])),
                        ft.DataCell(ft.Text(i[4])),
                        ft.DataCell(ft.Text(i[5]))
                    ]
                )
            )


    load()

    page.title = "Giáo viên"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 1100
    page.window.height = 770
    # page.window.full_screen=True
    page.window.resizable = False
    page.window.maximizable=False
    page.window.center()
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Row(
                        controls=[
                            ft.Text(f"Xin chào Giáo viên {data_py.find_user(id1).get('name')}", size=20)
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Column(
                        controls=[
                            ft.DataTable(
                                vertical_lines=ft.border.BorderSide(3, ft.Colors.BLUE),
                                horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREEN),
                                border=ft.border.all(2, ft.Colors.RED),
                                column_spacing=140,
                                heading_row_height=50,
                                border_radius=10,
                                columns=[
                                    ft.DataColumn(ft.Text(col)) for col in column
                                ],
                                rows=row1
                            )
                        ],
                        scroll=ft.ScrollMode.ALWAYS,
                        height=480,
                        width=1100
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Text(value="Tổng kết", size=20),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER, 
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.OutlinedButton(text="Tuần", width=85, on_click=lambda e: page.go("/summary/week")),
                                                ft.OutlinedButton(text="Học kỳ", width=95, on_click=lambda e: page.go("/summary/semester"))
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER, 
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.OutlinedButton(text="Năm học", width=110, on_click=lambda e: page.go("/summary/year"))
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER, 
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                border=ft.border.all(2, ft.Colors.RED),
                                border_radius=10,
                                height=130,
                                width=200,
                                # alignment=ft.MainAxisAlignment.END
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Text(value="Xuất file excel", size=20),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER, 
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.OutlinedButton(text="Tuần", width=85, on_click=lambda e: page.go("/export/week")),
                                                ft.OutlinedButton(text="Học kỳ", width=95, on_click=lambda e: page.go("/export/semester"))
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER, 
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.OutlinedButton(text="Năm học", width=110, on_click=lambda e: page.go("/export/year"))
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER, 
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                border=ft.border.all(2, ft.Colors.RED),
                                border_radius=10,
                                height=130,
                                width=200,
                                # alignment=ft.MainAxisAlignment.END
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Text(value="Tài khoản", size=20),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER, 
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.OutlinedButton(text="Thêm tài khoản", width=150, on_click=lambda e: page.go("/createAccount"))
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER, 
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                border=ft.border.all(2, ft.Colors.RED),
                                border_radius=10,
                                height=130,
                                width=200,
                                # alignment=ft.MainAxisAlignment.END
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Row(
                        controls=[ft.OutlinedButton(text="Thoát", width=100, on_click=lambda e: page.window.destroy())],
                        alignment=ft.MainAxisAlignment.END
                    )
                    
                ]
            ))
        
        if page.route == "/summary/week":
            t4=ft.Column(
                controls=[],
                scroll=ft.ScrollMode.ALWAYS,
                width=700,
                height=650
            )

            def click(e):
                t7=logic.summary.week.generate_weekly_summary().values()
                t8=data_py.team.read_mainfile()
                for i in t7:
                    for k in t8["idteam"]:
                        if str(k["id_team"]) == str(next(iter(i))):
                            t4.controls.append(ft.Text(f"Tên nhóm: {k["name"]}", size=18))
                    for j in i.values():
                        t4.controls.append(ft.Text(
                            f"Tên: {j['name']}, điểm cộng: {j['give']}, điểm trừ: {j["error"]}, đánh giá: {j["ratings"]}, Tổng điểm: {str(j["total"])}",
                            size=18
                        ))
                t5.disabled=True
                page.update()

                
            
            t5=ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=False)

            row2=[]

            tt=data_py.summary.read_main("week")
            if data_py.summary.read_main("semester")["num"] == 0 and tt["num"] >= config.semester_1:
                row2.append(ft.Text("Tối đa tuần học kỳ 1", size=20))
                t5.disabled=True
                page.update()
            elif data_py.summary.read_main("semester")["num"] == 1 and tt["num"] == config.semester_total:
                row2.append(ft.Text("Tối đa tuần học kỳ 2", size=20))
                t5.disabled=True
                page.update()
            elif data_py.summary.read_main("semester")["num"] == 2:
                row2.append(ft.Text("Tối đa học kỳ", size=20))
                t5.disabled=True
                page.update()
            t6=ft.Column(
                controls=row2
            )
                    

            
            page.views.append(
                ft.View(
                    "/summary/week",
                    [
                        ft.AppBar(title=ft.Text("Tổng kết - Tuần"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        t5,t6,t4
                    ]
                )
            )
        if page.route == "/summary/semester":
            t4=ft.Column(
                controls=[],
                scroll=ft.ScrollMode.ALWAYS,
                width=700,
                height=650
            )

            def click(e):
                t7=logic.summary.semester.generate_weekly_summary()
                t8=data_py.team.read_mainfile()
                for i in t7:
                    for k in t8["idteam"]:
                        if str(k["id_team"]) == str(next(iter(i))):
                            t4.controls.append(ft.Text(f"Tên nhóm: {k["name"]}", size=18))
                    for j in i[1]:
                        t4.controls.append(ft.Text(
                            f"Tên: {j[0]}, đánh giá: {j[2]}, Tổng điểm: {j[1]}",
                            size=18
                        ))
                t5.disabled=True
                page.update()

            t5=ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=False)

            row2=[]

            tt=data_py.summary.read_main("week")
            if data_py.summary.read_main("semester")["num"] == 0 and not tt["num"] <= config.semester_1:
                row2.append(ft.Text("Tối đa tuần học kỳ 1", size=20))
                t5.disabled=True
                page.update()
            elif data_py.summary.read_main("semester")["num"] == 1 and not tt["num"] == config.semester_total:
                row2.append(ft.Text("Tối đa tuần học kỳ 2", size=20))
                t5.disabled=True
                page.update()
            elif data_py.summary.read_main("semester")["num"] == 2:
                row2.append(ft.Text("Tối đa học kỳ", size=20))
                t5.disabled=True
                page.update()

            t6=ft.Column(
                controls=row2
            )

            page.views.append(
                ft.View(
                    "/error",
                    [
                        ft.AppBar(title=ft.Text("Tổng kết - Học kỳ"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        t5,t6,t4
                    ]
                )
            )
        if page.route == "/summary/year":

            t4=ft.Column(
                controls=[],
                scroll=ft.ScrollMode.ALWAYS,
                width=700,
                height=650
            )

            def click(e):
                t7=logic.summary.year.generate_weekly_summary()
                t8=data_py.team.read_mainfile()
                for i in t7:
                    for k in t8["idteam"]:
                        if str(k["id_team"]) == str(next(iter(i))):
                            t4.controls.append(ft.Text(f"Tên nhóm: {k["name"]}", size=18))
                    for j in i[1]:
                        t4.controls.append(ft.Text(
                            f"Tên: {j[0]}, đánh giá: {j[2]}, Tổng điểm: {j[1]}",
                            size=18
                        ))
                t5.disabled=True
                page.update()

            t5=ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=False)

            row2=[]

            if not data_py.summary.read_main("semester")["num"] <= 2:
                row2.append(ft.Text("Không đử học kỳ", size=20))
                t6.controls=row2
            
            t6=ft.Column(
                controls=row2
            )
            page.views.append(
                ft.View(
                    "/summary/year",
                    [
                        ft.AppBar(title=ft.Text("Tổng kết - Học kỳ"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        t5,t6,t4
                    ]
                )
            )
        
        if page.route == "/export/week":
            t4=data_py.summary.read_main("week")
            row3=[]
            for i in range(1, t4["num"]+1):
                if i<=9:
                    row3.append(ft.Checkbox(label=f"Tuần 0{i}"))
                else:
                    row3.append(ft.Checkbox(label=f"Tuần {i}"))
            t5=[]
            for i in data_py.team.read_mainfile()["idteam"]:t5.append(i["id_team"])
            t6={}
            def check(e):
                t8=find_selected_numbers_end(row3)
                # print(t8)
                if t8!=[]:
                    # print(1)
                    t10.disabled=False
                    page.update()
                    for i in t5:
                        t7=data_py.summary.read(i, "week", int(t8[-1]))
                        t6[str(i)]=t7
                else:
                    t10.disabled=True
                    page.update()
            for i in row3:
                i.on_change=check
            def click(e):
                # print(t6)
                t9.value="Đã xuất ra file mang tên"+logic.export.week.__init__(t6)
                page.update()
            t9=ft.Text(value="",size=20)
            t10=ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=True)
            page.views.append(
                ft.View(
                    "/export/week",
                    [
                        ft.AppBar(title=ft.Text("Xuất ra file excel - Tuần"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.Row(
                            controls=[
                                ft.Column(
                                    controls=row3,
                                    scroll=ft.ScrollMode.ALWAYS,
                                    height=650,
                                    width=100
                                ),
                                t10,
                                t9
                            ]
                        )
                    ]
                )
            )
        if page.route == "/export/semester":
            t4=data_py.summary.read_main("semester")
            row3=[]
            for i in range(1, t4["num"]+1):
                if i<=9:
                    row3.append(ft.Checkbox(label=f"Học kỳ 0{i}"))
                else:
                    row3.append(ft.Checkbox(label=f"Học kỳ {i}"))
            t5=[]
            for i in data_py.team.read_mainfile()["idteam"]:t5.append(i["id_team"])
            t6={}
            def check(e):
                t8=find_selected_numbers_end(row3)
                if t8!=[]:
                    t10.disabled=False
                    page.update()
                    for i in t5:
                        t7=data_py.summary.read(i, "semester", int(t8[-1]))
                        t6[str(i)]=t7['students']
                else:
                    t10.disabled=True
                    page.update()
            for i in row3:
                i.on_change=check
            def click(e):
                t9.value="Đã xuất ra file mang tên "+logic.export.semester.__init__(t6)
                page.update()
            t9=ft.Text(value="",size=20)
            t10=ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=True)
            page.views.append(
                ft.View(
                    "/export/semester",
                    [
                        ft.AppBar(title=ft.Text("Xuất ra file excel - Học kỳ"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.Row(
                            controls=[
                                ft.Column(
                                    controls=row3,
                                    scroll=ft.ScrollMode.ALWAYS,
                                    height=100,
                                    width=100
                                ),
                                t10,
                                t9
                            ]
                        )
                    ]
                )
            )
        if page.route == "/export/year":
            def click(e):
                t5=data_py.summary.read(1, "year", 1)
                t9.value="Đã xuất ra file mang tên "+logic.export.year.__init__(t5)
                page.update()
            t10=ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=False)
            t9=ft.Text(value="",size=20)
            page.views.append(
                ft.View(
                    "/export/year",
                    [
                        ft.AppBar(title=ft.Text("Xuất ra file excel - Nắm học"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.Row([
                                t10,
                                t9
                            ]
                        )
                    ]
                )
            )
        
        if page.route == "/createAccount":
            t3=ft.TextField(
                label="Tên",
                width=300,
                text_align=ft.TextAlign.LEFT
            )

            t4=ft.TextField(
                label="Mật khẩu",
                width=300,
                password=True,
                text_align=ft.TextAlign.LEFT
            )

            t5=ft.Text(value=config.roles[3],size=20)

            t6=ft.TextField(
                label="Tên tổ",
                width=300,
                text_align=ft.TextAlign.LEFT,
                visible=False
            )

            t7=ft.ListView(spacing=10, padding=20, width=300, visible=True)
            

            class State1:
                def __init__(self):
                    self.selected_role = ''

            state1 = State1()

            def click1(e):
                state1.selected_role = e.control.text
                page.update()

            for i in data_py.team.read_mainfile()['idteam']:
                t7.controls.append(ft.Button(i['name'], on_click=click1))
            class State:
                def __init__(self):
                    self.selected_role = config.roles[3]

            state = State()

            def click(e):
                state.selected_role = e.control.text
                t5.value = e.control.text
                if e.control.text == config.roles[2]:
                    t6.visible = True
                    t7.visible = False
                else:
                    t7.visible = True
                    t6.visible = False
                page.update()

            def click2(e):
                if not t3.value or not t4.value:
                    page.show_snack_bar(ft.SnackBar(content=ft.Text("Vui lòng nhập tên và mật khẩu")))
                    return
                
                if not state.selected_role:
                    page.show_snack_bar(ft.SnackBar(content=ft.Text("Vui lòng chọn vai trò")))
                    return
                id2 = len(data_py.UserData)
                t10=logic.reg.register(t3.value, t4.value, id2+1, state.selected_role)
                if t10 == "Tạo tài khoản thành công.":
                    if state.selected_role != config.roles[2]:
                        logic.team.add_member(data_py.team.find_team(state1.selected_role),id2+1)
                    else:
                        logic.team.create_team(t6.value,id2)
                    load()
                    page.update()
                    page.go('/')
                    
            page.views.append(
                ft.View(
                    "/createAccount",
                    [
                        ft.AppBar(title=ft.Text("Tạo tài khoản"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        # Container bọc ngoài để căn giữa theo chiều dọc và ngang
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    t3,
                                    t4,
                                    ft.Container(
                                        content=ft.Row(
                                            [
                                                ft.PopupMenuButton(
                                                    icon=ft.Icons.VIEW_LIST,
                                                    items=[
                                                        ft.PopupMenuItem(text=config.roles[1], on_click=click),
                                                        ft.PopupMenuItem(text=config.roles[2], on_click=click),
                                                        ft.PopupMenuItem(text=config.roles[3], on_click=click),
                                                        
                                                    ]
                                                ),
                                                t5
                                            ],
                                            # horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
                                            alignment=ft.MainAxisAlignment.CENTER, 
                                        ),
                                        alignment=ft.alignment.center, 
                                        # expand=True 
                                    ),
                                    t6,
                                    t7,
                                    ft.ElevatedButton(
                                        text="Tạo tài khoản",
                                        width=200,
                                        height=40,
                                        on_click=click2
                                    )
                                ],
                                spacing=20, 
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
                                alignment=ft.MainAxisAlignment.CENTER, 
                            ),
                            alignment=ft.alignment.center, 
                            expand=True 
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