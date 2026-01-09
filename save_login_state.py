from playwright.sync_api import sync_playwright

def generate_auth_state():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="playwright-profile",
            channel="chrome",
            headless=False
        )

        # 🔹 GLOBAL TIMEOUTS (NO PAGE CODE CHANGE REQUIRED)
        context.set_default_timeout(30000)               # 30 seconds
        context.set_default_navigation_timeout(30000)    # 30 seconds

        page = context.new_page()

        print("\n👉 Opening dev.futurx.app")
        page.goto("https://dev.futurx.app")

        print("\n👉 Login manually (Google / Email)")
        print("👉 Wait until dashboard is fully loaded")
        print("👉 DO NOT close the browser")
        print("👉 Press ENTER only after login is complete\n")

        # 🔴 USER CONTROLLED PAUSE (prevents early close)
        input("⏸️  Press ENTER to save auth state...")

        # Extra stabilization (no navigation triggered)
        page.wait_for_load_state("networkidle")

        context.storage_state(path="auth_state.json")
        print("\n✅ auth_state.json generated successfully")

        print("👉 Browser will close now")
        context.close()

if __name__ == "__main__":
    generate_auth_state()
