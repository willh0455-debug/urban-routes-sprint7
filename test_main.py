import data
from helpers import is_url_reachable


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Runs once before all tests; checks the server URL.
        if is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        # Add in S8
        pass

    def test_select_plan(self):
        # Add in S8
        pass

    def test_fill_phone_number(self):
        # Add in S8
        pass

    def test_fill_card(self):
        # Add in S8
        pass

    def test_comment_for_driver(self):
        # Add in S8
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        pass

    def test_order_2_ice_creams(self):
        # Prepared in Sprint 7; real steps added in Sprint 8.
        for _ in range(2):
            # Add in S8
            pass

    def test_car_search_model_appears(self):
        # Add in S8
        pass

