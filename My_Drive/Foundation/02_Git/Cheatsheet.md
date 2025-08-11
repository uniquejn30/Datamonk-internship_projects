# 📘 Git Command Reference Guide

This is a quick-reference guide for essential Git commands — covering configuration, working with repositories, branching, merging, stashing, history, and collaboration.

---

## 🔧 Git Configuration

| **Command** | **Description** |
| --- | --- |
| `git config --global user.name "<name>"` | Set your Git username for all repositories. |
| `git config --global user.email "<email>"` | Set your email address for commits. |

---

## 📁 Repository Setup

| **Command** | **Description** |
| --- | --- |
| `git init` | Initialize a new Git repository locally. |
| `git clone <url>` | Clone a remote repository to your system. |

---

## 📌 Staging and Committing

| **Command** | **Description** |
| --- | --- |
| `git status` | Show the working directory status. |
| `git add <file>` / `git add .` | Stage file(s) for the next commit. |
| `git commit -m "<message>"` | Commit staged changes with a message. |
| `git diff` | Show unstaged changes. |
| `git diff --staged` | Show staged differences. |
| `git reset [file]` | Unstage a file (keep changes). |
| `git rm <file>` | Remove a file and stage the deletion. |
| `git mv <old> <new>` | Rename a file and stage the change. |

---

## 🌿 Branching & Merging

| **Command** | **Description** |
| --- | --- |
| `git branch <name>` | Create a new branch. |
| `git branch` / `git branch -a` | List local or all branches. |
| `git checkout <branch>` | Switch to an existing branch. |
| `git checkout -b <branch>` | Create and switch to a new branch. |
| `git merge <branch>` | Merge another branch into the current one. |
| `git rebase <branch>` | Reapply commits on top of another base branch. |
| `git log` | View the commit history. |
| `git log --stat -M` | Show file rename/delete stats in history. |
| `git show <SHA>` | Show details of a specific commit. |
| `git log branchB..branchA` | Commits in branchA not in branchB. |
| `git diff branchB...branchA` | View code differences between two branches. |

---

## 🌐 Remote Collaboration

| **Command** | **Description** |
| --- | --- |
| `git remote add <alias> <url>` | Add a remote repository. |
| `git fetch <alias>` | Download changes from a remote repo. |
| `git pull` | Fetch and merge from remote. |
| `git push <alias> <branch>` | Push your branch to remote. |

---

## 🧰 Stashing Changes

| **Command** | **Description** |
| --- | --- |
| `git stash` | Temporarily save your changes. |
| `git stash list` | List all stashed changes. |
| `git stash pop` / `git stash apply` | Reapply (and optionally remove) stash. |
| `git stash drop` / `git stash clear` | Delete specific/all stashed entries. |

---

## 💣 Undoing & Resetting

| **Command** | **Description** |
| --- | --- |
| `git reset --hard <commit>` | Reset to a specific commit and discard changes. |

---

## 🛠️ Examples & Notes

These commands form the core of most Git workflows. Start with the basics, then explore more advanced workflows as you get comfortable.

---

### 🚀 Start a New Repository

```bash
git init
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
