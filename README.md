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

### Advantages and Disadvantages
# python-design-patterns
