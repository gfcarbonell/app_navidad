var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");
Backbone.$ = $
var DocumentoIdentificacion = require("../models/documento_identificacion");


class DocumentosIdentificaciones extends Backbone.Collection
{
	initialize()
	{
		this.model = DocumentoIdentificacion; 
		this.url = "/api/documentos_identificaciones";
	    this.fetch();
	}
}

module.exports = DocumentosIdentificaciones;