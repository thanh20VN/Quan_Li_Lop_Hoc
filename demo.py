# from time import sleep
# import flet as ft


# def main(page: ft.Page):

#     lv = ft.ListView(spacing=10, padding=20, width=150)
#     lvc = ft.Container(
#         content=lv,
#         bgcolor=ft.Colors.GREY_500,
#     )
#     c = ft.Row(
#         [
#             lvc,
#             ft.PopupMenuButton(
#                 items=[lvc]
#             )
#         ],
#         expand=True,
#         vertical_alignment=ft.CrossAxisAlignment.START,
#     )

#     count = 1

#     for i in range(0, 60):
#         lv.controls.append(ft.Button(f"Line {count}", color=ft.Colors.ON_SECONDARY))
#         count += 1

#     page.add(c)

#     for i in range(0, 60):
#         sleep(1)
#         lv.controls.append(ft.Text(f"Line {count}", color=ft.Colors.ON_SECONDARY))
#         count += 1
#         page.update()


# ft.app(main)


import flet as ft

def main(page: ft.Page):
    page.title = "ListView with Icons"
    page.vertical_alignment = ft.CrossAxisAlignment.START

    # Create a ListView
    my_list_view = ft.ListView(
        expand=True,
        spacing=10,
        padding=20,
        # height=10,
        # width=80,
        controls=[
            ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.AMBER),
                    ft.Text("Item 1 with a star"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.HOME, color=ft.Colors.BLUE_500),
                    ft.Text("Item 2 with a home icon"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.SETTINGS, color=ft.Colors.GREY_700, size=20),
                    ft.Text("Item 3 with settings icon"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN_ACCENT_700),
                    ft.Text("Item 4 with a checkmark"),
                ]
            ),
        ]
    )

    page.add(my_list_view)

if __name__ == "__main__":
    ft.app(target=main)