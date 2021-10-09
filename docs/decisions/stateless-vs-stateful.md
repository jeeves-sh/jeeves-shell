---
title: Use stateful workflow instead of stateless
number: 1
status: accepted
---

## Stateful

```shell
# Set the task I am working on
jeeves task start CBS-123

# Find the task I am working on right now
jeeves task current

# Split the task
jeeves task split [CBS-123]

# Create a prerequisite to current task
jeeves task create prerequisite --to CBS-123

# Create a task to follow after current task
jeeves task create next

# Send task to review
jeeves task to review

# Mark task as done
jeeves task to done

# What next task to work on from my board or the backlog?
jeeves task next

jeeves task link CBS-3464 split-to CBS-3467
```
