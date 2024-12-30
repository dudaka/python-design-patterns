# Abstract Factory

- The abstract factory design patten is a creational DP that provides an interface for creating families of realetd or dependent objects without specifying their concrete classes.

- It separates the process of creating objects from the actual implementation of those objects, allowing for greater flexibility and ease of modification.

- It is often used when a system should be independent of how its products are created, composed, and represented.

- It is similar to the FM only that it creates families/groups of objects instead of a single object like FM.

## Use cases

- GUI toolkits: to create widgets for different platforms (Windows, Mac, Linux).
  The factory creates the appropriate widget based on the platform it is running on, allowing the same codebase to be used across different patforms.

- Game Engines: To create objects such as characters, weapons, and levels. The factory creates objects based on the game's settings, allowing the same codebase to be used for different types of games.

- Database Connections: Applications that need to connect to diffent types of databases use the AF pattern to create the appropriate database connection.
  The factory creates a connection based on the configuration settings, allowing the same codebase to be used for different types of databases.

- Document Generators: to create different types of document (PDF, Word, HTML) based on the requirements of the client. The factory creates the appropriate document based on the client's needs, allowing the efficent document generation and customization.

- Automobile Manufacturing: To create different types of vehicles (cars, trucks, buses) on the production lines.
  The factory creates the appropriate vehicle based on the customer's order, allowing for effecient production and customization.

- Payment Gateway: To create different types of payment methods (credit card, debit card, net banking) for different countries.
  The factoy creates the appropriate payment method based on the customer's location, allowing seamless payments across different countries.

- Logging Frameworks: To create different types of loggers (console, file, database) based on the configuration settings.
  The allows the same codebase to be used for different types of logging, depending on the requirements of the application.

- Builders: to create diffent typoes of building (houses, apartments, commercial buildings) based on the requirements of the client.
  The factory creates the appropriate building based on the client's needs, allowing for efficent construction and customization.

## Terminologies

- Abstract Factory

- Concrete Factory

- Abstract Product

- Concrete Product

- Product Family

- Factory Hierarchy: In somce cases, the AF pattern can have a hierarchical structure, where there may be an AF that defines common methods or provides default implementations, and then multiple sub-factories that inherit from the AF and provide specialized implementations for different product families.

- Client: The client is the code or component that uses the AF patterns. It interacts with the AF and the abstract product classes to create and work with the products. The client code remains unaware of the specific concrete classes or implement details.
