# CloudFileHub API

## Overview

Django FileHub is a powerful file and folder management web application that allows users to efficiently organize, create, rename, delete, and share their files and folders. The application comes equipped with a user-friendly interface and robust functionality to streamline your file management experience.

### Key Features

- **Folder Management:**
  - Create new folders to organize your files systematically.
  - Rename and delete folders to maintain a tidy file structure.

- **File Operations:**
  - Create new files effortlessly.
  - Rename and delete files as needed.

- **File Sharing:**
  - **One-Time Share:** Share files securely for a one-time access experience.
  - **Public Share:** Make selected files publicly accessible.
  - **Email Share Link:** Share files conveniently by sending share links via email.

### Why CloudFileHub API?

- **Intuitive Interface:** The user-friendly design ensures a seamless and intuitive file management experience.

- **Flexible Sharing Options:** Choose between one-time share for added security, public sharing for widespread access, or share via email links for personalized sharing.

- **Efficient Organization:** Keep your files and folders organized with easy-to-use management tools.

## Running the API

Follow these steps to run the Django FileHub API locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/CloudFileHub/api.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd api
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run The Development Server:**
   ```bash
   python manage.py runserver
   ```

7. **Run The Development Server:**
   ```bash
   python manage.py runserver
   ```

8. **Access The API:**
   Open your web browser and go to http://127.0.0.1:8000/ to interact with the Django FileHub API
