from data_Access.Guest_Access import Guest_Access

class Guest_Controller:
    def __init__(self):
        self.guest_access = Guest_Access()

    def get_guest_age_distribution_data(self, bins=10):
        """
        Prepares data for guest age distribution histogram.
        Expected format for ChartView: {'ages': [...], 'bins': ...}
        """
        raw_data = self.guest_access.access_guest_ages()
        if not raw_data:
            return {'ages': [], 'bins': bins}
            
        ages = [row['age'] for row in raw_data]
        return {'ages': ages, 'bins': bins}

    def get_guest_country_distribution_data(self):
        """
        Prepares data for guest distribution by country bar chart.
        Expected format for ChartView: {'countries': [...], 'counts': [...]}
        """
        raw_data = self.guest_access.access_guest_countries()
        if not raw_data:
            return {'countries': [], 'counts': []}
            
        countries = [row['country'] for row in raw_data]
        counts = [row['guest_count'] for row in raw_data]
        return {'countries': countries, 'counts': counts}

    def get_guest_booking_frequency_data(self):
        """
        Prepares data for guest booking frequency pie chart (new vs. returning).
        Expected format for ChartView: {'labels': [...], 'sizes': [...]}
        """
        frequency_stats = self.guest_access.access_guest_booking_frequency()
        labels = ['New Guests', 'Returning Guests']
        sizes = [
            frequency_stats.get('new_guests', 0), 
            frequency_stats.get('returning_guests', 0)
        ]
        
        if not any(sizes):
            return {'labels': [], 'sizes': []}
            
        return {'labels': labels, 'sizes': sizes}