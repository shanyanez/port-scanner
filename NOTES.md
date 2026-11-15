# Notes

A running log of what has changed in this project, and what could come next.

## Done

- 2026-11-13: The scanner now prints how long the scan took, as the last line of the output.
- 2026-11-15: Every scan now saves its results to last_scan.txt (date and range on the first line, then one open port per line). The file is listed in .gitignore so it never gets committed.

## Next ideas

- Compare today's scan with the previous one (read last_scan.txt before overwriting it) and point out what changed
- Add a few simple tests (for example, that bad arguments are rejected)
- Reword the comments in scanner.py that describe ports as "doors", so they match the README's tone
