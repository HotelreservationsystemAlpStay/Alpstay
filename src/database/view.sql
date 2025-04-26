CREATE VIEW
    extended_hotel AS
SELECT
    Hotel.*,
    Address.*
FROM
    Hotel
    JOIN Address on Address.address_id = Hotel.address_id;


CREATE VIEW extended_hotel_room AS
SELECT
    Hotel.*,
    Address.*,
    (
        SELECT MAX(Room_Type.max_guests)
        FROM Room
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE Room.hotel_id = Hotel.hotel_id
    ) AS max_guests
FROM
    Hotel
    JOIN Address ON Address.address_id = Hotel.address_id


CREATE VIEW
    extended_room AS
SELECT
    Room.*,
    Facilities.*,
    Room_Type.*
FROM
    Room
    JOIN Room_Facilities ON Room_Facilities.room_id = Room.room_id
    JOIN Facilities on Facilities.facility_id = Room_Facilities.facility_id
    JOIN Room_Type ON Room_Type.type_id = Room.type_id;

/*Example Query for getting Rooms in Date Range*/
SELECT
    Room.*
FROM
    Room
    JOIN Booking on Booking.room_id = Room.room_id
WHERE
    Room.room_id NOT in (
        SELECT
            Booking.room_id
        FROM
            Booking
        Where
            (
                Booking.check_in_date BETWEEN '2025-06-01' AND '2025-06-05'
            )
            OR (
                Booking.check_out_date BETWEEN '2025-06-01' AND '2025-06-05'
            )
            OR (
                Booking.check_in_date <= '2025-06-01'
                AND Booking.check_out_date >= '2025-06-05'
            )
    )