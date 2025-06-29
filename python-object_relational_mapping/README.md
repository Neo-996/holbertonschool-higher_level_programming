# MySQL & SQLAlchemy State-City Project

This project contains a series of Python scripts for interacting with a MySQL database that manages information about U.S. states and cities. It uses both raw SQL and SQLAlchemy (an ORM) to demonstrate various database operations.

## Contents

### 0 - 6: Basic SQL Scripts
1. `0-select_states.py` - Get all states.
2. `1-filter_states.py` - Filter states by name.
3. `2-my_filter_states.py` - Filter states by user input.
4. `3-my_safe_filter_states.py` - Prevent SQL Injection by using parameterized queries.
5. `4-cities_by_state.py` - Get cities with their corresponding states.
6. `5-filter_cities.py` - Get all cities of a given state.

### 6 - 14: SQLAlchemy (ORM-based)
7. `6-model_state.py` - First SQLAlchemy model (`State`).
8. `7-model_state_fetch_all.py` - List all `State` objects from the database.
9. `8-model_state_fetch_first.py` - Print the first `State` object.
10. `9-model_state_filter_a.py` - List all states containing the letter `a`.
11. `10-model_state_get.py` - Get a state by ID.
12. `11-model_state_insert.py` - Add a new state to the database.
13. `12-model_state_update_id_2.py` - Update the name of the state with ID = 2.
14. `13-model_state_delete_a.py` - Delete all states containing the letter `a`.
15. `14-model_city_fetch_by_state.py` - Display all cities grouped by state.

## Requirements

- Python 3.x
- MySQL server
- MySQLdb (for raw SQL)
- SQLAlchemy (for ORM-based scripts)
