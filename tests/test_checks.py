import asyncio
import pytest
from constants.constants import *
from playwright.async_api import Page

from pages.test_login_page import TestLoginPage
from utils.EnvLoader import EnvLoader


@pytest.mark.asyncio
@pytest.mark.parametrize("column_name,testcaseid",
                          [("testcaseId","test1")])
async def test_navigates_to_google(page:Page,column_name,testcaseid):
    check=TestLoginPage(page)
    loader=EnvLoader("inputdata.csv",column_name,testcaseid)
    loader.load_csv()
    await check.execute(testcaseid)
    # await check.upload_files("resources/html/TestFinalHtml.html")

@pytest.mark.asyncio
@pytest.mark.parametrize("column_name,testcaseid",
                          [("testcaseId","test1")])
async def test_navigates_to_google(page:Page,column_name,testcaseid):
    check=TestLoginPage(page)
    loader=EnvLoader("inputdata.csv",column_name,testcaseid)
    loader.load_csv()
    await check.execute(testcaseid)
    # await check.upload_files("resources/html/TestFinalHtml.html")