Section 3: Debugging the Factory & Strategy Flow

In this part of the lab, I used VS Code’s debugger with Poetry’s Python interpreter to trace the execution flow of sample.py and the operator selection logic.

Call Stack Debugging

I set breakpoints in:

sample.py at the line:

output = run_anonymizer("initial")


anonymizer_engine.py inside anonymize()

engine_base.py inside _operate() / __operate_on_text()

operators_factory.py at the line:

operator = operators_by_type.get(operator_name)


Then I ran the program in debug mode, stepping through the execution until the debugger stopped at this crucial factory selection point.

At this breakpoint, the VARIABLES window clearly showed:

operator_name = 'initial'

operators_by_type contained a dictionary of available operators

self referencing the factory instance

A screenshot of this (call-stack.png) has been added to the repository root.

Number of Conditional Branches Used

How many if/elif statements are used to select the operator?

Answer: 0

There is no conditional branching involved in selecting the operator implementation.

Data Structure Used

What Python data structure is used to select operators?

Answer: A dictionary (hash map)

Example observed during debugging:

operators_by_type = {
    'custom': Custom,
    'encrypt': Encrypt,
    'hash': Hash,
    'keep': Keep,
    'mask': Mask,
    'redact': Redact,
    'replace': Replace,
    'initial': Initial,
}


The keys are operator names (strings),
and the values are the corresponding operator classes.

Demonstration of the Strategy Design Pattern

This implementation demonstrates the Strategy Pattern because:

Each operator is a separate strategy class implementing a shared interface (Operator)

The behavior is chosen at runtime by selecting the correct strategy from a dictionary

No code needs to be modified when adding a new operator — only the dictionary needs extended
This adheres to the Open-Closed Principle (open for extension, closed for modification)

Instead of a giant if/else or switch tree:

if operator == "hash": ...
elif operator == "mask": ...
elif operator == "redact": ...


The factory simply does:

operator = operators_by_type.get(operator_name)


This is dynamic dispatch and strategy injection.

Screenshot

The file call-stack.png included in this repository captures:

The paused execution at operator selection

The call stack showing the full invocation path

The VARIABLES panel displaying operator_name and the operator dictionary