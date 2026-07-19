# Library Management System

[![Python Version](https://img.shields.io/badge/Language-Python%203.8%2B-blue.svg)](https://www.python.org/)
[![Development IDE](https://img.shields.io/badge/IDE-PyCharm-black.svg?style=flat&logo=pycharm&logoColor=white)](https://www.jetbrains.com/pycharm/)

A modular, production-grade console application built in Python utilizing robust Object-Oriented Programming (OOP) architectures to manage library catalogs, member accounts, and book circulation logs. Designed with clean architectural separation to mock real-world software workflows, complete with persistent storage configurations.

---

## 🚀 Key Engineering Features

* **Object-Oriented Architecture:** Engineered using encapsulation, inheritance, and polymorphism patterns to decouple core domain models (`Book`, `Member`, `Transaction`, `Library`).
* **Persistent Data Matrix:** Implements automated state persistence using standard file streams (`JSON` / `CSV` mapping modules) ensuring catalog configurations survive application restarts.
* **Smart Circulation Logic:** Features transactional check-out and check-in algorithms tracking availability states, due date rules, and dynamic membership limits.
* **Advanced Query Routing:** Supports rapid cross-field searches enabling system users to query items seamlessly by Title, Author, or ISBN keys.

---

## 🛠️ Technical Stack & Framework

* **Core Language:** Python 3.8
* **Data Layer:** Flat-file data serialization via built-in packages (`json` or `csv`).
* **Testing & Tools:** Built-in validation algorithms, error handling blocks (`try-except`), and terminal formatting schemes.

---

## 📊 Class Architecture Design

The backend is built around discrete functional entities interacting through a centralized controller class:

* `Book`: Model tracking structural metadata (ISBN, title, author, quantity available, borrowing status).
* `Member`: System entity tracking individual student/staff credentials and active borrowed lists.
* `Library`: The transactional command hub managing indexing arrays, stream processing, and system operations.

---

## 🖥️ User Operations Control Portal

The application runs a clean terminal control console providing administrative options:

1. **Add New Book Asset** — Validates structural fields and logs new assets to storage.
2. **Register System Member** — Instantiates user profiles with discrete clearance levels.
3. **Issue Book Loan** — Validates token tracking limits and changes asset availability flags.
4. **Process Book Return** — Computes active transaction deltas and restores asset quantities.
5. **Search Catalog Index** — Returns targeted data structures instantly based on input keys.
6. **Graceful System Exit** — Flushes transient runtime data streams directly back to physical file packages.
