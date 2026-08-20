"""Minimal example for 2048Terminal."""

from 2048terminal import 2048terminal


def main():
 runner = 2048terminal({"name": "2048Terminal", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()