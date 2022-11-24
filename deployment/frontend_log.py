import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def agg_original_skew(df):
    num_fea = [
        'Customer_Age', 'Dependent_count', 'Months_on_book', 
        'Total_Relationship_Count', 'Months_Inactive_12_mon', 
        'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
        'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 
        'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio'
    ]
    return df[num_fea].agg(['mean', 'std', 'skew'])

def agg_log_skew(df):
    return np.log10(
        df[[
            'Months_Inactive_12_mon', 'Credit_Limit', 'Avg_Open_To_Buy',
            'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Ct_Chng_Q4_Q1',
            'Avg_Utilization_Ratio'
           ]] + 10**-10
    ) \
      .agg(['mean', 'std', 'skew']
)

def agg_sqrt_skew(df):
    return np.sqrt(
        df[['Months_Inactive_12_mon', 'Total_Amt_Chng_Q4_Q1', 'Total_Ct_Chng_Q4_Q1',
            'Avg_Utilization_Ratio']]
    ) \
      .agg(['mean', 'std', 'skew'])

# KDE
def plot_original_log(df):
    fig, axes = plt.subplots(2,2, layout="constrained")
    sns.kdeplot(x=df['Credit_Limit'], ax=axes[0][0])

    sns.kdeplot(x=np.log10(df['Credit_Limit'] + 10**-10), ax=axes[0][1])

    sns.boxplot(x=df['Credit_Limit'], ax=axes[1][0])

    sns.boxplot(x=np.log10(df['Credit_Limit'] + 10**-10), ax=axes[1][1])

    return fig