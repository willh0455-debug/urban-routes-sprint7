""
main.py — Sprint 7 scaffolding
- Contains a Pytest-style class with stubbed tests for Sprint 8
- Checks the server once in setup_class using helpers.is_url_reachable
"""

import data
from helpers import is_url_reachable


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        """Runs once before all tests — Task 4 server check."""
        url = getattr(data, "URBAN_ROUTES_URL", "")
        if url and is_url_reachable(url):
            print("Connected to the Urban Routes server")
        else:
            print(
                "Cannot connect to Urban Routes. Check the server is on and still running"
            )

    # ---- Task 3: 8 placeholder tests (prep for Sprint 8) ----
    def test_set_route(self):
        # Add in S8
        # print("function created for set route")
        pass

    def test_select_plan(self):
        # Add in S8
        # print("function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        # print("function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        # print("function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        # print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        # print("function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Task 5: prepare the loop now; implement actions in Sprint 8
        for _ in range(2):
            # Add in S8
            pass

    def test_car_search_model_appears(self):
        # Add in S8
        # print("function created for car search model appears")
        pass
