import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('stereotype_results.csv')

# Count occurrences of each label_str
label_counts = df['label_str'].value_counts()

# Print the counts
print("Label counts:")
print(label_counts)
print(f"\nTotal responses: {len(df)}")

# Create bar plot
plt.figure(figsize=(10, 6))
label_counts.plot(kind='bar', color=['#2E86AB', '#A23B72', '#F18F01'])
plt.title('Distribution of Label Responses', fontsize=14, fontweight='bold')
plt.xlabel('Label', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Add count labels on top of bars
for i, v in enumerate(label_counts):
    plt.text(i, v + 0.5, str(v), ha='center', va='bottom', fontweight='bold')

plt.savefig('label_distribution.png', dpi=300, bbox_inches='tight')
print("\nBar plot saved as 'label_distribution.png'")
plt.show()

# Filter rows where label_str is "agree"
agree_rows = df[df['label_str'] == 'agree']

print(f"\n{'='*80}")
print(f"Rows where label_str = 'agree' ({len(agree_rows)} total):")
print(f"{'='*80}\n")

# Display agree rows with relevant columns
if len(agree_rows) > 0:
    display_cols = ['item_index', 'stereotype_topic', 'target_group', 
                    'stereotype_template', 'model_name', 'label_str', 'label_int']
    print(agree_rows[display_cols].to_string(index=False))
    
    # Save to CSV
    agree_rows.to_csv('agree_responses.csv', index=False)
    print(f"\n\nAgree responses saved to 'agree_responses.csv'")
else:
    print("No rows found with label_str = 'agree'")
