# EXAMPLE BASELINE BEFORE / AFTER

## Purpose
Show what a messy repo looks like before S.D.T. and what it looks like after baseline.

## Before baseline
A typical repo before S.D.T. might look like this:

```text
example-old-repo/
├── README.md
├── script.sh
├── notes.txt
└── random-output.json

Typical problems:

no clear current truth
no next-operator path
no product statement
no distinction between current reality and future plans
no product/system boundary
no standard handoff structure
After baseline

After running sdt baseline, the repo gains the minimum SDT floors:

example-old-repo/
├── .gitignore
├── README.md
├── WHAT_IS_REAL_NOW.md
├── PROJECT_STATE.md
└── docs/
    ├── operator/
    │   ├── ZERO_CONTEXT_HANDOFF_CHECKLIST.md
    │   ├── COLD_START_RECOVERY.md
    │   └── NEXT_OPERATOR_PACKET_TEMPLATE.md
    ├── product/
    │   ├── PRODUCT_STATEMENT.md
    │   ├── WHAT_THIS_PRODUCT_IS.md
    │   ├── CURRENT_VS_PLANNED.md
    │   └── PRODUCT_SYSTEM_BOUNDARY.md
    └── status/
        └── SDT_BASELINE_GAP_REPORT.md
What changed

S.D.T. did not magically understand the whole repo.

It did:

scaffold the missing operator floor
scaffold the missing product truth floor
create a baseline gap report
make missing truth obvious
make the repo easier to continue safely
Example command
sdt baseline   --path /path/to/existing-repo   --product-name "Existing Product"   --product-statement "Existing Product is a product for X."
Report-only example
sdt baseline   --path /path/to/existing-repo   --product-name "Existing Product"   --product-statement "Existing Product is a product for X."   --report-only

