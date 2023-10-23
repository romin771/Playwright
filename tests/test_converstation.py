from playwright.async_api import async_playwright
from pages.login_page import LoginPage
import json
import pytest


contact_conversation_id = []
async def contact_handler(request):
    if request.post_data:
        my_json = json.loads(request.post_data)
        if "request" in my_json and my_json["request"] == "conversation_get":
            contact_conversation_id.append(request.post_data)


@pytest.mark.asyncio
async def test_chat_user_like():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page_user = await browser.new_page()
        context = await browser.new_context()
        page_operators = await context.new_page()
        page_user.on("request", contact_handler)


        contact_url = 'file:///Users/romin/Desktop/widget.html'
        await page_user.goto(contact_url)

        operator_url = 'https://www.userlike.com/en/'
        await page_operators.goto(operator_url)

        # Operator :: login and go to message center
        lp = LoginPage(page_operators)
        await lp.navigate_to_login()
        await lp.login("romin5954@gmail.com", "RominRomin!234!234")
        message_center_menu = page_operators.locator('a[data-capab="message_center"]')
        await message_center_menu.click()


        # Contact :: send message to operator from widget
        iframe_counter = page_user.locator('iframe').nth(1)
        await iframe_counter.click()
        iframe_title = page_user.frame_locator('[title="Messenger"]').locator('body')
        start_new_conversation_button = iframe_title.locator('.e16mbzbx0.frame-1127ylp')
        await start_new_conversation_button.click()

        message_textfield = iframe_title.locator(".frame-fz713g.e3usqwx0")
        await message_textfield.type("Hi")

        send_message = iframe_title.locator(".e1jpo3mb1.frame-ag41p4").last
        await send_message.click()


        # Extracting converstation id from Contact message
        my_json = json.loads(contact_conversation_id[0])
        conversation_id = my_json["body"]["conversation_id"]
        print("contact conversation ID is : ", conversation_id)


        # Operator :: get the tile
        conversation_tile = page_operators.locator('.umc-3f2z7').first
        await conversation_tile.click()
        ccid = page_operators.locator('.chakra-editable__preview.umc-p2mkcg') # get the converstation id
        op_innertext = await ccid.inner_text()
        parts = op_innertext.split('#')
        operator_conversation_id = parts[1]
        print("Operator converstation ID is: ", operator_conversation_id)

        assert conversation_id == int(operator_conversation_id), " Converstation id is not equal"

        # Operator :: send message to contact
        message_field = page_operators.locator(".content-editable.umc-1uz54nk")
        await message_field.click()
        await message_field.fill(" hi, how can i help you ?")

        send_button = page_operators.locator('button[aria-label="Send message"]')
        await send_button.click()

        # Get the message I have send to contact
        operator_text = page_operators.locator('.umc-1j9ff7p').last
        operator_message = await operator_text.inner_text()
        # Receive the message I have get from operator
        iframe_titles = page_user.frame_locator('[title="Messenger"]').locator('body')
        received_message = iframe_titles.locator('.e13soig20.frame-1vaku2.ep428ig0').last
        received_message_text = await received_message.inner_text()

        assert received_message_text in operator_message




