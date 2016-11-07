var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");
Backbone.$   = $;


class DocumentoIdentificacion extends Backbone.Model
{
	urlRoot() { return "/api/documentos_identificaciones/"; }

	url() 
	{
	  var base = this.urlRoot();
	  if (this.isNew()) return base;
	  return base + (base.charAt(base.length - 1) == "/" ? '' : "/") + encodeURIComponent(this.get("id")) + "/";
	}
}

module.exports = DocumentoIdentificacion;
