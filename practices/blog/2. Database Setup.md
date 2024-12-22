# Database Setup Guide for Django Projects

This document provides a comprehensive step-by-step guide to set up SQLite, MySQL, and Oracle databases for Django projects. Follow these instructions to configure and integrate your database with Django.

---

## **1. SQLite Setup**

### **Overview**
### **Steps**

1. **Default Configuration**
   - Open your project’s `settings.py` file and locate the `DATABASES` section:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

2. **Run Migrations**
   - Apply the default migrations to set up the database:
     ```bash
     python manage.py migrate
     ```

3. **Verify Database File**
   - Confirm the creation of the database file:
     ```bash
     ls db.sqlite3
     ```

4. **Access the Database**
   - Enter the SQLite shell to inspect the database:
     ```bash
     python manage.py dbshell
     ```

---

## **2. MySQL Setup**

### **Overview**
### **Steps**

1. **Install MySQL Server**
   - On Ubuntu:
     ```bash
     sudo apt update
     sudo apt install mysql-server
     ```

2. **Create a MySQL Database**
   - Log in to MySQL:
     ```bash
     sudo mysql
     ```
   - Create the database and user:
     ```sql
     CREATE DATABASE blog_db;
     CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
     GRANT ALL PRIVILEGES ON blog_db.* TO 'username'@'localhost';
     FLUSH PRIVILEGES;
     ```

3. **Install Python Connector**
   - Install `mysqlclient`:
     ```bash
     pip install mysqlclient
     ```
   - Alternatively, install `mysql-connector-python` if `mysqlclient` fails:
     ```bash
     pip install mysql-connector-python
     ```

4. **Update `settings.py`**
   - Modify the `DATABASES` section:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'blog_db',
             'USER': 'username',
             'PASSWORD': 'password',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

5. **Run Migrations**
   - Apply migrations to create tables:
     ```bash
     python manage.py migrate
     ```

6. **Verify Tables in MySQL**
   - Log in to MySQL and check the tables:
     ```bash
     mysql -u username -p
     USE blog_db;
     SHOW TABLES;
     ```

---

## **3. Oracle Setup**

### **Overview**
### **Steps**

1. **Download Oracle Instant Client**
   - Visit the [Oracle Instant Client Downloads page](https://www.oracle.com/database/technologies/instant-client.html).
   - Download the appropriate package for your system (e.g., Linux x86-64).

2. **Install Oracle Instant Client**
   - Extract the downloaded files:
     ```bash
     mkdir -p /opt/oracle
     unzip instantclient-basic-linux.x64*.zip -d /opt/oracle
     mv /opt/oracle/instantclient_* /opt/oracle/instantclient
     ```
   - Add the library path to your environment:
     ```bash
     export LD_LIBRARY_PATH=/opt/oracle/instantclient:$LD_LIBRARY_PATH
     ```

3. **Install `cx_Oracle`**
   - Install the Python Oracle client:
     ```bash
     pip install cx_Oracle
     ```

4. **Update `settings.py`**
   - Modify the `DATABASES` section:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.oracle',
             'NAME': 'orclpdb1',  # Replace with your Oracle Service Name
             'USER': 'username',
             'PASSWORD': 'password',
             'HOST': 'localhost',
             'PORT': '1521',
         }
     }
     ```

5. **Run Migrations**
   - Apply migrations to create tables:
     ```bash
     python manage.py migrate
     ```

6. **Verify Tables in Oracle**
   - Log in to Oracle and list the tables:
     ```sql
     SELECT table_name FROM user_tables;
     ```

---
