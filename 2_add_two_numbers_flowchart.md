# Add Two Numbers Flowchart

```mermaid
flowchart TD
    A[Start with l1, l2, and carry = 0] --> B[Create dummy result node]
    B --> C[Set current to dummy]
    C --> D{l1 exists OR l2 exists OR carry exists?}
    D -- No --> E[Return dummy.next]
    D -- Yes --> F[Read val1 from l1, or 0 if l1 is empty]
    F --> G[Read val2 from l2, or 0 if l2 is empty]
    G --> H[total = val1 + val2 + carry]
    H --> I[carry = total // 10]
    I --> J[Create new result node with total % 10]
    J --> K[Move current to new node]
    K --> L[Move l1 forward if possible]
    L --> M[Move l2 forward if possible]
    M --> D
```

## Key Idea

The linked lists store digits in reverse order, so the algorithm adds one digit
pair at a time from left to right, carrying any overflow into the next step.
