# Alpstay

This project results from the python module "Anwendungsentwicklung mit Python" from the FHNW. 
The goal is to create a hotel reservation system, which uses a partially given mysql database. In several iterations, we work on user stories and try to implement them on the bases of the newly learned concepts.

## Organization

### Decision Github
This project could have been realized as a jupiter notebook. A jupiter notebook like DeepNote is great for using code in a documentation. It doesn't require a local installation of Python and the Libraries are provided automatically. However, we have decided to create a console application due to the fact, that we wanted to see, how the application as a whole will work. This provides a better understanding for software and the work within a team.

When working with a team, versioning is an essential part of working together. The best-known tool for this is any kind of git. Due to prior knowledge, the benefit of Github Pro as a student and recommendation of the coaches, we decided to use Github as our versioning tool. 

### Kanban Board
To track progress and tasks as a team, a kanban board is a very easy choice would be the Microsoft Planner. However, with Github Projects, the kanban board with tasks, bugs and issues is directly integrated in the project. The wide variety of standard, built-in features as types, milestones and great filtering, Github Projects is perfect to use in a small team as ours. 

Our Kanban Board: [GitHub Project Board](https://github.com/orgs/HotelreservationsystemAlpStay/projects/1/views/2)

### Time Planning
Additionally, the time planning is easy to use with Github projects. Creating a tasks provides the ability to add it on a timeline.

### Communication
Communicating with each other can be quite hard, especially, when the team members can't see eachother often. Therefore, we communicated using Teams or WhatsApp. We tried to come together 1-2 times per week at the FHNW.

### Code Documentation
Documentation of the code happens in the code itself using docstrings as well as in the ReadMe. The ReadMe contains all user stories, in which concepts, structures and interesting decisions and findings are held. The docstrings contain information about how to use certain classes and methods.

### GitHub Projects
Project planning and task management for Alpstay were handled via GitHub Projects. This allowed for transparent progress tracking and clear assignment of responsibilities within the team.

The project board was divided into various status categories to map the workflow:
*   **OnHold:** Tasks that were temporarily paused (currently 6 tasks).
*   **Backlog:** Planned tasks that have not yet been started (currently 2 out of 5 tasks in the visible scope).
*   **Ready (DOR - Definition of Ready):** Tasks ready for processing.
*   **In Progress:** Tasks actively being worked on (currently 1 out of 3 tasks in the visible scope).
*   **In Review:** Tasks awaiting review.
*   **Done:** Successfully completed tasks (currently 65 tasks).

Some of the central tasks processed included:
*   **Database User Stories:** Implementation of specific requirements for database interaction.
*   **Manager Setup:** Establishment of the manager layer to separate business logic from the presentation layer.
*   **App Implementation:** Development of the main application logic.
*   **Optional User Stories:** Implementation of additional functionalities such as email dispatch.
*   **Error Handling:** Implementation of robust error handling mechanisms.

This structured approach helped to design the development efficiently and to systematically process the various user stories.

## Structure
The Software is built up on 5 Layers. 

### Model
All Tables from the database are created as models in the python code. The connection between the classes is one-directional, due to the database being one-directional. Additionally, we arent using stark concepts to be needing bi-directional connections.

### Data Access Layer
The first layer is called the data access layer and has two types of classes. The Base_Access_Controller provides direct access to the underlying SQLITE-Database.
Using this Base_Access_Controller, for each model exists a data_access class. With said class, data can either be extracted from the db or be inserted or deleted based on the objects and their properties. 

### Business Logic
The Business Logic Layer encapsulates the core functionality of the application. For each model, there is a corresponding logic class that interacts with the respective data_access class from the DAL.
This layer is responsible for all validation, processing rules, and decision-making logic. By separating the business logic from the data access and user interface layers, the code remains modular, maintainable, and scalable.


### View / GUI
The GUI is implemented as a console-based menu system. It serves as the interface between the user and the application logic.
User inputs are collected, processed, and forwarded to the appropriate methods in the Business Logic Layer. Output from the logic is then displayed in a user-friendly format.
The GUI does not directly access the database; instead, it relies entirely on the Business Logic Layer to handle data operations, ensuring a clean separation of concerns.

### Utils
The Utils layer provides cross-cutting utility functions used throughout the application. It contains helper classes with static methods for validation and formatting operations. Formatting.py is responsible for date formatting and conversion, while Validator.py handles input validation across all application layers.

## Class Diagram
!!Bild muss hier noch eingefügt werden!!
Each table in our Class Diagram represents a table from the sqlite file. For each table there is a model file in our models folder where an object of a class can be created. All classed contains their attributes, each one starts with _ because we also used them to create "private" attributes in python. We know that they are not private with _, to be clear they are not even being name mangled but, its a convention, which should be enough for our use cases. Each attribute is marked with - because we consider them to be "private". 

### Connections between classes:
- Booking – Invoice: We use a basic association because an invoice contains a booking_id. We modelled it as a 1:n relation, since – as mentioned later in the corresponding user story – a booking can have multiple invoices (for example if something changes or is corrected later). An invoice, however, always belongs to exactly one booking.
- Booking – Rating: We use a basic association because a rating contains a booking_id. We modelled it as a 1-to-(0..1) relationship: each rating belongs to exactly one booking, but not every booking has to be rated — so it can have zero or one rating. As defined later, a rating can only be created for an existing booking, which prevents fake ratings. Also, it's not possible to submit more than one rating per booking, making the system fair and controlled.
- Booking - Room: This is a basic association since a booking stores the room_id. We modelled it as an n:1 relationship — each booking must be linked to exactly one room, which was also defined in the project description. On the other hand, a room can of course be booked multiple times, so it can have many bookings or not even one booking.
- Booking – Guest: This is a basic association, since a booking contains the guest_id. We use an n:1 relationship — every booking belongs to exactly one guest, while a guest can have zero or multiple bookings. We intentionally decided against allowing multiple guests per booking, as this would make it unclear who the main booker is. If a guest brings others, they can be recorded at check-in instead.
- Address - Guest: We used an aggregation because the address is conceptually a part of the guest, but both can exist independently — for example, an address can exist in the database without being linked to a guest yet, and a guest can be created before assigning them an address. The association is implemented via address_id in the Guest class. We modeled it as a 1:n relationship: one address can belong to multiple guests (e.g. people living in the same household), while each guest has exactly one address.
- Address - Hotel: As with the Guest relationship, we used aggregation here as well. An address is conceptually a part of the hotel, but both entities can exist independently — for example, an address can already exist before a hotel is assigned to it, and a hotel object can be created before linking it to an address. The connection is made via address_id in the Hotel class. We modeled this as a 1:n relationship: one address can be shared by multiple hotels (e.g. multiple hotels in one building), but each hotel has exactly one address.
- Guest - User: We used a basic association since the User class contains a guest_id. The relationship is 1:1 because each guest must have exactly one user login, and each user login must be linked to exactly one guest account. This applies even for admin users — they also need a guest account in our logic to keep the structure consistent and simplify access control. 
- Rating - Hotel: We used a basic association since the Rating contains a hotel_id. It's a n:1 relationship, because each rating must be linked to exactly one hotel, while a hotel can have zero, one or many ratings — depending on how many guests decide to leave feedback.
- Hotel - Room: We modelled this as a composition, since a room cannot exist without a hotel — it only makes sense in the context of one. The Room class also contains the hotel_id. It's a 1:n relationship, because a hotel can have none, one or many rooms, but each room always belongs to exactly one hotel.
- Facility - Room: This is a standard association, since the Room class holds a list of facilities. We used a many-to-many (n:n) relationship because a room can offer multiple facilities (like TV, minibar etc.), and the same facility (e.g. WiFi) can be available in many rooms.
- Room - Room Type: This is an association, since each room references a room type. We modelled it as an n:1 relationship because each room must have exactly one room type (e.g., Single, Double, Suite), while a room type can be assigned to none, one, or many rooms.

## How to run the application
To run the Alpstay hotel reservation system, follow these steps:

1.  **Prerequisites:**
    *   Ensure you have Python installed on your system (preferably Python 3.12 or newer).
    *   Make sure you have `pip` (Python package installer) available.

2.  **Install Dependencies:**
    Navigate to the `src` directory and install the required Python packages using the `requirements.txt` file:
    ```bash
    cd src
    pip install -r requirements.txt
    ```

3.  **Database Setup:**
    The application uses an SQLite database. The `sqlite.db` file is located in the `src/database/` directory.
    *   The initial database schema and some sample data can be found in `db.sql` or `sqlite_.sql`.
    *   When the application runs for the first time, it should connect to the existing `sqlite.db`. No special setup is usually required if the file is present.

4.  **Run the Application:**
    From the `src` directory, execute the `App.py` script:
    ```bash
    python App.py
    ```
    This will start the console-based menu system.

5.  **Using the Application:**
    *   The application will present you with a main menu and subsequent sub-menus for different user stories and functionalities.
    *   Navigate through the menus by entering the number corresponding to your choice and pressing Enter.
    *   Follow the on-screen prompts to input required information (e.g., city names, dates, hotel IDs).
    *   **Input Validation:** The system performs input validation. If you enter invalid data (e.g., text where a number is expected, or an invalid date format), you will usually receive an error message and be prompted to try again. Pay attention to the expected input formats.
    *   **Admin Functions:** Some functionalities require admin privileges. You will be prompted to log in as an admin.
    *   **Guest Functions:** Other functionalities may require you to log in as a guest or will ask for guest-specific information.

6.  **Test Users:**

    You can use the following credentials for testing (every password is hashed in the DB):
    *   **Admin User:**
        *   User ID: `6`
        *   Password: `admin`
    *   **Guest User:**
        *   User ID: `1`
        *   Password: `fciwke-peOlme-8rutjj`

7. **Things you can write as input**

    Here are practical examples of inputs you can use when testing different user stories:
    *   **Cities:** `Zürich`, `Luzern`, `Bern`, `Basel`
    *   **Hotel names:** `Hotel Baur au Lac`, `Four Seasons Hôtel des Bergues`, `Grand Hotel National`, `Bellevue Palace`, `Les Trois Rois`
    *   **Star ratings:** `3`to`5`
    *   **Number of guests:** `1` to `6` (depending on room type: Single=1, Double=2, Suite=4, Family Room=5, Penthouse=6)
    *   **Dates:** Use any format e.g., `01.08.2025` to `13.08.2025` for future bookings
    *   **Room IDs:** `1` to `5` (for booking specific rooms)
    *   **Booking IDs:** `1` to `5` (for invoice generation, cancellation, or rating)
    *   **Hotel IDs:** `1` to `5` 
    *   **Address IDs:** `1` to `5` (for admin hotel management)
    *   **Rating scores:** `1` to `5` (for hotel ratings)
    *   **Phone numbers:** Numbers only (no formatting characters) like `41123456789` or `123456789`
    *   **Room Type descriptions:** `Single`, `Double`, `Suite`, `Family Room`, `Penthouse`
    *   **Facility names:** `WiFi`, `TV`, `Air Conditioning`, `Mini Bar`, `Balcony`
    *   **Email addresses:** Any valid format like `test@example.com` for booking confirmations

8.  **Exiting the Application:**
    Most menus will have a "back" or "exit" option to navigate to the previous menu or close the application.

**Important Notes:**
*   The application is console-based, so all interactions happen in your terminal or command prompt.
*   If you encounter errors that are not handled by a `try-except` block (which should be rare for user input validation), the application might terminate. In such cases, you can restart it by running `python App.py` again.
*   For data visualization features (User Stories DV1, DV2, DV3), new windows will pop up to display the charts. Ensure your environment allows GUI windows to be created by Python (this usually works with standard Python installations that include Tkinter).

## Userstories
The original user stories were written in german is it is a german-based course. Due to the majority of code being developed in english, the documentation is in english. The description of the user stories are in english aswell as in german. Additionally, for the spirit of the documentation, the user stories are seperated or combined.

## Minimale User Stories

### 1. As a guest, I want to search for a hotel in a city, so that i can choose the one, that meets my criteria:
Als Gast möchte ich die verfügbaren Hotels durchsuchen, damit ich dasjenige auswählen kann, welches meinen Wünschen entspricht

This user story was not implemented directly, as it does not contain any specific input or interaction. We interpreted it as a general template that serves as a basis for the following, more detailed sub-stories that reflect the actual functionality.

### 1.1. Criteria 1: City
Ich möchte alle Hotels in einer Stadt durchsuchen, damit ich das Hotel nach meinem bevorzugten Standort (Stadt) auswählen kann.

First, the user is asked for the city in which they would like to search for hotels. This input is then passed to the controller/business logic, which checks whether the city is a valid string and then calls the data access layer. In the data access layer, a SQL statement selects all hotels in the specified city. For each hotel found, a hotel object is created and added to a list. This list is then returned to the controller/business logic, which again returns it to the GUI. In the GUI, all hotels from the list are printed out using a for loop that iterates through each hotel object. If no hotel is found, a matching print statement is shown.

### 1.2. Criteria 2: Stars
Ich möchte alle Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen.

First, the user is asked for the city in which they are looking for a hotel and how many stars the hotel should at least have. This input is passed to the controller/business logic, which checks whether the city is a valid string and whether the stars input is valid. It then calls the data access layer, where a SQL statement selects all hotels in that city with at least the specified number of stars. For each result, a hotel object is created and added to a list. This list is returned to the controller/business logic and then passed to the GUI, where all matching hotels are printed in a for loop. If no hotel matches the filter, a matching print statement is shown.

We didn’t reuse the method from Story 1.1 because it made more sense to filter directly in the SQL query. That way, we don’t load unnecessary data and it just works more efficiently.

### 1.3. Criteria 3: Amount of guests in a room
Ich möchte alle Hotels in einer Stadt durchsuchen, die Zimmer haben, die meiner Gästezahl entsprechen (nur 1 Zimmer pro Buchung).

The user is first asked for the city, the minimum number of stars, and how many guests should at least fit into the room. This input is passed to the controller/business logic, which validates all fields and then calls the data access layer. There, a SQL query selects all hotels in the given city with at least the specified star rating and room capacity. For each result, a hotel object is created and added to a list. This list is returned to the controller/business logic and then to the GUI, where the results are printed using a for loop. If no matching hotels are found, a matching print message is shown.

As mentioned in 1.2, we didn’t reuse the previous DAL or BL methods, since each method is built for a specific filter combination. Reusing them would’ve made the logic messy and less efficient, so we kept each case clean and separate.

### 1.4. Criteria 4: Availability (Room in a hotel is available between start date and end date)
Ich möchte alle Hotels in einer Stadt durchsuchen, die während meines Aufenthaltes ("von" (check_in_date) und "bis" (check_out_date)) Zimmer zur Verfügung haben, damit ich nur relevante Ergebnisse sehe.

The user is asked to enter the city, minimum number of stars, number of guests, and a check-in and check-out date. These inputs are passed to the controller/business logic, where all fields are validated. The business logic then calls the data access layer, where a SQL query checks for hotels in the specified city that meet all criteria and have available rooms in the given date range. Bookings that have been cancelled are not considered. For each result, a hotel object is created and added to a list. This list is passed back through the controller to the GUI, where all matching hotels are printed in a for loop. If no hotels match the filters, a fitting message is shown.

Although the original user story only required filtering by city and dates, we also included filters for minimum stars and guests. This made the logic more consistent. If a user only wants to search by city and date, this can be done via User Story 1.5.

As mentioned before, we didn’t reuse the previous methods because date availability requires a completely different SQL logic. Combining all filters in one query keeps the implementation clean and avoids unnecessary complexity.

### 1.5. Criteria 5: Combine the upper four criteria
Ich möchte Wünsche kombinieren können, z.B. die verfügbaren Zimmer zusammen mit meiner Gästezahl und der mindest Anzahl Sterne.

The user is asked to enter any combination of filters: city, minimum stars, number of guests, check-in date, and check-out date. Each input is optional, but check-in and check-out must be provided together if used. However at least one information must be provided, otherwise there would be no need for this function. The controller/business logic validates the inputs and ensures that at least one filter is given. It then calls the data access layer, where a dynamic SQL query is built based on the selected filters. Cancelled bookings are not considered. For each result, a hotel object is created and added to a list, which is then returned through the controller to the GUI and printed in a for loop. If no hotels match the filters, a matching message is shown.

As with the previous stories, we chose not to reuse earlier methods, since the logic here is dynamic and would have become too messy with chained or nested calls. Keeping this functionality in a dedicated method made the implementation much clearer and easier to maintain, in this case it is even more important to do this, because there is much logic behind creating the SQLite statement, basend on the inputs.

### 1.6. Criteria 6: The following Information should be displayed: Hotel name, hotel address, amount of stars
Ich möchte die folgenden Informationen pro Hotel sehen: Name, Adresse, Anzahl der Sterne.

The user is asked to enter the name of a hotel they want to know more about. This input is passed to the controller/business logic, which calls the data access layer. There, a SQL query selects all matching hotels by name and returns the corresponding hotel object along with the street and city information. The data is then returned through the controller to the GUI, where the hotel details (name, stars, city, and street) are printed. If no matching hotel is found, a fitting message is shown.

We kept this logic separate from the previous stories, as it focuses on displaying detailed information for one specific hotel rather than searching based on filters.

We decided to not perform a fetchone query in this case, because there could be multiple hotels with the same name, in this case all hotels are shown and the user can see the differences in the street, which usually in combination with the city is unique. 

### 2. As a guest, I want to see the details of different room types, which are available in a hotel, including the following information for this room: maximum amount of guests, description, price and facilities
Als Gast möchte ich Details zu verschiedenen Zimmertypen (Single, Double, Suite usw.), die in einem Hotel verfügbar sind, sehen, einschliesslich der maximalen Anzahl von Gästen für dieses Zimmer, Beschreibung, Preis und Ausstattung, um eine fundierte Entscheidung zu treffen.

This userstory does not provide a correct requirement due to using different terms to describe, what is needed:
>I want to see the details of different room types [...] including the following information: [...] description, price and facilities.<br>

A room type has the following attributes: 
room_type_id: INT(10)
description: VARCHAR(255)
max_guests: INT(10)
The connection from room type to facilities is over the room itself. Therefore are not available RoomTypes displayed, rather are the rooms itself displayed. 

My function to get the user input has the possiblity to come from antoher function with the requirement of check-in and check-out dates being mandatory. With a simple if-while check, this additional requirement has been added. The rest of the code is a simple getter of hotel and its rooms and a custom print method.

The Room Access, which directly corresponds with the data access creates the filter dynamically based on the arguments. The biggest, most important and trickiest part of creating such a filter is the query to get rooms, which do not have a booking in the provided time slot. The query in its form after editing the values out looks like this.
```
SELECT DISTINCT extended_room.* 
from extended_room 
JOIN Booking ON Booking.room_id = extended_room.room_id
WHERE
Booking.room_id not IN (
    SELECT extended_room.room_id from extended_room 
        JOIN Booking ON Booking.room_id = extended_room.room_id 
        WHERE ( 
            (Booking.check_in_date BETWEEN ? AND ?) OR 
            (Booking.check_out_date BETWEEN ? AND ?) OR 
            (Booking.check_in_date <= ? AND Booking.check_out_date >= ?) 
        ) 
    )
AND
extended_room.hotel_id in (,)
AND
extended_room.type_id = ?
```
The `NOT IN` before the second select statement provides the possibility to only show rooms, that are not in the timerange. Additionally with `DISTINCT`, the record shows only once. Before the `DISTINCT` was in the query, we had the problem that certain rooms were twice in the results or even worse a reserved room did appear in the list.

This user story 2 directly covers user sotry 2.1 and 2.2. 

### 2.1. As a guest, I want to see the following information for each room: room type, maximum amount of guest, description, facilities, price per night and total price
Ich möchte die folgenden Informationen pro Zimmer sehen: Zimmertyp, max. Anzahl der Gäste, Beschreibung, Ausstattung, Preis pro Nacht und Gesamtpreis.

This user story is covered by the description and implementation of User Story 2.

### 2.2 As a guest, I only want to see available rooms if I have specified the dates of my stay
Ich möchte nur die verfügbaren Zimmer sehen, sofern ich meinen Aufenthalt (von – bis) spezifiziert habe.

This user story is covered by the description and implementation of User Story 2.

### 3. As an admin, I want to have the possibility to update information about hotels
Als Admin des Buchungssystems möchte ich die Möglichkeit haben, Hotelinformationen zu pflegen, um aktuelle Informationen im System zu haben.

This user story serves as a general requirement for managing hotel information by an admin. The specific functionalities like adding, deleting, and updating hotels are detailed in sub-stories 3.1, 3.2, and 3.3, which describe the console interactions and backend processes for each operation.

### 3.1. As an admin, I want to add new hotels to the system
Ich möchte neue Hotels zum System hinzufügen

The user is first asked to log in as admin. If successful, they enter the hotel’s name, number of stars, and address ID. These inputs are passed to the controller/business logic and then to the data access layer. There, a new hotel is added to the database. We don't set the hotel ID manually – instead, SQLite handles it automatically with Autoincrement. If everything works, a success message is shown. If not, an error message appears - however this should almost never be the case unless the db is not responding. 

### 3.2. As an admin, I want to delete hotels from the system
Ich möchte Hotels aus dem System entfernen

Again, the user has to authenticate as admin. After that, they enter the hotel ID they want to delete. The controller passes that to the data access layer, where a delete command is executed. If a hotel with that ID exists, it’s removed and a success message is shown. If no hotel with that ID is found, the user gets a message telling them so.

We kept the logic simple: if no row was deleted, we just assume the hotel doens't exist.

### 3.3. As an admin, I want to update information of hotel
Ich möchte die Information bestimmter Hotel aktualisieren, z.B. den Namen, die Sterne usw.

After admin login, the user is asked to enter the hotel ID and then optionally a new name, number of stars, or address ID. They can leave fields empty if they don’t want to change them. However at least one value must be changed, otherwise there would be no logic in calling this function. These values are passed on to the controller and then to the data access layer. There, an update statement is built depending on which fields were filled in. If at least one hotel was updated, a success message is shown. If not, the hotel probably didn’t exist.

We made the update flexible, so that only the changed fields are updated. That keeps it clean and avoids overwriting stuff unnecessarily.

### 4. As a guest, I want to book a room in a certain hotel
Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen

This userstory uses user story 2.2 to get the needed information about the hotel and rooms on the provided dates. After a logn, the booking manager creates a new entry vie the data access and returns a ned booking object, which gives confirmation, that everython worked.

### 5. As a guest, I want to receive an invoice after my stay
Als Gast möchte ich nach meinem Aufenthalt eine REchnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der Invoice Tabelle hinzu

The user is asked to enter a booking ID. This ID is passed to the controller, which calls a method to fetch the booking details from the data access layer. There, a SQL query pulls all relevant info from a view that includes booking data, guest name, and hotel information. If the booking is cancelled, no invoice is created and a matching message is shown.

If the booking is active / not cancelled, the current date is set as the invoice issue date, and a new invoice is inserted into the database. The controller then returns all necessary objects back to the GUI, where the full invoice is printed out – including guest name, hotel info, dates, total amount and more.

We made it possible to create multiple invoices for the same booking on purpose. This way, if something changes later (e.g. a correction or customer request), a new invoice can be generated easily without overwriting anything.

We also extended this story a bit, you can now add your e-mail, where you'd like to receive the confirmation. This was realised with an api, we transfer some variables to the webhook on make.com where a html mail is sent to the e-mail

### 6. As a guest, I want to be able to cancel my booking
Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hint: Sorgt für die entsprechende Invoice. 

To cancel a booking, the guest first needs to log in. They are then prompted to enter the ID of the booking they wish to cancel. The `Booking_Manager` validates the ID and checks if the booking can be cancelled (e.g., it's not in the past or already cancelled). If valid, the `Booking_Access` layer updates the booking's status to 'cancelled' in the database. The system also considers implications for invoices, potentially marking an existing invoice as void or generating a cancellation confirmation, as hinted in the user story. A success or failure message is then displayed to the guest via the console GUI.

### 7. As a guest, I want to have dynamics prices to profit from dynamic pricing
Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann. Hint: Wendet in der Hochsaison höhere und in der Nebensaison niedrigere Tarife an.

The user is first asked to enter the city, check-in date, and check-out date. This info is passed to the controller, where the dates are parsed and sent to the data access layer. There, we check for all rooms in the given city that aren’t already booked during that period (cancelled bookings don’t count). The query also joins the hotel and room type, so we can show more than just room IDs.

In the business logic, we go through each room and create a Room object. Then we check how many nights fall into high season (May to September) and how many don’t. Based on that, we calculate the total price with a 20% increase for high season and 20% discount for off-season. We also calculate the average price per night. All of this is then returned to the GUI, where we show the user a detailed overview.

We wanted to make pricing as clear as possible, so users know exactly what they’re paying for – not just the total, but how it’s made up.

However, we decided not to use this pricing logic in all bookings and searches for now, because in reality each hotel would probably want to set their own surcharges - mountain hotels have high season in winter, city hotels in summer - so a fixed rule wouldn’t really make sense everywhere...

### 8. As an admin, I want to see all bookings
Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.

Admins, after successful authentication, can access a menu option to view all bookings. This triggers the `Booking_Manager` to fetch all booking records via the `Booking_Access` layer from the database. The console GUI then displays a list of these bookings, showing key details for each (e.g., Booking ID, Guest Name, Hotel Name, Check-in/Check-out Dates, Status). This comprehensive overview is essential for administrative tasks and monitoring, and as mentioned in "User Stories mit DB-Schemaänderung 1", it can be a prerequisite for other operations like updating booking details.

### 9. As an admin, I want to see all rooms with their facilities
Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.

For an admin to view all rooms and their facilities, they first log in and select the relevant option from the admin menu in the console application. The `Room_Manager`, potentially in conjunction with `Facility_Manager` (or through queries in `Room_Access` that join facility data), retrieves all room details and their associated facilities. The console GUI then presents this information, typically listing each room with its properties (e.g., room ID, hotel, type, capacity) and a sub-list of its facilities. This allows admins to have a clear inventory for management and promotional purposes.

### 10. As an admin, I want to be capable to update master data (RoomTypes, Facilities, Prices)
Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat. Hint: Stammdaten sind alle Daten, die nicht von anderen Daten abhängen.

To update master data, I want to see, what I am going to change. Additionally, the user story explicitly says, that only admins should be able to change the master data. As another requirement from a user expirience stand-point, the user may decides to not update something due to seeing, that the information is already correct. Therefore instances of menus were created.

To access the main application, the user has to be authenticated and asked, which type of master data wants to be updated. Based on this choice, the specified menu is called. The parameters for these instances are the application and the menu at the moment. With the menu as parameter, the user is able to choose the option back and return to this menu.

For all menus, the options are pretty similar:

1. Get information
2. Update information
3. back

## User Stories mit DB-Schemaänderung

### 1. As and admin, I want to update missing information in bookings
Als Admin möchte ich alle Buchungen bearbeiten können, um fehlende Informationen zu ergänzen (z.B. Telefonnummer). 

Through using user story 8, all bookings were gathered and used to display. the admin can choose a booking and alter the telefon number of the booking.

### 2. As a guest, I want to see my booking history
Als Gast möchte ich auf meine Buchungshistorie zuzugreifen ("lesen"), damit ich meine kommenden Reservierungen verwalten kann.

This was not created as an own user story - as there would be no use case for this without the logic of the following story.

### 2.1. For all bookings, I should be able to use the following action "create", "update", "cancel".
Die Anwendungsfälle für meine Buchungen sind "neu/erstellen", "ändern/aktualisieren", "stornieren/löschen".

We only created the usa case for creating a booking as change / update can't really do much instead of cancelling the booking and there already is a story for cancelling a booking - so we dont know what the point of doing this again would be :D.

The user first selects a hotel and is then asked to enter the desired check-in and check-out date. These dates are passed to the controller, where they are parsed and validated. The controller then calls the business logic to get all available rooms for that hotel in the selected time range. Rooms that are already booked (except cancelled ones) are filtered out via SQL. The result includes detailed information like room type, price per night, and max guests. Based on the number of nights, we also calculate the total amount directly.

All rooms are printed out clearly for the user. After a short wait, the user is asked to enter the Room ID of the room they want to book. The selected room and amount are validated again. Then, the user is asked to log in as a guest. Once logged in, the system fetches the guest ID linked to the user and uses all the gathered data to create a new booking.

The controller validates all key fields again (IDs, dates, total amount) and then calls the DAL, where a new row is inserted into the Booking table. The new booking ID is retrieved using lastrowid, and a Booking object is returned. The GUI then prints a confirmation message including the new booking ID.

### 3. As a guest, I want to create a rating about the stay at a hotel
Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.

The user is first asked to log in as a guest. If the login is successful, we get the guest ID and then retrieve all bookings connected to that guest. These are printed out so the user can choose the correct booking ID for which they want to leave a rating.

To avoid misuse, we check if the selected booking actually belongs to the logged-in guest. If that’s the case, the user is asked to enter a score between 1 and 5, and optionally a written review. Before creating the rating, we check if a rating for this booking already exists. If not, the rating is created and saved to the database.

For this feature, we added a separate Rating table with the following fields:

- rating_id: Primary key

- booking_id: Foreign key (linked to the booking, so each rating belongs to one stay)

- hotel_id: Foreign key (linked to the hotel that was rated)

- score: Integer from 1 to 5

- review: Free text, optional

- created_at: Date the rating was submitted – so users and admins can see when it was written

We decided to structure it this way to make sure ratings are tied to real bookings only and can’t be spammed. Also, limiting one rating per booking keeps things clean and traceable.

### 4. As a guest, I want to read ratings before I book
Als Gast möchte ich vor der Buchung Hotelbewertungen lesen, damit ich das beste Hotel auswählen kann.

When a guest is browsing hotels (e.g., after a search in User Story 1.x), they can choose to view ratings for a specific hotel through the `Rating_Manager`, which fetches all ratings associated with that hotel ID from the `Rating_Access` layer. These ratings, including scores and review texts, are then displayed in the console GUI. This allows guests to make more informed decisions based on the experiences of previous guests. This feature utilizes the `Rating` table schema from DB User Story 3.

## User Stories with data visualization

### As an admin, I want to see the occupancy rate for each room type
Als Admin möchte ich die Belegungsraten für jeden Zimmertyp in meinem Hotel sehen, damit ich weiss, welche Zimmer am beliebtesten sind und ich meine Buchungsstrategien optimieren kann. Hint: Wählt ein geeignetes Diagramm, um die Auslastung nach Zimmertyp darzustellen (z. B. wie oft jeder Zimmertyp gebucht wird).

After an admin logs in, they can access a feature to visualize room type occupancy. The `Booking_Manager` (using `Booking_Access`) typically retrieves booking data, which is then aggregated by room type with the help of `Room_Type_Manager` (using `Room_Type_Access`) or by joining room data in `Room_Access`. The `src/views/Chart_View.py` module, specifically its `draw_occupancy_chart` method, then generates a bar chart. Each bar in this chart represents a room type (e.g., "Single", "Double", "Suite"), and the height of the bar corresponds to the total number of times that room type has been booked. This visualization provides a clear overview of which room types are most popular, enabling admins to make informed decisions about pricing, inventory management, and marketing strategies.

### As an admin, I want to analyze my guests based on demografic attributes
Als Admin möchte ich eine Aufschlüsselung der demografischen Merkmale meiner Gäste sehen, damit ich gezieltes Marketing planen kann. Hint: Wählt ein geeignetes Diagramm, um die Verteilung der Gäste nach verschiedenen Merkmalen darzustellen (z. B. Altersspanne, Nationalität, wiederkehrende Gäste). Möglicherweise müssen Sie der Tabelle „Gäste“ einige Spalten hinzufügen.

This feature provides admins with insights into their guest demographics through several visualizations, all generated by `src/views/Chart_View.py` after admin authentication. The `Guest_Manager` is responsible for fetching and preparing the necessary data from his respective access layers `Guest_Access`. The system offers the following demographic charts:
1.  **Guest Distribution by Country (`draw_guest_country_chart`):** This bar chart displays the number of guests originating from different countries. The country data is derived from the `Guest_Access`. This helps in identifying key geographic markets and tailoring marketing efforts accordingly.
2.  **Guest Age Distribution (`draw_guest_age_histogram`):** A histogram is used to show the distribution of guest ages. This requires age data to be available for guests. Understanding the age demographics allows the hotel to customize amenities and services.
3.  **Guest Booking Frequency (`draw_guest_booking_frequency_pie_chart`):** This pie chart visualizes the proportion of new guests versus returning guests. The `Guest_Access` module's `access_guest_booking_frequency` method directly analyzes the `Booking` table to categorize guests: those with a single booking are counted as 'New Guests', and those with more than one booking are counted as 'Returning Guests'. The data is then prepared by `Guest_Manager` for visualization. This chart is crucial for evaluating guest loyalty and the effectiveness of customer retention strategies.
These visualizations empower admins to better understand their customer base, enabling more effective targeted marketing, personalized service offerings, and strategic business planning.

## Optional user stories

### 1. As an admin, I want to see the total revenue of my hotel so that I can analyze the financial performance of the hotel.
Als Admin möchte ich die Gesamteinnahmen meines Hotels sehen, damit ich die finanzielle Leistung des Hotels analysieren kann.
1.1. Zeigt die Gesamteinnahmen (Revenue) an, die sich aus allen Buchungen für einen bestimmten Zeitraum ergeben.
1.2. Eine zeitliche Aufschlüsselung (z. B. Umsatz nach Monat, Quartal, Jahr) bereitstellen.
Hint: Füge eine Trendlinie ein, um zu veranschaulichen, wie sich die Einnahmen im Laufe der Zeit verändern.

The implementation of this user story is partially addressed in the project by the `draw_total_revenue_per_hotel_chart` method in `src/views/Chart_View.py`. This method visualizes the total revenue per hotel as a bar chart. The data for this is typically prepared by the `Hotel_Manager`. The `Hotel_Access.amount_per_hotel` method queries the `booking_view` to sum the `total_amount` for each hotel.
The specific requirements of sub-point 1.1 (revenue for a specific period) and 1.2 (temporal breakdown with trend line) are not yet explicitly implemented in the current visualization. These would require enhancements to filter data by time periods and implement more complex time-series charts.

### 4. As a guest user, I want to book a room and receive a booking confirmation with all details via email to have binding proof of my reservation.
Als Gastnutzer möchte ich ein Zimmer buchen und eine
Buchungsbestätigung mit allen Details per E-Mail erhalten, um
einen verbindlichen Nachweis meiner Reservierung zu haben.
Hint: Verwende die Python-Bibliothek «smtplib» oder eine
ähnliche.

This functionality has already been implemented and documented as part of User Story 5 of the 'Minimal User Stories' ("As a guest, I want to receive an invoice after my stay"): *"We also extended this story a bit, you can now add your e-mail, where you'd like to receive the confirmation. This was realised with an api, we transfer some variables to the webhook on make.com where a html mail is sent to the e-mail"*.
When a guest completes a booking or an invoice is generated, the system can send a confirmation via email. This is done by capturing the guest's email address and using an external API (webhook on make.com) to send an HTML email with the relevant booking or invoice details.

## OOP / concepts from OOP
The whole application runs on generating and writing model objects from and to the database. Withing the layers of the application, objects are used to carry and alter information. To effectivly use objects, the main instance of the class `application` holds all managers and therefore handles all managers in one place. This one instance of an application and the one instances of the managers provide to ability to not have too much usage of power and handling everything in one place.

On start of the application, a starting menu will be instanced. All menus inheret from the class `menu`. This class has basic functions as run, input, display and add item. With `run()`, the menu will be displayed and uses the function `display()` to display all available options in the menu. These options have to be defined in the __init__-function with the method `add_item(name, function)`. In this case, name is the displayed name and the function is the corresponding function name, which will be called. The method `input()` handles the input and calls the function. To create a menu instance, the title and the running instance of the application is expected.

In some cases, another parameter is added to the __init__-function of a child class, which is a menu. This menu is used as the previous menu so that the user can chose a menu and has the possibility to return back to his origin menu.

## Usage of generative tools as ChatGPT, Gemini or Claude
Generative Tools as ChatGPT, Gemini, Claude or others were used in project. When a tool was used in a user story, it will be declared in the story itself. For the whole project were tools used to verify, whether all required tasks were fullfilled. Additionally, generative tools helped correcting wording mistakes and propose better worded sentences.
