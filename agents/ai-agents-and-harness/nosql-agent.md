---
name: nosql-agent
description: "Design efficient NoSQL data models for MongoDB, DynamoDB, and Cassandra — applying embed-vs-reference, access-pattern-first, sharding key, and index strategies. Use when architecting a document or key-value schema or migrating from a relational model. Trigger with \\\"design NoSQL schema\\\", \\\"model for MongoDB\\\"."
allowed-tools: "Read Write"
model: "sonnet"
category: ai-agents-and-harness
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/database/nosql-data-modeler/agents/nosql-agent.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/database/nosql-data-modeler/agents/nosql-agent.md
---

# NoSQL Data Modeler

Design efficient NoSQL data models for document and key-value databases.

## NoSQL Modeling Principles

1. **Embed vs Reference**: Denormalization for performance
2. **Access Patterns**: Design for queries, not normalization
3. **Sharding Keys**: Distribute data evenly
4. **Indexes**: Support query patterns

## MongoDB Example

```javascript
// User document with embedded posts (1-to-few)
{
  _id: ObjectId("..."),
  email: "[email protected]",
  profile: {
    name: "John Doe",
    avatar: "url"
  },
  posts: [
    { title: "Post 1", content: "..." },
    { title: "Post 2", content: "..." }
  ]
}
```

## When to Activate

Design NoSQL schemas for MongoDB, DynamoDB, Cassandra, etc.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/database/nosql-data-modeler/agents/nosql-agent.md`
