import json

from playwright.async_api import Page, expect
from constants.constants import *
from utils.EnvLoader import EnvLoader


class TestLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("xpath=//*[contains(text(),'Username')]/following-sibling::input[1]")
        self.password = page.locator("xpath=//*[contains(text(),'Password')]/following-sibling::input[1]")
        self.email = page.locator("xpath=//*[contains(text(),'Email')]/following-sibling::input[1]")
        self.comments = page.locator("xpath=//*[contains(text(),'Comments')]/following-sibling::textarea")
        self.disabled_input = page.locator("xpath=//*[contains(text(),'Disabled Input')]/following-sibling::input[1]")
        self.upload_file = page.locator("xpath=//*[contains(text(),'Upload')]/following-sibling::input[1]")
        self.male_gender = page.locator("xpath=//*[contains(text(),'Male')]/preceding-sibling::input[1]")
        self.female_gender = page.locator("xpath=//*[contains(text(),'Female')]/preceding-sibling::input[1]")
        self.dob = page.locator("xpath=//*[contains(text(),'Date')]/following-sibling::input[1]")
        self.java_skill = page.locator("xpath=//*[contains(text(),'Java')]/preceding-sibling::input[1]")
        self.python_skill = page.locator("xpath=//*[contains(text(),'Python')]/preceding-sibling::input[1]")
        self.select = page.locator("xpath=//*[contains(text(),'Country')]/following-sibling::select[1]")
        self.multiselect = page.locator("xpath=//*[contains(text(),'Multi')]/following-sibling::select[1]")
        self.show_alert_btn = page.locator("xpath=//button[contains(text(),'Show Alert')]")
        self.show_modal_btn = page.locator("xpath=//button[contains(text(),'Show Modal')]")
        self.open_tab_btn = page.locator("xpath=//button[contains(text(),'Open Tab')]")
        self.open_window_btn = page.locator("xpath=//button[contains(text(),'Open Window')]")
        self.open_frame_window_btn = page.locator("xpath=//button[contains(text(),'Open Frame Window')]")
        self.dynamic_content = page.locator(
            "xpath=//*[contains(text(),'Modal & Dynamic Content')]/following-sibling::div")
        self.fames_1 = page.locator("xpath=//*[contains(text(),'Iframes')]/following-sibling::div/iframe[1]")
        self.fames_2 = page.locator("xpath=//*[contains(text(),'Iframes')]/following-sibling::div/iframe[2]")
        self.left_click_btn = page.locator("xpath=//button[contains(text(),'Left Click Me')]")
        self.right_click_btn = page.locator("xpath=//*[contains(text(),'Right Click Me')]")
        self.modal_div = self.page.locator("xpath=//*[contains(text(),'This is a Modal')]/parent::div")

    async def execute(self, testcase_id):
        # await self.page.goto(VAR.get("URL"), wait_until="networkidle")
        #
        # # -------- BASIC FORM FILL --------
        # await self.username.wait_for(state="visible", timeout=10000)
        #
        # await self.username.fill(EnvLoader.var(testcase_id, "username"))
        # await self.password.fill(EnvLoader.var(testcase_id, "password"))
        # await self.email.fill(EnvLoader.var(testcase_id, "email"))
        # await self.comments.fill(EnvLoader.var(testcase_id, "comment"))
        #
        # assert await self.disabled_input.is_disabled(), "Disabled field is enabled!"
        #
        # # -------- RADIO & DATE --------
        # await self.male_gender.check()
        #
        # # FIXED DATE FORMAT (YYYY-MM-DD)
        # await self.dob.fill("1993-03-11")
        #
        # # Correct scroll
        # await self.dob.evaluate(
        #     "(el) => el.scrollIntoView({ block: 'start', behavior: 'smooth' })"
        # )
        #
        # await self.java_skill.check()
        #
        # # -------- SINGLE DROPDOWN --------
        # print("Username entered:", await self.username.input_value())
        #
        # options = [opt.strip() for opt in await self.select.locator("option").all_text_contents()]
        # print("Dropdown options:", options)
        #
        # await self.select.select_option(label="India")
        # await self.select.select_option("USA")
        #
        # selected_country = await self.select.input_value()
        # print("Selected country:", selected_country)
        #
        # # -------- MULTI-SELECT --------
        # await self.multiselect.select_option(["Selenium", "Java"])
        #
        # selected_skills = await self.multiselect.evaluate(
        #     "el => Array.from(el.selectedOptions).map(o => o.value)"
        # )
        # print("Selected skills:", selected_skills)
        #
        # # -------- ALERT / CONFIRM (YOUR PAGE USES confirm()) --------
        # # Register handler FIRST
        # dw = ""
        #
        # async def handle_dialog(dialog):
        #     nonlocal dw
        #     dw = dialog.message
        #     await dialog.accept()  # click OK
        #
        # self.page.once("dialog", handle_dialog)
        #
        # # NOW click the button
        # await self.show_alert_btn.click()
        #
        # print("Dialog text:", dw)
        # Click OK

        # # -------- MODAL HANDLING --------
        # await self.show_modal_btn.click()
        # await self.modal_div.wait_for(state="visible")
        #
        # modal_text = await self.modal_div.locator(".modal-content p").text_content()
        # print("Modal text:", modal_text)
        #
        # # Close modal
        # await self.page.click("#closeModal")
        # await self.modal_div.wait_for(state="hidden")
        # currwnt_tab=self.page
        # # -------- NEW TAB HANDLING (FIXED) --------
        # async with self.page.expect_popup() as popup_info:
        #     await self.open_tab_btn.click()
        #
        # new_tab = await popup_info.value
        # await new_tab.wait_for_load_state("domcontentloaded")
        # print("New tab title:", await new_tab.title())
        # await self.page.wait_for_timeout(1000)
        # ssw=[]
        # ssw=self.page.context.pages
        # await currwnt_tab.bring_to_front()
        # print(ssw)
        # await ssw[len(ssw)-1].close(
        # )
        #
        # await new_tab.close()
        # await self.right_click_btn.click(button="left")
        # await self.page.wait_for_timeout(2000)
        # await self.right_click_btn.click(button="right")
        # await self.page.wait_for_timeout(2000)
        # await self.right_click_btn.click(button="middle")
        # await self.page.wait_for_timeout(2000)

        # await self.open_frame_window_btn.click()
        # ssw = self.page.context.pages
        # new_win=ssw[len(ssw)-1]
        # await new_win.bring_to_front()
        # await ssw[len(ssw)-1].set_viewport_size({"width": 1920, "height": 1080})
        # frame=new_win.frame_locator("iframe")
        # await frame.locator("input").fill("sssssssssss")
        # print("wsfw")
        await self.page.goto("https://opensource-demo.orangehrmlive.com/",wait_until="domcontentloaded")
        await self.page.wait_for_timeout(2000)
        if not "dashboard" in self.page.url:
            user_name=self.page.locator("xpath=//*[contains(text(),'Username')]/ancestor::div[2]//input")
            password = self.page.locator("xpath=//*[contains(text(),'Password')]/ancestor::div[2]//input")
            await user_name.fill("Admin")
            await password.fill("admin123")
            await self.page.locator("//button[contains(.,'Login')]").click()
            # cookies=await self.page.context.cookies()
            # with open("cookies.json","w",encoding="utf-8") as file:
            #     json.dump(cookies,file)
            # print(cookies)
        print(self.page.title())
        await expect(self.page.url).to_have_url("**/dashboard")
        #
        # new_window = await popup_info.value
        # await new_window.wait_for_load_state("domcontentloaded")

        # maximize
        # await new_window.bring_to_front()
        # await new_window.set_viewport_size({"width": 1920, "height": 1080})
        #
        # # switch to iframe INSIDE the new window
        # inner_frame = new_window.frame_locator("iframe")
        #
        # # type inside iframe
        # await inner_frame.locator("#iframeInput").fill("sssssssssss")
        # await new_window.close()
        # print("wsfw")

    async def upload_files(self, path):
        root = Path(__file__).parent.parent
        file_path = root / path
        await self.upload_file.evaluate("""(d)=>d.scrollIntoView({
        block:'nearest',behaviour:'smooth'
        })""")
        await self.upload_file.set_input_files(file_path)
        # await self.page.wait_for_timeout(5000)
