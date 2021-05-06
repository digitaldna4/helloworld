import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel, "text": text}
    )

    print(response)

mytoken = "xoxb-2036634018387-2036676528211-yomma5ZcAwexQ9aQjJ9dmbCU"
post_message(mytoken, "#coin", "HelloWorld")
