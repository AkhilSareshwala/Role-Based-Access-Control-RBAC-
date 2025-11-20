# Fullstack RBAC – Project, Task, and User Management System

A role-based access control (RBAC) system built with **Django**, featuring:

- User Roles → **ADMIN**, **MANAGER**, **USER**
- Project & Task Management
- User Dashboard & Status Updates
- Admin Panel for complete user management


---

## 🚀 Features

### **Admin Role**
- Access `/dashboard`
- View users list
- Add/Edit/Delete users
- Assign roles (ADMIN / MANAGER / USER)
- Export users as CSV

### **Manager Role**
- Create Projects
- Create Tasks inside projects
- Assign tasks to users
- View all tasks under projects

### **User Role**
- View “My Tasks”
- Update task status (pending → in_progress → completed)

---

## 📌 Roles & Permission Logic

### **ADMIN**
- Full control over all users
- Cannot manage projects or tasks
- Permissions handled using `admin_required` decorator

### **MANAGER**
- Can create/edit projects
- Can create/assign tasks
- Can view tasks of their created projects
- Cannot access admin dashboard

### **USER**
- Can only view tasks assigned to them
- Can update status of their tasks
- Cannot create/edit projects or tasks

---

## 🔑 Default Role Behavior

| Role     | Access Dashboard | Manage Users | Manage Projects | Manage Tasks | Update Task Status |
|----------|------------------|--------------|------------------|---------------|---------------------|
| ADMIN    | ✅ Yes           | ✅ Yes        | ❌ No            | ❌ No         | ❌ No               |
| MANAGER  | ❌ No            | ❌ No         | ✅ Yes           | ✅ Yes        | ✅ Yes              |
| USER     | ❌ No            | ❌ No         | ❌ No            | ❌ No         | ✅ Yes (my tasks)  |

---

