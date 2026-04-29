import numpy as np
import matplotlib.pyplot as plt
import os

# Categories
labels = ['Software Dev', 'ML & AI', 'Data Mgmt', 'Critical Thinking', 'Communication', 'Lifelong Learning']
num_vars = len(labels)

# Data
target = [2, 3, 2, 3, 3, 3]
ai = [4, 4, 3, 4, 3, 4]
self_eval = [4, 4, 3, 4, 4, 4]
advisor = [3, 4, 3, 4, 4, 3]

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

def make_radar_chart(title, datasets, filename):
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # Draw one axe per variable and add labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)
    
    # Set y-axis limits (0 to 4 since levels are 1 to 4)
    ax.set_ylim(0, 4)
    ax.set_yticks([1, 2, 3, 4])
    ax.set_yticklabels(['1', '2', '3', '4'], color="grey", size=8)
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    
    for i, (name, data) in enumerate(datasets.items()):
        data = data + data[:1]  # Complete the loop
        ax.plot(angles, data, color=colors[i], linewidth=2, linestyle='solid', label=name)
        ax.fill(angles, data, color=colors[i], alpha=0.1)
        
        # Ensure 'assets/eval' dir exists
    if not os.path.exists('assets/eval'):
        os.makedirs('assets/eval')
        
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.title(title, size=14, y=1.1)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()

# 1. Target vs AI
datasets1 = {
    'Target Level': target,
    'AI Evaluation': ai
}
make_radar_chart('Program Targets vs AI Evaluation', datasets1, 'assets/eval/radar_ai_target.png')

# 2. Target vs AI vs Self
datasets2 = {
    'Target Level': target,
    'AI Evaluation': ai,
    'Self-Evaluation': self_eval
}
make_radar_chart('Targets vs AI vs Self', datasets2, 'assets/eval/radar_ai_target_self.png')

# 3. Target vs AI vs Self vs Advisor
datasets3 = {
    'Target Level': target,
    'AI Evaluation': ai,
    'Self-Evaluation': self_eval,
    'Advisor Evaluation': advisor
}
make_radar_chart('Comprehensive Evaluation Comparison', datasets3, 'assets/eval/radar_comprehensive.png')

print("Updated radar charts generated in assets/eval/ with Lifelong Learning")
