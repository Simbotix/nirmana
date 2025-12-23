# Requirements

This folder contains all requirements and setup documentation for the Nirmaha project.

## Documents

| File | Purpose |
|------|---------|
| [BUSINESS-REQUIREMENTS.md](./BUSINESS-REQUIREMENTS.md) | Core business logic, DocType specs, workflows |
| [STAGING-SETUP.md](./STAGING-SETUP.md) | How to setup staging site on press.appz.studio |

## For Claude

When working on this project:

1. **Read BUSINESS-REQUIREMENTS.md first** - Contains all DocType specifications, field definitions, and business logic
2. **Follow the workflows** - The rental flow diagram shows the correct state transitions
3. **Use the pricing logic** - Auto-select best rate for customers
4. **Implement all notifications** - SMS templates are defined, use MSG91
5. **Respect permissions** - Follow the permission matrix for roles

## Adding New Requirements

When sister provides new requirements:
1. Add to BUSINESS-REQUIREMENTS.md under appropriate section
2. Update DocType specs if schema changes
3. Add new SMS templates if notifications needed
4. Update this README if adding new docs
