📚 Library Management System
# 📚 Library Management System

A Django-based Library Management System where users can add, borrow, and return books. The system provides a simple interface for managing books and tracking borrowed items.

## 🚀 Features

✅ Add new books with title, author, and count  
✅ Borrow books and track due dates  
✅ Return books with recorded return dates  
✅ View all books in a list format  
✅ User roles: Students & Teachers  
✅ Responsive design for mobile and desktop  

---

## 🛠️ Technologies Used

🔹 **Backend:** Django (Python)  
🔹 **Frontend:** HTML, CSS  
🔹 **Database:** SQLite (default Django DB, can be changed)  

---

## 🏗️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Apply Migrations
python manage.py migrate
5️⃣ Run the Server
python manage.py runserver
6️⃣ Open in Browser
Go to: http://127.0.0.1:8000/

📝 Usage
1️⃣ Adding a New Book

Navigate to the Add Book section.
Enter the book title, author, and count.
Click Submit to add the book.
2️⃣ Borrowing a Book

Select a book from the list.
Enter the borrower's name and borrow date.
Click Submit to borrow the book.
3️⃣ Returning a Book

Navigate to the Borrowed Books section.
Enter the return date and mark it as returned.
📌 Future Improvements
✅ Search functionality for books
📅 Due date reminders for borrowed books
📊 Admin dashboard with statistics
🔐 User authentication system

📜 License
This project is open-source and available under the MIT License.

🚀 Happy Coding! 🚀
