import base64

encoded_string = "5uViw_EXL3b8VJS6uITtept8Gw7kJqOt5J9lebB-qQ_IOEL8F0HtBv9kICa-faT3BlbkFJgioCdmHY63kMFSKgLmQAkTA_nZqKerSeyAkEf6g2JPwcRnR1i6UOr3SoR3z8xbaCRkY8KR8UIA"
try:
    decoded = base64.b64decode(encoded_string)
    print("Decoded string:", decoded)
except Exception as e:
    print("Not valid Base64 or something else:", e)
