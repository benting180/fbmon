from flask import Flask, request, jsonify
import helper
import pandas as pd

app = Flask(__name__)

@app.route('/api/post_example', methods=['POST'])
def post_example():
    try:
        data = request.get_json()  # Assuming the data sent is in JSON format

        # Do something with the received data
        received_message = data.get('message', 'No message received')

        rows = jsonify(received_message).json

        df = pd.DataFrame.from_records(rows)

        df_filtered = helper.filter(df)

        msg = helper.df2msg(df_filtered)

        

        # You can perform any processing with the received data here
    except Exception as e:
        helper.send_telegram("something is wrong")
        response_data = {
        'status': 'fail'
    }
        
    helper.send_telegram(msg)
    response_data = {
        'status': 'success'
    }


    # helper.filter()
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)