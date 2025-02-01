# CS50 Project 4 - Network

A custom design project for CS50's Web Programming with Python and JavaScript course, which is a simple clone of X/Twitter. The project utilizes Django, HTML, JS and CSS.

## Demo

A short video where I go through the required specifications of the project: [https://youtu.be/tdkpOleV3NY](https://youtu.be/tdkpOleV3NY)

### Test Login Credentials

| Username | Password  |
|----------|-----------|
|   John   | password  |

---

## Project Features

### Core Functionality

1. **User Authentication**:
   - Users can register for an account, log in, and log out.
   - Different content is displayed based on whether a user is authenticated.

2. **New Post**:
   - Signed-in users can create new text-based posts.
   - Posts are added to the database and displayed across the application.

3. **All Posts**:
   - Displays all posts from all users, ordered by the most recent first.
   - Each post shows the username, content, timestamp, and like count.

4. **Profile Page**:
   - Clicking on a username leads to that user's profile page.
   - Displays the user's posts, follower count, and following count.
   - Users can follow or unfollow others from their profile pages.

5. **Following Feed**:
   - Displays posts only from users that the current user follows.
   - Requires the user to be signed in to access.

6. **Pagination**:
   - Posts are displayed in pages, with up to 10 posts per page.
   - Includes "Next" and "Previous" buttons for navigation.

7. **Edit Post**:
   - Users can edit their own posts.
   - Editing is done asynchronously without refreshing the page.

8. **Like/Unlike Posts**:
   - Users can toggle "likes" on any post.
   - Like counts update dynamically without a page reload.

---

## Additional Notes

- **Consistency**: Ensure that the layout, styling, and navigation maintain a cohesive design across the site.
- **Error Handling**: Provide clear feedback for invalid inputs, such as bids that do not meet the required criteria.
- **Extensibility**: The design and code should allow for future enhancements without significant rework.

---

## Running the Application

To start the application, follow these steps:

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

2. Running migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
2. Start the application
   ```bash
   python manage.py runserver

## Build static assets

To build static assets, follow these steps:

```bash
python manage.py collectstatic