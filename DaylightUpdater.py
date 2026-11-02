#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Safe Debian APT maintenance planner: preview by default."""
import argparse
import os
import subprocess
import sys

ACTIONS = {
    "update": ("apt-get", "update"),
    "upgrade": ("apt-get", "upgrade"),
    "full-upgrade": ("apt-get", "full-upgrade"),
    "autoclean": ("apt-get", "autoclean"),
    "autoremove": ("apt-get", "autoremove"),
}

def plan(action: str, apply: bool = False) -> tuple[str, ...]:
    if action not in ACTIONS:
        raise ValueError("Unknown APT action")
    cmd = ACTIONS[action]
    if not apply:
        if action == "update":
            return ("apt-get", "--version")
        return ("apt-get", "--simulate", cmd[-1])
    return cmd

def execute(action: str, apply: bool = False, runner=subprocess.run) -> int:
    if apply and os.geteuid() != 0:
        raise PermissionError("Apply mode requires root on a Debian-based system")
    result = runner(plan(action, apply=apply), check=False)
    return result.returncode

def cli(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", nargs="?", choices=tuple(ACTIONS))
    parser.add_argument("--apply", action="store_true", help="Execute selected APT action")
    parser.add_argument("--yes", action="store_true", help="Confirm non-interactive execution")
    args = parser.parse_args(argv)
    if args.action is None:
        if args.apply or args.yes:
            parser.error("Specify an action with --apply")
        return gui()
    if args.apply and not args.yes:
        answer = input(f"Run {' '.join(plan(args.action, True))} on this host? Type APPLY: ")
        if answer != "APPLY":
            print("Cancelled")
            return 1
    if not args.apply:
        print("PREVIEW ONLY: no packages will be installed or removed")
        if args.action == "update":
            print("Would refresh APT indexes; no network action performed")
            return 0
    print("Command:", " ".join(plan(args.action, args.apply)))
    return execute(args.action, args.apply)

def gui() -> int:
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.title("Daylight Updater — preview first")
    root.geometry("470x300")
    action = tk.StringVar(value="upgrade")
    tk.Label(root, text="Choose an action. Preview is the default.").pack(pady=10)
    for item in ACTIONS:
        tk.Radiobutton(root, text=item, variable=action, value=item).pack(anchor="w", padx=40)

    def preview() -> None:
        if action.get() == "update":
            messagebox.showinfo("Preview", "Would refresh package indexes; no action taken")
            return
        try:
            result = execute(action.get(), False)
            messagebox.showinfo("Preview", f"APT simulation exited with status {result}")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    def apply() -> None:
        if not messagebox.askyesno("Confirm system change", f"Execute {action.get()} on this computer?\nNo automatic cleanup or full-upgrade is chained."):
            return
        try:
            result = execute(action.get(), True)
            messagebox.showinfo("Result", f"APT exited with status {result}")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    tk.Button(root, text="Preview (safe)", command=preview).pack(side="left", padx=30)
    tk.Button(root, text="Apply (requires root)", command=apply).pack(side="right", padx=30)
    root.mainloop()
    return 0

if __name__ == "__main__":
    sys.exit(cli())
