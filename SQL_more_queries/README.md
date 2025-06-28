# Holberton SQL Project - SQL More Queries

This repository contains SQL scripts solving various database management and query problems on a MySQL server. Each script corresponds to a specific task, from user privilege management to complex joins between tables.

## Files and Descriptions

### 0. My privileges!
- Lists all privileges for MySQL users `user_0d_1` and `user_0d_2` on `localhost`.

### 1. Root user
- Creates MySQL user `user_0d_1` with all privileges and password `user_0d_1_pwd`.
- Ensures the user is created only if it does not exist.

### 2. Read user
- Creates a MySQL user `user_0d_2` with only read privileges.
- Ensures the user is created only if it does not exist.

### 3. Always a name
- Creates a table with a column that requires a non-null name value.

### 4. ID can't be null
- Creates a table where the `id` column cannot be `NULL`.

### 5. Unique ID
- Creates a table ensuring the `id` column is unique.

### 6. States table
- Creates a `states` table with appropriate columns and constraints.

### 7. Cities table
- Creates a `cities` table linked to the `states` table via a foreign key.

### 8. Cities of California
- Lists all cities that belong to the state of California.

### 9. Cities by States
- Lists all cities grouped or ordered by their respective states.

### 10. Genre ID by show
- Queries to find genre IDs associated with specific shows.

### 11. Genre ID for all shows
- Queries genre IDs for all shows in the database.

### 12. No genre
- Lists shows that do not have any genre assigned.

### 13. Number of shows by genre
- Displays the count of shows grouped by their genre.

### 14. My genres
- Lists genres associated with a specific user or criteria.

### 15. Only Comedy
- Lists all shows classified under the genre "Comedy".

### 16. List shows and genres
- Displays shows along with their respective genres using joins.

---

## Usage

Each `.sql` file is designed to be run with the MySQL command-line client, with the database name passed as an argument when required.

Example:

```bash
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
cat 6-states_table.sql | mysql -hlocalhost -uroot -p your_database_name
