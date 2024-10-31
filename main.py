import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By

def open_browser():
    driver = webdriver.Chrome()
    driver.get("https://kinnser.net/login.cfm")
    return driver

def close_browser(driver):
    driver.quit()
    st.session_state.pop('driver', None)
    st.success("Browser closed! You can now continue.")

def main():

    st.title("Open Chrome Browser")

    if st.button("Open Browser"):
        driver = open_browser()
        st.session_state.driver = driver  # Store driver in session state
        st.success("Browser opened! Please interact with it.")
        st.write("Close the browser to continue...")
        userElem = driver.find_element(By.ID, "username")
        userElem.send_keys("jason")

    if 'driver' in st.session_state:
        st.button("Close Browser", on_click=lambda: close_browser(st.session_state.driver))
        driver = open_browser()



if __name__ == "__main__":
    main()

