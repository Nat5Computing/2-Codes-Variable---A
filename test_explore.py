import subprocess

def test_variables_explore():
    try:
        result = subprocess.run(["python3", "variables_explore.py"], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ Your program crashed and could not run.")
            print("🔧 Error message:")
            print(result.stderr.strip())
            return
    except Exception as e:
        print("❌ Something went wrong while running your code.")
        print(f"Error: {e}")
        return

    print("✅ Your program ran successfully! Now try editing and testing variable names.")
    
if __name__ == "__main__":
    test_variables_explore()
