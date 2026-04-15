# DIAGRAM 01 — OPERATIONAL FLOW

```mermaid
flowchart TD
    A[Operator / Builder] --> B{What do you want to do?}

    B --> C[sdt new]
    B --> D[sdt baseline]
    B --> E[sdt doctor]

    C --> F[Create new repo path]
    F --> G[Apply Operator Floor]
    F --> H[Apply Product Truth Floor]
    G --> I[Write core files]
    H --> I
    I --> J[Optional git commit]
    J --> K[Repo ready for human / AI use]

    D --> L{Report only?}
    L -->|Yes| M[Generate SDT baseline gap report]
    L -->|No| N[Apply missing Operator Floor files]
    L -->|No| O[Apply missing Product Truth Floor files]
    N --> P[Write baseline gap report]
    O --> P
    P --> Q[Optional git commit]
    Q --> R[Existing repo becomes clearer / safer]

    E --> S[Check required SDT floor files]
    S --> T{All present?}
    T -->|Yes| U[PASS]
    T -->|No| V[Show missing files]

