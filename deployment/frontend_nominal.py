import matplotlib.pyplot as plt
import seaborn as sns

def plot_nominal_features(df, target):
    balanced = df.groupby(by=target, axis=0).sample(1627, random_state=17) \
                 .sort_values(by=target, ascending=False)
    
    fig, axes = plt.subplots(9,2, layout="constrained", figsize=(8,18))

    sns.countplot(data=df, hue='Card_Category', x=target, ax=axes[0][0])
    sns.countplot(data=balanced, hue='Card_Category', x=target, ax=axes[0][1])

    sns.countplot(data=df.loc[df['Card_Category'] == 'Blue'],
        hue="Card_Category", x=target, ax=axes[1][0])
    sns.countplot(data=balanced.loc[balanced['Card_Category'] == 'Blue'],
        hue="Card_Category", x=target, ax=axes[1][1])

    sns.countplot(data=df.loc[df['Card_Category'] == 'Silver'],
        hue="Card_Category", x=target, ax=axes[2][0])
    sns.countplot(data=balanced.loc[balanced['Card_Category'] == 'Silver'],
        hue="Card_Category", x=target, ax=axes[2][1])

    sns.countplot(data=df.loc[df['Card_Category'] == 'Gold'], 
        hue='Card_Category', x=target, ax=axes[3][0])
    sns.countplot(data=balanced.loc[balanced['Card_Category'] == 'Gold'], 
        hue='Card_Category', x=target, ax=axes[3][1])

    sns.countplot(data=df.loc[df['Card_Category'] == 'Platinum'], 
        hue='Card_Category', x=target, ax=axes[4][0])
    sns.countplot(data=balanced.loc[balanced['Card_Category'] == 'Platinum'], 
        hue='Card_Category', x=target, ax=axes[4][1])

    sns.countplot(data=df, hue='Gender', x=target, ax=axes[5][0])
    sns.countplot(data=balanced, hue='Gender', x=target, ax=axes[5][1])

    sns.countplot(data=df, hue='Education_Level', x=target, ax=axes[6][0])
    sns.countplot(data=balanced, hue='Education_Level', x=target, ax=axes[6][1])

    sns.countplot(data=df, hue='Marital_Status', x=target, ax=axes[7][0])
    sns.countplot(data=balanced, hue='Marital_Status', x=target, ax=axes[7][1])

    sns.countplot(data=df, hue='Income_Category', x=target, ax=axes[8][0])
    sns.countplot(data=balanced, hue='Income_Category', x=target, ax=axes[8][1])

    for ax in axes.ravel():
        ax.legend(loc='upper left')

    return fig