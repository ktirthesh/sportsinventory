
import time,random,string,json
from datetime import date
from requests import post

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

main_url="http://127.0.0.1:8050/"


urls={
    "add":"main/equipments/add",
    "list_no_items":"main/equipments/no_quantity",
    "update":"main/equipments/update",
}   



while(True): 
    result_all={
        "create_response":"",
        "update_response":"",
        "item_no_quantity_response":""
    }
    # create api call
    create_and_update_data={
        "name":random_char(10),
        'quantity':random.randint(1, 100)

    }

    response_create=post(url=main_url+urls["add"],data=create_and_update_data)
    result_all['create_response']="response_create|{}|{}".format(create_and_update_data,response_create.json())
    
    #update api call
    create_and_update_data['quantity']=random.randint(1, 100)
    response_update=post(url=main_url+urls["update"],data=create_and_update_data)
    result_all['update_response']="response_update|{}|{}".format(create_and_update_data,response_update.json())

    # list_no_quantity api call
    response_no_quantity=post(url=main_url+urls["list_no_items"])
    result_all['item_no_quantity_response']="item_no_quantity|{}".format(response_no_quantity.json())


    # save in json file
    json_object = json.dumps(result_all, indent=4)

    with open("response.json", "a") as outfile:
        outfile.write(json_object)
    main_string="api called at {}".format(date.today())
    print(main_string)
    time.sleep(1) 

 
# Serializing json
 
# Writing to sample.json    
