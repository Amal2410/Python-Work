from json import load

f=open("C:\\Users\\Admin\\Desktop\\PythonJuneWorks\\jsonworks\\countries.json",encoding="UTF-8")

data=load(f)

def  fetch_country_by_name(name):

    return[c for c in data if c.get ("name")==name][0]

country_data=fetch_country_by_name("India")

# print(country_data)

# if "regionalBlocs" in country_data:

#     block_data=country_data.get("regionalBlocs")[0]

#     if "otherNames" in block_data:
        
#         print(block_data.get("otherNames"))

#     else:

#         print(block_data.get("name"))

def get_area(dic):

    if "area" in dic:

        return dic.get("area")
    
    else:

        return 0
    
biggest_country_name=max(data,key=get_area)

# print(biggest_country_name.get("name"))

# for c in data:

#     for l in c.get("languages"):

#         if l.get("name")=="English":

#             print(c.get("name"))



# largest region

all_regions={c.get("region")for c in data}

# print(all_regions)

region_summary={}

for c in data:

    region_name=c.get("region")

    if region_name in region_summary:

        region_summary[region_name]+=c.get("area",0)

    else:

        region_summary[region_name]=c.get("area",0)

# print(region_summary)

key_values=[(v,k)for k,v in region_summary.items()]

print(max(key_values))