import os

def shutdown():
    confirm = input("Do you want to shutdown? (yes/no): ")
    
    if confirm.lower() == "yes":
        print("Shutting down...")
        os.system("shutdown /s /t 1")
    else:
        print("Cancelled.")

shutdown()