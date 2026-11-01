import tkinter as tk
from functools import partial


def addRightClickMenu(master, command_dict: dict[str:function]):
    context_menu = tk.Menu(master, tearoff=0)
    for label, command in command_dict.items():
        context_menu.add_command(label=label, command=command)

    def do_popup(event):
        try:
            # Display the context menu at the mouse pointer's position
            context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            # Release the mouse grab properly
            context_menu.grab_release()

    # 3. Bind the right-click event cross-platform
    # <Button-3> handles Windows and Linux right-clicks
    master.bind("<Button-3>", do_popup)
    # <Button-2> handles macOS right-clicks
    master.bind("<Button-2>", do_popup)
