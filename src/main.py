import flet as ft
from func.downloadFuncs import downloadAudio, downloadVideo


def main(page: ft.Page):
   
   page.window.title_bar_buttons_hidden = True
   page.window.title_bar_hidden = True
   
   page.window.width = 800
   page.window.height = 300
   
   page.window.resizable = False
   page.window.maximizable = False
   
   page.theme = ft.Theme(color_scheme_seed=ft.Colors.RED_900)
   
   
   async def closeWindow(e: ft.Event[ft.IconButton]):
       await page.window.close()
   
   async def minimizeWindow(e: ft.Event[ft.IconButton]):
       page.window.minimized = True
       
   
   titlebar = ft.WindowDragArea(
       expand=False,
       content=ft.Container(
           ft.Row([
               ft.IconButton(icon=ft.Icons.MORE_VERT),
               ft.Container(expand=True, content=ft.Text("YT-DLP Frontend"),),
               
               ft.IconButton(icon=ft.Icons.MINIMIZE, on_click=minimizeWindow),
               ft.IconButton(icon=ft.Icons.CLOSE, on_click=closeWindow)
           ])
       )
   )
   
   urlBar = ft.TextField(multiline=False, label="Type/Paste your URL here", expand=True)  
                  

   downloadtypeDropdown = ft.Dropdown(
       label="Download Type",
       options=[
           ft.DropdownOption(key="video", text="Video"),
           ft.DropdownOption(key="audio", text="Audio")
       ]
   )
   
   def downloadContent():
       if not urlBar.value:
           page.show_dialog(ft.SnackBar(ft.Text("Please paste in a URL")))
           return
    
       
       if downloadtypeDropdown.value == "video":
           downloadVideo(urlBar.value)
       elif downloadtypeDropdown.value == "audio":
           downloadAudio(urlBar.value)
   
   
   page.add(
       ft.Container(
           ft.Column([
            titlebar,
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    [
                        urlBar,
                        ft.Row([downloadtypeDropdown, ft.FilledButton("Download", on_click=lambda e: downloadContent())]),
                        
                    ],
                ),
                
            )
        ], expand=True),
           padding=5
       )
        
    )


ft.run(main)
