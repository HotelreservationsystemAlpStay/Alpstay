# Alpstay

This project results from the python module "Anwendungsentwicklung mit Python" from the FHNW. 
The goal is to create a hotel reservation system, which uses a partially given mysql database. In several iterations, we work on user stories and try to implement them on the bases of the newly learned concepts.

## Organization
### Time Planning
### Communication
### Project Board
### Code Documentation

## Userstories
The original user stories were written in german is it is a german-based course. Due to the majority of code being developed in english, the documentation is in english. The description of the user stories are in english aswell as in german. Additionally, for the spirit of the documentation, the user stories are seperated or combined.

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

### 2.1:

## Usage of generative tools as ChatGPT, Gemini or Claude
