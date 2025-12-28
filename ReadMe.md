# Folder Item Display

Tiny utility that recursively prints every file and subfolder under a root and keeps a running total. Handy when you want a quick inventory of an external drive without firing up Explorer/Finder.

## How it works

`file_reader.py` walks the directory tree with `os.listdir`, prints the path of each item, and accumulates counters for files and folders. To keep the walkthrough quick on large drives, the sample only processes every other folder in the root (`if index % 2 == 0`). You can remove that guard if you prefer a full traversal.

## Running the script

1. Edit `root_folder` inside `main()` so it points at the directory you want to inspect (e.g., `r"C:\\"`).
2. From the repo:

   ```bash
   python file_reader.py
   ```

3. Watch the console output for file/folder listings followed by a summary total.

## Customization ideas

- Comment out the `if index % 2 == 0` block to iterate through every folder.
- Replace the `print` statements with writes to a CSV if you need a record you can filter later.
- Wrap the counters in a lightweight CLI argument parser (`argparse`) if you want to pass the root path at runtime.

## Troubleshooting

If you hit `PermissionError` or `OSError` messages, the script will print the failing folder and continue. Run the terminal as an administrator (Windows) or with elevated permissions (macOS/Linux) when scanning system directories.
