import pandas as pd
import matplotlib.pyplot as plt

csv_file = 'training_progress.csv'
df = pd.read_csv(csv_file)
df.columns = df.columns.str.strip()

x = pd.to_numeric(df['iteration'], errors='coerce')
avg_score = pd.to_numeric(df['avg_score'], errors='coerce')
avg_chain_per_event = pd.to_numeric(df['avg_chain_per_event'], errors='coerce')
max_chain = pd.to_numeric(df['max_chain'], errors='coerce')
no_chain_rate = df['no_chain_rate'].str.rstrip('%').astype(float)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1. 平均スコア
ax = axes[0, 0]
ax.plot(x, avg_score, label='Avg Score', color='tab:blue', marker='o')
ax.set_title('Average Score')
ax.set_xlabel('Iteration')
ax.set_ylabel('Score')
ax.set_ylim(bottom=0)  # y軸0スタート
ax.grid(True)

# 2. 平均連鎖/イベント（軸の下限を1.00に指定）
ax = axes[0, 1]
ax.plot(x, avg_chain_per_event, label='Avg Chain/Event', color='tab:green', marker='s')
ax.set_title('Average Chain per Event')
ax.set_xlabel('Iteration')
ax.set_ylabel('Avg Chain')
ax.set_ylim(bottom=1.00)  # y軸1.00スタート
ax.grid(True)

# 3. 最大連鎖（軸下限0・整数目盛化）
ax = axes[1, 0]
ax.plot(x, max_chain, label='Max Chain', color='tab:orange', marker='^')
ax.set_title('Maximum Chain')
ax.set_xlabel('Iteration')
ax.set_ylabel('Max Chain')
ax.set_ylim(bottom=0)
ax.set_yticks(range(0, int(max_chain.max())+2))  # 0,1,2,3,...,最大値+1まで
ax.grid(True)

# 4. 連鎖なし率（軸下限0）
ax = axes[1, 1]
ax.plot(x, no_chain_rate, label='No Chain Rate (%)', color='tab:red', marker='x', linestyle='dashed')
ax.set_title('No Chain Rate')
ax.set_xlabel('Iteration')
ax.set_ylabel('No Chain Rate (%)')
ax.set_ylim(bottom=0)  # y軸0スタート
ax.grid(True)

plt.suptitle('Learning Progress (Puyo AI)')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()