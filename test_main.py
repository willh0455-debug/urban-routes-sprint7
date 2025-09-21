import data
from helpers import is_url_reachable


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        """
        Runs once before all tests.
        Checks if the Urban Routes server is reachable using the URL in data.py.
        """
        if is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # --- Sprint 8 placeholder tests ---

    def test_set_route(self,):
        # Add in S8
        print("function created for set route")
        pass

    def test_select_plan(self,):
        # Add in S8
        print("function created for select plan")
        pass

    def test_fill_phone_number(self,):
        # Add in S8
        print("function created for fill phone number")
        pass

    def test_fill_card(self,):
        # Add in S8
        print("function created for fill card")
        pass

    def test_comment_for_driver(self,):
        # Add in S8
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self,):
        # Add in S8
        print("function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self,):
        """
        In Sprint 8, you'll add the Selenium logic that clicks "Add ice cream" twice.
        Here we prepare the loop per Task 5.
        """
        for _ in range(2):  # iterate twice
            # Add in S8
            pass

    def test_car_search_model_appears(self,):
        # Add in S8
        print("function created for car search model appears")
        pass
git add main.py
git commit -m "Add Sprint 7 scaffolding (setup_class + 8 placeholder tests)"
ls -1 | grep -i "^data.py$" || nano data.py

