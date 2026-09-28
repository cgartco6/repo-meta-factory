import sys
import subprocess

def lock_assessment_pipeline():
    print("🔒 RUNNING ABSOLUTE AGENCY REPOSITORY LOCKDOWN ASSESSMENTS...")
    # Fire isolated unit test suite passes across standalone architecture profiles
    result = subprocess.run(["pytest", "-v"], capture_output=True, text=True)
    
    print(result.stdout)
    if result.returncode != 0:
        print("🚨 SYSTEM CRITICAL UNHANDLED BUGS CAPTURED. REPOSITORY BLOCKED.")
        print(result.stderr)
        sys.exit(1)
        
    print("🏆 MASTER GATE PASSED: All local microservice modules are validated, clean, and safe for cloud release.")
    sys.exit(0)

if __name__ == "__main__":
    lock_assessment_pipeline()
