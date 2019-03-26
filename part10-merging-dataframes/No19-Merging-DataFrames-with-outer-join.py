#Merging DataFrames with outer join
'''
This exercise picks up where the previous one left off. The DataFrames revenue, managers, and sales are pre-loaded into your namespace (and, of course, pandas is imported as pd). Moreover, the merged DataFrames revenue_and_sales and sales_and_managers have been pre-computed exactly as you did in the previous exercise.

The merged DataFrames contain enough information to construct a DataFrame with 5 rows with all known information correctly aligned and each branch listed only once. You will try to merge the merged DataFrames on all matching keys (which computes an inner join by default). You can compare the result to an outer join and also to an outer join with restricted subset of columns as keys.

Instructions
100 XP

Merge sales_and_managers with revenue_and_sales. Store the result as merge_default.
Print merge_default. This has been done for you.
Merge sales_and_managers with revenue_and_sales using how='outer'. Store the result as merge_outer.
Print merge_outer. This has been done for you.
Merge sales_and_managers with revenue_and_sales only on ['city','state'] using an outer join. Store the result as merge_outer_on and hit 'Submit Answer' to see what the merged DataFrames look like!
'''

#code
# Perform the first merge: merge_default
merge_default = pd.merge(sales_and_managers, revenue_and_sales)#default inner

# Print merge_default
print(merge_default)

# Perform the second merge: merge_outer
merge_outer = pd.merge( sales_and_managers ,revenue_and_sales, how='outer')

# Print merge_outer
print(merge_outer)#inner outer difference is in the row

# Perform the third merge: merge_outer_on
merge_outer_on = pd.merge(sales_and_managers , revenue_and_sales,on=['city','state'],how='outer')

# Print merge_outer_on
print(merge_outer_on)#on and outer difference is in the columns


'''original dataframe
In [2]: sales_and_managers.columns
Out[2]: Index(['city', 'state', 'units', 'branch', 'branch_id', 'manager'], dtype='object')

In [3]: revenue_and_sales.columns
Out[3]: Index(['city', 'branch_id', 'state', 'revenue', 'units'], dtype='object')



'''

'''result
        city state  units     branch  branch_id   manager  revenue
0  Mendocino    CA      1  Mendocino       47.0     Brett    200.0
1     Denver    CO      4     Denver       20.0      Joel     83.0
2     Austin    TX      2     Austin       10.0  Charlers    100.0


          city state  units       branch  branch_id   manager  revenue
0    Mendocino    CA      1    Mendocino       47.0     Brett    200.0
1       Denver    CO      4       Denver       20.0      Joel     83.0
2       Austin    TX      2       Austin       10.0  Charlers    100.0
3  Springfield    MO      5  Springfield       31.0     Sally      NaN
4  Springfield    IL      1          NaN        NaN       NaN      NaN
5  Springfield    IL      1          NaN       30.0       NaN      4.0
6  Springfield    MO      5          NaN        NaN       NaN      NaN


          city state  units_x       branch  branch_id_x   manager  branch_id_y  revenue  units_y
0    Mendocino    CA        1    Mendocino         47.0     Brett         47.0    200.0        1
1       Denver    CO        4       Denver         20.0      Joel         20.0     83.0        4
2       Austin    TX        2       Austin         10.0  Charlers         10.0    100.0        2
3  Springfield    MO        5  Springfield         31.0     Sally          NaN      NaN        5
4  Springfield    IL        1          NaN          NaN       NaN         30.0      4.0        1


'''