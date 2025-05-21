import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import sys 

class ChartView:
    def __init__(self, data, chart_type):
        """
        Initializes the ChartView, creates a new Tkinter Toplevel window,
        and displays a chart based on the provided data and chart type.

        Args:
            data (dict): The data to be plotted. The structure depends on the chart_type.
            chart_type (str): The type of chart to display.
                              (e.g., "occupancy", "guest_country", "guest_age_histogram", "guest_booking_frequency").
        """
        self.data = data
        self.root = tk.Toplevel()
        self.root.title("Chart")
        
        # Create Figure and Axes directly
        self.figure = Figure(figsize=(6, 5), dpi=100)
        chart_axes = self.figure.add_subplot(111)

        if chart_type == "occupancy":
            self.draw_occupancy_chart(chart_axes)
        elif chart_type == "guest_country":
            self.draw_guest_country_chart(chart_axes)
        elif chart_type == "guest_age_histogram":
            self.draw_guest_age_histogram(chart_axes)
        elif chart_type == "guest_booking_frequency":
            self.draw_guest_booking_frequency_pie_chart(chart_axes)
            
        canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        canvas.draw() # Draw the canvas
        canvas.get_tk_widget().pack(fill="both", expand=True)
        
        tk.Button(self.root, text="Close", command=self.close_window).pack()
        # Handle the window's "X" button
        self.root.protocol("WM_DELETE_WINDOW", self.close_window) 
        self.root.mainloop()

    def close_window(self):
        """
        Destroys the Tkinter Toplevel window, closes the Matplotlib figure,
        and then exits the entire program.
        """
        if self.root:
            try:
                self.root.destroy()
            except tk.TclError:
                pass

        # close the Matplotlib figure to release its resources.
        if hasattr(self, 'figure') and self.figure:
            plt.close(self.figure)
        
        sys.exit()

    def draw_occupancy_chart(self, chart_axes):
        """
        Draws a bar chart for occupancy rates by room type.

        Args:
            chart_axes (matplotlib.axes.Axes): The axes object to draw the chart on.
        """
        chart_axes.bar(self.data["room_type"], self.data["count"])
        chart_axes.set_title("Occupancy Rates by Room Type")
        chart_axes.set_xlabel("Room Type")
        chart_axes.set_ylabel("Number of Bookings")
        self.figure.tight_layout()

    def draw_guest_country_chart(self, chart_axes):
        """
        Draws a bar chart for guest distribution by country.

        Args:
            chart_axes (matplotlib.axes.Axes): The axes object to draw the chart on.
        """
        chart_axes.bar(self.data["countries"], self.data["counts"])
        chart_axes.set_title("Guest Distribution by Country")
        chart_axes.set_xlabel("Country")
        chart_axes.set_ylabel("Number of Guests")
        # Apply rotation and alignment to x-axis tick labels
        for label in chart_axes.get_xticklabels():
            label.set_rotation(45)
            label.set_ha('right')
        self.figure.tight_layout() 

    def draw_guest_age_histogram(self, chart_axes):
        """
        Draws a histogram for guest age distribution.

        Args:
            chart_axes (matplotlib.axes.Axes): The axes object to draw the chart on.
        """
        chart_axes.hist(self.data["ages"], bins=self.data.get("bins", 10), edgecolor='black')
        chart_axes.set_title("Guest Age Distribution")
        chart_axes.set_xlabel("Age Range")
        chart_axes.set_ylabel("Number of Guests")
        self.figure.tight_layout() 

    def draw_guest_booking_frequency_pie_chart(self, chart_axes):
        """
        Draws a pie chart for guest booking frequency (new vs. returning).

        Args:
            chart_axes (matplotlib.axes.Axes): The axes object to draw the chart on.
        """
        chart_axes.pie(self.data["sizes"], labels=self.data["labels"], autopct='%1.1f%%', startangle=90)
        chart_axes.set_title("Guest Booking Frequency (New vs. Returning)")
        chart_axes.axis('equal')
        self.figure.tight_layout() 

if __name__ == "__main__":
    # parent for all Toplevel chart windows.
    main_tk_root = tk.Tk()
    main_tk_root.withdraw()

    # Example data for occupancy chart
    occupancy_data = {'room_type': ['Single', 'Double', 'Suite'], 'count': [10, 25, 5]}
    ChartView(occupancy_data, "occupancy")

    # Example data for guest country chart
    #country_data = {'countries': ['Switzerland', 'Germany', 'France'], 'counts': [50, 30, 20]}
    #ChartView(country_data, "guest_country")

    # Example data for guest age histogram
    #age_data = {'ages': [22, 34, 45, 23, 33, 35, 28, 50, 61, 39, 42], 'bins': 5}
    #ChartView(age_data, "guest_age_histogram")
    
    # Example data for guest booking frequency
    #booking_freq_data = {'labels': ['New Guests', 'Returning Guests'], 'sizes': [70, 30]}
    #ChartView(booking_freq_data, "guest_booking_frequency")
