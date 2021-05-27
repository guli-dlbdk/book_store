
from app import app

if __name__ == '__main__':
    # dummy certificate -- pip3 install pyopenssl
    
    #app.run(host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')

    app.run(host='0.0.0.0', port=5000, debug=True)
