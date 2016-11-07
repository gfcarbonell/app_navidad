var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");
var validation   = require('backbone-validation');
Backbone.$   = $;
require("backbone-relational");
_.extend(Backbone.Model.prototype, validation.mixin);


class Usuario extends Backbone.Model
{
	urlRoot() { return "/api/usuarios/"; }

	url() 
	{
	  var base = this.urlRoot();
	  if (this.isNew()) return base;
	  return base + (base.charAt(base.length - 1) == "/" ? '' : "/") + encodeURIComponent(this.get("id")) + "/";
	}
}

module.exports = Usuario;
