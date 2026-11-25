# Verified count: 131 characters, 1 line.
LINE = "I am a pigeon with a corner office on your balcony. I bring the city to you, one crumb at a time, no rent, no meetings, just vibes."

import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)
