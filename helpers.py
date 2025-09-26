"""
helpers.py — Sprint 7 stubs (Selenium added in Sprint 8)
"""
from typing import Any, Optional
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

def is_url_reachable(url: str, timeout: int = 5) -> bool:
    try:
        try:
            req = Request(url, method="HEAD")
            with urlopen(req, timeout=timeout) as resp:
                status = getattr(resp, "status", 200)
                return 200 <= status < 400
        except HTTPError as e:
            if getattr(e, "code", None) in (405, 501):
                req = Request(url, method="GET")
                with urlopen(req, timeout=timeout) as resp:
                    status = getattr(resp, "status", 200)
                    return 200 <= status < 400
            return False
    except (HTTPError, URLError, ValueError):
        return False
    except Exception:
        return False

# 8 Sprint-7 helper stubs (names mirror common tests)
def set_route(from_address: str, to_address: str) -> None: pass
def select_plan(plan_name: str) -> None: pass
def fill_phone_number(phone_number: str) -> None: pass
def fill_card(card_number: str, card_code: str, card_owner: str = "") -> None: pass
def comment_for_driver(comment: str) -> None: pass
def order_blanket_and_handkerchiefs(blanket: bool = True, handkerchiefs: int = 1) -> None: pass
def order_2_ice_creams() -> None: pass
def car_search_model_appears(model_query: str) -> bool: return True
