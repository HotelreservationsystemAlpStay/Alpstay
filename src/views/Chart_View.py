import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class ChartView:
    def __init__(self, app, data, chart_type):
        """
        Initializes the ChartView.

        Args:
            app: The main application instance.
            data (dict): The data to be plotted.
            chart_type (str): The type of chart to display.
        """
        self.app = app
        self.data = data
        self.root = tk.Toplevel()
        self.root.title("Chart")
        
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
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        
        tk.Button(self.root, text="Close", command=self._handle_close).pack()
        self.root.protocol("WM_DELETE_WINDOW", self._handle_close)

    def _handle_close(self):
        """Handles closing the window and allows wait_window to unblock."""
        self.root.destroy()

    def show_and_wait(self):
        """Displays the chart window and waits until it's closed.
           Returns the StartMenu instance to be displayed next."""
        self.root.grab_set()
        self.root.wait_window()
        from views.StartMenu import StartMenu
        return StartMenu(self.app)

    def draw_occupancy_chart(self, chart_axes):
        """
        Draws a bar chart for occupancy rates by room type.

        Args:
            chart_axes (matplotlib.axes.Axes): The axes object to draw the chart on.
        """
        if self.data and self.data.get('room_type') and self.data.get('count'):
            chart_axes.bar(self.data['room_type'], self.data['count'])
            chart_axes.set_xlabel("Room Type")
            chart_axes.set_ylabel("Booking Count")
            chart_axes.set_title("Room Occupancy by Type")
        else:
            chart_axes.text(0.5, 0.5, "No occupancy data available", ha='center', va='center')
        self.figure.tight_layout()

    def draw_guest_country_chart(self, chart_axes):
        """
        Draws a bar chart for guest distribution by country.

        Args:
            chart_axes (matplotlib.axes.Axes): The axes object to draw the chart on.
        """
        if self.data and self.data.get('countries') and self.data.get('counts'):
            chart_axes.bar(self.data['countries'], self.data['counts'])
            chart_axes.set_xlabel("Country")
            chart_axes.set_ylabel("Number of Guests")
            chart_axes.set_title("Guest Distribution by Country")
            chart_axes.tick_params(axis='x', rotation=45)
        else:
            chart_axes.text(0.5, 0.5, "No country data available", ha='center', va='center')
        self.figure.tight_layout()

    def draw_guest_age_histogram(self, chart_axes):
        """
        Draws a histogram for guest age distribution.

        Args:
            chart_axes (matplotlib.axes.Axes): The axes object to draw the chart on.
        """
        if self.data and self.data.get('ages'):
            chart_axes.hist(self.data['ages'], bins=self.data.get('bins', 10), edgecolor='black')
            chart_axes.set_xlabel("Age")
            chart_axes.set_ylabel("Number of Guests")
            chart_axes.set_title("Guest Age Distribution")
        else:
            chart_axes.text(0.5, 0.5, "No age data available", ha='center', va='center')
        self.figure.tight_layout()

    def draw_guest_booking_frequency_pie_chart(self, chart_axes):
        """
        Draws a pie chart for guest booking frequency (new vs. returning).

        Args:
            chart_axes (matplotlib.axes.Axes): The axes object to draw the chart on.
        """
        if self.data and self.data.get('labels') and self.data.get('sizes') and any(self.data['sizes']):
            chart_axes.pie(self.data['sizes'], labels=self.data['labels'], autopct='%1.1f%%', startangle=90)
            chart_axes.axis('equal')
            chart_axes.set_title("Guest Booking Frequency (New vs. Returning)")
        else:
            chart_axes.text(0.5, 0.5, "No booking frequency data available", ha='center', va='center')
        self.figure.tight_layout()

if __name__ == "__main__":
    class MockApp:
        def __init__(self):
            self.roomType_Controller = None
            from views.StartMenu import StartMenu
            self.StartMenu = StartMenu

    main_tk_root = tk.Tk()
    main_tk_root.withdraw()

    mock_app_instance = MockApp()

    occupancy_data = {'room_type': ['Single', 'Double', 'Suite'], 'count': [10, 25, 5]}
    ChartView(mock_app_instance, occupancy_data, "occupancy")

    main_tk_root.mainloop()
