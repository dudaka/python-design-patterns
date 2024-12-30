# Factory Method

## Introduction

- The Factory Method is a creational design pattern that provides an interface for creating objects but allows subclasses to decide which class instantiate.
  It is a type of OOP pattern that promotes loose coupliung and adheres to the 'open-closed principle', which states that classes should be open for extension but closed for modification.

- The Factory Method pattern is useful when you want to delegate the responsibility of object creation to subclasses, rather than having the base class directly create objects. This allows for greater flexibility and extensibility, as new subclasses can be added without modifying the existing code.

- By using the Factory Method pattern, you can encapsulate the object creation logic within subclasses, providing a consistent way to create objects while allowing for flexibility and customization.
  This pattern is often used in frameworks and libaries where the exact object type needed is determined by the client.

## Use Cases

- Document Processing: Text editors or document processing software often use the Factory Method pattern to create different document types, such as Word documents, PDFs, or HTML files.

- Logging frameworks: To create different loggers based on the desired output format, such as console loggers, file loggers, database loggers.

- Database Connectivity: To create specific database connection objects for different database vendors, like MySQL, PostgreSQL, or Oracle.

- GUI Component Libararies: To create various UI components, such as buttons, text fields, or checkboxes, based on the platform-specific requirements.

- Object Serialization: To create serializers for different data formats, such as JSON, XML, or binary formats.

- Payment Gateways: To create instances of different payment gateway classes based on the selected provider, such as Paypal, Stripe, or Braintree.

- Maze Generation Algorithms: To create different maze object instances with various structures, such as simple mazes, randomized mazes, or mazes with specific patterns.

- Vehicle Manufacturing: To create different types of vehicles, such as cars, trrucks, motorcycles, or bycicles, based on customer requirements.

- Plugin Systems: To create instances of plugin objects based on the user's selection or dynamically loaded plugins.

- Game development: To create different game objects, such as characters, weapons, or power-ups, based on game logic or user input.

## Terminologies

- Product: It refers to the abstract base class or interface that defines the common methods and properties that all products (objects) created by the factory will have.

- Concrete Product: These are the concrete classes that implements the product interface. Each concrete product represents a specific variation or type of object that can be created by the factory.

- Creator: The creator is the abstract base class or interface that declares the factory method. It provides the contract for creating objects but doesn't sepcify the concrete class. It may also contain other methods that operate on the products.

- Concrete Creator: These are the concrete classes that inherit from the creator and implement the factory method. Each concrete creator is responsible for instantiating a specific concrete product class.

- Factory Method: It is an abstract method desclared in the creator that defines the contract for object creation. Subclasses of the creator implement this method to create instances of concrete production classes. The factory method is responsible for deciding which subclass of the product to instantiate.

- Client: The client is the code that uses the factory method to create objects. It interacts with the creator through the abstract base class or interface, without being aware of the concrete classes being instantiated.

## When Should I Use It

- Object creation: When you want to encapsulate the object creation logic in a separate component or class. The FM pattern allows you to delegate the responsibility of object creation to subclasses or sepcialized factory classes.

- Decoupling: When you want to decouple the client code from the specific classes it creates. By using the Factory Method pattern, the client code interacts with the abstract factory interface and is not directly dependent on concrete implementations.

- Extensibility: When you need to easily add or modify the types of objects created without modifying existing client code. The FM pattern provides an extension point by allowing the addition of new subclasses or factory classes without impacting existing code.

- Variation in object creation: When there are multiple variations or configurations of objects that need to be created. The FM pattern allows different subclasses or factories to provide specialized implemenations of obehjct creation based on specific criteria or requirements.

- Testing and Mocking: When you want to faciliate unit testing and mocking of objects. By using the FM pattern, you can create mock or stub objects by implementing a factory class that returns predetermined objects during testing.

## Advantages and Disavatages

- Encapsulation:
