# Contributing Guide
## Branching
The `main` branch is protected. To contribute:
1. Checkout a branch off of main:
- `git pull`
- `git checkout -b name-of-branch`
2. Make your changes and write them to a commit
- Stage changes in VSCode
or
- `git status`
- `git add <file>`
- `git commit -m 'A short description of changes'`
3. Push your changes to remote
- `git push --set-upstream origin <name-of-branch>`

## Make a merge request for your changes
1. Try to get some eyes on your merge request before merging
2. If there are multiple commits, squash them into one
3. Merge into the `main` branch
