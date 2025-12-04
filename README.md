# Facebook Login Automation Script

## Overview

This Python script demonstrates how Facebook's Android mobile app (FB4A) performs user authentication through their GraphQL API. It reverse-engineers the login flow to programmatically authenticate users.

## How It Works

### Function: `login(Uid_or_email_or_number, password)`

The main function accepts two parameters:
- **Uid_or_email_or_number**: User's email, phone number, or Facebook user ID
- **password**: Account password (plain text)

### Technical Breakdown

#### 1. **Request Headers**
The script constructs headers that mimic Facebook's official Android app (v417.0.0.33.65):

- **Authorization**: OAuth token for the Facebook app (`350685531728|...`)
- **User-Agent**: Identifies as Facebook Android app running on OnePlus device with Android 14
- **x-fb-friendly-name**: Specifies the GraphQL operation being called
- **x-fb-device-group**: Device group identifier (5719)
- Various tracking and analytics headers for Facebook's internal logging

#### 2. **Device Fingerprinting**
The script generates unique identifiers to mimic a real device:

```python
device_id = str(uuid.uuid4())              # Unique device identifier
waterfall_id = str(uuid.uuid4())           # Request tracking ID
secure_family_device_id = str(uuid.uuid4()) # Family device tracking
client_trace_id = str(uuid.uuid4())        # Client request trace
qpl_instance_id = int(time.time() * 1000000000000)  # Performance tracking
```

#### 3. **Password Formatting**
Facebook's Android app uses a special password format:

```
#PWD_FB4A:0:{timestamp}:{password}
```

- **#PWD_FB4A**: Prefix indicating Facebook Android app
- **0**: Encryption version/method identifier
- **{timestamp}**: Current Unix timestamp
- **{password}**: Plain text password

This format helps Facebook identify the source and timing of login attempts.

#### 4. **Request Parameters Structure**

The script builds a nested JSON structure with three main components:

**a) Client Input Parameters** (`client_input_params`):
- Authentication credentials (contact_point, password)
- Device information (device_id, family_device_id)
- Permission states (contacts, phone, WhatsApp)
- Login context (event_flow, event_step, try_num)
- Account associations (sim_phones, aymh_accounts)

**b) Server Parameters** (`server_params`):
- Login source tracking (server_login_source, login_source)
- Flow identifiers (waterfall_id, ar_event_source)
- Performance metrics (qpl_marker_id, qpl_instance_id)
- Feature flags and experiment groups
- UI element identifiers (password_text_input_id, username_text_input_id)

**c) Variables Wrapper**:
```python
variables = {
    "params": {
        "params": json.dumps({
            "params": json.dumps(params)  # Double-nested JSON
        }),
        "bloks_versioning_id": "...",  # Bloks UI framework version
        "app_id": "..."  # Specific Bloks screen identifier
    },
    "scale": "3",  # Screen density
    "nt_context": {...}  # UI context (navbar, pixel ratio, styles)
}
```

#### 5. **GraphQL Request**

The script makes a POST request to:
```
https://b-graph.facebook.com/graphql
```

With form-encoded data including:
- **method**: 'post'
- **fb_api_req_friendly_name**: The operation name
- **client_doc_id**: Document/query identifier
- **variables**: The nested JSON structure (stringified)
- **client_trace_id**: Request tracing

#### 6. **Response Handling**

The function returns the JSON response from Facebook's API, which typically contains:
- Authentication tokens (access_token, session_cookies)
- User information
- Error messages (if login fails)
- Additional security challenges (2FA, checkpoints)

### Key Features

- **Mimics Official App**: Uses exact headers and parameters from Facebook's Android app
- **Device Simulation**: Generates realistic device fingerprints
- **Bloks Framework**: Utilizes Facebook's internal Bloks UI framework for login
- **GraphQL API**: Communicates with Facebook's GraphQL endpoint instead of REST API
- **Timestamp Tracking**: Includes multiple timestamps for request correlation

### Endpoint Used

```
POST https://b-graph.facebook.com/graphql
```

This is Facebook's Business Graph API endpoint, used by mobile applications.

### Return Value

Returns a dictionary containing:
- Login success/failure status
- Access tokens and session data (if successful)
- Error codes and messages (if failed)
- Security challenge information (if required)

---

## ⚠️ Disclaimer

**This code is for educational and research purposes only.** Using automated access to Facebook may violate their Terms of Service and could result in account suspension or legal consequences. The author is not responsible for any misuse of this code. Always use official Facebook APIs and SDKs for legitimate applications. Unauthorized access to computer systems may be illegal under laws such as the Computer Fraud and Abuse Act (CFAA) and similar statutes worldwide.
