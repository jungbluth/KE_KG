import pandas as pd


edges = pd.read_csv("./data/merged/merged_kg/IMGVR_merged_final_kg_edges.tsv", sep="\t")
dims = edges.shape
print(dims)


for i in range(0, dims[0]):
    subj1 = edges.iloc[i, 1]#df['subject']
    obj1 = edges.iloc[i, 3]# df['object']\

    if( i %1000 == 0):
        print(i)

    for j in range(i+1, dims[0]):
         if(subj1 == edges.iloc[j, 3] and obj1 == edges.iloc[j, 1]):
             print(subj1 + "\t" + obj1)
             print("undirected "+str(i)+"\t"+str(j))

