try:
    from pyrogram import Client as PClient
except:
    os.system("pip install pyrogram")
    from pyrogram import Client as PClient

try:
    from telethon.sessions import StringSession
    from telethon.sessions.string import (_STRUCT_PREFORMAT, CURRENT_VERSION,
                                          StringSession)
    from telethon.sync import TelegramClient
except:
    os.system("pip install telethon")
    from telethon.sessions import StringSession
    from telethon.sessions.string import (_STRUCT_PREFORMAT, CURRENT_VERSION,
                                          StringSession)
    from telethon.sync import TelegramClient


def main():
    print("T E A M    E X T E N D E D   ! !")
    print("Hello!! Welcome to Extended Session Generator\n")
    print("Human Verification Required !!")
    while True:
        verify = int(randint(1, 50))
        okvai = int(input(f"Enter {verify} to continue: "))
        if okvai == verify:
                    generate_hellbot_session()
        else:
            print("Verification Failed! Try Again:")


def generate_hellbot_session():
    print("!!! HELLBOT Extended SESSION !!!")
    print("One session for all HellBot's Project.")
    api_id = int(input("\nEnter APP ID here: "))
    api_hash = input("\nEnter API_HASH here: ")
    with PClient(name="helluser", api_id=api_id, api_hash=api_hash, in_memory=True) as hell:
        print("\nYour HELLBOT SESSION is saved in your telegram saved messages.")
        _session = hell.export_session_string()
        hell_session = hellbot_session(_session)
        hell.send_message(
            "me",
            f"#HELLEXTENDED_SESSION \n\n`{hell_session}`",
        )


def challenge_code(username, choice):
    while True:
        otp = input("Enter the OTP sent to your Email: ")
        if otp.isdigit():
            break
        else:
            print("Enter digits only!")
    return otp


def hellbot(text):
    res = ''.join(
        map(
            random.choice,
            zip(text.lower(), text.upper()),
        )
    )
    return res.strip()


def hellbot_session(session):
    pyro_format = {
        351: ">B?256sI?",
        356: ">B?256sQ?",
        362: ">BI?256sQ?",
    }

    ipv4_dc = {
        1: "149.154.175.53",
        2: "149.154.167.51",
        3: "149.154.175.100",
        4: "149.154.167.91",
        5: "91.108.56.130",
    }
   
    new_session = CURRENT_VERSION + StringSession.encode(
        struct.pack(
            _STRUCT_PREFORMAT.format(4),
            dc_id,
            ipaddress.ip_address(ipv4_dc[dc_id]).packed,
            443,
            auth_key
        )
    )
    return f"=={hellbot('hell')}{new_session}{hellbot('bot')}=="

main()  # Fix indentation error
