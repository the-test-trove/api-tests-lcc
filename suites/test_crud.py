import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
import requests
from fixtures import fixture

# You can use the below format to describe a suite if you don't want to create a class.
# SUITE = {
#     "description": "Sample API tests for GET, POST, DELETE ",
#      "rank": 1
# }

base_url = fixture.url

@lcc.suite(description="Suite: Sample API tests for GET, POST, DELETE", rank=1)
class test_crud:
    api_auth = lcc.inject_fixture("api_auth")

    @lcc.test("Verify that GET request for users/1 gives a 200 OK")
    def test_get_users(self):
        lcc.set_step("checking for endpoint: %s" % base_url)
        response = requests.get(url=base_url + "/users/1")
        check_that("response code", response.status_code, equal_to(200), quiet=False)


    @lcc.test("Verify that GET request for /users/1 contains required params")
    def test_get_users_params(self):
        response = requests.get(url=base_url + "/users/1")
        result = response.json()
        check_that("the response ", result, has_entry("name"))
        require_that("the response", result, has_entry("email", contains_string("@")))
        check_that("the response ", result, has_entry("username", equal_to("Bret")))
        check_that("the response ", result, has_entry("address", is_dict()))
        require_that("the response", result, has_entry("address", has_entry("city", equal_to("Gwenborough"))))


    @lcc.test("Verify that POST request to /posts is successful")
    def test_post_req(self):
        body = {
          "title": 'Title for demo purpose',
          "body": 'Test title by Anisha',
          "userId": 500
        }
        response = requests.post(base_url + "/posts", data=body)
        result = response.json()
        require_that("the POSt request response", response.status_code, equal_to(201))
        lcc.log_info(str(result))
        check_that("the response", result, has_entry("title", equal_to("Title for demo purpose")))


    @lcc.test("Verify that the DELETE request to /posts/1 gives 200 OK")
    def test_del_req(self):
        response = requests.delete(base_url + "/posts/1")
        result = response.json()
        check_that(" the response for delete request", response.status_code, equal_to(200))
        assert_that(" the response for delete request", response.status_code, equal_to(200))
        lcc.log_info("Making sure that the DELETE request was successful: %s" % str(result))
