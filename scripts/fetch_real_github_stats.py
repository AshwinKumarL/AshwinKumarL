import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://github.com/users/AshwinKumarL/contributions'

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as res:
    html = res.read().decode('utf-8')

# Match total contributions in last year
total_match = re.search(r'([\d,]+)\s+contributions\s+in\s+the\s+last\s+year', html)
total_year = int(total_match.group(1).replace(',', '')) if total_match else 60

tooltips = re.findall(r'<tool-tip[^>]*>(.*?)</tool-tip>', html, re.DOTALL)
print(f"Total calendar cells: {len(tooltips)}")

days_data = []
for t in tooltips:
    t_clean = t.strip()
    m = re.search(r'(\d+|No)\s+contribution[s]?\s+on\s+([A-Za-z]+)\s+(\d+)(?:st|nd|rd|th)?', t_clean)
    if m:
        cnt = 0 if m.group(1) == 'No' else int(m.group(1))
        month = m.group(2)
        day = int(m.group(3))
        date_str = f"{month} {day}"
        days_data.append((date_str, cnt))

print(f"Successfully parsed {len(days_data)} days!")

active_days = [d for d in days_data if d[1] > 0]
print(f"Total active contribution days: {len(active_days)}")
for d in active_days:
    print(f"  {d[0]}: {d[1]} commits")

best_day = max(days_data, key=lambda x: x[1]) if days_data else ('N/A', 0)
this_week = sum(d[1] for d in days_data[-7:]) if len(days_data) >= 7 else 0

# Calculate longest and current streak
longest = 0
curr_temp = 0
for d in days_data:
    if d[1] > 0:
        curr_temp += 1
        longest = max(longest, curr_temp)
    else:
        curr_temp = 0

current_streak = 0
for d in reversed(days_data):
    if d[1] > 0:
        current_streak += 1
    elif current_streak > 0:
        break

print("\n================ EXACT REAL METRICS ================")
print(f"Total Contributions (Year): {total_year}")
print(f"This Week (Last 7 days):   {this_week}")
print(f"Best Day:                  {best_day[1]} ({best_day[0]})")
print(f"Longest Streak:            {longest} days")
print(f"Current Streak:            {current_streak} days")
print("====================================================")

# Save actual day-by-day counts into a 52x7 grid
grid_counts = np.zeros((52, 7), dtype=int) if 'np' in locals() else None

with open('scripts/real_stats.json', 'w', encoding='utf-8') as f:
    json.dump({
        'total': total_year,
        'this_week': this_week,
        'best_day_count': best_day[1],
        'best_day_date': best_day[0],
        'longest_streak': longest,
        'current_streak': current_streak,
        'daily_counts': [d[1] for d in days_data]
    }, f, indent=2)
