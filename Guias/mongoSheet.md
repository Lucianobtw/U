
# Create new db:

``` use db_name ```

# Create a collection:

``` db.createCollection("users") ```

# Insert doc(s): 

``` db.users.insertOne({ nombre: "John", edad: 25, ciudad: "Santiago" }) ```
	
``` 
db.collection("users").insertMany([ 
		{campo1: "valor1", campo2: "valor2"},
		{campo1: "valor1", campo2: "valor2"},
		{campo1: "valor1", campo2: "valor2"}
]); 
```
	
# Update doc(s): 
	
``` 
db.users.updateOne( 
	{campo1: "valor1"}, {$set: {campo2: "nuevoValor"}}
);
```

``` 
db.users.updateMany( 
	{campo1: "valor1"}, {$set: {campo2: "nuevoValor"}}
);
```

# Delete doc(s):

``` db.users.deleteOne({campo1: "valor1"}); ```
	
``` db.users.deleteMany({campo1: "valor1"}); ```

# Buscar uno:

``` db.users.findOne({campo1: "valor1"}); ```
	
# Contar: 

``` db.users.countDocuments({campo1: "valor1"}); ```
