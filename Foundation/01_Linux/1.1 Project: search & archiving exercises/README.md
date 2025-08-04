## 1. Why Does Linux Offer Multiple Help Systems: `man`, `--help`, and `help`?

Linux provides different tools for getting help, each suited for specific purposes:

- **`man` (manual pages):**  
  Offers in-depth documentation for most **external commands**. Use this when you want comprehensive information including usage, options, and examples.

- **`--help` flag:**  
  Adding `--help` to a command (like `ls --help`) shows a **quick usage summary** directly in the terminal. Great for a fast lookup of command options.

- **`help` command:**  
  Exclusive to **shell built-in commands** such as `cd`, `echo`, `export`. Use `help` to get short descriptions of these commands. This does **not work for external programs**.

> 🔸 **When to use `help` only:**  
When you need information about shell built-ins, `help` is the only valid option. `man` or `--help` won’t usually provide this.

---

## 2. Difference Between `ls | grep ".txt"` and `find . -name "*.txt"`

Both commands aim to find `.txt` files, but they work differently:

- **`ls | grep ".txt"`:**  
  - Filters file names in the **current directory only**.  
  - Simple and fast, but limited.  
  - May not handle special characters or nested folders well.

- **`find . -name "*.txt"`:**  
  - Searches **recursively** through the current directory and all subfolders.  
  - More powerful and flexible for deep searches.  
  - Handles special characters and file paths better.

> ✔️ Use `ls | grep` when working in a known folder.  
> 🔍 Use `find` when you need to explore subdirectories or unknown paths.

---

## 3. Using Piping with `history` to Find Past Commands

You can apply the same filtering logic used with `ps aux | grep` to your command history:

```bash
$ history | grep "ls"
