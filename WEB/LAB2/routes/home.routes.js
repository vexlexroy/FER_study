

var express = require('express');
var router = express.Router();
var http = require('http');
const data = require('../data/mydata');






router.get('/', function (req, res, next) {
   var recieved = '';
	http.get('http://localhost:3000/getCategories', function (response) {
		var rawdata = '';
		response.on('data', function (dat) {rawdata += dat;});
		
		response.on('end', function () {
			recieved = JSON.parse(rawdata);
			//console.log('recieving data: ', recieved);
			res.render('home', {categori:recieved, id:-1});
		});
	}).on('error', function (error) {
		  //console.log('Error recieving data: ', error);
		  res.status(500).send('Internal Server Error');
	    });

});





router.get('/getProducts/:id', function(req, res, next) {
  var id = parseInt(req.params.id.replace(':',''));
  http.get('http://localhost:3000/getCategories', function(response) {
    var rawdata = '';
    response.on('data', function(dat) {
      rawdata += dat;
    });

    response.on('end', function() {
      var received = JSON.parse(rawdata);
      //console.log('receiving data:', received);
		//console.log('receiving length:', received.length);
		//console.log('id:', id);
      if (id < received.length) {
        var category = received[id];
       //console.log('category:', category);

        if (category && category.products) {
			//console.log('products:', category.products);
          res.render('home', {categori: received, id: id, product: category.products});
        } else {
          res.status(404).send('Category or products not found');
        }
      } else {
        res.status(404).send('Category not found');
      }
    });
  }).on('error', function(error) {
    //console.log('Error receiving data:', error);
    res.status(500).send('Internal Server Error');
  });
});


router.get('/getCategories', function(req,res,next){
	const categori=data.categories;
	res.send(categori);
});



module.exports = router;