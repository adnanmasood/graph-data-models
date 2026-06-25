# EAV and Network Ancestry

Run with `make demo-eav`.

SQLite stores claim attributes as rows, then pivots them back into a typed claim. A recursive CTE demonstrates network-model ancestry.

Elegant: sparse attributes are easy to add. Awkward: validation is weak and business queries require many joins or pivots.
