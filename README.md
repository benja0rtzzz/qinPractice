# qinPractice

## 🧱 Design Pattern Used:

### 🎨 Decorator Pattern
> **Purpose:** Add behavior to an object **dynamically**, without modifying its code.

- Wraps an object with a decorator class that adds features.
- Follows the same interface as the original object.
- Useful for layering functionalities (e.g., logging, formatting, UI styling).

**Example:**

```python
coffee = Sugar(Milk(BasicCoffee()))
print(coffee.cost())
```

## Practice 🐯

> Make a **"Qin"-like** model with different types of meal decorators.
> Each combo has it's limits on how many decorators you can implement.
