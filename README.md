# Alpstay

This project results from the python module "Anwendungsentwicklung mit Python" from the FHNW. 
The goal is to create a hotel reservation system, which uses a partially given mysql database. In several iterations, we work on user stories and try to implement them on the bases of the newly learned concepts.

## Organization

### Decision Github
This project could have been realized as a jupiter notebook. A jupiter notebook like DeepNote is great for using code in a documentation. It doesn't require a local installation of Python and the Libraries are provided automatically. However, we have decided to create a console application due to the fact, that we wanted to see, how the application as a whole will work. This provides a better understanding for software and the work within a team.

When working with a team, versioning is an essential part of working together. The best-known tool for this is any kind of git. Due to prior knowledge, the benefit of Github Pro as a student and recommendation of the coaches, we decided to use Github as our versioning tool. 

### Kanban Board
To track progress and tasks as a team, a kanban boaA very easy to use choice would be the Microsoft Planner. However, with Github Projects, the kanban board with tasks, bugs and issues is directly integrated in the project. The wide variety of standard, built-in features as types, milestones and great filtering, Github Projects is perfect to use in a small team as ours. 

### Time Planning
Additionally, the time planning is easy to use with Github projects. Creating a tasks provides the ability to add it on a timeline.

### Communication
Communicating with each other can be quite hard, especially, when the team members can't see eachother often. Therefore, we communicated using Teams or WhatsApp. We tried to come together 1-2 times per week at the FHNW.

### Code Documentation
Documentation of the code happens in the code itself using docstrings as well as in the ReadMe. The ReadMe contains all user stories, in which concepts, structures and interesting decisions and findings are held. The docstrings contain information about how to use certain classes and methods.

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
The connection from room type to facilities is over the room itself.

### 2.1. As a guest, I want to see the following information for each room: room type, maximum amount of guest, description, facilities, price per night and total price
Ich möchte die folgenden Informationen pro Zimmer sehen: Zimmertyp, max. Anzahl der Gäste, Beschreibung, Ausstattung, Preis pro Nacht und Gesamtpreis.

### 2.2 As a guest, I only want to see available rooms if I have specified the dates of my stay
Ich möchte nur die verfügbaren Zimmer sehen, sofern ich meinen Aufenthalt (von – bis) spezifiziert habe.

### 3. As an admin, I want to have the possibility to update information about hotels
Als Admin des Buchungssystems möchte ich die Möglichkeit haben, Hotelinformationen zu pflegen, um aktuelle Informationen im System zu haben.

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

### 5. As a guest, I want to receive an invoice after my stay
Als Gast möchte ich nach meinem Aufenthalt eine REchnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der Invoice Tabelle hinzu

The user is asked to enter a booking ID. This ID is passed to the controller, which calls a method to fetch the booking details from the data access layer. There, a SQL query pulls all relevant info from a view that includes booking data, guest name, and hotel information. If the booking is cancelled, no invoice is created and a matching message is shown.

If the booking is active / not cancelled, the current date is set as the invoice issue date, and a new invoice is inserted into the database. The controller then returns all necessary objects back to the GUI, where the full invoice is printed out – including guest name, hotel info, dates, total amount and more.

We made it possible to create multiple invoices for the same booking on purpose. This way, if something changes later (e.g. a correction or customer request), a new invoice can be generated easily without overwriting anything.

### 6. As a guest, I want to be able to cancel my booking
Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hint: Sorgt für die entsprechende Invoice. 

### 7. As a guest, I want to have dynamics prices to profit from dynamic pricing
Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann. Hint: Wendet in der Hochsaison höhere und in der Nebensaison niedrigere Tarife an.

The user is first asked to enter the city, check-in date, and check-out date. This info is passed to the controller, where the dates are parsed and sent to the data access layer. There, we check for all rooms in the given city that aren’t already booked during that period (cancelled bookings don’t count). The query also joins the hotel and room type, so we can show more than just room IDs.

In the business logic, we go through each room and create a Room object. Then we check how many nights fall into high season (May to September) and how many don’t. Based on that, we calculate the total price with a 20% increase for high season and 20% discount for off-season. We also calculate the average price per night. All of this is then returned to the GUI, where we show the user a detailed overview.

We wanted to make pricing as clear as possible, so users know exactly what they’re paying for – not just the total, but how it’s made up.

However, we decided not to use this pricing logic in all bookings and searches for now, because in reality each hotel would probably want to set their own surcharges - mountain hotels have high season in winter, city hotels in summer - so a fixed rule wouldn’t really make sense everywhere...

### 8. As an admin, I want to see all bookings
Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.

### 9. As an admin, I want to see all rooms with their facilities
Als ADmin möchte ich eine Liste der Zimmer mit ihrer Ausstattuns sehen, damit ich sie besser bewerben kann.

### 10. As an admin, I want to be capable to update master data (RoomTypes, Facilities, Prices)
Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat. Hint: Stammdaten sind alle Daten, die nicht von anderen Daten abhängen.

### User Stories mit DB-Schemaänderung

### 1. As and admin, I want to update missing information in bookings
Als Admin möchte ich alle Buchungen bearbeiten können, um fehlende Informationen zu ergänzen (z.B. Telefonnummer). 



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

### User Stories with data visualization

### As an admin, I want to see the occupancy rate for each room type
Als Admin möchte ich die Belegungsraten für jeden Zimmertyp in meinem Hotel sehen, damit ich weiss, welche Zimmer am beliebtesten sind und ich meine Buchungsstrategien optimieren kann. Hint: Wählt ein geeignetes Diagramm, um die Auslastung nach Zimmertyp darzustellen (z. B. wie oft jeder Zimmertyp gebucht wird).

### As an admin, I want to analyze my guests based on demografic attributes
Als Admin möchte ich eine Aufschlüsselung der demografischen Merkmale meiner Gäste sehen, damit ich gezieltes Marketing
planen kann. Hint: Wählt ein geeignetes Diagramm, um die Verteilung der Gäste nach verschiedenen Merkmalen darzustellen (z. B. Altersspanne, Nationalität, wiederkehrende Gäste). Möglicherweise müssen Sie der Tabelle „Gäste“ einige Spalten hinzufügen.

### Optional user stories

## Usage of generative tools as ChatGPT, Gemini or Claude
Generative Tools as ChatGPT, Gemini, Claude or others were used in project. When a tool was used in a user story, it will be declared in the story itself. For the whole project were tools used to verify, whether all required tasks were fullfilled. Additionally, generative tools helped correcting wording mistakes and propose better worded sentences.
