import random
import time
import threading
import flet as ft

hacker_lines = [
    "Initializing root access...",
    "Bypassing firewall v4.2...",
    "Downloading personal gallery & contacts...",
    "Injecting payload into system kernel...",
    "Accessing front camera...",
    "DIQQAT: Telefoningiz nazoratga olindi! 😈",
    "Barcha parollar serverga yuborilmoqda...",
    "01010011 01100101 01100011 01110101 01110010 01101001 01110101",
    "Hazil aka, xavotir olmang, hamma narsa joyida! 😉",
    "Decrypting database...",
    "Establishing secure backdoor connection...",
    "System override successful.",
]

def main(page: ft.Page):
    page.title = "System Breach"
    page.bgcolor = ft.colors.BLACK
    page.padding = 20
    page.window_full_screen = True
    
    text_view = ft.Text(
        value="",
        color=ft.colors.GREEN_ACCENT,
        font_family="Courier",
        size=14,
        weight=ft.FontWeight.BOLD,
    )
    
    can_exit = [False]
    exit_view = ft.Text(
        value="",
        color=ft.colors.RED,
        size=16,
        weight=ft.FontWeight.BOLD,
    )

    def on_tap(e):
        if can_exit[0]:
            page.window_close()

    container = ft.Container(
        content=ft.Column(
            [
                ft.Row([text_view], expand=True),
                exit_view
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        expand=True,
        on_click=on_tap,
    )
    
    page.add(container)

    lines = []
    def update_loop():
        while True:
            new_line = random.choice(hacker_lines)
            lines.append(new_line)
            if len(lines) > 22:
                lines.pop(0)
            text_view.value = "\n".join(lines)
            page.update()
            time.sleep(0.08)

    def enable_exit_timer():
        time.sleep(5.0)
        can_exit[0] = True
        exit_view.value = "[ Hazil tugadi! Chiqish uchun ekranni bosing ]"
        page.update()

    threading.Thread(target=update_loop, daemon=True).start()
    threading.Thread(target=enable_exit_timer, daemon=True).start()

ft.app(target=main)