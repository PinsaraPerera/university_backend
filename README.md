## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/PinsaraPerera/Attendance_System_API.git
    cd Attendance_System_API/backend
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source ./venv/Scripts/activate  # On git bash
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the root of your project and add the necessary environment variables:

    ```sh
    touch .env
    ```

    Example `.env` file:

    ```plaintext
    PROJECT_ID=your_project_id
    REGION=your_region
    INSTANCE_NAME=your_instance_name
    DB_USER=your_db_user
    DB_PASS=your_db_password
    DB_NAME=your_db_name
    ```

## Running the Application

To start the FastAPI application with Uvicorn and enable the auto-reload feature for development, use the following command:

```sh
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### workflow to add new endpoint

01) create a database model in app/models
02) create a pydantic schema in app/schemas
03) add endpoints in app/api/endpoints
04) add CRUD for those endpoints in app/crud
05) add the router path in app/main.py