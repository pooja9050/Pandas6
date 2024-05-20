#196. Delete Duplicate Emails
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    min_id = person.groupby("email")["id"].transform("min")
    s = person[person["id"]!=min_id]
    person.drop(s.index, inplace=True)

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    min_id = person.groupby("email")["id"].transform("min")
    s = person[person["id"]!=min_id]
    person.drop(s.index, inplace=True)
    person.sort_values(by = ['id'], inplace=True)
    person.drop_duplicates(['email'], inplace=True)

#2082. The Number of Rich Customers
import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    n = store[store['amount']>500]['customer_id'].nunique()
    return pd.DataFrame({'rich_count': [n]})

import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    n = store[store['amount']>500]
    countrich = n['customer_id'].nunique()
    return pd.DataFrame([countrich],columns = ['rich_count'])
