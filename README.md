# To Do List

## Overview
This To Do List application enables users to manage their daily tasks efficiently through a set of RESTful API endpoints. Users can add, remove,update, and delete tasks. The application is designed with scalability and extensibility in mind. This architecture facilitates easy modifications and extensions.

## Features
- **Scalable Architecture**: Easily scale by increasing the number of lists.
- **Simple and Extensible**: Easily modified and extended to include additional functionalities.

## Installation
- Clone the following url in your command prompt: https://github.com/CodelineAtyab/genz-todo-list-app.git

### Prerequisites
- Python 3.x
- CherryPy

### Setup
1. Clone the repository (see the Installation section above).
2. Install required Python packages from requirements.txt: `pip install -r requirements.txt`

## Usage

- Post https://localhost:8080/api/v1/todoRecords<description used to create a new ToDoList task>
- Delete https://localhost:8080/api/v1/todoRecords/<description used to delete an existing ToDoList task>
- Put https://localhost:8080/api/v1/todoRecords/<description used to update an eisting ToDoList task>
- Get All https://localhost:8080/api/v1/todoRecords<description used to get all the ToDoList Tasks>
- Get Specific https://localhost:8080/api/v1/todoRecords/<description Used to get a specific ToDoList Task>

### Running the Program
- **Script**: `python main_app.py`
- **Access URL**: `https://localhost:8080/api/v1/todoRecords`

## Contributing
Contributions to this project are prohibited due to the Course Restrictions.

## License
This project is licensed under the MIT License.

## Contact
For any queries, please contact omantel@omantel.om

## Acknowledgements
- Class Implimintation by Abbas.
- Filtering and JSON conversion by Sara.
- Unit Testing for field validation by Sughiya.
- Restful API endpoint for Deletion point by Lujain.
- Restful API endpoint for Item Update point by Rudaina.
- Restful API endpoint for Item Retrieval point by Ziyad.
- Restful API endpoint for Item Creation point by Abdulaziz.
- Extremely Complex and Proffesional UI by Atyab.
- Implementing Pickle for Data Persistance by Maather.
- ReadMe by Haitham.