import os
import random
import time
from datetime import datetime, timedelta
import subprocess

# =========================
# CONFIG
# =========================
REPO_PATH = "/workspaces/intro-to-data-science"
TARGET_FOLDER = "/workspaces/intro-to-data-science/Py-programming-concepts"
GITHUB_EMAIL = "naeemullahmehmoodasghar@gmail.com"

# human-like behavior config
MIN_COMMITS_PER_DAY = 1
MAX_COMMITS_PER_DAY = 4
ACTIVE_DAYS_RANGE = (12, 22)   # days in month
TIME_GAP_RANGE = (20, 180)     # seconds between commits

# =========================
# UTILS
# =========================

def run(cmd):
    subprocess.run(cmd, shell=True, cwd=REPO_PATH)

def random_datetime_last_30_days():
    now = datetime.now()
    days_back = random.randint(1, 30)
    random_day = now - timedelta(days=days_back)
    random_time = random.randint(9, 22)  # active hours
    random_min = random.randint(0, 59)
    random_sec = random.randint(0, 59)
    return random_day.replace(hour=random_time, minute=random_min, second=random_sec)

def get_all_files(folder):
    files = []
    for root, dirs, filenames in os.walk(folder):
        for f in filenames:
            if not f.startswith("."):
                files.append(os.path.join(root, f))
    return files

def create_random_file():
    filename = f"auto_{int(time.time())}_{random.randint(100,999)}.txt"
    path = os.path.join(TARGET_FOLDER, filename)
    with open(path, "w") as f:
        f.write(f"Auto generated content at {datetime.now()}\n")
        f.write(f"Random value: {random.random()}\n")
    return path

def modify_file(file_path):
    with open(file_path, "a") as f:
        f.write(f"\nUpdate at {datetime.now()} | rand={random.randint(1,9999)}")

def make_commit(commit_time):
    commit_time_str = commit_time.strftime("%Y-%m-%d %H:%M:%S")

    os.environ["GIT_AUTHOR_DATE"] = commit_time_str
    os.environ["GIT_COMMITTER_DATE"] = commit_time_str
    os.environ["GIT_AUTHOR_EMAIL"] = GITHUB_EMAIL
    os.environ["GIT_COMMITTER_EMAIL"] = GITHUB_EMAIL

    run("git add .")
    run(f'git commit -m "auto update: {commit_time_str}"')

# =========================
# MAIN LOGIC
# =========================

def main():
    os.chdir(REPO_PATH)

    active_days = random.randint(ACTIVE_DAYS_RANGE[0], ACTIVE_DAYS_RANGE[1])
    print(f"[+] Active days: {active_days}")

    for day in range(active_days):
        commits_today = random.randint(MIN_COMMITS_PER_DAY, MAX_COMMITS_PER_DAY)
        print(f"[+] Day {day+1} -> commits: {commits_today}")

        for c in range(commits_today):
            files = get_all_files(TARGET_FOLDER)

            action = random.choice(["modify", "create"])

            if files and action == "modify":
                file_to_edit = random.choice(files)
                modify_file(file_to_edit)
                print(f"[edit] {file_to_edit}")
            else:
                new_file = create_random_file()
                print(f"[new] {new_file}")

            commit_time = random_datetime_last_30_days()
            make_commit(commit_time)

            sleep_time = random.randint(TIME_GAP_RANGE[0], TIME_GAP_RANGE[1])
            time.sleep(sleep_time)

    print("\n✅ Human-like automation commits completed!")
    print("➡ now run: git push origin main")

if __name__ == "__main__":
    main()
