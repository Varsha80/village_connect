VillageConnect:-Empowering Rural Communities

VillageConnect is a simple and impactful web application built using Flask(Python) and SQLite.  
It is designed to support rural communities by providing a platform where users can share, discover, and request local services such as water delivery, transportation, health assistance, and more along with a community forum for communication.

Home Page
- A clean, welcoming design with village-themed background
- Navigation to Services and Community Forum

Services Page
- Add a new service (title, description, location, user ID)
- Search services by keywords (e.g., "doctor", "transport")
- View all posted services
- (Optional) Delete a service by ID

Community Forum
- 📝 Post public messages with a user ID
- 💬 View all public posts on a digital noticeboard

REST API Endpoints
- GET /api/services → Returns all services in JSON
- POST /api/services → Add a service using JSON payload

Technologies Used

| Tool/Tech         | Purpose                            |
|-------------------|-------------------------------------|
| Python            | Backend logic                      |
| Flask             | Web framework                      |
| SQLite            | Lightweight database               |
| Flask-SQLAlchemy  | ORM for DB management              |
| HTML/CSS (Jinja2) | Frontend templating and styling    |
| Bootstrap (opt.)  | Responsive layout                  |


