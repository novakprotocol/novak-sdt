# DIAGRAM 02 — WHAT FILES S.D.T. ADDS

```mermaid
flowchart TD
    A[sdt new or sdt baseline] --> B[Operator Floor]
    A --> C[Product Truth Floor]
    A --> D[Status / Gap Report]

    B --> B1[WHAT_IS_REAL_NOW.md]
    B --> B2[PROJECT_STATE.md]
    B --> B3[ZERO_CONTEXT_HANDOFF_CHECKLIST.md]
    B --> B4[COLD_START_RECOVERY.md]
    B --> B5[NEXT_OPERATOR_PACKET_TEMPLATE.md]

    C --> C1[PRODUCT_STATEMENT.md]
    C --> C2[WHAT_THIS_PRODUCT_IS.md]
    C --> C3[CURRENT_VS_PLANNED.md]
    C --> C4[PRODUCT_SYSTEM_BOUNDARY.md]

    D --> D1[SDT_BASELINE_GAP_REPORT.md]

