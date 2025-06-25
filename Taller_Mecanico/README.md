# README for Taller Mecanico Project

## Overview
The Taller Mecanico project is a comprehensive system designed to manage various aspects of a mechanical workshop. It includes functionalities for managing clients, vehicles, mechanics, and now incorporates features for "Ficha Tecnica" (Technical Records) and "Facturacion" (Billing).

## Project Structure
The project consists of the following files:

- **taller_mecanico.py**: Contains the main application logic, managing database connections, user interactions, and functionalities related to clients, vehicles, mechanics, and the new features for "Ficha Tecnica" and "Facturacion".

- **taller_mecanico.sql**: Contains SQL commands to create the database and its tables, defining the structure for "Clientes", "Vehiculos", "Mecanicos", "Repuestos", "Reparaciones", and now includes tables for "Ficha Tecnica" and "Facturacion".

- **taller_mecanico.mmd**: A model diagram that visually represents the database schema, including entities and their relationships, which will be updated to reflect the new "Ficha Tecnica" and "Facturacion" entities.

- **DER_Taller_Mecanico.png**: An image representation of the database schema, generated from the .mmd file.

- **README.md**: Documentation for the project, including setup instructions, usage, and other relevant information.

## Features
1. **Client Management**: Add, update, view, and delete client records.
2. **Vehicle Management**: Add, update, view, and delete vehicle records.
3. **Mechanic Management**: Add, update, view, and delete mechanic records.
4. **Ficha Tecnica**: 
   - Create new technical records.
   - Modify existing records for vehicles, clients, or mechanics.
   - Consult existing technical records.
5. **Facturacion**: 
   - Create new billing records.
   - Annul existing billing records.
   - Consult existing billing records.

## Setup Instructions
1. Ensure you have Python and MySQL installed on your machine.
2. Create a MySQL database using the commands in `taller_mecanico.sql`.
3. Update the database connection parameters in `taller_mecanico.py` as needed.
4. Run the application using Python.

## Usage
- Launch the application by running `taller_mecanico.py`.
- Follow the on-screen menu to navigate through the various functionalities.

## Future Enhancements
- Additional features for reporting and analytics.
- User authentication and authorization.
- Improved user interface for better user experience.

## License
This project is licensed under the MIT License.