import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv('stereotype_results.csv')

# Create a crosstab of model_name and label_str
model_label_counts = pd.crosstab(df['model_name'], df['label_str'])

print("Model-by-Model Breakdown of Responses by Label:")
print("="*70)
print(model_label_counts)
print("\n")

# Calculate percentages
model_label_pct = pd.crosstab(df['model_name'], df['label_str'], normalize='index') * 100
print("Percentages (by model):")
print("="*70)
print(model_label_pct.round(2))
print("\n")

# Create grouped bar chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Raw counts
model_label_counts.plot(kind='bar', ax=ax1, color=['#F18F01', '#2E86AB', '#A23B72'])
ax1.set_title('Model Responses by Label (Counts)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Model', fontsize=12)
ax1.set_ylabel('Count', fontsize=12)
ax1.legend(title='Label', bbox_to_anchor=(1.05, 1), loc='upper left')
ax1.grid(axis='y', alpha=0.3)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')

# Add value labels on bars
for container in ax1.containers:
    ax1.bar_label(container, fmt='%d', padding=3)

# Plot 2: Percentages
model_label_pct.plot(kind='bar', ax=ax2, color=['#F18F01', '#2E86AB', '#A23B72'])
ax2.set_title('Model Responses by Label (Percentages)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Model', fontsize=12)
ax2.set_ylabel('Percentage (%)', fontsize=12)
ax2.legend(title='Label', bbox_to_anchor=(1.05, 1), loc='upper left')
ax2.grid(axis='y', alpha=0.3)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')

# Add value labels on bars
for container in ax2.containers:
    ax2.bar_label(container, fmt='%.1f%%', padding=3)

plt.tight_layout()
plt.savefig('model_breakdown.png', dpi=300, bbox_inches='tight')
print("Chart saved as 'model_breakdown.png'")
plt.show()

# Additional statistics
print("\n" + "="*70)
print("Summary Statistics by Model:")
print("="*70)
for model in df['model_name'].unique():
    model_data = df[df['model_name'] == model]
    total = len(model_data)
    print(f"\n{model}:")
    print(f"  Total responses: {total}")
    for label in ['agree', 'disagree', 'unclear']:
        count = len(model_data[model_data['label_str'] == label])
        pct = (count / total) * 100
        print(f"  {label.capitalize()}: {count} ({pct:.1f}%)")
