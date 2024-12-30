# Creational Design Patterns

## Builder

### Use Cases

- Document Creation: To generate documents, such as PDF or HTML files. It can be used to created different document types and styles.
- GUI creation: To create complex UI with different layout options and controls.
- Meal ordering: To create comple meal orders with different options, such as toppings, sides, and beverages.
- Car manufacturing: To create cars with different options and configuration, such as engine size, color, and features.
- Website creation: To create different types of web pages with different layouts and content.
- Game level design: To create different levels with differrent enemies, obtacles, and power-ups.
- Database query: To generate SQL queries of different parameters, options and commands.

### Terminologies

- Product:

  - The complex object being constructed.
  - It has multiple parts and requires a step-by-step process to construct.
  - Example: query, game, network, website, etc.

- Builder:

  - An abstract interface that defines the steps required to build an object.
  - It declares methods for creating and assembling parts of the product.

- Concrete Builder:

  - A concrete implementation of the Builder interface that provides an implementation for each of the Builder methods.
  - It defines and keeps track of the represenation it creates.

- Director:

  - A class that controls the construction process.
  - It knows which Builder to use and in what order to call the Builder methods to create a product.

- Client:
  - A class or module that uses the Builder pattern to create the product.
  - It is responsible for creating the Director object and configurating it with the appropriate builder.
  - The client can also work directly with the Builder if it needs more control over the construction process.

### When Should I Use It

- When you need to create complex objects that have multiple parts or properties with different values or combinations.
- When the construction process involves multiple steps or dependences that need to be resolved or configured dynamically.
- When you want to isolate the construction code from the rest of the codebase or clients, to improve modularity and maintainability.
- When you want to support multipe represenations or variants of the same object, without duplicating the construction logic.
- When you want to create objects using a fluent or readable syntax that allows you to chain multiple method calls and set diffent options or properties.

### Advantages and Disadvantages

- Advantages

  - Decouples an abstractionn from its implemenation so that the two can vary independently.
  - Improves extensibility by allowing new implementations to be added easily.
  - Reduces the number of subclasses that need to be created for both the abstraction and the implementation.
  - Provides a way to switch between different implementations at runtime.
  - Increases the flexibility and resusability of the code.

- Disadvantages
  - Increases the overall complexity of the code by introducing a new layer of abstraction.
  - Can make the code more difficult to understand and maintain due the added complexity.
  - Can lead to a performance overhead due to the extra layer of indirection.
  - Can make the code harder to test because of the added layer of abstraction.
  - It's not always the best solution for all problems, it's important to avaluate if it's the best pattern for the particular problem you're trying to solve.

### Things to Note

- Python provides several ways to define and initialize objects, such as object literals, keyword arguments, and data classes. The Builder pattern may not always be necessary or the best solution for every situation.
- Python allows for optional and default arguments in function and method definitions, which can simplify the Builder interface and implementation. Instead of defining separate methods for each optional parts, you can provide default values or use keyword arguments.
- Python's flexible syntax and dynamic typing can make it easier to create fluent interface for the Builder, where each method returns the Builder object itself. This allows for a more readable and concise construction process.
- Python's support for decorators and metaclasses can be used to automatically generate the Builder class or its methods, reducing boilerplate code and improving maintainability.
- Python's dynamic nature can also make it header to enforce type constraints and ensure the consistency or the object being built. You may need to use additional tools or libaries, such as type annotations, type checkers, or schema validators, to ensure the correctness and prevent runtion errors.
