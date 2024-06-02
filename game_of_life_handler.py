from bottle import response
import json

snapshots = {}

def snapshot(data):
    global snapshots
    try:
        snapshot = data.get('snapshot')
        if snapshot is not None:
            
            snapshots["1"] = snapshot
            
            print("Received snapshot:", snapshot)
            response.content_type = 'application/json'
            return json.dumps({"message": "Snapshot saved successfully."})
        else:
            response.status = 400
            return json.dumps({"message": "No snapshot provided."})
    except Exception as e:
        response.status = 500
        return json.dumps({"message": "Server error: " + str(e)})
    
def get_snapshot(name):
    global snapshots
    try:
        snapshot = snapshots[name]
        response.content_type = 'application/json'
        return dict(data=snapshot)  
    except Exception as e:
        response.status = 500
        return json.dumps({"message": "Server error: " + str(e)})