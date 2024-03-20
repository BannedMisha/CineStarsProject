class Cinema:
    def __init__(self):
        # Annahme: Hier werden verschiedene Preise und Verfügbarkeiten für Sitze, Parkplätze und Snacks festgelegt
        self.seat_prices = {"Standard": 10, "VIP": 20}
        self.available_seats = {"Standard": [1, 2, 3, 4, 5], "VIP": [1, 2]}
        self.parking_prices = {"Normal": 5, "VIP": 10}
        self.snack_prices = {"Popcorn": 5, "Soda": 3, "Nachos": 7}

    def calculate_ticket_price(self, seat_type):
        return self.seat_prices.get(seat_type, 0)

    def is_seat_available(self, seat_type, seat_number):
        return seat_number in self.available_seats.get(seat_type, [])

    def calculate_parking_cost(self, parking_type):
        return self.parking_prices.get(parking_type, 0)

    def get_snack_price(self, snack_name):
        return self.snack_prices.get(snack_name, 0)


class Hall:
    def __init__(self):
        # Annahme: Hier werden Sitzplätze unterschiedlichen Typs initialisiert
        self.reserved_seats = {"Standard": [], "VIP": []}

    def reserve_seat(self, seat_type, seat_number):
        if seat_number not in self.reserved_seats.get(seat_type, []):
            self.reserved_seats[seat_type].append(seat_number)
            return True
        else:
            return False


class Service:
    def __init__(self, cinema, hall, account, app):
        self.cinema = cinema
        self.hall = hall
        self.account = account
        self.app = app

    def reserve_seat(self, customer_id, seat_type, seat_number):
        if self.cinema.is_seat_available(seat_type, seat_number):
            reservation_success = self.hall.reserve_seat(seat_type, seat_number)
            if reservation_success:
                seat_price = self.cinema.calculate_ticket_price(seat_type)
                self.account.charge_reservation(customer_id, seat_price)
                return f"{seat_type} Seat {seat_number} reserved successfully. Total cost: {seat_price}."
            else:
                return f"{seat_type} Seat {seat_number} is already reserved."
        else:
            return f"{seat_type} Seat {seat_number} is not available."

    def order_snack(self, customer_id, snack_name):
        snack_price = self.cinema.get_snack_price(snack_name)
        if snack_price:
            self.account.charge_snack_order(customer_id, snack_price)
            return f"{snack_name} ordered successfully. Total cost: {snack_price}."
        else:
            return f"{snack_name} is not available."

    def book_parking(self, customer_id, parking_type):
        parking_cost = self.cinema.calculate_parking_cost(parking_type)
        if parking_cost:
            self.account.charge_parking(customer_id, parking_cost)
            return f"Parking ({parking_type}) booked successfully. Total cost: {parking_cost}."
        else:
            return f"Parking ({parking_type}) is not available."

    def communicate_with_app(self, message):
        return self.app.send_notification(message)

# Beispiel-Nutzung:
cinema = Cinema()
hall = Hall()
account = CustomerAccount()
app = MobileApp()

service = Service(cinema, hall, account, app)

result_seat_reservation = service.reserve_seat(customer_id=123, seat_type="VIP", seat_number=1)
result_snack_order = service.order_snack(customer_id=123, snack_name="Popcorn")
result_parking_booking = service.book_parking(customer_id=123, parking_type="VIP")

app_notification = service.communicate_with_app("Enjoy your movie!")

print(result_seat_reservation)
print(result_snack_order)
print(result_parking_booking)
print(app_notification)