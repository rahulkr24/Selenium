# constant
button = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]"
# add_button = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]"
# edit_button = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]"
# edit_pod_button= "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]"
# add_user_button = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]",
# edit_user_button = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]"


location_count = "/html[1]/body[1]/div[1]/div[3]/div[1]/h1[1]/div[1]"
pod_count = "/html[1]/body[1]/div[1]/div[3]/div[2]/h1[1]/div[1]"

user_count = "/html[1]/body[1]/div[1]/div[3]/div[3]/h1[1]/div[1]"
reservation_count = "/html[1]/body[1]/div[1]/div[3]/div[4]/h1[1]/div[1]"

location_button = {"location_path": "/html[1]/body[1]/div[2]/div[2]/div[1]/button[2]"}

add_new_location = {"loc_name": "test1", "add": "test1", "pin": "000000", "pri_name": "Qikpod",
                    "prin_contact": "9876543212",
                    "loc_name_path1": "/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/input[1]",
                    "address_path2": "/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[4]/div[1]/input[1]",
                    "pincode_path3": "/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[6]/div[1]/input[1]",
                    "pri_name_path4": "/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[8]/div[1]/input[1]",
                    "prin_contact_path5": "/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[10]/div[1]/input[1]",
                    "proceed_button": "/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[11]/div[1]/button[1]",
                    "ok_button": "/html[1]/body[1]/div[5]/div[2]/div[2]/button[1]"}

search_data = {"search_path": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]",
               "view_button": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[5]/button[1]"}

create_user_location = {"create_button": "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]",
                        "c_name_xpath": "/html[1]/body[1]/div[7]/div[3]/div[1]/div[1]/div[2]/div[1]/input[1]",
                        "type_xpath": "/html[1]/body[1]/div[7]/div[3]/div[1]/div[1]/div[4]/div[1]/select[1]",
                        "email_xpath": "/html[1]/body[1]/div[7]/div[3]/div[1]/div[1]/div[6]/div[1]/input[1]",
                        "phone_xpath": "/html[1]/body[1]/div[7]/div[3]/div[1]/div[1]/div[8]/div[1]/input[1]",
                        "address_xpath": "/html[1]/body[1]/div[7]/div[3]/div[1]/div[1]/div[10]/div[1]/input[1]",
                        "cancel_button": "/html[1]/body[1]/div[7]/div[3]/div[1]/div[1]/div[11]/div[1]/button[1]"}
# constant edit button
edit_user = {
    "loc_name_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/input[1]",
    "add_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]/input[1]",
    "pin_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[6]/div[1]/input[1]",
    "pri_name_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[8]/div[1]/input[1]",
    "prin_contact_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[10]/div[1]/input[1]",
    "update_button": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[11]/div[1]/button[1]",
    "yes_button": "/html[1]/body[1]/div[5]/div[2]/div[2]/button[1]"}

delete_location_data = {"delete_button": "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/button[1]",
                        "confirm_button": "/html[1]/body[1]/div[8]/div[2]/div[2]/button[1]"}

pod_button = "/html[1]/body[1]/div[3]/div[2]/div[1]/button[3]"

pod_dashboard_monitor = {"total_pod": "/html[1]/body[1]/div[1]/div[3]/div[2]/h1[1]/div[1]",
                         "deployed_pod": "/html[1]/body[1]/div[1]/div[3]/div[3]/h1[1]/div[1]",
                         "lab_pod": "/html[1]/body[1]/div[1]/div[3]/div[4]/h1[1]/div[1]",
                         "yellow_pod": "/html[1]/body[1]/div[1]/div[4]/div[4]/h1[1]/div[1]",
                         "green_pod": "/html[1]/body[1]/div[1]/div[4]/div[1]/h1[1]/div[1]",
                         "red_pod": "/html[1]/body[1]/div[1]/div[4]/div[2]/h1[1]/div[1]",
                         "orange_pod": "/html[1]/body[1]/div[1]/div[4]/div[3]/h1[1]/div[1]",
                         "active_pod": "/html[1]/body[1]/div[1]/div[5]/div[1]/h1[1]/div[1]",
                         "inactive_pod": "/html[1]/body[1]/div[1]/div[5]/div[2]/h1[1]/div[1]",
                         "unregistered_pod": "/html[1]/body[1]/div[1]/div[5]/div[3]/h1[1]/div[1]",
                         "certified_pod": "/html[1]/body[1]/div[1]/div[5]/div[4]/h1[1]/div[1]"}

register_new_pod = {"register_pod_button": "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[3]/button[1]",
                    "serial_no_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/input[1]",
                    "model_no_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]/input[1]",
                    "total_pod_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[6]/div[1]/input[1]",
                    "proceed_button": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[7]/div[1]/button[1]",
                    "ok_button": "/html[1]/body[1]/div[6]/div[2]/div[2]/button[1]"}

search_pod_data = {"search_xpath": "//input[@placeholder='Search']",
                   "view_button": "/html[1]/body[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/button[1]"}

checkbox_unselect1 = "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/input[1]"

edit_pod_detail = {
    "flag_button": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]/select[1]",
    "pod_state_button": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[6]/div[1]/select[1]",
    "pod_status": "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[2]/div[1]/select[1]",
    "update_button": "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[3]/div[1]/button[1]"}

get_pod_data = {"xpath_id_": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[7]/div[1]",
                "xpath_door": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[13]/div[1]",
                "xpath_current": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[8]/div[1]",
                "xpath_target": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[15]/div[1]",
                "xpath_health": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[9]/div[1]",
                "xpath_state": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[14]/div[1]",
                "xpath_power": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[16]/div[1]",
                "xpath_mac_add": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[23]/div[1]",
                "xpath_pod_wifi": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[28]/div[1]",
                "xpath_created": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[24]/div[1]",
                "xpath_updated": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[29]/div[1]",
                "xpath_location": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[26]/div[1]",
                "xpath_spot": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[30]/div[1]"}

delete_pod_data = {"delete_pod_button": "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/button[1]",
                   "confirm_button": "/html[1]/body[1]/div[5]/div[2]/div[2]/button[1]"}

goto_user_page = "/html[1]/body[1]/div[3]/div[2]/div[1]/button[4]"

add_new_user = {
    "a_name_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/input[1]",
    "u_type_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]/select[1]",
    "email_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[6]/div[1]/input[1]",
    "detail_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[8]/div[1]/input[1]",
    "phone_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[10]/div[1]/input[1]",
    "address_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[12]/div[1]/input[1]",
    "confirm_button": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[13]/div[1]/button[1]",
    "ok_button": "/html[1]/body[1]/div[6]/div[2]/div[2]/button[1]"}

search_user_data = {"search_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]",
                    "view_button": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/button[1]"}

get_user_data = {"get_name": "/html[1]/body[1]/div[1]/div[3]/div[1]/h1[1]/div[1]",
                 "get_email_": "/html[1]/body[1]/div[1]/div[3]/div[1]/h3[1]/div[1]",
                 "get_mobile": "/html[1]/body[1]/div[1]/div[3]/div[1]/h3[2]/div[1]",
                 "get_user_type": "/html[1]/body[1]/div[1]/div[3]/div[1]/h3[3]/div[1]",
                 "get_loc_count": "/html[1]/body[1]/div[1]/div[3]/div[2]/h1[1]/div[1]",
                 "get_reservation": "/html[1]/body[1]/div[1]/div[3]/div[3]/h1[1]/div[1]"}

edit_user_data = {
    "name_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/input[1]",
    "u_type_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]/select[1]",
    "email_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[6]/div[1]/input[1]",
    "phone_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[8]/div[1]/input[1]",
    "add_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[10]/div[1]/input[1]",
    "flat_no_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[12]/div[1]/input[1]",
    "update_button": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[13]/div[1]/button[1]",
    "ok_button": "/html[1]/body[1]/div[5]/div[2]/div[2]/button[1]"}

delete_user_detail = {"delete_button": "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/button[1]",
                      "ok_button": "/html[1]/body[1]/div[6]/div[2]/div[2]/button[1]"}

goto_reservation_page = "/html[1]/body[1]/div[3]/div[2]/div[1]/button[5]"

search_reservation_data = {
    "search_xpath": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]",
    "view_button": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/button[1]"}

get_reservation_data = {"xpath_reserve_for": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[4]/div[1]",
                        "xpath_drop_by": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[3]/div[1]",
                        "xpath_created_by": "/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]",
                        "xpath_pod_id": "/html[1]/body[1]/div[1]/div[3]/div[2]/div[2]/div[1]",
                        "xpath_loc": "/html[1]/body[1]/div[1]/div[3]/div[2]/div[5]/div[1]",
                        "xpath_status": "/html[1]/body[1]/div[1]/div[3]/div[2]/div[4]/div[1]",
                        "xpath_awb": "/html[1]/body[1]/div[1]/div[3]/div[3]/div[3]/div[1]",
                        "xpath_exp_date": "/html[1]/body[1]/div[1]/div[3]/div[3]/div[4]/div[1]",
                        "xpath_spot": "/html[1]/body[1]/div[1]/div[3]/div[3]/div[2]/div[1]",
                        "xpath_user_num": "/html[1]/body[1]/div[1]/div[4]/div[1]/div[2]/div[1]",
                        "xpath_drop_by_num": "/html[1]/body[1]/div[1]/div[4]/div[1]/div[3]/div[1]",
                        "xpath_created_by_num": "/html[1]/body[1]/div[1]/div[4]/div[1]/div[4]/div[1]",
                        "xpath_pod_name": "/html[1]/body[1]/div[1]/div[4]/div[2]/div[4]/div[1]",
                        "xpath_door": "/html[1]/body[1]/div[1]/div[4]/div[2]/div[3]/div[1]",
                        "xpath_pod_status": "/html[1]/body[1]/div[1]/div[4]/div[2]/div[2]/div[1]",
                        "xpath_drop_otp": "/html[1]/body[1]/div[1]/div[4]/div[3]/div[3]/div[1]",
                        "xpath_pickup_otp": "/html[1]/body[1]/div[1]/div[4]/div[3]/div[4]/div[1]",
                        "xpath_rto_otp": "/html[1]/body[1]/div[1]/div[4]/div[3]/div[5]/div[1]"}

back_to_reservation_page = "/html[1]/body[1]/div[5]/div[2]/div[1]/button[5]"
