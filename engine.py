import pandas as pd
def get_classes(day):
    df = pd.read_excel("time_table.xlsx" , "Sheet1")
    df["THEORY"] = df["THEORY"].ffill()
    df.set_index("THEORY", inplace=True)

    day_data = df.loc["FRI"]
    classes = []
    for i,r in day_data.iterrows():
        # print(i,r)
        for j in r.items():
            # print(df())
            if "-" in j[1] and j[1] != "-":
                if j[1][0] == "L":
                    class_type = "LAB"
                    start_time = df[j[0]].iloc[1]
                    end_time = df[j[0]].iloc[2]
                else:
                    class_type = "THEORY"
                    start_time = j[0]
                    end_time = df[j[0]].iloc[0]

                class_data = {"class_type":class_type,"class_name": j[1],"start_time":start_time,"end_time":end_time}
                classes.append(class_data)
                classes.sort(key= lambda item: item["start_time"])
    # print(classes)

    merged_classes = []
    for i in classes:
        if merged_classes == []:
            merged_classes.append(i)
        else:
            if merged_classes[-1]["end_time"] == i["start_time"]:
                merged_classes[-1]["end_time"] = i["end_time"]
            else:
                merged_classes.append(i)

    return merged_classes