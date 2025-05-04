# Dataclass and Dictionary Speed/Memory Benchmark (also added classic classes and named tuples)

This benchmark compares the times and memory usage of creating and accessing 1 million objects using:
- Dataclasses with and without `__slots__` and Dictionaries


## Summary Table (objects creation):

| Type                         | Operation  | Time [s]         | RSS Memory Increase [MB] |
|------------------------------|------------|------------------|--------------------------|
| Dataclass (no slots)         | Creation   | 0.6954           | 161.13                   |
| Dataclass (with slots)       | Creation   | 0.4910           | 53.88                    |
| Classic classes              | Creation   | 0.7026           | 161.125                  |
| Classic classes (with slots) | Creation   | 0.4904           | 53.875                   |
| Dictionaries                 | Creation   | 0.2464           | 239.00                   |
| Namedtuples                  | Creation   | 0.6000           | 69.00                    |



## Summary Table (objects access):

| Type                          | Operation    | Time [s]         | RSS Memory Increase [MB] |
|-------------------------------|--------------|------------------|-------------------------|
| Dataclass (no slots)          | Access       | 0.0607           | -                       |
| Dataclass (with slots)        | Access       | 0.0585           | -                       |
| Classic classes               | Access       | 0.0810           | -                       |
| Classic classes (with slots)  | Access       | 0.0607           | -                       |
| Dictionaries                  | Access       | 0.0614           | -                       |
| Namedtuples                   | Access       | 0.0596           | -                       |

<br>

#### Practical Guidance
```
General dataclass notes:
 - Despite dataclass being designed for clarity and structure, the plain version without slots is the least efficient in high-scale environments.
 - Accessing attributes (obj.attr) on a dataclass is typically faster than dictionary key access (dict["key"]), because attribute access is optimized at the C level.


Use @dataclass(slots=True) for:
    Any high-scale, performance-sensitive case (e.g., simulations, large data buffers).
    When memory matters more than creation speed (e.g., in data-intensive tasks or embedded systems).
    Also, as advantage you can remember about slightly faster access performance.
     * Best for performance-sensitive applications with many instances.

Use plain @dataclass when:
    You want readable, structured code and are only dealing with thousands (not millions) of objects.
     * Great for structured data, with optional type hints and built-in methods.

Use dict when:
    You need maximum flexibility or serialization compatibility, and memory use is not critical.
        Serialization: Dictionaries work more naturally with JSON or similar formats.
    Also, you may consider dictinaries when raw creation speed matters and memory use is not concern.
    Dictionaries are faster for dynamic operations like adding/removing fields or iterating keys/values.
     * Great for flexibility, not ideal when managing millions of objects in memory.
```

#### 🧠 Big Picture Comparison
| Type                   | Creation Time | Memory Usage    | Access Speed | Mutability     | Notes                                      |
|------------------------|----------------|------------------|----------------|----------------|--------------------------------------------|
| `dict`                | 🟢 Fastest     | 🔴 Worst        | 🟡 OK         | ✅ Mutable     | Dynamic, but heavy                         |
| `dataclass`           | 🔴 Slowest     | 🟠 High         | 🟢 Fast       | ✅ Mutable     | Structured but bulky                       |
| `dataclass (slots)`   | 🟡 Medium      | 🟢 Best         | 🟢 Fastest    | ✅ Mutable     | Best balance                               |
| `classic class`       | 🔴 Slow        | 🟠 High         | 🟡 Medium     | ✅ Mutable     | Manual + verbose                           |
| `classic + __slots__` | 🟡 Medium      | 🟢 Low          | 🟢 Fast       | ✅ Mutable     | Lean but no auto-features                  |
| `namedtuple`          | 🟡 Medium      | 🟢 Excellent    | 🟢 Fast       | ❌ Immutable   | Great for safe, fixed-structure data       |


#### Why is Dataclass without slots slower and uses more memory?
```
    Instance creation overhead:
        Regular dataclasses have a per-instance __dict__.
        Each field assignment is effectively a setattr into that __dict__.
        They also generate methods like __init__, __repr__, __eq__, which adds a small cost.

    Higher memory footprint:
        You get the overhead of the __dict__, plus Python’s normal object metadata.
        Memory scales poorly with large instance counts (millions).

    Slower due to Python-level field management:
        Even compared to dictionaries, the extra indirection through method-generated __init__ can cause slower creation.
```

#### Python Dictionaries: Strengths and Weaknesses (Performance)
```
When to Use dict (Performance Pros)
    Scenario	Why dict is a Good Fit
    Fast Creation	Dicts are fast to create — simple memory allocation with keys/values.
    Dynamic Structures	You can add/remove keys freely without pre-defining structure.
    Fast Key Lookup	Python dictionaries use a highly optimized hash table implementation with O(1) average-case access time.
    Serialization (e.g., JSON)	Dicts are natively supported by json, yaml, etc., which makes them easy to transmit or log.
    Variable Field Sets	Useful when not all objects have the same fields — e.g., sparse or irregular data.

Best use cases:
    Caching (e.g., memoization).
    Configurations or settings.
    JSON-like API results or parsed data.
    Prototypes where structure is not finalized.
    Lookup tables.

❌ When Not to Use dict (Performance Cons)
    Scenario	Why dict is a Bad Fit
    Memory-Constrained Environments	Each dictionary instance has overhead: separate hash table, pointers, and object headers — very memory heavy.
    Fixed Structure	If every item has the same keys, a dataclass or namedtuple is more memory- and type-efficient.
    High Object Count	With millions of objects, the memory cost adds up fast — ~10x more than using __slots__.
    Attribute Access in Tight Loops	dict["key"] is slower than obj.key due to hash lookup + bounds checking.
    Code Maintainability	Mistyped keys (dict["nmae"]) don't raise errors immediately — harder to debug and refactor.

Memory Efficiency Notes
    A single dict uses ~240–300 bytes minimum, even for a few keys.
    Slotted dataclass with same data may use ~50–80 bytes.
    Dictionaries grow in size dynamically (resizing hash table), leading to fragmentation and memory spikes.

Quick Summary: When to Use dict vs Alternatives
    Use Case	Recommended
    Few instances, need flexibility	✅ Use dict
    Many instances (10⁶+), fixed fields	❌ Avoid dict, ✅ Use dataclass(slots=True)
    Need speed in tight loops	❌ Avoid dict, ✅ Use dataclass or namedtuple
    JSON round-trips or schema-less data	✅ Use dict
    Memory-constrained workloads	❌ Avoid dict, ✅ Use slotted classes
```