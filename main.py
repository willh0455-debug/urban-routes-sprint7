import data          # Task 3: import data
import helpers       # Task 4: server reachability check

class TestUrbanRoutes:
    # Task 4: setup_class runs once before all tests
    @classmethod
    def setup_class(cls):
        # Add in S8: paste a fresh Start Server URL into data.URBAN_ROUTES_URL before real runs
        url = data.URBAN_ROUTES_URL
        if helpers.is_url_reachable(url):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # ---- Task 3 stubs ----
    def test_set_route(self):
        # Add in S8
        print("function created for set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Task 5: add a for loop that iterates twice
        for _ in range(2):
            # Add in S8
            pass
        print("function created for order 2 ice creams (loop prepared)")
        pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for car search model appears")
        pass


# Optional: quick local run so you can see prints without pytest
if __name__ == "__main__":
    TestUrbanRoutes.setup_class()
    t = TestUrbanRoutes()
    t.test_set_route()
    t.test_select_plan()
    t.test_fill_phone_number()
    t.test_fill_card()
    t.test_comment_for_driver()
    t.test_order_blanket_and_handkerchiefs()
    t.test_order_2_ice_creams()
    t.test_car_search_model_appears()


