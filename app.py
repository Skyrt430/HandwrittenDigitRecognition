import tkinter as tk

window = tk.Tk()
window.title("Digital Recognition")
window.geometry("400x520")

instructions_label = tk.Label(window, text="Draw a digit between 0 and 9", font=("Arial",16))
instructions_label.pack(pady=15)

canvas = tk.Canvas(window,width=280,height=280,background="black")
canvas.pack(pady=10)

def draw(event):
    r = 6
    x = event.x
    y = event.y
    
    canvas.create_oval(x-r,y-r,x+r,y+r, fill="white" , outline="white")
    
canvas.bind("<B1-Motion>",draw)

def clear():
    canvas.delete("all")

clear_button = tk.Button(window, text="Clear",font=("Arial",12),command=clear)
clear_button.pack(pady=5)

predict_button = tk.Button(window, text="Predict",font=("Arial",12))
predict_button.pack(pady=5)

result_label = tk.Label(window, text="Draw a digit and click Predict", font=("Arial",14))
result_label.pack(pady=10)


window.mainloop()