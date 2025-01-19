from queue import Queue
import random
import time

request_queue = Queue()

def generate_request():
    request_id = f"Request-{random.randint(1000, 9999)}"
    request_queue.put(request_id)
    print(f"Request {request_id} added to the queue.")

# Function to process a request
def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Processing request {request_id}...")
        time.sleep(1)
        print(f"Request {request_id} has been processed.")
    else:
        print("The queue is empty. No requests to process.")

# Main program loop
def main():
    print("Request processing system started. Press Ctrl+C to exit.")
    try:
        while True:
            action = random.choice(["generate", "process"])
            if action == "generate":
                generate_request()
            else:
                process_request()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nRequest processing system terminated.")

if __name__ == "__main__":
    main()
