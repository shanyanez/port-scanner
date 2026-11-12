# Port Scanner

A tiny port scanner for your own machine, written in plain Python with no extra installs.

## What it does

A lightweight port scanner for localhost. It attempts a TCP connection on each port in a given range and lists the ones that accept it, so you can see which services are running on your machine.

It only scans `127.0.0.1` (your own machine) on purpose.

## How to run it

```
python scanner.py              # checks ports 1 to 1024
python scanner.py 8000 9000    # checks ports 8000 to 9000
```

Example output:

```
Checking ports 8000 to 9000 on this computer...
   8080  open  (http-alt)
1 open port(s) found.
```

## How it works

1. For each port, it tries to open a connection and waits a fraction of a second.
2. If the connection works, a program is listening there, so the port is "open".
3. It checks many ports at the same time, so a thousand ports take about a second.
4. For each open port, it looks up the service that normally uses that number.

## Ideas for later

- Save the results to a file
- Show how long the scan took
- Compare today's scan with yesterday's and point out what changed
