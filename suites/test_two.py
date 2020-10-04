import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
import requests
from fixtures import fixture


base_url = fixture.url

#similarly you can create multiple suites based on your requirement

@lcc.suite(description="Suite: Sample Test Two", rank=2)
class test_two:
    api_auth = lcc.inject_fixture("api_auth")

    @lcc.test("Verify that ...")
    def test_another(self):
        lcc.log_info(("This is a placeholder test which will run second"))
        pass
