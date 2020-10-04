import lemoncheesecake.api as lcc
import os
from helpers import utilities


# setting the appropriate URL value from env variable
env = os.environ['ENV']
if env == "prod":
    url = utilities.config_reader('prod', 'base_url')

elif env == "qa":
    url = utilities.config_reader('qa', 'base_url')

else:
    raise Exception("Please set the env variable ENV as dev/qa/stage specifically. "
                    "To run your tests against Prod, run `$export ENV=prod` before you run the tests")


username = utilities.config_reader('auth', 'username')
auth = utilities.config_reader('auth', 'password')


@lcc.fixture(names=("api_auth", "auth"), scope="session")
def setup():
		# the below code snippet is to initialise the session at once as a setup step, currently the tests don't use auth
    # but below is the snippet for reference,
    # you can read more about fixtures here: http://docs.lemoncheesecake.io/en/latest/fixtures.html
    lcc.log_info("Tests are running against instance: %s" % url)
    lcc.log_info("Initialising the session/auth...")
    # session = requests.Session()
    # session.auth = (username, auth)

    # yield session

    #You can add any tear down steps here if needed.
		# lcc.log_info("Tests completed")
