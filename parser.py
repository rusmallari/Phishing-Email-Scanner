from email import policy
from email.parser import BytesParser


def parse_eml(path):
    with open(path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    subject = msg["subject"]
    sender = msg["from"]

    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                try:
                    body += str(part.get_content())
                except Exception:
                    pass
    else:
        try:
            body = str(msg.get_content())
        except Exception:
            body = ""

    headers = str(msg)

    return {
        "subject": subject,
        "sender": sender,
        "body": body,
        "headers": headers
    }
