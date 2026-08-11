import subprocess
import os

cartoon_dir = r"c:\Work\HowlabScienceLab\images\tokyo_2026_cartoon"
thumb_dir = r"c:\Work\HowlabScienceLab\images\tokyo_2026_cartoon_thumb"

def run_cmd(cmd):
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=r"c:\Work\HowlabScienceLab")
    return res.stdout, res.stderr

# Get untracked / modified files
stdout, _ = run_cmd(["git", "status", "--porcelain"])
lines = stdout.splitlines()

files_to_add = []
for line in lines:
    status = line[:2]
    filename = line[3:].strip('"')
    if status.strip() in ['??', 'M', 'A']:
        if os.path.isfile(os.path.join(r"c:\Work\HowlabScienceLab", filename)):
            files_to_add.append(filename)
        elif os.path.isdir(os.path.join(r"c:\Work\HowlabScienceLab", filename)):
            for root, _, files in os.walk(os.path.join(r"c:\Work\HowlabScienceLab", filename)):
                for f in files:
                    rel = os.path.relpath(os.path.join(root, f), r"c:\Work\HowlabScienceLab").replace('\\', '/')
                    files_to_add.append(rel)

print(f"Total untracked/modified files found: {len(files_to_add)}")

batch_size = 20
for i in range(0, len(files_to_add), batch_size):
    chunk = files_to_add[i:i+batch_size]
    print(f"Committing batch {i//batch_size + 1}/{(len(files_to_add) + batch_size - 1)//batch_size} ({len(chunk)} files)...")
    run_cmd(["git", "add"] + chunk)
    stdout, stderr = run_cmd(["git", "commit", "-m", f"chore: upload assets batch ({len(chunk)} files)"])
    print(stdout)
    if stderr:
        print("STDERR:", stderr)

print("Batch commit complete.")
