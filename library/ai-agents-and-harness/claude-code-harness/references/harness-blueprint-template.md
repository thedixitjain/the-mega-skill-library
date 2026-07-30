# Harness Blueprint Template

Use this template when the user wants a formal harness design.

## 1. Goal and delegation boundary

- what job the user is delegating
- what remains outside the harness
- what would count as success

## 2. Harness layers

- interface or host layer
- request assembly layer
- execution loop layer
- tool runtime layer
- memory/context layer
- transcript/recovery layer
- extension layer

## 3. Request assembly

- instruction sources
- system context
- user context
- tool exposure
- message normalization
- model request boundary

## 4. Turn loop

- loop stages
- stop conditions
- retry logic
- escalation points
- compaction triggers

## 5. Tool runtime

- tools and capabilities
- permission tiers
- verification strategy
- error handling

## 6. Memory and context

- turn context
- retrieved context
- working memory
- durable memory
- compaction or summarization

## 7. Permissions and safety

- approval points
- destructive action policy
- isolation or sandbox assumptions
- auditability

## 8. Transcript and recovery

- what is persisted
- what is resumable
- what gets rewritten or compacted
- how partial work is recovered

## 9. Extension surfaces

- plugins
- subagents
- MCP or external systems
- feature gates

## 10. Build order

- v1 harness core
- next control layers
- later extension layers
- validation milestones

