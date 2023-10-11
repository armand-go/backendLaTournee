# La Tournée — Backend home assignment

## Context

Order preparation is what makes an order become "real". It has both an impact on the customer experience and how they will receive their products as well as on our operational margin.

The way we manage glass containers is especially important: we want to minimize the amount of handling our agents perform while making sure
that transporting the products will be safe and practical to deliver.

As we want to provide a consistent experience for all our customers, we have defined preparation rules for how containers should be packed in crates.


## Preparation rules

We name "supplier crate" a crate that is stored in one of our warehouse as we received it from our suppliers. 
Those crates are not branded with La Tournée logo however using them can spare some handling and improve our cost-efficiency.


We have established the following rules:

- we want to use as _few_ crates as possible
- we do not want to transfer containers from a supplier crate to a custom crate if it is not needed: if an order product can be delivered with a *full* supplier crate, we use the supplier crate
- on top of supplier crates, we can use crates with 6-slots, 12-slots and, for small containers only, 20-slots
- there are some exceptions for products from the following brands:
	- "Orangina": bottles are too large to fit in a 20-slots crate however 2 bottles can fit in 1 slot (one bottle being upside-down): we never want to use the supplier crates for Orangina bottles as the crates sizing is very different from other crates so we will always move the units to 6 or 12-slots crates.
	- "La Tournée" containers are slightly too large to smoothly fit in 6 and 12-slots crates: we therefore can only put 5 containers in a 6-slots crate and 10 containers in a 12-slots crate.

**Examples:**
* Evian 1L bottles are supplied in 12-slots crate by our supplier. If a customer orders 18 units, we would deliver 1 supplier crate and 1 6-slots crate.
* if a customer orders 1 x "la-tournee-cafe-grains-espresso-370", 1 x "pajo-lait-amande-avoine-bio-75", 6 x "orangina-25", 12 x "coca-cola-cherry-33", we would deliver 1 6-slots crate to pack the coffee, almond milk and Orangina bottles (note that there would be one slot remaining free) and 1 20-slots crate for Coca-Cola cherry bottles.

## Tips

* to determine if a product is a small container (i.e. a container which fit in the 20 slots crate), we can look at the Deposit data in the store : if 20cts: its a small container, if 40cts its a big container.
* stucture of the store data:
  - sku
  - brand
  - packing: Number of units packed in a single crate by our suppliers; for beverages, it can be 6, 12, etc..
  - deposit: Deposit per unit expressed in euros: 20cts for small containers, 40cts for large containers.
  - preparation_in_crate: Flag to separate products that are delivered by the supplier in crates vs bags.

## Assignment

### Disclaimer

This assignment aims at being representative of the kind of problem/data we work with on a daily basis. 
That's why we ask that the function be written in python using fastapi framework.

We do not expect that you spend a lot of time on this. You should aim at 4h for the actual implementation.


### Instructions

We want to provide the crates dispatch in our production preparation app so that the agent knows which crates to pick before starting a preparation.

The objectives are:

* Using FastApi framework, Implement the following REST API endpoint : POST /orders/dispatch:
  * Input data: products list and quantity for an order (example below)

	```
	[
		{ID: "1", OrderID: "abc", SKU: "la-tournee-penne-ble-semi-complet-bio-350", UnitCount: 2},
		{ID: "2", OrderID: "abc", SKU: "la-tournee-pistaches-grillees-salees-200", UnitCount: 1}
	]
	```
  * Output data: json struct with count of quantity of all crates types (example below)
	```
	{
		Supplier: 0,
		Slot6: 1,
		Slot12: 0,
		Slot20: 0
	}
	```

	notes:
	- Supplier : number of supplier crates
	- Slot6:     number of crates with 6-slots
	- Slot12:    number of crates with 12-slots
	- Slot20:    number of crates with 20-slots


* Implement a controller function which compute the actual dispatch, called by the API endpoint function and returning the computed data. This controller will calculate the best quantity of crates for the given order, based on loaded store datas and all the constraints described above.
* you can use the load_data function below in your controller to load the store datas : the store datas simulates what you may found in a real database.

* Submit your implementation in a git repo.
* Include all details you would provide for a production ready contribution.

### What we will look at

* Structure of the project
* Input and output datas
* error cases
* How all rules and exceptions for the compute function are handled and tested
* Code structure, style, comments, etc..



Enjoy!