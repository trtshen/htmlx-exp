# Live Notes with Flask and HTMX

A minimalist note-taking web application that demonstrates the power of HTMX with Flask. This project showcases how to build a modern, responsive web application with minimal JavaScript using HTMX for dynamic content updates.

## Features

- **Real-time Updates**: Add, edit, and delete notes without page reloads
- **Inline Editing**: Edit notes directly in place
- **Persistent Storage**: Notes are stored in SQLite database
- **Minimal Design**: Clean, responsive UI with basic styling
- **Zero JavaScript**: All interactivity is handled by HTMX attributes

## Technologies Used

- **Backend**: [Flask](https://flask.palletsprojects.com/) (Python web framework)
- **Database**: SQLite via [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- **Frontend**: [HTMX](https://htmx.org/) (HTML extension for AJAX)
- **Styling**: Custom CSS

## How It Works

HTMX enables rich user interactions through HTML attributes rather than JavaScript. For example:

```html
<button hx-delete="/notes/1" hx-target="#note-1" hx-swap="outerHTML">Delete</button>
```

This button will send a DELETE request to `/notes/1` and replace the element with id `note-1` with the response.

## Project Structure

```
.
├── app.py                   # Main Flask application
├── requirements.txt         # Python dependencies
├── templates/               # HTML templates
│   ├── index.html           # Main page template
│   └── partials/            # Partial templates for HTMX updates
│       ├── note.html        # Individual note display
│       └── note_form.html   # Note editing form
└── notes.db                 # SQLite database (created on first run)
```

## Setup and Running

1. **Clone the repository**

2. **Set up a virtual environment (recommended)**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Visit [http://localhost:5000](http://localhost:5000) to use the application

## How to Use

- **Add a note**: Type in the text area at the top of the page and click "Add Note"
- **Edit a note**: Click the "Edit" button on any note
- **Delete a note**: Click the "Delete" button on any note
- **Cancel editing**: When editing, click "Cancel" to discard changes

## Development

This project serves as a demonstration of how to build modern web applications with minimal JavaScript using HTMX and Flask. Feel free to use it as a starting point for your own projects.

To extend the application, you might consider:

- Adding user authentication
- Implementing note categories or tags
- Adding rich text formatting
- Implementing search functionality
- Adding dark mode toggle

## Resources

- [HTMX Documentation](https://htmx.org/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)

## License

MIT

---

Created as an experimental project to explore the capabilities of HTMX with Python Flask.
