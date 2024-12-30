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

### Advantages

- Encapsulation: The FM pattern encapsulates the object creation logic in a separate component or class, proviing a clear separation of responsibilities.
  It promotes a more modular and organized code structure.

- Flexibility and Extensibility: The pattern allows for easy addition or modificatoiopn of object types without modififying existing client code. New subclasses or specialized factory classes can be introduced to create different variations of objects.

- Dependency inversion: The FM pattern promotes dependency inversion by allowing the client code to depend on abstractions (e.g., abstract factories or interfaces) rather than concrete implemenations.
  This enhanced code flexibility and maintainbility.

- Code Reusability: The pattern promotes code resusability by providing a consistent and reusable mechanism for creating objects.
  It avoids duplicating object creation logic throughout the codebase.

- Testing and Mocking: The FM pattern facilitates unit testing and mocking. It allows for the creations of mock or stub objects by implementing a factory class that returns predetermined objects during testing.

### Disadvantages

- Complexities: The introduction of multiple factory classes and subclasses can increase the complexity of the codebase, especially when dealing with a large number of object types or variations.
  This can make the code harder to understand and maintain.

- Increased Number of classes: Implementing the FM pattern often requires the creation of additional classes, such as abstract factories and concrete factorties.
  This can lead to an increased number of classes in the codebase, which might add complexity and overhead.

- Indirection: The FM pattern introduces an additional layer of indirection between the client code and the objects being created.
  This can make the code more abstract and require a deeper understanding of the underlying object creation process.

- Runtime overhead: In some cases, using the FM pattern can introduce a slight runtime overhead due to the need for dynamic object creation and the enviroment of additional classes and method calls.

- Tight coupling with Factories: While the client code is decouppled from the specific objects being created, it becomes tightly coupled to the factories or abstract factory interfaces. Changing the factory hierarchy or interfaces might require modifications in the client code as well.

### Things to Notes

- Abstraction: Define an abstract base class or interface that represents the common interface for all products created by the factory.
  This abstraction should declare the factory method that subclasses or specialized factory classes will implement.

- Concrate Implemenatation: Create concrete classes that inherit from the abstract base class or interface. Each concrete class represents a specific product that the factory can create. Implement the factory method in each concrete class to return an instance of the coressponding product.

- Factory Class: Implement a factory that encapsulates the object creation logic.
  The factory class should define the factory method as a static or class method.
  This method should create and return instances of the desired product based on the client's request or specific conditions.

- Client code: Should interact with the factory through the factory method.
  It should depend on the abstraction (abstract base class or interface) and not on the concrete product classes.
  This allows for flexibility and easy subtitution of defferent product type.

- Extensibility: The FM pattern is particularly useful when there is a need to add new product types without modifying existing code.
  To achive this, new concrete classes representing the aditional product types can be createsd, along with correspoding fractory methods in specialized factory classes.

- Dependency Injection: The FM pattern can be combined with the dependency injection prinples to further decouple the client code from the specific factory implementation.
  This allows for easy substitution of different factory implementations at runtime.

- Error handling: Consider how to handle scenarios where the FM cannot create the requested object.
  You can choose to raise an exception, return a default object, or implement a fallback strategy based on the specific requirements of your appllication.

- Naming Conventions: Choose meaningful names for your classes and methods that accurately reflect their purpose and role in the FM pattern.
  The helps improve code readibilty and maintainability.

- Documenation and Comments: Provide clear and concise documentation for your classes, methods, and interfaces. Explain the purpose of each component and the relationships between the.
  Additionally, consider adding comments within the code to clarify any complex or critical sectioos.
