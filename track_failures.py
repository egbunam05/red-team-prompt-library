
import json
import argparse
from collections import Counter

def load_logs(path):
    logs = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                logs.append(json.loads(line))
    return logs

def generate_report(logs):
    total_attacks = len(logs)
    if total_attacks == 0:
        return
        
    failures = [log for log in logs if log.get("failed")]
    total_failures = len(failures)
    
 
    vuln_score = (total_failures / total_attacks) * 100
    
   
    failure_modes = [log.get("failure_mode") for log in failures]
    mode_counts = Counter(failure_modes)
    
  
    categories = [log.get("category") for log in logs]
    cat_counts = Counter(categories)

    print("=== Red-Team Vulnerability Report ===")
    print(f"Total Attacks Executed: {total_attacks}")
    print(f"Successful Defenses:   {total_attacks - total_failures}")
    print(f"Model Failures:        {total_failures}")
    print(f"Vulnerability Score:   {vuln_score:.1f}%\n")
    
    print("=== Breakdown by Attack Category ===")
    for cat, count in cat_counts.items():
        print(f"- {cat}: {count} attacks")
        
    print("\n=== Root Cause Failure Modes ===")
    for mode, count in mode_counts.most_common():
        if mode != "None":
            print(f"⚠️ {mode}: {count} occurrences")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to JSONL log file")
    args = parser.parse_args()
    
    logs = load_logs(args.input)
    generate_report(logs)
