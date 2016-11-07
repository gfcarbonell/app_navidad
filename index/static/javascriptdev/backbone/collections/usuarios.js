var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");
Backbone.$ = $
var Usuario = require("../models/Usuario");


class Usuarios extends Backbone.Collection
{
	initialize()
	{
		this.model = Usuario; 
		this.url = "/api/usuarios";
	    this.fetch();
	}
}

module.exports = Usuarios;