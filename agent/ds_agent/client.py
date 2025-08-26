import argparse, csv, json, random, time
import urllib.request

def post_json(url, data):
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--backend", default="http://localhost:8000")
    p.add_argument("--dataset", type=int, default=1)
    p.add_argument("--csv", type=str, help="CSV path with columns x,y (optional)")
    p.add_argument("--random", type=int, default=0, help="Send N random rows")
    args = p.parse_args()

    rows = []
    if args.csv:
        with open(args.csv, newline="") as f:
            for r in csv.DictReader(f):
                rows.append({k: float(v) for k,v in r.items() if v != ""})
    if args.random:
        for _ in range(args.random):
            rows.append({"x": random.gauss(0,1), "y": random.gauss(2,0.5)})
    if not rows:
        print("No data to send"); return

    for r in rows:
        payload = {"dataset_id": args.dataset, "payload": r}
        try:
            out = post_json(f"{args.backend}/ingest/event", payload)
            # Simple pacing
            time.sleep(0.01)
        except Exception as e:
            print("Error:", e)
            break
    print(f"Sent {len(rows)} rows.")

if __name__ == "__main__":
    main()
