import express from 'express';
import { promisify } from 'util';
import redis from 'redis';


const listProducts = [
	{ Id: 1, name: "Suitcase 250", price: 50, stock: 4 },
	{ Id: 2, name: "Suitcase 450", price: 100, stock: 10 },
	{ Id: 3, name: "Suitcase 650", price: 350, stock: 2 },
	{ Id: 4, name: "Suitcase 1050", price: 550, stock: 5 }
];

const getItemById = id => {
	const item = listProducts.find(item => item.Id === id);
	return item;
}

const client = redis.createClient();
const asyncId = promisify(client.get).bind(client);

client.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

const reserveStockById = (itemId, stock) => {
	client.set(`item.${itemId}`, stock);
}

const getCurrentReservedStockById = async (itemId) => {
	const stock = await asyncId(`item.${itemId}`);
	return stock;
}

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
	res.json(listProducts);
});

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
	const itemId = Number(req.params.itemId);
	const item = getItemById(itemId);
	
	if (!item) {
		res.json({"status":"Product not found"});
		return;
	}
	let currentStock;
	try {
		currentStock = await getCurrentReservedStockById(itemId);
	} catch(err) {
		console.log(err);
	}
	let stock;
	if (currentStock !== null) {
		stock = currentStock;
	} else {
		stock = item.initialAvailableQuantity;
	}
	item.currentQuantity = stock;
	res.json(item);
});

app.get('/reserve_product/:itemId', async (req, res) => {
	const itemId = Number(req.params.itemId);
	const item = getItemById(itemId);
	if (!item) {
		res.json({"status":"Product not found"});
		return;
	}
	let currentStock;
        try {
                currentStock = await getCurrentReservedStockById(itemId);
        } catch(err) {
                console.log(err);
        }
	
	if (currentStock === null) {
		currentStock = item.initialAvailableQuantity;
	}
	if (currentStock <= 0) {
		res.json({"status":"Product not found"});
		return;
	}
	reserveStockById(itemId, Number(currentStock) - 1);
	res.json({"status":"Reservation confirmed","itemId":itemId});
});

app.listen(port, () => {
	console.log(`Server is running on http://localhost:${port}`);
});
