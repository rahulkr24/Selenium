from main import *
from xpath_portal import *


def test_valid_sign():
    signin("9845069130", "984130")


def test_dashboard():
    goto_dashboard()
    get_location_count(location_count=location_count)
    get_pods_count(pod_count=pod_count)
    get_users_count(user_count=pod_count)
    get_reservation_count(reservation_count=reservation_count)


def test_location():
    goto_location(**location_button)


def test_add_location():
    add_location(button, **add_new_location)
    search_location(search_="test1", **search_data)


def test_create_user():
    create_user(name="rahul", type_="Customer", email="rahulkumar@gmail.com", phone="9876543210",
                address="Ranchi Jharkhand", **create_user_location)


def test_edit_user_location():
    edit_user_location(button, loc_name="test1", add="test2", pin="000002", pri_name="Qikpod",
                       prin_contact="9998877665", **edit_user)
    search_location(search_="test1", **search_data)


def test_delete_location():
    delete_location(**delete_location_data)


def test_pods():
    goto_pods(pod_button=pod_button)
    get_pod_dashboard_monitor(**pod_dashboard_monitor)


def test_register_pod():
    register_pod(serial_no="9999999", model_no="LAB_TEST", total_pod="7", **register_new_pod)
    search_pod(search="999999", **search_pod_data)
    checkbox_unselect(checkbox_unselect1)


def test_edit_pod():
    edit_pod(button, flag="True", pod_state="Unregistered", status="inactive", **edit_pod_detail)
    checkbox_unselect(checkbox_unselect1)


def test_get_pod_details():
    get_pod_details(**get_pod_data)


def test_delete_pod():
    delete_pod(**delete_pod_data)


def test_users():
    goto_users(goto_user_page)


def test_add_user():
    add_users(button, name="test2", u_type="Customer", email="test@gamil.com", detail="test", phone="00000111100",
              address="test", **add_new_user)
    search_user(search_="test2", **search_user_data)


def test_edit_user_detail():
    edit_user_detail(name_="test1", u_type_="SiteAdmin", email_="test1@gmail.com", phone_="123456789", add="test1",
                     flat_no="102", **edit_user_data)
    search_user(search_="test1", **search_user_data)


def test_user_detail():
    users_detail(**get_user_data)


def test_delete_user():
    delete_user(**delete_user_detail)


def test_reservation():
    goto_reservations(goto_reservation_page)
    search_reservation(id_="Rahul Kumar", **search_reservation_data)
    get_reservation_details(**get_reservation_data)
    go_back_to_reservation(back_to_reservation_page)


def test_support():
    goto_support()


def test_logs():
    goto_logs()


def test_logout():
    goto_logout()
    driver.close()
