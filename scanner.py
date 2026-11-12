"""
A tiny port scanner for your own machine.

A "port" is a numbered door on a computer. Programs that talk over the
network (a web server, a database, a game) each listen behind one door.
This script knocks on a range of doors on *this* computer and tells you
which ones have something answering.

Run it:
    python scanner.py              # checks ports 1 to 1024
    python scanner.py 8000 9000    # checks ports 8000 to 9000
"""

import socket
import sys
from concurrent.futures import ThreadPoolExecutor

# We only ever scan this computer. Scanning machines you don't own
# is rude at best and illegal at worst, so the target is not an option.
HOST = "127.0.0.1"

# How long to wait at each door before deciding nobody is home.
TIMEOUT_SECONDS = 0.3


def is_open(port):
    """Knock on one port. True means a program answered."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as knock:
        knock.settimeout(TIMEOUT_SECONDS)
        # connect_ex returns 0 when the connection worked,
        # and an error number when it didn't. No exceptions to catch.
        return knock.connect_ex((HOST, port)) == 0


def guess_service(port):
    """Look up what usually lives on this port (80 is 'http', and so on)."""
    try:
        return socket.getservbyport(port)
    except OSError:
        return "unknown"


def scan(first, last):
    """Check every port from first to last and return the open ones."""
    ports = range(first, last + 1)
    # Knocking on doors is mostly waiting, so we do many at once.
    with ThreadPoolExecutor(max_workers=100) as pool:
        answers = pool.map(is_open, ports)
    return [port for port, answered in zip(ports, answers) if answered]


def read_range(args):
    """Turn the command-line arguments into a (first, last) pair of ports."""
    if not args:
        return 1, 1024
    if len(args) == 2 and all(a.isdigit() for a in args):
        first, last = int(args[0]), int(args[1])
        if 1 <= first <= last <= 65535:
            return first, last
    sys.exit("Usage: python scanner.py [first_port last_port]   (ports are 1 to 65535)")


def main():
    first, last = read_range(sys.argv[1:])
    print(f"Checking ports {first} to {last} on this computer...")

    open_ports = scan(first, last)

    if not open_ports:
        print("Nothing is listening in that range.")
        return
    for port in open_ports:
        print(f"  {port:>5}  open  ({guess_service(port)})")
    print(f"{len(open_ports)} open port(s) found.")


if __name__ == "__main__":
    main()
