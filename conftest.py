# # from playwright.sync_api import Playwright
# # import pytest
# # import warnings
# # from libraries.util import common

# # def create_browser_context(playwright: Playwright):
# #     browser = playwright.chromium.launch(headless=False)
# #     context = browser.new_context()
# #     page = context.new_page*()

# # # @pytest.fixture(scope='session', autouse=True)
# # @pytest.fixture(scope="function", autouse=True)
# # def uCommon():
# #     warnings.filterwarnings('ignore')
# #     return common()

# import pytest
# from pytest_zebrunner.tcm import Zephyr

# @pytest.hookimpl(trylast=True)
# def pytest_sessionstart():
#     Zephyr.set_test_cycle_key("EDA-R1667")
#     Zephyr.set_jira_project_key("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb250ZXh0Ijp7ImJhc2VVcmwiOiJodHRwczovL2VkYW1hbWEuYXRsYXNzaWFuLm5ldCIsInVzZXIiOnsiYWNjb3VudElkIjoiNjQxODA0NjM5ZDYzODNlMzJhMzI0ZWNmIn19LCJpc3MiOiJjb20ua2Fub2FoLnRlc3QtbWFuYWdlciIsInN1YiI6ImZjZDgzNjk0LTllMzAtM2NiNy05MGRjLTQ5ZmFiNTRjN2M3MyIsImV4cCI6MTcxODI0MDg4MSwiaWF0IjoxNjg2NzA0ODgxfQ.Zhtr9YQtqRGloc36QOHUtUEvEoXS0e5L2Oc_GK5jCq8")
