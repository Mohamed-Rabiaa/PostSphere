# PostSphere
A blog web application

## Introduction

PostSphere is a streamlined blog platform built with Django, focused on simplicity and efficient content management.  
Users can create, edit, and delete blog posts organized into predefined categories, with all content rendered server-side  
using the Django templating system.  
PostSphere features user authentication, SEO-friendly URLs, and a responsive design.

## Setup Instructions

1. Clone the project repository:
     ```bash
     git clone https://github.com/Mohamed-Rabiaa/PostSphere.git
     cd PostSphere

2. Set Up a Virtual Environment (Optional): Create and activate a virtual environment to keep dependencies isolated:
      ```bash
      python -m venv venv
      source venv/bin/activate

3. Install the required libraries:
     ```bash
     pip install -r requirements.txt

4. Set Environment Variables Before configuring the database, set the following environment variables based on your chosen database:
    ```bash
    export DATABASE_NAME='your_database_name'
    export USERNAME='your_database_username'
    export PASSWORD='your_database_password'
    export HOST='your_database_host'
    export PORT='your_database_port'

 Alternatively, you can store these in a .env file using a library like django-environ.

5. Update Database Settings in settings.py Use environment variables for the database configuration:

    ```bash
    import os
    
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or the relevant engine for your database
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('USERNAME'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
      }
    }

6. Run Migrations
  First, generate migration files for any model changes:
    ```bash
    python manage.py makemigrations
  Then, apply the migrations to set up the database schema:
  ```bash   
    python manage.py migrate
```
7. Create a Superuser Create a superuser to access Django’s admin panel:
    ```bash
    python manage.py createsuperuser

8. Run the Development Server Start the server to run the application:
    ```bash
    python manage.py runserver

9. Access the Application  
    Open a web browser and visit: `http://127.0.0.1:8000/accounts/login` to access the login page.  
    Access the admin panel via: `http://127.0.0.1:8000/admin/` using your superuser credentials.

## Usage

1. Register:
     * New users need to register by clicking the "Sign Up" link on the login page.
![Register](https://github.com/user-attachments/assets/25414462-8056-40a2-adde-245cb3df6666)

2. Creating a new post:
   * Go to the 'New Post' page and create a new post
![New Post](https://github.com/user-attachments/assets/33b269d0-3d31-4228-a105-98e82d96cb42)

3. Seeing your published post:
   * Go to the home page and you will see your post published there
   ![Home](https://github.com/user-attachments/assets/44551ff6-9016-4c70-a2b0-e3981ee6fb47)

4. Read the full post:
   * To read the full post Click on the post title on the home page
![Post Detail](https://github.com/user-attachments/assets/174d3565-3907-41ca-aad1-8240d8a18873)

## Overview Of The Project Architecture
1. Models  
   * User: Custom user model for authentication, profile, and image handling.  
   * Post: Blog posts associated with a Category. Fields include title, content, and category.  
   * Category: Organizes posts into categories like Tech, Culture, etc.

2. Views  
   * User Views:
      * register_view, login_view, profile_view logout_view:
       Handle user registration, login, profile management, and logout.
   * Post Views:
     * PostDetailView: Shows post details.
     * new_post_view, update_post_view, delete_post_view: CRUD operations for blog posts.
     * HomeView: Displays homepage with post filters like categories and latest posts.
     * CategoryPostsView: Displays posts filtered by category.
     * LatestPostsView: Displays the most 10 recent posts.

3. Forms
    * NewPostForm: A ModelForm used for creating and updating blog posts with custom title validation.
    * ProfileForm: Allows users to update their name, email, and profile image.
    * RegisterForm: Allows users to register to the website
    * LoginForm: Allows users to login to the website

4. Templates
    * Profile: Form for updating user profile.
    * Post Creation/Update: Forms for creating and updating posts with category selection.
    * Post List: Displays filtered posts (latest, by category).

5. URLs
    * accounts/urls.py:  
      `/register/`, `/login/`, `/profile/me`, `/logout/`: User authentication and profile routes.  
    * blog/urls.py:  
      `/home/`, `/home/latest_posts/`, `/home/<category>/`: Homepage and post filtering routes.  
      `/new_post/`, `/post_update/<slug>/`, `/post_delete/<slug>/`:  CRUD for posts.  

6. Static Files
    * CSS: Custom styles for layout and form handling.  
    * Media Handling: For user profile images using Django’s ImageField.  

## Contributing
Contributions are welcome! To contribute:

  1. Find a bug or suggest a new feature.
  2. Clone the project, make your changes, and commit them.
  3. Create a pull request.
   

Connect with me on [LinkedIn](https://www.linkedin.com/in/mohamed-rabiaa/). 
