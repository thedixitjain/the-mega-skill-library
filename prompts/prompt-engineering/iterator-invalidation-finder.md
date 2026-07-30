---
name: iterator-invalidation-finder
description: "Finds iterator invalidation bugs"
category: prompt-engineering
source_repo: trailofbits/skills
source_path: "plugins/c-review/prompts/general/iterator-invalidation-finder.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/c-review/prompts/general/iterator-invalidation-finder.md
---


**Finding ID Prefix:** `ITER` (e.g., ITER-001, ITER-002)

**Bug Patterns to Find:**

1. **Modification During Iteration**
   - Inserting into vector during iteration
   - Erasing from container during range-for
   - Resizing container while iterating

2. **Invalidated Iterator Use**
   - Using iterator after container modification
   - Storing iterator across modifying operations
   - End iterator cached and invalidated

3. **Pointer/Reference Invalidation**
   - Pointer to vector element after push_back
   - Reference to map value after insert
   - String char* after modification

4. **Range-Based For Issues**
   - Modifying container in range-for body
   - Breaking out but iterator still stored

**Common False Positives to Avoid:**

- **Iterator reassigned:** If iterator is reassigned after modifying operation (e.g., `it = vec.erase(it)`)
- **Non-invalidating operations:** Operations like `std::map::insert` don't invalidate existing iterators
- **Reserve before loop:** `vector::reserve` before iteration prevents reallocation invalidation
- **Index-based access:** Using indices instead of iterators doesn't have invalidation issues
- **Copy iteration:** Iterating over copy while modifying original is safe

**Search Patterns:**
```
for\s*\(.*begin\(\)|for\s*\(.*:\s*
\.erase\(|\.insert\(|\.push_back\(|\.clear\(
\.resize\(|\.reserve\(
iterator|::iterator|auto.*=.*begin
```

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/c-review/prompts/general/iterator-invalidation-finder.md`
