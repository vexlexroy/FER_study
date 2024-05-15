var express = require('express');
var router = express.Router();
const kategorija = ['Outdoors','Sports','Pizzas','Woks','Politics','Technology','Pets','BBQ'];


let { k } = require('./server.js');//sharing variable


	
router.get('/', function (req, res, next) {
	console.log(k);
	//const data=readData();
	res.render('home', {kat : kategorija, k});
});



module.exports = router;