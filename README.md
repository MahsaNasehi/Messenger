# Messenger DataBase Design
## Overview
The primary goal of this project is to familiarize ourselves with the process of database-side development and implement a simple web app in the form of a messaging platform, similar to popular platforms like Telegram. However, in this project, the focus is mainly on the database aspect, while other components are implemented at a minimal and very basic level.

## Database Design Includes the Following:
### User Account
A user is one of the main elements of our messaging platform. Each user must have an account to log in, which contains their personal information. This information includes the user's first name, last name, unique phone number, unique username, and more.

### Contact List
Each user has a contact list to make it easier to view or initiate chats.

### Chat
Any user who wants to communicate with another user must create a chat for this interaction. Each chat is specific to two users in the system, and for more than two participants, a group must be created, which will be discussed later. Two users can only have one chat with each other. It's worth noting that a chat includes a number of messages.

### Message
A series of messages are exchanged between any two users in the system. These messages include attributes to specify which chat they belong to and other details. Note that messages can also be related to a group; to manage them, you can use sender and receiver attributes or create a separate relationship, such as a separate table.

### Group Chat
Group chat is a feature that allows users to create a group and share their messages and announcements. Each group can have multiple members, and group members can share different text messages with each other.

### SpecialQueries
in the (Model\Advanced_Queries\SpecialQueries.sql) dir

## Technologies Utilized

- **Python**: Core programming language used for backend logic and application development.
- **Docker**: For containerizing the application and ensuring portability across different environments.
- **SQL**: Used for designing, querying, and managing the relational database.
- **FastAPI**: For building the web API to handle user interactions and data exchange.
- **Uvicorn**: ASGI server for running the FastAPI application.
- **Postman**: For testing and validating API endpoints, ensuring the functionality and performance of the backend.


## Installation

1. Clone this repository to your local machine:
   ```bash
      git clone https://github.com/MahsaNasehi/Messenger.git
   ```
2. Open the project in your preferred IDE (e.g., VS Code, or Pycharm).

3. Install and start Docker Desktop
4. Build and Start the Containers
   ```bash
      docker compose up -d
   ```
5. Install FastAPI and Uvicorn
   ```bash
      pip install fastapi uvicorn
   ```
6. Navigate into the directory of project(in the Controller dir) and run the Fastapi:
   ```bash
       fastapi run response_controller.py
   ```
   

## Endpoints
### (POST)
/pv_create/: For creating a private chat

/group_create/: For creating a group

/group_member_addition/: For adding members to groups

/msg_create/: For sending a message in a group

### (GET)
/read_user_by_id/: Takes a specific ID and returns the corresponding user.

/read_contact_by_id/: Takes a user’s ID and returns the IDs of their contacts.

/read_group_by_id/: Takes a group ID and returns the name of the group.

/read_group_member_by_id/: Takes a group ID and returns the IDs of its members.

/read_msg_by_id/: Takes a message ID and returns the remaining details of the message.

/read_pv_by_id/: Takes a private chat ID and returns the IDs of the two related users.

### (PATCH)
/update_user/: Updates the user's information based on the specified field.

/update_group/: Updates the name of the group.

/update_msg_content/: Edits the content of a message.

### (DELETE)
/delete_user_by_id/: Deletes a user from the messaging platform using their ID.

/delete_contact_by_ids/: Removes a specific contact from the contact list using their ID.

/delete_group_by_id/: Deletes a group using its ID.

/delete_group_member_by_ids/: Removes a user from a group using their ID.

/delete_pv_by_id/: Deletes a private chat using its ID.

/delete_msg_by_id/: Deletes a message from a group using its ID.

## License

The project is licensed under the MIT License.[LICENSE](LICENSE)

## Authors  
- **Mahsa Nasehi** [GitHub Profile](https://github.com/MahsaNasehi)
---
