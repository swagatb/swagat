import requests
def send_simple_message():
    rer = requests.post(
        "https://api.mailgun.net/v3/sandbox62c36289bae940cf820489ad2f669e1e.mailgun.org/messages",
        auth=("api", "key-a699074712d6fe84bb626dbfb872fad7"),
        data={"from": "sambit <sambitk@hotmail.com>",
              "to": "bikram <bikram.b@hcl.com>",
              "subject": "Hello bikram",
              "text": "Test mail"})
    import ipdb;ipdb.set_trace()


def send_simple_message_a():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox6f14abf2132f4bb5a70d095d80fe0a78.mailgun.org/messages",
        auth=("api", "key-ea87f55913f3938785c1ab7887b5e7b3"),
        data={"from": "sambit <sambitk@hotmail.com>",
              "to": ["bikram <bikram.b@hcl.com>"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
if __name__=="__main__":
    si=send_simple_message_a()
    import ipdb;ipdb.set_trace()
