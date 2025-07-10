import tkinter as tk

def show_popup(url):
    root = tk.Tk()
    root.attributes("-fullscreen", True)# stuff like this will probably be in some config file too
    root.configure(bg =  "black")

    
    label = tk.Label(root, text=f"You are on a distracting site:\n{url}\n\nClick below if you want to keep going.", fg="white", bg="black", font=("Helvetica", 24))
    label.pack(expand=True)


    def on_continue():
        
        root.destroy()

    button = tk.Button(root, text = "Keep going",  command=on_continue, font=("Helvetica", 20))
    button.pack(pady=20)

    root.mainloop()


