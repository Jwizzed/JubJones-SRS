import matplotlib.pyplot as plt
import numpy as np

# Data from Tracking Performance Table (ID Switches column)
cameras = ['c09', 'c12', 'c13', 'c16', 'c01', 'c02', 'c05']
baseline = [154, 98, 112, 142, 212, 154, 186]
spoton = [6, 1, 1, 42, 48, 3, 0]

x = np.arange(len(cameras))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 5.5))

# Plot bars
rects1 = ax.bar(x - width/2, baseline, width, label='Baseline', color='#E8734A', edgecolor='#333333', linewidth=0.8)
rects2 = ax.bar(x + width/2, spoton, width, label='SpotOn (Optimized)', color='#4A90D9', edgecolor='#333333', linewidth=0.8)

# Axis labels
ax.set_ylabel('Total Identity Switches', fontsize=13, fontweight='bold')
ax.set_xlabel('Camera', fontsize=13, fontweight='bold')
ax.set_title('Impact of Spatial Matching on Identity Switches', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(cameras, fontsize=12)
ax.set_ylim(0, 250)

# Legend - top left, out of the way of data
ax.legend(fontsize=11, loc='upper left', framealpha=0.95)

# Add value labels on top of each bar
for rect in rects1:
    h = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, h + 4, str(h),
            ha='center', va='bottom', fontsize=10, fontweight='bold', color='#333333')

for rect in rects2:
    h = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, h + 4, str(h),
            ha='center', va='bottom', fontsize=10, fontweight='bold', color='#333333')

# Environment separator
ax.axvline(x=3.5, color='gray', linestyle='--', linewidth=1.5)
ax.text(1.5, 235, 'Factory', ha='center', va='center', fontsize=12, fontweight='bold',
        bbox=dict(facecolor='white', alpha=0.9, edgecolor='gray', boxstyle='round,pad=0.3'))
ax.text(5.0, 235, 'Campus', ha='center', va='center', fontsize=12, fontweight='bold',
        bbox=dict(facecolor='white', alpha=0.9, edgecolor='gray', boxstyle='round,pad=0.3'))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.tight_layout()
plt.savefig('/Users/krittinsetdhavanich/Documents/spoton/JubJones-SRS/JCSSE PAPER/ablation_figure_5.png', dpi=300, bbox_inches='tight')
print("Saved ablation_figure_5.png successfully.")
