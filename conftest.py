from typing import Any, AsyncGenerator
from pathlib import Path

import pytest
from playwright.async_api import async_playwright, Playwright, Page,BrowserContext,Browser
import pytest_asyncio
import json
from dotenv import dotenv_values
from constants.constants import *

@pytest_asyncio.fixture(scope="function")
async def playwright():
    async with async_playwright() as playwright:
        load_all_keys()
        yield playwright

@pytest_asyncio.fixture(scope="function")
async def browser(playwright: Playwright):
    browser_type = getattr(playwright,VAR.get("BROWSER"))
    browser: Browser = await browser_type.launch(headless=bool(VAR.get("HEADLESS") == "True"),
                                                 slow_mo=int(VAR.get("SLOWMO")))

    yield browser
    await browser.close()

@pytest_asyncio.fixture(scope="function")
async def page(browser):
    root=Path(__file__).parent
    cookie_path=root/"resources"/"cookies"/"cookies.json"
    context:BrowserContext = await browser.new_context(
        storage_state=cookie_path if Path(cookie_path).exists() and Path(cookie_path).stat().st_size>0 else None
    )
    # custom_cookies=None
    # if Path("cookies.json").exists():
    #     with open("cookies.json", "r", encoding="utf-8") as c:
    #         custom_cookies = json.load(c)
    #     await context.add_cookies(custom_cookies)
    # else:
    #     with open("cookies.json", "w", encoding="utf-8") as c:
    #         json.dump(await context.cookies(),c)
    page:Page = await context.new_page()
    yield page
    await context.storage_state(path=cookie_path)
    await context.close()


def load_all_keys():
    root_folder = Path(__file__).parent.parent
    env_files = list(root_folder.rglob("*.env"))
    VAR.update({k:v for i in env_files if i.name == "config.env" for k,v in dotenv_values(i).items()})
    VAR.update({k: v for i in env_files if i.name == f"{VAR.get("ENV")}_config.env" for k, v in dotenv_values(i).items()})


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if "page" in item.funcargs:
            page: Page = item.funcargs["page"]

            screenshot_name = f"screenshot_{item.name}.png"
            page.screenshot(path=screenshot_name, full_page=True)
            print(f"\n[Screenshot saved as {screenshot_name}]")