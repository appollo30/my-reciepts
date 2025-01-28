import os
import json

def to_json(result):
    records = list()
    for (bbox, word) in result:
        record = dict()
        record["text"] = word[0]
        record["confidence"] = word[1]
        record["coords"] = {
            "top_left" : bbox[0],
            "top_right" : bbox[1],
            "bottom_left" : bbox[2],
            "bottom_right" : bbox[3]
        }
        records.append(record)
    return records

def write(result,file_name : str):
    with open(os.path.join(".","data","output",file_name),"w",encoding="utf-8") as f:
        json.dump(result,f,ensure_ascii=True,indent=4) 