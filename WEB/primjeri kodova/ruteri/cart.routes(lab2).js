

var express = require('express');
var router = express.Router();
var http = require('http');
const data = require('../data/mydata');

router.get('/', function(req, res, next) {
	var recieved = '';
	http.get('http://localhost:3000/cart/getAll', function (response) {
		var rawdata = '';
		response.on('data', function (dat) {rawdata += dat;});
		
		response.on('end', function () {
			recieved = JSON.parse(rawdata);
			//console.log('recieving data: ', recieved);
			let productarr = req.session.selectedProducts;
			productarr = JSON.stringify(productarr);
			productarr=productarr.replace('[','');
			productarr=productarr.replace(']','');
			productarr=productarr.split(',');
			res.render('cart', {data:recieved, productCount:productarr, id: -2});
		});
	}).on('error', function (error) {
		  //console.log('Error recieving data: ', error);
		  res.status(500).send('Internal Server Error');
	    });
});

router.get('/getAll', function(req, res, next) {
	const datAll = data;
	res.send(datAll);	
});

router.get('/remove/:id', function(req, res, next) {
	//console.log("inside");
  const selectedProducts = req.session.selectedProducts;
  const id = req.params.id;
  if (id >= 0 && id < selectedProducts.length) {//provjera id
    selectedProducts[id] += -1;// oduzimanje
	console.log("products arr:" + selectedProducts);
    req.session.selectedProducts = selectedProducts;// pohrana
	console.log("updated products:" + req.session.selectedProducts);
  }
  const previousLink = req.headers.referer || '/';
  req.session.previousLink = previousLink;
  res.redirect(previousLink);// povratak
});

router.get('/add/:id', function(req, res, next) {
	//console.log("inside");
  const selectedProducts = req.session.selectedProducts;
  const id = req.params.id;
  if (id >= 0 && id < selectedProducts.length) {//provjera id
    selectedProducts[id] += 1;// dodavanje
	console.log("products arr:" + selectedProducts);
    req.session.selectedProducts = selectedProducts;// pohrana
	console.log("updated products:" + req.session.selectedProducts);
  }
  const previousLink = req.headers.referer || '/';
  req.session.previousLink = previousLink;
  res.redirect(previousLink);// povratak
});

module.exports = router;