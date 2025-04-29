import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class ChartView:
    def __init__(self, data, chart_type):
        self.data = data
        self.root = tk.Toplevel()
        self.root.title("Chart")
        figure, chart_axes = plt.subplots()

        if chart_type == "occupancy":
            self.draw_occupancy_chart(chart_axes)
            
        canvas = FigureCanvasTkAgg(figure, master=self.root)
        canvas.get_tk_widget().pack(fill="both", expand=True)
        tk.Button(self.root, text="Close", command=self.root.destroy).pack()
        self.root.mainloop()

    def draw_occupancy_chart(self, chart_axes):
        chart_axes.bar(self.data["room_type"], self.data["count"])
        chart_axes.set_title("Occupancy Rates by Room Type")
        chart_axes.set_xlabel("Room Type")
        chart_axes.set_ylabel("Number of Bookings")
