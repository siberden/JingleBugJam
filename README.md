# Friendsgiving Jam App Testing

## Overview
This repository contains the test automation scripts for the Friendsgiving Jam App. The Friendsgiving Jam App simplifies the planning of friend gatherings by providing tools for event creation, menu planning, and sharing event details with friends. These tests ensure the app meets high standards of quality and functionality.

## Features
- **Event Creation Testing**: Verify the functionality of creating events with details such as event name, location, date, and time.
- **Menu Planning Testing**: Ensure the ability to add dishes and assign names to each dish for a well-organized menu.
- **Event Management Testing**: Validate the management of created events, including editing and deleting events.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/friendsgiving-jam-app-testing.git
   ```

2. Navigate to the project directory:
   ```bash
   cd friendsgiving-jam-app-testing
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the tests:
   ```bash
   pytest
   ```

## Project Structure
```
|-- pages/
|   |-- create_event_page.py  # Page object class for the Create Event page
|   |-- event_page.py         # Page object class for the Event page
|
|-- tests/
|   |-- test_create_event.py  # Test script for creating an event
|   |-- test_add_dish.py      # Test script for adding dishes to an event
|
|-- requirements.txt          # Lists the dependencies required for the project
```

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

