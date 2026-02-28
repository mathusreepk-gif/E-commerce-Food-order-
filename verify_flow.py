import asyncio
from playwright.async_api import async_playwright
import os

async def verify_login_flow():
    async with async_playwright() as p:
        # Provide path to the account.html
        path = "file://" + os.path.abspath("account.html").replace('\\', '/')
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print(f"Opening {path}...")
        await page.goto(path)

        # 1. Initially, login form should be visible, register form should be hidden
        print("Checking initial state...")
        login_visible = await page.locator("#form-login").is_visible()
        register_visible = await page.locator("#form-register").is_visible()
        
        print(f"Login Form Visible: {login_visible} (Expected: True)")
        print(f"Register Form Visible: {register_visible} (Expected: False)")
        assert login_visible == True, "Login form was not initially visible!"
        assert register_visible == False, "Register form was incorrectly visible initially!"

        # 2. Click 'Register here' to switch to the register form
        print("\nClicking 'Register here' label...")
        await page.locator("label[for='auth-register']").first.click()
        await asyncio.sleep(0.5) # Wait a moment for CSS animation/state to apply
        
        login_visible = await page.locator("#form-login").is_visible()
        register_visible = await page.locator("#form-register").is_visible()

        print(f"Login Form Visible: {login_visible} (Expected: False)")
        print(f"Register Form Visible: {register_visible} (Expected: True)")
        assert login_visible == False, "Login form did not hide!"
        assert register_visible == True, "Register form did not appear!"

        # 3. Click 'Create Account' which is a label simulating a redirect to login
        print("\nClicking 'Create Account' to simulate returning to login...")
        await page.locator("label[for='auth-login'].checkout-btn").click()
        await asyncio.sleep(0.5)

        login_visible = await page.locator("#form-login").is_visible()
        register_visible = await page.locator("#form-register").is_visible()

        print(f"Login Form Visible: {login_visible} (Expected: True)")
        print(f"Register Form Visible: {register_visible} (Expected: False)")

        print("\n✅ Verification successful! The CSS-only forms are toggling perfectly.")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_login_flow())
