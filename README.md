# Sports inventory basic


### Description
The repository contains the following APIs

### Database used : 
sqllite

### framework 
Django


## main/equipments/add

### method : 
POST

### description :
 to add item in inventory

### request body :

<table>
 <td>
 <tr>
 <th>Name</th>
 <th> Type</th>
<th>Is_madetory</th>
</tr>
</td>
 <tr>
 <th>name</th>
 <th>string</th>
 <th>true</th>
</tr>
 <tr>
 <th> quantity</th>
 <th>integer</th>
 <th>false</th>
</tr>
</table>

### Request example
```
{
    "name":"cricket ball"
    "quantity":10
}  
``` 
### Response 
```
{
    "status": true,
    "data": "record saved successfully"
}
```

## main/equipments/no_quantity
### method : 
POST

### description :
 render  the list of items which no zero inventory presence. 

### request body :
NA
### Request example
NA
### Response 
```
[
    {
        "name": "glouse",
        "quantity": 0
    },
    {
        "name": "bat",
        "quantity": 0
    }
]
```


## main/equipments/update


### method : 
POST

### description :
 to update item in inventory

### request body :

<table>
 <td>
 <tr>
 <th>Name</th>
 <th> Type</th>
<th>Is_madetory</th>
</tr>
</td>
 <tr>
 <th>name</th>
 <th>string</th>
 <th>true</th>
</tr>
 <tr>
 <th>quantity</th>
 <th>integer</th>
 <th>true</th>
</tr>
</table>

### Request example
```
{
    "name":"cricket ball"
    "quantity":10
}  
``` 
### Response 
```
{
    "status": true,
    "data": "record updated successfully"
}
```

# callscript.py

The python script contain following logic
1. call all apis as mention above(paramters are dynamic)
2. save the reposne in response.json file







