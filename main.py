import requests
import json
import re
from urllib.parse import unquote
import uuid
import time

def login(Uid_or_email_or_number, password):
    """Perform login using contact_point and password"""
    headers = {
        'x-fb-ta-logging-ids': f'graphql:{str(uuid.uuid4())}',
        'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
        'x-graphql-client-library': 'graphservice',
        'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
        'x-fb-privacy-context': '3643298472347298',
        'content-type': 'application/x-www-form-urlencoded',
        'x-graphql-request-purpose': 'fetch',
        'x-fb-background-state': '1',
        'x-fb-sim-hni': '47002',
        'user-agent': '[FBAN/FB4A;FBAV/417.0.0.33.65;FBBV/480086166;FBDM/{density=3.0,width=1080,height=2165};FBLC/en_US;FBRV/0;FBCR/;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/LE2101;FBSV/14;FBOP/1;FBCA/arm64-v8a:;]',
        'x-fb-connection-type': 'WIFI',
        'x-fb-device-group': '5719',
        'x-tigon-is-retry': 'False',
        'priority': 'u=3,i',
        'x-fb-http-engine': 'Liger',
        'x-fb-client-ip': 'True',
        'x-fb-server-cluster': 'True',
    }

    # Generate timestamps and IDs
    current_timestamp = int(time.time())
    device_id = str(uuid.uuid4())
    waterfall_id = str(uuid.uuid4())
    secure_family_device_id = str(uuid.uuid4())
    client_trace_id = str(uuid.uuid4())
    qpl_instance_id = int(time.time() * 1000000000000)

    # Format password: #PWD_FB4A:0:{timestamp}:{password}
    # If password already starts with #PWD_FB4A, use it as is
    if not password.startswith('#PWD_FB4A'):
        password_timestamp = int(time.time())
        formatted_password = f"#PWD_FB4A:0:{password_timestamp}:{password}"
    else:
        formatted_password = password

    # Build the nested variables structure
    client_input_params = {
        "aac": json.dumps({"aac_init_timestamp": current_timestamp}),
        "sim_phones": [],
        "aymh_accounts": [],
        "network_bssid": None,
        "secure_family_device_id": secure_family_device_id,
        "has_granted_read_contacts_permissions": 0,
        "auth_secure_device_id": "",
        "has_whatsapp_installed": 0,
        "password": formatted_password,
        "sso_token_map_json_string": "",
        "block_store_machine_id": "",
        "cloud_trust_token": None,
        "event_flow": "login_manual",
        "password_contains_non_ascii": "false",
        "sim_serials": [],
        "client_known_key_hash": "",
        "encrypted_msisdn": "",
        "has_granted_read_phone_permissions": 0,
        "app_manager_id": "",
        "should_show_nested_nta_from_aymh": 0,
        "device_id": device_id,
        "zero_balance_state": "",
        "login_attempt_count": 1,
        "machine_id": "",
        "accounts_list": [],
        "family_device_id": device_id,
        "fb_ig_device_id": [],
        "device_emails": [],
        "try_num": 1,
        "lois_settings": {"lois_token": ""},
        "event_step": "home_page",
        "headers_infra_flow_id": "",
        "openid_tokens": {},
        "contact_point": Uid_or_email_or_number
    }

    server_params = {
        "should_trigger_override_login_2fa_action": 0,
        "is_vanilla_password_page_empty_password": 0,
        "is_from_logged_out": 0,
        "should_trigger_override_login_success_action": 0,
        "login_credential_type": "none",
        "server_login_source": "login",
        "waterfall_id": waterfall_id,
        "two_step_login_type": "one_step_login",
        "login_source": "Login",
        "is_platform_login": 0,
        "pw_encryption_try_count": 1,
        "INTERNAL__latency_qpl_marker_id": 36707139,
        "is_from_aymh": 0,
        "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
        "is_from_landing_page": 0,
        "left_nav_button_action": "NONE",
        "password_text_input_id": "vvqsmp:102",
        "is_from_empty_password": 0,
        "is_from_msplit_fallback": 0,
        "ar_event_source": "login_home_page",
        "username_text_input_id": "vvqsmp:101",
        "layered_homepage_experiment_group": None,
        "device_id": device_id,
        "INTERNAL__latency_qpl_instance_id": qpl_instance_id,
        "reg_flow_source": "login_home_native_integration_point",
        "is_caa_perf_enabled": 1,
        "credential_type": "password",
        "is_from_password_entry_page": 0,
        "caller": "gslr",
        "family_device_id": device_id,
        "is_from_assistive_id": 0,
        "access_flow_version": "pre_mt_behavior",
        "is_from_logged_in_switcher": 0
    }

    params = {
        "client_input_params": client_input_params,
        "server_params": server_params
    }

    variables = {
        "params": {
            "params": json.dumps({
                "params": json.dumps(params)
            }),
            "bloks_versioning_id": "c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec",
            "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
        },
        "scale": "3",
        "nt_context": {
            "using_white_navbar": True,
            "pixel_ratio": 3,
            "is_push_on": True,
            "styles_id": "e6c6f61b7a86cdf3fa2eaaffa982fbd1",
            "bloks_version": "c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec"
        }
    }

    data = {
        'method': 'post',
        'pretty': 'false',
        'format': 'json',
        'server_timestamps': 'true',
        'locale': 'en_US',
        'purpose': 'fetch',
        'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
        'fb_api_caller_class': 'graphservice',
        'client_doc_id': '11994080423068421059028841356',
        'variables': json.dumps(variables),
        'fb_api_analytics_tags': '["GraphServices"]',
        'client_trace_id': client_trace_id,
    }

    try:
        response = requests.post('https://b-graph.facebook.com/graphql', headers=headers, data=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error in login: {e}")
        return None

