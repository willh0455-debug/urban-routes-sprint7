"""
main.py — Sprint 7 runner
"""
from data import BASE_URL
from helpers import is_url_reachable

def main() -> None:
    ok = is_url_reachable(BASE_URL)
    print(f"BASE_URL reachable: {ok} — {BASE_URL}")

if __name__ == "__main__":
    main()
