# chart.py

# Import required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data for product performance
np.random.seed(42)  # For reproducibility
products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
performance = np.random.randint(50, 100, size=len(products))

# Create a DataFrame
df = pd.DataFrame({"Product": products, "Performance": performance})

# Set figure size for 512x512 output
plt.figure(figsize=(8, 8))

# Create barplot
sns.barplot(
    x="Product",
    y="Performance",
    data=df,
    palette="Blues_d",
    edgecolor="black"
)

# Style the chart
plt.title("Product Performance Insights", fontsize=16, fontweight="bold")
plt.xlabel("Products", fontsize=12)
plt.ylabel("Performance Score", fontsize=12)
plt.xticks(rotation=30, fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Save chart as PNG (512x512 with dpi=64)
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches="tight")

# Show plot
plt.show()



