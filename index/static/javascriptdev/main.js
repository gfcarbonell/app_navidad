var Backbone 	   = require("backbone");
var $ 			     = require("jquery");
var Router       = require("./backbone/routers/router");
var BackboneCSRF = require("backbone.csrf");


$(() => {

    var router = new Router();
    Backbone.history.start({pushState: true});
    BackboneCSRF.initialize();
});
