import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
delay = 100


def goto_url_portal():
    driver.get("https://portal.qikpod.com/version-test")
    driver.maximize_window()


def click():
    my_element1 = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "bubble-element.Button.clickable-element")))
    my_element1.click()


def send_key_number(param):
    my_element2 = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "bubble-element Input")))
    my_element2.send_keys(param)


def send_otp(param):
    my_element4 = WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter OTP Send To Mobile Number']")))
    my_element4.send_keys(param)


def xpath_click(param):
    try:
        my_element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, param)))
        my_element.click()
    except Exception as e:
        print("------------failed----------------------")
        driver.close()
        assert True


def xpath_send_keys(param, key):
    try:
        my_element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, param)))
        my_element.send_keys(key)
    except Exception as e:
        print("------------failed----------------------")
        driver.close()
        assert True


def xpath_clear(param):
    try:
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, param))).clear()
    except Exception as e:
        print("------------failed----------------------")
        driver.close()
        assert True


def get_text(param):
    try:
        res = WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, param))).text
        return res
    except Exception as e:
        print("------------failed----------------------")
        driver.close()
        assert True


def signin(number, otp):
    goto_url_portal()
    try:
        click()
        send_key_number(number)
        click()
        send_otp(otp)
        click()
        print("Sign in successfully")
    except Exception as e:
        driver.close()


def goto_dashboard():
    click()
    print("--------------Dashboard-----------------")


def get_location_count(location_count):
    txt = get_text(location_count)
    print("location count is :", txt)
    return txt


def get_pods_count(pod_count):
    txt = get_text(pod_count)
    print("pods count is :", txt)
    return txt


def get_users_count(user_count):
    txt = get_text(user_count)
    print("users count is :", txt)
    return txt


def get_reservation_count(reservation_count):
    txt = get_text(reservation_count)
    print("reservation count is : ", txt)
    return txt


def goto_location(location_path):
    xpath_click(location_path)
    print("--------------Location-----------------")


def add_location(button, loc_name, loc_name_path1, add, address_path2, pin, pincode_path3,
                 pri_name, pri_name_path4, prin_contact, prin_contact_path5, proceed_button, ok_button):
    xpath_click(button)
    xpath_send_keys(loc_name_path1, loc_name)
    xpath_send_keys(address_path2, add)
    xpath_send_keys(pincode_path3, pin)
    xpath_send_keys(pri_name_path4, pri_name)
    xpath_send_keys(prin_contact_path5, prin_contact)

    xpath_click(proceed_button)
    xpath_click(ok_button)
    print("location added ")


def search_location(search_path, search_, view_button):
    xpath_send_keys(search_path, search_)
    xpath_click(view_button)
    print("searching---------")


def create_user(create_button, c_name_xpath, name, type_xpath, type_, email_xpath, email, phone_xpath, phone,
                address_xpath, address, cancel_button):
    xpath_click(create_button)
    xpath_send_keys(c_name_xpath, name)
    sel = Select(driver.find_element(By.XPATH, type_xpath))
    sel.select_by_visible_text(type_)
    xpath_send_keys(email_xpath, email)
    xpath_send_keys(phone_xpath, phone)
    xpath_send_keys(address_xpath, address)

    # i use cancel here
    xpath_click(cancel_button)
    print("create user ok")


def edit_user_location(edit_button, loc_name_xpath, loc_name, add_xpath, add, pin_xpath, pin, pri_name_xpath, pri_name,
                       prin_contact_xpath, prin_contact, update_button, yes_button):
    xpath_click(edit_button)
    xpath_clear(loc_name_xpath)
    xpath_send_keys(loc_name_xpath, loc_name)
    xpath_clear(add_xpath)
    xpath_send_keys(add_xpath, add)
    xpath_clear(pin_xpath)
    xpath_send_keys(pin_xpath, pin)
    xpath_clear(pri_name_xpath)
    xpath_send_keys(pri_name_xpath, pri_name)
    xpath_clear(prin_contact_xpath)
    xpath_send_keys(prin_contact_xpath, prin_contact)
    # update and yes
    xpath_click(update_button)
    xpath_click(yes_button)


def delete_location(delete_button, confirm_button):
    xpath_click(delete_button)
    xpath_click(confirm_button)
    print("location deleted")


def goto_pods(pod_button):
    xpath_click(pod_button)
    print("----------------------pods-----------------------")


def get_pod_dashboard_monitor(total_pod, deployed_pod, lab_pod, yellow_pod, green_pod, red_pod, orange_pod, active_pod,
                              inactive_pod, unregistered_pod, certified_pod):
    txt = get_text(total_pod)
    print("Total pod count is :", txt)
    txt = get_text(deployed_pod)
    print("Deployed Pods Count is :", txt)
    txt = get_text(lab_pod)
    print("Lab Pods Count is :", txt)
    txt = get_text(yellow_pod)
    print("Yellow Pods Count is :", txt)
    txt = get_text(green_pod)
    print("Green Pods Count is :", txt)
    txt = get_text(red_pod)
    print("Red Pods Count is :", txt)
    txt = get_text(orange_pod)
    print("Orange Pods Count is :", txt)
    txt = get_text(active_pod)
    print("Active Pods Count is :", txt)
    txt = get_text(inactive_pod)
    print("Inactive pod count is :", txt)
    txt = get_text(unregistered_pod)
    print("Unregistered pod count is :", txt)
    txt = get_text(certified_pod)
    print("Certified pod count is :", txt)


# def total_pod_count():
#     txt = get_text("/html[1]/body[1]/div[1]/div[3]/div[2]/h1[1]/div[1]")
#     print("Total pod count is :", txt)
#
#
# def deployed_pod_count():
#     txt = get_text("/html[1]/body[1]/div[1]/div[3]/div[3]/h1[1]/div[1]")
#     print("Deployed Pods Count is :", txt)
#
#
# def lab_pod_count():
#     txt = get_text("/html[1]/body[1]/div[1]/div[3]/div[4]/h1[1]/div[1]")
#     print("Lab Pods Count is :", txt)


# def green_pods_count():
#     txt = get_text("/html[1]/body[1]/div[1]/div[5]/div[2]/h1[1]/div[1]")
#     print("Inactive pods count is :", txt)
#
#
# def red_pods_count():
#     txt = get_text("/html[1]/body[1]/div[1]/div[3]/div[3]/h1[1]/div[1]")
#     print("Red Pods Count is :", txt)
#
#
# def orange_pods_count():
#     txt = get_text("/html[1]/body[1]/div[1]/div[3]/div[4]/h1[1]/div[1]")
#     print("Orange Pods Count is :", txt)
#
#
# def yellow_pods_count():
#     txt = get_text("/html[1]/body[1]/div[1]/div[3]/div[5]/h1[1]/div[1]")
#     print("Yellow Pods Count is :", txt)
#
#
# def active_pods_count():
#     txt = get_text("/html[1]/body[1]/div[1]/div[4]/div[1]/h1[1]/div[1]")
#     print("Active Pods Count is :", txt)
#
#
# def inactive_pods_count():
#     txt = get_text("/html[1]/body[1]/div[1]/div[4]/div[2]/h1[1]/div[1]")
#     print("Inactive Pods Count is :", txt)
#
#
# def unregistered_pods_count():
#     txt = get_text("/html[1]/body[1]/div[1]/div[4]/div[3]/h1[1]/div[1]")
#     print("Unregistered Pods Count is :", txt)
#
#
# def certified_pods_count():
#     txt = get_text("/html[1]/body[1]/div[1]/div[4]/div[4]/h1[1]/div[1]")
#     print("Certified Pods Count is :", txt)


def register_pod(register_pod_button, serial_no_xpath, serial_no, model_no_xpath, model_no, total_pod_xpath, total_pod,
                 proceed_button, ok_button):
    xpath_click(register_pod_button)
    xpath_send_keys(serial_no_xpath, serial_no)
    xpath_send_keys(model_no_xpath, model_no)
    xpath_send_keys(total_pod_xpath, total_pod)
    xpath_click(proceed_button)
    xpath_click(ok_button)


def search_pod(search_xpath, view_button, search):
    xpath_send_keys(search_xpath, search)
    xpath_click(view_button)


def checkbox_unselect(checkbox_unselect1):
    xpath_click(checkbox_unselect1)


def edit_pod(edit_pod_button, flag_button, flag, pod_state_button, pod_state, update_button, status, pod_status):
    xpath_click(edit_pod_button)
    select1 = Select(driver.find_element(By.XPATH, flag_button))
    select1.select_by_visible_text(flag)
    select2 = Select(driver.find_element(By.XPATH, pod_state_button))
    select2.select_by_visible_text(pod_state)
    select3 = Select(driver.find_element(By.XPATH, pod_status))
    select3.select_by_visible_text(status)
    xpath_click(update_button)


def get_pod_details(xpath_id_, xpath_door, xpath_current, xpath_target, xpath_health, xpath_state, xpath_power,
                    xpath_mac_add, xpath_pod_wifi, xpath_created, xpath_updated, xpath_location, xpath_spot):
    print("-------Details------")
    id_ = get_text(xpath_id_)
    door = get_text(xpath_door)
    print(id_)
    print(door)

    print("-------Version------")
    current = get_text(xpath_current)
    target = get_text(xpath_target)
    print(current)
    print(target)

    print("-------Status------")

    health = get_text(xpath_health)
    state = get_text(xpath_state)
    power = get_text(xpath_power)
    print(health)
    print(state)
    print(power)

    print("-------Address------")
    mac_add = get_text(xpath_mac_add)
    pod_wifi = get_text(xpath_pod_wifi)
    print(mac_add)
    print(pod_wifi)

    print("-------Date / Time------")
    created = get_text(xpath_created)
    updated = get_text(xpath_updated)
    print(created)
    print(updated)

    print("-------Location------")
    location = get_text(xpath_location)
    spot = get_text(xpath_spot)
    print(location)
    print(spot)


def pod_logs_100():
    sel = Select(driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[2]/select[1]"))
    sel.select_by_visible_text("100")


def pod_logs_200():
    sel = Select(driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[2]/select[1]"))
    sel.select_by_visible_text("200")


def pod_logs_300():
    sel = Select(driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[2]/select[1]"))
    sel.select_by_visible_text("300")


def delete_pod(delete_pod_button, confirm_button):
    xpath_click(delete_pod_button)
    xpath_click(confirm_button)
    print("delete pod")
    time.sleep(8)


def goto_users(goto_user):
    xpath_click(goto_user)
    print("-------------------users--------------------")


def add_users(add_user_button, a_name_xpath, name, u_type_xpath, u_type, email_xpath, email, detail_xpath, detail,
              phone_xpath, phone, address_xpath, address, confirm_button, ok_button):
    xpath_click(add_user_button)
    xpath_send_keys(a_name_xpath, name)
    sel = Select(driver.find_element(By.XPATH, u_type_xpath))
    sel.select_by_visible_text(u_type)
    xpath_send_keys(email_xpath, email)
    xpath_send_keys(detail_xpath, detail)
    xpath_send_keys(phone_xpath, phone)
    xpath_send_keys(address_xpath, address)
    xpath_click(confirm_button)
    xpath_click(ok_button)
    print("add users done")


def search_user(search_xpath, view_button, search_):
    xpath_send_keys(search_xpath, search_)
    xpath_click(view_button)
    print("----------searching-----------------")


def users_detail(get_name, get_email_, get_mobile, get_user_type, get_loc_count, get_reservation):
    print("--------------User Details---------------")
    name_ = get_text(get_name)
    email_ = get_text(get_email_)
    mobile = get_text(get_mobile)
    user_type = get_text(get_user_type)
    loc_count = get_text(get_loc_count)
    reservation = get_text(get_reservation)
    print("Name :", name_)
    print("Email id :", email_)
    print("Mobile No :", mobile)
    print("User type :", user_type)
    print("Location Count :", loc_count)
    print("Reservation Count :", reservation)


def edit_user_detail(name_xpath, name_, u_type_xpath, email_xpath, phone_xpath, add_xpath, u_type_, email_, phone_, add,
                     flat_no, flat_no_xpath, update_button, ok_button):
    print("edit user details----------------")
    WebDriverWait(driver, delay).until(EC.element_to_be_clickable(
        (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]"))).click()

    xpath_clear(name_xpath)
    xpath_send_keys(name_xpath, name_)

    sel = Select(driver.find_element(By.XPATH, u_type_xpath))
    sel.select_by_visible_text(u_type_)

    xpath_clear(email_xpath)
    xpath_send_keys(email_xpath, email_)

    xpath_clear(phone_xpath)
    xpath_send_keys(phone_xpath, phone_)

    xpath_clear(add_xpath)
    xpath_send_keys(add_xpath, add)

    xpath_clear(flat_no_xpath)
    xpath_send_keys(flat_no_xpath, flat_no)

    xpath_click(update_button)
    xpath_click(ok_button)


def delete_user(delete_button, ok_button):
    xpath_click(delete_button)
    xpath_click(ok_button)
    print("delete user ")


def goto_reservations(goto_reservation):
    xpath_click(goto_reservation)
    print("--------------------reservation------------------")


def search_reservation(search_xpath, view_button, id_):
    xpath_send_keys(search_xpath, id_)
    xpath_click(view_button)


def get_reservation_details(xpath_reserve_for, xpath_drop_by, xpath_created_by, xpath_pod_id, xpath_loc, xpath_status,
                            xpath_awb,
                            xpath_exp_date, xpath_spot, xpath_user_num, xpath_drop_by_num, xpath_created_by_num,
                            xpath_pod_name, xpath_door, xpath_pod_status, xpath_drop_otp, xpath_pickup_otp,
                            xpath_rto_otp):
    print("-----------Users Details-----------")
    reserve_for = get_text(xpath_reserve_for)
    drop_by = get_text(xpath_drop_by)
    created_by = get_text(xpath_created_by)
    print(reserve_for)
    print(drop_by)
    print(created_by)

    print("-----------Pod Details-----------")
    pod_id = get_text(xpath_pod_id)
    loc = get_text(xpath_loc)
    status = get_text(xpath_status)

    print(pod_id)
    print(loc)
    print(status)

    print("-----------Reservation Details-----------")
    awb = get_text(xpath_awb)
    exp_date = get_text(xpath_exp_date)
    spot = get_text(xpath_spot)
    print(awb)
    print(exp_date)
    print(spot)

    print("--------User Number---------")
    user_num = get_text(xpath_user_num)
    drop_by_num = get_text(xpath_drop_by_num)
    created_by_num = get_text(xpath_created_by_num)
    print(user_num)
    print(drop_by_num)
    print(created_by_num)
    print("--------Pod Details---------")
    _pod_name = get_text(xpath_pod_name)
    _door = get_text(xpath_door)
    _pod_status = get_text(xpath_pod_status)
    print(_pod_name)
    print(_door)
    print(_pod_status)
    print("--------Reservation otp---------")
    drop_otp = get_text(xpath_drop_otp)
    pickup_otp = get_text(xpath_pickup_otp)
    rto_otp = get_text(xpath_rto_otp)
    print(drop_otp)
    print(pickup_otp)
    print(rto_otp)


def go_back_to_reservation(back_to_reservation):
    xpath_click(back_to_reservation)


def goto_support():
    xpath_click("//html[1]/body[1]/div[3]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
    print("support ok")


def goto_logs():
    xpath_click("/html[1]/body[1]/div[3]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]")
    # auto refresh uncheck
    xpath_click("/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    print("logs ok")


# def goto_account():
#     xpath_click("/html[1]/body[1]/div[3]/div[4]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/button[1]")
#     print("account ok")


def goto_logout():
    xpath_click("/html[1]/body[1]/div[3]/div[4]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/button[1]")
    time.sleep(1)
    xpath_click("/html[1]/body[1]/div[3]/div[2]/div[1]/button[1]")
    # confirm No and then YEs
    xpath_click("/html[1]/body[1]/div[4]/div[4]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/button[1]")
    time.sleep(1)
    xpath_click("/html[1]/body[1]/div[3]/div[2]/div[2]/button[1]")

    print("logout successfully")
