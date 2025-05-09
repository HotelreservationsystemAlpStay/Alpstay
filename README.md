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

### View

### Utils

## Userstories
The original user stories were written in german is it is a german-based course. Due to the majority of code being developed in english, the documentation is in english. The description of the user stories are in english aswell as in german. Additionally, for the spirit of the documentation, the user stories are seperated or combined.

## Minimale User Stories

### 1. As a guest, I want to search for a hotel in a city, so that i can choose the one, that meets my criteria:
Als Gast möchte ich die verfügbaren Hotels durchsuchen, damit ich dasjenige auswählen kann, welches meinen Wünschen entspricht

### 1.1. Criteria 1: City
Ich möchte alle Hotels in einer Stadt durchsuchen, damit ich das Hotel nach meinem bevorzugten Standort (Stadt) auswählen kann.

### 1.2. Criteria 2: Stars
Ich möchte alle Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen.

### 1.3. Criteria 3: Amount of guests in a room
Ich möchte alle Hotels in einer Stadt durchsuchen, die Zimmer haben, die meiner Gästezahl entsprechen (nur 1 Zimmer pro Buchung).

### 1.4. Criteria 4: Availability (Room in a hotel is available between start date and end date)
Ich möchte alle Hotels in einer Stadt durchsuchen, die während meines Aufenthaltes ("von" (check_in_date) und "bis" (check_out_date)) Zimmer zur Verfügung haben, damit ich nur relevante Ergebnisse sehe.

### 1.5. Criteria 5: Combine the upper four criteria
Ich möchte Wünsche kombinieren können, z.B. die verfügbaren Zimmer zusammen mit meiner Gästezahl und der mindest Anzahl Sterne.

### 1.6. Criteria 6: The following Information should be displayed: Hotel name, hotel address, amount of stars
Ich möchte die folgenden Informationen pro Hotel sehen: Name, Adresse, Anzahl der Sterne.

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

### 3.2. As an admin, I want to delete hotels from the system
Ich möchte Hotels aus dem System entfernen

### 3.3. As an admin, I want to update information of hotel
Ich möchte die Information bestimmter Hotel aktualisieren, z.B. den Namen, die Sterne usw.


### 4. As a guest, I want to book a room in a certain hotel
Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen

### 5. As a guest, I want to receive an invoice after my stay
Als Gast möchte ich nach meinem Aufenthalt eine REchnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der Invoice Tabelle hinzu

### 6. As a guest, I want to be able to cancel my booking
Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hint: Sorgt für die entsprechende Invoice. 

### 7. As a guest, I want to have dynamics prices to profit from dynamic pricing
Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann. Hint: Wendet in der Hochsaison höhere und in der Nebensaison niedrigere Tarife an.

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

### 2.1. For all bookings, I should be able to use the following action "create", "update", "cancel".
Die Anwendungsfälle für meine Buchungen sind "neu/erstellen", "ändern/aktualisieren", "stornieren/löschen".

### 3. As a guest, I want to create a rating about the stay at a hotel
Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.

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
