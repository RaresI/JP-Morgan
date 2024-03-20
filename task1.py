import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    df = pd.read_csv(file)
    print(df.head())

def exercise_1(df):
    column_names = df.columns.tolist()

    return column_names

def exercise_2(df, k):
    first_n_rows = df.head(n)

    return first_n_rows

def exercise_3(df, k):
    random_sample = df.sample(n=k)

    return random_sample

def exercise_4(df):
    uniq_tran_types = df['type'].unique()

    return uniq_tran_types

def exercise_5(df):
    top_dest = df['nameDest'].value_counts().head(10)

    return top_dest

def exercise_6(df):
    fraud_detec_rows = df[df['isFraud'] == 1]

    return fraud_detec_rows

def exercise_7(df):
    distinct_dest = df.groupby('nameOrig')['nameDest'].nunique()

    distinct_dest_sorted = distinct_dest.reset_index(name='num_distinct_dest').sort_values(by='num_distinct_dest', ascending=False)

    return distinct_dest_sorted

def visual_1(df):
    def transaction_counts(df):

        transaction_counts = df['type'].value_counts()
        return transaction_counts
    
    def transaction_counts_split_by_fraud(df):
        transaction_counts_split = df.groupby(['type', 'isFraud']).size().unstack(fill_value=0)
        return transaction_counts_split

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction Types')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Frequency')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction Types split by Fraud')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Frequency')
    axs[1].legend(title='Fraud Detected', loc='upper right')

    fig.suptitle('Transaction Types Analysis', fontsize=16)

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    description = "The first chart shows the distribution of transaction types, providing insights into the most common types of transactions. The second chart further analyzes transaction types by splitting them based on fraud detection, allowing for comparison between fraudulent and non-fraudulent transactions."

    return description



def visual_2(df):
    def query(df):

        cash_out_df = df[df['type'] == 'CASH_OUT']
        cash_out_df['origin_account_balance_delta'] = cash_out_df['oldbalanceOrg'] - cash_out_df['newbalanceOrig']
        cash_out_df['destination_account_balance_delta'] = cash_out_df['oldbalanceDest'] - cash_out_df['newbalanceDest']
        query_result = cash_out_df[['origin_account_balance_delta', 'destination_account_balance_delta']]        
        return query_result
    
    plot = query(df).plot.scatter(x='origin_account_balance_delta',y='destination_account_balance_delta')
    plot.set_title('Origin Account Balance Delta vs Destination Account Balance Delta for Cash Out Transactions')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    description = "This scatter plot visualizes the relationship between the origin account balance delta and the destination account balance delta for Cash Out transactions. It helps to understand the pattern of money movement between accounts during Cash Out transactions."

    return description




def exercise_custom(df):
    fraudulent_tran = df[df['isFraud'] == 1].group.by('type')['amount'].sum()

    return fraudulent_tran
    
def visual_custom(df):
    def query(df):
        # Group the DataFrame by transaction type and sum the 'amount' for fraudulent transactions
        fraudulent_tran = df[df['isFraud'] == 1].groupby('type')['amount'].sum()
        
        # Return the total amount of fraudulent transactions per transaction type
        return fraudulent_tran

    # Call the query function to get the data
    fraudulent_tran = query(df)

    fraudulent_tran.plot(kind='bar', figsize=(8,6))
    plt.title('Total Amount of Fraudulent Transactions per Transaction Type')
    plt.xlabel('Transaction Type')
    plt.ylabel('Total Amount')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    description = "This bar chart shows the total amount of fraudulent transactions for each transaction type. It helps to identify which transaction types are associated with the highest fraudulent activities."

    return description
    


# Test exercises here
file = "transactions.csv"
df = pd.read_csv(file)
exercise_0(file)

column_names = exercise_1(df)
print("Column names: ", column_names)

n = 5
first_n_rows = exercise_2(df, n)
print(f"First {n} rows:")
print(first_n_rows)

random_sample = exercise_3(df, n)
print(f"Random sample of {n} rows:")
print(random_sample)

unique_types = exercise_4(df)
print("Unique transaction types:")
print(unique_types)

top_dest = exercise_5(df)
print("Top 10 transaction destinations with frequencies:")
print(top_dest)

fraud_detected_rows = exercise_6(df)
print("Rows with fraud detected:")
print(fraud_detected_rows)

distinct_destinations_per_source_df = exercise_7(df)
print("DataFrame containing the number of distinct destinations each source has interacted with (sorted in descending order):")
print(distinct_destinations_per_source_df)

description = visual_1(df)
print(description)
plt.show()

description = visual_2(df)
print(description)
plt.show()

description = visual_custom(df)
print(description)
plt.show()