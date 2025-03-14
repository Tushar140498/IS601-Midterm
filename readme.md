# Calculator Application

## Table of Contents
- [Project Overview](#project-overview)
- [Core Functionalities](#core-functionalities)
- [Plugin System](#plugin-system)
- [Calculation History Management](#calculation-history-management)
- [Professional Logging Practices](#professional-logging-practices)
- [Advanced Data Handling with Pandas](#advanced-data-handling-with-pandas)
- [Design Patterns for Scalable Architecture](#design-patterns-for-scalable-architecture)
- [Testing and Code Quality](#testing-and-code-quality)
- [Version Control Best Practices](#version-control-best-practices)
- [Documentation](#documentation)
- [Video Showcase](#video-showcase)

## Project Overview
This calculator application provides a command-line interface (REPL) that supports basic arithmetic operations, manages calculation history, and allows for plugin integration. It utilizes Pandas for efficient data management and includes professional logging practices to track application behavior.

## Core Functionalities
The application features a REPL that enables users to:
- Execute arithmetic operations: addition, subtraction, multiplication, and division.
- Manage calculation history through commands to show, save, clear, and delete history entries.
- Access extended functionalities via dynamically loaded plugins.

## Plugin System
A flexible plugin system has been implemented to facilitate seamless integration of new commands or features. This allows developers to create plugins that can be dynamically loaded without altering the core application code. The application includes a "Menu" command in the REPL to list all available plugin commands, enhancing user discoverability.

## Calculation History Management
Pandas is utilized to manage calculation history effectively. Users can:
- Load and display history from a CSV file.
- Save the current history to a CSV file.
- Clear or delete specific history entries, with these changes reflected in the CSV file.

## Professional Logging Practices
A comprehensive logging system is established to record:
- Detailed application operations and data manipulations.
- Errors and informational messages.
- Different log message severity levels (INFO, WARNING, ERROR) for effective monitoring.

Dynamic logging configuration is supported through environment variables, allowing customization of logging levels and output destinations.

## Advanced Data Handling with Pandas
Pandas is employed for:
- Efficient data reading and writing to CSV files.
- Management of calculation history, ensuring robust data handling.

## Design Patterns for Scalable Architecture
Key design patterns are incorporated to address software design challenges:
- **Facade Pattern**: Offers a simplified interface for complex data manipulations with Pandas.
- **Command Pattern**: Structures commands within the REPL for effective calculation and history management.
- **Factory Method, Singleton, and Strategy Patterns**: Further enhance the application's structure, flexibility, and scalability.

## Testing and Code Quality
The application achieves a minimum of 90% test coverage using Pytest. Code quality is maintained and verified against PEP 8 standards using Pylint.

## Version Control Best Practices
Logical commits are utilized to clearly group feature development and corresponding tests, evidencing clear development progression.

## Documentation
Comprehensive documentation is compiled in this README.md, covering setup instructions, usage examples, and an in-depth analysis of architectural decisions, with emphasis on the implementation and impact of chosen design patterns and logging strategy.

## Video Showcase
A video has been created to showcase the features and functionalities of this calculator application. You can watch the video [here](https://drive.google.com/file/d/1CbPSNE6mGL0gKOO-3BM_NZKL_s6TTEIS/view?usp=drive_link).

## Cloning the Repository
To clone the repository, use the following command:
```bash
git clone https://github.com/your-username/calculator-app.git