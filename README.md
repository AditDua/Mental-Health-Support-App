
# Mental Health Support Application

This is a web application designed to help users track their mental health through journal entries and mood ratings. It offers resources for mental health support and provides a user-friendly interface for managing personal reflections and emotional states.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Routes](#routes)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication
- Create and manage journal entries
- Rate mood on a scale of 1 to 5 with emoji representations
- View a list of journal entries
- Access mental health resources
- Responsive design using Bootstrap

## Technologies Used

- Flask: Web framework for building the application
- SQLAlchemy: ORM for database management
- SQLite: Database for storing user information and journal entries
- HTML/CSS: For front-end design
- Bootstrap: CSS framework for responsive design
- Werkzeug: For password hashing and security

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   git clone (https://github.com/AditDua/Mental-Health-Support-App/)
   
   cd mental-health-journal

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   - For Windows:
     venv\Scripts\activate

   - For macOS/Linux:
     source venv/bin/activate

5. Install the required packages:

   pip install -r requirements.txt

6. Set up the database:

   python app.py

7. Run the application:

   python app.py

   The application will be accessible at http://127.0.0.1:5000.

## Usage

1. Register a New User: Navigate to the registration page (/register) and fill in the required fields.
2. Log In: Use your credentials to log in at the /login page.
3. Add Journal Entries: After logging in, you can create new journal entries by navigating to the /journal page.
4. View Entries: Your journal entries will be displayed on the home page (/), where you can see your mood ratings and content.
5. Access Resources: Click on the "Resources" link to find helpful mental health resources.

## Routes

- `/`: Home page displaying journal entries.
- `/login`: User login page.
- `/register`: User registration page.
- `/journal`: Page for adding new journal entries.
- `/resources`: Page displaying mental health resources.
- `/logout`: Logs out the user.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
