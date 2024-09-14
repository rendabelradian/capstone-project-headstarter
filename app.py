from flask import Flask, request, jsonify
import datetime
import random

app = Flask(__name__)

# In-memory database for simplicity
bathroom_schedule = []

# AI Logic: Simple logic to find optimal time slots
def find_optimal_slot():
    # Placeholder AI logic: Returns a random time slot
    current_time = datetime.datetime.now()
    slot = current_time + datetime.timedelta(minutes=random.randint(1, 60))
    return slot.strftime("%Y-%m-%d %H:%M")

@app.route('/schedule', methods=['POST'])
def schedule_bathroom():
    user_data = request.json
    user_id = user_data.get('user_id')
    
    # Apply AI logic to find the optimal slot
    optimal_slot = find_optimal_slot()
    
    # Store the schedule
    bathroom_schedule.append({
        'user_id': user_id,
        'time_slot': optimal_slot
    })
    
    return jsonify({
        'status': 'success',
        'scheduled_time': optimal_slot
    })

@app.route('/get_schedule', methods=['GET'])
def get_schedule():
    return jsonify(bathroom_schedule)

if __name__ == '__main__':
    app.run(debug=True)
